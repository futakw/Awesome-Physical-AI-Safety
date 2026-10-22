import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import validate_catalog as v
import build_visualizations as charts


class MinimalMetadataTests(unittest.TestCase):
    def setUp(self):
        self.tax = {n: json.loads((v.TAXONOMY_DIR / (n + '.json')).read_text()) for n in ['defense', 'evaluation', 'benchmark', 'threat_model']}
        self.papers = json.loads(v.DATA_PATH.read_text())

    def test_legacy_and_minimal_defense(self):
        for p in self.papers:
            errors = []
            v.validate_extensions(errors, p['id'], p, self.tax)
            self.assertFalse(errors)
        paper = copy.deepcopy(next(p for p in self.papers if p.get('defense')))
        paper['defense'] = {k: paper['defense'][k] for k in ['mechanism', 'defends_against', 'curation_status']}
        paper.pop('evaluation', None)
        paper.pop('benchmark', None)
        errors = []
        v.validate_extensions(errors, 'minimal', paper, self.tax)
        self.assertEqual(errors, [])
        # Current chart must have exactly the same cells without legacy-only fields.
        original = next(p for p in self.papers if p['id'] == paper['id'])
        baseline = charts.outputs(self.papers)
        modified = charts.outputs([paper if p["id"] == paper["id"] else p for p in self.papers])
        self.assertEqual(baseline, modified)

    def test_invalid_minimal_and_optional_values(self):
        for d in [None, {}, {'mechanism': [], 'defends_against': []}, {'mechanism': ['unknown'], 'defends_against': [], 'curation_status': 'paper-verified'}, {'mechanism': [], 'defends_against': [], 'curation_status': 'paper-verified', 'position': ['unknown']}]:
            errors = []
            v.validate_extensions(errors, 'bad', {'defense': d}, self.tax)
            self.assertTrue(errors)

    def test_only_live_figures_generated(self):
        self.assertEqual({p.name for p in charts.outputs(self.papers)}, {'submission-growth.svg', 'field-timeline.svg', 'threat-heatmap.svg', 'threat-risk-heatmap.svg', 'defense-heatmap.svg'})
        template = (v.ROOT / 'templates/explorer.html').read_text()
        for name in ['renderEvaluation', 'renderModelEnvironment', 'renderBenchmarkV2', 'renderExtensionMap']:
            self.assertNotIn('function ' + name + '(', template)


if __name__ == '__main__':
    unittest.main()
