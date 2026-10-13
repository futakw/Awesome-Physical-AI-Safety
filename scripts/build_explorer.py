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
    import sys

    sys.path.insert(0, str(ROOT / "scripts"))
    import labels_ja as L

    papers = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    labels_payload = {
        "sections": L.SECTIONS_JA,
        "risks": L.RISK_LABELS_JA,
        "lifecycle": L.LIFECYCLE_JA,
        "surface": L.SURFACE_JA,
        "mechanism": L.MECHANISM_JA,
        "target": L.TARGET_JA,
        "consequence": L.CONSEQUENCE_JA,
        "kind": L.KIND_JA,
    }

    for placeholder, payload in (
        ("__PAPERS_JSON__", papers),
        ("__LABELS_JA_JSON__", labels_payload),
    ):
        if placeholder not in template:
            raise SystemExit(f"explorer template is missing {placeholder}")
        template = template.replace(
            placeholder, json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        )

    OUTPUT_PATH.write_text(template, encoding="utf-8")
    print(f"Generated docs/index.html with {len(papers)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
