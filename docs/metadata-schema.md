# Type-Specific Metadata Pilot

The catalog keeps a small common record and adds optional extensions only where they apply.

- `defense`: proposed defense position, mechanism, protected surface, addressed threats, and assumptions.
- `evaluation`: experimental environments, platforms, evaluated models, attacker access, metrics, and physical validation.
- `benchmark`: evaluated dimensions, distribution shifts, environment, base platforms, and artifact availability.

`null` means not yet verified, an empty list means verified with no applicable value, and an absent extension means the extension does not apply to that paper.

Controlled values are maintained under [`data/taxonomy`](../data/taxonomy/). The first pilot covers ten representative attack, defense, OOD, and benchmark papers before catalog-wide enrichment.

The optional extension contract is documented in [`paper-extensions.schema.json`](../data/schema/paper-extensions.schema.json), while `scripts/validate_catalog.py` enforces the controlled vocabularies.
