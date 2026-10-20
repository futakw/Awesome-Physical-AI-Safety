"""Regression checks for the controlled secondary-tag vocabulary."""

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
        for paper in json.loads(catalog.DATA_PATH.read_text(encoding="utf-8")):
            catalog.validate_tags(errors, paper["id"], paper["tags"], allowed)
        self.assertEqual(errors, [])

    def test_invalid_record_tags_are_rejected(self):
        cases = [None, "known", [], [1], ["unknown"], ["known", "known"]]
        for tags in cases:
            with self.subTest(tags=tags):
                errors = []
                catalog.validate_tags(errors, "example", tags, {"known"})
                self.assertTrue(errors)

    def test_registered_tags_are_accepted(self):
        errors = []
        catalog.validate_tags(errors, "example", ["known"], {"known"})
        self.assertEqual(errors, [])

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
