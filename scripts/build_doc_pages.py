#!/usr/bin/env python3
"""Build self-contained rendered views of Markdown docs for the explorer."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEMPLATE = '''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5.8.1/github-markdown.min.css"><style>body{{max-width:1100px;margin:32px auto;padding:0 22px;background:#fff}}.markdown-body{{font-size:15px}}</style></head><body><article id="content" class="markdown-body"></article><script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script><script>const source={source};document.getElementById('content').innerHTML=marked.parse(source);document.querySelectorAll('a').forEach(a=>{{a.target='_blank';a.rel='noopener noreferrer'}});</script></body></html>'''

PAGES = [
    (ROOT / 'README.md', ROOT / 'docs' / 'readme.html', 'Awesome Physical AI Safety'),
    (ROOT / 'README.ja.md', ROOT / 'docs' / 'readme.ja.html', 'Awesome Physical AI Safety (日本語)'),
    (ROOT / 'docs' / 'taxonomy.md', ROOT / 'docs' / 'taxonomy.html', 'Taxonomy'),
    (ROOT / 'docs' / 'taxonomy.ja.md', ROOT / 'docs' / 'taxonomy.ja.html', 'Taxonomy (日本語)'),
]

# The EN/JA language-switcher line at the top of each source file links to its
# sibling .md file, which is correct on GitHub (renders natively) but 404s or
# opens raw Markdown from inside these generated pages. Point the switcher at
# the rendered sibling .html page instead, only in this generated output.
SWITCHER_TARGETS = {
    'README.md': ('README.ja.md', 'readme.ja.html'),
    'README.ja.md': ('README.md', 'readme.html'),
    'taxonomy.md': ('taxonomy.ja.md', 'taxonomy.ja.html'),
    'taxonomy.ja.md': ('taxonomy.md', 'taxonomy.html'),
}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Fail if rendered documentation is stale')
    args = parser.parse_args()
    stale = []
    for source, output, title in PAGES:
        text = source.read_text(encoding='utf-8')
        if source.parent == ROOT:
            # GitHub Pages publishes docs/ only; use the mirrored SVGs there.
            text = text.replace('](assets/visualizations/', '](visualizations/').replace('](docs/', '](../docs/')
            text = text.replace('="assets/visualizations/', '="visualizations/')
            for filename in ('LICENSE', 'LICENSES.md', 'CONTRIBUTING.md', 'CONTRIBUTING.ja.md', 'CITATION.cff'):
                text = text.replace(f']({filename})', f'](../{filename})')
        md_target, html_target = SWITCHER_TARGETS[source.name]
        text = text.replace(f']({md_target})', f']({html_target})')
        lang = 'ja' if source.name.endswith('.ja.md') else 'en'
        rendered = TEMPLATE.format(title=title, lang=lang, source=json.dumps(text))
        if args.check:
            if not output.exists() or output.read_text(encoding='utf-8') != rendered:
                stale.append(output.relative_to(ROOT))
        else:
            output.write_text(rendered, encoding='utf-8')
            print(f'Generated {output.name}')
    if stale:
        print('Generated documentation is stale:')
        for path in stale:
            print(f'- {path}')
        return 1
    if args.check:
        print(f'Verified {len(PAGES)} rendered documentation pages')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
