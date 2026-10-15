# コントリビューション

[English](CONTRIBUTING.md) | **日本語（このページ）**

Awesome Physical AI Safetyの改善にご協力いただきありがとうございます。

継続的な文献メンテナンスについては、[日次キュレーションワークフロー](docs/daily-curation-workflow.md)（英語）に従ってください。

## 論文の追加・更新

1. `data/papers.json`を編集する。
2. 安定した`id`、公式タイトル、第一著者の姓、venue、年、論文URL、（可能であれば）公式のプロジェクトまたはGitHub URLを持つ1件のレコードを追加する。
3. 1つの主たる`section`を割り当て、そのsectionのクローズド語彙（`scripts/validate_catalog.py`の`SUBSECTIONS[section]`）から`subsection`を選ぶ。論文が既存の値に妥当に当てはまる場合はそれを再利用し、本当にどれにも当てはまらない場合のみ新しい値を追加する。追加する際は、同じコミットで`validate_catalog.py`と`scripts/labels_ja.py`の両方を更新すること（詳細は[メタデータスキーマ](docs/metadata-schema.md#subsection)を参照）。
4. 実証的に評価されたリスクアウトカム（または空の`risks`リスト）、構造化された`threat_model`、焦点を絞ったmechanism・OODタグを追加する。
5. 以下を実行する:

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

6. メタデータの変更を、生成された`README.md`と`README.ja.md`とともにコミットする。

## 表示ルール

- 著者は`FirstAuthor et al.`の形式で表示されます。`first_author`には第一著者の姓を格納してください。
- 公式の論文タイトルと確認済みのvenueを使用してください。生成されたテーブルはタイトルを`paper_url`に直接リンクします。採録venueが未確認の場合は`arXiv`を使用してください。
- `year`には確認済みvenue自体の年（公式proceedings、DBLP、またはvenueのacceptanceページに基づくproceedings/program年）を設定してください。arXiv投稿年ではありません。同じ論文でもarXivプレプリントと実際の採録venueでは年が異なることがよくあります。レコードの`venue`を`arXiv`/`OpenReview`から正式なvenueに変更する際は、同時に`year`もそのvenueの年に更新してください。詳細は[メタデータスキーマ](docs/metadata-schema.md#venue-and-year)を参照してください。
- `code_url`には公式または著者自身がメンテナンスする実装のみをリンクしてください。
- 公式リポジトリが不明な場合は`code_url`を`null`のままにしてください。
- GitHub starバッジおよびその他のproject/codeリンクは、`code_url`から論文タイトルの横に自動生成されます。
- リスクラベルは、論文が対応する実証的な指標を報告している場合にのみ追加してください。動機・考察・脅威の可能性・物理ロボットの使用のみからラベルを推測しないでください。対応するアウトカム指標がないsurvey論文や研究には空の`risks`リストを使用してください。
- `threat_model`は、[taxonomy（日本語）](docs/taxonomy.ja.md)で定義された統制語彙である`kind`・`lifecycle`・`mechanism`・`surface`・`target`・`consequence`を用いて構造化してください。防御手法については、防御方法そのものではなく緩和対象の脅威を記述してください。
- レコードが複数の独立した脅威にまたがり、単一の脅威経路を特定できない場合は、`survey`または`evaluation`のcoverageバリアントを使用してください。実験設定や副次的な記述子は`tags`に含めてください。`tags`は構造化メタデータのままであり、独立したテーブル列としてはレンダリングされません。
- 論文1件につき1つのカタログレコードを追加し、1つの主たるセクションを割り当ててください。生成されたテーマ別テーブルは、同じレコードを追加のビューとして表示することがあります。

## スコープ

スコープはphysical AIの安全性・セキュリティ・堅牢性・プライバシー・倫理的/社会的アウトカム・信頼できる実運用です。VLAを主軸としつつ、身体化された挙動・物理的インタラクション・実運用関連のリスクを研究している限り、ロボットポリシー・自動運転・身体性AIエージェントに関する研究もスコープに含まれます。汎用LLM/VLM研究には、physical AIとの明示的な関連が必要です。

## プルリクエスト

各プルリクエストは焦点を絞ってください。新しい論文がなぜ選択したセクションに属するのか、どのphysical AIシステムを研究しているのか、どのリスク・メカニズム・評価原則に貢献するのかを説明してください。

## ライセンス

コードのコントリビューションはMITの下で、カタログのオリジナルコンテンツのコントリビューションはCC BY 4.0の下でライセンスされます。ご自身が寄稿する権利を持つ素材のみを提出してください。各ライセンスの範囲については[LICENSES.md](LICENSES.md)（英語）を参照してください。
