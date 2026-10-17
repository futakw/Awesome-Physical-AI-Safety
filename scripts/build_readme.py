#!/usr/bin/env python3
"""Generate the public paper list from data/papers.json."""

from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from html import escape
from pathlib import Path
from urllib.parse import quote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
README_PATH = ROOT / "README.md"
PAGES_URL = "https://futakw.github.io/Awesome-Physical-AI-Safety"

SECTIONS = OrderedDict(
    [
        ("surveys", ("📚", "Surveys and Perspectives")),
        ("ood-generalization", ("🌍", "Robustness and OOD Generalization")),
        ("training-attacks", ("🧪", "Training-Time Attacks")),
        ("inference-attacks", ("⚡", "Inference-Time Attacks")),
        ("defenses", ("🛡️", "Defenses and Safety Mechanisms")),
        ("benchmarks", ("📊", "Benchmarks and Evaluation")),
        ("system-security", ("🔐", "System-Level Security, Privacy, and Misuse")),
    ]
)

RISK_LABELS = {
    "task-reliability": "Task",
    "physical-safety": "Physical",
    "ethical-societal": "Ethics",
    "security-privacy": "Security/Privacy",
}

RISK_COLORS = {
    "task-reliability": "6F9FEF",
    "physical-safety": "B88A24",
    "ethical-societal": "9873D4",
    "security-privacy": "D96F8A",
}

THREAT_COLORS = {
    "lifecycle": "6F9FEF",
    "surface": "D47A5D",
    "mechanism": "3FA89B",
    "target": "9873D4",
    "consequence": "D96F8A",
    "survey": "657A8C",
    "evaluation": "2F7F9B",
}


DISPLAY_LABELS = {
    "vla-policy": "VLA policy",
}


def display_label(value: str) -> str:
    return DISPLAY_LABELS.get(value, value.replace("-", " ").title())


def badge(text: str, color: str) -> str:
    escaped = text.replace("-", "--").replace("_", "__").replace(" ", "_")
    url = f"https://img.shields.io/badge/-{quote(escaped, safe='')}-{color}?style=flat"
    return f"![{text}]({url})"


def primary_label(values: list[str]) -> str:
    if not values:
        return "Unestablished"
    label = display_label(values[0])
    return f"{label} +{len(values) - 1}" if len(values) > 1 else label


def risk_cell(risks: list[str]) -> str:
    if not risks:
        return "—"
    return " ".join(badge(RISK_LABELS[risk], RISK_COLORS[risk]) for risk in risks)


def threat_model_cell(threat_model: dict) -> str:
    kind = threat_model["kind"]
    if kind in {"survey", "evaluation"}:
        coverage = threat_model["coverage"]
        lifecycles = coverage["lifecycles"]
        lifecycle = "Cross-lifecycle" if len(lifecycles) > 2 else " → ".join(display_label(value) for value in lifecycles)
        surfaces = coverage["surfaces"]
        surface = "Multiple surfaces" if len(surfaces) > 2 else " + ".join(display_label(value) for value in surfaces)
        return " ".join(
            [
                badge(lifecycle, THREAT_COLORS["lifecycle"]),
                badge(surface, THREAT_COLORS["surface"]),
                "<br>",
                badge(f"{display_label(kind)} coverage", THREAT_COLORS[kind]),
            ]
        )
    lifecycle = " → ".join(display_label(value) for value in threat_model["lifecycle"])
    surface = primary_label(threat_model["surface"])
    mechanism = primary_label(threat_model["mechanism"])
    target = display_label(threat_model["target"][0])
    consequence = display_label(threat_model["consequence"][0])
    return " ".join(
        [
            badge(lifecycle, THREAT_COLORS["lifecycle"]),
            badge(surface, THREAT_COLORS["surface"]),
            "<br>",
            badge(mechanism, THREAT_COLORS["mechanism"]),
            "&nbsp;→&nbsp;",
            badge(target, THREAT_COLORS["target"]),
            "&nbsp;→&nbsp;",
            badge(consequence, THREAT_COLORS["consequence"]),
        ]
    )


def github_repo(url: str | None) -> str | None:
    if not url:
        return None
    parsed = urlparse(url)
    if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return None
    return f"{parts[0]}/{parts[1].removesuffix('.git')}"


def paper_cell(paper: dict) -> str:
    title = (
        paper["title"]
        .replace("|", "\\|")
        .replace("[", "\\[")
        .replace("]", "\\]")
    )
    paper_url = paper.get("paper_url")
    parts = [f"**[{title}]({paper_url})**" if paper_url else f"**{title}**"]
    code_url = paper.get("code_url")
    repo = github_repo(code_url)
    if repo:
        badge = f"https://img.shields.io/github/stars/{repo}?style=social"
        parts.append(f"[![GitHub stars]({badge})]({code_url})")
    elif code_url:
        parts.append(f"[Project / Code]({code_url})")
    author = paper["first_author"]
    author_label = author if author.lower().endswith("et al.") else f"{author} et al."
    return " ".join(parts) + f"<br><sub>{author_label}</sub>"


def subsection_anchor(section_key: str, subsection: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", subsection.lower()).strip("-")
    return f"{section_key}-{slug}"


def render(papers: list[dict]) -> str:
    paper_count = len(papers)
    lines = [
        "# Awesome Physical AI Safety",
        "",
        "**English (this page)** | [Japanese](README.ja.md)",
        "",
        "**🤖 An LLM-assisted bibliography of safety, security, robustness, ethical and societal risks, and trustworthy deployment across VLA, robots, autonomous systems, and embodied agents.**",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)",
        "[![Cite this repository](https://img.shields.io/badge/Cite-CITATION.cff-blue.svg)](CITATION.cff)",
        "[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23348593.svg)](https://doi.org/10.5281/zenodo.23348593)",
        "[![LLM-assisted](https://img.shields.io/badge/curation-%F0%9F%A4%96%20LLM--assisted-critical.svg)](docs/agent/daily-curation-workflow.md)",
        f"[![Licenses: MIT + CC BY 4.0](https://img.shields.io/badge/Licenses-MIT%20%2B%20CC%20BY%204.0-3FA89B?style=flat)](LICENSES.md) [![Papers](https://img.shields.io/badge/Papers-{paper_count}-6F9FEF?style=flat)]({PAGES_URL}/) [![Update](https://img.shields.io/badge/Update-Daily-D47A5D?style=flat)](docs/agent/daily-curation-workflow.md)",
        "",
        f"**[🔎 Explore the interactive research landscape →]({PAGES_URL}/#heatmap)** — open any chart cell to inspect its contributing papers.",
        "",
        "⭐ **If this catalog is useful to you, please star the repo** — it helps other researchers find it and signals that a maintained taxonomy for this field is worth keeping alive.",
        "",
        "## Author",
        "",
        "[**Futa Waseda**](https://futa-waseda.netlify.app/) — Project Assistant Professor, National Institute of Informatics (NII), Japan.",
        "",
        "## About This Catalog",
        "",
        "This LLM-assisted catalog helps researchers explore **how physical AI systems fail** and **which risk outcomes are evaluated** across VLAs, robots, autonomous systems, and embodied agents.",
        "",
        "<p align=\"center\">",
        "  <a href=\"assets/visualizations/physical-ai-safety-overview.png\">",
        "    <img src=\"assets/visualizations/physical-ai-safety-overview.png\" alt=\"Awesome Physical AI Safety overview: structured threat and failure taxonomy, and evaluated risk outcomes\" width=\"750\">",
        "  </a>",
        "</p>",
        "",
        "The five-part threat taxonomy describes studied failure paths; **Measured Risk** labels are classified separately using the metrics reported in each paper. See the [taxonomy and labeling criteria](docs/reference/taxonomy.md) for details.",
        "",
        "### Scope",
        "",
        "This catalog focuses on the safety and trustworthiness of **foundation model–based Physical AI**, viewed through **Perception → Cognition → Planning → Action**. This is a conceptual pipeline, not a required modular architecture, and includes VLA models and LLM/VLM-driven embodied systems in human–robot interaction, multi-robot collaboration, and autonomous driving. General-purpose LLM/VLM work without a clear physical-AI connection is out of scope.",
        "",
        "### Curation Policy",
        "",
        "Taxonomy and workflow design are author-maintained, while paper collection and classification are updated through an LLM-assisted process without individual human review before each update. Metadata may contain errors; please verify important details against the original papers. [Corrections and contributions](CONTRIBUTING.md) are welcome.",
        "",
        "Each paper has one catalog record and one primary-contribution section. Cross-cutting tables are generated views of those same records, not separate entries.",
        "",
        "The optional Defense, Evaluation, and Benchmark metadata extensions are documented in [docs/reference/metadata-schema.md](docs/reference/metadata-schema.md).",
        "",
        "## 📚 Citing",
        "",
        "Cite this catalog for its bibliography, taxonomy, metadata, visualizations, or curation methodology; cite original papers for individual claims. See [CITATION.cff](CITATION.cff).",
        "",
        "```bibtex",
        "@software{Waseda_Awesome_Physical_AI_2026,",
        "  author = {Waseda, Futa},",
        "  doi    = {10.5281/zenodo.23348593},",
        "  month  = oct,",
        "  title  = {{Awesome Physical AI Safety}},",
        "  url    = {https://github.com/futakw/Awesome-Physical-AI-Safety},",
        "  year   = {2026}",
        "}",
        "```",
        "",
        "## 🔎 Research Landscape",
        "",
        "These metadata-based views reveal relationships within this catalog—not field-wide prevalence or evidence that a defense works. Open a cell to check its source papers.",
        "",
        "![Cumulative papers by first submission date](assets/visualizations/submission-growth.svg)",
        "",
        "Cumulative papers by initial submission date (arXiv v1, UTC); unknown dates are excluded. This describes the current catalog sample.",
        "",
        f"[![Cataloged papers by research area and year](assets/visualizations/field-timeline.svg)]({PAGES_URL}/#timeline)",
        "",
        f"Where has this catalog grown over time? [Explore the timeline →]({PAGES_URL}/#timeline)",
        "",
        f"[![Threat mechanisms by entry surface in this catalog](assets/visualizations/threat-heatmap.svg)]({PAGES_URL}/#heatmap)",
        "",
        f"Which threat mechanisms appear at which entry surfaces? [Explore the cross-map →]({PAGES_URL}/#heatmap)",
        "",
        f"[![Threat mechanisms by empirically evaluated risk in this catalog](assets/visualizations/threat-risk-heatmap.svg)]({PAGES_URL}/#risk)",
        "",
        f"Which measured outcomes are reported for each mechanism? [Inspect the underlying papers →]({PAGES_URL}/#risk)",
        "",
    ]
    lines.extend([
        "## How to Read the Catalog",
        "",
        "Each paper is organized by its primary contribution, with two complementary metadata columns:",
        "",
        "### Measured Risk",
        "",
        "Risk labels summarize the outcomes evaluated in each paper:",
        "",
        f"- {badge('Task', RISK_COLORS['task-reliability'])}: Task or route success.",
        f"- {badge('Physical', RISK_COLORS['physical-safety'])}: Collisions, damage, or unsafe motion.",
        f"- {badge('Ethics', RISK_COLORS['ethical-societal'])}: Harmful compliance, policy violations, or disparities.",
        f"- {badge('Security/Privacy', RISK_COLORS['security-privacy'])}: Attack success, hijacking, or information leakage.",
        "",
        "**—** indicates that no corresponding risk outcome is identified from the reported metrics.",
        "",
        "### Threat Model",
        "",
        "Each entry summarizes the structured threat and failure taxonomy in two lines:",
        "",
        f"{badge('Lifecycle', THREAT_COLORS['lifecycle'])} · {badge('Surface', THREAT_COLORS['surface'])}<br>{badge('Mechanism', THREAT_COLORS['mechanism'])} &nbsp;→&nbsp; {badge('Target', THREAT_COLORS['target'])} &nbsp;→&nbsp; {badge('Consequence', THREAT_COLORS['consequence'])}",
        "",
        "A `+N` suffix indicates additional values stored in `data/papers.json`.",
        "",
        "For detailed definitions and classification criteria, see the [full taxonomy](docs/reference/taxonomy.md).",
        "",
        "## 🧭 Contents",
        "",
    ])

    present_sections = [key for key in SECTIONS if any(p["section"] == key for p in papers)]
    section_order = {key: index for index, key in enumerate(present_sections)}
    subsection_order: dict[tuple[str, str], int] = {}
    for paper in papers:
        key = (paper["section"], paper["subsection"])
        if key not in subsection_order:
            subsection_order[key] = len(subsection_order)
    ethics_papers = sorted(
        (p for p in papers if "ethical-societal" in p["risks"]),
        key=lambda p: (
            section_order[p["section"]],
            subsection_order[(p["section"], p["subsection"])],
            -p["year"],
            p["title"].lower(),
        ),
    )
    for key in present_sections:
        icon, title = SECTIONS[key]
        lines.append(f"- [{icon} {title}](#{key})")
    if ethics_papers:
        lines.append("- [⚖️ Ethics & Societal Safety](#ethics-societal-safety)")
    lines.extend(["", "<details>", '<summary><strong>Show subsection index</strong></summary>', ""])
    for key in present_sections:
        icon, title = SECTIONS[key]
        lines.append(f"- **{icon} {title}**")
        subsections = []
        for paper in papers:
            if paper["section"] == key and paper["subsection"] not in subsections:
                subsections.append(paper["subsection"])
        for subsection in subsections:
            lines.append(
                f"  - [{subsection}](#{subsection_anchor(key, subsection)})"
            )
    lines.extend(["", "</details>", "", f"**{len(papers)} papers in the current catalog.**", ""])

    for section_key in present_sections:
        section_papers = [p for p in papers if p["section"] == section_key]
        icon, title = SECTIONS[section_key]
        lines.extend([f'<a id="{section_key}"></a>', "", f"## {icon} {title}", ""])
        subsections = []
        for paper in section_papers:
            if paper["subsection"] not in subsections:
                subsections.append(paper["subsection"])
        for subsection in subsections:
            lines.extend(
                [
                    f'<a id="{subsection_anchor(section_key, subsection)}"></a>',
                    "",
                    f"### {subsection}",
                    "",
                    "| Paper | Venue | Measured Risk | Threat Model |",
                    "|---|---:|---|---|",
                ]
            )
            rows = [p for p in section_papers if p["subsection"] == subsection]
            rows.sort(key=lambda p: (-p["year"], p["title"].lower()))
            for paper in rows:
                risk = risk_cell(paper["risks"])
                venue = f"{paper['venue']} {paper['year']}"
                lines.append(
                    f"| {paper_cell(paper)} | {venue} | {risk} | {threat_model_cell(paper['threat_model'])} |"
                )
            lines.append("")

    if ethics_papers:
        lines.extend([
            '<a id="ethics-societal-safety"></a>',
            "",
            "## ⚖️ Ethics & Societal Safety",
            "",
            f"This thematic view reuses {len(ethics_papers)} catalog records labeled `ethical-societal`. It does not add separate paper records or independently verify their outcome labels.",
            "",
            "| Paper | Venue | Measured Risk | Threat Model |",
            "|---|---:|---|---|",
        ])
        for paper in ethics_papers:
            section_key = paper["section"]
            primary_section = SECTIONS[section_key][1]
            primary_anchor = subsection_anchor(section_key, paper["subsection"])
            paper_info = (
                f"{paper_cell(paper)}<br>"
                f'<sub>Primary: <a href="#{primary_anchor}">'
                f"{escape(primary_section)} / {escape(paper['subsection'])}</a></sub>"
            )
            venue = f"{paper['venue']} {paper['year']}"
            lines.append(
                f"| {paper_info} | {venue} | {risk_cell(paper['risks'])} | {threat_model_cell(paper['threat_model'])} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Contributing",
            "",
            "Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and add or update the corresponding record in `data/papers.json`. Do not edit generated paper tables directly.",
            "",
            "## Licenses",
            "",
            "Code is licensed under [MIT](LICENSE); original catalog content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See [LICENSES.md](LICENSES.md) for scope and attribution details. Linked papers and third-party materials retain their own terms.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if README.md is stale")
    args = parser.parse_args()
    papers = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    output = render(papers)
    if args.check:
        current = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""
        if current != output:
            print("README.md is stale; run scripts/build_readme.py")
            return 1
        return 0
    README_PATH.write_text(output, encoding="utf-8")
    print(f"Generated README.md with {len(papers)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
