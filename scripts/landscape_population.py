"""Population shared by the static and interactive concrete-threat maps."""

CONCRETE_THREAT_KINDS = ("adversarial", "non-adversarial", "system-failure")


def concrete_threat_papers(papers: list[dict]) -> list[dict]:
    return [p for p in papers if p["threat_model"]["kind"] in CONCRETE_THREAT_KINDS]
