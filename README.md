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

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms** | Li et al. | arXiv 2026 | Task, Physical, Ethical, Security/Privacy | Survey coverage — training/inference attacks, defenses, OOD, and safety benchmarks | Survey, Taxonomy | [Paper](https://arxiv.org/abs/2604.23775) · [![GitHub stars](https://img.shields.io/github/stars/LiQiiiii/Awesome-VLA-Safety?style=social)](https://github.com/LiQiiiii/Awesome-VLA-Safety) |

### Embodied AI Safety and Security

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Navigating Embodied Intelligence: Enabling Technologies, Security and Privacy, and Emerging Trends** | Wang et al. | IEEE IoT Journal 2026 | Task, Physical, Ethical, Security/Privacy | Survey coverage — security and privacy threats across the embodied system stack | Survey, Security, Privacy | [Paper](https://doi.org/10.1109/JIOT.2025.3649049) |
| **What Breaks Embodied AI Security: LLM Vulnerabilities, CPS Flaws, or Something Else?** | Ma et al. | arXiv 2026 | Physical, Security/Privacy | Survey coverage — LLM jailbreaks, CPS flaws, and closed-loop system mismatch | Perspective, Closed Loop Safety | [Paper](https://arxiv.org/abs/2602.17345) |
| **Towards Robust and Secure Embodied AI: A Survey on Vulnerabilities and Attacks** | Xing et al. | arXiv 2025 | Task, Physical, Security/Privacy | Survey coverage — adversarial threats across perception, planning, and control | Survey, Vulnerability Taxonomy | [Paper](https://arxiv.org/abs/2502.13175) |
| **Towards Safe and Trustworthy Embodied AI: Foundations, Status, and Prospects** | Tan et al. | OpenReview 2025 | Task, Physical, Ethical, Security/Privacy | Survey coverage — design failures, misalignment, intervention, and recovery | Survey, Trustworthiness, Maturity Model | [Paper](https://openreview.net/forum?id=Eu6Yt21Alv) · [![GitHub stars](https://img.shields.io/github/stars/AI45Lab/Awesome-Trustworthy-Embodied-AI?style=social)](https://github.com/AI45Lab/Awesome-Trustworthy-Embodied-AI) |

### Domain-Specific Surveys

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **A Survey on Vision-Language-Action Models for Autonomous Driving** | Jiang et al. | arXiv 2025 | Task, Physical | Survey coverage — OOD, robustness, safety, and formal verification in autonomous driving | Survey, Autonomous Driving, Closed Loop Control | [Paper](https://arxiv.org/abs/2506.24044) · [![GitHub stars](https://img.shields.io/github/stars/JohnsonJiang1996/Awesome-VLA4AD?style=social)](https://github.com/JohnsonJiang1996/Awesome-VLA4AD) |

<a id="ood-generalization"></a>

## 🌍 Robustness and OOD Generalization

### Representation and Language-Action Generalization

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment** | Dalal et al. | arXiv 2026 | Task | Non-adversarial OOD — representation shift, language instruction, viewpoint camera | Representation Shift, Language Instruction, Viewpoint Camera | [Paper](https://arxiv.org/abs/2607.13429) · [![GitHub stars](https://img.shields.io/github/stars/dwipddalal/Anchor-Align?style=social)](https://github.com/dwipddalal/Anchor-Align) |

### Action and Spatial Generalization

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior** | Niu et al. | CVPR 2026 | Task, Physical | Non-adversarial OOD — action neighborhood, spatial shift | Action Neighborhood, Spatial Shift | [Paper](https://arxiv.org/abs/2604.01570) · [![GitHub stars](https://img.shields.io/github/stars/Haochen-Niu/FAN-VLA?style=social)](https://github.com/Haochen-Niu/FAN-VLA) |

### Benchmarks for Distribution Shift

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization** | Zhou et al. | arXiv 2025 | Task | Non-adversarial OOD — benchmark, spatial shift, memorization | Benchmark, Spatial Shift, Memorization | [Paper](https://arxiv.org/abs/2510.03827) · [![GitHub stars](https://img.shields.io/github/stars/Zxy-MLlab/LIBERO-PRO?style=social)](https://github.com/Zxy-MLlab/LIBERO-PRO) |

### Geometry and Object-Centric Stress Testing

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Geometric Red-Teaming for Robotic Manipulation** | Goel et al. | arXiv 2025 | Task, Physical | Non-adversarial OOD — object geometry, red teaming, real robot | Object Geometry, Red Teaming, Real Robot | [Paper](https://arxiv.org/abs/2509.12379) |

### Language and Instruction Generalization

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **ICR-Drive: Instruction Counterfactual Robustness for End-to-End Language-Driven Autonomous Driving** | Hamid et al. | arXiv 2026 | Task, Physical | Non-adversarial OOD — language instruction, counterfactual robustness | Language Instruction, Counterfactual Robustness | [Paper](https://arxiv.org/abs/2604.05378) · [![GitHub stars](https://img.shields.io/github/stars/icrdrive/icrdrive?style=social)](https://github.com/icrdrive/icrdrive) |

### Open-World Evaluation

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **How VLAs (Really) Work in Open-World Environments** | Rasouli et al. | arXiv 2026 | Task, Physical | Non-adversarial OOD — open world, environment domain | Open World, Environment Domain | [Paper](https://arxiv.org/abs/2604.21192) |
| **pi0.5: A Vision-Language-Action Model with Open-World Generalization** | Black et al. | arXiv 2025 | Task, Physical | Non-adversarial OOD — open world, environment domain, long horizon | Open World, Environment Domain, Long Horizon | [Paper](https://arxiv.org/abs/2504.16054) · [![GitHub stars](https://img.shields.io/github/stars/Physical-Intelligence/openpi?style=social)](https://github.com/Physical-Intelligence/openpi) |

<a id="training-attacks"></a>

## 🧪 Training-Time Attacks

### Backdoors and Data Poisoning

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models** | Xu et al. | arXiv 2026 | Task, Physical, Security/Privacy | Training-time attack — backdoor, action chunk, temporal attack | Backdoor, Action Chunk, Temporal Attack | [Paper](https://arxiv.org/abs/2601.14323) |
| **State Backdoor: Towards Stealthy Real-World Poisoning Attack on Vision-Language-Action Models in State Space** | Guo et al. | arXiv 2026 | Task, Physical, Security/Privacy | Training-time attack — backdoor, state attack, physical access | Backdoor, State Attack, Physical Access | [Paper](https://arxiv.org/abs/2601.04266) |
| **BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization** | Zhou et al. | NeurIPS 2025 | Task, Physical, Security/Privacy | Training-time attack — backdoor, training data | Backdoor, Training Data | [Paper](https://arxiv.org/abs/2505.16640) · [![GitHub stars](https://img.shields.io/github/stars/Zxy-MLlab/BadVLA?style=social)](https://github.com/Zxy-MLlab/BadVLA) |
| **Can We Trust Embodied Agents? Exploring Backdoor Attacks Against Embodied LLM-Based Decision-Making Systems** | Jiao et al. | ICLR 2025 | Task, Physical, Security/Privacy | Training-time attack — backdoor, decision making, knowledge injection | Backdoor, Decision Making, Knowledge Injection | [Paper](https://arxiv.org/abs/2405.20774) · [![GitHub stars](https://img.shields.io/github/stars/ASGuard-UCI/BALD?style=social)](https://github.com/ASGuard-UCI/BALD) |
| **DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models** | Xu et al. | arXiv 2025 | Task, Physical, Security/Privacy | Training-time attack — backdoor, action output | Backdoor, Action Output | [Paper](https://arxiv.org/abs/2510.10932) · [![GitHub stars](https://img.shields.io/github/stars/megaknight114/DropVLA?style=social)](https://github.com/megaknight114/DropVLA) |
| **Goal-Oriented Backdoor Attack Against Vision-Language-Action Models via Physical Objects** | Zhou et al. | arXiv 2025 | Task, Physical, Security/Privacy | Training-time attack — physical-object backdoor for goal hijacking | Backdoor, Physical Object, Goal Hijacking | [Paper](https://arxiv.org/abs/2510.09269) · [Project / Code](https://goba-attack.github.io/) |

<a id="inference-attacks"></a>

## ⚡ Inference-Time Attacks

### Visual Perturbations and Patches

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models** | Lu et al. | CVPR 2026 | Task, Physical, Security/Privacy | Inference-time attack — adversarial patch, black box transfer, sim to real | Adversarial Patch, Black Box Transfer, Sim To Real | [Paper](https://arxiv.org/abs/2511.21192) · [![GitHub stars](https://img.shields.io/github/stars/yuyi-sd/UPA-RFAS?style=social)](https://github.com/yuyi-sd/UPA-RFAS) |
| **ADVEDM: Fine-Grained Adversarial Attack Against VLM-Based Embodied Agents** | Wang et al. | NeurIPS 2025 | Task, Physical | Inference-time attack — fine grained attack, semantic manipulation, visual perturbation | Fine Grained Attack, Semantic Manipulation, Visual Perturbation | [Paper](https://arxiv.org/abs/2509.16645) |
| **Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics** | Wang et al. | ICCV 2025 | Task, Physical | Inference-time attack — adversarial patch, digital perturbation, real robot | Adversarial Patch, Digital Perturbation, Real Robot | [Paper](https://arxiv.org/abs/2411.13587) · [![GitHub stars](https://img.shields.io/github/stars/William-wAng618/roboticAttack?style=social)](https://github.com/William-wAng618/roboticAttack) |
| **Model-Agnostic Adversarial Attack and Defense for Vision-Language-Action Models** | Xu et al. | arXiv 2025 | Task, Physical | Inference-time attack — adversarial patch, model agnostic, adversarial fine tuning | Adversarial Patch, Model Agnostic, Adversarial Fine Tuning | [Paper](https://arxiv.org/abs/2510.13237) · [![GitHub stars](https://img.shields.io/github/stars/trustmlyoungscientist/EDPA_attack_defense?style=social)](https://github.com/trustmlyoungscientist/EDPA_attack_defense) |
| **When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models** | Yan et al. | arXiv 2025 | Task, Physical | Inference-time attack — digital perturbation, multimodal misalignment | Digital Perturbation, Multimodal Misalignment | [Paper](https://arxiv.org/abs/2511.16203) |

### Planning, Action, and Trajectory Manipulation

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **FreezeVLA: Action-Freezing Attacks Against Vision-Language-Action Models** | Wang et al. | arXiv 2025 | Task, Physical | Inference-time attack — action freezing, dangerous inaction, digital perturbation | Action Freezing, Dangerous Inaction, Digital Perturbation | [Paper](https://arxiv.org/abs/2509.19870) · [![GitHub stars](https://img.shields.io/github/stars/xinwong/FreezeVLA?style=social)](https://github.com/xinwong/FreezeVLA) |

### Sensor, State, and Physical Interventions

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Phantom Menace: Exploring and Enhancing the Robustness of VLA Models Against Physical Sensor Attacks** | Lu et al. | AAAI 2026 | Task, Physical, Security/Privacy | Inference-time attack — sensor attack, physical intervention | Sensor Attack, Physical Intervention | [Paper](https://arxiv.org/abs/2511.10008) |

### Jailbreaks and Prompt Injection

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **CHAI: Command Hijacking Against Embodied AI** | Burbano et al. | SaTML 2026 | Physical, Ethical, Security/Privacy | Inference-time attack — command hijacking, typographic attack, visual prompt injection | Command Hijacking, Typographic Attack, Visual Prompt Injection | [Paper](https://arxiv.org/abs/2510.00181) · [![GitHub stars](https://img.shields.io/github/stars/Cyphysecurity/chai?style=social)](https://github.com/Cyphysecurity/chai) |
| **If You're Waiting for a Sign... That Might Not Be It! Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems** | Chang et al. | arXiv 2026 | Task, Physical, Ethical, Security/Privacy | Inference-time attack — untrusted scene text used as visual prompt injection | Visual Prompt Injection, Trust Boundary, Scene Text | [Paper](https://arxiv.org/abs/2604.19844) |
| **Adversarial Attacks on Robotic Vision-Language-Action Models** | Jones et al. | arXiv 2025 | Physical, Ethical, Security/Privacy | Inference-time attack — jailbreak, command hijacking | Jailbreak, Command Hijacking | [Paper](https://arxiv.org/abs/2506.03350) · [![GitHub stars](https://img.shields.io/github/stars/eliotjones1/robogcg?style=social)](https://github.com/eliotjones1/robogcg) |
| **BadRobot: Jailbreaking Embodied LLM Agents in the Physical World** | Zhang et al. | ICLR 2025 | Physical, Ethical, Security/Privacy | Inference-time attack — jailbreak, voice instruction, physical harm | Jailbreak, Voice Instruction, Physical Harm | [Paper](https://arxiv.org/abs/2407.20242) · [![GitHub stars](https://img.shields.io/github/stars/Rookie143/BadRobot?style=social)](https://github.com/Rookie143/BadRobot) |
| **Jailbreaking LLM-Controlled Robots** | Robey et al. | ICRA 2025 | Physical, Ethical, Security/Privacy | Inference-time attack — jailbreak, harmful policy, real robot | Jailbreak, Harmful Policy, Real Robot | [Paper](https://arxiv.org/abs/2410.13691) · [![GitHub stars](https://img.shields.io/github/stars/arobey1/robopair?style=social)](https://github.com/arobey1/robopair) |
| **POEX: Towards Policy Executable Jailbreak Attacks Against the LLM-Based Robots** | Lu et al. | arXiv 2025 | Physical, Ethical, Security/Privacy | Inference-time attack — jailbreak, policy executability, real robot | Jailbreak, Policy Executability, Real Robot | [Paper](https://arxiv.org/abs/2412.16633) · [Project / Code](https://poex-jailbreak.github.io/) |

### Upstream VLM Attacks

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Chain of Attack: On the Robustness of Vision-Language Models Against Transfer-Based Adversarial Attacks** | Xie et al. | CVPR 2025 | Task, Ethical, Security/Privacy | Inference-time attack — transfer attack, black box, multimodal semantics | Transfer Attack, Black Box, Multimodal Semantics | [Paper](https://arxiv.org/abs/2411.15720) · [![GitHub stars](https://img.shields.io/github/stars/Shelton1013/Chain_of_Attack?style=social)](https://github.com/Shelton1013/Chain_of_Attack) |

<a id="defenses"></a>

## 🛡️ Defenses and Safety Mechanisms

### Robust Training and Safety Alignment

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **SafeVLA: Towards Safety Alignment of Vision-Language-Action Models via Constrained Learning** | Zhang et al. | NeurIPS 2025 | Task, Physical, Ethical | Hazardous instructions and unsafe policy generation | Safety Alignment, Constrained Learning | [Paper](https://arxiv.org/abs/2503.03480) · [![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/SafeVLA?style=social)](https://github.com/PKU-Alignment/SafeVLA) |

### Runtime Monitoring and Guardrails

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **RC-NF: Robot-Conditioned Normalizing Flow for Real-Time Anomaly Detection in Robotic Manipulation** | Zhou et al. | arXiv 2026 | Task, Physical | Non-adversarial execution anomaly — state-conditioned manipulation failures | Anomaly Detection, Normalizing Flow, Runtime Monitoring | [Paper](https://arxiv.org/abs/2603.11106) |
| **Safety Guardrails for LLM-Enabled Robots** | Ravichandran et al. | IEEE RA-L 2026 | Physical, Ethical, Security/Privacy | Jailbreaks and unsafe plans from untrusted instructions | Guardrail, Control Synthesis | [Paper](https://arxiv.org/abs/2503.07885) |
| **From Words to Safety: Language-Conditioned Safety Filtering for Robot Navigation** | Feng et al. | arXiv 2025 | Task, Physical | Unsafe navigation commands and context-dependent physical constraint violations | Language Conditioned, Safety Filter, Navigation | [Paper](https://arxiv.org/abs/2511.05889) |
| **ROVER: Regulator-Driven Robust Temporal Verification of Black-Box Robot Policies** | Sakano et al. | arXiv 2025 | Task, Physical | Black-box policy failure — temporal safety-property violations during execution | Temporal Verification, Black Box Policy, Runtime Regulator | [Paper](https://arxiv.org/abs/2511.17781) |
| **VLSA: Vision-Language-Action Models with a Plug-and-Play Safety Constraint Layer** | Hu et al. | arXiv 2025 | Task, Physical | Unsafe VLA actions that violate physical constraints | Guardrail, Safety Constraint | [Paper](https://arxiv.org/abs/2512.11891) · [![GitHub stars](https://img.shields.io/github/stars/THU-RCSCT/vlsa-aegis?style=social)](https://github.com/THU-RCSCT/vlsa-aegis) |

### Action Shielding, Fail-Safes, and Recovery

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **SAFE: Multitask Failure Detection for Vision-Language-Action Models** | Gu et al. | NeurIPS 2025 | Task, Physical | Non-adversarial execution failures and OOD anomalies | Failure Detection, Runtime Monitoring | [Paper](https://arxiv.org/abs/2506.09937) · [![GitHub stars](https://img.shields.io/github/stars/vla-safe/SAFE?style=social)](https://github.com/vla-safe/SAFE) |
| **Plug in the Safety Chip: Enforcing Constraints for LLM-Driven Robot Agents** | Yang et al. | arXiv 2023 | Task, Physical | Unsafe LLM-generated plans that violate formal constraints | Formal Constraint, Runtime Monitoring | [Paper](https://arxiv.org/abs/2309.09919) |

### Representation Steering and Inference-Time Defense

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration** | Zhang et al. | arXiv 2026 | Task, Physical | Non-adversarial OOD — linguistic grounding degradation and instruction neglect | Linguistic Grounding, Attention Recalibration, Train Free | [Paper](https://arxiv.org/abs/2603.06001) |
| **Concept Enhancement Engineering: A Lightweight and Efficient Robust Defense Against Jailbreak Attacks in Embodied AI** | Yang et al. | arXiv 2025 | Physical, Ethical, Security/Privacy | Jailbreak attacks on embodied LLM planners | Jailbreak Defense, Representation Steering, Inference Time | [Paper](https://arxiv.org/abs/2504.13201) |

### System and Communication Defenses

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **AgentSafe: Safeguarding Large Language Model-Based Multi-Agent Systems via Hierarchical Data Management** | Mao et al. | arXiv 2025 | Task, Ethical, Security/Privacy | Memory poisoning, impersonation, and unauthorized inter-agent access | Multi Agent, Memory Defense, Communication Security | [Paper](https://arxiv.org/abs/2503.04392) |

### Active Perception and Recovery

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation** | Xu et al. | arXiv 2025 | Task, Physical | Non-adversarial OOD — spatial, object, color, and background shifts causing memory traps | Memory Trap, Affordance Field, Recovery | [Paper](https://arxiv.org/abs/2512.07472) |
| **FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models** | Lin et al. | arXiv 2025 | Task, Physical | Non-adversarial execution failure — detection, explanation, and closed-loop recovery | Failure Recovery, Reasoning, Closed Loop | [Paper](https://arxiv.org/abs/2510.01642) |
| **Embodied Active Defense: Leveraging Recurrent Feedback to Counter Adversarial Patches** | Wu et al. | ICLR 2024 | Task, Physical, Security/Privacy | Physical adversarial patches, including unseen or adaptive patches | Adversarial Patch, Active Perception, Recurrent Feedback | [Paper](https://arxiv.org/abs/2404.00540) |

### Multimodal Perception and Physical Safeguards

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation** | Yu et al. | arXiv 2026 | Task, Physical | Non-adversarial OOD — low light, hidden thermal state, occlusion, and geometric violations | Thermal Perception, Control Barrier Function, OOD | [Paper](https://arxiv.org/abs/2603.05754) · [Project / Code](https://thisanwerss.github.io/Safe-Night-VLA/) |

### Human-in-the-Loop Safety Refinement

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Human-in-the-Loop Online Rejection Sampling for Robotic Manipulation** | Lu et al. | arXiv 2025 | Task, Physical | Non-adversarial failure — unsafe or low-quality policy rollouts rejected by human feedback | Human In The Loop, Rejection Sampling, Policy Refinement | [Paper](https://arxiv.org/abs/2510.26406) · [Project / Code](https://hiors-project.github.io/) |

### Runtime Observation Interventions

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Run-Time Observation Interventions Make Vision-Language-Action Models More Visually Robust** | Hancock et al. | arXiv 2024 | Task, Physical | Non-adversarial OOD — task-irrelevant object and background distractors | Visual Distractor, Observation Intervention, Model Agnostic | [Paper](https://arxiv.org/abs/2410.01971) · [![GitHub stars](https://img.shields.io/github/stars/irom-princeton/byovla?style=social)](https://github.com/irom-princeton/byovla) |

<a id="benchmarks"></a>

## 📊 Benchmarks and Evaluation

### Comprehensive VLA Evaluation

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models** | Zhang et al. | arXiv 2025 | Task, Physical | Evaluation — capability, robustness, and closed-loop safety failures | Benchmark, Closed Loop | [Paper](https://arxiv.org/abs/2512.22539) · [![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/VLA-Arena?style=social)](https://github.com/PKU-Alignment/VLA-Arena) |

### Adversarial and Physical Robustness

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness** | Ru et al. | OpenReview 2026 | Task, Physical | Adversarial and physical robustness — visual and physical perturbations | Benchmark, Physical Robustness | [Paper](https://openreview.net/forum?id=31EjDFwFEe) |

### Task and Physical Safety

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks** | Lu et al. | AAAI 2026 | Task, Physical | Interactive physical hazards — mitigation and recovery failures | Interactive Safety, Risk Mitigation, Closed Loop | [Paper](https://arxiv.org/abs/2506.16402) |
| **SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents** | Yin et al. | arXiv 2025 | Task, Physical, Ethical | Hazardous instructions — unsafe embodied task planning | Hazardous Instruction, Task Planning | [Paper](https://arxiv.org/abs/2412.13178) · [![GitHub stars](https://img.shields.io/github/stars/shengyin1224/SafeAgentBench?style=social)](https://github.com/shengyin1224/SafeAgentBench) |
| **EARBench: Towards Evaluating Physical Risk Awareness for Task Planning of Foundation Model-Based Embodied AI Agents** | Zhu et al. | arXiv 2024 | Task, Physical | Physical-risk scenarios — insufficient hazard awareness | Physical Risk Awareness, Task Planning | [Paper](https://arxiv.org/abs/2408.04449) |

### Semantic and Ethical Safety

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Generating Robot Constitutions and Benchmarks for Semantic Safety** | Sermanet et al. | arXiv 2025 | Physical, Ethical | Semantic safety — constitution violations and harmful actions | Robot Constitution, Semantic Safety | [Paper](https://arxiv.org/abs/2503.08663) · [![GitHub stars](https://img.shields.io/github/stars/asimov-benchmark/asimov-benchmark.github.io?style=social)](https://github.com/asimov-benchmark/asimov-benchmark.github.io) |

### Evaluation Infrastructure

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Evaluating Real-World Robot Manipulation Policies in Simulation** | Li et al. | CoRL 2024 | Task, Physical | Sim-to-real shift — policy evaluation under environment mismatch | Simulation, Sim To Real, Evaluation Framework | [Paper](https://arxiv.org/abs/2405.05941) · [![GitHub stars](https://img.shields.io/github/stars/simpler-env/SimplerEnv?style=social)](https://github.com/simpler-env/SimplerEnv) |
| **LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning** | Liu et al. | NeurIPS Datasets and Benchmarks 2023 | Task | Non-adversarial OOD — task composition and knowledge-transfer shifts | Benchmark, Lifelong Learning, Knowledge Transfer | [Paper](https://arxiv.org/abs/2306.03310) · [![GitHub stars](https://img.shields.io/github/stars/Lifelong-Robot-Learning/LIBERO?style=social)](https://github.com/Lifelong-Robot-Learning/LIBERO) |

### Safety and Hazard Benchmarks

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models** | Chen et al. | arXiv 2026 | Task, Physical, Ethical | Semantic safety — hazardous instructions, unsafe context, and harmful action execution | Semantic Safety, Hazard, Benchmark | [Paper](https://arxiv.org/abs/2604.12447) |
| **AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions** | Ying et al. | arXiv 2025 | Physical, Ethical | Hazardous instructions — harmful or policy-violating embodied actions | Hazardous Instruction, Embodied Agent, Benchmark | [Paper](https://arxiv.org/abs/2506.14697) |
| **SafeMind: Benchmarking and Mitigating Safety Risks in Embodied LLM Agents** | Chen et al. | arXiv 2025 | Physical, Ethical, Security/Privacy | Hazardous instructions and unsafe embodied planning under adversarial prompting | Safety Benchmark, Jailbreak, Mitigation | [Paper](https://arxiv.org/abs/2509.25885) |

### Robustness and Uncertainty Evaluation

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Confidence Calibration in Vision-Language-Action Models** | Zollo et al. | arXiv 2025 | Task, Physical | Non-adversarial uncertainty — overconfidence under errors and distribution shift | Confidence Calibration, Uncertainty, Selective Prediction | [Paper](https://arxiv.org/abs/2507.17383) |
| **VLATest: Testing and Evaluating Vision-Language-Action Models for Robotic Manipulation** | Wang et al. | arXiv 2024 | Task, Physical | Evaluation — natural and adversarial input mutations in manipulation tasks | Testing, Input Mutation, Robotic Manipulation | [Paper](https://arxiv.org/abs/2409.12894) |

<a id="system-security"></a>

## 🔐 System-Level Security, Privacy, and Misuse

### Cross-Layer System Security

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Beyond Model Jailbreak: Systematic Dissection of the Ten Deadly Sins in Embodied Intelligence** | Huang et al. | arXiv 2025 | Physical, Security/Privacy | System-level attack — wireless, cloud, application, and firmware compromise | Cloud API, Firmware, Wireless | [Paper](https://arxiv.org/abs/2512.06387) |

### Privacy, Misuse, and Covert Channels

| Paper | Authors | Venue | Risk | Threat Model | Focus | Resources |
|---|---|---:|---|---|---|---|
| **Cyber-Physical Steganography in Robotic Motion Control** | Chang et al. | IEICE Transactions 2026 | Ethical, Security/Privacy | System-level misuse — covert channels encoded in robot trajectories | Covert Channel, Trajectory Manipulation, Misuse | [Paper](https://arxiv.org/abs/2501.04541) |

## Scope and Curation Policy

The core scope is VLA safety, robustness, security, and evaluation. Closely related LLM-robot, VLM-driven embodied-agent, autonomous-driving, and robot-policy papers are included when they expose a risk, mechanism, defense, or evaluation principle that transfers directly to VLA systems.

A paper is listed once under its primary contribution. Risk outcomes and mechanisms are represented as multi-label metadata rather than by duplicating the paper across sections.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and add or update the corresponding record in `data/papers.json`. Do not edit generated paper tables directly.

## Acknowledgements

The organization is informed by the lifecycle and attack/defense views used in [Awesome-VLA-Safety](https://github.com/LiQiiiii/Awesome-VLA-Safety) and [Awesome-LVLM-Safety](https://github.com/XuankunRong/Awesome-LVLM-Safety), extended with explicit risk-outcome and OOD-generalization axes.

## License

MIT License. Paper titles, author names, venues, and links remain the property of their respective authors and publishers.
