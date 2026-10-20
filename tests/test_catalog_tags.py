"""Regression checks for the controlled secondary-tag vocabulary."""

import csv
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_catalog as catalog


class ControlledTagsTests(unittest.TestCase):
    def test_existing_catalog_tags_are_registered(self):
        errors = []
        allowed = catalog.load_tag_vocabulary(errors)
        papers = json.loads(catalog.DATA_PATH.read_text(encoding="utf-8"))
        for paper in papers:
            catalog.validate_tags(errors, paper["id"], paper["tags"], allowed)
        self.assertEqual(errors, [])
        self.assertEqual(allowed, {tag for paper in papers for tag in paper["tags"]})

    def test_invalid_record_tags_are_rejected(self):
        cases = [None, "known", [1], ["unknown"], ["known", "known"]]
        for tags in cases:
            with self.subTest(tags=tags):
                errors = []
                catalog.validate_tags(errors, "example", tags, {"known"})
                self.assertTrue(errors)

    def test_registered_tags_are_accepted(self):
        errors = []
        catalog.validate_tags(errors, "example", ["known"], {"known"})
        self.assertEqual(errors, [])

    def test_empty_tags_are_allowed(self):
        errors = []
        catalog.validate_tags(errors, "example", [], {"known"})
        self.assertEqual(errors, [])

    def test_related_surveys_require_unique_https_urls(self):
        for refs in (None, [], [None], ["http://example.org/survey"], ["https://example.org", "https://example.org"], "https://example.org"):
            with self.subTest(refs=refs):
                errors = []
                catalog.validate_related_surveys(errors, "example", refs)
                self.assertTrue(errors)
        errors = []
        catalog.validate_related_surveys(errors, "example", ["https://arxiv.org/abs/2608.16843"])
        self.assertEqual(errors, [])

    def test_migration_examples_and_audit_coverage(self):
        papers = json.loads(catalog.DATA_PATH.read_text(encoding="utf-8"))
        by_id = {paper["id"]: paper for paper in papers}
        self.assertIn("false-candidate-persistence", by_id["arxiv-2610-23293"]["tags"])
        self.assertNotIn("black-box", by_id["saber-2026-vla"]["tags"])
        self.assertEqual(by_id["saber-2026-vla"]["evaluation"]["access"], ["black-box"])
        self.assertEqual(by_id["zhang-2025-robustvla-rl-post-training"]["related_surveys"], ["https://arxiv.org/abs/2608.16843"])
        operational = {"abstract-verified", "candidate-audit-follow-up", "full-text-reviewed", "priority-literature-review-2026-10", "supervisor-audit", "survey-2608.16843", "survey-reference"}
        self.assertFalse(operational & {tag for paper in papers for tag in paper["tags"]})
        audit_path = catalog.ROOT / "audit" / "secondary_tag_cleanup_2026-10.csv"
        with audit_path.open(encoding="utf-8", newline="") as source:
            rows = list(csv.DictReader(source))
        self.assertEqual(len(rows), 1473)
        self.assertTrue(all(row["paper_id"] in by_id for row in rows))
        self.assertTrue(all(row["action"] in {"retain", "remove", "migrate"} for row in rows))

    def test_invalid_registries_fail_closed(self):
        cases = [None, {}, [], [1], [""], [" padded"], ["known", "known"]]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            for values in cases:
                with self.subTest(values=values):
                    (path / "tags.json").write_text(json.dumps(values), encoding="utf-8")
                    errors = []
                    with patch.object(catalog, "TAXONOMY_DIR", path):
                        catalog.load_tag_vocabulary(errors)
                    self.assertTrue(errors)
            (path / "tags.json").write_text("not JSON", encoding="utf-8")
            errors = []
            with patch.object(catalog, "TAXONOMY_DIR", path):
                self.assertEqual(catalog.load_tag_vocabulary(errors), set())
            self.assertTrue(errors)
            (path / "tags.json").unlink()
            errors = []
            with patch.object(catalog, "TAXONOMY_DIR", path):
                self.assertEqual(catalog.load_tag_vocabulary(errors), set())
            self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
