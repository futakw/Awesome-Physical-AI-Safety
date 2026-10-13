#!/usr/bin/env python3
"""Build self-contained rendered views of Markdown docs for the explorer."""
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

for source, output, title in PAGES:
    text = source.read_text(encoding='utf-8')
    if source.parent == ROOT:
        # The rendered page lives under docs/, so adjust repository-root links.
        text = text.replace('](assets/', '](../assets/').replace('](docs/', '](../docs/')
        for filename in ('LICENSE', 'LICENSES.md', 'CONTRIBUTING.md', 'CONTRIBUTING.ja.md', 'CITATION.cff'):
            text = text.replace(f']({filename})', f'](../{filename})')
    lang = 'ja' if source.name.endswith('.ja.md') else 'en'
    output.write_text(TEMPLATE.format(title=title, lang=lang, source=json.dumps(text)), encoding='utf-8')
    print(f'Generated {output.name}')
