#!/usr/bin/env python3
"""Bounded curation queue. State is supplied externally, never in the catalog."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import re
import signal
import sys
import tempfile
import unicodedata
from urllib.parse import urlparse

LIMIT = 20
SIGNALS = {'revision', 'venue', 'code', 'correction', 'invalid-metadata'}
STATES = {'pending', 'held', 'done', 'rejected'}


def now():
    return datetime.now(timezone.utc).isoformat()


def title_key(title):
    return re.sub(r'[^\w]', '', unicodedata.normalize('NFKC', title).casefold())


def identity(url, fallback):
    m = re.search(r'arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?', url)
    if m:
        return 'arxiv:' + m[1]
    m = re.search(r'openreview\.net/(?:forum|pdf)\?id=([^&]+)', url)
    if m:
        return 'openreview:' + m[1]
    if url.startswith('https://doi.org/'):
        return 'doi:' + url.split('doi.org/', 1)[1].casefold()
    return fallback


class Queue:
    def __init__(self, path, run_id=None):
        self.path = Path(path)
        self.run_id = run_id

    def load(self):
        data = json.loads(self.path.read_text())
        if not isinstance(data, dict) or data.get('version') != 1 or not isinstance(data.get('entries'), list) or not isinstance(data.get('sources'), dict) or not isinstance(data.get('runs'), dict):
            raise ValueError('Invalid queue schema')
        for run in data['runs'].values():
            if not isinstance(run, dict) or not isinstance(run.get('claimed'), list) or not isinstance(run.get('outcomes'), dict):
                raise ValueError('Invalid run summary')
        ids = []
        for e in data['entries']:
            if not isinstance(e, dict) or not all(k in e for k in ['id', 'paper_url', 'title', 'first_seen', 'lane', 'status', 'reason', 'source_version', 'evidence_key']):
                raise ValueError('Incomplete queue entry')
            if e['lane'] not in {'new', 'maintenance'} or e['status'] not in STATES:
                raise ValueError('Invalid queue entry state')
            ids.append(e['id'])
        if len(ids) != len(set(ids)):
            raise ValueError('Duplicate queue identity')
        return data

    def save(self, data):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(prefix='.queue-', dir=self.path.parent)
        try:
            os.fchmod(fd, 0o600)
            with os.fdopen(fd, 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write('\n')
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, self.path)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)

    @contextmanager
    def transaction(self, guarded=True):
        with self.path.with_suffix('.mutex').open('a') as mutex:
            fcntl.flock(mutex, fcntl.LOCK_EX)
            data = self.load()
            if guarded:
                if data.get('active_run') != self.run_id or not self.run_id:
                    raise RuntimeError('Not the active run owner')
                with self.path.with_suffix('.run.lock').open('a') as probe:
                    try:
                        fcntl.flock(probe, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    except BlockingIOError:
                        pass
                    else:
                        raise RuntimeError('Guard process is not holding the run lock')
            yield data
            self.save(data)

    def initialize(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.with_suffix('.mutex').open('a') as mutex:
            fcntl.flock(mutex, fcntl.LOCK_EX)
            if self.path.exists():
                self.load()  # Never reset an existing or unreadable queue.
                return
            self.save({'version': 1, 'entries': [], 'sources': {}, 'runs': {}, 'active_run': None})

    @contextmanager
    def guard(self, lane, run_id):
        if lane not in {'new', 'maintenance'} or not run_id:
            raise ValueError('A lane and nonempty fresh run ID are required')
        self.run_id = run_id
        with self.path.with_suffix('.run.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.transaction(guarded=False) as data:
                if run_id in data['runs']:
                    raise ValueError('Use a fresh run ID')
                old = data.get('active_run')
                if old:
                    data['runs'][old]['status'] = 'interrupted'
                    data['runs'][old]['remaining'] = self.counts(data)
                data['active_run'] = run_id
                data['runs'][run_id] = {'lane': lane, 'started': now(), 'status': 'running', 'claimed': [], 'outcomes': {}}
            status = 'failed'
            try:
                yield self
                status = 'success'
            finally:
                with self.transaction(guarded=False) as data:
                    run = data['runs'][run_id]
                    run.update(status=status, finished=now(), remaining=self.counts(data))
                    data['active_run'] = None
                    # Preserve the current run and the latest 49 completed reports.
                    for key in list(data['runs'])[:-50]:
                        del data['runs'][key]

    def ingest(self, candidates, catalog, checkpoints=()):
        index = {}
        for r in catalog:
            index[identity(r['paper_url'], r['id'])] = r
            index['title:' + title_key(r['title'])] = r
        with self.transaction() as data:
            for entry in data['entries']:
                if entry['lane'] == 'new' and (entry['id'] in index or 'title:' + title_key(entry['title']) in index):
                    entry.update(status='done', reason='Already catalogued; no new-paper review required')
            for c in candidates:
                if not c.get('id') or not c.get('title') or urlparse(c.get('paper_url', '')).scheme != 'https':
                    raise ValueError('Candidate needs ID, title and HTTPS source')
                cid = identity(c['paper_url'], c['id'])
                match = index.get(cid) or index.get('title:' + title_key(c['title']))
                if match and c.get('signal') not in SIGNALS:
                    continue  # Unknown venue or missing code is not an update signal.
                lane = 'maintenance' if match else 'new'
                if match:
                    cid = identity(match['paper_url'], match['id'])
                entry = next((e for e in data['entries'] if e['id'] == cid or title_key(e['title']) == title_key(c['title'])), None)
                version = c.get('source_version')
                evidence = c.get('evidence_key', str(c.get('signal')) + ':' + str(version) if match else version)
                if entry:
                    changed = ((version is not None and version != entry['source_version']) or
                               (evidence is not None and evidence != entry['evidence_key']))
                    # A terminal decision or hold is reconsidered only with evidence change.
                    if changed:
                        entry.update(status='pending', reason=c.get('reason', ''))
                        if version is not None:
                            entry['source_version'] = version
                        if evidence is not None:
                            entry['evidence_key'] = evidence
                    entry.update(title=c['title'], paper_url=c['paper_url'], lane=lane)
                else:
                    data['entries'].append({'id': cid, 'paper_url': c['paper_url'], 'title': c['title'], 'first_seen': now(), 'lane': lane, 'status': 'pending', 'reason': c.get('reason', ''), 'source_version': version, 'evidence_key': evidence})
            for cp in checkpoints:
                if cp.get('success') is True:
                    data['sources'][cp['source']] = {'cursor': cp['cursor'], 'checked_at': now()}

    def claim(self, cid=None):
        with self.transaction() as data:
            run = data['runs'][self.run_id]
            if len(run['claimed']) >= LIMIT:
                return None
            eligible = sorted((e for e in data['entries'] if e['lane'] == run['lane'] and e['status'] == 'pending' and e['id'] not in run['claimed']), key=lambda e: (e['first_seen'], e['id']))
            if cid is not None:
                eligible = [e for e in eligible if e['id'] == cid]
            if not eligible:
                return None
            entry = eligible[0]
            run['claimed'].append(entry['id'])  # Reserve before any primary-source reading.
            return dict(entry)

    def resolve(self, cid, outcome, reason=''):
        if outcome not in {'added', 'updated', 'unchanged', 'held', 'rejected'}:
            raise ValueError('Invalid review outcome')
        with self.transaction() as data:
            run = data['runs'][self.run_id]
            if cid not in run['claimed'] or cid in run['outcomes']:
                raise ValueError('Outcome requires an unresolved claim in this run')
            if (run['lane'] == 'new' and outcome == 'updated') or (run['lane'] == 'maintenance' and outcome == 'added'):
                raise ValueError('Outcome crosses lane responsibilities')
            entry = next(e for e in data['entries'] if e['id'] == cid)
            entry.update(status={'held': 'held', 'rejected': 'rejected'}.get(outcome, 'done'), reason=reason)
            run['outcomes'][cid] = outcome

    @staticmethod
    def counts(data):
        result = {lane: {'pending': 0, 'held': 0, 'total': 0} for lane in ['new', 'maintenance']}
        for e in data['entries']:
            if e['status'] in {'pending', 'held'}:
                result[e['lane']][e['status']] += 1
                result[e['lane']]['total'] += 1
        result['total'] = sum(result[lane]['total'] for lane in ['new', 'maintenance'])
        return result

    def report(self):
        try:
            data = self.load()
            run = data['runs'].get(self.run_id, {})
            return {'reviewed': len(run.get('claimed', [])), 'outcomes': {k: list(run.get('outcomes', {}).values()).count(k) for k in ['added', 'updated', 'held', 'rejected']}, 'remaining': self.counts(data), 'run_status': run.get('status', 'not-started')}
        except (OSError, ValueError, KeyError, TypeError):
            return {'remaining': None, 'error': 'unknown: queue read failed'}


def format_report(report):
    if report['remaining'] is None:
        return '今回：確認 不明/20件\n残り：不明・読み取り失敗（0件ではありません）'
    o, c = report['outcomes'], report['remaining']
    lines = [f"今回：確認 {report['reviewed']}/20件、追加 {o['added']}件、更新 {o['updated']}件、保留 {o['held']}件、除外 {o['rejected']}件", '残り：']
    for lane, label in [('new', '新規候補'), ('maintenance', '既収録保守')]:
        n = c[lane]
        lines.append(f"- {label} {n['total']}件（未処理 {n['pending']}件・保留 {n['held']}件）")
    lines.append(f"- 合計 {c['total']}件")
    return '\n'.join(lines)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state', required=True, type=Path)
    p.add_argument('--run-id')
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('init')
    sub.add_parser('report').add_argument('--json', action='store_true')
    sub.add_parser('guard').add_argument('--lane', choices=['new', 'maintenance'], required=True)
    ingest = sub.add_parser('ingest')
    ingest.add_argument('--batch', type=Path, required=True)
    ingest.add_argument('--catalog', type=Path, required=True)
    sub.add_parser('claim').add_argument('--id')
    resolve = sub.add_parser('resolve')
    resolve.add_argument('--id', required=True)
    resolve.add_argument('--outcome', required=True)
    resolve.add_argument('--reason', default='')
    a = p.parse_args(argv)
    q = Queue(a.state, a.run_id)
    try:
        if a.command == 'init':
            q.initialize()
        elif a.command == 'report':
            r = q.report()
            print(json.dumps(r, ensure_ascii=False) if a.json else format_report(r))
            return int(r['remaining'] is None)
        elif a.command == 'guard':
            signal.signal(signal.SIGTERM, lambda *_: (_ for _ in ()).throw(InterruptedError('Guard terminated')))
            with q.guard(a.lane, a.run_id):
                print('LOCKED: keep this tool session alive through publication; send success or failed to finish.', flush=True)
                ending = sys.stdin.readline().strip()
                if ending != 'success':
                    raise RuntimeError('Run interrupted or failed')
            print(format_report(q.report()), flush=True)
        elif a.command == 'ingest':
            batch = json.loads(a.batch.read_text())
            q.ingest(batch.get('candidates', []), json.loads(a.catalog.read_text()), batch.get('checkpoints', []))
        elif a.command == 'claim':
            print(json.dumps(q.claim(a.id), ensure_ascii=False))
        elif a.command == 'resolve':
            q.resolve(a.id, a.outcome, a.reason)
        return 0
    except (OSError, ValueError, KeyError, TypeError, RuntimeError, KeyboardInterrupt) as exc:
        print(str(exc), file=sys.stderr)
        print(format_report(q.report()))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
