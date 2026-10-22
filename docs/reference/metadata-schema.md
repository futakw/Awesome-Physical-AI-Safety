# Type-Specific Metadata Pilot

Recurring curation collects common bibliographic and classification fields, `risks`, the structured `threat_model`, and a minimal `defense` object when a substantive mitigation is established.

- `defense` requires only `mechanism`, `defends_against`, and `curation_status`, which support the public Defense × Threat view. Its absence after review means no substantive mitigation was established. Never publish `defense: null`.
- `position`, `protected_surface`, and `assumptions` remain optional legacy defense fields. Validate them when present, preserve existing values, and do not collect or backfill them during recurring runs.
- `evaluation` and `benchmark` are legacy extensions: retain and validate existing objects, but do not collect, backfill, or refresh them in either recurring workflow. Their absence means not collected, not audited non-applicability. Do not create empty objects or null placeholders to simulate a review.
- Do not remove existing detailed metadata as part of this policy change. The validator accepts both minimal and complete legacy defense objects.

Primary empirical results must still be inspected when assigning risk outcomes; stopping metric-list collection does not relax the evidence requirement. `threat_model.curation_status` and `defense.curation_status` record actual evidence depth (`paper-verified`, `abstract-verified`, `catalog-derived`, or `reference-only`). Reading targeted methods, experiments, and limitations is sufficient for paper-level verification of those fields; do not claim an exhaustive full-paper review.

Controlled values remain in `data/taxonomy/`. The optional extension contract is in `paper-extensions.schema.json`; `scripts/validate_catalog.py` enforces controlled values. Existing evaluation objects continue to store environments, named models/platforms, access, metrics and physical validation, and existing benchmark objects retain their original dimensions and availability. Neither extension is needed by current public views.

## Secondary tags

`tags` is a list of unique scientific descriptors registered in [`data/taxonomy/tags.json`](../../data/taxonomy/tags.json). An empty list is valid when all useful descriptors are represented by structured fields. The validator rejects unregistered values, duplicates, and non-string entries. Do not use tags for values already captured by `scope`, `risks`, `threat_model`, `evaluation`, `benchmark`, `defense`, `section`, `subsection`, `venue`, or `year`, or for curation status, temporary audit work, or source references. Add a genuinely new scientific descriptor to the registry in the same change that first uses it, after checking that no structured field or existing tag expresses the same meaning. Defined HOW failure modes, including `self-assessment-failure`, belong in `threat_model.mechanism` or broad-evaluation `coverage.mechanisms`, rather than duplicate `tags` entries. External survey citations belong in optional `related_surveys`, an array of unique HTTPS URLs to survey records not represented in this catalog. See the [taxonomy rules](taxonomy.md#controlled-secondary-tags).

## Venue and year

`venue` and `year` together describe where and when the work was published, not
when it first appeared online. `year` is the year of the stated `venue`:

- If `venue` is a named conference or journal (e.g. `CVPR`, `ICCV`, `NeurIPS`),
  `year` is that venue's own year — the year printed on its proceedings or
  program, confirmed from the official proceedings page, DBLP, or the venue's
  acceptance notification, never inferred from the arXiv post date.
- If `venue` is `arXiv` or `OpenReview` (acceptance unverified), `year` is the
  year of the cited arXiv/OpenReview version.

An arXiv preprint and its eventual conference appearance routinely fall in
different calendar years (e.g. posted to arXiv in 2025, accepted at CVPR
2026); `year` must track the confirmed venue, not the preprint. Whenever a
record's `venue` is changed away from `arXiv`/`OpenReview` to a named
venue — including updating an existing record once a preprint is accepted —
re-derive `year` from that venue's own listing; do not carry over the old
arXiv-based year.

## Venue ranking

Venue-ranking metadata is maintained separately in [`data/venue_ranks.json`](../../data/venue_ranks.json), rather than duplicated in each paper record. The table follows the official ICORE/CORE conference taxonomy and is used by the Explorer's venue-rank filter. See [`venue-rankings.md`](venue-rankings.md) for the scope, normalization, and non-inheritance rules.

## Subsection

`subsection` is a closed vocabulary scoped per `section`, enforced by
`scripts/validate_catalog.py`'s `SUBSECTIONS` dict (one allowed set of values
per `section`, mirroring how `SECTIONS`, `RISKS`, and the `threat_model`
fields are enforced). It is not free text and not a per-paper judgment call:
every record's `subsection` must already appear in that section's set.

When adding or updating a record:

- Check `SUBSECTIONS[section]` in `scripts/validate_catalog.py` first and
  reuse an existing value whenever the paper reasonably fits one — do not
  invent a new label just because the existing wording doesn't match
  perfectly.
- Only add a new subsection value when the paper genuinely doesn't fit any
  existing one for that section. Adding one requires, in the same commit:
  adding it to `SUBSECTIONS[section]` in `scripts/validate_catalog.py`, and
  adding its Japanese translation to `SUBSECTIONS_JA` in
  `scripts/labels_ja.py` (`validate_catalog.py` rejects the record otherwise,
  and `scripts/build_readme_ja.py` prints a `WARNING` for any untranslated
  value).
- Before adding a new value, consider whether it duplicates an existing one
  in spirit (e.g. a slightly different phrasing of an already-covered topic)
  — subsections exist to group papers for browsing, so near-duplicates
  undermine that rather than improving precision.
- The same subsection name may legitimately exist under more than one
  `section` (e.g. "Failure Detection and Recovery" under both `defenses` and
  `benchmarks`) — these describe the same topic approached as different
  contribution types and are not duplicates of each other.

## Initial submission metadata

Every record contains `first_submission_date` (ISO `YYYY-MM-DD`, or `null`) and
`first_submission_source` (official evidence URL, or `null`). Both are null when
unverified. The date is the earliest verified submission of this same work,
not catalog addition, latest revision, acceptance, or proceedings publication.
For arXiv use the UTC date of `[v1]` in Submission history. Keep `year` unchanged:
it serves a separate bibliographic purpose. A later version or retitling must
not reset the initial date. For other sources, do not substitute publication
or generic record-creation dates for submission dates.

The current machine verifier supports arXiv v1 histories. Other sources remain
null until their submission semantics and an appropriate verifier are established.
Missing dates are excluded from submission-date charts and counted explicitly.
`verify_bibliography.py` checks every populated date against its evidence source;
a missing or mismatched source date fails verification. The focused command
`python3 scripts/verify_submission_dates.py` checks all populated dates without
claiming that other bibliographic fields passed.

## Cataloguing date

Every record contains `catalogued_date` as a non-null ISO `YYYY-MM-DD` string.
It records the UTC date on which that record first entered the versioned catalog,
not the paper's submission, revision, acceptance, or publication date. Set it
when adding a record and never change it when updating metadata, replacing a
URL, recording a venue, or retitling the same work in place.

The landing page's **Recently catalogued** list sorts by this field. Records
sharing a date use their catalog order as the tie-breaker, with later records
shown first. The initial migration derives historical values from the UTC date
of the first Git commit whose `data/papers.json` contains each stable record ID.
`first_submission_date` remains separate and continues to drive the submission
timeline.
