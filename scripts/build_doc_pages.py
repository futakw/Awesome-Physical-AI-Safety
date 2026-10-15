#!/usr/bin/env python3
"""Build self-contained rendered views of Markdown docs for the explorer."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES_URL = "https://futakw.github.io/Awesome-Physical-AI-Safety"

TEMPLATE = '''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{description}"><meta name="robots" content="index, follow"><link rel="canonical" href="{url}"><link rel="alternate" hreflang="{hreflang}" href="{url}"><link rel="alternate" hreflang="{alt_hreflang}" href="{alt_url}"><link rel="alternate" hreflang="x-default" href="{default_url}"><meta property="og:type" content="website"><meta property="og:site_name" content="Awesome Physical AI Safety"><meta property="og:locale" content="{og_locale}"><meta property="og:url" content="{url}"><meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{description}"><script type="application/ld+json">{jsonld}</script><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5.8.1/github-markdown.min.css"><style>body{{max-width:1100px;margin:32px auto;padding:0 22px;background:#fff}}.markdown-body{{font-size:15px}}</style></head><body><article id="content" class="markdown-body"></article><script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script><script>const source={source};document.getElementById('content').innerHTML=marked.parse(source);document.querySelectorAll('a').forEach(a=>{{a.target='_blank';a.rel='noopener noreferrer'}});</script></body></html>'''

EN_DESCRIPTION = (
    "A daily-updated, LLM-assisted bibliography of physical AI safety research: safety, "
    "security, robustness, and trustworthy deployment for vision-language-action (VLA) "
    "models, robots, autonomous systems, and embodied agents."
)
JA_DESCRIPTION = (
    "フィジカルAI（physical AI）の安全性に関する論文カタログ。VLA（Vision-Language-Action）・"
    "ロボット・自動運転・身体性AIエージェントの安全性、セキュリティ、堅牢性、信頼できる実運用について、"
    "毎日更新されるLLM支援のカタログです。"
)
# Keep this list curated to genuinely high-value search phrases that match the
# catalog's actual taxonomy (see MECHANISMS/SURFACES in validate_catalog.py) —
# add to it, don't just append every mechanism name (keyword stuffing hurts
# more than it helps).
EN_KEYWORDS = [
    "physical AI", "physical AI safety", "VLA safety", "vision-language-action models",
    "embodied AI safety", "robot security", "autonomous system security",
    "humanoid robot safety", "robot jailbreak", "prompt injection robot",
    "adversarial attacks on robots", "backdoor attack VLA", "data poisoning robot",
    "sensor spoofing", "trustworthy robotics", "AI safety benchmark",
]
JA_KEYWORDS = [
    "フィジカルAI", "フィジカルAI 安全性", "VLA 安全性", "Vision-Language-Action モデル",
    "身体性AI 安全性", "ロボット セキュリティ", "自律システム セキュリティ",
    "ヒューマノイド 安全性", "ロボット ジェイルブレイク", "プロンプトインジェクション ロボット",
    "敵対的攻撃 ロボット", "バックドア攻撃 VLA", "データ汚染 ロボット",
    "センサースプーフィング", "信頼できるロボティクス", "AI安全性ベンチマーク",
]

# (source, output, title, description, url, lang, og_locale, keywords)
PAGE_DEFS = [
    (ROOT / 'README.md', ROOT / 'docs' / 'readme.html', 'Awesome Physical AI Safety', EN_DESCRIPTION, f'{PAGES_URL}/readme.html', 'en', 'en_US', EN_KEYWORDS),
    (ROOT / 'README.ja.md', ROOT / 'docs' / 'readme.ja.html', 'Awesome Physical AI Safety (日本語)', JA_DESCRIPTION, f'{PAGES_URL}/readme.ja.html', 'ja', 'ja_JP', JA_KEYWORDS),
    (ROOT / 'docs' / 'taxonomy.md', ROOT / 'docs' / 'taxonomy.html', 'Taxonomy — Awesome Physical AI Safety', 'The failure-source, threat-model, and evaluated-risk taxonomy used to classify every paper in the Awesome Physical AI Safety catalog.', f'{PAGES_URL}/taxonomy.html', 'en', 'en_US', EN_KEYWORDS),
    (ROOT / 'docs' / 'taxonomy.ja.md', ROOT / 'docs' / 'taxonomy.ja.html', 'Taxonomy — Awesome Physical AI Safety (日本語)', 'Awesome Physical AI Safetyカタログで各論文を分類するための、失敗要因・脅威モデル・評価リスクの分類体系です。', f'{PAGES_URL}/taxonomy.ja.html', 'ja', 'ja_JP', JA_KEYWORDS),
]

PAGES_BY_SOURCE_NAME = {p[0].name: p for p in PAGE_DEFS}

# The EN/JA language-switcher line at the top of each source file links to its
# sibling .md file, which is correct on GitHub (renders natively) but 404s or
# opens raw Markdown from inside these generated pages. Point the switcher at
# the rendered sibling .html page instead, only in this generated output. The
# same pairing also drives the hreflang alternates below.
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
    for source, output, title, description, url, lang, og_locale, keywords in PAGE_DEFS:
        text = source.read_text(encoding='utf-8')
        if source.parent == ROOT:
            # GitHub Pages publishes docs/ only; use the mirrored SVGs there.
            text = text.replace('](assets/visualizations/', '](visualizations/').replace('](docs/', '](../docs/')
            text = text.replace('="assets/visualizations/', '="visualizations/')
            for filename in ('LICENSE', 'LICENSES.md', 'CONTRIBUTING.md', 'CONTRIBUTING.ja.md', 'CITATION.cff'):
                text = text.replace(f']({filename})', f'](../{filename})')
        md_target, html_target = SWITCHER_TARGETS[source.name]
        text = text.replace(f']({md_target})', f']({html_target})')
        alt_source_name, _ = SWITCHER_TARGETS[source.name]
        alt_page = PAGES_BY_SOURCE_NAME[alt_source_name]
        alt_url, alt_lang = alt_page[4], alt_page[5]
        default_url = url if lang == 'en' else alt_url
        jsonld = json.dumps({
            "@context": "https://schema.org",
            "@type": "Dataset",
            "name": title,
            "description": description,
            "url": url,
            "inLanguage": lang,
            "keywords": keywords,
            "isPartOf": {"@type": "Dataset", "name": "Awesome Physical AI Safety", "url": f"{PAGES_URL}/"},
            "sameAs": "https://github.com/futakw/Awesome-Physical-AI-Safety",
            "creator": {"@type": "Person", "name": "Futa Waseda"},
            "license": "https://github.com/futakw/Awesome-Physical-AI-Safety/blob/main/LICENSES.md",
        }, ensure_ascii=False)
        rendered = TEMPLATE.format(
            title=html.escape(title, quote=True),
            lang=lang,
            source=json.dumps(text),
            description=html.escape(description, quote=True),
            url=html.escape(url, quote=True),
            hreflang=lang,
            alt_hreflang=alt_lang,
            alt_url=html.escape(alt_url, quote=True),
            default_url=html.escape(default_url, quote=True),
            og_locale=og_locale,
            jsonld=jsonld,
        )
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
        print(f'Verified {len(PAGE_DEFS)} rendered documentation pages')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
