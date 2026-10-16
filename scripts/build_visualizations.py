#!/usr/bin/env python3
"""Generate static SVG landscape views from data/papers.json."""

from __future__ import annotations

import argparse
import html
import json
import math
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
OUTPUT_DIR = ROOT / "assets" / "visualizations"
PAGES_OUTPUT_DIR = ROOT / "docs" / "visualizations"

SECTION_ORDER = [
    "surveys", "ood-generalization", "training-attacks", "inference-attacks",
    "defenses", "benchmarks", "system-security",
]
SECTION_LABELS = {
    "surveys": "Surveys", "ood-generalization": "OOD Generalization",
    "training-attacks": "Training Attacks", "inference-attacks": "Inference Attacks",
    "defenses": "Defenses", "benchmarks": "Benchmarks", "system-security": "System Security",
}
SECTION_COLORS = {
    "surveys": "#667585", "ood-generalization": "#2F7D73",
    "training-attacks": "#7356A3", "inference-attacks": "#B0523A",
    "defenses": "#4F67A5", "benchmarks": "#C48724", "system-security": "#AE4560",
}

BG, PANEL, TEXT, MUTED, GRID = "#FFFFFF", "#F7F9FC", "#202938", "#657287", "#DCE3EC"

# Canonical family groupings from docs/reference/taxonomy.md — chart axes are ordered
# and grouped by these, not by raw frequency, so related values sit together.
# mechanism (HOW) is technique-oriented: it classifies the concrete attack
# technique or failure mode a paper studies, grouped by kind of operation, not
# by where it occurs (surface, a deliberately different axis) or an inferred
# root cause. Mirrors docs/reference/taxonomy.md and templates/explorer.html's
# MECHANISM_GROUPS/SURFACE_GROUPS.
MECHANISM_GROUPS = [
    {"name": "data-model-corruption", "label": "Data & Model Corruption", "values": ["data-poisoning", "backdoor", "malicious-adapter", "checkpoint-compromise", "reward-manipulation", "memory-poisoning", "retrieval-poisoning", "membership-inference"]},
    {"name": "perturbation-spoofing", "label": "Perturbation & Spoofing", "values": ["digital-perturbation", "adversarial-patch", "adversarial-object", "sensor-spoofing", "feedback-spoofing", "environment-manipulation"]},
    {"name": "instruction-semantic-manipulation", "label": "Instruction & Semantic Manipulation", "values": ["direct-prompt-injection", "indirect-prompt-injection", "jailbreak", "typographic-injection", "hazardous-instruction"]},
    {"name": "runtime-system-manipulation", "label": "Runtime & System Manipulation", "values": ["middleware-compromise", "network-attack", "denial-of-service", "covert-channel", "state-manipulation", "action-manipulation", "trajectory-manipulation", "representation-manipulation"]},
    {"name": "distribution-shift-uncertainty", "label": "Distribution Shift & Uncertainty", "values": ["distribution-shift", "instruction-ambiguity", "uncertainty-miscalibration"]},
    {"name": "reasoning-planning-execution-failure", "label": "Reasoning, Planning & Execution Failure", "values": ["perception-error", "semantic-misalignment", "planning-error", "execution-error", "multimodal-desynchronization"]},
]
SURFACE_GROUPS = [
    {"name": "training-infrastructure", "label": "Training & Infrastructure", "values": ["model-supply-chain", "middleware-network"]},
    {"name": "perception", "label": "Perception", "values": ["visual-perception", "audio-perception", "physical-semantic-environment"]},
    {"name": "language", "label": "Language", "values": ["user-instruction", "context-memory-retrieval", "multi-agent-communication"]},
    {"name": "proprioception", "label": "Proprioception", "values": ["proprioception"]},
    {"name": "planning-state", "label": "Planning & State", "values": ["world-state", "task-planning"]},
    {"name": "reasoning", "label": "Reasoning", "values": ["reasoning-representation"]},
    {"name": "action-control", "label": "Action & Control", "values": ["action-interface", "execution-control"]},
]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def label(value: str) -> str:
    overrides = {"vla": "VLA", "ood": "OOD", "llm": "LLM", "vlm": "VLM"}
    return " ".join(overrides.get(part, part.capitalize()) for part in value.split("-"))


def split_label(text: str, max_len: int = 14) -> list[str]:
    if len(text) <= max_len:
        return [text]
    words = text.split(" ")
    if len(words) < 2:
        return [text]
    best, best_diff, acc = 0, float("inf"), 0
    for i in range(len(words) - 1):
        acc += len(words[i]) + 1
        diff = abs(acc - len(text) / 2)
        if diff < best_diff:
            best_diff, best = diff, i
    return [" ".join(words[: best + 1]), " ".join(words[best + 1 :])]


def rotated_axis_label(x: float, y: float, angle: float, text: str) -> str:
    lines = split_label(text)
    tspans = "".join(
        f'<tspan x="0" dy="{"0" if i == 0 else "1.05"}em">{esc(line)}</tspan>' for i, line in enumerate(lines)
    )
    return f'<text class="axis" text-anchor="start" transform="translate({x:.1f} {y:.1f}) rotate({angle})">{tspans}</text>'


def family_label(group: dict) -> str:
    return group["label"]


def family_of(value: str, groups: list[dict]) -> dict | None:
    return next((g for g in groups if value in g["values"]), None)


def wrapped_end_label(x: float, y: float, text: str, max_len: int = 24) -> str:
    lines = split_label(text, max_len)
    if len(lines) == 1:
        return f'<text class="axis" text-anchor="end" x="{x:.1f}" y="{y:.1f}">{esc(lines[0])}</text>'
    tspans = "".join(
        f'<tspan x="{x:.1f}" dy="{"-0.35" if i == 0 else "1.1"}em">{esc(line)}</tspan>' for i, line in enumerate(lines)
    )
    return f'<text class="axis" text-anchor="end" x="{x:.1f}" y="{y:.1f}">{tspans}</text>'


def svg_document(title: str, description: str, width: int, height: int, body: list[str]) -> str:
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc" viewBox="0 0 {width} {height}">',
        f'<title id="title">{esc(title)}</title>', f'<desc id="desc">{esc(description)}</desc>',
        "<style>",
        "text { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }",
        ".title { font-size: 28px; font-weight: 650; fill: #202938; }",
        ".subtitle { font-size: 14px; fill: #657287; }",
        ".axis { font-size: 13px; fill: #657287; }",
        ".label { font-size: 13px; fill: #202938; }",
        ".small { font-size: 11px; fill: #657287; }",
        "</style>", f'<rect width="{width}" height="{height}" fill="{BG}"/>', *body, "</svg>", "",
    ])


def header(title: str, subtitle: str) -> list[str]:
    return [
        f'<text class="title" x="48" y="48">{esc(title)}</text>',
        f'<text class="subtitle" x="48" y="74">{esc(subtitle)}</text>',
    ]


def threat_values(paper: dict, field: str) -> list[str]:
    threat = paper["threat_model"]
    if threat["kind"] in {"survey", "evaluation"}:
        key = {"lifecycle": "lifecycles", "mechanism": "mechanisms", "surface": "surfaces", "consequence": "consequences"}.get(field)
        return threat["coverage"].get(key, []) if key else []
    return threat.get(field, [])


def render_timeline(papers: list[dict]) -> str:
    width, height = 1200, 430
    body = header("Field timeline", "Bubble area represents the number of cataloged papers in each research area and year.")
    years = sorted({paper["year"] for paper in papers})
    groups = {
        (section, year): [paper for paper in papers if paper["section"] == section and paper["year"] == year]
        for section in SECTION_ORDER
        for year in years
    }
    left, right, top, row_gap = 250, 1120, 92, 44
    x_positions = {year: left + i * (right - left) / (len(years) - 1) for i, year in enumerate(years)}
    max_count = max(len(group) for group in groups.values())
    for year, x in x_positions.items():
        body += [
            f'<line x1="{x:.1f}" y1="{top - 18}" x2="{x:.1f}" y2="{top + row_gap * (len(SECTION_ORDER) - 1) + 24}" stroke="{GRID}"/>',
            f'<text class="label" x="{x:.1f}" y="{top - 34}" text-anchor="middle">{year}</text>',
        ]
    for row, section in enumerate(SECTION_ORDER):
        y = top + row * row_gap
        body += [
            f'<text class="label" x="{left - 28}" y="{y + 5}" text-anchor="end">{esc(SECTION_LABELS[section])}</text>',
            f'<line x1="{left}" y1="{y}" x2="{right}" y2="{y}" stroke="{GRID}"/>',
        ]
        for year, x in x_positions.items():
            group = groups[(section, year)]
            count = len(group)
            if not count:
                continue
            radius = 7 + 19 * math.sqrt(count / max_count)
            papers_title = "\n".join(f"[{paper['venue']} {paper['year']}] {paper['title']}" for paper in group)
            body += [
                f'<circle cx="{x:.1f}" cy="{y}" r="{radius:.1f}" fill="{SECTION_COLORS[section]}" fill-opacity="0.88"><title>{esc(papers_title)}</title></circle>',
                f'<text x="{x:.1f}" y="{y + 5}" text-anchor="middle" font-size="12" font-weight="600" fill="#FFFFFF">{count}</text>',
            ]
    body.append(f'<text class="small" x="{left}" y="{height - 34}">No bubble means no paper in the current catalog for that area-year cell.</text>')
    return svg_document("Field timeline", "Research-area lanes with annual paper-count bubbles.", width, height, body)


def blend(low: str, high: str, fraction: float) -> str:
    fraction = max(0.0, min(1.0, fraction))
    lo = [int(low[i:i + 2], 16) for i in (1, 3, 5)]
    hi = [int(high[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(a + (b - a) * fraction):02X}" for a, b in zip(lo, hi))


def render_heatmap(papers: list[dict]) -> str:
    width, height = 1200, 610
    body = header("Where threats enter and how they act", "Mechanism family × surface family co-occurrence for concrete threat models; survey coverage is excluded.")
    concrete = [p for p in papers if p["threat_model"]["kind"] not in {"survey", "evaluation"}]
    mechanisms, surfaces = MECHANISM_GROUPS, SURFACE_GROUPS
    left, top, cell_w, cell_h = 330, 195, 110, 50
    cell_data = []
    for mech_group in mechanisms:
        for surf_group in surfaces:
            matching = [
                paper for paper in concrete
                if any(m in mech_group["values"] for m in threat_values(paper, "mechanism"))
                and any(s in surf_group["values"] for s in threat_values(paper, "surface"))
            ]
            cell_data.append((mech_group, surf_group, matching))
    max_value = max((len(matching) for _, _, matching in cell_data), default=1) or 1
    for col, surf_group in enumerate(surfaces):
        x = left + col * cell_w + cell_w / 2
        body.append(rotated_axis_label(x - 8, top - 16, -30, family_label(surf_group)))
    for row, mech_group in enumerate(mechanisms):
        y = top + row * cell_h
        body.append(wrapped_end_label(left - 18, y + cell_h / 2 + 5, family_label(mech_group)))
    for mech_group, surf_group, matching in cell_data:
        row, col = mechanisms.index(mech_group), surfaces.index(surf_group)
        y = top + row * cell_h
        x = left + col * cell_w
        value = len(matching)
        fraction = value / max_value if max_value else 0
        color = blend("#EEF3F8", "#4F67A5", fraction ** 0.72)
        text_color = "#FFFFFF" if fraction > 0.48 else TEXT
        papers_title = "\n".join(f"[{paper['venue']} {paper['year']}] {paper['title']}" for paper in matching)
        body += [
            f'<rect x="{x + 2}" y="{y + 2}" width="{cell_w - 4}" height="{cell_h - 4}" rx="6" fill="{color}"><title>{esc(papers_title)}</title></rect>',
            f'<text x="{x + cell_w / 2:.1f}" y="{y + cell_h / 2 + 5:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="{text_color}">{value if value else ""}</text>',
        ]
    body += [
        f'<text class="axis" x="{left + len(surfaces) * cell_w / 2}" y="{top + len(mechanisms) * cell_h + 42}" text-anchor="middle">Threat surface family</text>',
        f'<text class="axis" transform="translate(48 {top + len(mechanisms) * cell_h / 2}) rotate(-90)" text-anchor="middle">Mechanism family</text>',
        f'<text class="small" x="{left}" y="{top + len(mechanisms) * cell_h + 64}">All {len(mechanisms)} mechanism and {len(surfaces)} surface families are shown; multi-label records contribute to each applicable cell.</text>',
    ]
    return svg_document("Threat mechanism and surface heatmap", "Heatmap of mechanism family and surface family co-occurrence counts.", width, height, body)


def render_defense_heatmap(papers: list[dict]) -> str:
    width, height = 1200, 980
    body = header("Defense coverage map", "Defense subsections × the threats they address; multi-label records contribute to each applicable cell.")
    defenses = [paper for paper in papers if paper["section"] == "defenses"]
    subsections = [value for value, _ in Counter(paper["subsection"] for paper in defenses).most_common()]
    concrete = [paper for paper in papers if paper["threat_model"].get("kind") not in {"survey", "evaluation"}]
    mechanisms = [value for value, _ in Counter(value for paper in concrete for value in threat_values(paper, "mechanism")).most_common(10)]
    left, top, cell_w, cell_h = 390, 185, 77, 43
    max_value = max((sum(1 for paper in defenses if paper["subsection"] == subsection and mechanism in threat_values(paper, "mechanism")) for subsection in subsections for mechanism in mechanisms), default=1)
    for col, mechanism in enumerate(mechanisms):
        x = left + col * cell_w + cell_w / 2
        body.append(f'<text class="axis" text-anchor="start" transform="translate({x - 8:.1f} {top - 18}) rotate(-52)">{esc(label(mechanism))}</text>')
    for row, subsection in enumerate(subsections):
        y = top + row * cell_h
        body.append(f'<text class="label" x="{left - 18}" y="{y + cell_h / 2 + 4:.1f}" text-anchor="end">{esc(subsection)}</text>')
        for col, mechanism in enumerate(mechanisms):
            matching = [paper for paper in defenses if paper["subsection"] == subsection and mechanism in threat_values(paper, "mechanism")]
            value = len(matching)
            fraction = value / max_value if max_value else 0
            color = blend("#EEF3F8", "#6F9FEF", fraction ** 0.72)
            x = left + col * cell_w
            text_color = "#FFFFFF" if fraction > 0.48 else TEXT
            papers_title = "\n".join(f"[{paper['venue']} {paper['year']}] {paper['title']}" for paper in matching)
            body += [
                f'<rect x="{x + 2}" y="{y + 2}" width="{cell_w - 4}" height="{cell_h - 4}" rx="6" fill="{color}"><title>{esc(papers_title)}</title></rect>',
                f'<text x="{x + cell_w / 2:.1f}" y="{y + cell_h / 2 + 4:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="{text_color}">{value if value else ""}</text>',
            ]
    body += [
        f'<text class="axis" x="{left + 5 * cell_w}" y="{top + len(subsections) * cell_h + 36}" text-anchor="middle">threat_model.mechanism</text>',
        f'<text class="axis" transform="translate(45 {top + len(subsections) * cell_h / 2}) rotate(-90)" text-anchor="middle">Defense subsection</text>',
    ]
    return svg_document("Defense coverage map", "Defense subsection and addressed-threat mechanism counts.", width, height, body)


def render_benchmark_heatmap(papers: list[dict]) -> str:
    width, height = 1200, 760
    body = header("Benchmark coverage map", "Benchmark subsections × the threat mechanisms represented in their evaluations.")
    benchmarks = [paper for paper in papers if paper["section"] == "benchmarks"]
    subsections = [value for value, _ in Counter(paper["subsection"] for paper in benchmarks).most_common()]
    concrete = [paper for paper in papers if paper["threat_model"].get("kind") not in {"survey", "evaluation"}]
    mechanisms = [value for value, _ in Counter(value for paper in concrete for value in threat_values(paper, "mechanism")).most_common(10)]
    left, top, cell_w, cell_h = 390, 185, 77, 43
    max_value = max((sum(1 for paper in benchmarks if paper["subsection"] == subsection and mechanism in threat_values(paper, "mechanism")) for subsection in subsections for mechanism in mechanisms), default=1)
    for col, mechanism in enumerate(mechanisms):
        x = left + col * cell_w + cell_w / 2
        body.append(f'<text class="axis" text-anchor="start" transform="translate({x - 8:.1f} {top - 18}) rotate(-52)">{esc(label(mechanism))}</text>')
    for row, subsection in enumerate(subsections):
        y = top + row * cell_h
        body.append(f'<text class="label" x="{left - 18}" y="{y + cell_h / 2 + 4:.1f}" text-anchor="end">{esc(subsection)}</text>')
        for col, mechanism in enumerate(mechanisms):
            matching = [paper for paper in benchmarks if paper["subsection"] == subsection and mechanism in threat_values(paper, "mechanism")]
            value = len(matching); fraction = value / max_value if max_value else 0; color = blend("#EEF3F8", "#6F9FEF", fraction ** 0.72); x = left + col * cell_w; text_color = "#FFFFFF" if fraction > 0.48 else TEXT
            papers_title = "\n".join(f"[{paper['venue']} {paper['year']}] {paper['title']}" for paper in matching)
            body += [f'<rect x="{x + 2}" y="{y + 2}" width="{cell_w - 4}" height="{cell_h - 4}" rx="6" fill="{color}"><title>{esc(papers_title)}</title></rect>', f'<text x="{x + cell_w / 2:.1f}" y="{y + cell_h / 2 + 4:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="{text_color}">{value if value else ""}</text>']
    body += [f'<text class="axis" x="{left + 5 * cell_w}" y="{top + len(subsections) * cell_h + 36}" text-anchor="middle">threat_model.mechanism</text>', f'<text class="axis" transform="translate(45 {top + len(subsections) * cell_h / 2}) rotate(-90)" text-anchor="middle">Benchmark subsection</text>']
    return svg_document("Benchmark coverage map", "Benchmark subsection and threat-mechanism counts.", width, height, body)


def render_extension_heatmap(papers, extension, title, subtitle, row_field, col_field, row_label, col_label, cols_override=None):
    items = [paper for paper in papers if extension in paper]
    rows = list(dict.fromkeys(value for paper in items for value in paper[extension][row_field]))
    cols = cols_override or list(dict.fromkeys(value for paper in items for value in paper[extension][col_field]))
    width, left, top, cell_h = 1200, 300, 185, 54
    cell_w = min(125, (width - left - 35) / max(1, len(cols)))
    height = max(620, int(top + len(rows) * cell_h + 90))
    body = header(title, f"{subtitle} ({len(items)} enriched papers).")
    cells = {(row, col): [paper for paper in items if row in paper[extension][row_field] and col in paper[extension][col_field]] for row in rows for col in cols}
    max_value = max((len(value) for value in cells.values()), default=1)
    for index, col in enumerate(cols):
        x = left + index * cell_w + cell_w / 2
        body.append(f'<text class="axis" text-anchor="start" transform="translate({x - 8:.1f} {top - 18}) rotate(-52)">{esc(label(col))}</text>')
    for rindex, row in enumerate(rows):
        y = top + rindex * cell_h
        body.append(f'<text class="label" x="{left - 18}" y="{y + cell_h / 2 + 4:.1f}" text-anchor="end">{esc(label(row))}</text>')
        for cindex, col in enumerate(cols):
            matching = cells[(row, col)]; value = len(matching); fraction = value / max_value if max_value else 0
            x = left + cindex * cell_w; color = blend("#EEF3F8", "#6F9FEF", fraction ** 0.72); text_color = "#FFFFFF" if fraction > 0.48 else TEXT
            papers_title = "\n".join(f"[{paper['venue']} {paper['year']}] {paper['title']}" for paper in matching)
            body += [f'<rect x="{x + 2}" y="{y + 2}" width="{cell_w - 4}" height="{cell_h - 4}" rx="6" fill="{color}"><title>{esc(papers_title)}</title></rect>', f'<text x="{x + cell_w / 2:.1f}" y="{y + cell_h / 2 + 4:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="{text_color}">{value if value else ""}</text>']
    body += [f'<text class="axis" x="{left + len(cols) * cell_w / 2}" y="{top + len(rows) * cell_h + 40}" text-anchor="middle">{esc(col_label)}</text>', f'<text class="axis" transform="translate(45 {top + len(rows) * cell_h / 2}) rotate(-90)" text-anchor="middle">{esc(row_label)}</text>']
    return svg_document(title, subtitle, width, height, body)


def order_by_groups(values: list[str], groups: list[dict]) -> list[str]:
    order = [v for group in groups for v in group["values"]]
    present = set(values)
    return [v for v in order if v in present]


def ordered_threat_mechanisms(papers: list[dict]) -> list[str]:
    concrete = [paper for paper in papers if paper["threat_model"]["kind"] not in {"survey", "evaluation"}]
    top = [value for value, _ in Counter(value for paper in concrete for value in threat_values(paper, "mechanism")).most_common(10)]
    return order_by_groups(top, MECHANISM_GROUPS)


def render_threat_risk_heatmap(papers: list[dict]) -> str:
    # Include benchmark/evaluation records: their threat coverage and evaluated
    # risks are precisely what this cross-map is intended to summarize.
    concrete = [paper for paper in papers if paper["threat_model"]["kind"] != "survey"]
    rows = MECHANISM_GROUPS
    cols = ["task-reliability", "physical-safety", "ethical-societal", "security-privacy"]
    width, left, top, cell_h = 1200, 330, 112, 50
    cell_w = 190
    height = max(430, int(top + len(rows) * cell_h + 70))
    body = header("Threat mechanism family × evaluated risk", "Empirically evaluated outcome families; empty cells remain visible.")
    cells = {
        (row["name"], col): [
            paper for paper in concrete
            if any(m in row["values"] for m in threat_values(paper, "mechanism")) and col in paper.get("risks", [])
        ]
        for row in rows for col in cols
    }
    max_value = max((len(value) for value in cells.values()), default=1)
    for index, col in enumerate(cols):
        x = left + index * cell_w + cell_w / 2
        body.append(f'<text class="axis" x="{x:.1f}" y="{top - 12}" text-anchor="middle">{esc(label(col))}</text>')
    for rindex, row in enumerate(rows):
        y = top + rindex * cell_h
        body.append(wrapped_end_label(left - 18, y + cell_h / 2 + 5, family_label(row)))
        for cindex, col in enumerate(cols):
            matching = cells[(row["name"], col)]
            value = len(matching)
            fraction = value / max_value if max_value else 0
            x = left + cindex * cell_w
            color = blend("#EEF3F8", "#9873D4", fraction ** 0.72)
            text_color = "#FFFFFF" if fraction > 0.48 else TEXT
            papers_title = "\n".join(f"[{paper['venue']} {paper['year']}] {paper['title']}" for paper in matching)
            body += [
                f'<rect x="{x + 2}" y="{y + 2}" width="{cell_w - 4}" height="{cell_h - 4}" rx="6" fill="{color}"><title>{esc(papers_title)}</title></rect>',
                f'<text x="{x + cell_w / 2:.1f}" y="{y + cell_h / 2 + 4:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="{text_color}">{value if value else ""}</text>',
            ]
    body += [
        f'<text class="axis" x="{left + len(cols) * cell_w / 2}" y="{top + len(rows) * cell_h + 40}" text-anchor="middle">Evaluated risk</text>',
        f'<text class="axis" transform="translate(45 {top + len(rows) * cell_h / 2}) rotate(-90)" text-anchor="middle">Mechanism family</text>',
        f'<text class="small" x="{left}" y="{height - 18}">All {len(rows)} mechanism families are shown; risk labels require a corresponding empirical outcome metric.</text>',
    ]
    return svg_document("Threat mechanism family × evaluated risk", "Cross-map of threat mechanism families and empirically evaluated risk outcomes.", width, height, body)


def render_benchmark_threat_consequence(papers: list[dict]) -> str:
    items = [paper for paper in papers if paper["section"] == "benchmarks"]
    rows = [value for value, _ in Counter(value for paper in items for value in threat_values(paper, "mechanism")).most_common()]
    cols = list(dict.fromkeys(value for paper in items for value in threat_values(paper, "consequence")))
    width, left, top, cell_h = 1200, 300, 185, 54
    cell_w = min(135, (width - left - 35) / max(1, len(cols))); height = max(720, int(top + len(rows) * cell_h + 90))
    body = header("Threat mechanism × consequence", f"Benchmark papers only ({len(items)} papers).")
    cells = {(row, col): [paper for paper in items if row in threat_values(paper, "mechanism") and col in threat_values(paper, "consequence")] for row in rows for col in cols}
    max_value = max((len(value) for value in cells.values()), default=1)
    for index, col in enumerate(cols):
        x = left + index * cell_w + cell_w / 2; body.append(f'<text class="axis" text-anchor="start" transform="translate({x - 8:.1f} {top - 18}) rotate(-52)">{esc(label(col))}</text>')
    for rindex, row in enumerate(rows):
        y = top + rindex * cell_h; body.append(f'<text class="label" x="{left - 18}" y="{y + cell_h / 2 + 4:.1f}" text-anchor="end">{esc(label(row))}</text>')
        for cindex, col in enumerate(cols):
            matching = cells[(row, col)]; value = len(matching); fraction = value / max_value if max_value else 0; x = left + cindex * cell_w; color = blend("#EEF3F8", "#6F9FEF", fraction ** 0.72); text_color = "#FFFFFF" if fraction > 0.48 else TEXT
            papers_title = "\n".join(f"[{paper['venue']} {paper['year']}] {paper['title']}" for paper in matching)
            body += [f'<rect x="{x + 2}" y="{y + 2}" width="{cell_w - 4}" height="{cell_h - 4}" rx="6" fill="{color}"><title>{esc(papers_title)}</title></rect>', f'<text x="{x + cell_w / 2:.1f}" y="{y + cell_h / 2 + 4:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="{text_color}">{value if value else ""}</text>']
    return svg_document("Threat mechanism × consequence", "Benchmark threat and consequence cross-map.", width, height, body)


def render_submission_growth(papers: list[dict]) -> str:
    counts = Counter(p["first_submission_date"] for p in papers if p.get("first_submission_date"))
    width, height = 1200, 270
    known = sum(counts.values())
    body = [f'<text x="48" y="35" font-size="22" font-weight="650" fill="{TEXT}">Papers by first submission date</text>',
            f'<text class="subtitle" x="48" y="59">Cumulative papers in this catalog · {known} dated · {len(papers) - known} unknown dates excluded</text>']
    if not counts:
        body.append('<text class="label" x="48" y="140">No verified submission dates available.</text>')
        return svg_document("Submission history", "No verified dates.", width, height, body)
    days = sorted(counts)
    start, end = date.fromisoformat(days[0]), date.fromisoformat(days[-1])
    left, right, top, bottom = 74, 1110, 84, 208
    span = max((end - start).days, 1)
    x = lambda d: left + (d - start).days / span * (right - left)
    ceiling = max(50, math.ceil(known / 50) * 50)
    y = lambda n: bottom - n / ceiling * (bottom - top)
    for n in range(0, ceiling + 1, max(50, ceiling // 4 // 50 * 50)):
        yy = y(n)
        body += [f'<line x1="{left}" y1="{yy:.2f}" x2="{right}" y2="{yy:.2f}" stroke="{GRID}"/>',
                 f'<text class="axis" x="{left - 12}" y="{yy + 4:.2f}" text-anchor="end">{n}</text>']
    path = f'M {left} {bottom}'
    total = 0
    for day in days:
        total += counts[day]
        path += f' H {x(date.fromisoformat(day)):.2f} V {y(total):.2f}'
    body += [f'<path d="{path} L {right} {bottom} Z" fill="#2F7D73" fill-opacity="0.10"/>',
             f'<path d="{path}" fill="none" stroke="#2F7D73" stroke-width="2.5"/>',
             f'<text class="label" x="{right + 10}" y="{y(total) + 4:.2f}">{total}</text>']
    ticks = [start] + [date(year, 1, 1) for year in range(start.year + 1, end.year + 1)] + [end]
    for d in ticks:
        if d != end and d != start and min((d-start).days, (end-d).days) < span * .09:
            continue
        body.append(f'<text class="axis" x="{x(d):.2f}" y="230" text-anchor="middle">{d.isoformat() if d in (start, end) else str(d.year)}</text>')
    body.append('<text class="small" x="48" y="256">arXiv v1 dates (UTC). This is the current curated sample, not catalog-addition history or field-wide publication volume.</text>')
    return svg_document("Papers by first submission date", f"Cumulative initial submissions: {known} dated papers; {len(papers)-known} unknown dates excluded.", width, height, body)


def outputs(papers: list[dict]) -> dict[Path, str]:
    return {
        OUTPUT_DIR / "submission-growth.svg": render_submission_growth(papers),
        OUTPUT_DIR / "field-timeline.svg": render_timeline(papers),
        OUTPUT_DIR / "threat-heatmap.svg": render_heatmap(papers),
        OUTPUT_DIR / "threat-risk-heatmap.svg": render_threat_risk_heatmap(papers),
        OUTPUT_DIR / "defense-heatmap.svg": render_extension_heatmap(papers, "defense", "Defense mechanism × defended threat", "Columns follow the Threat Cross-Map order, including empty cells", "mechanism", "defends_against", "Defense mechanism", "Defended threat", ordered_threat_mechanisms(papers)),
        OUTPUT_DIR / "benchmark-heatmap.svg": render_benchmark_threat_consequence(papers),
        OUTPUT_DIR / "evaluation-heatmap.svg": render_extension_heatmap(papers, "evaluation", "Evaluation environment × metric", "Catalog-wide metadata; unspecified marks records awaiting paper-level verification", "environments", "metrics", "Environment", "Metric"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated SVG files are stale")
    args = parser.parse_args()
    papers = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    rendered = outputs(papers)
    stale = []
    for path, content in rendered.items():
        for target in (path, PAGES_OUTPUT_DIR / path.name):
            if args.check:
                if not target.exists() or target.read_text(encoding="utf-8") != content:
                    stale.append(target.relative_to(ROOT))
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")
    if stale:
        print("Generated visualizations are stale:")
        for path in stale:
            print(f"- {path}")
        return 1
    action = "Verified" if args.check else "Generated"
    print(f"{action} {len(rendered)} visualizations from {len(papers)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
