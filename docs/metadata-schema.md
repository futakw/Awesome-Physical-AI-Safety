# Type-Specific Metadata Pilot

The catalog keeps a small common record and adds optional extensions only where they apply.

- `defense`: proposed defense position, mechanism, protected surface, addressed threats, and assumptions.
- `evaluation`: experimental environments, platforms, evaluated models, attacker access, metrics, and physical validation.
- `benchmark`: evaluated dimensions, distribution shifts, environment, base platforms, and artifact availability.

`null` means not yet verified, an empty list means no value could be established, and an absent extension means the extension does not apply to that paper. Each extension includes `curation_status`; catalog-wide inferred values are explicitly marked `catalog-derived` until checked against the original paper.

Controlled values are maintained under [`data/taxonomy`](../data/taxonomy/). Type-specific extensions now cover every applicable catalog record, with provenance status retained for later paper-level verification.

Within `evaluation`, `models` stores explicitly named evaluated target models or policies. `platforms` stores explicitly named benchmarks, simulators, datasets, or physical robot platforms used for evaluation. Generic descriptions such as “a robotic arm” are not treated as platform names. Names obtained from an abstract are marked `abstract-verified`; unmentioned models or platforms are not inferred.

For `survey` and `evaluation` threat models, `coverage` contains `lifecycles`, `mechanisms`, `surfaces`, and `consequences`. This keeps benchmark threat/consequence aggregation aligned with concrete threat-model records.

The optional extension contract is documented in [`paper-extensions.schema.json`](../data/schema/paper-extensions.schema.json), while `scripts/validate_catalog.py` enforces the controlled vocabularies.
