#!/usr/bin/env python3
"""Build self-contained rendered views of Markdown docs for the explorer."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEMPLATE = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5.8.1/github-markdown.min.css"><style>body{{max-width:1100px;margin:32px auto;padding:0 22px;background:#fff}}.markdown-body{{font-size:15px}}</style></head><body><article id="content" class="markdown-body"></article><script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script><script>const source={source};document.getElementById('content').innerHTML=marked.parse(source);document.querySelectorAll('a').forEach(a=>{{a.target='_blank';a.rel='noopener noreferrer'}});</script></body></html>'''

for source, output, title in [(ROOT/'README.md', ROOT/'docs'/'readme.html', 'Awesome Physical AI Safety'), (ROOT/'docs'/'taxonomy.md', ROOT/'docs'/'taxonomy.html', 'Taxonomy')]:
    text = source.read_text(encoding='utf-8')
    if source.name == 'README.md':
        # The rendered page lives under docs/, so adjust repository-root links.
        text = text.replace('](assets/', '](../assets/').replace('](docs/', '](../docs/')
    output.write_text(TEMPLATE.format(title=title, source=json.dumps(text)), encoding='utf-8')
    print(f'Generated {output.name}')
