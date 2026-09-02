# Awesome Responsible VLA

A curated, taxonomy-driven list of research on the safety, robustness, security, and responsible deployment of Vision-Language-Action models and closely related embodied agents.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> This list separates **risk outcomes** (what goes wrong) from **failure sources and mechanisms** (why it goes wrong). GitHub star badges are live and are shown only for identified official repositories.

## Taxonomy at a Glance

### Risk outcomes

- **Task & Reliability:** task failure, degraded success, dangerous inaction, or recovery failure.
- **Physical Safety:** collision, injury, damage, unsafe motion, or constraint violation.
- **Ethical & Societal:** harmful instruction execution, misuse, deception, or oversight failure.
- **Security & Privacy:** unauthorized control, backdoors, leakage, covert channels, or system compromise.

### Failure sources

- **Adversarial:** malicious manipulation of inputs, training, states, actions, or system components.
- **Non-adversarial / OOD:** failures under unseen viewpoints, objects, language, tasks, environments, embodiments, or dynamics.
- **Design / system:** misalignment, misspecified objectives, sensor faults, planner-executor mismatch, or failed recovery.

See [the full taxonomy](docs/taxonomy.md) for definitions and inclusion rules.

## 🧭 Contents

- [📚 Surveys and Perspectives](#surveys)
- [🌍 Robustness and OOD Generalization](#ood-generalization)
- [🧪 Training-Time Attacks](#training-attacks)
- [⚡ Inference-Time Attacks](#inference-attacks)
- [🛡️ Defenses and Safety Mechanisms](#defenses)
- [📊 Benchmarks and Evaluation](#benchmarks)
- [🔐 System-Level Security, Privacy, and Misuse](#system-security)

**65 papers in the current catalog.**

<a id="surveys"></a>

## 📚 Surveys and Perspectives

### VLA Safety Surveys

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms](https://arxiv.org/abs/2604.23775)** [![GitHub stars](https://img.shields.io/github/stars/LiQiiiii/Awesome-VLA-Safety?style=social)](https://github.com/LiQiiiii/Awesome-VLA-Safety) | Li et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Survey scope (attacks, defenses, OOD, safety evaluation) |

### Embodied AI Safety and Security

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Navigating Embodied Intelligence: Enabling Technologies, Security and Privacy, and Emerging Trends](https://doi.org/10.1109/JIOT.2025.3649049)** | Wang et al. | IEEE IoT Journal 2026 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Survey scope (system security, privacy) |
| **[What Breaks Embodied AI Security: LLM Vulnerabilities, CPS Flaws, or Something Else?](https://arxiv.org/abs/2602.17345)** | Ma et al. | arXiv 2026 | •&nbsp;Physical<br>•&nbsp;Security/Privacy | Survey scope (LLM jailbreak, CPS flaw, closed-loop mismatch) |
| **[Towards Robust and Secure Embodied AI: A Survey on Vulnerabilities and Attacks](https://arxiv.org/abs/2502.13175)** | Xing et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | Survey scope (perception, planning, control attacks) |
| **[Towards Safe and Trustworthy Embodied AI: Foundations, Status, and Prospects](https://openreview.net/forum?id=Eu6Yt21Alv)** [![GitHub stars](https://img.shields.io/github/stars/AI45Lab/Awesome-Trustworthy-Embodied-AI?style=social)](https://github.com/AI45Lab/Awesome-Trustworthy-Embodied-AI) | Tan et al. | OpenReview 2025 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Survey scope (design failure, misalignment, recovery) |

### Domain-Specific Surveys

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[A Survey on Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2506.24044)** [![GitHub stars](https://img.shields.io/github/stars/JohnsonJiang1996/Awesome-VLA4AD?style=social)](https://github.com/JohnsonJiang1996/Awesome-VLA4AD) | Jiang et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Survey scope (OOD, safety, formal verification) |

<a id="ood-generalization"></a>

## 🌍 Robustness and OOD Generalization

### Representation and Language-Action Generalization

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](https://arxiv.org/abs/2607.13429)** [![GitHub stars](https://img.shields.io/github/stars/dwipddalal/Anchor-Align?style=social)](https://github.com/dwipddalal/Anchor-Align) | Dalal et al. | arXiv 2026 | •&nbsp;Task | Non-adversarial OOD (representation, language, viewpoint) |

### Action and Spatial Generalization

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior](https://arxiv.org/abs/2604.01570)** [![GitHub stars](https://img.shields.io/github/stars/Haochen-Niu/FAN-VLA?style=social)](https://github.com/Haochen-Niu/FAN-VLA) | Niu et al. | CVPR 2026 | •&nbsp;Task<br>•&nbsp;Physical | Non-adversarial OOD (action neighborhood, spatial shift) |

### Benchmarks for Distribution Shift

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](https://arxiv.org/abs/2510.03827)** [![GitHub stars](https://img.shields.io/github/stars/Zxy-MLlab/LIBERO-PRO?style=social)](https://github.com/Zxy-MLlab/LIBERO-PRO) | Zhou et al. | arXiv 2025 | •&nbsp;Task | Non-adversarial OOD (spatial shift, memorization) |

### Geometry and Object-Centric Stress Testing

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Geometric Red-Teaming for Robotic Manipulation](https://arxiv.org/abs/2509.12379)** | Goel et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Non-adversarial OOD (object geometry) |

### Language and Instruction Generalization

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[ICR-Drive: Instruction Counterfactual Robustness for End-to-End Language-Driven Autonomous Driving](https://arxiv.org/abs/2604.05378)** [![GitHub stars](https://img.shields.io/github/stars/icrdrive/icrdrive?style=social)](https://github.com/icrdrive/icrdrive) | Hamid et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | Non-adversarial OOD (language, counterfactual scenario) |

### Open-World Evaluation

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[How VLAs (Really) Work in Open-World Environments](https://arxiv.org/abs/2604.21192)** | Rasouli et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | Non-adversarial OOD (open-world environment) |
| **[pi0.5: A Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)** [![GitHub stars](https://img.shields.io/github/stars/Physical-Intelligence/openpi?style=social)](https://github.com/Physical-Intelligence/openpi) | Black et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Non-adversarial OOD (open world, environment, long horizon) |

<a id="training-attacks"></a>

## 🧪 Training-Time Attacks

### Backdoors and Data Poisoning

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2601.14323)** | Xu et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | Training-time attack (temporal action-chunk backdoor) |
| **[State Backdoor: Towards Stealthy Real-World Poisoning Attack on Vision-Language-Action Models in State Space](https://arxiv.org/abs/2601.04266)** | Guo et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | Training-time attack (state backdoor) |
| **[BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://arxiv.org/abs/2505.16640)** [![GitHub stars](https://img.shields.io/github/stars/Zxy-MLlab/BadVLA?style=social)](https://github.com/Zxy-MLlab/BadVLA) | Zhou et al. | NeurIPS 2025 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | Training-time attack (backdoor) |
| **[Can We Trust Embodied Agents? Exploring Backdoor Attacks Against Embodied LLM-Based Decision-Making Systems](https://arxiv.org/abs/2405.20774)** [![GitHub stars](https://img.shields.io/github/stars/ASGuard-UCI/BALD?style=social)](https://github.com/ASGuard-UCI/BALD) | Jiao et al. | ICLR 2025 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | Training-time attack (decision-making backdoor) |
| **[DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models](https://arxiv.org/abs/2510.10932)** [![GitHub stars](https://img.shields.io/github/stars/megaknight114/DropVLA?style=social)](https://github.com/megaknight114/DropVLA) | Xu et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | Training-time attack (action-output backdoor) |
| **[Goal-Oriented Backdoor Attack Against Vision-Language-Action Models via Physical Objects](https://arxiv.org/abs/2510.09269)** [Project / Code](https://goba-attack.github.io/) | Zhou et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | Training-time attack (physical-object backdoor) |

<a id="inference-attacks"></a>

## ⚡ Inference-Time Attacks

### Visual Perturbations and Patches

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.21192)** [![GitHub stars](https://img.shields.io/github/stars/yuyi-sd/UPA-RFAS?style=social)](https://github.com/yuyi-sd/UPA-RFAS) | Lu et al. | CVPR 2026 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | Inference-time attack (adversarial patch) |
| **[ADVEDM: Fine-Grained Adversarial Attack Against VLM-Based Embodied Agents](https://arxiv.org/abs/2509.16645)** | Wang et al. | NeurIPS 2025 | •&nbsp;Task<br>•&nbsp;Physical | Inference-time attack (semantic visual perturbation) |
| **[Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2411.13587)** [![GitHub stars](https://img.shields.io/github/stars/William-wAng618/roboticAttack?style=social)](https://github.com/William-wAng618/roboticAttack) | Wang et al. | ICCV 2025 | •&nbsp;Task<br>•&nbsp;Physical | Inference-time attack (adversarial patch) |
| **[Model-Agnostic Adversarial Attack and Defense for Vision-Language-Action Models](https://arxiv.org/abs/2510.13237)** [![GitHub stars](https://img.shields.io/github/stars/trustmlyoungscientist/EDPA_attack_defense?style=social)](https://github.com/trustmlyoungscientist/EDPA_attack_defense) | Xu et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Inference-time attack (adversarial patch) |
| **[When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.16203)** | Yan et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Inference-time attack (multimodal perturbation) |

### Planning, Action, and Trajectory Manipulation

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[FreezeVLA: Action-Freezing Attacks Against Vision-Language-Action Models](https://arxiv.org/abs/2509.19870)** [![GitHub stars](https://img.shields.io/github/stars/xinwong/FreezeVLA?style=social)](https://github.com/xinwong/FreezeVLA) | Wang et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Inference-time attack (action freezing) |

### Sensor, State, and Physical Interventions

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Phantom Menace: Exploring and Enhancing the Robustness of VLA Models Against Physical Sensor Attacks](https://arxiv.org/abs/2511.10008)** | Lu et al. | AAAI 2026 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | Inference-time attack (physical sensor intervention) |

### Jailbreaks and Prompt Injection

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[CHAI: Command Hijacking Against Embodied AI](https://arxiv.org/abs/2510.00181)** [![GitHub stars](https://img.shields.io/github/stars/Cyphysecurity/chai?style=social)](https://github.com/Cyphysecurity/chai) | Burbano et al. | SaTML 2026 | •&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Inference-time attack (visual prompt injection) |
| **[If You're Waiting for a Sign... That Might Not Be It! Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems](https://arxiv.org/abs/2604.19844)** | Chang et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Inference-time attack (visual prompt injection) |
| **[Adversarial Attacks on Robotic Vision-Language-Action Models](https://arxiv.org/abs/2506.03350)** [![GitHub stars](https://img.shields.io/github/stars/eliotjones1/robogcg?style=social)](https://github.com/eliotjones1/robogcg) | Jones et al. | arXiv 2025 | •&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Inference-time attack (jailbreak, command hijacking) |
| **[BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://arxiv.org/abs/2407.20242)** [![GitHub stars](https://img.shields.io/github/stars/Rookie143/BadRobot?style=social)](https://github.com/Rookie143/BadRobot) | Zhang et al. | ICLR 2025 | •&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Inference-time attack (voice jailbreak) |
| **[Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691)** [![GitHub stars](https://img.shields.io/github/stars/arobey1/robopair?style=social)](https://github.com/arobey1/robopair) | Robey et al. | ICRA 2025 | •&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Inference-time attack (jailbreak) |
| **[POEX: Towards Policy Executable Jailbreak Attacks Against the LLM-Based Robots](https://arxiv.org/abs/2412.16633)** [Project / Code](https://poex-jailbreak.github.io/) | Lu et al. | arXiv 2025 | •&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Inference-time attack (executable jailbreak) |

### Upstream VLM Attacks

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Chain of Attack: On the Robustness of Vision-Language Models Against Transfer-Based Adversarial Attacks](https://arxiv.org/abs/2411.15720)** [![GitHub stars](https://img.shields.io/github/stars/Shelton1013/Chain_of_Attack?style=social)](https://github.com/Shelton1013/Chain_of_Attack) | Xie et al. | CVPR 2025 | •&nbsp;Task<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Inference-time attack (black-box transfer) |

<a id="defenses"></a>

## 🛡️ Defenses and Safety Mechanisms

### Robust Training and Safety Alignment

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[SafeVLA: Towards Safety Alignment of Vision-Language-Action Models via Constrained Learning](https://arxiv.org/abs/2503.03480)** [![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/SafeVLA?style=social)](https://github.com/PKU-Alignment/SafeVLA) | Zhang et al. | NeurIPS 2025 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Ethical | Hazardous instruction (unsafe policy generation) |

### Runtime Monitoring and Guardrails

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[RC-NF: Robot-Conditioned Normalizing Flow for Real-Time Anomaly Detection in Robotic Manipulation](https://arxiv.org/abs/2603.11106)** | Zhou et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | Execution failure (state-conditioned anomaly) |
| **[Safety Guardrails for LLM-Enabled Robots](https://arxiv.org/abs/2503.07885)** | Ravichandran et al. | IEEE RA-L 2026 | •&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Hazardous instruction (jailbreak, unsafe plan) |
| **[From Words to Safety: Language-Conditioned Safety Filtering for Robot Navigation](https://arxiv.org/abs/2511.05889)** | Feng et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Physical safety violation (unsafe command, context constraint) |
| **[ROVER: Regulator-Driven Robust Temporal Verification of Black-Box Robot Policies](https://arxiv.org/abs/2511.17781)** | Sakano et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Policy failure (temporal safety-property violation) |
| **[VLSA: Vision-Language-Action Models with a Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)** [![GitHub stars](https://img.shields.io/github/stars/THU-RCSCT/vlsa-aegis?style=social)](https://github.com/THU-RCSCT/vlsa-aegis) | Hu et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Physical safety violation (unsafe VLA action) |

### Action Shielding, Fail-Safes, and Recovery

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[SAFE: Multitask Failure Detection for Vision-Language-Action Models](https://arxiv.org/abs/2506.09937)** [![GitHub stars](https://img.shields.io/github/stars/vla-safe/SAFE?style=social)](https://github.com/vla-safe/SAFE) | Gu et al. | NeurIPS 2025 | •&nbsp;Task<br>•&nbsp;Physical | Execution failure (OOD anomaly) |
| **[Plug in the Safety Chip: Enforcing Constraints for LLM-Driven Robot Agents](https://arxiv.org/abs/2309.09919)** | Yang et al. | arXiv 2023 | •&nbsp;Task<br>•&nbsp;Physical | Planning failure (formal-constraint violation) |

### Representation Steering and Inference-Time Defense

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration](https://arxiv.org/abs/2603.06001)** | Zhang et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | Non-adversarial OOD (linguistic grounding, instruction neglect) |
| **[Concept Enhancement Engineering: A Lightweight and Efficient Robust Defense Against Jailbreak Attacks in Embodied AI](https://arxiv.org/abs/2504.13201)** | Yang et al. | arXiv 2025 | •&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Inference-time attack (planner jailbreak) |

### System and Communication Defenses

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[AgentSafe: Safeguarding Large Language Model-Based Multi-Agent Systems via Hierarchical Data Management](https://arxiv.org/abs/2503.04392)** | Mao et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | System-level attack (memory poisoning, impersonation, unauthorized access) |

### Active Perception and Recovery

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation](https://arxiv.org/abs/2512.07472)** | Xu et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Non-adversarial OOD (spatial, object, color, background) |
| **[FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models](https://arxiv.org/abs/2510.01642)** | Lin et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Execution failure (closed-loop policy failure) |
| **[Embodied Active Defense: Leveraging Recurrent Feedback to Counter Adversarial Patches](https://arxiv.org/abs/2404.00540)** | Wu et al. | ICLR 2024 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Security/Privacy | Inference-time attack (adaptive adversarial patch) |

### Multimodal Perception and Physical Safeguards

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation](https://arxiv.org/abs/2603.05754)** [Project / Code](https://thisanwerss.github.io/Safe-Night-VLA/) | Yu et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical | Non-adversarial OOD (low light, occlusion, geometry) |

### Human-in-the-Loop Safety Refinement

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Human-in-the-Loop Online Rejection Sampling for Robotic Manipulation](https://arxiv.org/abs/2510.26406)** [Project / Code](https://hiors-project.github.io/) | Lu et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Policy failure (unsafe or low-quality rollout) |

### Runtime Observation Interventions

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Run-Time Observation Interventions Make Vision-Language-Action Models More Visually Robust](https://arxiv.org/abs/2410.01971)** [![GitHub stars](https://img.shields.io/github/stars/irom-princeton/byovla?style=social)](https://github.com/irom-princeton/byovla) | Hancock et al. | arXiv 2024 | •&nbsp;Task<br>•&nbsp;Physical | Non-adversarial OOD (object, background distractor) |

<a id="benchmarks"></a>

## 📊 Benchmarks and Evaluation

### Comprehensive VLA Evaluation

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](https://arxiv.org/abs/2512.22539)** [![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/VLA-Arena?style=social)](https://github.com/PKU-Alignment/VLA-Arena) | Zhang et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Evaluation scope (capability, robustness, closed-loop safety) |

### Adversarial and Physical Robustness

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness](https://openreview.net/forum?id=31EjDFwFEe)** | Ru et al. | OpenReview 2026 | •&nbsp;Task<br>•&nbsp;Physical | Evaluation scope (visual, physical perturbation) |

### Task and Physical Safety

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks](https://arxiv.org/abs/2506.16402)** | Lu et al. | AAAI 2026 | •&nbsp;Task<br>•&nbsp;Physical | Physical safety violation (mitigation, recovery failure) |
| **[SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)** [![GitHub stars](https://img.shields.io/github/stars/shengyin1224/SafeAgentBench?style=social)](https://github.com/shengyin1224/SafeAgentBench) | Yin et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Ethical | Hazardous instruction (unsafe task planning) |
| **[EARBench: Towards Evaluating Physical Risk Awareness for Task Planning of Foundation Model-Based Embodied AI Agents](https://arxiv.org/abs/2408.04449)** | Zhu et al. | arXiv 2024 | •&nbsp;Task<br>•&nbsp;Physical | Physical safety violation (insufficient hazard awareness) |

### Semantic and Ethical Safety

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Generating Robot Constitutions and Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663)** [![GitHub stars](https://img.shields.io/github/stars/asimov-benchmark/asimov-benchmark.github.io?style=social)](https://github.com/asimov-benchmark/asimov-benchmark.github.io) | Sermanet et al. | arXiv 2025 | •&nbsp;Physical<br>•&nbsp;Ethical | Semantic safety violation (constitution, harmful action) |

### Evaluation Infrastructure

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941)** [![GitHub stars](https://img.shields.io/github/stars/simpler-env/SimplerEnv?style=social)](https://github.com/simpler-env/SimplerEnv) | Li et al. | CoRL 2024 | •&nbsp;Task<br>•&nbsp;Physical | Non-adversarial OOD (sim-to-real) |
| **[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)** [![GitHub stars](https://img.shields.io/github/stars/Lifelong-Robot-Learning/LIBERO?style=social)](https://github.com/Lifelong-Robot-Learning/LIBERO) | Liu et al. | NeurIPS Datasets and Benchmarks 2023 | •&nbsp;Task | Non-adversarial OOD (task composition, knowledge transfer) |

### Safety and Hazard Benchmarks

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2604.12447)** | Chen et al. | arXiv 2026 | •&nbsp;Task<br>•&nbsp;Physical<br>•&nbsp;Ethical | Semantic safety violation (instruction, context, harmful action) |
| **[AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697)** | Ying et al. | arXiv 2025 | •&nbsp;Physical<br>•&nbsp;Ethical | Hazardous instruction (harmful embodied action) |
| **[SafeMind: Benchmarking and Mitigating Safety Risks in Embodied LLM Agents](https://arxiv.org/abs/2509.25885)** | Chen et al. | arXiv 2025 | •&nbsp;Physical<br>•&nbsp;Ethical<br>•&nbsp;Security/Privacy | Hazardous instruction (adversarial prompt, unsafe planning) |

### Robustness and Uncertainty Evaluation

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Confidence Calibration in Vision-Language-Action Models](https://arxiv.org/abs/2507.17383)** | Zollo et al. | arXiv 2025 | •&nbsp;Task<br>•&nbsp;Physical | Uncertainty failure (overconfidence, distribution shift) |
| **[VLATest: Testing and Evaluating Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2409.12894)** | Wang et al. | arXiv 2024 | •&nbsp;Task<br>•&nbsp;Physical | Evaluation scope (natural, adversarial input mutation) |

<a id="system-security"></a>

## 🔐 System-Level Security, Privacy, and Misuse

### Cross-Layer System Security

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Beyond Model Jailbreak: Systematic Dissection of the Ten Deadly Sins in Embodied Intelligence](https://arxiv.org/abs/2512.06387)** | Huang et al. | arXiv 2025 | •&nbsp;Physical<br>•&nbsp;Security/Privacy | System-level attack (wireless, cloud, application, firmware) |

### Privacy, Misuse, and Covert Channels

| Paper | Authors | Venue | Risk | Threat Model |
|---|---|---:|---|---|
| **[Cyber-Physical Steganography in Robotic Motion Control](https://arxiv.org/abs/2501.04541)** | Chang et al. | IEICE Transactions 2026 | •&nbsp;Ethical<br>•&nbsp;Security/Privacy | System-level misuse (trajectory covert channel) |

## Scope and Curation Policy

The core scope is VLA safety, robustness, security, and evaluation. Closely related LLM-robot, VLM-driven embodied-agent, autonomous-driving, and robot-policy papers are included when they expose a risk, mechanism, defense, or evaluation principle that transfers directly to VLA systems.

A paper is listed once under its primary contribution. Risk outcomes and mechanisms are represented as multi-label metadata rather than by duplicating the paper across sections.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and add or update the corresponding record in `data/papers.json`. Do not edit generated paper tables directly.

## Acknowledgements

The organization is informed by the lifecycle and attack/defense views used in [Awesome-VLA-Safety](https://github.com/LiQiiiii/Awesome-VLA-Safety) and [Awesome-LVLM-Safety](https://github.com/XuankunRong/Awesome-LVLM-Safety), extended with explicit risk-outcome and OOD-generalization axes.

## License

MIT License. Paper titles, author names, venues, and links remain the property of their respective authors and publishers.
