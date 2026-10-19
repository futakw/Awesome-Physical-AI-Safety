#!/usr/bin/env python3
"""Compare generated Explorer and static Mechanism × Surface populations/cells.

Requires Node.js to execute the Explorer's own counting functions, without a DOM.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from build_visualizations import MECHANISM_GROUPS, SURFACE_GROUPS, render_heatmap, threat_values
from landscape_population import concrete_threat_papers

ROOT = Path(__file__).resolve().parents[1]


def extract(source: str, pattern: str) -> str:
    match = re.search(pattern, source, re.MULTILINE | re.DOTALL)
    if not match:
        raise AssertionError(f"Explorer declaration not found: {pattern}")
    return match.group()


def explorer_code(source: str) -> str:
    declarations = [extract(source, rf"^const {name} = .*?^\];")
                    for name in ("MECHANISM_GROUPS", "SURFACE_GROUPS")]
    declarations += [extract(source, r"^const CONCRETE_THREAT_KINDS = [^\n]+"),
                     extract(source, r"^const COVERAGE_FIELDS = [^\n]+"),
                     extract(source, r"^const threatValues = .*?^};")]
    declarations += [extract(source, rf"^function {name}\(.*?^}}")
                     for name in ("viewBasePapers", "mechanismSurfaceCells")]
    return "\n".join(declarations)


def expected(papers: list[dict]) -> dict:
    concrete = concrete_threat_papers(papers)
    counts = [sum(bool(set(threat_values(p, "mechanism")) & set(mg["values"]))
                  and bool(set(threat_values(p, "surface")) & set(sg["values"]))
                  for p in concrete)
              for mg in MECHANISM_GROUPS for sg in SURFACE_GROUPS]
    return {"ids": [p["id"] for p in concrete], "counts": counts}


def svg_counts(svg: str) -> list[int]:
    root = ET.fromstring(svg)
    return [int(node.text or "0") for node in root.iter("{http://www.w3.org/2000/svg}text")
            if node.get("font-size") == "12" and node.get("font-weight") == "600"]


def fixture_papers() -> list[dict]:
    # Multiple matching leaves in one family must count once. Broad coverage
    # must stay excluded here, while still participating in risk views.
    papers = [
        {"id": "concrete", "threat_model": {"kind": "adversarial",
         "mechanism": ["backdoor", "data-poisoning"],
         "surface": ["model-supply-chain", "middleware-network", "visual-perception"]}},
        {"id": "empty-technique", "threat_model": {"kind": "system-failure",
         "mechanism": [], "surface": ["visual-perception"]}},
        *[{"id": kind, "threat_model": {"kind": kind, "coverage": {
          "mechanisms": ["backdoor"], "surfaces": ["model-supply-chain"]}}}
          for kind in ("survey", "evaluation")],
    ]
    for paper in papers:
        paper.update(venue="arXiv", year=2026, title=paper["id"])
    return papers


def main() -> None:
    node = shutil.which("node")
    if not node:
        raise SystemExit("Node.js is required for the landscape consistency check")
    template = (ROOT / "templates/explorer.html").read_text()
    generated = (ROOT / "docs/index.html").read_text()
    # A stale generated Explorer must not pass using only the current template.
    for name in ("viewBasePapers", "mechanismSurfaceCells", "renderHeatmap", "renderLpOverview"):
        pattern = rf"^function {name}\(.*?^}}"
        assert extract(template, pattern) == extract(generated, pattern), f"Regenerate Explorer: {name}"
    code = explorer_code(generated)
    papers = json.loads((ROOT / "data/papers.json").read_text())
    embedded_papers = extract(generated, r"^const papers = [^\n]+")
    assert json.loads(embedded_papers.removeprefix("const papers = ").removesuffix(";")) == papers, \
        "Regenerate Explorer: embedded catalog data is stale"
    cases = [papers, [p for p in papers if p["year"] == 2026], fixture_papers()]
    harness = r"""
const fs = require('node:fs'), vm = require('node:vm');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
const result = input.cases.map(papers => vm.runInNewContext(input.code + `
JSON.stringify({
  ids: viewBasePapers('heatmap', papers).map(p => p.id),
  counts: mechanismSurfaceCells(papers).map(cell => cell.n)
})`, {papers}));
process.stdout.write(JSON.stringify(result.map(JSON.parse)));
"""
    result = subprocess.run([node, "-e", harness], input=json.dumps({"code": code, "cases": cases}),
                            text=True, capture_output=True, check=True)
    for case, actual in zip(cases, json.loads(result.stdout), strict=True):
        wanted = expected(case)
        assert actual == wanted, "Static/Explorer population or cell counts differ"
        assert svg_counts(render_heatmap(case)) == wanted["counts"], "Rendered SVG counts differ"
    wanted = expected(papers)
    for path in (ROOT / "assets/visualizations/threat-heatmap.svg",
                 ROOT / "docs/visualizations/threat-heatmap.svg"):
        assert svg_counts(path.read_text()) == wanted["counts"], f"Regenerate {path.name}"
    print(f"Verified {len(wanted['ids'])}/{len(papers)} eligible records and all {len(wanted['counts'])} cells "
          "across Explorer/static outputs, a filtered subset, and multi-label/coverage fixtures")


if __name__ == "__main__":
    main()
