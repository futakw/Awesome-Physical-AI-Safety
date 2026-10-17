#!/usr/bin/env python3
"""Check public taxonomy vocabulary against canonical references and validators."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from validate_catalog import CONSEQUENCES, LIFECYCLES, MECHANISMS, RISKS, SURFACES, TARGETS


ROOT = Path(__file__).resolve().parents[1]
AXES = {
    "lifecycle": LIFECYCLES,
    "surface": SURFACES,
    "mechanism": MECHANISMS,
    "target": TARGETS,
    "consequence": CONSEQUENCES,
    "risks": RISKS,
}
PUBLIC_AXIS_HEADINGS = ["WHEN", "WHERE", "HOW", "TARGET", "CONSEQUENCE", "MEASURED RISK"]
REFERENCE_FILES = {
    "en": ROOT / "docs" / "reference" / "taxonomy.md",
    "ja": ROOT / "docs" / "reference" / "taxonomy.ja.md",
}
PUBLIC_FILES = {
    "en": ROOT / "docs" / "public" / "taxonomy.md",
    "ja": ROOT / "docs" / "public" / "taxonomy.ja.md",
}


def synced_block(text: str, axis: str, path: Path) -> str:
    pattern = rf"<!-- taxonomy-sync:start {axis} -->(.*?)<!-- taxonomy-sync:end {axis} -->"
    match = re.search(pattern, text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"{path}: missing taxonomy-sync block for {axis}")
    return match.group(1)


def labels(block: str) -> set[str]:
    return set(re.findall(r"`([a-z][a-z0-9-]*)`", block))


def public_families(block: str) -> list[str]:
    return re.findall(r"^\| \*\*(.+?)\*\* \|", block, flags=re.MULTILINE)


def reference_section(text: str, axis: str, path: Path) -> str:
    headings = {
        "surface": r"^### (?:Where\?|どこから？).*$",
        "mechanism": r"^### (?:How\?|どのように？).*$",
        "target": r"^### (?:What Is the Target|攻撃・評価の対象は何か？).*$",
    }
    match = re.search(headings[axis], text, flags=re.MULTILINE | re.IGNORECASE)
    if not match:
        raise ValueError(f"{path}: cannot find canonical {axis} section")
    following = re.search(r"^### ", text[match.end():], flags=re.MULTILINE)
    end = match.end() + following.start() if following else len(text)
    return text[match.end():end]


def canonical_families(text: str, axis: str, path: Path) -> list[str]:
    section = reference_section(text, axis, path)
    return re.findall(r"^\| \*\*(.+?)\*\* \|\s*\|", section, flags=re.MULTILINE)


def main() -> int:
    errors: list[str] = []
    public_texts = {lang: path.read_text(encoding="utf-8") for lang, path in PUBLIC_FILES.items()}
    reference_texts = {lang: path.read_text(encoding="utf-8") for lang, path in REFERENCE_FILES.items()}

    for lang, text in public_texts.items():
        path = PUBLIC_FILES[lang]
        actual_headings = re.findall(
            r"^## (WHEN|WHERE|HOW|TARGET|CONSEQUENCE|MEASURED RISK)$", text, flags=re.MULTILINE
        )
        if actual_headings != PUBLIC_AXIS_HEADINGS:
            errors.append(
                f"{path}: public axes differ; expected={PUBLIC_AXIS_HEADINGS}, actual={actual_headings}"
            )
        for axis, expected in AXES.items():
            try:
                actual = labels(synced_block(text, axis, path))
            except ValueError as error:
                errors.append(str(error))
                continue
            if actual != expected:
                errors.append(
                    f"{path}: {axis} labels differ; missing={sorted(expected - actual)}, "
                    f"unexpected={sorted(actual - expected)}"
                )

        for axis in ("surface", "mechanism", "target"):
            try:
                actual = public_families(synced_block(text, axis, path))
                expected = canonical_families(reference_texts[lang], axis, REFERENCE_FILES[lang])
            except ValueError as error:
                errors.append(str(error))
                continue
            if actual != expected:
                errors.append(f"{path}: {axis} families differ; expected={expected}, actual={actual}")

    for axis in AXES:
        en_labels = labels(synced_block(public_texts["en"], axis, PUBLIC_FILES["en"]))
        ja_labels = labels(synced_block(public_texts["ja"], axis, PUBLIC_FILES["ja"]))
        if en_labels != ja_labels:
            errors.append(f"English/Japanese public {axis} labels are not aligned")

    if errors:
        print("Public taxonomy consistency check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Verified public taxonomy: 6 axes, canonical families, and all leaf labels")
    return 0


if __name__ == "__main__":
    sys.exit(main())
