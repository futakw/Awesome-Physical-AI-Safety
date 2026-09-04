# Daily Curation Workflow

This document defines the maintenance workflow for incorporating newly discovered literature into Awesome Responsible VLA. The catalog should remain reproducible, evidence-coded, English-only, and safe for eventual public release.

## 1. Search and Verify

1. Search primary sources for new papers and material revisions in Responsible VLA, embodied-agent safety, physical AI security, robustness, OOD generalization, attacks, defenses, privacy, failure detection, and safety evaluation.
2. Prefer arXiv, OpenReview, official proceedings, author project pages, and official repositories.
3. Confirm the official title, first author, publication year, venue, paper URL, and official project or code URL.
4. Check `data/papers.json` by normalized title, paper URL, arXiv ID, DOI, and known title changes before adding a record.
5. Update an existing record for a material revision or renamed paper. Do not create a second entry for the same work.

## 2. Decide Scope

Include work that directly contributes at least one of the following:

- VLA safety, robustness, security, privacy, misuse, or trustworthy evaluation
- transferable embodied-agent or robot-policy failure analysis
- adversarial or non-adversarial/OOD evaluation relevant to perception-decision-action loops
- runtime monitoring, guardrails, action shielding, fail-safe behavior, recovery, or uncertainty handling
- a survey or benchmark that materially organizes Responsible VLA research

Exclude unrelated uses of the acronym VLA, generic capability papers without a responsible-deployment connection, secondary articles without a traceable primary source, and exact duplicates.

## 3. Add Catalog Metadata

Add or update records only in `data/papers.json`. Follow [the taxonomy](taxonomy.md) and [the contribution rules](../CONTRIBUTING.md).

For each record:

- use a stable, unique `id`
- store the official title and first-author surname
- use the confirmed venue, or `arXiv` when acceptance is unverified
- link the title to the primary paper source through `paper_url`
- use `code_url` only for an official or author-maintained repository or project page
- assign one primary section and subsection
- assign `risks` only from outcomes empirically measured in the paper
- write a compact `threat_model` in `Category (primary mechanism or shift)` form
- keep experimental settings and secondary descriptors in `tags`

Do not add private research questions, unpublished interpretations, personal work notes, local paths, or content from private research folders.

## 4. Regenerate and Validate

Run all checks from the repository root:

```bash
python3 scripts/validate_catalog.py
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
python3 scripts/build_visualizations.py
python3 scripts/build_visualizations.py --check
python3 scripts/build_explorer.py
git diff --check
```

Review the generated README and confirm:

- the paper appears once in the correct subsection
- the table title links to the paper
- an official code or project link appears beside the title when available
- Risk and Threat Model remain compact and evidence-consistent
- the table of contents includes any new subsection
- the total paper count is correct
- the generated landscape figures are current
- no private marker, local path, CJK text, or personal research content is present

## 5. Commit and Push

Before pushing, verify that the remote repository is still private whenever private maintenance is intended. Commit `data/papers.json` together with the generated `README.md`. Use a concise maintenance commit message, then push the current branch.

If validation fails, metadata is uncertain, the remote is unexpectedly public, or unrelated local changes are present, do not push. Record the unresolved item in the daily research report instead.

## 6. Daily Report

Report only the operational result:

- search date and coverage window
- number of new papers and updated records
- titles of newly added papers
- uncertain or excluded candidates and the reason
- catalog count after validation
- validation result
- commit hash and push result, or the exact blocker

An empty update is valid. If no verified new paper is found, leave the catalog unchanged and report the searched sources and date range.
