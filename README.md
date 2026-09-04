# Awesome Responsible VLA

A curated, taxonomy-driven list of research on the safety, robustness, security, and responsible deployment of Vision-Language-Action models and closely related embodied agents.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> This list separates **empirically evaluated risk outcomes** (what the paper measures) from **failure sources and mechanisms** (why it goes wrong). GitHub star badges are live and are shown only for identified official repositories.

## Taxonomy at a Glance

### Risk outcomes

A label is shown only when the paper reports a corresponding empirical outcome metric; discussion or potential impact alone does not qualify.

- ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) task or route completion, success rate, or equivalent execution outcome.
- ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) collision, damage, unsafe motion or force, physical harm, or safety-constraint violation.
- ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) harmful-instruction compliance or refusal, prohibited behavior, or policy/constitution violation.
- ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) attack success, backdoor activation, control hijacking, unauthorized access, leakage, or compromise.
- **—:** no directly corresponding outcome is empirically evaluated, as is common for surveys and diagnostic-only work.

### Failure sources

- **Adversarial:** malicious manipulation of inputs, training, states, actions, or system components.
- **Non-adversarial / OOD:** failures under unseen viewpoints, objects, language, tasks, environments, embodiments, or dynamics.
- **Design / system:** misalignment, misspecified objectives, sensor faults, planner-executor mismatch, or failed recovery.

### Threat model badges

Each concrete threat model is rendered in two lines. A `+N` suffix indicates additional values retained in `data/papers.json`.

![Lifecycle](https://img.shields.io/badge/-Lifecycle-2563EB?style=flat-square) ![Surface](https://img.shields.io/badge/-Surface-0F766E?style=flat-square)<br>![Mechanism](https://img.shields.io/badge/-Mechanism-C2410C?style=flat-square) &nbsp;→&nbsp; ![Target](https://img.shields.io/badge/-Target-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Consequence](https://img.shields.io/badge/-Consequence-B91C1C?style=flat-square)

See [the full taxonomy](docs/taxonomy.md) for definitions and inclusion rules.

## 🧭 Contents

- [📚 Surveys and Perspectives](#surveys)
- [🌍 Robustness and OOD Generalization](#ood-generalization)
- [🧪 Training-Time Attacks](#training-attacks)
- [⚡ Inference-Time Attacks](#inference-attacks)
- [🛡️ Defenses and Safety Mechanisms](#defenses)
- [📊 Benchmarks and Evaluation](#benchmarks)
- [🔐 System-Level Security, Privacy, and Misuse](#system-security)

<details>
<summary><strong>Show subsection index</strong></summary>

- **📚 Surveys and Perspectives**
  - [VLA Safety Surveys](#surveys-vla-safety-surveys)
  - [Embodied AI Safety and Security](#surveys-embodied-ai-safety-and-security)
  - [Domain-Specific Surveys](#surveys-domain-specific-surveys)
  - [Position Papers and Research Agendas](#surveys-position-papers-and-research-agendas)
  - [General VLA Surveys](#surveys-general-vla-surveys)
  - [Training and Adaptation Surveys](#surveys-training-and-adaptation-surveys)
- **🌍 Robustness and OOD Generalization**
  - [Representation and Language-Action Generalization](#ood-generalization-representation-and-language-action-generalization)
  - [Action and Spatial Generalization](#ood-generalization-action-and-spatial-generalization)
  - [Geometry and Object-Centric Stress Testing](#ood-generalization-geometry-and-object-centric-stress-testing)
  - [Language and Instruction Generalization](#ood-generalization-language-and-instruction-generalization)
  - [Open-World Evaluation](#ood-generalization-open-world-evaluation)
  - [Driving Robustness and Generalization](#ood-generalization-driving-robustness-and-generalization)
- **🧪 Training-Time Attacks**
  - [Backdoors and Data Poisoning](#training-attacks-backdoors-and-data-poisoning)
- **⚡ Inference-Time Attacks**
  - [Visual Perturbations and Patches](#inference-attacks-visual-perturbations-and-patches)
  - [Planning, Action, and Trajectory Manipulation](#inference-attacks-planning-action-and-trajectory-manipulation)
  - [Sensor, State, and Physical Interventions](#inference-attacks-sensor-state-and-physical-interventions)
  - [Jailbreaks and Prompt Injection](#inference-attacks-jailbreaks-and-prompt-injection)
  - [Upstream VLM Attacks](#inference-attacks-upstream-vlm-attacks)
- **🛡️ Defenses and Safety Mechanisms**
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
- **📊 Benchmarks and Evaluation**
  - [OOD and Generalization Benchmarks](#benchmarks-ood-and-generalization-benchmarks)
  - [Comprehensive VLA Evaluation](#benchmarks-comprehensive-vla-evaluation)
  - [Adversarial and Physical Robustness](#benchmarks-adversarial-and-physical-robustness)
  - [Task and Physical Safety](#benchmarks-task-and-physical-safety)
  - [Semantic and Ethical Safety](#benchmarks-semantic-and-ethical-safety)
  - [Evaluation Infrastructure](#benchmarks-evaluation-infrastructure)
  - [Safety and Hazard Benchmarks](#benchmarks-safety-and-hazard-benchmarks)
  - [Robustness and Uncertainty Evaluation](#benchmarks-robustness-and-uncertainty-evaluation)
  - [Safety-Critical Perception Evaluation](#benchmarks-safety-critical-perception-evaluation)
- **🔐 System-Level Security, Privacy, and Misuse**
  - [Cross-Layer System Security](#system-security-cross-layer-system-security)
  - [Privacy, Misuse, and Covert Channels](#system-security-privacy-misuse-and-covert-channels)

</details>

**124 papers in the current catalog.**

<a id="surveys"></a>

## 📚 Surveys and Perspectives

<a id="surveys-vla-safety-surveys"></a>

### VLA Safety Surveys

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms](https://arxiv.org/abs/2604.23775)** [![GitHub stars](https://img.shields.io/github/stars/LiQiiiii/Awesome-VLA-Safety?style=social)](https://github.com/LiQiiiii/Awesome-VLA-Safety)<br><sub>Li et al.</sub> | arXiv 2026 | — | ![Cross-lifecycle](https://img.shields.io/badge/-Cross--lifecycle-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |

<a id="surveys-embodied-ai-safety-and-security"></a>

### Embodied AI Safety and Security

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Navigating Embodied Intelligence: Enabling Technologies, Security and Privacy, and Emerging Trends](https://doi.org/10.1109/JIOT.2025.3649049)**<br><sub>Wang et al.</sub> | IEEE IoT Journal 2026 | — | ![Cross-lifecycle](https://img.shields.io/badge/-Cross--lifecycle-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |
| **[What Breaks Embodied AI Security: LLM Vulnerabilities, CPS Flaws, or Something Else?](https://arxiv.org/abs/2602.17345)**<br><sub>Ma et al.</sub> | arXiv 2026 | — | ![Inference → System](https://img.shields.io/badge/-Inference_%E2%86%92_System-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |
| **[Towards Robust and Secure Embodied AI: A Survey on Vulnerabilities and Attacks](https://arxiv.org/abs/2502.13175)**<br><sub>Xing et al.</sub> | arXiv 2025 | — | ![Cross-lifecycle](https://img.shields.io/badge/-Cross--lifecycle-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |
| **[Towards Safe and Trustworthy Embodied AI: Foundations, Status, and Prospects](https://openreview.net/forum?id=Eu6Yt21Alv)** [![GitHub stars](https://img.shields.io/github/stars/AI45Lab/Awesome-Trustworthy-Embodied-AI?style=social)](https://github.com/AI45Lab/Awesome-Trustworthy-Embodied-AI)<br><sub>Tan et al.</sub> | OpenReview 2025 | — | ![Cross-lifecycle](https://img.shields.io/badge/-Cross--lifecycle-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |

<a id="surveys-domain-specific-surveys"></a>

### Domain-Specific Surveys

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[A Survey on Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2506.24044)** [![GitHub stars](https://img.shields.io/github/stars/JohnsonJiang1996/Awesome-VLA4AD?style=social)](https://github.com/JohnsonJiang1996/Awesome-VLA4AD)<br><sub>Jiang et al.</sub> | arXiv 2025 | — | ![Cross-lifecycle](https://img.shields.io/badge/-Cross--lifecycle-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |
| **[Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](https://arxiv.org/abs/2510.07077)** [Project / Code](https://vla-survey.github.io/)<br><sub>Kawaharazuka et al.</sub> | IEEE Access 2025 | — | ![Cross-lifecycle](https://img.shields.io/badge/-Cross--lifecycle-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |

<a id="surveys-position-papers-and-research-agendas"></a>

### Position Papers and Research Agendas

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Position: Human-Robot Interaction in Embodied Intelligence Demands a Shift From Static Privacy Controls to Dynamic Learning](https://arxiv.org/abs/2509.19041)**<br><sub>Zhang et al.</sub> | NeurIPS Workshop 2025 | — | ![Inference → System](https://img.shields.io/badge/-Inference_%E2%86%92_System-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |

<a id="surveys-general-vla-surveys"></a>

### General VLA Surveys

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey](https://arxiv.org/abs/2508.13073)** [![GitHub stars](https://img.shields.io/github/stars/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation?style=social)](https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation)<br><sub>Shao et al.</sub> | arXiv 2025 | — | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |
| **[Pure Vision Language Action (VLA) Models: A Comprehensive Survey](https://arxiv.org/abs/2509.19012)**<br><sub>Zhang et al.</sub> | arXiv 2025 | — | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |
| **[Vision Language Action Models in Robotic Manipulation: A Systematic Review](https://arxiv.org/abs/2507.10672)** [![GitHub stars](https://img.shields.io/github/stars/Muhayyuddin/VLAs?style=social)](https://github.com/Muhayyuddin/VLAs)<br><sub>Din et al.</sub> | arXiv 2025 | — | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |
| **[Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges](https://arxiv.org/abs/2505.04769)** [![GitHub stars](https://img.shields.io/github/stars/Applied-AI-Research-Lab/Vision-Language-Action-Models-Concepts-Progress-Applications-and-Challenges?style=social)](https://github.com/Applied-AI-Research-Lab/Vision-Language-Action-Models-Concepts-Progress-Applications-and-Challenges)<br><sub>Sapkota et al.</sub> | arXiv 2025 | — | ![Cross-lifecycle](https://img.shields.io/badge/-Cross--lifecycle-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |
| **[A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093)** [![GitHub stars](https://img.shields.io/github/stars/yueen-ma/Awesome-VLA?style=social)](https://github.com/yueen-ma/Awesome-VLA)<br><sub>Ma et al.</sub> | arXiv 2024 | — | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |

<a id="surveys-training-and-adaptation-surveys"></a>

### Training and Adaptation Surveys

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[A Survey on Efficient Vision-Language-Action Models](https://arxiv.org/abs/2510.24795)** [Project / Code](https://evla-survey.github.io/)<br><sub>Yu et al.</sub> | arXiv 2025 | — | ![Cross-lifecycle](https://img.shields.io/badge/-Cross--lifecycle-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |
| **[A Survey on Vision-Language-Action Models: An Action Tokenization Perspective](https://arxiv.org/abs/2507.01925)**<br><sub>Zhong et al.</sub> | arXiv 2025 | — | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Action Interface + Reasoning Representation](https://img.shields.io/badge/-Action_Interface_%2B_Reasoning_Representation-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |
| **[Parallels Between VLA Model Post-Training and Human Motor Learning: Progress, Challenges, and Trends](https://arxiv.org/abs/2506.20966)** [![GitHub stars](https://img.shields.io/github/stars/AoqunJin/Awesome-VLA-Post-Training?style=social)](https://github.com/AoqunJin/Awesome-VLA-Post-Training)<br><sub>Xiang et al.</sub> | arXiv 2025 | — | ![Training](https://img.shields.io/badge/-Training-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Survey coverage](https://img.shields.io/badge/-Survey_coverage-6B7280?style=flat-square) |

<a id="ood-generalization"></a>

## 🌍 Robustness and OOD Generalization

<a id="ood-generalization-representation-and-language-action-generalization"></a>

### Representation and Language-Action Generalization

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](https://arxiv.org/abs/2607.13429)** [![GitHub stars](https://img.shields.io/github/stars/dwipddalal/Anchor-Align?style=social)](https://github.com/dwipddalal/Anchor-Align)<br><sub>Dalal et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization](https://arxiv.org/abs/2510.25616)** [Project / Code](https://blind-vla-paper.github.io/)<br><sub>Kachaev et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +1](https://img.shields.io/badge/-Visual_Perception_%2B1-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="ood-generalization-action-and-spatial-generalization"></a>

### Action and Spatial Generalization

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior](https://arxiv.org/abs/2604.01570)** [![GitHub stars](https://img.shields.io/github/stars/Haochen-Niu/FAN-VLA?style=social)](https://github.com/Haochen-Niu/FAN-VLA)<br><sub>Niu et al.</sub> | CVPR 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![World State +1](https://img.shields.io/badge/-World_State_%2B1-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="ood-generalization-geometry-and-object-centric-stress-testing"></a>

### Geometry and Object-Centric Stress Testing

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Geometric Red-Teaming for Robotic Manipulation](https://arxiv.org/abs/2509.12379)**<br><sub>Goel et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +1](https://img.shields.io/badge/-Visual_Perception_%2B1-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="ood-generalization-language-and-instruction-generalization"></a>

### Language and Instruction Generalization

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[ICR-Drive: Instruction Counterfactual Robustness for End-to-End Language-Driven Autonomous Driving](https://arxiv.org/abs/2604.05378)** [![GitHub stars](https://img.shields.io/github/stars/icrdrive/icrdrive?style=social)](https://github.com/icrdrive/icrdrive)<br><sub>Hamid et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +1](https://img.shields.io/badge/-User_Instruction_%2B1-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="ood-generalization-open-world-evaluation"></a>

### Open-World Evaluation

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[How VLAs (Really) Work in Open-World Environments](https://arxiv.org/abs/2604.21192)**<br><sub>Rasouli et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +1](https://img.shields.io/badge/-Visual_Perception_%2B1-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[pi0.5: A Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)** [![GitHub stars](https://img.shields.io/github/stars/Physical-Intelligence/openpi?style=social)](https://github.com/Physical-Intelligence/openpi)<br><sub>Black et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="ood-generalization-driving-robustness-and-generalization"></a>

### Driving Robustness and Generalization

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Generative Scenario Rollouts for End-to-End Autonomous Driving](https://arxiv.org/abs/2601.11475)**<br><sub>Yasarla et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![World State +1](https://img.shields.io/badge/-World_State_%2B1-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Shift & Drift: A Zero-Shot Benchmark for Generalizable and Robust Autonomous Driving Motion Planning](https://arxiv.org/abs/2607.07844)**<br><sub>Canevaro et al.</sub> | IROS 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![World State +1](https://img.shields.io/badge/-World_State_%2B1-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="training-attacks"></a>

## 🧪 Training-Time Attacks

<a id="training-attacks-backdoors-and-data-poisoning"></a>

### Backdoors and Data Poisoning

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Inject Once Survive Later: Backdooring Vision-Language-Action Models to Persist Through Downstream Fine-tuning](https://arxiv.org/abs/2602.00500)** [Project / Code](https://jianyi2004.github.io/infuse-vla-backdoor/)<br><sub>Zhou et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Model Supply Chain +1](https://img.shields.io/badge/-Model_Supply_Chain_%2B1-0F766E?style=flat-square) <br> ![Backdoor](https://img.shields.io/badge/-Backdoor-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Targeted Action](https://img.shields.io/badge/-Targeted_Action-B91C1C?style=flat-square) |
| **[SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2601.14323)**<br><sub>Xu et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Model Supply Chain +2](https://img.shields.io/badge/-Model_Supply_Chain_%2B2-0F766E?style=flat-square) <br> ![Backdoor](https://img.shields.io/badge/-Backdoor-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Targeted Action](https://img.shields.io/badge/-Targeted_Action-B91C1C?style=flat-square) |
| **[State Backdoor: Towards Stealthy Real-World Poisoning Attack on Vision-Language-Action Models in State Space](https://arxiv.org/abs/2601.04266)**<br><sub>Guo et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Model Supply Chain +2](https://img.shields.io/badge/-Model_Supply_Chain_%2B2-0F766E?style=flat-square) <br> ![Backdoor](https://img.shields.io/badge/-Backdoor-C2410C?style=flat-square) &nbsp;→&nbsp; ![World State](https://img.shields.io/badge/-World_State-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Targeted Action](https://img.shields.io/badge/-Targeted_Action-B91C1C?style=flat-square) |
| **[BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://arxiv.org/abs/2505.16640)** [![GitHub stars](https://img.shields.io/github/stars/Zxy-MLlab/BadVLA?style=social)](https://github.com/Zxy-MLlab/BadVLA)<br><sub>Zhou et al.</sub> | NeurIPS 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Model Supply Chain +1](https://img.shields.io/badge/-Model_Supply_Chain_%2B1-0F766E?style=flat-square) <br> ![Backdoor](https://img.shields.io/badge/-Backdoor-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Targeted Action](https://img.shields.io/badge/-Targeted_Action-B91C1C?style=flat-square) |
| **[Can We Trust Embodied Agents? Exploring Backdoor Attacks Against Embodied LLM-Based Decision-Making Systems](https://arxiv.org/abs/2405.20774)** [![GitHub stars](https://img.shields.io/github/stars/ASGuard-UCI/BALD?style=social)](https://github.com/ASGuard-UCI/BALD)<br><sub>Jiao et al.</sub> | ICLR 2025 | ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Model Supply Chain +1](https://img.shields.io/badge/-Model_Supply_Chain_%2B1-0F766E?style=flat-square) <br> ![Backdoor](https://img.shields.io/badge/-Backdoor-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Targeted Action](https://img.shields.io/badge/-Targeted_Action-B91C1C?style=flat-square) |
| **[DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models](https://arxiv.org/abs/2510.10932)** [![GitHub stars](https://img.shields.io/github/stars/megaknight114/DropVLA?style=social)](https://github.com/megaknight114/DropVLA)<br><sub>Xu et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Model Supply Chain +2](https://img.shields.io/badge/-Model_Supply_Chain_%2B2-0F766E?style=flat-square) <br> ![Backdoor](https://img.shields.io/badge/-Backdoor-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Targeted Action](https://img.shields.io/badge/-Targeted_Action-B91C1C?style=flat-square) |
| **[Goal-Oriented Backdoor Attack Against Vision-Language-Action Models via Physical Objects](https://arxiv.org/abs/2510.09269)** [Project / Code](https://goba-attack.github.io/)<br><sub>Zhou et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Model Supply Chain +2](https://img.shields.io/badge/-Model_Supply_Chain_%2B2-0F766E?style=flat-square) <br> ![Backdoor](https://img.shields.io/badge/-Backdoor-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Targeted Action](https://img.shields.io/badge/-Targeted_Action-B91C1C?style=flat-square) |

<a id="inference-attacks"></a>

## ⚡ Inference-Time Attacks

<a id="inference-attacks-visual-perturbations-and-patches"></a>

### Visual Perturbations and Patches

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.21192)** [![GitHub stars](https://img.shields.io/github/stars/yuyi-sd/UPA-RFAS?style=social)](https://github.com/yuyi-sd/UPA-RFAS)<br><sub>Lu et al.</sub> | CVPR 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Adversarial Patch](https://img.shields.io/badge/-Adversarial_Patch-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[ADVEDM: Fine-Grained Adversarial Attack Against VLM-Based Embodied Agents](https://arxiv.org/abs/2509.16645)**<br><sub>Wang et al.</sub> | NeurIPS 2025 | ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Digital Perturbation](https://img.shields.io/badge/-Digital_Perturbation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Reasoning Process](https://img.shields.io/badge/-Reasoning_Process-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Targeted Action](https://img.shields.io/badge/-Targeted_Action-B91C1C?style=flat-square) |
| **[Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2411.13587)** [![GitHub stars](https://img.shields.io/github/stars/William-wAng618/roboticAttack?style=social)](https://github.com/William-wAng618/roboticAttack)<br><sub>Wang et al.</sub> | ICCV 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Adversarial Patch](https://img.shields.io/badge/-Adversarial_Patch-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Model-Agnostic Adversarial Attack and Defense for Vision-Language-Action Models](https://arxiv.org/abs/2510.13237)** [![GitHub stars](https://img.shields.io/github/stars/trustmlyoungscientist/EDPA_attack_defense?style=social)](https://github.com/trustmlyoungscientist/EDPA_attack_defense)<br><sub>Xu et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Adversarial Patch](https://img.shields.io/badge/-Adversarial_Patch-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.16203)**<br><sub>Yan et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +1](https://img.shields.io/badge/-Visual_Perception_%2B1-0F766E?style=flat-square) <br> ![Digital Perturbation](https://img.shields.io/badge/-Digital_Perturbation-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="inference-attacks-planning-action-and-trajectory-manipulation"></a>

### Planning, Action, and Trajectory Manipulation

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[FreezeVLA: Action-Freezing Attacks Against Vision-Language-Action Models](https://arxiv.org/abs/2509.19870)** [![GitHub stars](https://img.shields.io/github/stars/xinwong/FreezeVLA?style=social)](https://github.com/xinwong/FreezeVLA)<br><sub>Wang et al.</sub> | arXiv 2025 | ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Digital Perturbation](https://img.shields.io/badge/-Digital_Perturbation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Action Freezing](https://img.shields.io/badge/-Action_Freezing-B91C1C?style=flat-square) |

<a id="inference-attacks-sensor-state-and-physical-interventions"></a>

### Sensor, State, and Physical Interventions

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Phantom Menace: Exploring and Enhancing the Robustness of VLA Models Against Physical Sensor Attacks](https://arxiv.org/abs/2511.10008)**<br><sub>Lu et al.</sub> | AAAI 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Sensor Spoofing](https://img.shields.io/badge/-Sensor_Spoofing-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks](https://doi.org/10.1145/3733800.3763262)** [![GitHub stars](https://img.shields.io/github/stars/ZJUshine/lamps-vla-robustness.github.io?style=social)](https://github.com/ZJUshine/lamps-vla-robustness.github.io)<br><sub>Lu et al.</sub> | LAMPS@CCS 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +1](https://img.shields.io/badge/-Visual_Perception_%2B1-0F766E?style=flat-square) <br> ![Sensor Spoofing](https://img.shields.io/badge/-Sensor_Spoofing-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="inference-attacks-jailbreaks-and-prompt-injection"></a>

### Jailbreaks and Prompt Injection

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[CHAI: Command Hijacking Against Embodied AI](https://arxiv.org/abs/2510.00181)** [![GitHub stars](https://img.shields.io/github/stars/Cyphysecurity/chai?style=social)](https://github.com/Cyphysecurity/chai)<br><sub>Burbano et al.</sub> | SaTML 2026 | ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Physical Semantic Environment](https://img.shields.io/badge/-Physical_Semantic_Environment-0F766E?style=flat-square) <br> ![Indirect Prompt Injection +2](https://img.shields.io/badge/-Indirect_Prompt_Injection_%2B2-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Control Hijacking](https://img.shields.io/badge/-Control_Hijacking-B91C1C?style=flat-square) |
| **[If You're Waiting for a Sign... That Might Not Be It! Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems](https://arxiv.org/abs/2604.19844)**<br><sub>Chang et al.</sub> | arXiv 2026 | ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Physical Semantic Environment](https://img.shields.io/badge/-Physical_Semantic_Environment-0F766E?style=flat-square) <br> ![Indirect Prompt Injection +1](https://img.shields.io/badge/-Indirect_Prompt_Injection_%2B1-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Control Hijacking](https://img.shields.io/badge/-Control_Hijacking-B91C1C?style=flat-square) |
| **[Adversarial Attacks on Robotic Vision-Language-Action Models](https://arxiv.org/abs/2506.03350)** [![GitHub stars](https://img.shields.io/github/stars/eliotjones1/robogcg?style=social)](https://github.com/eliotjones1/robogcg)<br><sub>Jones et al.</sub> | arXiv 2025 | ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction](https://img.shields.io/badge/-User_Instruction-0F766E?style=flat-square) <br> ![Jailbreak +1](https://img.shields.io/badge/-Jailbreak_%2B1-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |
| **[BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://arxiv.org/abs/2407.20242)** [![GitHub stars](https://img.shields.io/github/stars/Rookie143/BadRobot?style=social)](https://github.com/Rookie143/BadRobot)<br><sub>Zhang et al.</sub> | ICLR 2025 | ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Audio Perception +1](https://img.shields.io/badge/-Audio_Perception_%2B1-0F766E?style=flat-square) <br> ![Jailbreak](https://img.shields.io/badge/-Jailbreak-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |
| **[Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691)** [![GitHub stars](https://img.shields.io/github/stars/arobey1/robopair?style=social)](https://github.com/arobey1/robopair)<br><sub>Robey et al.</sub> | ICRA 2025 | ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction](https://img.shields.io/badge/-User_Instruction-0F766E?style=flat-square) <br> ![Jailbreak](https://img.shields.io/badge/-Jailbreak-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |
| **[POEX: Towards Policy Executable Jailbreak Attacks Against the LLM-Based Robots](https://arxiv.org/abs/2412.16633)** [Project / Code](https://poex-jailbreak.github.io/)<br><sub>Lu et al.</sub> | arXiv 2025 | ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction](https://img.shields.io/badge/-User_Instruction-0F766E?style=flat-square) <br> ![Jailbreak](https://img.shields.io/badge/-Jailbreak-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |
| **[The Shawshank Redemption of Embodied AI: Understanding and Benchmarking Indirect Environmental Jailbreaks](https://arxiv.org/abs/2511.16347)** [Project / Code](https://shawshankiej.github.io/)<br><sub>Li et al.</sub> | arXiv 2025 | ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Physical Semantic Environment](https://img.shields.io/badge/-Physical_Semantic_Environment-0F766E?style=flat-square) <br> ![Indirect Prompt Injection +1](https://img.shields.io/badge/-Indirect_Prompt_Injection_%2B1-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |

<a id="inference-attacks-upstream-vlm-attacks"></a>

### Upstream VLM Attacks

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Chain of Attack: On the Robustness of Vision-Language Models Against Transfer-Based Adversarial Attacks](https://arxiv.org/abs/2411.15720)** [![GitHub stars](https://img.shields.io/github/stars/Shelton1013/Chain_of_Attack?style=social)](https://github.com/Shelton1013/Chain_of_Attack)<br><sub>Xie et al.</sub> | CVPR 2025 | ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Digital Perturbation](https://img.shields.io/badge/-Digital_Perturbation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Perception Model](https://img.shields.io/badge/-Perception_Model-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Control Hijacking](https://img.shields.io/badge/-Control_Hijacking-B91C1C?style=flat-square) |

<a id="defenses"></a>

## 🛡️ Defenses and Safety Mechanisms

<a id="defenses-robust-training-and-safety-alignment"></a>

### Robust Training and Safety Alignment

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[SafeVLA: Towards Safety Alignment of Vision-Language-Action Models via Constrained Learning](https://arxiv.org/abs/2503.03480)** [![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/SafeVLA?style=social)](https://github.com/PKU-Alignment/SafeVLA)<br><sub>Zhang et al.</sub> | NeurIPS 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +1](https://img.shields.io/badge/-User_Instruction_%2B1-0F766E?style=flat-square) <br> ![Constraint Violation](https://img.shields.io/badge/-Constraint_Violation-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Safety Optimized Reinforcement Learning via Multi-Objective Policy Optimization](https://arxiv.org/abs/2402.15197)**<br><sub>Honari et al.</sub> | arXiv 2024 | ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![World State +2](https://img.shields.io/badge/-World_State_%2B2-0F766E?style=flat-square) <br> ![Constraint Violation](https://img.shields.io/badge/-Constraint_Violation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Unsafe Motion](https://img.shields.io/badge/-Unsafe_Motion-B91C1C?style=flat-square) |

<a id="defenses-runtime-monitoring-and-guardrails"></a>

### Runtime Monitoring and Guardrails

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Causal Scene Narration with Runtime Safety Supervision for Vision-Language-Action Driving](https://arxiv.org/abs/2604.01723)**<br><sub>Li et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Planning Error](https://img.shields.io/badge/-Planning_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[RC-NF: Robot-Conditioned Normalizing Flow for Real-Time Anomaly Detection in Robotic Manipulation](https://arxiv.org/abs/2603.11106)**<br><sub>Zhou et al.</sub> | arXiv 2026 | — | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Proprioception +1](https://img.shields.io/badge/-Proprioception_%2B1-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Recovery Failure](https://img.shields.io/badge/-Recovery_Failure-B91C1C?style=flat-square) |
| **[Safety Guardrails for LLM-Enabled Robots](https://arxiv.org/abs/2503.07885)**<br><sub>Ravichandran et al.</sub> | IEEE RA-L 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +1](https://img.shields.io/badge/-User_Instruction_%2B1-0F766E?style=flat-square) <br> ![Jailbreak](https://img.shields.io/badge/-Jailbreak-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |
| **[From Words to Safety: Language-Conditioned Safety Filtering for Robot Navigation](https://arxiv.org/abs/2511.05889)**<br><sub>Feng et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +1](https://img.shields.io/badge/-User_Instruction_%2B1-0F766E?style=flat-square) <br> ![Constraint Violation](https://img.shields.io/badge/-Constraint_Violation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[ROVER: Regulator-Driven Robust Temporal Verification of Black-Box Robot Policies](https://arxiv.org/abs/2511.17781)**<br><sub>Sakano et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Action Interface +1](https://img.shields.io/badge/-Action_Interface_%2B1-0F766E?style=flat-square) <br> ![Unsafe Policy Behavior](https://img.shields.io/badge/-Unsafe_Policy_Behavior-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[VLSA: Vision-Language-Action Models with a Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)** [![GitHub stars](https://img.shields.io/github/stars/THU-RCSCT/vlsa-aegis?style=social)](https://github.com/THU-RCSCT/vlsa-aegis)<br><sub>Hu et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +1](https://img.shields.io/badge/-User_Instruction_%2B1-0F766E?style=flat-square) <br> ![Constraint Violation](https://img.shields.io/badge/-Constraint_Violation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="defenses-action-shielding-fail-safes-and-recovery"></a>

### Action Shielding, Fail-Safes, and Recovery

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation](https://arxiv.org/abs/2601.15541)** [Project / Code](https://sites.google.com/view/compliantvla)<br><sub>Zhang et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Proprioception +1](https://img.shields.io/badge/-Proprioception_%2B1-0F766E?style=flat-square) <br> ![Constraint Violation](https://img.shields.io/badge/-Constraint_Violation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[VLA Knows Its Limits: Adaptive Execution Horizons for Robot Policies](https://arxiv.org/abs/2602.21445)** [Project / Code](https://hatchetproject.github.io/autohorizon/)<br><sub>Wang et al.</sub> | ECCV 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic](https://arxiv.org/abs/2512.21220)**<br><sub>Wang et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +2](https://img.shields.io/badge/-User_Instruction_%2B2-0F766E?style=flat-square) <br> ![Hazardous Instruction](https://img.shields.io/badge/-Hazardous_Instruction-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |
| **[SAFE: Multitask Failure Detection for Vision-Language-Action Models](https://arxiv.org/abs/2506.09937)** [![GitHub stars](https://img.shields.io/github/stars/vla-safe/SAFE?style=social)](https://github.com/vla-safe/SAFE)<br><sub>Gu et al.</sub> | NeurIPS 2025 | — | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +1](https://img.shields.io/badge/-Visual_Perception_%2B1-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Recovery Failure](https://img.shields.io/badge/-Recovery_Failure-B91C1C?style=flat-square) |
| **[Semantically Safe Robot Manipulation: From Semantic Scene Understanding to Motion Safeguards](https://arxiv.org/abs/2410.15185)** [Project / Code](https://utiasdsl.github.io/semantic-manipulation/)<br><sub>Brunke et al.</sub> | ICRA 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +3](https://img.shields.io/badge/-Visual_Perception_%2B3-0F766E?style=flat-square) <br> ![Semantic Misalignment](https://img.shields.io/badge/-Semantic_Misalignment-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Collision](https://img.shields.io/badge/-Collision-B91C1C?style=flat-square) |
| **[Towards Safe Robot Foundation Models Using Inductive Biases](https://arxiv.org/abs/2505.10219)** [Project / Code](https://sites.google.com/view/safe-robot-foundation-models)<br><sub>Tölle et al.</sub> | arXiv 2025 | ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Action Interface +1](https://img.shields.io/badge/-Action_Interface_%2B1-0F766E?style=flat-square) <br> ![Constraint Violation](https://img.shields.io/badge/-Constraint_Violation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Collision](https://img.shields.io/badge/-Collision-B91C1C?style=flat-square) |
| **[Plug in the Safety Chip: Enforcing Constraints for LLM-Driven Robot Agents](https://arxiv.org/abs/2309.09919)**<br><sub>Yang et al.</sub> | arXiv 2023 | ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Task Planning +1](https://img.shields.io/badge/-Task_Planning_%2B1-0F766E?style=flat-square) <br> ![Planning Error](https://img.shields.io/badge/-Planning_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Unsafe Motion](https://img.shields.io/badge/-Unsafe_Motion-B91C1C?style=flat-square) |
| **[REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://proceedings.mlr.press/v229/liu23g.html)** [![GitHub stars](https://img.shields.io/github/stars/real-stanford/reflect?style=social)](https://github.com/real-stanford/reflect)<br><sub>Liu et al.</sub> | CoRL 2023 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments](https://arxiv.org/abs/2311.02817)**<br><sub>Yue et al.</sub> | arXiv 2023 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![World State +2](https://img.shields.io/badge/-World_State_%2B2-0F766E?style=flat-square) <br> ![Constraint Violation](https://img.shields.io/badge/-Constraint_Violation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Collision](https://img.shields.io/badge/-Collision-B91C1C?style=flat-square) |

<a id="defenses-representation-steering-and-inference-time-defense"></a>

### Representation Steering and Inference-Time Defense

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration](https://arxiv.org/abs/2603.06001)**<br><sub>Zhang et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +1](https://img.shields.io/badge/-User_Instruction_%2B1-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors](https://arxiv.org/abs/2607.12571)**<br><sub>Fu et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Model Supply Chain +1](https://img.shields.io/badge/-Model_Supply_Chain_%2B1-0F766E?style=flat-square) <br> ![Backdoor](https://img.shields.io/badge/-Backdoor-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Targeted Action](https://img.shields.io/badge/-Targeted_Action-B91C1C?style=flat-square) |
| **[Concept Enhancement Engineering: A Lightweight and Efficient Robust Defense Against Jailbreak Attacks in Embodied AI](https://arxiv.org/abs/2504.13201)**<br><sub>Yang et al.</sub> | arXiv 2025 | ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +1](https://img.shields.io/badge/-User_Instruction_%2B1-0F766E?style=flat-square) <br> ![Jailbreak](https://img.shields.io/badge/-Jailbreak-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |

<a id="defenses-system-and-communication-defenses"></a>

### System and Communication Defenses

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[AgentSafe: Safeguarding Large Language Model-Based Multi-Agent Systems via Hierarchical Data Management](https://arxiv.org/abs/2503.04392)**<br><sub>Mao et al.</sub> | arXiv 2025 | ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![System → Inference](https://img.shields.io/badge/-System_%E2%86%92_Inference-2563EB?style=flat-square) ![Context Memory Retrieval +1](https://img.shields.io/badge/-Context_Memory_Retrieval_%2B1-0F766E?style=flat-square) <br> ![Memory Poisoning +1](https://img.shields.io/badge/-Memory_Poisoning_%2B1-C2410C?style=flat-square) &nbsp;→&nbsp; ![Shared System State](https://img.shields.io/badge/-Shared_System_State-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Control Hijacking](https://img.shields.io/badge/-Control_Hijacking-B91C1C?style=flat-square) |

<a id="defenses-active-perception-and-recovery"></a>

### Active Perception and Recovery

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation](https://arxiv.org/abs/2512.07472)**<br><sub>Xu et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +1](https://img.shields.io/badge/-Visual_Perception_%2B1-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models](https://arxiv.org/abs/2510.01642)**<br><sub>Lin et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Embodied Active Defense: Leveraging Recurrent Feedback to Counter Adversarial Patches](https://arxiv.org/abs/2404.00540)**<br><sub>Wu et al.</sub> | ICLR 2024 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Adversarial Patch](https://img.shields.io/badge/-Adversarial_Patch-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="defenses-multimodal-perception-and-physical-safeguards"></a>

### Multimodal Perception and Physical Safeguards

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[DroneVLA: VLA based Aerial Manipulation](https://arxiv.org/abs/2601.13809)**<br><sub>Mehboob et al.</sub> | arXiv 2026 | — | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Constraint Violation](https://img.shields.io/badge/-Constraint_Violation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation](https://arxiv.org/abs/2603.05754)** [Project / Code](https://thisanwerss.github.io/Safe-Night-VLA/)<br><sub>Yu et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="defenses-human-in-the-loop-safety-refinement"></a>

### Human-in-the-Loop Safety Refinement

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Human-assisted Robotic Policy Refinement via Action Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/347110fb894281e5e937f6ccd998a6eb-Abstract-Conference.html)** [![GitHub stars](https://img.shields.io/github/stars/GeWu-Lab/Action-Preference-Optimization?style=social)](https://github.com/GeWu-Lab/Action-Preference-Optimization)<br><sub>Xia et al.</sub> | NeurIPS 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Action Interface](https://img.shields.io/badge/-Action_Interface-0F766E?style=flat-square) <br> ![Unsafe Policy Behavior](https://img.shields.io/badge/-Unsafe_Policy_Behavior-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Human-in-the-Loop Online Rejection Sampling for Robotic Manipulation](https://arxiv.org/abs/2510.26406)** [Project / Code](https://hiors-project.github.io/)<br><sub>Lu et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Action Interface](https://img.shields.io/badge/-Action_Interface-0F766E?style=flat-square) <br> ![Unsafe Policy Behavior](https://img.shields.io/badge/-Unsafe_Policy_Behavior-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="defenses-runtime-observation-interventions"></a>

### Runtime Observation Interventions

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Run-Time Observation Interventions Make Vision-Language-Action Models More Visually Robust](https://arxiv.org/abs/2410.01971)** [![GitHub stars](https://img.shields.io/github/stars/irom-princeton/byovla?style=social)](https://github.com/irom-princeton/byovla)<br><sub>Hancock et al.</sub> | arXiv 2024 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="defenses-reliability-oriented-policy-refinement"></a>

### Reliability-Oriented Policy Refinement

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[EvoVLA: Self-Evolving Vision-Language-Action Model](https://arxiv.org/abs/2511.16166)** [![GitHub stars](https://img.shields.io/github/stars/AIGeeksGroup/EvoVLA?style=social)](https://github.com/AIGeeksGroup/EvoVLA)<br><sub>Liu et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Task Planning +1](https://img.shields.io/badge/-Task_Planning_%2B1-0F766E?style=flat-square) <br> ![Unsafe Policy Behavior](https://img.shields.io/badge/-Unsafe_Policy_Behavior-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="defenses-model-unlearning-and-data-governance"></a>

### Model Unlearning and Data Governance

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models](https://arxiv.org/abs/2604.03956)**<br><sub>Ranjan et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Model Supply Chain](https://img.shields.io/badge/-Model_Supply_Chain-0F766E?style=flat-square) <br> ![Memorized Data Retention +1](https://img.shields.io/badge/-Memorized_Data_Retention_%2B1-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Privacy Leakage](https://img.shields.io/badge/-Privacy_Leakage-B91C1C?style=flat-square) |

<a id="defenses-safety-aware-policy-learning"></a>

### Safety-Aware Policy Learning

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[VLM-SAFE: Vision-Language Model-Guided Safety-Aware Reinforcement Learning with World Models for Autonomous Driving](https://arxiv.org/abs/2505.16377)** [Project / Code](https://ys-qu.github.io/vlsafe-website/)<br><sub>Qu et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +3](https://img.shields.io/badge/-Visual_Perception_%2B3-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="defenses-privacy-preserving-perception"></a>

### Privacy-Preserving Perception

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Privacy-Preserving Semantic Segmentation from Ultra-Low-Resolution RGB Inputs](https://arxiv.org/abs/2507.16034)** [![GitHub stars](https://img.shields.io/github/stars/hxy-0818/ULR2SS?style=social)](https://github.com/hxy-0818/ULR2SS)<br><sub>Huang et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Sensitive Data Exposure](https://img.shields.io/badge/-Sensitive_Data_Exposure-C2410C?style=flat-square) &nbsp;→&nbsp; ![Private Data](https://img.shields.io/badge/-Private_Data-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Privacy Leakage](https://img.shields.io/badge/-Privacy_Leakage-B91C1C?style=flat-square) |
| **[Real-Time Privacy Preservation for Robot Visual Perception](https://arxiv.org/abs/2505.05519)**<br><sub>Choi et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Sensitive Data Exposure](https://img.shields.io/badge/-Sensitive_Data_Exposure-C2410C?style=flat-square) &nbsp;→&nbsp; ![Private Data](https://img.shields.io/badge/-Private_Data-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Privacy Leakage](https://img.shields.io/badge/-Privacy_Leakage-B91C1C?style=flat-square) |

<a id="defenses-failure-detection-and-recovery"></a>

### Failure Detection and Recovery

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272)** [Project / Code](https://research.nvidia.com/labs/gear/ASPIRE/)<br><sub>Lu et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Context Memory Retrieval +2](https://img.shields.io/badge/-Context_Memory_Retrieval_%2B2-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement](https://arxiv.org/abs/2607.01111)**<br><sub>Hao et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Action Interface +1](https://img.shields.io/badge/-Action_Interface_%2B1-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645)**<br><sub>Zhao et al.</sub> | CVPR 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +3](https://img.shields.io/badge/-Visual_Perception_%2B3-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448)** [![GitHub stars](https://img.shields.io/github/stars/RLinf/RPent?style=social)](https://github.com/RLinf/RPent)<br><sub>Zhang et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +3](https://img.shields.io/badge/-Visual_Perception_%2B3-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Replanning Human-Robot Collaborative Tasks with Vision-Language Models via Semantic and Physical Dual-Correction](https://arxiv.org/abs/2602.14551)**<br><sub>Kato et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +3](https://img.shields.io/badge/-User_Instruction_%2B3-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models](https://arxiv.org/abs/2509.16072)** [Project / Code](https://clemgris.github.io/I-FailSense/)<br><sub>Grislain et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +1](https://img.shields.io/badge/-Visual_Perception_%2B1-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction](https://arxiv.org/abs/2504.14588)** [![GitHub stars](https://img.shields.io/github/stars/GeWu-Lab/Motion-based-Self-Reflection-Framework?style=social)](https://github.com/GeWu-Lab/Motion-based-Self-Reflection-Framework)<br><sub>Xia et al.</sub> | CVPR 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation](https://arxiv.org/abs/2405.17418)**<br><sub>Li et al.</sub> | arXiv 2024 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment](https://arxiv.org/abs/2307.00329)** [Project / Code](https://sites.google.com/view/doremi-paper)<br><sub>Guo et al.</sub> | IROS 2024 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +3](https://img.shields.io/badge/-Visual_Perception_%2B3-0F766E?style=flat-square) <br> ![Execution Error](https://img.shields.io/badge/-Execution_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="defenses-uncertainty-abstention-and-human-oversight"></a>

### Uncertainty, Abstention, and Human Oversight

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue](https://arxiv.org/abs/2509.15061)**<br><sub>Lin et al.</sub> | IROS 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction](https://img.shields.io/badge/-User_Instruction-0F766E?style=flat-square) <br> ![Instruction Ambiguity](https://img.shields.io/badge/-Instruction_Ambiguity-C2410C?style=flat-square) &nbsp;→&nbsp; ![Reasoning Process](https://img.shields.io/badge/-Reasoning_Process-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Do What? Teaching Vision-Language-Action Models to Reject the Impossible](https://arxiv.org/abs/2508.16292)**<br><sub>Hsieh et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction](https://img.shields.io/badge/-User_Instruction-0F766E?style=flat-square) <br> ![Planning Error](https://img.shields.io/badge/-Planning_Error-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](https://arxiv.org/abs/2307.01928)** [Project / Code](https://robot-help.github.io/)<br><sub>Ren et al.</sub> | CoRL 2023 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +2](https://img.shields.io/badge/-User_Instruction_%2B2-0F766E?style=flat-square) <br> ![Instruction Ambiguity](https://img.shields.io/badge/-Instruction_Ambiguity-C2410C?style=flat-square) &nbsp;→&nbsp; ![Reasoning Process](https://img.shields.io/badge/-Reasoning_Process-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="benchmarks"></a>

## 📊 Benchmarks and Evaluation

<a id="benchmarks-ood-and-generalization-benchmarks"></a>

### OOD and Generalization Benchmarks

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models](https://arxiv.org/abs/2603.28301)** [![GitHub stars](https://img.shields.io/github/stars/cau-hai-lab/LIBERO-Para?style=social)](https://github.com/cau-hai-lab/LIBERO-Para)<br><sub>Kim et al.</sub> | EMNLP 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html)** [![GitHub stars](https://img.shields.io/github/stars/sylvestf/LIBERO-plus?style=social)](https://github.com/sylvestf/LIBERO-plus)<br><sub>Fei et al.</sub> | CVPR 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +3](https://img.shields.io/badge/-Visual_Perception_%2B3-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](https://arxiv.org/abs/2510.03827)** [![GitHub stars](https://img.shields.io/github/stars/Zxy-MLlab/LIBERO-PRO?style=social)](https://github.com/Zxy-MLlab/LIBERO-PRO)<br><sub>Zhou et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +1](https://img.shields.io/badge/-Visual_Perception_%2B1-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="benchmarks-comprehensive-vla-evaluation"></a>

### Comprehensive VLA Evaluation

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](https://arxiv.org/abs/2512.22539)** [![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/VLA-Arena?style=social)](https://github.com/PKU-Alignment/VLA-Arena)<br><sub>Zhang et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |
| **[VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://arxiv.org/abs/2412.18194)** [![GitHub stars](https://img.shields.io/github/stars/OpenMOSS/VLABench?style=social)](https://github.com/OpenMOSS/VLABench)<br><sub>Zhang et al.</sub> | arXiv 2024 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |

<a id="benchmarks-adversarial-and-physical-robustness"></a>

### Adversarial and Physical Robustness

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[RedVLA: Physical Red Teaming for Vision-Language-Action Models](https://arxiv.org/abs/2604.22591)** [Project / Code](https://redvla.github.io/)<br><sub>Zhang et al.</sub> | arXiv 2026 | ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Physical Semantic Environment +1](https://img.shields.io/badge/-Physical_Semantic_Environment_%2B1-0F766E?style=flat-square) <br> ![Adversarial Object +1](https://img.shields.io/badge/-Adversarial_Object_%2B1-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Control Hijacking](https://img.shields.io/badge/-Control_Hijacking-B91C1C?style=flat-square) |
| **[VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness](https://openreview.net/forum?id=31EjDFwFEe)**<br><sub>Ru et al.</sub> | OpenReview 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |
| **[AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.12149)**<br><sub>Li et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Training → Inference](https://img.shields.io/badge/-Training_%E2%86%92_Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |
| **[Manipulation Facing Threats: Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models](https://arxiv.org/abs/2409.13174)** [Project / Code](https://chaducheng.github.io/Manipulate-Facing-Threats/)<br><sub>Cheng et al.</sub> | arXiv 2024 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception + Physical Semantic Environment](https://img.shields.io/badge/-Visual_Perception_%2B_Physical_Semantic_Environment-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |

<a id="benchmarks-task-and-physical-safety"></a>

### Task and Physical Safety

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2606.27079)**<br><sub>Lyu et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |
| **[IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks](https://arxiv.org/abs/2506.16402)**<br><sub>Lu et al.</sub> | AAAI 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +2](https://img.shields.io/badge/-User_Instruction_%2B2-0F766E?style=flat-square) <br> ![Constraint Violation](https://img.shields.io/badge/-Constraint_Violation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686)** [![GitHub stars](https://img.shields.io/github/stars/LIBERO-SAFETY/LIBERO-Safety?style=social)](https://github.com/LIBERO-SAFETY/LIBERO-Safety)<br><sub>Cui et al.</sub> | ECCV 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |
| **[SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.00773)** [Project / Code](https://safevla.org/)<br><sub>Fan et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |
| **[A Framework for Benchmarking and Aligning Task-Planning Safety in LLM-Based Embodied Agents](https://arxiv.org/abs/2504.14650)**<br><sub>Huang et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction + Task Planning](https://img.shields.io/badge/-User_Instruction_%2B_Task_Planning-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |
| **[CostNav: A Navigation Benchmark for Real-World Economic-Cost Evaluation of Physical AI Agents](https://arxiv.org/abs/2511.20216)** [![GitHub stars](https://img.shields.io/github/stars/worv-ai/CostNav?style=social)](https://github.com/worv-ai/CostNav)<br><sub>Seong et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Multiple surfaces](https://img.shields.io/badge/-Multiple_surfaces-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |
| **[SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)** [![GitHub stars](https://img.shields.io/github/stars/shengyin1224/SafeAgentBench?style=social)](https://github.com/shengyin1224/SafeAgentBench)<br><sub>Yin et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction](https://img.shields.io/badge/-User_Instruction-0F766E?style=flat-square) <br> ![Hazardous Instruction](https://img.shields.io/badge/-Hazardous_Instruction-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |
| **[EARBench: Towards Evaluating Physical Risk Awareness for Task Planning of Foundation Model-Based Embodied AI Agents](https://arxiv.org/abs/2408.04449)**<br><sub>Zhu et al.</sub> | arXiv 2024 | ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Constraint Violation](https://img.shields.io/badge/-Constraint_Violation-C2410C?style=flat-square) &nbsp;→&nbsp; ![Action Generation](https://img.shields.io/badge/-Action_Generation-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Unsafe Motion](https://img.shields.io/badge/-Unsafe_Motion-B91C1C?style=flat-square) |

<a id="benchmarks-semantic-and-ethical-safety"></a>

### Semantic and Ethical Safety

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Generating Robot Constitutions and Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663)** [![GitHub stars](https://img.shields.io/github/stars/asimov-benchmark/asimov-benchmark.github.io?style=social)](https://github.com/asimov-benchmark/asimov-benchmark.github.io)<br><sub>Sermanet et al.</sub> | arXiv 2025 | ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +1](https://img.shields.io/badge/-User_Instruction_%2B1-0F766E?style=flat-square) <br> ![Semantic Misalignment](https://img.shields.io/badge/-Semantic_Misalignment-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |

<a id="benchmarks-evaluation-infrastructure"></a>

### Evaluation Infrastructure

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941)** [![GitHub stars](https://img.shields.io/github/stars/simpler-env/SimplerEnv?style=social)](https://github.com/simpler-env/SimplerEnv)<br><sub>Li et al.</sub> | CoRL 2024 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)** [![GitHub stars](https://img.shields.io/github/stars/Lifelong-Robot-Learning/LIBERO?style=social)](https://github.com/Lifelong-Robot-Learning/LIBERO)<br><sub>Liu et al.</sub> | NeurIPS Datasets and Benchmarks 2023 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Distribution Shift](https://img.shields.io/badge/-Distribution_Shift-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |

<a id="benchmarks-safety-and-hazard-benchmarks"></a>

### Safety and Hazard Benchmarks

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2604.12447)**<br><sub>Chen et al.</sub> | arXiv 2026 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) ![Physical](https://img.shields.io/badge/-Physical-B91C1C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction +1](https://img.shields.io/badge/-User_Instruction_%2B1-0F766E?style=flat-square) <br> ![Semantic Misalignment](https://img.shields.io/badge/-Semantic_Misalignment-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |
| **[AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697)**<br><sub>Ying et al.</sub> | arXiv 2025 | ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction](https://img.shields.io/badge/-User_Instruction-0F766E?style=flat-square) <br> ![Hazardous Instruction](https://img.shields.io/badge/-Hazardous_Instruction-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |
| **[SafeMind: Benchmarking and Mitigating Safety Risks in Embodied LLM Agents](https://arxiv.org/abs/2509.25885)**<br><sub>Chen et al.</sub> | arXiv 2025 | ![Ethics](https://img.shields.io/badge/-Ethics-7E22CE?style=flat-square) ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![User Instruction](https://img.shields.io/badge/-User_Instruction-0F766E?style=flat-square) <br> ![Jailbreak](https://img.shields.io/badge/-Jailbreak-C2410C?style=flat-square) &nbsp;→&nbsp; ![Task Planner](https://img.shields.io/badge/-Task_Planner-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |

<a id="benchmarks-robustness-and-uncertainty-evaluation"></a>

### Robustness and Uncertainty Evaluation

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Confidence Calibration in Vision-Language-Action Models](https://arxiv.org/abs/2507.17383)**<br><sub>Zollo et al.</sub> | arXiv 2025 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Reasoning Representation +1](https://img.shields.io/badge/-Reasoning_Representation_%2B1-0F766E?style=flat-square) <br> ![Uncertainty Miscalibration](https://img.shields.io/badge/-Uncertainty_Miscalibration-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Task Failure](https://img.shields.io/badge/-Task_Failure-B91C1C?style=flat-square) |
| **[Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots](https://arxiv.org/abs/2507.17049)**<br><sub>Valle et al.</sub> | arXiv 2025 | — | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception +2](https://img.shields.io/badge/-Visual_Perception_%2B2-0F766E?style=flat-square) <br> ![Uncertainty Miscalibration](https://img.shields.io/badge/-Uncertainty_Miscalibration-C2410C?style=flat-square) &nbsp;→&nbsp; ![VLA policy](https://img.shields.io/badge/-VLA_policy-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Recovery Failure](https://img.shields.io/badge/-Recovery_Failure-B91C1C?style=flat-square) |
| **[VLATest: Testing and Evaluating Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2409.12894)**<br><sub>Wang et al.</sub> | arXiv 2024 | ![Task](https://img.shields.io/badge/-Task-2563EB?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception + User Instruction](https://img.shields.io/badge/-Visual_Perception_%2B_User_Instruction-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |

<a id="benchmarks-safety-critical-perception-evaluation"></a>

### Safety-Critical Perception Evaluation

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Can Vision-Language Models Understand Construction Workers? An Exploratory Study](https://arxiv.org/abs/2601.10835)**<br><sub>Bui et al.</sub> | arXiv 2026 | — | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |
| **[Privacy Risks of Robot Vision: A User Study on Image Modalities and Resolution](https://arxiv.org/abs/2505.07766)**<br><sub>Huang et al.</sub> | arXiv 2025 | ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![Inference](https://img.shields.io/badge/-Inference-2563EB?style=flat-square) ![Visual Perception](https://img.shields.io/badge/-Visual_Perception-0F766E?style=flat-square) <br> ![Evaluation coverage](https://img.shields.io/badge/-Evaluation_coverage-0369A1?style=flat-square) |

<a id="system-security"></a>

## 🔐 System-Level Security, Privacy, and Misuse

<a id="system-security-cross-layer-system-security"></a>

### Cross-Layer System Security

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Beyond Model Jailbreak: Systematic Dissection of the Ten Deadly Sins in Embodied Intelligence](https://arxiv.org/abs/2512.06387)**<br><sub>Huang et al.</sub> | arXiv 2025 | ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![System → Inference](https://img.shields.io/badge/-System_%E2%86%92_Inference-2563EB?style=flat-square) ![Model Supply Chain +2](https://img.shields.io/badge/-Model_Supply_Chain_%2B2-0F766E?style=flat-square) <br> ![Middleware Compromise +2](https://img.shields.io/badge/-Middleware_Compromise_%2B2-C2410C?style=flat-square) &nbsp;→&nbsp; ![Shared System State](https://img.shields.io/badge/-Shared_System_State-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Policy Violation](https://img.shields.io/badge/-Policy_Violation-B91C1C?style=flat-square) |

<a id="system-security-privacy-misuse-and-covert-channels"></a>

### Privacy, Misuse, and Covert Channels

| Paper | Venue | Evaluated Risk | Threat Model |
|---|---:|---|---|
| **[Cyber-Physical Steganography in Robotic Motion Control](https://arxiv.org/abs/2501.04541)**<br><sub>Chang et al.</sub> | IEICE Transactions 2026 | ![Security/Privacy](https://img.shields.io/badge/-Security%2FPrivacy-C2410C?style=flat-square) | ![System → Inference](https://img.shields.io/badge/-System_%E2%86%92_Inference-2563EB?style=flat-square) ![Action Interface +1](https://img.shields.io/badge/-Action_Interface_%2B1-0F766E?style=flat-square) <br> ![Covert Channel +1](https://img.shields.io/badge/-Covert_Channel_%2B1-C2410C?style=flat-square) &nbsp;→&nbsp; ![Robot Executor](https://img.shields.io/badge/-Robot_Executor-7E22CE?style=flat-square) &nbsp;→&nbsp; ![Privacy Leakage](https://img.shields.io/badge/-Privacy_Leakage-B91C1C?style=flat-square) |

## Scope and Curation Policy

The core scope is VLA safety, robustness, security, and evaluation. Closely related LLM-robot, VLM-driven embodied-agent, autonomous-driving, and robot-policy papers are included when they expose a risk, mechanism, defense, or evaluation principle that transfers directly to VLA systems.

A paper is listed once under its primary contribution. Risk outcomes and mechanisms are represented as multi-label metadata rather than by duplicating the paper across sections.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and add or update the corresponding record in `data/papers.json`. Do not edit generated paper tables directly.

## License

MIT License. Paper titles, author names, venues, and links remain the property of their respective authors and publishers.
