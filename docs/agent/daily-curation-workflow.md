# Bounded New-Paper Curation

**Audience:** recurring research scouts. This filename remains stable for existing integrations; scheduling is configured externally. Read the companion [maintenance workflow](biweekly-metadata-maintenance.md) for already-cataloged papers.

## 1. Start and coordinate

Inspect branch, remote and working tree, fetch the expected remote before editing, and preserve unrelated changes. Fast-forward only when safe. Use the shared queue/guard procedure in [curation-queue.md](curation-queue.md); hold its run lock through source review, catalog edits, validation and publication. If another run holds it, do not edit the catalog or queue; report current counts and exit. Initialize state only during setup, never recreate an unreadable queue during a run.

Read `AGENTS.md`, current Scope, `docs/reference/metadata-schema.md`, and relevant taxonomy sections. Load the catalog ID/title/URL index programmatically, not the complete JSON into model context. Use compact automation memory, a PAPERS heading/ID/date scan, and only the latest or specifically needed archive blocks. Do not read the full research archive or refresh the full source cache.

## 2. Discover and queue

Use source-specific successful scan boundaries and cached listing fingerprints. Screen only the new title/abstract/identifier/date delta. Reject duplicate identities and obvious scope failures before opening paper bodies. Compare normalized title, primary URL, arXiv/DOI/OpenReview IDs, and available title history. Do not re-add renamed work.

Scope requires a direct VLA or foundation-model Physical AI reliability contribution: safety, robustness, failure detection, recovery or trustworthy physical-agent execution. LLM/VLM-driven systems qualify through direct agent/task behavior or physical/symbolic safety-constraint evaluation, including simulation. Standalone VLM perception/recognition/grounding/video-rating papers do not qualify through robotics motivation alone. Generic capability work and broad surveys with an incidental safety chapter are excluded. Do not retrospectively delete existing records.

Enqueue new candidates in lane `new`. Mechanically detected updates to known records go to `maintenance` with a concrete revision/venue/code/correction/invalid-metadata signal and an evidence key; do not read or update those papers here. Missing code, an unconfirmed venue, or recent catalog addition alone is not a signal. Record successful scan cursors only after the candidate batch is durably enqueued; preserve boundaries for failed retrieval/parsing.

## 3. Review at most 20 candidates

Claim one candidate before inspecting paper bodies or performing targeted bibliography/field verification beyond discovery-listing title/abstract screening. Every admitted record requires a claim, even if its abstract suffices. The queue enforces 20 distinct candidates per run, including held and rejected outcomes. Title/ID/date deduplication and cheap discovery screening do not consume claims. Continue FIFO pending work; excess remains queued. Do not open unclaimed paper bodies. If a selected record is already cataloged, route it to maintenance without substantive review.

Read the abstract first, then only the methods, experiments and limitations passages needed for scope and the retained classification fields. Store source text locally; emit compact selected excerpts, not complete HTML/PDF or truncated bulk dumps. Do not characterize targeted inspection as an exhaustive full-paper review. For an existing cached source, use `scripts/paper_cache.py get <id>` first. A newly fetched cache document requires observed title/identifier comparison and `verify --match true --observed-title ...`; resolve mismatches before using it. No unverified cache evidence.

Confirm official title, first-author surname, identity, primary URL and arXiv v1 UTC submission date. Use arXiv/OpenReview for unconfirmed publication; do not hunt venues for new records. Use an official project/code link only when directly established and reachable; otherwise null. No opportunistic historical synchronization or metadata repairs.

Edit `data/papers.json`, never generated output. Collect common bibliography, dates, section/subsection, scope, empirically supported risks, structured threat model, and actual curation status. For a substantive secondary defense, collect only `mechanism`, `defends_against`, `curation_status`, regardless of primary section. Do not collect or backfill evaluation/benchmark extensions or legacy defense position/protected_surface/assumptions. Preserve all existing detailed metadata. Inspect empirical outcomes to support risks even though metric lists are no longer collected.

Use existing controlled values. Empty mechanism/tag lists are preferable to guesses where allowed. Add a new controlled leaf only when indispensable to express an evidenced, in-scope required classification; synchronize validator, Japanese labels and public taxonomy documentation when applicable. Do not add optional descriptive tags or redesign axes/sections. Preserve evidence-based mechanism/target semantics, including the explicit-report plus independently unmet-criterion rule for self-assessment-failure.

Resolve held/rejected candidates with a short reason. Holds require a changed evidence key, new version, or confirmed source restoration before another review. Keep accepted work pending until publication succeeds; only then resolve it as `added`. A failed publication leaves it pending for the next run.

## 4. Validate and publish once

If no catalog/schema/taxonomy/template change exists, do not generate files, verify unchanged bibliography, commit or push. Otherwise verify each changed record explicitly (skip bibliography only when no record changed):

```bash
python3 scripts/verify_bibliography.py --id <changed-id>
python3 scripts/validate_catalog.py
python3 scripts/check_public_taxonomy.py
python3 -m unittest discover -s tests
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
python3 scripts/build_readme_ja.py
python3 scripts/build_readme_ja.py --check
python3 scripts/build_visualizations.py
python3 scripts/build_visualizations.py --check
python3 scripts/build_doc_pages.py
python3 scripts/build_doc_pages.py --check
python3 scripts/build_explorer.py
python3 scripts/check_landscape_consistency.py
git diff --check
```

Run this suite once after changes settle. Repeat only for subsequent changes, failures, or remote integration. A failed retrieval, identity, bibliography, validator, translation or generated-output check is not a pass. Review changed risk/threat/defense annotations, placement, duplicate identities, paper/code links, matching English/Japanese counts, and absence of local paths or unpublished material.

Immediately before commit/push confirm expected fetch/push remote `https://github.com/futakw/Awesome-Physical-AI-Safety.git`, fresh `gh repo view futakw/Awesome-Physical-AI-Safety --json visibility` = `PUBLIC`, and unchanged remote main. Never change visibility, force-push, rewrite history, or discard unrelated work. If upstream advanced, integrate safely and rerun affected gates. Commit only this work; otherwise report the blocker. No literature change means no curation commit.

## 5. Finish and report, including empty or failed runs

Always report reviewed N/20, additions, updates, holds, exclusions, and both lanes' pending/held/total counts from the updated queue snapshot. Missing/unreadable queue means **unknown/read failed**, never zero. Include coverage, added titles or links to their single source-backed notes, catalog count, changed-record bibliography/generation results and commit/push result or blocker. Release the guard with success or failed, then capture its final report; archive the same counts. If setup/locking fails, call read-only `report` and still emit an end report.

Use PAPERS entries of 3–5 lines per paper/change, DASHBOARD at most three current findings, and a timestamped append-only archive block with IDs, decisions, counts, short reasons and publication result. Do not copy long summaries between them or copy queue contents into memory. Keep research-hub writes to the configured allowlist. Work directly by default; if necessary delegate at most one isolated subagent with only candidate IDs, sources and relevant rules, without conversation-history inheritance.
