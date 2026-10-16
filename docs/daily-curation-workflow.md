# Daily Curation Workflow

This document is the operational source of truth for recurring literature curation in Awesome Physical AI Safety. Keep automation prompts short: they should provide local execution context and point here rather than duplicate these rules.

## 1. Read Before Working

From the repository root, read:

- `AGENTS.md`
- the Scope and Curation Policy in `README.md`
- `CONTRIBUTING.md`
- `docs/taxonomy.md`
- `docs/metadata-schema.md`
- `data/papers.json`

Inspect the current branch, remote, and working tree before editing. Preserve unrelated changes; do not reset or overwrite them.

## 2. Search and Verify

1. Search primary sources for new papers and material revisions since the previous run.
2. Prefer arXiv, OpenReview, official proceedings, publisher pages, author project pages, and official or author-maintained repositories.
3. Read the abstract and inspect the method, experiments, and limitations when needed for scope or metadata decisions. Do not report abstract review as full-paper review.
4. Confirm the official title, first-author surname, paper identity, publication state, paper URL, and any official project or code URL.
5. Check normalized title, paper URL, arXiv ID, DOI, OpenReview ID, and title history before adding a record. Update renamed or materially revised work in place.

Crossref, search results, and other reading lists are discovery aids, not substitutes for a primary source.

## 3. Decide Scope

Use the current Scope in `README.md` and contribution rules in `CONTRIBUTING.md`. The catalog focuses on safety and trustworthiness of foundation model-based Physical AI. General LLM/VLM safety, conventional robotics, HRI, driving, or multi-robot work requires a concrete connection to the catalog scope.

Exclude unrelated uses of “VLA,” generic capability work without a responsible-deployment contribution, untraceable secondary sources, and duplicate or pre-rename versions of the same paper.

## 4. Add or Update Metadata

Edit `data/papers.json`; do not hand-edit generated README or documentation pages.

For every new or updated record:

- use a stable, unique `id`
- store the official title and first-author surname
- collect `first_submission_date` and `first_submission_source` as defined in `docs/metadata-schema.md`; use the arXiv v1 UTC date, never the revision, publication, or catalog-addition date
- use the confirmed venue and venue year; use `arXiv` when acceptance is unverified
- use a primary `paper_url` and only an official or author-maintained `code_url`
- assign one primary `section` and one valid `subsection`
- assign `risks` only for empirically evaluated outcomes
- use the controlled structured `threat_model` from `docs/taxonomy.md`
- audit secondary defense contributions regardless of primary section; add `defense` when the paper proposes or experimentally evaluates a substantive mitigation, and omit it after review when no such contribution exists
- exclude discussion-only recommendations, future-work suggestions, and survey coverage from `defense`
- keep experimental settings and secondary descriptors in `tags`
- set extension `curation_status` to the actual evidence depth

Never publish personal research questions, unpublished interpretations, private notes, local paths, or content from private research folders.

If a new section, subsection, or controlled value is genuinely required, update its validator and Japanese label in the same change. Do not leave translation warnings unresolved.

## 5. Regenerate and Validate

Verify each changed record by passing its ID explicitly:

```bash
python3 scripts/verify_bibliography.py --id <record-id-1> --id <record-id-2>
```

Then run:

```bash
python3 scripts/validate_catalog.py
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
python3 scripts/build_readme_ja.py
python3 scripts/build_readme_ja.py --check
python3 scripts/build_visualizations.py
python3 scripts/build_visualizations.py --check
python3 scripts/build_doc_pages.py
python3 scripts/build_doc_pages.py --check
python3 scripts/build_explorer.py
git diff --check
```

Bibliography verification is fail-closed. A title, first-author, year, initial-submission-date, identity, retrieval, or parsing failure blocks publication for that record. Do not treat an unavailable primary source as verified.

Review generated outputs for duplicate records, correct placement, working paper and code links, evidence-supported risks and threat metadata, matching English/Japanese counts, current visualizations, untranslated values, English-only public catalog fields, and absence of private information or local paths.

## 6. Commit and Push

The repository is publicly operated. Before pushing, confirm:

```bash
git remote -v
gh repo view futakw/Awesome-Physical-AI-Safety --json visibility
```

The expected repository is `futakw/Awesome-Physical-AI-Safety`, and visibility must be `PUBLIC`. Do not change repository visibility automatically.

Commit and push only when:

- every changed record passes primary-source bibliography verification
- catalog, README, documentation, visualization, explorer, and diff checks pass
- metadata identity and scope are certain
- no private or local information is present
- only changes belonging to the current work can be committed safely
- the remote and visibility are expected

Do not force-push, rewrite history, disable validation, discard unrelated changes, or publish around authentication, metadata, or primary-source failures. If safe isolation is not possible, leave the changes local and report the blocker.

If no verified new or materially revised record exists, leave the public repository unchanged and do not create a commit.

## 7. Report

Report:

- search date and coverage window
- new records and material revisions
- added or updated titles
- held or excluded candidates and reasons
- catalog count
- bibliography and validation results
- generated-output and translation status
- commit hash and push result, or the exact blocker

An empty update is valid when the search and its evidence are recorded.
