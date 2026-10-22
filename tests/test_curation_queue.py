import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from curation_queue import Queue, format_report


def candidate(i, **kwargs):
    return dict(id=f'p{i}', paper_url=f'https://arxiv.org/abs/2610.{i:05d}', title=f'Robot safety {i}', source_version='v1', **kwargs)


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.q = Queue(Path(self.tmp.name) / 'queue.json')
        self.q.initialize()

    def test_twenty_including_holds_and_rejections_then_next_run(self):
        with self.q.guard('new', 'first'):
            self.q.ingest([candidate(i) for i in range(21)], [])
            for i in range(20):
                e = self.q.claim()
                self.assertIsNotNone(e)
                self.q.resolve(e['id'], 'held' if i == 0 else 'rejected')
            self.assertIsNone(self.q.claim())
            self.assertEqual(self.q.report()['reviewed'], 20)
        self.assertEqual(self.q.report()['remaining']['new'], {'pending': 1, 'held': 1, 'total': 2})
        with self.q.guard('new', 'second'):
            self.assertEqual(self.q.claim()['id'], 'arxiv:2610.00020')
            self.assertIsNone(self.q.claim())

    def test_maintenance_limit_and_lane_outcomes(self):
        catalog = [dict(candidate(i)) for i in range(21)]
        with self.q.guard('maintenance', 'run'):
            self.q.ingest([candidate(i, signal='revision') for i in range(21)], catalog)
            for i in range(20):
                entry = self.q.claim()
                with self.assertRaises(ValueError):
                    self.q.resolve(entry['id'], 'added')
                self.q.resolve(entry['id'], 'unchanged')
            self.assertIsNone(self.q.claim())
        self.assertEqual(self.q.report()['remaining']['maintenance']['pending'], 1)

    def test_dedupe_retitle_and_known_records_require_signals(self):
        with self.q.guard('new', 'run'):
            c = candidate(1)
            self.q.ingest([c, c, dict(c, id='alias', paper_url='https://example.org/preprint', title='ROBOT: safety 1')], [])
            self.assertEqual(len(self.q.load()['entries']), 1)
            self.q.ingest([dict(c, title='Renamed robot safety')], [])
            self.assertEqual(len(self.q.load()['entries']), 1)
            known = candidate(2)
            self.q.ingest([known], [known])
            self.assertEqual(len(self.q.load()['entries']), 1)
            self.q.ingest([dict(known, signal='revision')], [known])
            self.assertEqual(self.q.report()['remaining']['maintenance']['pending'], 1)

    def test_held_only_reopens_on_changed_evidence(self):
        with self.q.guard('new', 'one'):
            self.q.ingest([candidate(1)], [])
            e = self.q.claim()
            self.q.resolve(e['id'], 'held', 'source unavailable')
        with self.q.guard('new', 'two'):
            self.q.ingest([candidate(1)], [])
            self.assertIsNone(self.q.claim())
            self.q.ingest([dict(candidate(1), evidence_key='source-restored')], [])
            self.assertIsNotNone(self.q.claim())

    def test_missing_version_is_not_new_evidence(self):
        with self.q.guard('new', 'first'):
            self.q.ingest([candidate(1)], [])
            e = self.q.claim()
            self.q.resolve(e['id'], 'held')
        with self.q.guard('new', 'next'):
            c = candidate(1)
            c.pop('source_version')
            self.q.ingest([c], [])
            self.assertIsNone(self.q.claim())
            self.assertEqual(self.q.load()['entries'][0]['source_version'], 'v1')

    def test_checkpoints_transactional_and_failure_preserves_boundary(self):
        with self.q.guard('new', 'one'):
            self.q.ingest([], [], [{'source': 'ro', 'cursor': 'first', 'success': True}])
            self.q.ingest([], [], [{'source': 'ro', 'cursor': 'second', 'success': False}])
            self.assertEqual(self.q.load()['sources']['ro']['cursor'], 'first')
            with self.assertRaises(ValueError):
                self.q.ingest([{'id': 'bad'}], [], [{'source': 'ro', 'cursor': 'third', 'success': True}])
            self.assertEqual(self.q.load()['sources']['ro']['cursor'], 'first')

    def test_failure_no_change_and_unknown_reports(self):
        with self.assertRaises(RuntimeError):
            with self.q.guard('new', 'failed'):
                self.q.ingest([candidate(1)], [])
                self.q.claim()
                raise RuntimeError('publication failed')
        report = self.q.report()
        self.assertEqual(report['run_status'], 'failed')
        self.assertEqual(report['remaining']['total'], 1)
        self.assertIn('合計 1件', format_report(report))
        with self.q.guard('maintenance', 'empty'):
            self.assertIsNone(self.q.claim())
        self.assertEqual(self.q.report()['reviewed'], 0)
        self.q.path.write_text('{broken')
        self.assertIsNone(self.q.report()['remaining'])
        self.assertIn('不明', format_report(self.q.report()))
        with self.assertRaises(ValueError):
            self.q.initialize()

    def test_guard_prevents_concurrent_work_and_unowned_writes(self):
        other = Queue(self.q.path, 'other')
        with self.assertRaises(RuntimeError):
            other.ingest([], [])
        with self.q.guard('new', 'first'):
            with self.assertRaises(BlockingIOError):
                with other.guard('maintenance', 'second'):
                    self.fail('must not acquire')
            with self.assertRaises(RuntimeError):
                other.ingest([], [])
        self.assertIsNone(self.q.load()['active_run'])

    def test_nonobject_queue_is_unknown_and_not_reset(self):
        self.q.path.write_text('[]')
        self.assertIsNone(self.q.report()['remaining'])
        with self.assertRaises(ValueError):
            self.q.initialize()
        self.assertEqual(self.q.path.read_text(), '[]')

    def test_persistent_guard_cli(self):
        script = Path(__file__).resolve().parents[1] / 'scripts/curation_queue.py'
        proc = subprocess.Popen([sys.executable, str(script), '--state', str(self.q.path), '--run-id', 'cli', 'guard', '--lane', 'new'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            self.assertIn('LOCKED', proc.stdout.readline())
            Queue(self.q.path, 'cli').ingest([candidate(1)], [])
            self.assertIsNotNone(Queue(self.q.path, 'cli').claim())
            out, err = proc.communicate('failed\n', timeout=10)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn('合計 1件', out)
            self.assertIsNone(self.q.load()['active_run'])
        finally:
            if proc.poll() is None:
                proc.kill()
                proc.communicate()


if __name__ == '__main__':
    unittest.main()
