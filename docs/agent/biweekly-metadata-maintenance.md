# Biweekly Metadata Maintenance

**Audience:** LLM agents and maintainers running periodic catalog maintenance.

This workflow maintains already-cataloged papers. New-paper discovery and addition belong to the daily curation workflow.

## 1. Read and Inspect

Read `AGENTS.md`, `docs/agent/daily-curation-workflow.md`, `docs/reference/metadata-schema.md`, and `data/papers.json`. Inspect the branch, remote, and working tree. Preserve unrelated changes. Use `scripts/paper_cache.py get <id>` (cache-first, no network access) before re-downloading a record's primary source; do not schedule a recurring full-cache refresh.

## 2. Select Content-Review Targets

Review only records matching at least one condition:

1. venue is still `arXiv`, `OpenReview`, `Preprint`, unset, or otherwise unconfirmed
2. `code_url` is `null`
3. the record was added or updated since the previous biweekly run
4. the paper is opened during venue or code maintenance and its secondary defense metadata may be incomplete
5. `section` is `defenses` but the `defense` extension is absent

Do not perform broad new-paper searches. Use existing paper IDs and URLs to reach primary sources directly.

### Mechanism and Target Vocabulary Stability

Do not run a recurring full-catalog `mechanism` or `target` reclassification. Recheck a record's `mechanism` or `target` only when: the record is already under review for another reason above and new primary-source evidence changes the picture; an ambiguity is resolved by newly available information; validation reports an invalid or deprecated value; or a formal taxonomy migration has been explicitly approved. When a `mechanism` or `target` assignment is corrected, update `threat_model.curation_status` to reflect the evidence actually checked.

## 3. Check Updates

### Venue

- Confirm acceptance or publication through OpenReview, official proceedings, or a publisher page.
- Distinguish submitted, accepted workshop, and accepted main-conference states.
- When a named venue is confirmed, update `venue` and its official venue year together.

### Official Project or Code

- Prefer links from the paper, author project page, or author-maintained repository.
- Keep `code_url: null` when no official or author-maintained artifact is confirmed.

### Secondary Defense Drift

- Audit reviewed records regardless of primary section.
- Add or update `defense` only for a substantive proposed or experimentally evaluated mitigation.
- Exclude discussion-only recommendations, future work, and survey coverage.
- Omit the field after an audited non-applicable result; never publish `defense: null`.

### Other Metadata

Update a formal title change or bibliographic correction only when found during the targeted checks. Do not expand the run into unrelated metadata research.

## 4. Catalog-Wide Mechanical Checks

Every run reports:

- total records with a `defense` object, grouped by primary section
- explicit `defense: null` count
- records in `section: defenses` without a `defense` object

Fix a null or missing primary-defense extension when primary evidence is available; otherwise report it as a blocker. Do not re-read every paper solely to reproduce the completed baseline audit.

Run the full catalog bibliography verification on every biweekly maintenance run:

```bash
python3 scripts/verify_bibliography.py
```

Treat retrieval, parsing, identity, title, author, year, and verified submission-date failures as failures, not successful checks.

## 5. Validate and Publish Changes

If records changed, follow the complete regeneration, validation, review, remote, visibility, commit, and push gates in `docs/agent/daily-curation-workflow.md`. Verify changed records explicitly before publication.

If no metadata changed, do not regenerate derived files or create a commit. Still report the full-verification and defense-sanity results.

## 6. Report

Report:

- venue updates
- official project or code additions
- secondary defense updates
- defense counts by section, null count, and missing primary-defense count
- other formal metadata corrections
- number of targeted records checked and unresolved
- full bibliography verification result
- validation, commit, and push result, or blocker
