# Repository Instructions

This public repository is the maintained catalog for Awesome Physical AI Safety.

## Sources of Truth

- Use `README.md` for the public scope and curation-policy summary.
- Use `docs/README.md` to identify each document's audience and whether it is source or generated output.
- Use `CONTRIBUTING.md` for contribution and display rules.
- Use `docs/taxonomy.md` for threat, risk, and classification semantics.
- Use `docs/metadata-schema.md` for record and extension semantics.
- Use `docs/agent/daily-curation-workflow.md` for daily literature curation.
- Use `docs/agent/biweekly-metadata-maintenance.md` for periodic metadata maintenance.
- Treat validators and generators as executable enforcement of these documents. If prose and code disagree, resolve the inconsistency instead of silently bypassing either one.

## Working Rules

- Inspect Git status before editing and preserve unrelated changes.
- Edit catalog records in `data/papers.json` and regenerate derived files with repository scripts.
- Do not hand-edit the generated outputs identified in `docs/README.md`.
- Keep public catalog data and English documentation in English. Maintain intentional Japanese pages and labels through their documented workflow.
- Never add private research notes, unpublished ideas, local filesystem paths, credentials, or personal workspace content.
- Run the validation and publication gates in the applicable workflow before committing or pushing.
- This repository is publicly operated. Confirm the expected remote and `PUBLIC` visibility before pushing; never change visibility automatically.
