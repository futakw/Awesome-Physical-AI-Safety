# Physical AI Safety Taxonomy

本カタログ独自の6軸taxonomyは、[Futa Waseda](https://futa-waseda.netlify.app/)が設計し、関連研究を踏まえて継続的に洗練しています。taxonomyの改善案は[GitHub Issue](https://github.com/futakw/Awesome-Physical-AI-Safety/issues/new)からお寄せください。

## Taxonomyの読み方

<p align="center">
  <a href="../visualizations/00_Taxonomy_example.png">
    <img src="../visualizations/00_Taxonomy_example.png" alt="具体例：視覚的adversarial patch攻撃を6つのtaxonomy軸すべてにマッピング" width="100%">
  </a>
</p>

本カタログの各論文は、6つの相補的なtaxonomy軸で記述されます。上の例は、1本の論文を6つの軸すべてにマッピングする方法を示します。

| 軸 | 主な問い |
|---|---|
| **WHEN** | いつ発生するか？ |
| **WHERE** | 脅威はどこから導入される、またはどこで評価されるか？ |
| **HOW** | どの攻撃手法・失敗モードを扱うか？ |
| **TARGET** | 攻撃・評価の対象は何か？ |
| **CONSEQUENCE** | 結果として何が起こるか？ |
| **MEASURED RISK** | どのリスクを実証的に評価したか？ |

## 概要

<p align="center">
  <a href="../visualizations/0_Taxonomy_Overview.png">
    <img src="../visualizations/0_Taxonomy_Overview.png" alt="Physical AI Safety taxonomyの6軸の概要" width="100%">
  </a>
</p>

## WHEN

WHENは、脅威が導入・発動される段階、または失敗が評価される段階を示します。複数の段階にまたがる場合もあり、例えばバックドアは学習時に埋め込まれ、推論時に発動します。

<p align="center">
  <a href="../visualizations/1_Taxonomy_When.png">
    <img src="../visualizations/1_Taxonomy_When.png" alt="WHEN軸：脅威・失敗が生じるlifecycleの段階" width="100%">
  </a>
</p>

<!-- taxonomy-sync:start lifecycle -->
| ラベル | 意味 |
|---|---|
| `training` | データ収集、事前学習、fine-tuning、post-training、model merging、checkpoint配布。 |
| `inference` | 実運用時の知覚、推論、計画、行動生成、interaction。 |
| `system` | middleware、network、外部service、multi-agent通信、実行基盤。 |
<!-- taxonomy-sync:end lifecycle -->

## WHERE

WHEREは、直接操作・変化・破損・評価されるsurfaceを表します。その後に影響を受けうる全ての内部componentを列挙する軸ではありません。

<p align="center">
  <a href="../visualizations/2_Taxonomy_Where.png">
    <img src="../visualizations/2_Taxonomy_Where.png" alt="WHERE軸：perceive-reason-actパイプライン上のsurface family" width="100%">
  </a>
</p>

<!-- taxonomy-sync:start surface -->
| Family | ラベル |
|---|---|
| **訓練・インフラ** | `model-supply-chain`, `middleware-network` |
| **知覚** | `visual-perception`, `audio-perception`, `physical-semantic-environment` |
| **言語** | `user-instruction`, `context-memory-retrieval`, `multi-agent-communication` |
| **固有受容感覚** | `proprioception` |
| **計画・状態** | `world-state`, `task-planning` |
| **推論** | `reasoning-representation` |
| **行動・制御** | `action-interface`, `execution-control` |
<!-- taxonomy-sync:end surface -->

例えば、camera画像内の印刷された指示は`physical-semantic-environment`、汚染された検索文書は`context-memory-retrieval`というsurfaceに対応します。

## HOW

HOWは、論文が扱う具体的な攻撃手法または失敗モードを表します。これはtechnique-orientedな軸であり、そのラベルが最深部の内部原因であると主張するものではありません。

<p align="center">
  <a href="../visualizations/3_Taxonomy_How.png">
    <img src="../visualizations/3_Taxonomy_How.png" alt="HOW軸：technique-orientedなmechanism family" width="100%">
  </a>
</p>

<!-- taxonomy-sync:start mechanism -->
| Family | ラベル |
|---|---|
| **データ・モデルへの攻撃** | `data-poisoning`, `backdoor`, `malicious-adapter`, `checkpoint-compromise`, `reward-manipulation`, `memory-poisoning`, `retrieval-poisoning`, `membership-inference` |
| **摂動・なりすまし** | `digital-perturbation`, `adversarial-patch`, `adversarial-object`, `sensor-spoofing`, `feedback-spoofing`, `environment-manipulation` |
| **命令・意味操作** | `direct-prompt-injection`, `indirect-prompt-injection`, `jailbreak`, `typographic-injection`, `hazardous-instruction` |
| **ランタイム・システム操作** | `middleware-compromise`, `network-attack`, `denial-of-service`, `covert-channel`, `state-manipulation`, `action-manipulation`, `trajectory-manipulation`, `representation-manipulation` |
| **分布シフト・不確実性** | `distribution-shift`, `instruction-ambiguity`, `uncertainty-miscalibration` |
| **推論・計画・実行の失敗** | `perception-error`, `semantic-misalignment`, `planning-error`, `execution-error`, `multimodal-desynchronization` |
<!-- taxonomy-sync:end mechanism -->

「データ・モデルへの攻撃」は、データやモデルの汚染・侵害に加え、それらから機微情報を推定する攻撃を含みます。Membership inferenceはデータやモデルの改変を必要としません。

## TARGET

TARGETは、研究が明示的に攻撃・保護・評価するcomponent、能力、資産を表します。system内部の因果経路を推定する軸ではありません。

<p align="center">
  <a href="../visualizations/4_Taxonomy_Target.png">
    <img src="../visualizations/4_Taxonomy_Target.png" alt="TARGET軸：明示的に攻撃・評価されるcomponent、能力、資産" width="100%">
  </a>
</p>

<!-- taxonomy-sync:start target -->
| Family | ラベル |
|---|---|
| **知覚・理解** | `perception-model` |
| **推論・計画・ポリシー** | `task-planner`, `reasoning-process`, `world-state`, `vla-policy` |
| **行動・システム運用** | `action-generation`, `robot-executor`, `runtime-monitor`, `shared-system-state` |
| **データ・プライバシー資産** | `private-data` |
<!-- taxonomy-sync:end target -->

画像を使った攻撃であるだけでは、TARGETが`perception-model`になるとは限りません。end-to-end policyの振る舞いだけを評価する研究では、`vla-policy`が適切な場合があります。

## CONSEQUENCE

CONSEQUENCEは、脅威・失敗経路が到達した具体的な結果を表します。familyを持たない、12ラベルのフラットな統制語彙です。

<!-- taxonomy-sync:start consequence -->
| ラベル | 結果 |
|---|---|
| `task-failure` | 与えられたtaskやrouteを完了できない。 |
| `recovery-failure` | 検知、緩和、再計画、復旧によって安全な動作へ戻れない。 |
| `collision` | robotが障害物、人、接触禁止物に接触する。 |
| `unsafe-motion` | 安全でない力、速度、姿勢、軌道、制御が生じる。 |
| `physical-damage` | 人、robot、物体、環境が負傷・破損する。 |
| `targeted-action` | 攻撃者が選んだ行動または行動列をsystemが実行する。 |
| `action-freezing` | policyが停止する、または危険な不作為を生む。 |
| `control-hijacking` | 権限のない主体がrobotの振る舞いに影響を与える。 |
| `unsafe-success` | taskは成功するが、安全性条件に違反する。 |
| `policy-violation` | agentが明示的に禁止された、または有害な振る舞いをする。 |
| `privacy-leakage` | 機微情報が推定・公開・送信される。 |
| `availability-loss` | systemが停止、遅延、service拒否の状態になる。 |
<!-- taxonomy-sync:end consequence -->

## MEASURED RISK

MEASURED RISKは、論文が実験で測定した広いrisk domainを表します。起こりうるリスクとして議論しただけでは付与せず、対応する評価指標が報告された場合に使います。

<p align="center">
  <a href="../visualizations/6_Taxonomy_MeasuredRisk.png">
    <img src="../visualizations/6_Taxonomy_MeasuredRisk.png" alt="MEASURED RISK軸：実証的に評価される4つの広いrisk domain" width="100%">
  </a>
</p>

<!-- taxonomy-sync:start risks -->
| Category | 代表的な根拠 |
|---|---|
| **タスク・信頼性** (`task-reliability`) | Task success、route completion、または同等のend-to-end結果。 |
| **物理的安全性** (`physical-safety`) | 衝突、損害、安全でない力・動作、明示的なphysical-risk proxy。 |
| **倫理・社会** (`ethical-societal`) | 有害行動、policy violation、refusal、人やgroup間の格差の測定。 |
| **セキュリティ・プライバシー** (`security-privacy`) | Attack success、不正制御、情報漏洩、system compromise。 |
<!-- taxonomy-sync:end risks -->

## 混同しやすい軸の違い

| 軸 | 覚えておく点 |
|---|---|
| **WHERE** | 操作・評価されるsurface、すなわち配送channelやsystem boundary。 |
| **HOW** | 研究対象の攻撃手法・失敗モード。必ずしもroot causeの説明ではない。 |
| **TARGET** | 研究が明示的に攻撃・保護・評価する対象。内部の因果mechanismを知っていることを意味しない。 |
| **CONSEQUENCE** | 具体的な結果。familyを持たない12ラベルのフラットな語彙。 |
| **MEASURED RISK** | 報告された指標で裏付けられる4つの広いrisk domain。 |

## 例

以下は特定の論文に対する完全なannotationではなく、説明用の例です。実運用中のVLAに可視的なadversarial patchを提示し、robotがtaskに失敗するかを評価する研究を考えます。

| 軸 | ラベル例 |
|---|---|
| WHEN | `inference` |
| WHERE | `visual-perception` |
| HOW | `adversarial-patch` |
| TARGET | `vla-policy` |
| CONSEQUENCE | `task-failure` |
| MEASURED RISK | `task-reliability`。attack successも報告する場合は`security-privacy`も該当。 |

厳密な定義、境界事例、annotation方針は[詳細なTaxonomy・Annotation Guidelines](../reference/taxonomy.ja.md)を参照してください。
