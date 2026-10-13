# Awesome Physical AI Safety

[English](README.md) | **日本語（このページ）**

**🤖 VLA・ロボット・自動運転・身体性AIエージェントにおける安全性、セキュリティ、堅牢性、倫理的・社会的リスク、信頼できる実運用に関する、LLM支援の文献カタログです。**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Cite this repository](https://img.shields.io/badge/Cite-CITATION.cff-blue.svg)](CITATION.cff)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23348593.svg)](https://doi.org/10.5281/zenodo.23348593)
[![LLM-assisted](https://img.shields.io/badge/curation-%F0%9F%A4%96%20LLM--assisted-critical.svg)](docs/daily-curation-workflow.md)
[![Licenses: MIT + CC BY 4.0](https://img.shields.io/badge/Licenses-MIT%20%2B%20CC%20BY%204.0-3FA89B?style=flat)](LICENSES.md) [![Papers](https://img.shields.io/badge/Papers-250-6F9FEF?style=flat)](https://futakw.github.io/Awesome-Physical-AI-Safety/) [![Update](https://img.shields.io/badge/Update-Daily-D47A5D?style=flat)](docs/daily-curation-workflow.md)

**[🔎 インタラクティブな研究ランドスケープを見る →](https://futakw.github.io/Awesome-Physical-AI-Safety/#heatmap)** — チャートのセルをクリックすると、該当する論文の一覧が開きます。

⭐ **このカタログが役に立ったら、ぜひリポジトリにStarをお願いします** — この分野のtaxonomyを維持する価値を示すことにもつながります。

> この日本語版は概要のみです。**全論文一覧（現在250件）は英語版に一本化**しています — 論文タイトル・著者名は公式表記（英語）のまま掲載するのが正確なためです。一覧は [README.md](README.md) または [インタラクティブexplorer](https://futakw.github.io/Awesome-Physical-AI-Safety/) からご覧ください。

## 著者

[**Futa Waseda**](https://futa-waseda.netlify.app/) — 国立情報学研究所（NII）特任助教（Project Assistant Professor）。

## このカタログについて

- **🤖 完全LLM自動運用、人間レビューなし。** 論文の検索・メタデータ抽出・taxonomyへの分類・コミットまで、全て自律AIエージェントが[日次キュレーションワークフロー](docs/daily-curation-workflow.md)（英語）に従って実行しています。**コミット前に人間が個別チェックすることはありません。** 掲載内容は暫定的なものとして扱い、重要な判断の際は一次情報（論文本体）を直接ご確認ください。誤りを見つけた場合はissueまたはPRでご報告ください。
- **taxonomyと手法の設計者。** リスク分類、失敗要因、構造化threat modelスキーマ（`kind`/`lifecycle`/`mechanism`/`surface`/`target`/`consequence`）は**Futa Waseda**が設計し、文献収集・キュレーション手法も同氏が設計しました。詳細は[taxonomy定義](docs/taxonomy.md)（英語）を参照してください。
- **貢献歓迎。** 新しい論文の追加、既存エントリの修正、taxonomyの改善はPull Requestで歓迎します。詳細は[CONTRIBUTING.md](CONTRIBUTING.md)（英語）を参照してください。

## 📚 引用

このカタログの書誌情報・taxonomy・メタデータ・可視化・キュレーション手法を引用する場合は以下を、個々の論文の主張を引用する場合は元論文を引用してください。詳細は[CITATION.cff](CITATION.cff)を参照してください。

```bibtex
@software{Waseda_Awesome_Physical_AI_2026,
  author = {Waseda, Futa},
  doi    = {10.5281/zenodo.23348593},
  month  = oct,
  title  = {{Awesome Physical AI Safety}},
  url    = {https://github.com/futakw/Awesome-Physical-AI-Safety},
  year   = {2026}
}
```

## Taxonomyの概要

分類体系（taxonomy）そのものの用語は、カタログデータとの一貫性のため英語の統制語彙を使用しています。各用語の定義は以下の通りです。

### リスクアウトカム（評価された結果）

論文が実際に測定した指標に対応する場合のみラベルが付与されます。考察や潜在的な影響への言及だけでは付与されません。

- ![タスク](https://img.shields.io/badge/-%E3%82%BF%E3%82%B9%E3%82%AF-6F9FEF?style=flat)
- ![物理的安全性](https://img.shields.io/badge/-%E7%89%A9%E7%90%86%E7%9A%84%E5%AE%89%E5%85%A8%E6%80%A7-D96F8A?style=flat)
- ![倫理・社会](https://img.shields.io/badge/-%E5%80%AB%E7%90%86%E3%83%BB%E7%A4%BE%E4%BC%9A-9873D4?style=flat)
- ![セキュリティ/プライバシー](https://img.shields.io/badge/-%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%2F%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC-B88A24?style=flat)
- **—:** 対応する実証的な評価指標がない場合（survey論文や診断のみの研究で一般的）。

### 失敗要因

- **Adversarial（敵対的）:** 入力・学習・状態・行動・システム構成要素への意図的な操作。
- **Non-adversarial / OOD（非敵対的・分布外）:** 未知の視点・物体・言語・タスク・環境・身体・時間変化下での失敗。
- **Design / system（設計・システム）:** 目的の誤設定、マルチモーダル不整合、報酬ハッキング、センサ故障、プランナー・実行系の不整合、リカバリ不全。

### Threat Modelの構造

各レコードは `kind`（種別）→ `lifecycle`（発生段階）→ `mechanism`（手法）→ `surface`（侵入面）→ `target`（対象）→ `consequence`（結果）という多軸の構造化データを持ちます。詳細な語彙定義は[taxonomy定義](docs/taxonomy.md)（英語）を参照してください。

## 🔎 研究ランドスケープ

論文数の推移、脅威メカニズムと侵入面の関係、脅威メカニズムと評価されたリスクの関係などをインタラクティブに可視化しています。

**[→ インタラクティブexplorerを開く](https://futakw.github.io/Awesome-Physical-AI-Safety/)**

