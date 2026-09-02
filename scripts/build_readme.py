#!/usr/bin/env python3
"""Generate the public paper list from data/papers.json."""

from __future__ import annotations

import argparse
import json
from collections import OrderedDict
from pathlib import Path
from urllib.parse import urlparse


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
    "ethical-societal": "Ethical",
    "security-privacy": "Security/Privacy",
}


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


def display_tag(tag: str) -> str:
    special = {"ood": "OOD", "vla": "VLA", "llm": "LLM", "api": "API"}
    return " ".join(special.get(piece, piece.capitalize()) for piece in tag.split("-"))


def resources(paper: dict) -> str:
    parts = [f"[Paper]({paper['paper_url']})"]
    code_url = paper.get("code_url")
    repo = github_repo(code_url)
    if repo:
        badge = f"https://img.shields.io/github/stars/{repo}?style=social"
        parts.append(f"[![GitHub stars]({badge})]({code_url})")
    elif code_url:
        parts.append(f"[Project / Code]({code_url})")
    return " · ".join(parts)


def render(papers: list[dict]) -> str:
    lines = [
        "# Awesome Responsible VLA",
        "",
        "A curated, taxonomy-driven list of research on the safety, robustness, security, and responsible deployment of Vision-Language-Action models and closely related embodied agents.",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)",
        "",
        "> This list separates **risk outcomes** (what goes wrong) from **failure sources and mechanisms** (why it goes wrong). GitHub star badges are live and are shown only for identified official repositories.",
        "",
        "## Taxonomy at a Glance",
        "",
        "### Risk outcomes",
        "",
        "- **Task & Reliability:** task failure, degraded success, dangerous inaction, or recovery failure.",
        "- **Physical Safety:** collision, injury, damage, unsafe motion, or constraint violation.",
        "- **Ethical & Societal:** harmful instruction execution, misuse, deception, or oversight failure.",
        "- **Security & Privacy:** unauthorized control, backdoors, leakage, covert channels, or system compromise.",
        "",
        "### Failure sources",
        "",
        "- **Adversarial:** malicious manipulation of inputs, training, states, actions, or system components.",
        "- **Non-adversarial / OOD:** failures under unseen viewpoints, objects, language, tasks, environments, embodiments, or dynamics.",
        "- **Design / system:** misalignment, misspecified objectives, sensor faults, planner-executor mismatch, or failed recovery.",
        "",
        "See [the full taxonomy](docs/taxonomy.md) for definitions and inclusion rules.",
        "",
        "## 🧭 Contents",
        "",
    ]

    present_sections = [key for key in SECTIONS if any(p["section"] == key for p in papers)]
    for key in present_sections:
        icon, title = SECTIONS[key]
        lines.append(f"- [{icon} {title}](#{key})")
    lines.extend(["", f"**{len(papers)} papers in the current catalog.**", ""])

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
                    f"### {subsection}",
                    "",
                    "| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |",
                    "|---|---|---:|---|---|---|---|",
                ]
            )
            rows = [p for p in section_papers if p["subsection"] == subsection]
            rows.sort(key=lambda p: (-p["year"], p["title"].lower()))
            for paper in rows:
                risk = ", ".join(RISK_LABELS[item] for item in paper["risks"])
                focus = ", ".join(display_tag(item) for item in paper["tags"][:3])
                title = paper["title"].replace("|", "\\|")
                venue = f"{paper['venue']} {paper['year']}"
                lines.append(
                    f"| **{title}** | {paper['first_author']} et al. | {venue} | {risk} | {paper['threat_model']} | {focus} | {resources(paper)} |"
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
            "## Contributing",
            "",
            "Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and add or update the corresponding record in `data/papers.json`. Do not edit generated paper tables directly.",
            "",
            "## Acknowledgements",
            "",
            "The organization is informed by the lifecycle and attack/defense views used in [Awesome-VLA-Safety](https://github.com/LiQiiiii/Awesome-VLA-Safety) and [Awesome-LVLM-Safety](https://github.com/XuankunRong/Awesome-LVLM-Safety), extended with explicit risk-outcome and OOD-generalization axes.",
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
