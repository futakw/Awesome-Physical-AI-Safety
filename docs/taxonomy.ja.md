# Taxonomyとキュレーション方針

[English](taxonomy.md) | **日本語（このページ）**

> 統制語彙（`kind`・`lifecycle`・`mechanism`・`surface`・`target`・`consequence`などの実際の値）は`data/papers.json`との一貫性のため英語のまま記載しています。日本語は説明文のみです。

このリポジトリは多軸のtaxonomyを使用しています。論文の主要セクションはその研究の主たる貢献を表し、独立したメタデータがリスクにさらされるアウトカム・失敗要因・メカニズム・評価体制を記述します。

## 1. 実証的に評価されたリスクアウトカム

`risks`フィールドはevidence-coded（証拠に基づく）であり、起こりうる結果の一覧ではありません。論文の実験が当該アウトカムの指標を報告している場合にのみラベルが付与されます。4つのリスクすべてを論じるsurvey論文は空のリストを持つ一方、攻撃論文がタスク成功率と攻撃成功率の両方を報告していれば`Task Success`と`Security & Privacy`の両方が付与されることがあります。物理環境での実行だけでは`Physical Safety`ラベルの根拠にはなりません。

### タスク・信頼性リスク（Task and Reliability Risk）

タスクまたは経路の完了、成功率、またはそれに相当するend-to-endの実行結果。行動の逸脱、検知精度、キャリブレーション誤差、攻撃成功のみでは該当しません。

### 物理的安全性リスク（Physical Safety Risk）

衝突、人への傷害、物体・環境への損害、安全でない力や動作、物理的危害の実行、安全制約違反、または明示的な物理リスクの代理指標。

### 倫理・社会的リスク（Ethical and Societal Risk）

有害または禁止された指示への準拠・拒否、方針や憲章（constitution）の違反、明示的に測定された有害な身体化行動、またはアクセス・タスク成功・支援品質・危険への曝露における人や集団間の測定された格差。公平性への動機、モデルの帰納バイアス、ベンチマークによる「公平な評価」を謳う文言だけでは、対応する社会的アウトカムの指標がない限り該当しません。

### セキュリティ・プライバシーリスク（Security and Privacy Risk）

攻撃成功、バックドア起動、不正な制御、コマンド乗っ取り、情報漏洩、秘密裏の通信、メモリや通信の侵害、システム侵害。

### 付与ルール

1. 実験で実際に報告されている指標を特定する。
2. それらの指標のみを上記4つのアウトカムに対応付ける。
3. タイトル、動機、実運用設定、または仮想的な下流の帰結からラベルを付与しない。
4. 対応する報告指標がない場合は空の`risks`リストを使用する。READMEでは`—`と表示される。

## 2. 失敗要因

### Adversarial（敵対的・悪意のある操作）

攻撃者が入力・学習データ・モデル状態・行動・環境・システム構成要素を意図的に操作する。

### Non-Adversarial（非敵対的）・OOD

攻撃者を想定せず、未知の視点・見た目・物体・幾何・言語・タスク・環境・身体・時間変化のもとでシステムが失敗する。

### Design, Training, or System Failure（設計・学習・システムの失敗）

目的の誤設定、マルチモーダル不整合、報酬ハッキング、センサ故障、プランナー・実行系の不整合、または不十分なランタイムリカバリから生じる失敗。

## 3. 構造化されたThreat Model

> **ステータス: 採用済み。** 全てのカタログレコードとREADME生成器はこのスキーマを使用します。

`threat_model`フィールドはコンパクトな自由記述文字列ではなく、構造化されたオブジェクトです。脅威が「いつ」発生し、「どのように」作用し、「どのシステム境界」を使い、「何を」標的とし、「どんな帰結」を生むかを分離します。

### コアフィールド

| フィールド | 型 | 具体的な研究で必須か | 意味 | 例 |
|---|---|---:|---|---|
| `kind` | string | Yes | 失敗の大まかな発生源、またはレコードの範囲 | `adversarial` |
| `lifecycle` | 文字列の配列 | Yes | 脅威が導入・発動される段階、または失敗が評価される段階 | `training`, `inference` |
| `mechanism` | 文字列の配列 | Yes | 攻撃・シフト・失敗がどのように生じるか | `adversarial-patch` |
| `surface` | 文字列の配列 | Yes | 脅威・シフト・失敗が導入または観測される直接のシステム境界 | `visual-perception` |
| `target` | 文字列の配列 | Yes | 影響を受ける、または評価されるコンポーネント・表現・資産 | `vla-policy` |
| `consequence` | 文字列の配列 | Yes | 脅威・失敗連鎖の具体的な到達点 | `task-failure` |

このリポジトリは記述的な意味ラベルを使用します。個々の論文やサーベイが定義した番号付きサーフェスコードを正規のメタデータとしては使用しません。

### Threat Kinds（脅威の種別）

| 値 | 使用する場合 |
|---|---|
| `adversarial` | 攻撃者が学習・入力・状態・モデル・行動・インフラを意図的に操作する。 |
| `non-adversarial` | 研究が攻撃者を想定せず、OODシフト・曖昧さ・不確実性・自然発生的な失敗を評価する。 |
| `system-failure` | 失敗がシステム設計・統合・コントローラー・リカバリ・インフラの挙動に起因する。 |
| `evaluation` | ベンチマークが複数の異なる脅威をカバーし、単一の主要な脅威経路を持たない。 |
| `survey` | サーベイやポジションペーパーが、単一の具体的な脅威ではなく脅威のランドスケープを記述する。 |

### Lifecycle語彙

| 値 | 定義 |
|---|---|
| `training` | データ収集、事前学習、ファインチューニング、post-training、モデルマージ、またはチェックポイント配布。 |
| `inference` | デプロイ時の知覚・推論・計画・行動生成・ランタイムでのインタラクション。 |
| `system` | ミドルウェア、ネットワーキング、外部サービス、マルチエージェント、または実行インフラ。 |

`lifecycle`はマルチラベルです。バックドアは`training`中に埋め込まれ、`inference`中に発動することがあります。

### Surface語彙

| 値 | 表す境界 |
|---|---|
| `model-supply-chain` | 学習データ、アダプタ、チェックポイント、事前学習済みコンポーネント、またはモデル配布。 |
| `user-instruction` | 現在のタスクや制御意図として受理される、認証済みのテキストまたは音声。 |
| `context-memory-retrieval` | インタラクション履歴、永続メモリ、ICL例、RAGドキュメント、またはツール結果。 |
| `physical-semantic-environment` | シーン中のテキスト、標識、ラベル、ディスプレイ、QRコードなど、正しく知覚された意味的コンテンツ。 |
| `visual-perception` | 画像、動画、カメラ、視覚トークン、パッチ、テクスチャ、または光学信号。 |
| `audio-perception` | 音声、マイク、音響信号、または音声特徴量。 |
| `proprioception` | 関節状態、力、触覚フィードバック、またはロボット内部のセンシング。 |
| `world-state` | 物体間の関係、占有状況、位置推定、シーングラフ、アフォーダンス、または予測された状態。 |
| `reasoning-representation` | 隠れ状態、アテンション、chain-of-thought、またはクロスモーダル表現。 |
| `task-planning` | 目標、タスク分解、行動順序、経路、またはリカバリ戦略。 |
| `action-interface` | 行動トークン、行動チャンク、コード、ツール呼び出し、API、スキル、または連続制御。 |
| `middleware-network` | ROS/ROS2、DDS、ドライバ、認証情報、クラウドモデル、リモートAPI、または通信。 |
| `multi-agent-communication` | ロボット間メッセージ、共有メモリ、主張、または協調状態。 |
| `execution-control` | 軌道、アクチュエータコマンド、安全停止、フリーズ、またはリソース可用性。 |

`surface`は研究が直接操作・シフト・破損・評価したインターフェースのみを記録します。推測される内部伝播経路はエンコードしません。異なるlifecycle段階で異なるインターフェースが使われる場合、複数の値が許容されます。例えば、視覚的に発動するバックドアは学習時に`model-supply-chain`、推論時に`visual-perception`の両方を使うことがあります。

### Mechanism語彙

| ファミリー | 値の例 |
|---|---|
| 学習・サプライチェーン | `data-poisoning`, `backdoor`, `malicious-adapter`, `checkpoint-compromise`, `reward-manipulation` |
| 視覚・物理入力 | `digital-perturbation`, `adversarial-patch`, `adversarial-object`, `typographic-injection`, `environment-manipulation` |
| 言語・文脈 | `jailbreak`, `direct-prompt-injection`, `indirect-prompt-injection`, `command-hijacking`, `memory-poisoning`, `retrieval-poisoning` |
| センサー・状態 | `sensor-spoofing`, `state-manipulation`, `feedback-spoofing`, `multimodal-desynchronization` |
| 推論・計画・行動 | `representation-hijacking`, `planning-hijacking`, `action-manipulation`, `action-freezing`, `trajectory-manipulation` |
| システム・通信 | `middleware-compromise`, `network-attack`, `multi-agent-propagation`, `denial-of-service`, `sensitive-data-exposure`, `memorized-data-retention`, `covert-channel` |
| 非敵対的・システム失敗 | `distribution-shift`, `instruction-ambiguity`, `perception-error`, `semantic-misalignment`, `planning-error`, `execution-error`, `constraint-violation`, `uncertainty-miscalibration`, `unsafe-policy-behavior` |

### Target語彙

| 値 | 対象 |
|---|---|
| `perception-model` | 視覚・音声・マルチモーダル知覚コンポーネント。 |
| `world-state` | 下流の意思決定に使われる構造化・予測された状態。 |
| `reasoning-process` | 内部推論、アテンション、またはマルチモーダル整合。 |
| `task-planner` | 目標選択、タスク分解、経路、または高レベルのポリシー意図。 |
| `vla-policy` | end-to-end、または部分的に公開されたVLAポリシー。 |
| `action-generation` | 行動トークン、チャンク、軌道、コード、またはツール生成。 |
| `runtime-monitor` | ガードレール、検証器、検知器、または安全性判定器。 |
| `robot-executor` | コントローラー、アクチュエータ、安全停止、または実行プロセス。 |
| `shared-system-state` | メモリ、ミドルウェア、クラウドサービス、またはマルチエージェント間の共有状態。 |
| `private-data` | 学習メンバーシップ、観測、識別情報、位置情報などの機微データ。 |

### Consequence語彙

| 値 | 具体的な到達点 |
|---|---|
| `task-failure` | 割り当てられたタスクや経路が完了しない。 |
| `targeted-action` | システムが攻撃者の選択した行動または行動系列を実行する。 |
| `action-freezing` | ポリシーが停止する、または危険な無行動を生じる。 |
| `unsafe-success` | 安全性を損なった状態でタスクが成功する。 |
| `collision` | ロボットが障害物・人・禁止された物体に接触する。 |
| `unsafe-motion` | 安全でない力・速度・姿勢・軌道・制御挙動が発生する。 |
| `physical-damage` | 人・ロボット・物体・環境に危害や損害が生じる。 |
| `control-hijacking` | 権限のない主体がロボットの挙動への影響力を得る。 |
| `policy-violation` | エージェントが明示的に禁止された、または有害な行動を実行する。 |
| `privacy-leakage` | 機微な情報が推測・露出・送信される。 |
| `availability-loss` | システムがフリーズ・停止・遅延、またはサービス拒否状態になる。 |
| `recovery-failure` | 検知・緩和・再計画・リカバリが安全な動作を回復できない。 |

既存の`risks`フィールドは別個のまま残ります。`risks`は実証的に評価されたアウトカムのファミリーを記録し、`consequence`は脅威経路が表す具体的な到達点を記録します。

### 具体的な研究の例

```json
"threat_model": {
  "kind": "adversarial",
  "lifecycle": ["inference"],
  "mechanism": ["adversarial-patch"],
  "surface": ["visual-perception"],
  "target": ["vla-policy"],
  "consequence": ["task-failure"]
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
  "consequence": ["targeted-action", "task-failure"]
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
