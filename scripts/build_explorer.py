#!/usr/bin/env python3
"""Build the self-contained interactive GitHub Pages explorer."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
TEMPLATE_PATH = ROOT / "docs" / "explorer_template.html"
OUTPUT_PATH = ROOT / "docs" / "index.html"


def main() -> int:
    papers = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    payload = json.dumps(papers, ensure_ascii=False, separators=(",", ":"))
    if "__PAPERS_JSON__" not in template:
        raise SystemExit("explorer template is missing __PAPERS_JSON__")
    output = template.replace("__PAPERS_JSON__", payload)
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(f"Generated docs/index.html with {len(papers)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
