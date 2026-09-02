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

## Contents

- [Surveys and Perspectives](#surveys-and-perspectives)
- [Robustness and OOD Generalization](#robustness-and-ood-generalization)
- [Training-Time Attacks](#training-time-attacks)
- [Inference-Time Attacks](#inference-time-attacks)
- [Defenses and Safety Mechanisms](#defenses-and-safety-mechanisms)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [System-Level Security, Privacy, and Misuse](#system-level-security-privacy-and-misuse)

**49 papers in the current catalog.**

## Surveys and Perspectives

### VLA Safety Surveys

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms** | Li et al. | arXiv 2026 | Task, Physical, Ethical, Security/Privacy | Survey, Taxonomy | [Paper](https://arxiv.org/abs/2604.23775) · [![GitHub stars](https://img.shields.io/github/stars/LiQiiiii/Awesome-VLA-Safety?style=social)](https://github.com/LiQiiiii/Awesome-VLA-Safety) |

### Embodied AI Safety and Security

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Navigating Embodied Intelligence: Enabling Technologies, Security and Privacy, and Emerging Trends** | Wang et al. | IEEE IoT Journal 2026 | Task, Physical, Ethical, Security/Privacy | Survey, Security, Privacy | [Paper](https://doi.org/10.1109/JIOT.2025.3649049) |
| **What Breaks Embodied AI Security: LLM Vulnerabilities, CPS Flaws, or Something Else?** | Ma et al. | arXiv 2026 | Physical, Security/Privacy | Perspective, Closed Loop Safety | [Paper](https://arxiv.org/abs/2602.17345) |
| **Towards Robust and Secure Embodied AI: A Survey on Vulnerabilities and Attacks** | Xing et al. | arXiv 2025 | Task, Physical, Security/Privacy | Survey, Vulnerability Taxonomy | [Paper](https://arxiv.org/abs/2502.13175) |
| **Towards Safe and Trustworthy Embodied AI: Foundations, Status, and Prospects** | Tan et al. | OpenReview 2025 | Task, Physical, Ethical, Security/Privacy | Survey, Trustworthiness, Maturity Model | [Paper](https://openreview.net/forum?id=Eu6Yt21Alv) · [![GitHub stars](https://img.shields.io/github/stars/AI45Lab/Awesome-Trustworthy-Embodied-AI?style=social)](https://github.com/AI45Lab/Awesome-Trustworthy-Embodied-AI) |

### Domain-Specific Surveys

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **A Survey on Vision-Language-Action Models for Autonomous Driving** | Jiang et al. | arXiv 2025 | Task, Physical | Survey, Autonomous Driving, Closed Loop Control | [Paper](https://arxiv.org/abs/2506.24044) · [![GitHub stars](https://img.shields.io/github/stars/JohnsonJiang1996/Awesome-VLA4AD?style=social)](https://github.com/JohnsonJiang1996/Awesome-VLA4AD) |

## Robustness and OOD Generalization

### Representation and Language-Action Generalization

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment** | Dalal et al. | arXiv 2026 | Task | Representation Shift, Language Instruction, Viewpoint Camera | [Paper](https://arxiv.org/abs/2607.13429) · [![GitHub stars](https://img.shields.io/github/stars/dwipddalal/Anchor-Align?style=social)](https://github.com/dwipddalal/Anchor-Align) |

### Action and Spatial Generalization

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior** | Niu et al. | CVPR 2026 | Task, Physical | Action Neighborhood, Spatial Shift | [Paper](https://arxiv.org/abs/2604.01570) · [![GitHub stars](https://img.shields.io/github/stars/Haochen-Niu/FAN-VLA?style=social)](https://github.com/Haochen-Niu/FAN-VLA) |

### Benchmarks for Distribution Shift

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization** | Zhou et al. | arXiv 2025 | Task | Benchmark, Spatial Shift, Memorization | [Paper](https://arxiv.org/abs/2510.03827) · [![GitHub stars](https://img.shields.io/github/stars/Zxy-MLlab/LIBERO-PRO?style=social)](https://github.com/Zxy-MLlab/LIBERO-PRO) |

### Geometry and Object-Centric Stress Testing

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Geometric Red-Teaming for Robotic Manipulation** | Goel et al. | arXiv 2025 | Task, Physical | Object Geometry, Red Teaming, Real Robot | [Paper](https://arxiv.org/abs/2509.12379) |

### Language and Instruction Generalization

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **ICR-Drive: Instruction Counterfactual Robustness for End-to-End Language-Driven Autonomous Driving** | Hamid et al. | arXiv 2026 | Task, Physical | Language Instruction, Counterfactual Robustness | [Paper](https://arxiv.org/abs/2604.05378) · [![GitHub stars](https://img.shields.io/github/stars/icrdrive/icrdrive?style=social)](https://github.com/icrdrive/icrdrive) |

### Open-World Evaluation

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **How VLAs (Really) Work in Open-World Environments** | Rasouli et al. | arXiv 2026 | Task, Physical | Open World, Environment Domain | [Paper](https://arxiv.org/abs/2604.21192) |
| **pi0.5: A Vision-Language-Action Model with Open-World Generalization** | Black et al. | arXiv 2025 | Task, Physical | Open World, Environment Domain, Long Horizon | [Paper](https://arxiv.org/abs/2504.16054) · [![GitHub stars](https://img.shields.io/github/stars/Physical-Intelligence/openpi?style=social)](https://github.com/Physical-Intelligence/openpi) |

## Training-Time Attacks

### Backdoors and Data Poisoning

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models** | Xu et al. | arXiv 2026 | Task, Physical, Security/Privacy | Backdoor, Action Chunk, Temporal Attack | [Paper](https://arxiv.org/abs/2601.14323) |
| **State Backdoor: Towards Stealthy Real-World Poisoning Attack on Vision-Language-Action Models in State Space** | Guo et al. | arXiv 2026 | Task, Physical, Security/Privacy | Backdoor, State Attack, Physical Access | [Paper](https://arxiv.org/abs/2601.04266) |
| **BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization** | Zhou et al. | NeurIPS 2025 | Task, Physical, Security/Privacy | Backdoor, Training Data | [Paper](https://arxiv.org/abs/2505.16640) · [![GitHub stars](https://img.shields.io/github/stars/Zxy-MLlab/BadVLA?style=social)](https://github.com/Zxy-MLlab/BadVLA) |
| **Can We Trust Embodied Agents? Exploring Backdoor Attacks Against Embodied LLM-Based Decision-Making Systems** | Jiao et al. | ICLR 2025 | Task, Physical, Security/Privacy | Backdoor, Decision Making, Knowledge Injection | [Paper](https://arxiv.org/abs/2405.20774) · [![GitHub stars](https://img.shields.io/github/stars/ASGuard-UCI/BALD?style=social)](https://github.com/ASGuard-UCI/BALD) |
| **DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models** | Xu et al. | arXiv 2025 | Task, Physical, Security/Privacy | Backdoor, Action Output | [Paper](https://arxiv.org/abs/2510.10932) · [![GitHub stars](https://img.shields.io/github/stars/megaknight114/DropVLA?style=social)](https://github.com/megaknight114/DropVLA) |

## Inference-Time Attacks

### Visual Perturbations and Patches

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models** | Lu et al. | CVPR 2026 | Task, Physical, Security/Privacy | Adversarial Patch, Black Box Transfer, Sim To Real | [Paper](https://arxiv.org/abs/2511.21192) · [![GitHub stars](https://img.shields.io/github/stars/yuyi-sd/UPA-RFAS?style=social)](https://github.com/yuyi-sd/UPA-RFAS) |
| **ADVEDM: Fine-Grained Adversarial Attack Against VLM-Based Embodied Agents** | Wang et al. | NeurIPS 2025 | Task, Physical | Fine Grained Attack, Semantic Manipulation, Visual Perturbation | [Paper](https://arxiv.org/abs/2509.16645) |
| **Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics** | Wang et al. | ICCV 2025 | Task, Physical | Adversarial Patch, Digital Perturbation, Real Robot | [Paper](https://arxiv.org/abs/2411.13587) · [![GitHub stars](https://img.shields.io/github/stars/William-wAng618/roboticAttack?style=social)](https://github.com/William-wAng618/roboticAttack) |
| **Model-Agnostic Adversarial Attack and Defense for Vision-Language-Action Models** | Xu et al. | arXiv 2025 | Task, Physical | Adversarial Patch, Model Agnostic, Adversarial Fine Tuning | [Paper](https://arxiv.org/abs/2510.13237) · [![GitHub stars](https://img.shields.io/github/stars/trustmlyoungscientist/EDPA_attack_defense?style=social)](https://github.com/trustmlyoungscientist/EDPA_attack_defense) |
| **When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models** | Yan et al. | arXiv 2025 | Task, Physical | Digital Perturbation, Multimodal Misalignment | [Paper](https://arxiv.org/abs/2511.16203) |

### Planning, Action, and Trajectory Manipulation

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **FreezeVLA: Action-Freezing Attacks Against Vision-Language-Action Models** | Wang et al. | arXiv 2025 | Task, Physical | Action Freezing, Dangerous Inaction, Digital Perturbation | [Paper](https://arxiv.org/abs/2509.19870) · [![GitHub stars](https://img.shields.io/github/stars/xinwong/FreezeVLA?style=social)](https://github.com/xinwong/FreezeVLA) |

### Sensor, State, and Physical Interventions

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Phantom Menace: Exploring and Enhancing the Robustness of VLA Models Against Physical Sensor Attacks** | Lu et al. | AAAI 2026 | Task, Physical, Security/Privacy | Sensor Attack, Physical Intervention | [Paper](https://arxiv.org/abs/2511.10008) |

### Jailbreaks and Prompt Injection

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **CHAI: Command Hijacking Against Embodied AI** | Burbano et al. | SaTML 2026 | Physical, Ethical, Security/Privacy | Command Hijacking, Typographic Attack, Visual Prompt Injection | [Paper](https://arxiv.org/abs/2510.00181) · [![GitHub stars](https://img.shields.io/github/stars/Cyphysecurity/chai?style=social)](https://github.com/Cyphysecurity/chai) |
| **Adversarial Attacks on Robotic Vision-Language-Action Models** | Jones et al. | arXiv 2025 | Physical, Ethical, Security/Privacy | Jailbreak, Command Hijacking | [Paper](https://arxiv.org/abs/2506.03350) · [![GitHub stars](https://img.shields.io/github/stars/eliotjones1/robogcg?style=social)](https://github.com/eliotjones1/robogcg) |
| **BadRobot: Jailbreaking Embodied LLM Agents in the Physical World** | Zhang et al. | ICLR 2025 | Physical, Ethical, Security/Privacy | Jailbreak, Voice Instruction, Physical Harm | [Paper](https://arxiv.org/abs/2407.20242) · [![GitHub stars](https://img.shields.io/github/stars/Rookie143/BadRobot?style=social)](https://github.com/Rookie143/BadRobot) |
| **Jailbreaking LLM-Controlled Robots** | Robey et al. | ICRA 2025 | Physical, Ethical, Security/Privacy | Jailbreak, Harmful Policy, Real Robot | [Paper](https://arxiv.org/abs/2410.13691) · [![GitHub stars](https://img.shields.io/github/stars/arobey1/robopair?style=social)](https://github.com/arobey1/robopair) |
| **POEX: Towards Policy Executable Jailbreak Attacks Against the LLM-Based Robots** | Lu et al. | arXiv 2025 | Physical, Ethical, Security/Privacy | Jailbreak, Policy Executability, Real Robot | [Paper](https://arxiv.org/abs/2412.16633) · [Project / Code](https://poex-jailbreak.github.io/) |

### Upstream VLM Attacks

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Chain of Attack: On the Robustness of Vision-Language Models Against Transfer-Based Adversarial Attacks** | Xie et al. | CVPR 2025 | Task, Ethical, Security/Privacy | Transfer Attack, Black Box, Multimodal Semantics | [Paper](https://arxiv.org/abs/2411.15720) · [![GitHub stars](https://img.shields.io/github/stars/Shelton1013/Chain_of_Attack?style=social)](https://github.com/Shelton1013/Chain_of_Attack) |

## Defenses and Safety Mechanisms

### Robust Training and Safety Alignment

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **SafeVLA: Towards Safety Alignment of Vision-Language-Action Models via Constrained Learning** | Zhang et al. | NeurIPS 2025 | Task, Physical, Ethical | Safety Alignment, Constrained Learning | [Paper](https://arxiv.org/abs/2503.03480) · [![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/SafeVLA?style=social)](https://github.com/PKU-Alignment/SafeVLA) |

### Runtime Monitoring and Guardrails

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Safety Guardrails for LLM-Enabled Robots** | Ravichandran et al. | IEEE RA-L 2026 | Physical, Ethical, Security/Privacy | Guardrail, Control Synthesis | [Paper](https://arxiv.org/abs/2503.07885) |
| **VLSA: Vision-Language-Action Models with a Plug-and-Play Safety Constraint Layer** | Hu et al. | arXiv 2025 | Task, Physical | Guardrail, Safety Constraint | [Paper](https://arxiv.org/abs/2512.11891) · [![GitHub stars](https://img.shields.io/github/stars/THU-RCSCT/vlsa-aegis?style=social)](https://github.com/THU-RCSCT/vlsa-aegis) |

### Action Shielding, Fail-Safes, and Recovery

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **SAFE: Multitask Failure Detection for Vision-Language-Action Models** | Gu et al. | NeurIPS 2025 | Task, Physical | Failure Detection, Runtime Monitoring | [Paper](https://arxiv.org/abs/2506.09937) · [![GitHub stars](https://img.shields.io/github/stars/vla-safe/SAFE?style=social)](https://github.com/vla-safe/SAFE) |
| **Plug in the Safety Chip: Enforcing Constraints for LLM-Driven Robot Agents** | Yang et al. | arXiv 2023 | Task, Physical | Formal Constraint, Runtime Monitoring | [Paper](https://arxiv.org/abs/2309.09919) |

### Representation Steering and Inference-Time Defense

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Concept Enhancement Engineering: A Lightweight and Efficient Robust Defense Against Jailbreak Attacks in Embodied AI** | Yang et al. | arXiv 2025 | Physical, Ethical, Security/Privacy | Jailbreak Defense, Representation Steering, Inference Time | [Paper](https://arxiv.org/abs/2504.13201) |

### System and Communication Defenses

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **AgentSafe: Safeguarding Large Language Model-Based Multi-Agent Systems via Hierarchical Data Management** | Mao et al. | arXiv 2025 | Task, Ethical, Security/Privacy | Multi Agent, Memory Defense, Communication Security | [Paper](https://arxiv.org/abs/2503.04392) |

### Active Perception and Recovery

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Embodied Active Defense: Leveraging Recurrent Feedback to Counter Adversarial Patches** | Wu et al. | ICLR 2024 | Task, Physical, Security/Privacy | Adversarial Patch, Active Perception, Recurrent Feedback | [Paper](https://arxiv.org/abs/2404.00540) |

## Benchmarks and Evaluation

### Comprehensive VLA Evaluation

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models** | Zhang et al. | arXiv 2025 | Task, Physical | Benchmark, Closed Loop | [Paper](https://arxiv.org/abs/2512.22539) · [![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/VLA-Arena?style=social)](https://github.com/PKU-Alignment/VLA-Arena) |

### Adversarial and Physical Robustness

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness** | Ru et al. | OpenReview 2026 | Task, Physical | Benchmark, Physical Robustness | [Paper](https://openreview.net/forum?id=31EjDFwFEe) |

### Task and Physical Safety

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks** | Lu et al. | AAAI 2026 | Task, Physical | Interactive Safety, Risk Mitigation, Closed Loop | [Paper](https://arxiv.org/abs/2506.16402) |
| **SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents** | Yin et al. | arXiv 2025 | Task, Physical, Ethical | Hazardous Instruction, Task Planning | [Paper](https://arxiv.org/abs/2412.13178) · [![GitHub stars](https://img.shields.io/github/stars/shengyin1224/SafeAgentBench?style=social)](https://github.com/shengyin1224/SafeAgentBench) |
| **EARBench: Towards Evaluating Physical Risk Awareness for Task Planning of Foundation Model-Based Embodied AI Agents** | Zhu et al. | arXiv 2024 | Task, Physical | Physical Risk Awareness, Task Planning | [Paper](https://arxiv.org/abs/2408.04449) |

### Semantic and Ethical Safety

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Generating Robot Constitutions and Benchmarks for Semantic Safety** | Sermanet et al. | arXiv 2025 | Physical, Ethical | Robot Constitution, Semantic Safety | [Paper](https://arxiv.org/abs/2503.08663) · [![GitHub stars](https://img.shields.io/github/stars/asimov-benchmark/asimov-benchmark.github.io?style=social)](https://github.com/asimov-benchmark/asimov-benchmark.github.io) |

### Evaluation Infrastructure

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Evaluating Real-World Robot Manipulation Policies in Simulation** | Li et al. | CoRL 2024 | Task, Physical | Simulation, Sim To Real, Evaluation Framework | [Paper](https://arxiv.org/abs/2405.05941) · [![GitHub stars](https://img.shields.io/github/stars/simpler-env/SimplerEnv?style=social)](https://github.com/simpler-env/SimplerEnv) |
| **LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning** | Liu et al. | NeurIPS Datasets and Benchmarks 2023 | Task | Benchmark, Lifelong Learning, Knowledge Transfer | [Paper](https://arxiv.org/abs/2306.03310) · [![GitHub stars](https://img.shields.io/github/stars/Lifelong-Robot-Learning/LIBERO?style=social)](https://github.com/Lifelong-Robot-Learning/LIBERO) |

## System-Level Security, Privacy, and Misuse

### Cross-Layer System Security

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Beyond Model Jailbreak: Systematic Dissection of the Ten Deadly Sins in Embodied Intelligence** | Huang et al. | arXiv 2025 | Physical, Security/Privacy | Cloud API, Firmware, Wireless | [Paper](https://arxiv.org/abs/2512.06387) |

### Privacy, Misuse, and Covert Channels

| Paper | Authors | Venue | Risk | Focus | Resources |
|---|---|---:|---|---|---|
| **Cyber-Physical Steganography in Robotic Motion Control** | Chang et al. | IEICE Transactions 2026 | Ethical, Security/Privacy | Covert Channel, Trajectory Manipulation, Misuse | [Paper](https://arxiv.org/abs/2501.04541) |

## Scope and Curation Policy

The core scope is VLA safety, robustness, security, and evaluation. Closely related LLM-robot, VLM-driven embodied-agent, autonomous-driving, and robot-policy papers are included when they expose a risk, mechanism, defense, or evaluation principle that transfers directly to VLA systems.

A paper is listed once under its primary contribution. Risk outcomes and mechanisms are represented as multi-label metadata rather than by duplicating the paper across sections.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and add or update the corresponding record in `data/papers.json`. Do not edit generated paper tables directly.

## Acknowledgements

The organization is informed by the lifecycle and attack/defense views used in [Awesome-VLA-Safety](https://github.com/LiQiiiii/Awesome-VLA-Safety) and [Awesome-LVLM-Safety](https://github.com/XuankunRong/Awesome-LVLM-Safety), extended with explicit risk-outcome and OOD-generalization axes.

## License

MIT License. Paper titles, author names, venues, and links remain the property of their respective authors and publishers.
