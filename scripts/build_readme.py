#!/usr/bin/env python3
"""Generate the public paper list from data/papers.json."""

from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from pathlib import Path
from urllib.parse import quote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
README_PATH = ROOT / "README.md"

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
    "physical-safety": "D96F8A",
    "ethical-societal": "9873D4",
    "security-privacy": "B88A24",
}

THREAT_COLORS = {
    "lifecycle": "6F9FEF",
    "surface": "3FA89B",
    "mechanism": "D47A5D",
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
    lines = [
        "# Awesome Responsible VLA",
        "",
        "A curated, taxonomy-driven list of research on the safety, robustness, security, and responsible deployment of Vision-Language-Action models and closely related embodied agents.",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)",
        "",
        "> This list separates **empirically evaluated risk outcomes** (what the paper measures) from **failure sources and mechanisms** (why it goes wrong). GitHub star badges are live and are shown only for identified official repositories.",
        "",
        "## Provenance",
        "",
        "The taxonomy (risk outcomes, failure sources, and the structured threat model schema) was designed by **Futa Waseda**, who also designed the literature collection and curation methodology.",
        "",
        "Day-to-day catalog maintenance — searching for new papers, extracting metadata, and classifying each entry against the taxonomy — is performed by an autonomous AI agent following the fixed rules in [the daily curation workflow](docs/daily-curation-workflow.md). **No per-entry human review is performed before an entry is committed.** Report suspected misclassifications or errors via an issue or pull request.",
        "",
        "## Research Landscape",
        "",
        "[![Field timeline of the paper catalog](assets/visualizations/field-timeline.svg)](docs/visualizations.md)",
        "",
        "Open the [interactive explorer](docs/index.html) for hoverable paper lists in the field timeline and the Threat, Threat × Risk, Defense, Benchmark, and Evaluation cross-maps.",
        "",
    ]
    lines.extend([
        "## Taxonomy at a Glance",
        "",
        "### Risk outcomes",
        "",
        "A label is shown only when the paper reports a corresponding empirical outcome metric; discussion or potential impact alone does not qualify.",
        "",
        f"- {badge('Task', RISK_COLORS['task-reliability'])} task or route completion, success rate, or equivalent execution outcome.",
        f"- {badge('Physical', RISK_COLORS['physical-safety'])} collision, damage, unsafe motion or force, physical harm, or safety-constraint violation.",
        f"- {badge('Ethics', RISK_COLORS['ethical-societal'])} harmful-instruction compliance or refusal, prohibited behavior, or policy/constitution violation.",
        f"- {badge('Security/Privacy', RISK_COLORS['security-privacy'])} attack success, backdoor activation, control hijacking, unauthorized access, leakage, or compromise.",
        "- **—:** no directly corresponding outcome is empirically evaluated, as is common for surveys and diagnostic-only work.",
        "",
        "### Failure sources",
        "",
        "- **Adversarial:** malicious manipulation of inputs, training, states, actions, or system components.",
        "- **Non-adversarial / OOD:** failures under unseen viewpoints, objects, language, tasks, environments, embodiments, or dynamics.",
        "- **Design / system:** misalignment, misspecified objectives, sensor faults, planner-executor mismatch, or failed recovery.",
        "",
        "### Threat model badges",
        "",
        "Each concrete threat model is rendered in two lines. A `+N` suffix indicates additional values retained in `data/papers.json`.",
        "",
        f"{badge('Lifecycle', THREAT_COLORS['lifecycle'])} {badge('Surface', THREAT_COLORS['surface'])}<br>{badge('Mechanism', THREAT_COLORS['mechanism'])} &nbsp;→&nbsp; {badge('Target', THREAT_COLORS['target'])} &nbsp;→&nbsp; {badge('Consequence', THREAT_COLORS['consequence'])}",
        "",
        "See [the full taxonomy](docs/taxonomy.md) for definitions and inclusion rules.",
        "",
        "## 🧭 Contents",
        "",
    ])

    present_sections = [key for key in SECTIONS if any(p["section"] == key for p in papers)]
    for key in present_sections:
        icon, title = SECTIONS[key]
        lines.append(f"- [{icon} {title}](#{key})")
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
                    "| Paper | Venue | Evaluated Risk | Threat Model |",
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

    lines.extend(
        [
            "## Scope and Curation Policy",
            "",
            "The core scope is VLA safety, robustness, security, and evaluation. Closely related LLM-robot, VLM-driven embodied-agent, autonomous-driving, and robot-policy papers are included when they expose a risk, mechanism, defense, or evaluation principle that transfers directly to VLA systems.",
            "",
            "A paper is listed once under its primary contribution. Risk outcomes and mechanisms are represented as multi-label metadata rather than by duplicating the paper across sections.",
            "",
            "The optional Defense, Evaluation, and Benchmark metadata extensions are documented in [docs/metadata-schema.md](docs/metadata-schema.md).",
            "",
            "## Contributing",
            "",
            "Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and add or update the corresponding record in `data/papers.json`. Do not edit generated paper tables directly.",
            "",
            "## License",
            "",
            "MIT License. Paper titles, author names, venues, and links remain the property of their respective authors and publishers.",
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
