"""Japanese display-label dictionaries for the catalog taxonomy and structure.

Keys are the canonical English values used in data/papers.json. Any value not
present here falls back to the English display label (see display_label_ja in
build_readme_ja.py) so that new taxonomy values or subsections introduced by
daily curation never break the Japanese build — they just render in English
until a translation is added here.
"""

SECTIONS_JA = {
    "surveys": "サーベイと展望",
    "ood-generalization": "堅牢性とOOD汎化",
    "training-attacks": "学習時攻撃",
    "inference-attacks": "推論時攻撃",
    "defenses": "防御と安全機構",
    "benchmarks": "ベンチマークと評価",
    "system-security": "システムレベルのセキュリティ・プライバシー・悪用",
}

SUBSECTIONS_JA = {
    "Action Shielding, Fail-Safes, and Recovery": "行動シールディング・フェイルセーフ・リカバリ",
    "Action and Spatial Generalization": "行動・空間汎化",
    "Active Perception and Recovery": "能動知覚とリカバリ",
    "Adversarial and Physical Robustness": "敵対的・物理的堅牢性",
    "Backdoors and Data Poisoning": "バックドアとデータ汚染",
    "Comprehensive VLA Evaluation": "VLAの包括的評価",
    "Cross-Layer System Security": "レイヤー横断システムセキュリティ",
    "Data, Model, and Supply-Chain Attacks": "データ・モデル・サプライチェーン攻撃",
    "Domain-Specific Surveys": "ドメイン特化サーベイ",
    "Driving Robustness and Generalization": "自動運転の堅牢性・汎化",
    "Embodied AI Safety and Security": "身体性AIの安全性とセキュリティ",
    "Evaluation Infrastructure": "評価インフラ",
    "Failure Detection and Recovery": "失敗検知とリカバリ",
    "General VLA Surveys": "一般的VLAサーベイ",
    "Geometry and Object-Centric Stress Testing": "幾何・物体中心のストレステスト",
    "Human-in-the-Loop Safety Refinement": "Human-in-the-Loopによる安全性改善",
    "Jailbreaks and Prompt Injection": "ジェイルブレイクとプロンプトインジェクション",
    "Language and Instruction Generalization": "言語・指示の汎化",
    "Language and Instruction Robustness": "言語・指示の堅牢性",
    "Model Unlearning and Data Governance": "モデルアンラーニングとデータガバナンス",
    "Multimodal Perception and Physical Safeguards": "マルチモーダル知覚と物理的セーフガード",
    "OOD and Generalization Benchmarks": "OOD・汎化ベンチマーク",
    "Open-World Evaluation": "オープンワールド評価",
    "Planning, Action, and Trajectory Manipulation": "計画・行動・軌道操作",
    "Position Papers and Research Agendas": "ポジションペーパーと研究課題",
    "Privacy and Data Leakage": "プライバシーとデータ漏洩",
    "Privacy, Misuse, and Covert Channels": "プライバシー・悪用・秘密通信路",
    "Privacy-Preserving Perception": "プライバシー保護知覚",
    "Reliability-Oriented Policy Refinement": "信頼性志向のポリシー改善",
    "Representation Steering and Inference-Time Defense": "表現操作と推論時防御",
    "Representation and Language-Action Generalization": "表現・言語行動汎化",
    "Robust Training and Safety Alignment": "頑健な学習と安全アライメント",
    "Robustness and Uncertainty Evaluation": "堅牢性と不確実性の評価",
    "Runtime Monitoring and Guardrails": "ランタイム監視とガードレール",
    "Runtime Observation Interventions": "ランタイム観測介入",
    "Safety and Hazard Benchmarks": "安全性・ハザードベンチマーク",
    "Safety-Aware Policy Learning": "安全性を考慮したポリシー学習",
    "Safety-Critical Perception Evaluation": "安全重視知覚評価",
    "Semantic and Ethical Safety": "意味的・倫理的安全性",
    "Sensor, State, and Physical Interventions": "センサー・状態・物理的介入",
    "System and Communication Defenses": "システム・通信防御",
    "Task and Physical Safety": "タスクと物理的安全性",
    "Training and Adaptation Surveys": "学習・適応サーベイ",
    "Uncertainty, Abstention, and Human Oversight": "不確実性・棄却・人間による監督",
    "Upstream VLM Attacks": "上流VLMへの攻撃",
    "VLA Safety Surveys": "VLA安全性サーベイ",
    "Visual Perturbations and Patches": "視覚摂動とパッチ",
}

RISK_LABELS_JA = {
    "task-reliability": "タスク",
    "physical-safety": "物理的安全性",
    "ethical-societal": "倫理・社会",
    "security-privacy": "セキュリティ/プライバシー",
}

LIFECYCLE_JA = {
    "training": "学習",
    "inference": "推論",
    "system": "システム",
}

SURFACE_JA = {
    "model-supply-chain": "モデルサプライチェーン",
    "user-instruction": "ユーザー指示",
    "context-memory-retrieval": "文脈・メモリ・検索",
    "physical-semantic-environment": "物理的意味環境",
    "visual-perception": "視覚",
    "audio-perception": "聴覚",
    "proprioception": "固有受容感覚",
    "world-state": "世界状態",
    "reasoning-representation": "推論表現",
    "task-planning": "タスク計画",
    "action-interface": "行動インターフェース",
    "middleware-network": "ミドルウェア・ネットワーク",
    "multi-agent-communication": "マルチエージェント通信",
    "execution-control": "実行制御",
}

MECHANISM_JA = {
    "action-manipulation": "行動操作",
    "adversarial-object": "敵対的物体",
    "adversarial-patch": "敵対的パッチ",
    "backdoor": "バックドア",
    "checkpoint-compromise": "チェックポイント侵害",
    "command-hijacking": "コマンド乗っ取り",
    "constraint-violation": "制約違反",
    "covert-channel": "秘密通信路",
    "data-poisoning": "データ汚染",
    "digital-perturbation": "デジタル摂動",
    "direct-prompt-injection": "直接プロンプトインジェクション",
    "distribution-shift": "分布シフト",
    "environment-manipulation": "環境操作",
    "execution-error": "実行エラー",
    "hazardous-instruction": "危険指示",
    "indirect-prompt-injection": "間接プロンプトインジェクション",
    "instruction-ambiguity": "指示の曖昧性",
    "jailbreak": "ジェイルブレイク",
    "memorized-data-retention": "記憶データの保持",
    "memory-poisoning": "メモリ汚染",
    "middleware-compromise": "ミドルウェア侵害",
    "multi-agent-propagation": "マルチエージェント伝播",
    "multimodal-desynchronization": "マルチモーダル非同期",
    "multiple": "複数",
    "network-attack": "ネットワーク攻撃",
    "perception-error": "知覚エラー",
    "planning-error": "計画エラー",
    "planning-hijacking": "計画乗っ取り",
    "representation-hijacking": "表現乗っ取り",
    "semantic-misalignment": "意味的不整合",
    "sensitive-data-exposure": "機微データ露出",
    "sensor-spoofing": "センサースプーフィング",
    "state-manipulation": "状態操作",
    "trajectory-manipulation": "軌道操作",
    "typographic-injection": "文字列インジェクション",
    "uncertainty-miscalibration": "不確実性のキャリブレーション誤り",
    "unsafe-policy-behavior": "安全でないポリシー挙動",
}

TARGET_JA = {
    "action-generation": "行動生成",
    "perception-model": "知覚モデル",
    "private-data": "プライベートデータ",
    "reasoning-process": "推論プロセス",
    "robot-executor": "ロボット実行系",
    "runtime-monitor": "ランタイムモニター",
    "shared-system-state": "共有システム状態",
    "task-planner": "タスクプランナー",
    "vla-policy": "VLAポリシー",
    "world-state": "世界状態",
}

CONSEQUENCE_JA = {
    "action-freezing": "行動フリーズ",
    "availability-loss": "可用性喪失",
    "collision": "衝突",
    "control-hijacking": "制御乗っ取り",
    "physical-damage": "物理的損害",
    "policy-violation": "方針違反",
    "privacy-leakage": "プライバシー漏洩",
    "recovery-failure": "リカバリ失敗",
    "targeted-action": "標的化された行動",
    "task-failure": "タスク失敗",
    "unsafe-motion": "安全でない動作",
    "unsafe-success": "安全性を損なう成功",
}

KIND_JA = {
    "survey": "サーベイ",
    "evaluation": "評価",
}

DISPLAY_LABELS_JA: dict[str, str] = {}
for table in (
    SURFACE_JA,
    MECHANISM_JA,
    TARGET_JA,
    CONSEQUENCE_JA,
    LIFECYCLE_JA,
):
    DISPLAY_LABELS_JA.update(table)
