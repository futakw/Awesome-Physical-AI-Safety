# Taxonomyとキュレーション方針

[English](taxonomy.md) | **日本語（このページ）**

> 統制語彙（`kind`・`lifecycle`・`mechanism`・`surface`・`target`・`consequence`などの実際の値）は`data/papers.json`との一貫性のため英語のまま記載しています。日本語は説明文のみです。

このリポジトリは多軸のtaxonomyを使用しています。論文の主要セクションはその研究の主たる貢献を表し、独立したメタデータがリスクにさらされるアウトカム・失敗要因・メカニズム・評価体制を記述します。

## 1. 実証的に評価されたリスクアウトカム

`risks`フィールドはevidence-coded（証拠に基づく）であり、起こりうる結果の一覧ではありません。論文の実験が当該アウトカムの指標を報告している場合にのみラベルが付与されます。4つのリスクすべてを論じるsurvey論文は空のリストを持つ一方、攻撃論文がタスク成功率と攻撃成功率の両方を報告していれば`task-reliability`と`security-privacy`の両方が付与されることがあります。物理環境での実行だけでは`physical-safety`ラベルの根拠にはなりません。

| ラベル | 値 | 該当する条件 |
|---|---|---|
| **タスク・信頼性** | `task-reliability` | タスクまたは経路の完了、成功率、またはそれに相当するend-to-endの実行結果。行動の逸脱、検知精度、キャリブレーション誤差、攻撃成功のみでは該当しません。 |
| **物理的安全性** | `physical-safety` | 衝突、人への傷害、物体・環境への損害、安全でない力や動作、物理的危害の実行、安全制約違反、または明示的な物理リスクの代理指標。 |
| **倫理・社会** | `ethical-societal` | 有害または禁止された指示への準拠・拒否、方針や憲章（constitution）の違反、明示的に測定された有害な身体化行動、またはアクセス・タスク成功・支援品質・危険への曝露における人や集団間の測定された格差。公平性への動機、モデルの帰納バイアス、ベンチマークによる「公平な評価」を謳う文言だけでは、対応する社会的アウトカムの指標がない限り該当しません。 |
| **セキュリティ/プライバシー** | `security-privacy` | 攻撃成功、バックドア起動、不正な制御、コマンド乗っ取り、情報漏洩、秘密裏の通信、メモリや通信の侵害、システム侵害。 |

### 付与ルール

1. 実験で実際に報告されている指標を特定する。
2. それらの指標のみを上記4つのアウトカムに対応付ける。
3. タイトル、動機、実運用設定、または仮想的な下流の帰結からラベルを付与しない。
4. 対応する報告指標がない場合は空の`risks`リストを使用する。READMEでは`—`と表示される。

## 2. 失敗要因

論文の`threat_model.kind`は3つの失敗要因のいずれかです（複数の脅威にまたがるレコード用の`survey`/`evaluation`もあります。詳細は[Threat Kinds](#threat-kinds脅威の種別)を参照）。

| ラベル | 値 | 定義 |
|---|---|---|
| **Adversarial（敵対的・悪意のある操作）** | `adversarial` | 攻撃者が入力・学習データ・モデル状態・行動・環境・システム構成要素を意図的に操作する。 |
| **Non-Adversarial（非敵対的）・OOD** | `non-adversarial` | 攻撃者を想定せず、未知の視点・見た目・物体・幾何・言語・タスク・環境・身体・時間変化のもとでシステムが失敗する。 |
| **設計・学習・システムの失敗** | `system-failure` | 目的の誤設定、マルチモーダル不整合、報酬ハッキング、センサ故障、プランナー・実行系の不整合、または不十分なランタイムリカバリから生じる失敗。 |

## 3. 構造化されたThreat Model

> **ステータス: 採用済み。** 全てのカタログレコードとREADME生成器はこのスキーマを使用します。

`threat_model`フィールドはコンパクトな自由記述文字列ではなく、構造化されたオブジェクトです。5つのフィールドが脅威・失敗経路に関する5つの問いに答えます——**いつ**発生するか（When）、**どこから**侵入するか（Where）、**どのように**作用するか（How）、**何を**標的とするか（What is the target）、**どんな帰結**を生むか（What follows）。加えて`kind`は、このレコードがどの種類に属するかを表す別フィールドです。

### 役割分担

各フィールドは別々の問いに答え、別々の根拠から割り当てます。固定的なマッピングルールで他のフィールドから推測するものではありません。

- **`surface`（どこから）**: 脅威が導入・シフト・観測されるシステム境界やインターフェース — 侵入口や配送チャネル。
- **`mechanism`（どのように）**: 論文が研究している攻撃手法・失敗モード。
- **`target`（何が狙われたか）**: 論文の明示的な目的・損失関数・評価プロトコルが名指すコンポーネント・機能・資産 — 経路上で影響を受けうる全てのコンポーネントではない。
- **`consequence`（どんな帰結）**: 脅威・失敗経路が到達する具体的な結末。
- **`risks`（何が測定されたか、セクション1）**: `threat_model`とは独立した、実証的に評価された広いリスク領域。

知覚経由の配送チャネル（`surface`）があるからといって知覚が`target`になるわけではなく、下流の効果があるからといって2つ目の`mechanism`ラベルになるわけではなく、リスク領域があるからといってどの`consequence`が起きたかが決まるわけでもありません。具体的なdo/don'tの境界は、以下の各語彙の付与ルールを参照してください。

### コアフィールド

| フィールド | 問い | 型 | 具体的な研究で必須か | 意味 | 例 |
|---|---|---|---:|---|---|
| `lifecycle` | いつ？（When?） | 文字列の配列 | Yes | 脅威が導入・発動される段階、または失敗が評価される段階 | `training`, `inference` |
| `surface` | どこから？（Where?） | 文字列の配列 | Yes | 脅威・シフト・失敗が導入または観測される直接のシステム境界 | `visual-perception` |
| `mechanism` | どのように？（How?） | 文字列の配列 | Yes | 攻撃・シフト・失敗がどのように生じるか | `adversarial-patch` |
| `target` | 攻撃・評価の対象は何か？（What is the target of attack or evaluation?） | 文字列の配列 | Yes | 明示的に攻撃・評価の対象とされたコンポーネント・機能・資産 — 経路上で影響を受けうる全てではない | `vla-policy` |
| `consequence` | どんな帰結？（What follows?） | 文字列の配列 | Yes | 脅威・失敗連鎖の具体的な到達点 | `task-failure` |
| `kind` | *（レコードの種類、5つの問いとは別）* | string | Yes | 失敗の大まかな発生源、またはレコードの範囲 | `adversarial` |
| `curation_status` | *（来歴情報、5つの問いとは別）* | string | Yes | この割り当てが一次資料に対してどの程度確認されたか — [Mechanismの監査状況](#mechanismの監査状況)を参照 | `paper-verified` |

このリポジトリは記述的な意味ラベルを使用します。個々の論文やサーベイが定義した番号付きサーフェスコードを正規のメタデータとしては使用しません。

### Threat Kinds（脅威の種別）

| 値 | 使用する場合 |
|---|---|
| `adversarial` | 攻撃者が学習・入力・状態・モデル・行動・インフラを意図的に操作する。 |
| `non-adversarial` | 研究が攻撃者を想定せず、OODシフト・曖昧さ・不確実性・自然発生的な失敗を評価する。 |
| `system-failure` | 失敗がシステム設計・統合・コントローラー・リカバリ・インフラの挙動に起因する。 |
| `evaluation` | ベンチマークが複数の異なる脅威をカバーし、単一の主要な脅威経路を持たない。 |
| `survey` | サーベイやポジションペーパーが、単一の具体的な脅威ではなく脅威のランドスケープを記述する。 |

### いつ？（When?）— Lifecycle語彙

| 値 | 定義 |
|---|---|
| `training` | データ収集、事前学習、ファインチューニング、post-training、モデルマージ、またはチェックポイント配布。 |
| `inference` | デプロイ時の知覚・推論・計画・行動生成・ランタイムでのインタラクション。 |
| `system` | ミドルウェア、ネットワーキング、外部サービス、マルチエージェント、または実行インフラ。 |

`lifecycle`はマルチラベルです。バックドアは`training`中に埋め込まれ、`inference`中に発動することがあります。

### どこから？（Where?）— Surface語彙

以下は「知覚→推論→行動」という一連の流れに沿って、上流の学習・インフラ層から下流の行動・制御層まで区分ごとに並べています。

| 値 | 表す境界 |
|---|---|
| **訓練・インフラ** | |
| `model-supply-chain` | 学習データ、アダプタ、チェックポイント、事前学習済みコンポーネント、またはモデル配布。 |
| `middleware-network` | ROS/ROS2、DDS、ドライバ、認証情報、クラウドモデル、リモートAPI、または通信。 |
| **知覚** | |
| `visual-perception` | 画像、動画、カメラ、視覚トークン、パッチ、テクスチャ、または光学信号。 |
| `audio-perception` | 音声、マイク、音響信号、または音声特徴量。 |
| `physical-semantic-environment` | シーン中のテキスト、標識、ラベル、ディスプレイ、QRコードなど、正しく知覚された、環境中の意味的コンテンツ。 |
| **言語** | |
| `user-instruction` | 現在のタスクや制御意図として受理される、認証済みのテキストまたは音声。 |
| `context-memory-retrieval` | インタラクション履歴、永続メモリ、ICL例、RAGドキュメント、またはツール結果。 |
| `multi-agent-communication` | ロボット間メッセージ、共有メモリ、主張、または協調状態。 |
| **固有受容感覚** | |
| `proprioception` | 関節状態、力、触覚フィードバック、またはロボット内部のセンシング。 |
| **計画・状態** | |
| `world-state` | 物体間の関係、占有状況、位置推定、シーングラフ、アフォーダンス、または予測された状態。 |
| `task-planning` | 目標、タスク分解、行動順序、経路、またはリカバリ戦略。 |
| **推論** | |
| `reasoning-representation` | 隠れ状態、アテンション、chain-of-thought、またはクロスモーダル表現。 |
| **行動・制御** | |
| `action-interface` | 行動トークン、行動チャンク、コード、ツール呼び出し、API、スキル、または連続制御。 |
| `execution-control` | 軌道、アクチュエータコマンド、安全停止、フリーズ、またはリソース可用性。 |

`surface`は研究が直接操作・シフト・破損・評価したインターフェースのみを記録します。推測される内部伝播経路はエンコードしません。異なるlifecycle段階で異なるインターフェースが使われる場合、複数の値が許容されます。例えば、視覚的に発動するバックドアは学習時に`model-supply-chain`、推論時に`visual-perception`の両方を使うことがあります。

### どのように？（How?）— Mechanism語彙（Technique-oriented）

`mechanism`は論文が実際に研究している**具体的な攻撃手法または失敗モード**を分類します。推論された因果メカニズムではありません。「攻撃はどう実行されたか／どんな失敗モードが研究されているか」に答えるもので、「根本原因は何か」には答えません。`adversarial-patch`・`typographic-injection`・`backdoor`・`membership-inference`のような、具体的な研究用語は、それが基礎的な原理ではなく個別の攻撃実装を指す場合でも維持します。ファミリーは関連する攻撃手法・失敗モードをまとめており、これは`surface`（知覚→推論→行動のパイプライン上の「どこで」起きるか）とは意図的に別軸です。1つのmechanismファミリーが1つのsurfaceファミリーに対応するわけではありません。**データ・モデルへの攻撃**は、データ・モデル・メモリ・検索ストアの汚染や侵害に加え、それらから機微情報を推定する攻撃を含む広い分類です。データやモデルの改変を必須とはせず、`membership-inference`もこのfamilyに含めます。

**付与ルール:**

1. 論文のMethod/Experimentsで裏付けられる場合のみラベルを付与する。タイトルだけからは付与しない。
2. 複数ラベルは、それぞれが独立して根拠を持ち別々の情報を伝える場合に許容する（例: テキストが印字された敵対的パッチは`adversarial-patch`と`typographic-injection`の両方を満たしうる）。
3. 1つ目の機構が下流の効果を引き起こしたというだけの理由で2つ目のラベルを追加しない（例: jailbreakの結果としてロボットの計画が変化しただけなら、ラベルは`jailbreak`のみとし、計画への影響は`target`/`consequence`で表現する）。
4. 防御論文が想定する脅威モデルだけから攻撃手法を推論しない。手作業で作成した・モデル化されていない「unsafe」な例に対してのみ評価している防御論文には、実証されたHOWは存在せず、フィールドを省略するか論文自身が実証した値のみを用いる。
5. 最も具体的で裏付けのあるラベルを優先する。論文の根拠が具体的な手法を立証していない場合は`mechanism`を空リストにする。これは「まだレビューしていない」とは異なる状態であり、下記の`curation_status`で区別する。
6. 内部モデル状態への直接操作を名指すラベル（例: `representation-manipulation`）は、論文の最適化変数または攻撃対象そのものが内部表現である場合にのみ使用する。内部特徴量ベースの損失を使って入力（パッチ・テキストプレフィックス・摂動）を最適化しているだけの場合は該当しない — それは入力レベルの手法（`adversarial-patch`、`digital-perturbation`等）であり、内部特徴量は損失の目標値として参照されているに過ぎない。

| 値 | 攻撃手法・失敗モード |
|---|---|
| **データ・モデルへの攻撃** | |
| `data-poisoning` | 学習データを汚染し、あらかじめ定めた失敗や挙動を誘発する。 |
| `backdoor` | トリガー条件を埋め込み、攻撃者が選んだ挙動を発動させる。 |
| `malicious-adapter` | 隠れた有害な挙動を持つファインチューニング済みアダプタ・LoRAモジュール・プラグインを配布する。 |
| `checkpoint-compromise` | 事前学習済み・共有されたモデルチェックポイントを配布前に改ざんする。 |
| `reward-manipulation` | 学習信号や報酬関数を汚染し、安全でない挙動を形作る。 |
| `memory-poisoning` | 永続メモリや長期コンテキストストアを悪意あるコンテンツで汚染する。 |
| `retrieval-poisoning` | 検索コーパス内の文書や例を汚染し、取得される内容に偏りを生じさせる。 |
| `membership-inference` | 特定のデータが学習・メモリに含まれていたかを、主にモデル内部の特徴量や確信度信号から推定する（プロンプトレベルのアクセスのみを想定しない）。 |
| **摂動・なりすまし** | |
| `digital-perturbation` | 知覚できない、または制約されたノイズをデジタル入力（画像・テキスト・音声等）に加える。 |
| `adversarial-patch` | 知覚を欺くために作り込まれた目に見えるパッチやテクスチャを配置する。 |
| `adversarial-object` | 狙った失敗を引き起こすよう設計された物理的物体を用いる。 |
| `sensor-spoofing` | 物理センサー（GPS、LiDAR、IMU等）に偽の信号を与える。 |
| `feedback-spoofing` | 内部・外部のフィードバック信号を偽装してシステムを欺く。 |
| `environment-manipulation` | 物理的な物体やシーンの配置を変更し、失敗を誘発する。 |
| **命令・意味操作** | |
| `direct-prompt-injection` | 悪意ある指示をユーザー入力として直接与える。 |
| `indirect-prompt-injection` | 悪意ある指示を、システムが後で処理するコンテンツに埋め込む。 |
| `jailbreak` | プロンプトまたは最適化された敵対的入力により安全性学習を回避し、制限された・意図しない挙動を引き出す。 |
| `typographic-injection` | シーン中に描画されたテキストが読み取られ、指示として扱われるか、視覚・意味的判断を上書きする形で作用する。 |
| `hazardous-instruction` | 一見無害な指示が、物理的・社会的に有害な結果につながる。指示追従失敗として広く研究・ベンチマーク化されている分類。 |
| **ランタイム・システム操作** | |
| `middleware-compromise` | ミドルウェア、ドライバ、通信層を侵害する。 |
| `network-attack` | ネットワーク通信を傍受・改ざん・妨害する。 |
| `denial-of-service` | リソース枯渇・フラッディング、または安全機構の悪用により可用性を低下・遮断する。 |
| `covert-channel` | 認可されていない経路で情報を秘密裏に持ち出す、または通信する。 |
| `state-manipulation` | センシングとは独立に、システムの内部の信念・状態表現をランタイムで直接改ざんする — 直接的な改ざんが実証されている場合のみ使用し、下流の不具合から推論しない。 |
| `action-manipulation` | 出力される行動トークンやコマンドを実行前に直接改変する。 |
| `trajectory-manipulation` | 生成された運動軌道そのものが実証された手法の対象である場合に使用し、既に付与された摂動・注入ラベルの単なる下流効果には使わない。 |
| `representation-manipulation` | 内部の隠れ状態やクロスモーダル表現が、攻撃者によって直接最適化・上書きされる対象である場合に使用する — 内部特徴量ベースの損失で入力を最適化しているだけの場合は該当しない（付与ルール6を参照）。 |
| **分布シフト・不確実性** | |
| `distribution-shift` | 攻撃者を想定せず、テスト時の条件が学習時の分布と異なる。 |
| `instruction-ambiguity` | 悪意のない自然な指示が、記述不足または曖昧である。 |
| `uncertainty-miscalibration` | システムの確信度が実際の信頼性と一致しない。 |
| **推論・計画・実行の失敗** | |
| `perception-error` | 敵対的な原因なしに、知覚が誤認識・誤定位する。 |
| `semantic-misalignment` | 敵対的な原因なしに、言語と視覚・行動のグラウンディングが乖離する。 |
| `planning-error` | 攻撃者なしに、プランナーが実行不可能・非最適・安全でない計画を生成する。 |
| `execution-error` | 攻撃者なしに、低レベルの実行が意図した行動から逸脱する。 |
| `multimodal-desynchronization` | モダリティ間の時間的・意味的整合が崩れ、統合理解が汚染される。 |

一部のラベルは、現時点で採用論文がゼロであっても統制語彙として定義を維持することがあります。明確で再利用可能な技術を指す場合（現時点では`representation-manipulation`が該当）、根拠論文が見つかるたびに追加・削除するのではなく、定義を維持しておきます。

`kind`はmechanismファミリーと緩く相関しますが、厳密な上位階層ではありません。`adversarial`は上記の攻撃系ファミリーのほとんどにまたがり（1つに限定されない）、`non-adversarial`/`system-failure`は「分布シフト・不確実性」「推論・計画・実行の失敗」に集中する傾向がありますが完全ではなく、`survey`/`evaluation`は`coverage.mechanisms`を通じて複数ファミリーを同時にカバーすることがあります。`kind`は`mechanism`の上位階層ではなく、別の軸（レコードの種類）として扱ってください。

### Mechanismの監査状況

`threat_model.curation_status`は、現在の`mechanism`（および構造化threat_modelの他フィールド）の割り当てが一次資料に対してどの程度確認されたかを記録します。`defense`/`evaluation`/`benchmark`拡張と同じ尺度（`paper-verified`、`abstract-verified`、`catalog-derived`、`reference-only`）を使用します。これにより、「現行語彙でまだ再確認していないレコード」（`catalog-derived`）と「レビュー済みだが具体的な手法の根拠が見つからなかったレコード」（`mechanism`が空リストの`paper-verified`）を区別できます。どちらも有効な状態ですが、今後のキュレーションにとって意味が異なります。

### 攻撃・評価の対象は何か？（What is the target of attack or evaluation?）— Target語彙（目的志向）

`target`は、論文が明示的に述べる攻撃目的・防御目標・評価設計によって**明示的に狙われた**機能・コンポーネント・資産です。因果連鎖上で影響を受けうる全てのコンポーネントではなく、また内部モデル挙動についての推測的な主張でもありません。

**付与ルール:**

1. 論文が明示する攻撃目的・損失関数・評価プロトコルを特定し、そこから`target`を割り当てる — `surface`（どこから届いたか）や`consequence`（何が結果として起きたか）からは割り当てない。
2. 攻撃が画像・音声等の知覚チャネル経由で届いたというだけで`perception-model`を付与しない。知覚・認識精度そのものが攻撃・測定対象である場合にのみ付与する。
3. 観測された失敗が計画・推論的に見えるというだけで`reasoning-process`や`task-planner`を付与しない。論文の目的や評価プロトコルが明示的に推論・計画に関わる場合（例：タスクプランの誘導を明示目標とする、計画・意思決定の正しさを評価指標とする）にのみ付与する。
4. 複数のtargetは、論文が複数のコンポーネントを明示的に攻撃・防御・評価している場合にのみ許容する。保険的な付与はしない。
5. `vla-policy`は、ポリシー全体またはそのタスクレベルの挙動が明示的な対象であり、より狭いtargetが確立されていない場合に引き続き適切である。論文が述べていない内部計算を推測して、より狭いラベルに置き換えない。

| 値 | 対象 |
|---|---|
| **知覚・理解** | |
| `perception-model` | 視覚・音声・マルチモーダル知覚コンポーネント。 |
| **推論・計画・ポリシー** | |
| `task-planner` | 目標選択、タスク分解、経路、または高レベルのポリシー意図。 |
| `reasoning-process` | 内部推論、アテンション、またはマルチモーダル整合。明示的な目的・評価対象である場合に使用する。 |
| `world-state` | 下流の意思決定に使われる構造化・予測された状態。計画に使われるworld modelを含む。 |
| `vla-policy` | end-to-end、または部分的に公開されたVLAポリシー。ポリシー全体またはそのタスクレベルの挙動が明示的対象で、より狭いラベルが確立されていない場合に使用する。 |
| **行動・システム運用** | |
| `action-generation` | 行動トークン、チャンク、軌道、コード、またはツール生成。 |
| `robot-executor` | コントローラー、アクチュエータ、安全停止、または実行プロセス。 |
| `runtime-monitor` | ガードレール、検証器、検知器、または安全性判定器。 |
| `shared-system-state` | メモリ、ミドルウェア、クラウドサービス、またはマルチエージェント間の共有状態。 |
| **データ・プライバシー資産** | |
| `private-data` | 学習メンバーシップ、観測、識別情報、位置情報などの機微データ。 |

`vla-policy`はモデル・データ系ファミリーではなく推論・計画・ポリシーに分類しています。カタログ全体で見ると、`vla-policy`は保存された成果物としての抽出・汚染（これは`mechanism`側の`backdoor`・`data-poisoning`・`checkpoint-compromise`・`membership-inference`が既に担う）ではなく、圧倒的に**ポリシーの挙動**（攻撃やシフトのもとでのタスク成功・失敗）を指して使われているためです。`private-data`は他のファミリーに馴染まない独立した関心事（データ・プライバシーへの露出）を表すため、Surface語彙の`proprioception`と同様に単一リーフの独立ファミリーとして維持しています。

### どんな帰結？（What follows?）— Consequence語彙（フラットな統制語彙）

`consequence`は**ファミリー分類のないフラットな統制語彙**です。`risks`（セクション1）が既にリスク領域の俯瞰（タスク・信頼性／物理的安全性／倫理・社会／セキュリティ・プライバシー）を提供しているため、`consequence`を同じようにファミリー分類すると`risks`と意味的に重複します。`consequence`はその代わりに脅威・失敗経路の具体的な到達点を記録します。1つのリスク領域が複数の異なる、互いに置き換え不可能な帰結にまたがることは日常的です（例：`security-privacy`は`control-hijacking`・`targeted-action`・`privacy-leakage`のいずれも含みますが、これらは`risks`だけでは区別できない異なる結果です）。`unsafe-success`と`policy-violation`は、外部の攻撃者が原因かどうかを問わず「エージェント自身の行動が安全・倫理規範に違反する」ことを表し、一方`control-hijacking`は「外部主体が制御権を得る」ことを明示的に指します。`ethical-societal`リスクはほぼ`policy-violation`に集中し`control-hijacking`にはほとんど現れない、というのはまさに`risks`だけでは表現できない区別の例です。

| 値 | 具体的な到達点 |
|---|---|
| `task-failure` | 割り当てられたタスクや経路が完了しない。 |
| `recovery-failure` | 検知・緩和・再計画・リカバリが安全な動作を回復できない。 |
| `collision` | ロボットが障害物・人・禁止された物体に接触する。 |
| `unsafe-motion` | 安全でない力・速度・姿勢・軌道・制御挙動が発生する。 |
| `physical-damage` | 人・ロボット・物体・環境に危害や損害が生じる。 |
| `targeted-action` | システムが攻撃者の選択した行動または行動系列を実行する。 |
| `action-freezing` | ポリシーが停止する、または危険な無行動を生じる。 |
| `control-hijacking` | 権限のない主体がロボットの挙動への影響力を得る。 |
| `unsafe-success` | 安全性を損なった状態でタスクが成功する。 |
| `policy-violation` | エージェントが明示的に禁止された、または有害な行動を実行する。 |
| `privacy-leakage` | 機微な情報が推測・露出・送信される。 |
| `availability-loss` | システムがフリーズ・停止・遅延、またはサービス拒否状態になる。 |

既存の`risks`フィールドは別個のまま残り、異なる役割を担います。`risks`は実証的に評価された広いリスク領域（セクション1）を記録し、`consequence`は脅威経路が表す具体的な到達点を記録します。どちらからもう一方を復元することはできません。

### 具体的な研究の例

```json
"threat_model": {
  "kind": "adversarial",
  "lifecycle": ["inference"],
  "mechanism": ["adversarial-patch"],
  "surface": ["visual-perception"],
  "target": ["vla-policy"],
  "consequence": ["task-failure"],
  "curation_status": "paper-verified"
}
```

### バックドアの例

```json
"threat_model": {
  "kind": "adversarial",
  "lifecycle": ["training", "inference"],
  "mechanism": ["backdoor"],
  "surface": ["model-supply-chain", "visual-perception"],
  "target": ["action-generation"],
  "consequence": ["targeted-action", "task-failure"],
  "curation_status": "paper-verified"
}
```

### サーベイ・広範な評価のレコード

サーベイや広範なベンチマークには、単一の標的や帰結を捏造して割り当てるべきではありません。代わりにcoverage（カバレッジ）バリアントを使用します。安全機構を分析しない一般的なサーベイは空の`mechanisms`リストを、広範な安全・セキュリティサーベイは`["multiple"]`を使用できます。

```json
"threat_model": {
  "kind": "survey",
  "coverage": {
    "lifecycles": ["training", "inference", "system"],
    "mechanisms": ["multiple"],
    "curation_status": "abstract-verified",
    "surfaces": [
      "model-supply-chain",
      "user-instruction",
      "context-memory-retrieval",
      "physical-semantic-environment",
      "visual-perception",
      "audio-perception",
      "proprioception",
      "world-state",
      "reasoning-representation",
      "task-planning",
      "action-interface",
      "middleware-network",
      "multi-agent-communication",
      "execution-control"
    ]
  }
}
```

### READMEでの表示

READMEは単一の`Threat Model`列を保持します。生成器は構造化メタデータを、明快なジュエルトーンのパレット（lifecycleはペリウィンクルブルー、surfaceはミントティール、mechanismはコーラル、targetはバイオレット、consequenceはピンクラズベリー）を用いて2行のコンパクトな要約としてレンダリングします。`+N`サフィックスは`data/papers.json`に保持されている追加の値を示します。

| 研究タイプ | 表示例 |
|---|---|
| Adversarial patch | `Inference` `Visual Perception`<br>`Adversarial Patch` → `VLA Policy` → `Task Failure` |
| Backdoor | `Training → Inference` `Model Supply Chain +1`<br>`Backdoor` → `Action Generation` → `Targeted Action` |
| OOD evaluation | `Inference` `Visual Perception`<br>`Distribution Shift` → `VLA Policy` → `Task Failure` |
| Runtime defense | `Inference` `Action Interface`<br>`Unsafe Policy Behavior` → `Runtime Monitor` → `Collision` |
| Survey | `Cross-lifecycle` `Multiple surfaces`<br>`Survey coverage` |

詳細な攻撃連鎖は、カタログメタデータではなく対応する論文のノートや一次資料に記載します。これにより、論文が明示的に確立していない伝播ステップをエンコードすることを避けます。

## 4. OOD汎化の軸

OOD汎化は攻撃のサブタイプではなく、独立したファーストクラスのセクションです。

- **視覚的な見た目:** テクスチャ、色、照明、背景
- **視点・カメラ:** カメラの姿勢、カメラの種類、順序、または視点の欠落
- **物体の幾何・空間配置:** 形状、サイズ、関節構造、配置
- **言語・指示:** 言い換え、曖昧さ、未知の組み合わせ
- **タスクの構成性:** 未知のタスク、長期ホライズン、サブタスクの組み合わせ
- **環境・ドメイン:** 新しい部屋、雑然とした環境、動態、sim-to-real転移
- **身体（embodiment）:** ロボットの形態、行動空間、制御周波数
- **時間的ダイナミクス:** レイテンシ、非同期観測、動く物体

## 5. 評価レベル

- 知覚・意味的な正確性
- 指示・視覚・行動の整合性
- 行動予測の品質
- 軌道逸脱・制約違反
- タスク成功・安全性を損なう成功
- 物理的危害、ニアミス、危険指示への拒否
- インタラクティブな緩和・リカバリ
- 不確実性・キャリブレーション
- 実機ロボットでの検証

## 採録基準

physical AIの安全性または信頼できる実運用を研究しており、かつ以下のいずれかに該当する論文を採録します。

1. VLA、ロボットポリシー、自動運転システム、身体性AIエージェントの安全性・堅牢性・セキュリティ・プライバシー・悪用・信頼できる評価を直接研究している。
2. 物理的インタラクションや実運用に関連する身体化された失敗・攻撃・人への影響を分析している。
3. physical AIの挙動に対するOOD・安全性・社会的評価プロトコルを提案している。
4. 身体性システム向けの防御・ランタイムモニター・ガードレール・action shield・フェイルセーフ・リカバリ機構を提案している。

physical AIリスクや信頼できる実運用との明示的な関連がない限り、汎用VLM・LLM・ロボティクス・能力系の論文は採録しません。

## 分類ルール

各論文には1つのカタログレコードと1つの主たる貢献セクションを割り当てます。横断的な性質は`risks`と`tags`で表現し、生成されたテーマ別ビューは重複エントリを作成することなく同じレコードを表示できます。

人の主観的なprivacy・trust・fairnessを扱い、特定の脅威・失敗mechanismを実証していない評価研究では、`coverage.mechanisms` を空リストにできます。攻撃や因果的な失敗経路を推測で割り当てることを避けるための扱いです。

### Subsection

主たる`section`の中で、各レコードにはさらに細かい`subsection`を1つ割り当てます。これはsection内のテーブルを閲覧しやすくするための2段階目の分類です。`section`と同様に`subsection`もクローズド語彙で、現在の正式な一覧は`scripts/validate_catalog.py`の`SUBSECTIONS[section]`にあります。以下は参照用に転記したものです。

**surveys**: Domain-Specific Surveys · Embodied AI Safety and Security · General VLA Surveys · Governance and Deployment Assurance · Position Papers and Research Agendas · Privacy, Fairness, and Human-Robot Trust · Training and Adaptation Surveys · World Model Safety and Security

**ood-generalization**: Action and Spatial Generalization · Driving Robustness and Generalization · Language and Instruction Generalization · OOD and Generalization · Open-World Evaluation · Reliability-Oriented Policy Refinement · Representation and Language-Action Generalization

**training-attacks**: Backdoors and Data Poisoning · Privacy and Data Leakage

**inference-attacks**: Jailbreaks and Prompt Injection · Planning, Action, and Trajectory Manipulation · Privacy and Data Leakage · Sensor, State, and Physical Interventions · Upstream VLM Attacks · Visual Perturbations and Patches

**defenses**: Failure Detection, Shielding, and Recovery · Model Unlearning and Data Governance · Multimodal Perception and Physical Safeguards · Privacy-Preserving Perception · Representation Steering and Inference-Time Defense · Runtime Monitoring and Guardrails · Safety Requirements and Assurance · Safety-Aligned and Robust Policy Training · System and Communication Defenses · Uncertainty, Abstention, and Human Oversight

**benchmarks**: Adversarial and Physical Robustness · Evaluation Infrastructure · Failure Detection and Recovery · Governance and Deployment Assurance · Human-Robot Trust and Fairness · Privacy and Data Leakage · Robustness, Uncertainty, and OOD Generalization · Safety-Critical Perception Evaluation · Semantic and Ethical Safety · Task and Physical Safety

**system-security**: Cross-Layer System Security · Privacy, Misuse, and Covert Channels

同じsubsection名が複数のsectionにまたがって存在することがあります（例: "Failure Detection and Recovery"は`defenses`と`benchmarks`の両方、"Privacy and Data Leakage"は3つの攻撃・ベンチマーク系sectionに存在）。これは同じテーマを異なる貢献タイプ（防御する／ベンチマークする／攻撃に利用する）から扱っているためであり、重複ではありません。

論文をキュレーションする際は、既存のsubsectionに妥当に当てはまる場合はそれを再利用してください。本当にどれにも当てはまらない場合のみ新しい値を追加し、その際は同じコミットで`scripts/validate_catalog.py`の`SUBSECTIONS[section]`と`scripts/labels_ja.py`の`SUBSECTIONS_JA`の両方を更新してください。運用ルールの詳細は[メタデータスキーマ](metadata-schema.md#subsection)を参照してください。
