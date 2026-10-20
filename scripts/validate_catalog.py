#!/usr/bin/env python3
"""Validate public metadata and guard against accidental private-content leakage."""

from __future__ import annotations

from datetime import date
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
VENUE_RANKS_PATH = ROOT / "data" / "venue_ranks.json"
TAXONOMY_DIR = ROOT / "data" / "taxonomy"

REQUIRED = {
    "catalogued_date",
    "first_submission_date",
    "first_submission_source",
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
# subsection is a closed vocabulary scoped per section. Add a new value here
# (and its translation in scripts/labels_ja.py's SUBSECTIONS_JA) only after
# checking this list for an existing subsection that already fits — see
# docs/agent/daily-curation-workflow.md and docs/reference/metadata-schema.md#subsection.
SUBSECTIONS = {
    "surveys": {
        "Embodied AI Safety and Security",
        "Position Papers and Research Agendas",
        "Privacy, Fairness, and Human-Robot Trust",
        "General VLA Surveys",
        "Domain-Specific Surveys",
        "Training and Adaptation Surveys",
        "World Model Safety and Security",
        "Governance and Deployment Assurance",
    },
    "ood-generalization": {
        "Representation and Language-Action Generalization",
        "OOD and Generalization",
        "Action and Spatial Generalization",
        "Open-World Evaluation",
        "Driving Robustness and Generalization",
        "Language and Instruction Generalization",
        "Reliability-Oriented Policy Refinement",
    },
    "training-attacks": {
        "Backdoors and Data Poisoning",
        "Privacy and Data Leakage",
    },
    "inference-attacks": {
        "Jailbreaks and Prompt Injection",
        "Visual Perturbations and Patches",
        "Planning, Action, and Trajectory Manipulation",
        "Sensor, State, and Physical Interventions",
        "Upstream VLM Attacks",
        "Privacy and Data Leakage",
    },
    "defenses": {
        "Runtime Monitoring and Guardrails",
        "Failure Detection, Shielding, and Recovery",
        "Safety-Aligned and Robust Policy Training",
        "Uncertainty, Abstention, and Human Oversight",
        "Representation Steering and Inference-Time Defense",
        "Multimodal Perception and Physical Safeguards",
        "System and Communication Defenses",
        "Privacy-Preserving Perception",
        "Model Unlearning and Data Governance",
        "Safety Requirements and Assurance",
    },
    "benchmarks": {
        "Task and Physical Safety",
        "Semantic and Ethical Safety",
        "Human-Robot Trust and Fairness",
        "Robustness, Uncertainty, and OOD Generalization",
        "Evaluation Infrastructure",
        "Adversarial and Physical Robustness",
        "Safety-Critical Perception Evaluation",
        "Failure Detection and Recovery",
        "Governance and Deployment Assurance",
        "Privacy and Data Leakage",
    },
    "system-security": {
        "Cross-Layer System Security",
        "Privacy, Misuse, and Covert Channels",
    },
}
RISKS = {"task-reliability", "physical-safety", "ethical-societal", "security-privacy"}
THREAT_KINDS = {"adversarial", "non-adversarial", "system-failure", "evaluation", "survey"}
LIFECYCLES = {"training", "inference", "system"}
# Technique-oriented vocabulary (see docs/reference/taxonomy.md "How? — Mechanism
# Vocabulary"). HOW classifies the concrete attack technique or failure mode a
# paper studies; it does not require establishing an underlying causal
# mechanism, and a label may remain defined here with zero current users when
# no catalog paper yet demonstrates it (e.g. representation-manipulation).
MECHANISMS = {
    "action-manipulation", "adversarial-object", "adversarial-patch",
    "backdoor", "checkpoint-compromise",
    "covert-channel", "data-poisoning", "denial-of-service", "digital-perturbation",
    "direct-prompt-injection", "distribution-shift", "environment-manipulation",
    "execution-error", "feedback-spoofing", "hazardous-instruction",
    "indirect-prompt-injection", "instruction-ambiguity", "jailbreak", "malicious-adapter",
    "membership-inference", "memory-poisoning", "middleware-compromise",
    "multimodal-desynchronization", "network-attack", "perception-error", "planning-error",
    "representation-manipulation",
    "retrieval-poisoning", "reward-manipulation", "self-assessment-failure", "semantic-misalignment", "sensor-spoofing",
    "state-manipulation", "trajectory-manipulation", "typographic-injection",
    "uncertainty-miscalibration",
}
# Ordered to match the perceive -> reason -> act grouping in docs/reference/taxonomy.md
# (training & infrastructure -> perception -> language -> proprioception ->
# planning & state -> reasoning -> action & control). A set, so this order
# has no runtime effect; it's kept for readability/consistency with the docs.
SURFACES = {
    "model-supply-chain", "middleware-network",
    "visual-perception", "audio-perception", "physical-semantic-environment",
    "user-instruction", "context-memory-retrieval", "multi-agent-communication",
    "proprioception",
    "world-state", "task-planning",
    "reasoning-representation",
    "action-interface", "execution-control",
}
TARGETS = {
    "perception-model", "world-state", "reasoning-process", "task-planner", "vla-policy",
    "action-generation", "runtime-monitor", "robot-executor", "shared-system-state",
    "private-data",
}
CONSEQUENCES = {
    "task-failure", "targeted-action", "action-freezing", "unsafe-success", "collision",
    "unsafe-motion", "physical-damage", "control-hijacking", "policy-violation",
    "privacy-leakage", "availability-loss", "recovery-failure",
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
JAPANESE_FILES = {
    "README.ja.md",
    "CONTRIBUTING.ja.md",
    "docs/reference/taxonomy.ja.md",
    "docs/public/taxonomy.ja.md",
}
VENUE_RANK_BANDS = {"A*", "A", "B", "C", "regional", "other", "unranked"}
VENUE_RANK_STATUSES = {"ranked", "unranked", "not-covered"}


def valid_url(value: str | None) -> bool:
    if value is None:
        return True
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate_submission(errors: list[str], label: str, paper: dict) -> None:
    value = paper.get("first_submission_date")
    source = paper.get("first_submission_source")
    if value is None:
        if source is not None:
            errors.append(f"{label}: unknown submission date requires null source")
        return
    try:
        if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError
        date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label}: invalid first_submission_date")
    if not isinstance(source, str) or not valid_url(source):
        errors.append(f"{label}: verified submission date requires HTTPS source")


def validate_catalogued_date(errors: list[str], label: str, paper: dict) -> None:
    value = paper.get("catalogued_date")
    try:
        if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError
        parsed = date.fromisoformat(value)
        if parsed > date.today():
            errors.append(f"{label}: catalogued_date must not be in the future")
    except ValueError:
        errors.append(f"{label}: invalid catalogued_date")


def validate_venue_ranks(errors: list[str], papers: list[dict]) -> None:
    if not VENUE_RANKS_PATH.exists():
        errors.append("data/venue_ranks.json is missing")
        return
    try:
        payload = json.loads(VENUE_RANKS_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"data/venue_ranks.json is invalid JSON: {exc}")
        return
    if payload.get("schema_version") != 1:
        errors.append("data/venue_ranks.json: schema_version must be 1")
    venues = payload.get("venues")
    if not isinstance(venues, dict):
        errors.append("data/venue_ranks.json: venues must be an object")
        return
    paper_venues = {paper.get("venue") for paper in papers}
    missing = sorted(paper_venues - set(venues))
    extra = sorted(venue for venue in set(venues) - paper_venues if not venues[venue].get("parent_only"))
    if missing:
        errors.append(f"data/venue_ranks.json: missing catalog venues {missing}")
    if extra:
        errors.append(f"data/venue_ranks.json: entries not used by catalog {extra}")
    for venue, record in venues.items():
        label = f"venue rank {venue}"
        if not isinstance(record, dict):
            errors.append(f"{label}: record must be an object")
            continue
        if not isinstance(record.get("canonical_name"), str) or not record["canonical_name"].strip():
            errors.append(f"{label}: canonical_name must be a non-empty string")
        if not isinstance(record.get("aliases"), list) or any(not isinstance(item, str) for item in record["aliases"]):
            errors.append(f"{label}: aliases must be a list of strings")
        if record.get("core_rank_band") not in VENUE_RANK_BANDS:
            errors.append(f"{label}: invalid core_rank_band {record.get('core_rank_band')!r}")
        if record.get("ranking_status") not in VENUE_RANK_STATUSES:
            errors.append(f"{label}: invalid ranking_status {record.get('ranking_status')!r}")
        if not isinstance(record.get("ranking_edition"), str) or not record["ranking_edition"]:
            errors.append(f"{label}: ranking_edition must be a non-empty string")
        if not isinstance(record.get("checked_date"), str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", record["checked_date"]):
            errors.append(f"{label}: checked_date must be YYYY-MM-DD")
        if not valid_url(record.get("source_url")):
            errors.append(f"{label}: source_url must be an HTTPS URL")
        if "parent_only" in record and not isinstance(record["parent_only"], bool):
            errors.append(f"{label}: parent_only must be boolean")


def validate_string_list(
    errors: list[str], label: str, field: str, value: object, allowed: set[str], *, empty_ok: bool = False
) -> None:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        errors.append(f"{label}: threat_model.{field} must be a list of strings")
        return
    if not value and not empty_ok:
        errors.append(f"{label}: threat_model.{field} must not be empty")
    if len(value) != len(set(value)):
        errors.append(f"{label}: threat_model.{field} contains duplicates")
    invalid = set(value) - allowed
    if invalid:
        errors.append(f"{label}: invalid threat_model.{field} {sorted(invalid)}")


def validate_threat_model(errors: list[str], label: str, threat_model: object, taxonomies: dict) -> None:
    if not isinstance(threat_model, dict):
        errors.append(f"{label}: threat_model must be an object")
        return
    kind = threat_model.get("kind")
    if kind not in THREAT_KINDS:
        errors.append(f"{label}: invalid threat_model.kind {kind!r}")
        return
    if threat_model.get("curation_status") not in taxonomies["threat_model"]["curation_statuses"]:
        errors.append(f"{label}: invalid threat_model.curation_status {threat_model.get('curation_status')!r}")
    if kind in {"survey", "evaluation"}:
        if set(threat_model) != {"kind", "coverage", "curation_status"}:
            errors.append(f"{label}: {kind} threat_model must contain only kind, coverage, and curation_status")
        coverage = threat_model.get("coverage")
        if not isinstance(coverage, dict):
            errors.append(f"{label}: threat_model.coverage must be an object")
            return
        if set(coverage) != {"lifecycles", "mechanisms", "surfaces", "consequences"}:
            errors.append(f"{label}: threat_model.coverage must contain lifecycles, mechanisms, surfaces, and consequences")
        validate_string_list(errors, label, "coverage.lifecycles", coverage.get("lifecycles"), LIFECYCLES)
        mechanisms = coverage.get("mechanisms")
        if mechanisms == ["multiple"]:
            pass
        else:
            validate_string_list(errors, label, "coverage.mechanisms", mechanisms, MECHANISMS, empty_ok=True)
        validate_string_list(errors, label, "coverage.surfaces", coverage.get("surfaces"), SURFACES)
        validate_string_list(errors, label, "coverage.consequences", coverage.get("consequences"), CONSEQUENCES, empty_ok=True)
        return
    expected = {"kind", "lifecycle", "mechanism", "surface", "target", "consequence", "curation_status"}
    if set(threat_model) != expected:
        errors.append(f"{label}: concrete threat_model fields must be {sorted(expected)}")
    validate_string_list(errors, label, "lifecycle", threat_model.get("lifecycle"), LIFECYCLES)
    # empty_ok: a reviewed record may have no leaf that fits without inferring an
    # unsupported technique (see docs/reference/taxonomy.md, HOW assignment rules).
    validate_string_list(errors, label, "mechanism", threat_model.get("mechanism"), MECHANISMS, empty_ok=True)
    validate_string_list(errors, label, "surface", threat_model.get("surface"), SURFACES)
    validate_string_list(errors, label, "target", threat_model.get("target"), TARGETS)
    validate_string_list(errors, label, "consequence", threat_model.get("consequence"), CONSEQUENCES)


def validate_values(errors: list[str], label: str, field: str, value: object, allowed: set[str]) -> None:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        errors.append(f"{label}: {field} must be a list of strings")
        return
    invalid = set(value) - allowed
    if invalid:
        errors.append(f"{label}: invalid {field} {sorted(invalid)}")


def validate_extensions(errors: list[str], label: str, paper: dict, taxonomies: dict) -> None:
    if "defense" in paper and paper["defense"] is None:
        errors.append(f"{label}: defense must be an object or omitted after audit; null is not publishable")
    defense = paper.get("defense")
    if defense is not None:
        expected = {"position", "mechanism", "protected_surface", "defends_against", "assumptions", "curation_status"}
        if set(defense) != expected:
            errors.append(f"{label}: defense fields must be {sorted(expected)}")
        validate_values(errors, label, "defense.position", defense.get("position"), set(taxonomies["defense"]["positions"]))
        validate_values(errors, label, "defense.mechanism", defense.get("mechanism"), set(taxonomies["defense"]["mechanisms"]))
        validate_values(errors, label, "defense.protected_surface", defense.get("protected_surface"), SURFACES)
        validate_values(errors, label, "defense.defends_against", defense.get("defends_against"), MECHANISMS)
        validate_values(errors, label, "defense.assumptions", defense.get("assumptions"), set(taxonomies["defense"]["assumptions"]))
        if defense.get("curation_status") not in taxonomies["defense"]["curation_statuses"]:
            errors.append(f"{label}: invalid defense.curation_status {defense.get('curation_status')!r}")
    evaluation = paper.get("evaluation")
    if evaluation is not None:
        expected = {"environments", "platforms", "models", "access", "metrics", "physical_validation", "curation_status"}
        if set(evaluation) != expected:
            errors.append(f"{label}: evaluation fields must be {sorted(expected)}")
        validate_values(errors, label, "evaluation.environments", evaluation.get("environments"), set(taxonomies["evaluation"]["environments"]))
        validate_values(errors, label, "evaluation.access", evaluation.get("access"), set(taxonomies["evaluation"]["access"]))
        validate_values(errors, label, "evaluation.metrics", evaluation.get("metrics"), set(taxonomies["evaluation"]["metrics"]))
        if evaluation.get("physical_validation") not in {True, False, None}:
            errors.append(f"{label}: evaluation.physical_validation must be true, false, or null")
        if evaluation.get("curation_status") not in taxonomies["evaluation"]["curation_statuses"]:
            errors.append(f"{label}: invalid evaluation.curation_status {evaluation.get('curation_status')!r}")
    benchmark = paper.get("benchmark")
    if benchmark is not None:
        expected = {"evaluates", "shift_types", "environment", "base_platforms", "public_data", "leaderboard", "curation_status"}
        if set(benchmark) != expected:
            errors.append(f"{label}: benchmark fields must be {sorted(expected)}")
        validate_values(errors, label, "benchmark.evaluates", benchmark.get("evaluates"), set(taxonomies["benchmark"]["evaluates"]))
        validate_values(errors, label, "benchmark.shift_types", benchmark.get("shift_types"), set(taxonomies["benchmark"]["shift_types"]))
        if benchmark.get("environment") not in set(taxonomies["benchmark"]["environments"]):
            errors.append(f"{label}: invalid benchmark.environment {benchmark.get('environment')!r}")
        if benchmark.get("curation_status") not in taxonomies["benchmark"]["curation_statuses"]:
            errors.append(f"{label}: invalid benchmark.curation_status {benchmark.get('curation_status')!r}")


def load_tag_vocabulary(errors: list[str]) -> set[str]:
    path = TAXONOMY_DIR / "tags.json"
    try:
        values = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"data/taxonomy/tags.json: cannot load vocabulary: {exc}")
        return set()
    if not isinstance(values, list) or not values or any(
        not isinstance(value, str) or not value.strip() or value != value.strip()
        for value in values
    ):
        errors.append("data/taxonomy/tags.json: must be a non-empty array of non-blank, trimmed strings")
        return set()
    if len(values) != len(set(values)):
        errors.append("data/taxonomy/tags.json: contains duplicate values")
    return set(values)


def validate_tags(errors: list[str], label: str, tags: object, allowed: set[str]) -> None:
    if not isinstance(tags, list) or any(not isinstance(tag, str) for tag in tags):
        errors.append(f"{label}: tags must be a list of strings")
        return
    if not tags:
        errors.append(f"{label}: tags must not be empty")
    if len(tags) != len(set(tags)):
        errors.append(f"{label}: tags contains duplicates")
    invalid = set(tags) - allowed
    if invalid:
        errors.append(f"{label}: unregistered tags {sorted(invalid)}; register values in data/taxonomy/tags.json")


def main() -> int:
    errors: list[str] = []
    papers = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    taxonomies = {name: json.loads((TAXONOMY_DIR / f"{name}.json").read_text(encoding="utf-8")) for name in ("defense", "evaluation", "benchmark", "threat_model")}
    if not isinstance(papers, list) or not papers:
        errors.append("data/papers.json must be a non-empty array")
        papers = []
    validate_venue_ranks(errors, papers)
    allowed_tags = load_tag_vocabulary(errors)

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
        section = paper.get("section")
        if section not in SECTIONS:
            errors.append(f"{label}: invalid section {section!r}")
        elif paper.get("subsection") not in SUBSECTIONS[section]:
            errors.append(f"{label}: invalid subsection {paper.get('subsection')!r} for section {section!r}")
        if not isinstance(paper.get("risks"), list):
            errors.append(f"{label}: risks must be a list")
        else:
            invalid_risks = set(paper["risks"]) - RISKS
            if invalid_risks:
                errors.append(f"{label}: invalid risks {sorted(invalid_risks)}")
        validate_tags(errors, label, paper.get("tags"), allowed_tags)
        validate_threat_model(errors, label, paper.get("threat_model"), taxonomies)
        validate_extensions(errors, label, paper, taxonomies)
        validate_catalogued_date(errors, label, paper)
        validate_submission(errors, label, paper)
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
        if path.suffix in {".md", ".json"} and relative not in JAPANESE_FILES and CJK.search(text):
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
