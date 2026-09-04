# Awesome Responsible VLA

A curated, taxonomy-driven list of research on the safety, robustness, security, and responsible deployment of Vision-Language-Action models and closely related embodied agents.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> This list separates **empirically evaluated risk outcomes** (what the paper measures) from **failure sources and mechanisms** (why it goes wrong). GitHub star badges are live and are shown only for identified official repositories.

## Taxonomy at a Glance

### Risk outcomes

A label is shown only when the paper reports a corresponding empirical outcome metric; discussion or potential impact alone does not qualify.

- **Task Success:** task or route completion, success rate, or equivalent execution outcome.
- **Physical Safety:** collision, damage, unsafe motion or force, physical harm, or safety-constraint violation.
- **Ethical Safety:** harmful-instruction compliance or refusal, prohibited behavior, or policy/constitution violation.
- **Security & Privacy:** attack success, backdoor activation, control hijacking, unauthorized access, leakage, or compromise.
- **—:** no directly corresponding outcome is empirically evaluated, as is common for surveys and diagnostic-only work.

### Failure sources

- **Adversarial:** malicious manipulation of inputs, training, states, actions, or system components.
- **Non-adversarial / OOD:** failures under unseen viewpoints, objects, language, tasks, environments, embodiments, or dynamics.
- **Design / system:** misalignment, misspecified objectives, sensor faults, planner-executor mismatch, or failed recovery.

See [the full taxonomy](docs/taxonomy.md) for definitions and inclusion rules.

## 🧭 Contents

- [📚 Surveys and Perspectives](#surveys)
  - [VLA Safety Surveys](#surveys-vla-safety-surveys)
  - [Embodied AI Safety and Security](#surveys-embodied-ai-safety-and-security)
  - [Domain-Specific Surveys](#surveys-domain-specific-surveys)
  - [Position Papers and Research Agendas](#surveys-position-papers-and-research-agendas)
  - [General VLA Surveys](#surveys-general-vla-surveys)
  - [Training and Adaptation Surveys](#surveys-training-and-adaptation-surveys)
- [🌍 Robustness and OOD Generalization](#ood-generalization)
  - [Representation and Language-Action Generalization](#ood-generalization-representation-and-language-action-generalization)
  - [Action and Spatial Generalization](#ood-generalization-action-and-spatial-generalization)
  - [Geometry and Object-Centric Stress Testing](#ood-generalization-geometry-and-object-centric-stress-testing)
  - [Language and Instruction Generalization](#ood-generalization-language-and-instruction-generalization)
  - [Open-World Evaluation](#ood-generalization-open-world-evaluation)
  - [Driving Robustness and Generalization](#ood-generalization-driving-robustness-and-generalization)
- [🧪 Training-Time Attacks](#training-attacks)
  - [Backdoors and Data Poisoning](#training-attacks-backdoors-and-data-poisoning)
- [⚡ Inference-Time Attacks](#inference-attacks)
  - [Visual Perturbations and Patches](#inference-attacks-visual-perturbations-and-patches)
  - [Planning, Action, and Trajectory Manipulation](#inference-attacks-planning-action-and-trajectory-manipulation)
  - [Sensor, State, and Physical Interventions](#inference-attacks-sensor-state-and-physical-interventions)
  - [Jailbreaks and Prompt Injection](#inference-attacks-jailbreaks-and-prompt-injection)
  - [Upstream VLM Attacks](#inference-attacks-upstream-vlm-attacks)
- [🛡️ Defenses and Safety Mechanisms](#defenses)
  - [Robust Training and Safety Alignment](#defenses-robust-training-and-safety-alignment)
  - [Runtime Monitoring and Guardrails](#defenses-runtime-monitoring-and-guardrails)
  - [Action Shielding, Fail-Safes, and Recovery](#defenses-action-shielding-fail-safes-and-recovery)
  - [Representation Steering and Inference-Time Defense](#defenses-representation-steering-and-inference-time-defense)
  - [System and Communication Defenses](#defenses-system-and-communication-defenses)
  - [Active Perception and Recovery](#defenses-active-perception-and-recovery)
  - [Multimodal Perception and Physical Safeguards](#defenses-multimodal-perception-and-physical-safeguards)
  - [Human-in-the-Loop Safety Refinement](#defenses-human-in-the-loop-safety-refinement)
  - [Runtime Observation Interventions](#defenses-runtime-observation-interventions)
  - [Reliability-Oriented Policy Refinement](#defenses-reliability-oriented-policy-refinement)
  - [Model Unlearning and Data Governance](#defenses-model-unlearning-and-data-governance)
  - [Safety-Aware Policy Learning](#defenses-safety-aware-policy-learning)
  - [Privacy-Preserving Perception](#defenses-privacy-preserving-perception)
  - [Failure Detection and Recovery](#defenses-failure-detection-and-recovery)
  - [Uncertainty, Abstention, and Human Oversight](#defenses-uncertainty-abstention-and-human-oversight)
- [📊 Benchmarks and Evaluation](#benchmarks)
  - [OOD and Generalization Benchmarks](#benchmarks-ood-and-generalization-benchmarks)
  - [Comprehensive VLA Evaluation](#benchmarks-comprehensive-vla-evaluation)
  - [Adversarial and Physical Robustness](#benchmarks-adversarial-and-physical-robustness)
  - [Task and Physical Safety](#benchmarks-task-and-physical-safety)
  - [Semantic and Ethical Safety](#benchmarks-semantic-and-ethical-safety)
  - [Evaluation Infrastructure](#benchmarks-evaluation-infrastructure)
  - [Safety and Hazard Benchmarks](#benchmarks-safety-and-hazard-benchmarks)
  - [Robustness and Uncertainty Evaluation](#benchmarks-robustness-and-uncertainty-evaluation)
  - [Safety-Critical Perception Evaluation](#benchmarks-safety-critical-perception-evaluation)
- [🔐 System-Level Security, Privacy, and Misuse](#system-security)
  - [Cross-Layer System Security](#system-security-cross-layer-system-security)
  - [Privacy, Misuse, and Covert Channels](#system-security-privacy-misuse-and-covert-channels)

**124 papers in the current catalog.**

<a id="surveys"></a>

## 📚 Surveys and Perspectives

<a id="surveys-vla-safety-surveys"></a>

### VLA Safety Surveys

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms](https://arxiv.org/abs/2604.23775)** [![GitHub stars](https://img.shields.io/github/stars/LiQiiiii/Awesome-VLA-Safety?style=social)](https://github.com/LiQiiiii/Awesome-VLA-Safety) | Li et al. | arXiv 2026 | — | `Cross-lifecycle` · `Multiple surfaces`<br>Survey coverage |

<a id="surveys-embodied-ai-safety-and-security"></a>

### Embodied AI Safety and Security

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Navigating Embodied Intelligence: Enabling Technologies, Security and Privacy, and Emerging Trends](https://doi.org/10.1109/JIOT.2025.3649049)** | Wang et al. | IEEE IoT Journal 2026 | — | `Cross-lifecycle` · `Multiple surfaces`<br>Survey coverage |
| **[What Breaks Embodied AI Security: LLM Vulnerabilities, CPS Flaws, or Something Else?](https://arxiv.org/abs/2602.17345)** | Ma et al. | arXiv 2026 | — | `Inference → System` · `Multiple surfaces`<br>Survey coverage |
| **[Towards Robust and Secure Embodied AI: A Survey on Vulnerabilities and Attacks](https://arxiv.org/abs/2502.13175)** | Xing et al. | arXiv 2025 | — | `Cross-lifecycle` · `Multiple surfaces`<br>Survey coverage |
| **[Towards Safe and Trustworthy Embodied AI: Foundations, Status, and Prospects](https://openreview.net/forum?id=Eu6Yt21Alv)** [![GitHub stars](https://img.shields.io/github/stars/AI45Lab/Awesome-Trustworthy-Embodied-AI?style=social)](https://github.com/AI45Lab/Awesome-Trustworthy-Embodied-AI) | Tan et al. | OpenReview 2025 | — | `Cross-lifecycle` · `Multiple surfaces`<br>Survey coverage |

<a id="surveys-domain-specific-surveys"></a>

### Domain-Specific Surveys

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[A Survey on Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2506.24044)** [![GitHub stars](https://img.shields.io/github/stars/JohnsonJiang1996/Awesome-VLA4AD?style=social)](https://github.com/JohnsonJiang1996/Awesome-VLA4AD) | Jiang et al. | arXiv 2025 | — | `Cross-lifecycle` · `Multiple surfaces`<br>Survey coverage |
| **[Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](https://arxiv.org/abs/2510.07077)** [Project / Code](https://vla-survey.github.io/) | Kawaharazuka et al. | IEEE Access 2025 | — | `Cross-lifecycle` · `Multiple surfaces`<br>Survey coverage |

<a id="surveys-position-papers-and-research-agendas"></a>

### Position Papers and Research Agendas

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Position: Human-Robot Interaction in Embodied Intelligence Demands a Shift From Static Privacy Controls to Dynamic Learning](https://arxiv.org/abs/2509.19041)** | Zhang et al. | NeurIPS Workshop 2025 | — | `Inference → System` · `Multiple surfaces`<br>Survey coverage |

<a id="surveys-general-vla-surveys"></a>

### General VLA Surveys

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey](https://arxiv.org/abs/2508.13073)** [![GitHub stars](https://img.shields.io/github/stars/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation?style=social)](https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation) | Shao et al. | arXiv 2025 | — | `Training → Inference` · `Multiple surfaces`<br>Survey coverage |
| **[Pure Vision Language Action (VLA) Models: A Comprehensive Survey](https://arxiv.org/abs/2509.19012)** | Zhang et al. | arXiv 2025 | — | `Training → Inference` · `Multiple surfaces`<br>Survey coverage |
| **[Vision Language Action Models in Robotic Manipulation: A Systematic Review](https://arxiv.org/abs/2507.10672)** [![GitHub stars](https://img.shields.io/github/stars/Muhayyuddin/VLAs?style=social)](https://github.com/Muhayyuddin/VLAs) | Din et al. | arXiv 2025 | — | `Training → Inference` · `Multiple surfaces`<br>Survey coverage |
| **[Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges](https://arxiv.org/abs/2505.04769)** [![GitHub stars](https://img.shields.io/github/stars/Applied-AI-Research-Lab/Vision-Language-Action-Models-Concepts-Progress-Applications-and-Challenges?style=social)](https://github.com/Applied-AI-Research-Lab/Vision-Language-Action-Models-Concepts-Progress-Applications-and-Challenges) | Sapkota et al. | arXiv 2025 | — | `Cross-lifecycle` · `Multiple surfaces`<br>Survey coverage |
| **[A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093)** [![GitHub stars](https://img.shields.io/github/stars/yueen-ma/Awesome-VLA?style=social)](https://github.com/yueen-ma/Awesome-VLA) | Ma et al. | arXiv 2024 | — | `Training → Inference` · `Multiple surfaces`<br>Survey coverage |

<a id="surveys-training-and-adaptation-surveys"></a>

### Training and Adaptation Surveys

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[A Survey on Efficient Vision-Language-Action Models](https://arxiv.org/abs/2510.24795)** [Project / Code](https://evla-survey.github.io/) | Yu et al. | arXiv 2025 | — | `Cross-lifecycle` · `Multiple surfaces`<br>Survey coverage |
| **[A Survey on Vision-Language-Action Models: An Action Tokenization Perspective](https://arxiv.org/abs/2507.01925)** | Zhong et al. | arXiv 2025 | — | `Training → Inference` · `Action Interface + Reasoning Representation`<br>Survey coverage |
| **[Parallels Between VLA Model Post-Training and Human Motor Learning: Progress, Challenges, and Trends](https://arxiv.org/abs/2506.20966)** [![GitHub stars](https://img.shields.io/github/stars/AoqunJin/Awesome-VLA-Post-Training?style=social)](https://github.com/AoqunJin/Awesome-VLA-Post-Training) | Xiang et al. | arXiv 2025 | — | `Training` · `Multiple surfaces`<br>Survey coverage |

<a id="ood-generalization"></a>

## 🌍 Robustness and OOD Generalization

<a id="ood-generalization-representation-and-language-action-generalization"></a>

### Representation and Language-Action Generalization

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](https://arxiv.org/abs/2607.13429)** [![GitHub stars](https://img.shields.io/github/stars/dwipddalal/Anchor-Align?style=social)](https://github.com/dwipddalal/Anchor-Align) | Dalal et al. | arXiv 2026 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Distribution Shift → VLA policy → Task Failure |
| **[Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization](https://arxiv.org/abs/2510.25616)** [Project / Code](https://blind-vla-paper.github.io/) | Kachaev et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `Visual Perception + Reasoning Representation`<br>Distribution Shift → VLA policy → Task Failure |

<a id="ood-generalization-action-and-spatial-generalization"></a>

### Action and Spatial Generalization

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior](https://arxiv.org/abs/2604.01570)** [![GitHub stars](https://img.shields.io/github/stars/Haochen-Niu/FAN-VLA?style=social)](https://github.com/Haochen-Niu/FAN-VLA) | Niu et al. | CVPR 2026 | •&nbsp;Task | `Inference` · `World State + Action Interface`<br>Distribution Shift → Action Generation → Task Failure |

<a id="ood-generalization-geometry-and-object-centric-stress-testing"></a>

### Geometry and Object-Centric Stress Testing

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Geometric Red-Teaming for Robotic Manipulation](https://arxiv.org/abs/2509.12379)** | Goel et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `Visual Perception + World State`<br>Distribution Shift → VLA policy → Task Failure |

<a id="ood-generalization-language-and-instruction-generalization"></a>

### Language and Instruction Generalization

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[ICR-Drive: Instruction Counterfactual Robustness for End-to-End Language-Driven Autonomous Driving](https://arxiv.org/abs/2604.05378)** [![GitHub stars](https://img.shields.io/github/stars/icrdrive/icrdrive?style=social)](https://github.com/icrdrive/icrdrive) | Hamid et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `User Instruction + World State`<br>Distribution Shift → Task Planner → Task Failure |

<a id="ood-generalization-open-world-evaluation"></a>

### Open-World Evaluation

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[How VLAs (Really) Work in Open-World Environments](https://arxiv.org/abs/2604.21192)** | Rasouli et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Visual Perception + World State`<br>Distribution Shift → VLA policy → Task Failure |
| **[pi0.5: A Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)** [![GitHub stars](https://img.shields.io/github/stars/Physical-Intelligence/openpi?style=social)](https://github.com/Physical-Intelligence/openpi) | Black et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Distribution Shift → VLA policy → Task Failure |

<a id="ood-generalization-driving-robustness-and-generalization"></a>

### Driving Robustness and Generalization

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Generative Scenario Rollouts for End-to-End Autonomous Driving](https://arxiv.org/abs/2601.11475)** | Yasarla et al. | arXiv 2026 | •&nbsp;Task | `Inference` · `World State + Task Planning`<br>Distribution Shift → Task Planner → Task Failure |
| **[Shift & Drift: A Zero-Shot Benchmark for Generalizable and Robust Autonomous Driving Motion Planning](https://arxiv.org/abs/2607.07844)** | Canevaro et al. | IROS 2026 | •&nbsp;Task | `Inference` · `World State + Execution Control`<br>Distribution Shift → Task Planner → Task Failure |

<a id="training-attacks"></a>

## 🧪 Training-Time Attacks

<a id="training-attacks-backdoors-and-data-poisoning"></a>

### Backdoors and Data Poisoning

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Inject Once Survive Later: Backdooring Vision-Language-Action Models to Persist Through Downstream Fine-tuning](https://arxiv.org/abs/2602.00500)** [Project / Code](https://jianyi2004.github.io/infuse-vla-backdoor/) | Zhou et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Training → Inference` · `Model Supply Chain + Visual Perception`<br>Backdoor → VLA policy → Targeted Action |
| **[SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2601.14323)** | Xu et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Training → Inference` · `Multiple surfaces`<br>Backdoor → Action Generation → Targeted Action |
| **[State Backdoor: Towards Stealthy Real-World Poisoning Attack on Vision-Language-Action Models in State Space](https://arxiv.org/abs/2601.04266)** | Guo et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Training → Inference` · `Multiple surfaces`<br>Backdoor → World State → Targeted Action |
| **[BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://arxiv.org/abs/2505.16640)** [![GitHub stars](https://img.shields.io/github/stars/Zxy-MLlab/BadVLA?style=social)](https://github.com/Zxy-MLlab/BadVLA) | Zhou et al. | NeurIPS 2025 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Training → Inference` · `Model Supply Chain + Visual Perception`<br>Backdoor → VLA policy → Targeted Action |
| **[Can We Trust Embodied Agents? Exploring Backdoor Attacks Against Embodied LLM-Based Decision-Making Systems](https://arxiv.org/abs/2405.20774)** [![GitHub stars](https://img.shields.io/github/stars/ASGuard-UCI/BALD?style=social)](https://github.com/ASGuard-UCI/BALD) | Jiao et al. | ICLR 2025 | •&nbsp;Security/Privacy | `Training → Inference` · `Model Supply Chain + User Instruction`<br>Backdoor → Task Planner → Targeted Action |
| **[DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models](https://arxiv.org/abs/2510.10932)** [![GitHub stars](https://img.shields.io/github/stars/megaknight114/DropVLA?style=social)](https://github.com/megaknight114/DropVLA) | Xu et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Training → Inference` · `Multiple surfaces`<br>Backdoor → Action Generation → Targeted Action |
| **[Goal-Oriented Backdoor Attack Against Vision-Language-Action Models via Physical Objects](https://arxiv.org/abs/2510.09269)** [Project / Code](https://goba-attack.github.io/) | Zhou et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Training → Inference` · `Multiple surfaces`<br>Backdoor → Task Planner → Targeted Action |

<a id="inference-attacks"></a>

## ⚡ Inference-Time Attacks

<a id="inference-attacks-visual-perturbations-and-patches"></a>

### Visual Perturbations and Patches

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.21192)** [![GitHub stars](https://img.shields.io/github/stars/yuyi-sd/UPA-RFAS?style=social)](https://github.com/yuyi-sd/UPA-RFAS) | Lu et al. | CVPR 2026 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Visual Perception`<br>Adversarial Patch → VLA policy → Task Failure |
| **[ADVEDM: Fine-Grained Adversarial Attack Against VLM-Based Embodied Agents](https://arxiv.org/abs/2509.16645)** | Wang et al. | NeurIPS 2025 | •&nbsp;Security/Privacy | `Inference` · `Visual Perception`<br>Digital Perturbation → Reasoning Process → Targeted Action |
| **[Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2411.13587)** [![GitHub stars](https://img.shields.io/github/stars/William-wAng618/roboticAttack?style=social)](https://github.com/William-wAng618/roboticAttack) | Wang et al. | ICCV 2025 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Visual Perception`<br>Adversarial Patch → VLA policy → Task Failure |
| **[Model-Agnostic Adversarial Attack and Defense for Vision-Language-Action Models](https://arxiv.org/abs/2510.13237)** [![GitHub stars](https://img.shields.io/github/stars/trustmlyoungscientist/EDPA_attack_defense?style=social)](https://github.com/trustmlyoungscientist/EDPA_attack_defense) | Xu et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Visual Perception`<br>Adversarial Patch → VLA policy → Task Failure |
| **[When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.16203)** | Yan et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Visual Perception + User Instruction`<br>Digital Perturbation → VLA policy → Task Failure |

<a id="inference-attacks-planning-action-and-trajectory-manipulation"></a>

### Planning, Action, and Trajectory Manipulation

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[FreezeVLA: Action-Freezing Attacks Against Vision-Language-Action Models](https://arxiv.org/abs/2509.19870)** [![GitHub stars](https://img.shields.io/github/stars/xinwong/FreezeVLA?style=social)](https://github.com/xinwong/FreezeVLA) | Wang et al. | arXiv 2025 | •&nbsp;Security/Privacy | `Inference` · `Visual Perception`<br>Digital Perturbation → Action Generation → Action Freezing |

<a id="inference-attacks-sensor-state-and-physical-interventions"></a>

### Sensor, State, and Physical Interventions

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Phantom Menace: Exploring and Enhancing the Robustness of VLA Models Against Physical Sensor Attacks](https://arxiv.org/abs/2511.10008)** | Lu et al. | AAAI 2026 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Multiple surfaces`<br>Sensor Spoofing → VLA policy → Task Failure |
| **[Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks](https://doi.org/10.1145/3733800.3763262)** [![GitHub stars](https://img.shields.io/github/stars/ZJUshine/lamps-vla-robustness.github.io?style=social)](https://github.com/ZJUshine/lamps-vla-robustness.github.io) | Lu et al. | LAMPS@CCS 2025 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Visual Perception + Audio Perception`<br>Sensor Spoofing → VLA policy → Task Failure |

<a id="inference-attacks-jailbreaks-and-prompt-injection"></a>

### Jailbreaks and Prompt Injection

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[CHAI: Command Hijacking Against Embodied AI](https://arxiv.org/abs/2510.00181)** [![GitHub stars](https://img.shields.io/github/stars/Cyphysecurity/chai?style=social)](https://github.com/Cyphysecurity/chai) | Burbano et al. | SaTML 2026 | •&nbsp;Security/Privacy | `Inference` · `Physical Semantic Environment`<br>Multiple mechanisms → Task Planner → Control Hijacking |
| **[If You're Waiting for a Sign... That Might Not Be It! Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems](https://arxiv.org/abs/2604.19844)** | Chang et al. | arXiv 2026 | •&nbsp;Security/Privacy | `Inference` · `Physical Semantic Environment`<br>Indirect Prompt Injection + Typographic Injection → Task Planner → Control Hijacking |
| **[Adversarial Attacks on Robotic Vision-Language-Action Models](https://arxiv.org/abs/2506.03350)** [![GitHub stars](https://img.shields.io/github/stars/eliotjones1/robogcg?style=social)](https://github.com/eliotjones1/robogcg) | Jones et al. | arXiv 2025 | •&nbsp;Physical<br>•&nbsp;Ethics<br>•&nbsp;Security/Privacy | `Inference` · `User Instruction`<br>Jailbreak + Command Hijacking → Task Planner → Policy Violation |
| **[BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://arxiv.org/abs/2407.20242)** [![GitHub stars](https://img.shields.io/github/stars/Rookie143/BadRobot?style=social)](https://github.com/Rookie143/BadRobot) | Zhang et al. | ICLR 2025 | •&nbsp;Physical<br>•&nbsp;Ethics<br>•&nbsp;Security/Privacy | `Inference` · `Audio Perception + User Instruction`<br>Jailbreak → Task Planner → Policy Violation |
| **[Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691)** [![GitHub stars](https://img.shields.io/github/stars/arobey1/robopair?style=social)](https://github.com/arobey1/robopair) | Robey et al. | ICRA 2025 | •&nbsp;Physical<br>•&nbsp;Ethics<br>•&nbsp;Security/Privacy | `Inference` · `User Instruction`<br>Jailbreak → Task Planner → Policy Violation |
| **[POEX: Towards Policy Executable Jailbreak Attacks Against the LLM-Based Robots](https://arxiv.org/abs/2412.16633)** [Project / Code](https://poex-jailbreak.github.io/) | Lu et al. | arXiv 2025 | •&nbsp;Physical<br>•&nbsp;Ethics<br>•&nbsp;Security/Privacy | `Inference` · `User Instruction`<br>Jailbreak → Task Planner → Policy Violation |
| **[The Shawshank Redemption of Embodied AI: Understanding and Benchmarking Indirect Environmental Jailbreaks](https://arxiv.org/abs/2511.16347)** [Project / Code](https://shawshankiej.github.io/) | Li et al. | arXiv 2025 | •&nbsp;Ethics<br>•&nbsp;Security/Privacy | `Inference` · `Physical Semantic Environment`<br>Indirect Prompt Injection + Environment Manipulation → Task Planner → Policy Violation |

<a id="inference-attacks-upstream-vlm-attacks"></a>

### Upstream VLM Attacks

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Chain of Attack: On the Robustness of Vision-Language Models Against Transfer-Based Adversarial Attacks](https://arxiv.org/abs/2411.15720)** [![GitHub stars](https://img.shields.io/github/stars/Shelton1013/Chain_of_Attack?style=social)](https://github.com/Shelton1013/Chain_of_Attack) | Xie et al. | CVPR 2025 | •&nbsp;Security/Privacy | `Inference` · `Visual Perception`<br>Digital Perturbation → Perception Model → Control Hijacking |

<a id="defenses"></a>

## 🛡️ Defenses and Safety Mechanisms

<a id="defenses-robust-training-and-safety-alignment"></a>

### Robust Training and Safety Alignment

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[SafeVLA: Towards Safety Alignment of Vision-Language-Action Models via Constrained Learning](https://arxiv.org/abs/2503.03480)** [![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/SafeVLA?style=social)](https://github.com/PKU-Alignment/SafeVLA) | Zhang et al. | NeurIPS 2025 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `User Instruction + Action Interface`<br>Constraint Violation → VLA policy → Task Failure |
| **[Safety Optimized Reinforcement Learning via Multi-Objective Policy Optimization](https://arxiv.org/abs/2402.15197)** | Honari et al. | arXiv 2024 | •&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Constraint Violation → Action Generation → Unsafe Motion |

<a id="defenses-runtime-monitoring-and-guardrails"></a>

### Runtime Monitoring and Guardrails

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Causal Scene Narration with Runtime Safety Supervision for Vision-Language-Action Driving](https://arxiv.org/abs/2604.01723)** | Li et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Planning Error → Task Planner → Task Failure |
| **[RC-NF: Robot-Conditioned Normalizing Flow for Real-Time Anomaly Detection in Robotic Manipulation](https://arxiv.org/abs/2603.11106)** | Zhou et al. | arXiv 2026 | — | `Inference` · `Proprioception + World State`<br>Execution Error → Action Generation → Recovery Failure |
| **[Safety Guardrails for LLM-Enabled Robots](https://arxiv.org/abs/2503.07885)** | Ravichandran et al. | IEEE RA-L 2026 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | `Inference` · `User Instruction + World State`<br>Jailbreak → Task Planner → Policy Violation |
| **[From Words to Safety: Language-Conditioned Safety Filtering for Robot Navigation](https://arxiv.org/abs/2511.05889)** | Feng et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `User Instruction + World State`<br>Constraint Violation → Action Generation → Task Failure |
| **[ROVER: Regulator-Driven Robust Temporal Verification of Black-Box Robot Policies](https://arxiv.org/abs/2511.17781)** | Sakano et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Action Interface + Execution Control`<br>Unsafe Policy Behavior → Action Generation → Task Failure |
| **[VLSA: Vision-Language-Action Models with a Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)** [![GitHub stars](https://img.shields.io/github/stars/THU-RCSCT/vlsa-aegis?style=social)](https://github.com/THU-RCSCT/vlsa-aegis) | Hu et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `User Instruction + Action Interface`<br>Constraint Violation → Action Generation → Task Failure |

<a id="defenses-action-shielding-fail-safes-and-recovery"></a>

### Action Shielding, Fail-Safes, and Recovery

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation](https://arxiv.org/abs/2601.15541)** [Project / Code](https://sites.google.com/view/compliantvla) | Zhang et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Proprioception + Action Interface`<br>Constraint Violation → Action Generation → Task Failure |
| **[VLA Knows Its Limits: Adaptive Execution Horizons for Robot Policies](https://arxiv.org/abs/2602.21445)** [Project / Code](https://hatchetproject.github.io/autohorizon/) | Wang et al. | ECCV 2026 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Execution Error → Action Generation → Task Failure |
| **[RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic](https://arxiv.org/abs/2512.21220)** | Wang et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Hazardous Instruction → Task Planner → Policy Violation |
| **[SAFE: Multitask Failure Detection for Vision-Language-Action Models](https://arxiv.org/abs/2506.09937)** [![GitHub stars](https://img.shields.io/github/stars/vla-safe/SAFE?style=social)](https://github.com/vla-safe/SAFE) | Gu et al. | NeurIPS 2025 | — | `Inference` · `Visual Perception + Action Interface`<br>Execution Error → Action Generation → Recovery Failure |
| **[Semantically Safe Robot Manipulation: From Semantic Scene Understanding to Motion Safeguards](https://arxiv.org/abs/2410.15185)** [Project / Code](https://utiasdsl.github.io/semantic-manipulation/) | Brunke et al. | ICRA 2025 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Semantic Misalignment → Task Planner → Collision |
| **[Towards Safe Robot Foundation Models Using Inductive Biases](https://arxiv.org/abs/2505.10219)** [Project / Code](https://sites.google.com/view/safe-robot-foundation-models) | Tölle et al. | arXiv 2025 | •&nbsp;Physical | `Inference` · `Action Interface + Execution Control`<br>Constraint Violation → Action Generation → Collision |
| **[Plug in the Safety Chip: Enforcing Constraints for LLM-Driven Robot Agents](https://arxiv.org/abs/2309.09919)** | Yang et al. | arXiv 2023 | •&nbsp;Physical | `Inference` · `Task Planning + Action Interface`<br>Planning Error → Task Planner → Unsafe Motion |
| **[REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://proceedings.mlr.press/v229/liu23g.html)** [![GitHub stars](https://img.shields.io/github/stars/real-stanford/reflect?style=social)](https://github.com/real-stanford/reflect) | Liu et al. | CoRL 2023 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Execution Error → Action Generation → Task Failure |
| **[Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments](https://arxiv.org/abs/2311.02817)** | Yue et al. | arXiv 2023 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Constraint Violation → Action Generation → Collision |

<a id="defenses-representation-steering-and-inference-time-defense"></a>

### Representation Steering and Inference-Time Defense

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration](https://arxiv.org/abs/2603.06001)** | Zhang et al. | arXiv 2026 | •&nbsp;Task | `Inference` · `User Instruction + Reasoning Representation`<br>Distribution Shift → VLA policy → Task Failure |
| **[TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors](https://arxiv.org/abs/2607.12571)** | Fu et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Training → Inference` · `Model Supply Chain + Visual Perception`<br>Backdoor → Action Generation → Targeted Action |
| **[Concept Enhancement Engineering: A Lightweight and Efficient Robust Defense Against Jailbreak Attacks in Embodied AI](https://arxiv.org/abs/2504.13201)** | Yang et al. | arXiv 2025 | •&nbsp;Ethics<br>•&nbsp;Security/Privacy | `Inference` · `User Instruction + Reasoning Representation`<br>Jailbreak → Task Planner → Policy Violation |

<a id="defenses-system-and-communication-defenses"></a>

### System and Communication Defenses

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[AgentSafe: Safeguarding Large Language Model-Based Multi-Agent Systems via Hierarchical Data Management](https://arxiv.org/abs/2503.04392)** | Mao et al. | arXiv 2025 | •&nbsp;Security/Privacy | `System → Inference` · `Context Memory Retrieval + Multi Agent Communication`<br>Memory Poisoning + Multi Agent Propagation → Shared System State → Control Hijacking |

<a id="defenses-active-perception-and-recovery"></a>

### Active Perception and Recovery

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation](https://arxiv.org/abs/2512.07472)** | Xu et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `Visual Perception + World State`<br>Distribution Shift → VLA policy → Task Failure |
| **[FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models](https://arxiv.org/abs/2510.01642)** | Lin et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Execution Error → Action Generation → Task Failure |
| **[Embodied Active Defense: Leveraging Recurrent Feedback to Counter Adversarial Patches](https://arxiv.org/abs/2404.00540)** | Wu et al. | ICLR 2024 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Visual Perception`<br>Adversarial Patch → VLA policy → Task Failure |

<a id="defenses-multimodal-perception-and-physical-safeguards"></a>

### Multimodal Perception and Physical Safeguards

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[DroneVLA: VLA based Aerial Manipulation](https://arxiv.org/abs/2601.13809)** | Mehboob et al. | arXiv 2026 | — | `Inference` · `Multiple surfaces`<br>Constraint Violation → Action Generation → Task Failure |
| **[Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation](https://arxiv.org/abs/2603.05754)** [Project / Code](https://thisanwerss.github.io/Safe-Night-VLA/) | Yu et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Visual Perception`<br>Distribution Shift → VLA policy → Task Failure |

<a id="defenses-human-in-the-loop-safety-refinement"></a>

### Human-in-the-Loop Safety Refinement

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Human-assisted Robotic Policy Refinement via Action Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/347110fb894281e5e937f6ccd998a6eb-Abstract-Conference.html)** [![GitHub stars](https://img.shields.io/github/stars/GeWu-Lab/Action-Preference-Optimization?style=social)](https://github.com/GeWu-Lab/Action-Preference-Optimization) | Xia et al. | NeurIPS 2025 | •&nbsp;Task | `Inference` · `Action Interface`<br>Unsafe Policy Behavior → VLA policy → Task Failure |
| **[Human-in-the-Loop Online Rejection Sampling for Robotic Manipulation](https://arxiv.org/abs/2510.26406)** [Project / Code](https://hiors-project.github.io/) | Lu et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `Action Interface`<br>Unsafe Policy Behavior → VLA policy → Task Failure |

<a id="defenses-runtime-observation-interventions"></a>

### Runtime Observation Interventions

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Run-Time Observation Interventions Make Vision-Language-Action Models More Visually Robust](https://arxiv.org/abs/2410.01971)** [![GitHub stars](https://img.shields.io/github/stars/irom-princeton/byovla?style=social)](https://github.com/irom-princeton/byovla) | Hancock et al. | arXiv 2024 | •&nbsp;Task | `Inference` · `Visual Perception`<br>Distribution Shift → VLA policy → Task Failure |

<a id="defenses-reliability-oriented-policy-refinement"></a>

### Reliability-Oriented Policy Refinement

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[EvoVLA: Self-Evolving Vision-Language-Action Model](https://arxiv.org/abs/2511.16166)** [![GitHub stars](https://img.shields.io/github/stars/AIGeeksGroup/EvoVLA?style=social)](https://github.com/AIGeeksGroup/EvoVLA) | Liu et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `Task Planning + Action Interface`<br>Unsafe Policy Behavior → VLA policy → Task Failure |

<a id="defenses-model-unlearning-and-data-governance"></a>

### Model Unlearning and Data Governance

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models](https://arxiv.org/abs/2604.03956)** | Ranjan et al. | arXiv 2026 | •&nbsp;Task | `Training → Inference` · `Model Supply Chain`<br>Memorized Data Retention + Unsafe Policy Behavior → VLA policy → Privacy Leakage |

<a id="defenses-safety-aware-policy-learning"></a>

### Safety-Aware Policy Learning

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[VLM-SAFE: Vision-Language Model-Guided Safety-Aware Reinforcement Learning with World Models for Autonomous Driving](https://arxiv.org/abs/2505.16377)** [Project / Code](https://ys-qu.github.io/vlsafe-website/) | Qu et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Distribution Shift → Task Planner → Task Failure |

<a id="defenses-privacy-preserving-perception"></a>

### Privacy-Preserving Perception

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Privacy-Preserving Semantic Segmentation from Ultra-Low-Resolution RGB Inputs](https://arxiv.org/abs/2507.16034)** [![GitHub stars](https://img.shields.io/github/stars/hxy-0818/ULR2SS?style=social)](https://github.com/hxy-0818/ULR2SS) | Huang et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Visual Perception`<br>Sensitive Data Exposure → Private Data → Privacy Leakage |
| **[Real-Time Privacy Preservation for Robot Visual Perception](https://arxiv.org/abs/2505.05519)** | Choi et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Visual Perception`<br>Sensitive Data Exposure → Private Data → Privacy Leakage |

<a id="defenses-failure-detection-and-recovery"></a>

### Failure Detection and Recovery

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272)** [Project / Code](https://research.nvidia.com/labs/gear/ASPIRE/) | Lu et al. | arXiv 2026 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Execution Error → Action Generation → Task Failure |
| **[FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement](https://arxiv.org/abs/2607.01111)** | Hao et al. | arXiv 2026 | •&nbsp;Task | `Inference` · `Action Interface + Execution Control`<br>Execution Error → Action Generation → Task Failure |
| **[FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645)** | Zhao et al. | CVPR 2026 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Execution Error → Action Generation → Task Failure |
| **[Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448)** [![GitHub stars](https://img.shields.io/github/stars/RLinf/RPent?style=social)](https://github.com/RLinf/RPent) | Zhang et al. | arXiv 2026 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Execution Error → Action Generation → Task Failure |
| **[Replanning Human-Robot Collaborative Tasks with Vision-Language Models via Semantic and Physical Dual-Correction](https://arxiv.org/abs/2602.14551)** | Kato et al. | arXiv 2026 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Execution Error → Action Generation → Task Failure |
| **[I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models](https://arxiv.org/abs/2509.16072)** [Project / Code](https://clemgris.github.io/I-FailSense/) | Grislain et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `Visual Perception + Proprioception`<br>Execution Error → Action Generation → Task Failure |
| **[Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction](https://arxiv.org/abs/2504.14588)** [![GitHub stars](https://img.shields.io/github/stars/GeWu-Lab/Motion-based-Self-Reflection-Framework?style=social)](https://github.com/GeWu-Lab/Motion-based-Self-Reflection-Framework) | Xia et al. | CVPR 2025 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Execution Error → Action Generation → Task Failure |
| **[A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation](https://arxiv.org/abs/2405.17418)** | Li et al. | arXiv 2024 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Execution Error → Action Generation → Task Failure |
| **[DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment](https://arxiv.org/abs/2307.00329)** [Project / Code](https://sites.google.com/view/doremi-paper) | Guo et al. | IROS 2024 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Execution Error → Action Generation → Task Failure |

<a id="defenses-uncertainty-abstention-and-human-oversight"></a>

### Uncertainty, Abstention, and Human Oversight

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue](https://arxiv.org/abs/2509.15061)** | Lin et al. | IROS 2026 | •&nbsp;Task | `Inference` · `User Instruction`<br>Instruction Ambiguity → Reasoning Process → Task Failure |
| **[Do What? Teaching Vision-Language-Action Models to Reject the Impossible](https://arxiv.org/abs/2508.16292)** | Hsieh et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `User Instruction`<br>Planning Error → Task Planner → Task Failure |
| **[Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](https://arxiv.org/abs/2307.01928)** [Project / Code](https://robot-help.github.io/) | Ren et al. | CoRL 2023 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Instruction Ambiguity → Reasoning Process → Task Failure |

<a id="benchmarks"></a>

## 📊 Benchmarks and Evaluation

<a id="benchmarks-ood-and-generalization-benchmarks"></a>

### OOD and Generalization Benchmarks

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models](https://arxiv.org/abs/2603.28301)** [![GitHub stars](https://img.shields.io/github/stars/cau-hai-lab/LIBERO-Para?style=social)](https://github.com/cau-hai-lab/LIBERO-Para) | Kim et al. | EMNLP 2026 | •&nbsp;Task | `Inference` · `Visual Perception`<br>Distribution Shift → VLA policy → Task Failure |
| **[LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html)** [![GitHub stars](https://img.shields.io/github/stars/sylvestf/LIBERO-plus?style=social)](https://github.com/sylvestf/LIBERO-plus) | Fei et al. | CVPR 2026 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Distribution Shift → VLA policy → Task Failure |
| **[LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](https://arxiv.org/abs/2510.03827)** [![GitHub stars](https://img.shields.io/github/stars/Zxy-MLlab/LIBERO-PRO?style=social)](https://github.com/Zxy-MLlab/LIBERO-PRO) | Zhou et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `Visual Perception + World State`<br>Distribution Shift → VLA policy → Task Failure |

<a id="benchmarks-comprehensive-vla-evaluation"></a>

### Comprehensive VLA Evaluation

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](https://arxiv.org/abs/2512.22539)** [![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/VLA-Arena?style=social)](https://github.com/PKU-Alignment/VLA-Arena) | Zhang et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Evaluation coverage |
| **[VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://arxiv.org/abs/2412.18194)** [![GitHub stars](https://img.shields.io/github/stars/OpenMOSS/VLABench?style=social)](https://github.com/OpenMOSS/VLABench) | Zhang et al. | arXiv 2024 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Evaluation coverage |

<a id="benchmarks-adversarial-and-physical-robustness"></a>

### Adversarial and Physical Robustness

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[RedVLA: Physical Red Teaming for Vision-Language-Action Models](https://arxiv.org/abs/2604.22591)** [Project / Code](https://redvla.github.io/) | Zhang et al. | arXiv 2026 | •&nbsp;Physical<br>•&nbsp;Security/Privacy | `Inference` · `Physical Semantic Environment + Visual Perception`<br>Adversarial Object + Environment Manipulation → VLA policy → Control Hijacking |
| **[VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness](https://openreview.net/forum?id=31EjDFwFEe)** | Ru et al. | OpenReview 2026 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Multiple surfaces`<br>Evaluation coverage |
| **[AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.12149)** | Li et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Training → Inference` · `Multiple surfaces`<br>Evaluation coverage |
| **[Manipulation Facing Threats: Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models](https://arxiv.org/abs/2409.13174)** [Project / Code](https://chaducheng.github.io/Manipulate-Facing-Threats/) | Cheng et al. | arXiv 2024 | •&nbsp;Task<br>•&nbsp;Security/Privacy | `Inference` · `Visual Perception + Physical Semantic Environment`<br>Evaluation coverage |

<a id="benchmarks-task-and-physical-safety"></a>

### Task and Physical Safety

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2606.27079)** | Lyu et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Evaluation coverage |
| **[IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks](https://arxiv.org/abs/2506.16402)** | Lu et al. | AAAI 2026 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Constraint Violation → Action Generation → Task Failure |
| **[LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686)** [![GitHub stars](https://img.shields.io/github/stars/LIBERO-SAFETY/LIBERO-Safety?style=social)](https://github.com/LIBERO-SAFETY/LIBERO-Safety) | Cui et al. | ECCV 2026 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Evaluation coverage |
| **[SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.00773)** [Project / Code](https://safevla.org/) | Fan et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Evaluation coverage |
| **[A Framework for Benchmarking and Aligning Task-Planning Safety in LLM-Based Embodied Agents](https://arxiv.org/abs/2504.14650)** | Huang et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `User Instruction + Task Planning`<br>Evaluation coverage |
| **[CostNav: A Navigation Benchmark for Real-World Economic-Cost Evaluation of Physical AI Agents](https://arxiv.org/abs/2511.20216)** [![GitHub stars](https://img.shields.io/github/stars/worv-ai/CostNav?style=social)](https://github.com/worv-ai/CostNav) | Seong et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Evaluation coverage |
| **[SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)** [![GitHub stars](https://img.shields.io/github/stars/shengyin1224/SafeAgentBench?style=social)](https://github.com/shengyin1224/SafeAgentBench) | Yin et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Ethics | `Inference` · `User Instruction`<br>Hazardous Instruction → Task Planner → Policy Violation |
| **[EARBench: Towards Evaluating Physical Risk Awareness for Task Planning of Foundation Model-Based Embodied AI Agents](https://arxiv.org/abs/2408.04449)** | Zhu et al. | arXiv 2024 | •&nbsp;Physical | `Inference` · `Multiple surfaces`<br>Constraint Violation → Action Generation → Unsafe Motion |

<a id="benchmarks-semantic-and-ethical-safety"></a>

### Semantic and Ethical Safety

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Generating Robot Constitutions and Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663)** [![GitHub stars](https://img.shields.io/github/stars/asimov-benchmark/asimov-benchmark.github.io?style=social)](https://github.com/asimov-benchmark/asimov-benchmark.github.io) | Sermanet et al. | arXiv 2025 | •&nbsp;Ethics | `Inference` · `User Instruction + World State`<br>Semantic Misalignment → Task Planner → Policy Violation |

<a id="benchmarks-evaluation-infrastructure"></a>

### Evaluation Infrastructure

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941)** [![GitHub stars](https://img.shields.io/github/stars/simpler-env/SimplerEnv?style=social)](https://github.com/simpler-env/SimplerEnv) | Li et al. | CoRL 2024 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Distribution Shift → VLA policy → Task Failure |
| **[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)** [![GitHub stars](https://img.shields.io/github/stars/Lifelong-Robot-Learning/LIBERO?style=social)](https://github.com/Lifelong-Robot-Learning/LIBERO) | Liu et al. | NeurIPS Datasets and Benchmarks 2023 | •&nbsp;Task | `Inference` · `Multiple surfaces`<br>Distribution Shift → VLA policy → Task Failure |

<a id="benchmarks-safety-and-hazard-benchmarks"></a>

### Safety and Hazard Benchmarks

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2604.12447)** | Chen et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | `Inference` · `User Instruction + World State`<br>Semantic Misalignment → Task Planner → Policy Violation |
| **[AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697)** | Ying et al. | arXiv 2025 | •&nbsp;Ethics | `Inference` · `User Instruction`<br>Hazardous Instruction → Task Planner → Policy Violation |
| **[SafeMind: Benchmarking and Mitigating Safety Risks in Embodied LLM Agents](https://arxiv.org/abs/2509.25885)** | Chen et al. | arXiv 2025 | •&nbsp;Ethics<br>•&nbsp;Security/Privacy | `Inference` · `User Instruction`<br>Jailbreak → Task Planner → Policy Violation |

<a id="benchmarks-robustness-and-uncertainty-evaluation"></a>

### Robustness and Uncertainty Evaluation

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Confidence Calibration in Vision-Language-Action Models](https://arxiv.org/abs/2507.17383)** | Zollo et al. | arXiv 2025 | •&nbsp;Task | `Inference` · `Reasoning Representation + Action Interface`<br>Uncertainty Miscalibration → VLA policy → Task Failure |
| **[Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots](https://arxiv.org/abs/2507.17049)** | Valle et al. | arXiv 2025 | — | `Inference` · `Multiple surfaces`<br>Uncertainty Miscalibration → VLA policy → Recovery Failure |
| **[VLATest: Testing and Evaluating Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2409.12894)** | Wang et al. | arXiv 2024 | •&nbsp;Task | `Inference` · `Visual Perception + User Instruction`<br>Evaluation coverage |

<a id="benchmarks-safety-critical-perception-evaluation"></a>

### Safety-Critical Perception Evaluation

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Can Vision-Language Models Understand Construction Workers? An Exploratory Study](https://arxiv.org/abs/2601.10835)** | Bui et al. | arXiv 2026 | — | `Inference` · `Visual Perception`<br>Evaluation coverage |
| **[Privacy Risks of Robot Vision: A User Study on Image Modalities and Resolution](https://arxiv.org/abs/2505.07766)** | Huang et al. | arXiv 2025 | •&nbsp;Security/Privacy | `Inference` · `Visual Perception`<br>Evaluation coverage |

<a id="system-security"></a>

## 🔐 System-Level Security, Privacy, and Misuse

<a id="system-security-cross-layer-system-security"></a>

### Cross-Layer System Security

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Beyond Model Jailbreak: Systematic Dissection of the Ten Deadly Sins in Embodied Intelligence](https://arxiv.org/abs/2512.06387)** | Huang et al. | arXiv 2025 | •&nbsp;Security/Privacy | `System → Inference` · `Multiple surfaces`<br>Multiple mechanisms → Shared System State → Policy Violation |

<a id="system-security-privacy-misuse-and-covert-channels"></a>

### Privacy, Misuse, and Covert Channels

| Paper | Authors | Venue | Evaluated Risk | Threat Model |
|---|---|---:|---|---|
| **[Cyber-Physical Steganography in Robotic Motion Control](https://arxiv.org/abs/2501.04541)** | Chang et al. | IEICE Transactions 2026 | •&nbsp;Security/Privacy | `System → Inference` · `Action Interface + Execution Control`<br>Covert Channel + Trajectory Manipulation → Robot Executor → Privacy Leakage |

## Scope and Curation Policy

The core scope is VLA safety, robustness, security, and evaluation. Closely related LLM-robot, VLM-driven embodied-agent, autonomous-driving, and robot-policy papers are included when they expose a risk, mechanism, defense, or evaluation principle that transfers directly to VLA systems.

A paper is listed once under its primary contribution. Risk outcomes and mechanisms are represented as multi-label metadata rather than by duplicating the paper across sections.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and add or update the corresponding record in `data/papers.json`. Do not edit generated paper tables directly.

## License

MIT License. Paper titles, author names, venues, and links remain the property of their respective authors and publishers.
