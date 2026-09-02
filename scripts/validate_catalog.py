#!/usr/bin/env python3
"""Validate public metadata and guard against accidental private-content leakage."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"

REQUIRED = {
    "id",
    "title",
    "first_author",
    "venue",
    "year",
    "paper_url",
    "code_url",
    "section",
    "subsection",
    "scope",
    "risks",
    "threat_model",
    "tags",
}
SECTIONS = {
    "surveys",
    "ood-generalization",
    "training-attacks",
    "inference-attacks",
    "defenses",
    "benchmarks",
    "system-security",
}
RISKS = {"task-reliability", "physical-safety", "ethical-societal", "security-privacy"}
THREAT_CATEGORIES = {
    "Training-time attack",
    "Inference-time attack",
    "System-level attack",
    "Non-adversarial OOD",
    "Execution failure",
    "Planning failure",
    "Policy failure",
    "Uncertainty failure",
    "Hazardous instruction",
    "Physical safety violation",
    "Semantic safety violation",
    "System-level misuse",
    "Survey scope",
    "Evaluation scope",
}
PRIVATE_MARKERS = {
    "my_works",
    "research_questions",
    "kakenhi",
    "idea_notes",
    "project_c",
    "raw/papers",
    "responsible-vla-wiki",
}
CJK = re.compile(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]")


def valid_url(value: str | None) -> bool:
    if value is None:
        return True
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main() -> int:
    errors: list[str] = []
    papers = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if not isinstance(papers, list) or not papers:
        errors.append("data/papers.json must be a non-empty array")
        papers = []

    seen_ids: set[str] = set()
    seen_titles: set[str] = set()
    seen_paper_urls: set[str] = set()
    for index, paper in enumerate(papers):
        label = paper.get("id", f"record[{index}]")
        missing = REQUIRED - set(paper)
        if missing:
            errors.append(f"{label}: missing {sorted(missing)}")
        paper_id = paper.get("id")
        title = paper.get("title")
        if paper_id in seen_ids:
            errors.append(f"{label}: duplicate id")
        if title and title.casefold() in seen_titles:
            errors.append(f"{label}: duplicate title")
        if paper_id:
            seen_ids.add(paper_id)
        if title:
            seen_titles.add(title.casefold())
        paper_url = paper.get("paper_url")
        if paper_url in seen_paper_urls:
            errors.append(f"{label}: duplicate paper_url {paper_url!r}")
        if paper_url:
            seen_paper_urls.add(paper_url)
        if paper.get("section") not in SECTIONS:
            errors.append(f"{label}: invalid section {paper.get('section')!r}")
        invalid_risks = set(paper.get("risks", [])) - RISKS
        if invalid_risks:
            errors.append(f"{label}: invalid risks {sorted(invalid_risks)}")
        if not isinstance(paper.get("risks"), list):
            errors.append(f"{label}: risks must be a list")
        if not paper.get("tags"):
            errors.append(f"{label}: tags must not be empty")
        if not isinstance(paper.get("threat_model"), str) or not paper.get("threat_model", "").strip():
            errors.append(f"{label}: threat_model must be a non-empty string")
        else:
            threat_model = paper["threat_model"]
            category = threat_model.split(" (", 1)[0]
            if category not in THREAT_CATEGORIES:
                errors.append(f"{label}: invalid threat category {category!r}")
            if " (" in threat_model and not threat_model.endswith(")"):
                errors.append(f"{label}: threat_model must use 'Category (detail)' notation")
            if len(threat_model) > 90:
                errors.append(f"{label}: threat_model exceeds 90 characters")
        if not isinstance(paper.get("year"), int) or not 2000 <= paper.get("year", 0) <= 2100:
            errors.append(f"{label}: invalid year")
        for field in ("paper_url", "code_url"):
            if not valid_url(paper.get(field)):
                errors.append(f"{label}: invalid {field}")

    public_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts
    ]
    for path in public_files:
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        lower_path = relative.lower()
        for marker in PRIVATE_MARKERS:
            if marker in lower_path:
                errors.append(f"{relative}: private marker {marker!r} in path")
            if path.resolve() != Path(__file__).resolve() and marker in text.lower():
                errors.append(f"{relative}: private marker {marker!r} in content")
        if path.suffix in {".md", ".json"} and CJK.search(text):
            errors.append(f"{relative}: contains CJK text; the public repository must be English-only")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(papers)} paper records and {len(public_files)} public files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
