# Contributing

**English (this page)** | [Japanese](CONTRIBUTING.ja.md)

Thank you for helping improve Awesome Physical AI Safety.

For recurring LLM-assisted literature maintenance, follow the [daily curation workflow](docs/agent/daily-curation-workflow.md). The [documentation map](docs/reference/README.md) distinguishes reader documentation, agent runbooks, source templates, and generated Pages output.

## Add or Update a Paper

1. Edit `data/papers.json`.
2. Add one record with a stable ID, `catalogued_date` (the current UTC date), official title, first-author surname, venue, year, paper URL, and—when available—the official project or GitHub URL.
3. Assign one primary `section`, then a `subsection` chosen from that section's closed vocabulary (`SUBSECTIONS[section]` in `scripts/validate_catalog.py`) — reuse an existing value when the paper reasonably fits one; only add a new value when it genuinely doesn't, and add it to both `validate_catalog.py` and `scripts/labels_ja.py` in the same commit (see [the metadata schema](docs/reference/metadata-schema.md#subsection)).
4. Add empirically evaluated risk outcomes (or an empty `risks` list), a structured `threat_model`, and focused scientific descriptors only when structured metadata does not already express them.
5. Run:

```bash
python3 scripts/validate_catalog.py
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
python3 scripts/build_readme_ja.py
python3 scripts/build_readme_ja.py --check
python3 scripts/build_visualizations.py
python3 scripts/build_visualizations.py --check
python3 scripts/build_explorer.py
```

6. Commit the metadata change together with the generated `README.md` and `README.ja.md`.

## Display Rules

- Authors are displayed as `FirstAuthor et al.`; store the first author's surname in `first_author`.
- Use the official paper title and confirmed venue. The generated table links the title directly to `paper_url`; use `arXiv` when no accepted venue is confirmed.
- Set `catalogued_date` once, to the UTC date the record first enters the versioned catalog. Do not change it during later metadata, URL, title, or venue updates. This is distinct from `first_submission_date`; see [the metadata schema](docs/reference/metadata-schema.md#cataloguing-date).
- Set `year` to the confirmed venue's own proceedings/program year (from the official proceedings, DBLP, or the venue's acceptance page) — not the arXiv posting year. An arXiv preprint and its eventual conference appearance can fall in different calendar years; when a record's `venue` moves from `arXiv`/`OpenReview` to a named venue, update `year` to match at the same time. See [the metadata schema](docs/reference/metadata-schema.md#venue-and-year).
- Link only an official or author-maintained implementation as `code_url`.
- Leave `code_url` as `null` when no official repository is known.
- GitHub star badges and other project/code links are generated beside the paper title from `code_url`.
- Add a risk label only when the paper reports a corresponding empirical metric. Do not infer labels from motivation, discussion, threat potential, or the use of a physical robot alone. Use an empty `risks` list for surveys and papers without a matching outcome metric.
- Structure `threat_model` using the controlled `kind`, `lifecycle`, `mechanism`, `surface`, `target`, and `consequence` vocabularies defined in [the taxonomy](docs/reference/taxonomy.md), plus `curation_status` recording how the assignment was checked. `mechanism` is technique-oriented: assign only from the paper's method or experiments, never from the title alone, and use an empty list rather than an unsupported guess when no concrete technique is established. `target` is objective-oriented: assign from the paper's explicitly stated attack/defense/evaluation objective, not from `surface` (the delivery channel) or `consequence` (the result) — e.g. an attack delivered through a visual perturbation does not make `perception-model` the target unless perception accuracy is itself what is attacked or measured. For defenses, describe the threat being mitigated rather than the defense method.
- Use the `survey` or `evaluation` coverage variant when a record spans multiple independent threats and no single threat path is supported. `tags` is a duplicate-free list of scientific descriptors from `data/taxonomy/tags.json`; it may be empty when structured fields already capture the relevant information. Do not repeat values from `scope`, `risks`, `threat_model`, `evaluation`, `benchmark`, `defense`, `section`, `subsection`, `venue`, or `year`, or use tags for curation status and temporary audit work. Add a new descriptor to the registry in the same change as its first use after checking existing fields and tags. Put HOW failure modes such as `self-assessment-failure` in `threat_model.mechanism` or `coverage.mechanisms`, without duplicating them in `tags`. Put external survey citations that have no catalog record in `related_surveys` as HTTPS URLs. Secondary tags are not rendered as a separate table column.
- Add one catalog record and assign one primary section per paper. Generated thematic tables may display that same record as an additional view.
- Audit every paper for a secondary defense contribution regardless of its primary section. Add `defense` when the paper proposes or experimentally evaluates a substantive mitigation; omit it after review when no such contribution exists. Discussion-only recommendations and survey coverage do not qualify.

## Scope

The scope is physical-AI safety, security, robustness, privacy, ethical and societal outcomes, and trustworthy deployment. VLA is a major focus; robot-policy, autonomous-driving, and embodied-agent work is also in scope when it studies embodied behavior, physical interaction, or deployment-relevant risk. General-purpose LLM/VLM work needs an explicit physical-AI connection.

## Pull Requests

Keep each pull request focused. Explain why a new paper belongs in the selected section, which physical-AI system it studies, and what risk, mechanism, or evaluation principle it contributes.

## Licensing

Code contributions are under MIT; original catalog content contributions are under CC BY 4.0. Submit only material you have the right to contribute, and see [LICENSES.md](LICENSES.md) for the scope of each license.
