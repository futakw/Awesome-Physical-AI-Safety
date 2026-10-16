#!/usr/bin/env python3
"""Generate README.ja.md: a full Japanese mirror of README.md.

Paper titles, author surnames, venue names, and raw taxonomy vocabulary
*values* (the data/papers.json strings like `adversarial-patch`) are never
translated — they are bibliographic/controlled data. Only display labels
(section/subsection headings, badge text, UI strings) are translated, via the
dictionaries in labels_ja.py. Any value missing from those dictionaries falls
back to the English display label automatically, so new taxonomy values or
subsections added by daily curation degrade gracefully instead of breaking
the build.
"""

from __future__ import annotations

import argparse
import json
from html import escape

from build_readme import (
    DATA_PATH,
    PAGES_URL,
    RISK_COLORS,
    ROOT,
    SECTIONS,
    THREAT_COLORS,
    badge,
    display_label,
    github_repo,
    subsection_anchor,
)
from labels_ja import (
    CONSEQUENCE_JA,
    DISPLAY_LABELS_JA,
    KIND_JA,
    LIFECYCLE_JA,
    MECHANISM_JA,
    RISK_LABELS_JA,
    SECTIONS_JA,
    SUBSECTIONS_JA,
    SURFACE_JA,
    TARGET_JA,
)

README_JA_PATH = ROOT / "README.ja.md"


def label_ja(value: str) -> str:
    return DISPLAY_LABELS_JA.get(value, display_label(value))


def section_title_ja(key: str) -> str:
    return SECTIONS_JA.get(key, SECTIONS[key][1])


def subsection_title_ja(name: str) -> str:
    return SUBSECTIONS_JA.get(name, name)


def primary_label_ja(values: list[str]) -> str:
    label = label_ja(values[0])
    return f"{label} +{len(values) - 1}" if len(values) > 1 else label


def risk_cell_ja(risks: list[str]) -> str:
    if not risks:
        return "—"
    return " ".join(
        badge(RISK_LABELS_JA.get(risk, risk), RISK_COLORS[risk]) for risk in risks
    )


def threat_model_cell_ja(threat_model: dict) -> str:
    kind = threat_model["kind"]
    if kind in {"survey", "evaluation"}:
        coverage = threat_model["coverage"]
        lifecycles = coverage["lifecycles"]
        lifecycle = (
            "複数ライフサイクル"
            if len(lifecycles) > 2
            else " → ".join(LIFECYCLE_JA.get(v, v) for v in lifecycles)
        )
        surfaces = coverage["surfaces"]
        surface = (
            "複数サーフェス"
            if len(surfaces) > 2
            else " + ".join(SURFACE_JA.get(v, v) for v in surfaces)
        )
        kind_label = KIND_JA.get(kind, kind)
        return " ".join(
            [
                badge(lifecycle, THREAT_COLORS["lifecycle"]),
                badge(surface, THREAT_COLORS["surface"]),
                "<br>",
                badge(f"{kind_label}カバレッジ", THREAT_COLORS[kind]),
            ]
        )
    lifecycle = " → ".join(LIFECYCLE_JA.get(v, v) for v in threat_model["lifecycle"])
    surface = primary_label_ja(threat_model["surface"])
    mechanism_values = threat_model["mechanism"]
    mechanism_label = MECHANISM_JA.get(mechanism_values[0], mechanism_values[0])
    mechanism = (
        f"{mechanism_label} +{len(mechanism_values) - 1}"
        if len(mechanism_values) > 1
        else mechanism_label
    )
    target = TARGET_JA.get(threat_model["target"][0], threat_model["target"][0])
    consequence = CONSEQUENCE_JA.get(
        threat_model["consequence"][0], threat_model["consequence"][0]
    )
    return " ".join(
        [
            badge(lifecycle, THREAT_COLORS["lifecycle"]),
            badge(surface, THREAT_COLORS["surface"]),
            "<br>",
            badge(mechanism, THREAT_COLORS["mechanism"]),
            "&nbsp;→&nbsp;",
            badge(target, THREAT_COLORS["target"]),
            "&nbsp;→&nbsp;",
            badge(consequence, THREAT_COLORS["consequence"]),
        ]
    )


def paper_cell(paper: dict) -> str:
    title = paper["title"].replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")
    paper_url = paper.get("paper_url")
    parts = [f"**[{title}]({paper_url})**" if paper_url else f"**{title}**"]
    code_url = paper.get("code_url")
    repo = github_repo(code_url)
    if repo:
        stars_badge = f"https://img.shields.io/github/stars/{repo}?style=social"
        parts.append(f"[![GitHub stars]({stars_badge})]({code_url})")
    elif code_url:
        parts.append(f"[Project / Code]({code_url})")
    author = paper["first_author"]
    author_label = author if author.lower().endswith("et al.") else f"{author} et al."
    return " ".join(parts) + f"<br><sub>{author_label}</sub>"


def render_overview(paper_count: int) -> list[str]:
    return [
        "# Awesome Physical AI Safety",
        "",
        "[English](README.md) | **日本語（このページ）**",
        "",
        "**🤖 VLA・ロボット・自動運転・身体性AIエージェントにおける安全性、セキュリティ、堅牢性、倫理的・社会的リスク、信頼できる実運用に関する、LLM支援の文献カタログです。**",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)",
        "[![Cite this repository](https://img.shields.io/badge/Cite-CITATION.cff-blue.svg)](CITATION.cff)",
        "[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23348593.svg)](https://doi.org/10.5281/zenodo.23348593)",
        "[![LLM-assisted](https://img.shields.io/badge/curation-%F0%9F%A4%96%20LLM--assisted-critical.svg)](docs/agent/daily-curation-workflow.md)",
        f"[![Licenses: MIT + CC BY 4.0](https://img.shields.io/badge/Licenses-MIT%20%2B%20CC%20BY%204.0-3FA89B?style=flat)](LICENSES.md) [![Papers](https://img.shields.io/badge/Papers-{paper_count}-6F9FEF?style=flat)]({PAGES_URL}/) [![Update](https://img.shields.io/badge/Update-Daily-D47A5D?style=flat)](docs/agent/daily-curation-workflow.md)",
        "",
        f"**[🔎 インタラクティブな研究ランドスケープを見る →]({PAGES_URL}/#heatmap)** — チャートのセルをクリックすると、該当する論文の一覧が開きます。",
        "",
        "⭐ **このカタログが役に立ったら、ぜひリポジトリにStarをお願いします** — この分野のtaxonomyを維持する価値を示すことにもつながります。",
        "",
        "> 論文タイトル・著者名・taxonomyの統制語彙（`adversarial-patch` など）は公式表記（英語）のまま掲載しています。それ以外の見出しや説明文は日本語に翻訳しています。",
        "",
        "## 著者",
        "",
        "[**Futa Waseda**](https://futa-waseda.netlify.app/) — 国立情報学研究所（NII）特任助教（Project Assistant Professor）。",
        "",
        "## このカタログについて",
        "",
        "VLA・ロボット・自動運転・身体性AIエージェントを対象に、**Physical AIがどのように失敗するか**、**各研究がどのリスクを評価しているか**を整理するLLM支援の研究カタログです。",
        "",
        "<p align=\"center\">",
        "  <a href=\"assets/visualizations/physical-ai-safety-overview.png\">",
        "    <img src=\"assets/visualizations/physical-ai-safety-overview.png\" alt=\"Physical AI Safetyの構造化された脅威・失敗taxonomyと評価されたリスクアウトカムの概観\" width=\"750\">",
        "  </a>",
        "</p>",
        "",
        "5軸の脅威・失敗taxonomyで研究が扱う失敗経路を記述し、**Evaluated Risk Outcomes** は論文が報告した評価指標に基づいて別途分類します。定義と付与基準は[Taxonomyの詳細](docs/taxonomy.ja.md)をご覧ください。",
        "",
        "### スコープ",
        "",
        "このカタログは、**Foundation Modelに基づくPhysical AI**の安全性と信頼性を中心に、**Perception → Cognition → Planning → Action**の流れで捉えます。この流れは概念上の枠組みであり、独立したモジュール構成を要求しません。VLAやLLM/VLM駆動の身体性AIを対象とし、人との協働・複数ロボット・自動運転も含みます。Physical AIとの明確な関連を持たない汎用LLM/VLM研究はスコープ外です。",
        "",
        "### キュレーション方針",
        "",
        "taxonomyと更新手法は著者が設計し、論文収集・メタデータ抽出・分類はLLM支援のワークフローで更新しています。更新時に個々の論文を人間が事前レビューする運用ではないため、分類に誤りが含まれる可能性があります。重要な情報は元論文をご確認ください。[修正・追加の提案](CONTRIBUTING.ja.md)を歓迎します。",
        "",
        "各論文は1つのカタログレコードと1つの主たる貢献セクションを持ちます。横断的なテーブルは同じレコードを別の切り口で表示した生成ビューであり、別エントリではありません。",
        "",
        "Defense・Evaluation・Benchmarkの拡張メタデータについては[docs/metadata-schema.md](docs/metadata-schema.md)（英語）を参照してください。",
        "",
        "## 📚 引用",
        "",
        "このカタログの書誌情報・taxonomy・メタデータ・可視化・キュレーション手法を引用する場合は以下を、個々の論文の主張を引用する場合は元論文を引用してください。詳細は[CITATION.cff](CITATION.cff)を参照してください。",
        "",
        "```bibtex",
        "@software{Waseda_Awesome_Physical_AI_2026,",
        "  author = {Waseda, Futa},",
        "  doi    = {10.5281/zenodo.23348593},",
        "  month  = oct,",
        "  title  = {{Awesome Physical AI Safety}},",
        "  url    = {https://github.com/futakw/Awesome-Physical-AI-Safety},",
        "  year   = {2026}",
        "}",
        "```",
        "",
        "## 🔎 研究ランドスケープ",
        "",
        "これらの可視化はカタログ内のメタデータに基づく関係性を示すものであり、分野全体での頻度や防御手法の有効性を示すものではありません。セルをクリックすると元論文を確認できます。",
        "",
        "![Cumulative papers by first submission date](assets/visualizations/submission-growth.svg)",
        "",
        "初回投稿日（arXiv v1・UTC）ごとの累積論文数。投稿日不明の論文は除外しています。現在の収録論文を対象とした集計です。",
        "",
        f"[![Cataloged papers by research area and year](assets/visualizations/field-timeline.svg)]({PAGES_URL}/#timeline)",
        "",
        f"このカタログはどのように成長してきたか？ [タイムラインを見る →]({PAGES_URL}/#timeline)",
        "",
        f"[![Threat mechanisms by entry surface in this catalog](assets/visualizations/threat-heatmap.svg)]({PAGES_URL}/#heatmap)",
        "",
        f"どの脅威メカニズムがどの侵入面で発生するか？ [クロスマップを見る →]({PAGES_URL}/#heatmap)",
        "",
        f"[![Threat mechanisms by empirically evaluated risk in this catalog](assets/visualizations/threat-risk-heatmap.svg)]({PAGES_URL}/#risk)",
        "",
        f"各メカニズムについてどの評価済みアウトカムが報告されているか？ [元論文を確認する →]({PAGES_URL}/#risk)",
        "",
        "## カタログの読み方",
        "",
        "各論文は主な貢献に基づいて分類され、相補的な2つのメタデータ列で整理されています。",
        "",
        "### Evaluated Risk（評価されたリスク）",
        "",
        "リスクラベルは、各論文で評価されたアウトカムを要約します。",
        "",
        f"- {badge('Task', RISK_COLORS['task-reliability'])}: タスクまたは経路の成功。",
        f"- {badge('Physical', RISK_COLORS['physical-safety'])}: 衝突、損傷、安全でない動作。",
        f"- {badge('Ethics', RISK_COLORS['ethical-societal'])}: 有害な指示への準拠、方針違反、格差。",
        f"- {badge('Security/Privacy', RISK_COLORS['security-privacy'])}: 攻撃成功、乗っ取り、情報漏洩。",
        "",
        "**—** は、報告された評価指標から対応するリスクアウトカムが特定されないことを示します。",
        "",
        "### Threat Model（脅威モデル）",
        "",
        "各エントリは、構造化された脅威・失敗taxonomyを2行で要約します。",
        "",
        f"{badge('ライフサイクル', THREAT_COLORS['lifecycle'])} · {badge('サーフェス', THREAT_COLORS['surface'])}<br>{badge('メカニズム', THREAT_COLORS['mechanism'])} &nbsp;→&nbsp; {badge('ターゲット', THREAT_COLORS['target'])} &nbsp;→&nbsp; {badge('帰結', THREAT_COLORS['consequence'])}",
        "",
        "`+N` は、`data/papers.json` に保存された追加の値の数を示します。",
        "",
        "詳細な定義と分類基準は、[taxonomyの詳細](docs/taxonomy.ja.md)を参照してください。",
        "",
        "## 🧭 目次",
        "",
    ]


def render_catalog(papers: list[dict]) -> list[str]:
    lines: list[str] = []
    present_sections = [key for key in SECTIONS if any(p["section"] == key for p in papers)]
    section_order = {key: index for index, key in enumerate(present_sections)}
    subsection_order: dict[tuple[str, str], int] = {}
    for paper in papers:
        key = (paper["section"], paper["subsection"])
        if key not in subsection_order:
            subsection_order[key] = len(subsection_order)
    ethics_papers = sorted(
        (p for p in papers if "ethical-societal" in p["risks"]),
        key=lambda p: (
            section_order[p["section"]],
            subsection_order[(p["section"], p["subsection"])],
            -p["year"],
            p["title"].lower(),
        ),
    )

    for key in present_sections:
        icon, _ = SECTIONS[key]
        lines.append(f"- [{icon} {section_title_ja(key)}](#{key})")
    if ethics_papers:
        lines.append("- [⚖️ 倫理・社会的安全性](#ethics-societal-safety)")
    lines.extend(["", "<details>", "<summary><strong>サブセクション一覧を表示</strong></summary>", ""])
    for key in present_sections:
        icon, _ = SECTIONS[key]
        lines.append(f"- **{icon} {section_title_ja(key)}**")
        subsections: list[str] = []
        for paper in papers:
            if paper["section"] == key and paper["subsection"] not in subsections:
                subsections.append(paper["subsection"])
        for subsection in subsections:
            lines.append(
                f"  - [{subsection_title_ja(subsection)}](#{subsection_anchor(key, subsection)})"
            )
    lines.extend(["", "</details>", "", f"**現在のカタログには{len(papers)}件の論文があります。**", ""])

    for section_key in present_sections:
        section_papers = [p for p in papers if p["section"] == section_key]
        icon, _ = SECTIONS[section_key]
        lines.extend([f'<a id="{section_key}"></a>', "", f"## {icon} {section_title_ja(section_key)}", ""])
        subsections = []
        for paper in section_papers:
            if paper["subsection"] not in subsections:
                subsections.append(paper["subsection"])
        for subsection in subsections:
            lines.extend(
                [
                    f'<a id="{subsection_anchor(section_key, subsection)}"></a>',
                    "",
                    f"### {subsection_title_ja(subsection)}",
                    "",
                    "| 論文 | 発表先 | 評価されたリスク | Threat Model |",
                    "|---|---:|---|---|",
                ]
            )
            rows = [p for p in section_papers if p["subsection"] == subsection]
            rows.sort(key=lambda p: (-p["year"], p["title"].lower()))
            for paper in rows:
                risk = risk_cell_ja(paper["risks"])
                venue = f"{paper['venue']} {paper['year']}"
                lines.append(
                    f"| {paper_cell(paper)} | {venue} | {risk} | {threat_model_cell_ja(paper['threat_model'])} |"
                )
            lines.append("")

    if ethics_papers:
        lines.extend(
            [
                '<a id="ethics-societal-safety"></a>',
                "",
                "## ⚖️ 倫理・社会的安全性",
                "",
                f"このテーマ別ビューは`ethical-societal`ラベルが付いた{len(ethics_papers)}件のカタログレコードを再掲載したものです。新しい論文レコードを追加したり、評価ラベルを独自に検証したりするものではありません。",
                "",
                "| 論文 | 発表先 | 評価されたリスク | Threat Model |",
                "|---|---:|---|---|",
            ]
        )
        for paper in ethics_papers:
            section_key = paper["section"]
            primary_section_ja = section_title_ja(section_key)
            primary_anchor = subsection_anchor(section_key, paper["subsection"])
            paper_info = (
                f"{paper_cell(paper)}<br>"
                f'<sub>主掲載: <a href="#{primary_anchor}">'
                f"{escape(primary_section_ja)} / {escape(subsection_title_ja(paper['subsection']))}</a></sub>"
            )
            venue = f"{paper['venue']} {paper['year']}"
            lines.append(
                f"| {paper_info} | {venue} | {risk_cell_ja(paper['risks'])} | {threat_model_cell_ja(paper['threat_model'])} |"
            )
        lines.append("")

    lines.extend(
        [
            "## コントリビューション",
            "",
            "コントリビューションを歓迎します。[CONTRIBUTING（日本語）](CONTRIBUTING.ja.md)をお読みいただき、`data/papers.json`の該当レコードを追加・更新してください。生成されたテーブルを直接編集しないでください。",
            "",
            "## ライセンス",
            "",
            "コードは[MIT](LICENSE)、カタログのオリジナルコンテンツは[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)の下でライセンスされています。範囲と帰属表示の詳細は[LICENSES.md](LICENSES.md)（英語）を参照してください。リンク先の論文・サードパーティ素材はそれぞれの条件に従います。",
            "",
        ]
    )
    return lines


def render(papers: list[dict]) -> str:
    lines = render_overview(len(papers)) + render_catalog(papers)
    return "\n".join(lines) + "\n"


def warn_untranslated_subsections(papers: list[dict]) -> None:
    missing = sorted({p["subsection"] for p in papers} - set(SUBSECTIONS_JA))
    if missing:
        print(
            "WARNING: subsection(s) missing from scripts/labels_ja.py SUBSECTIONS_JA "
            "(rendering in English in README.ja.md until translated):"
        )
        for name in missing:
            print(f"  - {name!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    papers = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    output = render(papers)
    warn_untranslated_subsections(papers)

    if args.check:
        current = README_JA_PATH.read_text(encoding="utf-8") if README_JA_PATH.exists() else ""
        if current != output:
            print("README.ja.md is out of date. Run scripts/build_readme_ja.py.")
            return 1
        print("README.ja.md is up to date.")
        return 0

    README_JA_PATH.write_text(output, encoding="utf-8")
    print(f"Generated README.ja.md with {len(papers)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
