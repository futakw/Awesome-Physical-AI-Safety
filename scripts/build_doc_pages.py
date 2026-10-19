#!/usr/bin/env python3
"""Build self-contained rendered views of Markdown docs for the explorer."""
import argparse
import html
import json
import re
from urllib.parse import urlsplit
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES_URL = "https://futakw.github.io/Awesome-Physical-AI-Safety"

DOC_STYLE = '''
  :root {
    color-scheme: light; --bg:#EEF1F3; --surface:#FFFFFF; --surface-2:#F4F6F8;
    --ink:#14171C; --muted:#5B6672; --ink-faint:#8A93A0; --line:#D8DEE3; --line-strong:#C2C9D1;
    --accent:#CC5200; --accent-ink:#FFFFFF; --signal:#0E7490; --signal-soft:#D7EEF2;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      color-scheme: dark; --bg:#0B0D10; --surface:#14171C; --surface-2:#1B1F26;
      --ink:#ECEFF2; --muted:#9AA7B4; --ink-faint:#6B7682; --line:#262B33; --line-strong:#333A44;
      --accent:#FF7A33; --accent-ink:#1B0D03; --signal:#4FD6E8; --signal-soft:#122C31;
    }
  }
  * { box-sizing:border-box; }
  body { max-width:900px; margin:0 auto; padding:40px 24px 72px; background:var(--bg); color:var(--ink); font:15px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }
  .markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4 { font-weight:800; letter-spacing:-.015em; line-height:1.25; margin:1.6em 0 .6em; }
  .markdown-body h1 { font-size:28px; padding-bottom:.4em; border-bottom:1px solid var(--line); }
  .markdown-body h2 { font-size:21px; padding-bottom:.35em; border-bottom:1px solid var(--line); }
  .markdown-body h3 { font-size:16.5px; }
  .markdown-body h1:first-child { margin-top:0; }
  .markdown-body p,.markdown-body li { font-size:15px; }
  .markdown-body p { margin:.8em 0; }
  .markdown-body a { color:var(--signal); text-decoration:none; }
  .markdown-body a:hover { text-decoration:underline; }
  .markdown-body strong { font-weight:700; }
  .markdown-body ul,.markdown-body ol { padding-left:1.4em; }
  .markdown-body li + li { margin-top:.25em; }
  .markdown-body code { font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.9em; background:var(--surface-2); border:1px solid var(--line); border-radius:4px; padding:.12em .4em; }
  .markdown-body pre { background:var(--surface-2); border:1px solid var(--line); border-radius:8px; padding:14px 16px; overflow:auto; }
  .markdown-body pre code { background:none; border:none; padding:0; }
  .markdown-body blockquote { margin:1em 0; padding:.2em 1em; border-left:3px solid var(--line-strong); color:var(--muted); }
  .markdown-body hr { border:none; border-top:1px solid var(--line); margin:2em 0; }
  .markdown-body img { max-width:100%; border-radius:8px; }
  .markdown-body table { width:100%; border-collapse:collapse; margin:1em 0; font-size:13.5px; display:block; overflow:auto; }
  .markdown-body th,.markdown-body td { padding:8px 12px; border:1px solid var(--line); text-align:left; vertical-align:top; }
  .markdown-body th { background:var(--surface-2); color:var(--muted); font-size:11.5px; text-transform:uppercase; letter-spacing:.02em; }
  .markdown-body tr:nth-child(even) td { background:var(--surface-2); }
'''

TEMPLATE = '''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="favicon.svg" type="image/svg+xml" sizes="any"><title>{title}</title><meta name="description" content="{description}"><meta name="robots" content="index, follow"><link rel="canonical" href="{url}"><link rel="alternate" hreflang="{hreflang}" href="{url}"><link rel="alternate" hreflang="{alt_hreflang}" href="{alt_url}"><link rel="alternate" hreflang="x-default" href="{default_url}"><meta property="og:type" content="website"><meta property="og:site_name" content="Awesome Physical AI Safety"><meta property="og:locale" content="{og_locale}"><meta property="og:url" content="{url}"><meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{description}"><script type="application/ld+json">{jsonld}</script><style>''' + DOC_STYLE.replace('{', '{{').replace('}', '}}') + '''</style></head><body><article id="content" class="markdown-body"></article><script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script><script src="https://cdn.jsdelivr.net/npm/marked-gfm-heading-id@3.2.0/lib/index.umd.min.js"></script><script>marked.use(markedGfmHeadingId.gfmHeadingId());const source={source};document.getElementById('content').innerHTML=marked.parse(source);document.querySelectorAll('a').forEach(a=>{{a.target='_blank';a.rel='noopener noreferrer'}});if(location.hash){{requestAnimationFrame(()=>document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView());}}</script></body></html>'''

EN_DESCRIPTION = (
    "A daily-updated, LLM-assisted catalog of physical AI and embodied AI safety research "
    "on VLA models, robots, and autonomous systems, covering security, robustness, and "
    "trustworthy deployment."
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
    (ROOT / 'docs' / 'public' / 'taxonomy.md', ROOT / 'docs' / 'taxonomy.html', 'Taxonomy — Awesome Physical AI Safety', 'A reader-friendly guide to the six axes used to organize Physical AI Safety research.', f'{PAGES_URL}/taxonomy.html', 'en', 'en_US', EN_KEYWORDS),
    (ROOT / 'docs' / 'public' / 'taxonomy.ja.md', ROOT / 'docs' / 'taxonomy.ja.html', 'Taxonomy — Awesome Physical AI Safety (日本語)', 'Physical AI Safety研究を整理する6つの軸を、読者向けに簡潔に説明します。', f'{PAGES_URL}/taxonomy.ja.html', 'ja', 'ja_JP', JA_KEYWORDS),
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

def rewrite_links(text: str, source: Path) -> str:
    """Resolve repository links from the source location, not the Pages root."""
    md_target, html_target = SWITCHER_TARGETS[source.name]
    text = text.replace(f']({md_target})', f']({html_target})')

    def destination(url: str) -> str:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path or parts.path.startswith('/'):
            return url
        if parts.path in {html_target, 'readme.html', 'readme.ja.html', 'taxonomy.html', 'taxonomy.ja.html'}:
            return url
        target = (source.parent / parts.path).resolve()
        try:
            relative = target.relative_to(ROOT).as_posix()
        except ValueError:
            return url
        suffix = ('?' + parts.query if parts.query else '') + ('#' + parts.fragment if parts.fragment else '')
        # Images and charts are mirrored in the Pages publication directory.
        for prefix in ('assets/visualizations/', 'docs/visualizations/'):
            if relative.startswith(prefix):
                return 'visualizations/' + relative[len(prefix):] + suffix
        # Contributor Markdown and repository-level files are read on GitHub.
        return 'https://github.com/futakw/Awesome-Physical-AI-Safety/blob/main/' + relative + suffix

    text = re.sub(r'(\]\()([^\s)]+)(\))', lambda m: m[1] + destination(m[2]) + m[3], text)
    return re.sub(r'((?:href|src)=")([^"]+)(")', lambda m: m[1] + destination(m[2]) + m[3], text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Fail if rendered documentation is stale')
    args = parser.parse_args()
    stale = []
    for source, output, title, description, url, lang, og_locale, keywords in PAGE_DEFS:
        text = source.read_text(encoding='utf-8')
        text = rewrite_links(text, source)
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
