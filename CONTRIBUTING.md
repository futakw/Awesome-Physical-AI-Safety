# Contributing

**English (this page)** | [Japanese](CONTRIBUTING.ja.md)

Thank you for helping improve Awesome Physical AI Safety.

For recurring literature maintenance, follow the [daily curation workflow](docs/daily-curation-workflow.md).

## Add or Update a Paper

1. Edit `data/papers.json`.
2. Add one record with a stable ID, official title, first-author surname, venue, year, paper URL, and—when available—the official project or GitHub URL.
3. Assign one primary `section` and `subsection`.
4. Add empirically evaluated risk outcomes (or an empty `risks` list), a structured `threat_model`, and focused mechanism or OOD tags.
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
- Set `year` to the confirmed venue's own proceedings/program year (from the official proceedings, DBLP, or the venue's acceptance page) — not the arXiv posting year. An arXiv preprint and its eventual conference appearance can fall in different calendar years; when a record's `venue` moves from `arXiv`/`OpenReview` to a named venue, update `year` to match at the same time. See [the metadata schema](docs/metadata-schema.md#venue-and-year).
- Link only an official or author-maintained implementation as `code_url`.
- Leave `code_url` as `null` when no official repository is known.
- GitHub star badges and other project/code links are generated beside the paper title from `code_url`.
- Add a risk label only when the paper reports a corresponding empirical metric. Do not infer labels from motivation, discussion, threat potential, or the use of a physical robot alone. Use an empty `risks` list for surveys and papers without a matching outcome metric.
- Structure `threat_model` using the controlled `kind`, `lifecycle`, `mechanism`, `surface`, `target`, and `consequence` vocabularies defined in [the taxonomy](docs/taxonomy.md). For defenses, describe the threat being mitigated rather than the defense method.
- Use the `survey` or `evaluation` coverage variant when a record spans multiple independent threats and no single threat path is supported. Experimental settings and secondary descriptors belong in `tags`; tags remain structured metadata and are not rendered as a separate table column.
- Add one catalog record and assign one primary section per paper. Generated thematic tables may display that same record as an additional view.

## Scope

The scope is physical-AI safety, security, robustness, privacy, ethical and societal outcomes, and trustworthy deployment. VLA is a major focus; robot-policy, autonomous-driving, and embodied-agent work is also in scope when it studies embodied behavior, physical interaction, or deployment-relevant risk. General-purpose LLM/VLM work needs an explicit physical-AI connection.

## Pull Requests

Keep each pull request focused. Explain why a new paper belongs in the selected section, which physical-AI system it studies, and what risk, mechanism, or evaluation principle it contributes.

## Licensing

Code contributions are under MIT; original catalog content contributions are under CC BY 4.0. Submit only material you have the right to contribute, and see [LICENSES.md](LICENSES.md) for the scope of each license.
