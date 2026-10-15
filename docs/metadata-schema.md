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

`abstract-verified` is also supported for defense and benchmark extensions when the primary abstract establishes the method or evaluation scope but the full paper has not been audited. Unmentioned metrics, platforms, models, and artifact availability are left empty or null rather than inferred.

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
