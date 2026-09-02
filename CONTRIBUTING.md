# Contributing

Thank you for helping improve Awesome Responsible VLA.

## Add or Update a Paper

1. Edit `data/papers.json`.
2. Add one record with a stable ID, official title, first-author surname, venue, year, paper URL, and—when available—the official project or GitHub URL.
3. Assign one primary `section` and `subsection`.
4. Add one or more risk outcomes and focused mechanism or OOD tags.
5. Run:

```bash
python3 scripts/validate_catalog.py
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
```

6. Commit both the metadata change and the generated `README.md`.

## Display Rules

- Authors are displayed as `FirstAuthor et al.`; store the first author's surname in `first_author`.
- Use the official paper title and confirmed venue. Use `arXiv` when no accepted venue is confirmed.
- Link only an official or author-maintained implementation as `code_url`.
- Leave `code_url` as `null` when no official repository is known.
- GitHub star badges are generated automatically from valid GitHub repository URLs.
- List a paper once. Express cross-cutting properties through `risks` and `tags`.

## Scope

The core scope is Responsible VLA. Adjacent embodied-agent, autonomous-driving, and robot-policy work is accepted only when it contributes a directly transferable risk, threat, defense, or evaluation principle.

## Pull Requests

Keep each pull request focused. Explain why a new paper belongs in the selected section and identify whether it is core VLA work or adjacent embodied-agent work.

