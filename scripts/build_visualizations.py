#!/usr/bin/env python3
"""Generate static SVG landscape views from data/papers.json."""

from __future__ import annotations

import argparse
import html
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
OUTPUT_DIR = ROOT / "assets" / "visualizations"

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


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def label(value: str) -> str:
    overrides = {"vla": "VLA", "ood": "OOD", "llm": "LLM", "vlm": "VLM"}
    return " ".join(overrides.get(part, part.capitalize()) for part in value.split("-"))


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
        key = {"lifecycle": "lifecycles", "mechanism": "mechanisms", "surface": "surfaces"}.get(field)
        return threat["coverage"].get(key, []) if key else []
    return threat.get(field, [])


def render_topic_trends(papers: list[dict]) -> str:
    width, height = 1200, 650
    body = header("Research areas over time", "Paper counts in the curated catalog; 2026 is an incomplete snapshot.")
    years = sorted({paper["year"] for paper in papers})
    counts = {year: Counter(p["section"] for p in papers if p["year"] == year) for year in years}
    totals = {year: sum(counts[year].values()) for year in years}
    chart_left, chart_top, chart_right, chart_bottom = 90, 120, 1140, 510
    y_max = int(math.ceil(max(totals.values()) / 10) * 10)
    for tick in range(0, y_max + 1, 10):
        y = chart_bottom - (tick / y_max) * (chart_bottom - chart_top)
        body += [
            f'<line x1="{chart_left}" y1="{y:.1f}" x2="{chart_right}" y2="{y:.1f}" stroke="{GRID}"/>',
            f'<text class="axis" x="{chart_left - 14}" y="{y + 5:.1f}" text-anchor="end">{tick}</text>',
        ]
    slot = (chart_right - chart_left) / len(years)
    bar_width = min(150, slot * 0.54)
    for i, year in enumerate(years):
        x = chart_left + slot * (i + 0.5) - bar_width / 2
        y_cursor = chart_bottom
        for section in reversed(SECTION_ORDER):
            count = counts[year][section]
            if not count:
                continue
            h = count / y_max * (chart_bottom - chart_top)
            y_cursor -= h
            body.append(f'<rect x="{x:.1f}" y="{y_cursor:.1f}" width="{bar_width:.1f}" height="{h:.1f}" fill="{SECTION_COLORS[section]}"><title>{esc(SECTION_LABELS[section])}: {count}</title></rect>')
        body += [
            f'<text class="label" x="{x + bar_width / 2:.1f}" y="{chart_bottom + 30}" text-anchor="middle">{year}</text>',
            f'<text class="label" x="{x + bar_width / 2:.1f}" y="{y_cursor - 10:.1f}" text-anchor="middle">{totals[year]}</text>',
        ]
    body.append('<text class="axis" transform="translate(28 330) rotate(-90)" text-anchor="middle">Papers</text>')
    for i, section in enumerate(SECTION_ORDER):
        row, col = divmod(i, 4)
        x, y = 72 + col * 270, 565 + row * 34
        body += [
            f'<rect x="{x}" y="{y - 12}" width="14" height="14" rx="3" fill="{SECTION_COLORS[section]}"/>',
            f'<text class="label" x="{x + 23}" y="{y}">{esc(SECTION_LABELS[section])}</text>',
        ]
    return svg_document("Research areas over time", "Stacked annual paper counts by research area.", width, height, body)


def render_timeline(papers: list[dict]) -> str:
    width, height = 1200, 650
    body = header("Field timeline", "Bubble area represents the number of cataloged papers in each research area and year.")
    years = sorted({paper["year"] for paper in papers})
    counts = Counter((paper["section"], paper["year"]) for paper in papers)
    left, right, top, row_gap = 250, 1120, 128, 64
    x_positions = {year: left + i * (right - left) / (len(years) - 1) for i, year in enumerate(years)}
    max_count = max(counts.values())
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
            count = counts[(section, year)]
            if not count:
                continue
            radius = 7 + 19 * math.sqrt(count / max_count)
            body += [
                f'<circle cx="{x:.1f}" cy="{y}" r="{radius:.1f}" fill="{SECTION_COLORS[section]}" fill-opacity="0.88"><title>{esc(SECTION_LABELS[section])}, {year}: {count} papers</title></circle>',
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
    width, height = 1200, 850
    body = header("Where threats enter and how they act", "Mechanism × surface co-occurrence for concrete threat models; survey coverage is excluded.")
    concrete = [p for p in papers if p["threat_model"]["kind"] not in {"survey", "evaluation"}]
    mechanism_counts = Counter(v for p in concrete for v in threat_values(p, "mechanism"))
    surface_counts = Counter(v for p in concrete for v in threat_values(p, "surface"))
    mechanisms = [value for value, _ in mechanism_counts.most_common(10)]
    surfaces = [value for value, _ in surface_counts.most_common(10)]
    cells = Counter((mechanism, surface) for paper in concrete for mechanism in threat_values(paper, "mechanism") for surface in threat_values(paper, "surface"))
    max_value = max(cells[(m, s)] for m in mechanisms for s in surfaces)
    left, top, cell_w, cell_h = 300, 275, 82, 51
    for col, surface in enumerate(surfaces):
        x = left + col * cell_w + cell_w / 2
        body.append(f'<text class="axis" text-anchor="start" transform="translate({x - 8:.1f} {top - 18}) rotate(-55)">{esc(label(surface))}</text>')
    for row, mechanism in enumerate(mechanisms):
        y = top + row * cell_h
        body.append(f'<text class="label" x="{left - 18}" y="{y + cell_h / 2 + 5:.1f}" text-anchor="end">{esc(label(mechanism))}</text>')
        for col, surface in enumerate(surfaces):
            value = cells[(mechanism, surface)]
            fraction = value / max_value if max_value else 0
            color = blend("#EEF3F8", "#4F67A5", fraction ** 0.72)
            x = left + col * cell_w
            text_color = "#FFFFFF" if fraction > 0.48 else TEXT
            body += [
                f'<rect x="{x + 2}" y="{y + 2}" width="{cell_w - 4}" height="{cell_h - 4}" rx="6" fill="{color}"><title>{esc(label(mechanism))} × {esc(label(surface))}: {value} papers</title></rect>',
                f'<text x="{x + cell_w / 2:.1f}" y="{y + cell_h / 2 + 5:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="{text_color}">{value if value else ""}</text>',
            ]
    body += [
        f'<text class="axis" x="{left + 5 * cell_w}" y="{height - 45}" text-anchor="middle">Threat surface</text>',
        f'<text class="axis" transform="translate(48 {top + 5 * cell_h}) rotate(-90)" text-anchor="middle">Mechanism</text>',
        f'<text class="small" x="{left}" y="{height - 18}">Top 10 mechanisms and surfaces by paper frequency; multi-label records contribute to each applicable cell.</text>',
    ]
    return svg_document("Threat mechanism and surface heatmap", "Heatmap of mechanism and surface co-occurrence counts.", width, height, body)


def paper_features(paper: dict) -> set[str]:
    threat = paper["threat_model"]
    features = {f"kind:{threat['kind']}", f"scope:{paper['scope']}"}
    features.update(f"risk:{value}" for value in paper["risks"])
    for field in ("lifecycle", "mechanism", "surface", "target", "consequence"):
        features.update(f"{field}:{value}" for value in threat_values(paper, field))
    return features


def top_eigenvector(matrix: list[list[float]], orthogonal: list[list[float]]) -> tuple[list[float], float]:
    n = len(matrix)
    vector = [math.sin((i + 1) * 1.61803398875) for i in range(n)]
    for basis in orthogonal:
        projection = sum(a * b for a, b in zip(vector, basis))
        vector = [a - projection * b for a, b in zip(vector, basis)]
    norm = math.sqrt(sum(value * value for value in vector)) or 1.0
    vector = [value / norm for value in vector]
    for _ in range(300):
        candidate = [sum(matrix[i][j] * vector[j] for j in range(n)) for i in range(n)]
        for basis in orthogonal:
            projection = sum(a * b for a, b in zip(candidate, basis))
            candidate = [a - projection * b for a, b in zip(candidate, basis)]
        norm = math.sqrt(sum(value * value for value in candidate)) or 1.0
        candidate = [value / norm for value in candidate]
        if sum((a - b) ** 2 for a, b in zip(candidate, vector)) < 1e-14:
            vector = candidate
            break
        vector = candidate
    eigenvalue = sum(vector[i] * sum(matrix[i][j] * vector[j] for j in range(n)) for i in range(n))
    return vector, max(eigenvalue, 0.0)


def taxonomy_projection(papers: list[dict]) -> list[tuple[float, float]]:
    feature_sets = [paper_features(paper) for paper in papers]
    frequencies = Counter(feature for values in feature_sets for feature in values)
    vocabulary = sorted(frequencies)
    vectors = []
    for values in feature_sets:
        row = [math.log((len(papers) + 1) / (frequencies[f] + 1)) + 1 if f in values else 0.0 for f in vocabulary]
        norm = math.sqrt(sum(value * value for value in row)) or 1.0
        vectors.append([value / norm for value in row])
    means = [sum(row[col] for row in vectors) / len(vectors) for col in range(len(vocabulary))]
    centered = [[value - means[col] for col, value in enumerate(row)] for row in vectors]
    gram = [[sum(a * b for a, b in zip(row_a, row_b)) for row_b in centered] for row_a in centered]
    first, value_1 = top_eigenvector(gram, [])
    second, value_2 = top_eigenvector(gram, [first])
    return [(first[i] * math.sqrt(value_1), second[i] * math.sqrt(value_2)) for i in range(len(papers))]


def topic_x_score(paper: dict) -> float:
    kind = paper["threat_model"]["kind"]
    return -1.0 if kind == "adversarial" else 1.0 if kind == "non-adversarial" else 0.0


def topic_y_score(paper: dict) -> float:
    section = paper["section"]
    if section == "defenses":
        return 1.0
    if section in {"training-attacks", "inference-attacks"}:
        return -0.85
    if section == "system-security":
        return -0.65
    if section == "benchmarks":
        return -0.55
    if section == "ood-generalization":
        return 0.05
    return 0.0


def render_topic_map(papers: list[dict]) -> str:
    width, height = 1200, 760
    body = header("Taxonomy map of the catalog", "Explicit axes: adversarial ↔ non-adversarial and attack/benchmark ↔ defense.")
    left, right, top, bottom = 75, 1125, 115, 625
    def scale(value: float, low: float, high: float, start: float, end: float) -> float:
        return (start + end) / 2 if high == low else start + (value - low) / (high - low) * (end - start)
    mapped = []
    for paper in papers:
        seed = sum(ord(char) for char in paper["id"])
        jitter_x = ((seed % 17) - 8) * 0.012
        jitter_y = ((seed % 13) - 6) * 0.012
        mapped.append((scale(topic_x_score(paper) + jitter_x, -1.08, 1.08, left, right), scale(topic_y_score(paper) + jitter_y, -1.08, 1.08, bottom, top)))
    body += [
        f'<rect x="{left}" y="{top}" width="{right-left}" height="{bottom-top}" rx="10" fill="{PANEL}" stroke="{GRID}"/>',
        f'<line x1="{(left+right)/2}" y1="{top}" x2="{(left+right)/2}" y2="{bottom}" stroke="{GRID}" stroke-dasharray="4 7"/>',
        f'<line x1="{left}" y1="{(top+bottom)/2}" x2="{right}" y2="{(top+bottom)/2}" stroke="{GRID}" stroke-dasharray="4 7"/>',
        f'<text class="axis" x="{left}" y="{bottom + 30}">Adversarial</text>',
        f'<text class="axis" x="{right}" y="{bottom + 30}" text-anchor="end">Non-adversarial</text>',
        f'<text class="axis" transform="translate(26 {top + 8}) rotate(-90)">Defense</text>',
        f'<text class="axis" transform="translate(26 {bottom}) rotate(-90)">Attack + Benchmark</text>',
    ]
    for paper, (x, y) in zip(papers, mapped):
        section = paper["section"]
        body.append(f'<a href="{esc(paper["paper_url"])}"><circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{SECTION_COLORS[section]}" fill-opacity="0.80" stroke="#FFFFFF" stroke-width="1.5"><title>{esc(paper["title"])} — {esc(SECTION_LABELS[section])}</title></circle></a>')
    for i, section in enumerate(SECTION_ORDER):
        row, col = divmod(i, 4)
        x, y = 78 + col * 272, 682 + row * 34
        body += [
            f'<circle cx="{x + 7}" cy="{y - 5}" r="7" fill="{SECTION_COLORS[section]}"/>',
            f'<text class="label" x="{x + 22}" y="{y}">{esc(SECTION_LABELS[section])}</text>',
        ]
    return svg_document("Taxonomy map", "Two-dimensional metadata projection of all cataloged papers.", width, height, body)


def outputs(papers: list[dict]) -> dict[Path, str]:
    return {
        OUTPUT_DIR / "topic-map.svg": render_topic_map(papers),
        OUTPUT_DIR / "topic-trends.svg": render_topic_trends(papers),
        OUTPUT_DIR / "field-timeline.svg": render_timeline(papers),
        OUTPUT_DIR / "threat-heatmap.svg": render_heatmap(papers),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated SVG files are stale")
    args = parser.parse_args()
    papers = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    rendered = outputs(papers)
    stale = []
    for path, content in rendered.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT))
        else:
            path.write_text(content, encoding="utf-8")
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
