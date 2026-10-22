# Bounded Biweekly Metadata Maintenance

**Audience:** periodic maintainers of already-cataloged papers. Preserve the existing biweekly schedule. New-paper admission belongs to the [scout](daily-curation-workflow.md).

## Start and select

Use the same external queue and whole-run guard as the scout; see [curation-queue.md](curation-queue.md). Inspect/fetch the expected remote before editing and preserve unrelated changes. Load only the catalog index, compact memory and relevant workflow/schema/taxonomy sections.

Process only lane `maintenance`, FIFO, at most **20 claimed records** per run including held/rejected/unchanged results. A concrete signal is required: changed source version, specific acceptance/publication or official code-release evidence, a reported correction, or validator-detected inconsistency. An unconfirmed venue, null code URL, recent addition or elapsed time alone never selects a record. Carry forward specific known unresolved evidence issues; do not enqueue all unconfirmed venues or missing-code records. Do not discover/admit new papers.

## Targeted review

Use `scripts/paper_cache.py get <id>` first; no recurring full-cache refresh. Follow the source-title/identifier verification procedure in the scout workflow for new cache content. Read only the passages necessary for the signaled field, including methods/results/limitations when an actual content revision changes a retained classification. Do not re-summarize the full paper or follow unrelated citations.

- Confirm a venue from official acceptance/proceedings/publisher evidence; update venue and venue year together. Author claims alone do not establish acceptance.
- Update an official project/code URL only with specific author-maintained evidence and reachability. Do not routinely crawl existing URLs or retry known 404s without a restoration/release signal.
- Correct title, identity, risks, threat model or minimal secondary defense only when new evidence or a concrete inconsistency warrants it. No blanket mechanism/target reclassification.
- Apply the narrowed Physical AI scope and indispensable-only taxonomy rule. Do not remove existing historical records as a side effect.
- Do not collect, backfill or refresh `evaluation`, `benchmark`, or legacy defense position/protected_surface/assumptions. Preserve existing values; collect only common retained fields and defense mechanism/defends_against/curation_status.
- If a claim cannot be established, preserve current metadata and hold with a reason. Reopen a hold only when evidence changes. Resolve `updated` only after successful publication; failures leave proposed work pending. Use `unchanged` when the signaled update was checked and requires no change.

## Verification and publication

**Do not run a full-catalog network bibliography audit.** Verify changed records by explicit IDs only. Full bibliography rereads, link sweeps and reclassification require a separate explicit request, not this recurring task.

Cheap catalog-wide mechanical validators remain publication gates and may enqueue concrete inconsistencies without rereading every paper. Preserve the null-defense prohibition. If an existing invalid record blocks validation, do not bypass it to publish unrelated changes.

For actual changes, execute the scout's complete fail-closed generation, test, leakage, remote/PUBLIC, commit and push gates once changes settle. If no metadata changed, do not regenerate, verify unchanged bibliography or create a commit. Do not perform research synthesis or synchronize unrelated historical notes.

## Every exit reports both queue lanes

On success, no change, lock contention or failure, report reviewed N/20, additions/updates/holds/exclusions; remaining new and maintenance counts, each split pending/held; and their combined total from the final snapshot. Unreadable state is unknown, never zero. Include changed-record bibliography and publication status or the exact blocker. Use the same counts in the timestamped archive block; never duplicate full paper summaries or queue contents in memory. Do not change notification settings.
