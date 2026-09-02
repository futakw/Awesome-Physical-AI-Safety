# Taxonomy and Curation Policy

This repository uses a multi-axis taxonomy. A paper's primary section describes its main research contribution; independent metadata describes the outcomes at risk, the failure source, the mechanism, and the evaluation regime.

## 1. Risk Outcomes

Risk outcomes are multi-label because a system may complete a task while remaining unsafe, unethical, or compromised.

### Task and Reliability Risk

Task failure, degraded success, wrong-object or wrong-subtask execution, trajectory deviation, dangerous inaction, recovery failure, and uncertainty or calibration failure.

### Physical Safety Risk

Collision, human injury, object or environment damage, unsafe force or motion, safety-constraint violation, and failure to mitigate an emerging hazard.

### Ethical and Societal Risk

Execution of harmful or prohibited instructions, inappropriate use, deceptive behavior, insufficient human oversight, and socially harmful embodied behavior.

### Security and Privacy Risk

Unauthorized control, backdoor persistence, information leakage, covert communication, compromised memory or agent communication, and cloud, network, firmware, or application compromise.

## 2. Failure Sources

### Adversarial or Malicious

An attacker intentionally manipulates inputs, training data, model states, actions, the environment, or system components.

### Non-Adversarial or OOD

The system fails under unseen viewpoints, visual appearances, objects, geometries, language, tasks, environments, embodiments, or temporal dynamics without assuming an attacker.

### Design, Training, or System Failure

The failure arises from objective misspecification, multimodal misalignment, reward hacking, sensor faults, planner-executor mismatch, or insufficient runtime recovery.

## 3. Threat Mechanisms

Each catalog record includes a concise `threat_model` field. It identifies whether the paper assumes a malicious adversary, a non-adversarial distribution shift, a design/system failure, or an evaluation scope spanning several threat families. Defense papers describe the threat being mitigated, rather than merely naming the defense mechanism.

### Visual and Physical Input Attacks

- Digital perturbations
- Localized adversarial patches, including printed patches
- Adversarial objects, textures, signs, and scene interventions
- Typographic attacks and visual prompt injection
- Lighting, occlusion, geometry, and placement manipulation

### Language and Instruction Attacks

- Jailbreaks
- Direct and indirect prompt injection
- Command hijacking
- Malicious or ambiguous instructions
- Policy-executability-aware attacks

### Sensor and State Attacks

- Camera, microphone, and proprioception corruption
- State manipulation
- Temporal sensor attacks
- Multimodal desynchronization

### Training-Time Attacks

- Data poisoning
- Input-, action-, and state-level backdoors
- Reward manipulation
- Fine-tuning and supply-chain compromise

### Representation, Planning, and Action Attacks

- Multimodal alignment corruption
- Subtask and future-plan hijacking
- Action freezing and action-chunk manipulation
- Trajectory manipulation

### System-Level Attacks

- Memory and inter-agent communication attacks
- Cloud, API, wireless, network, firmware, and application compromise
- Covert channels and privacy leakage

## 4. OOD Generalization Axes

OOD generalization is a first-class section rather than a subtype of attack.

- **Visual appearance:** texture, color, lighting, and background
- **Viewpoint and camera:** camera pose, camera type, ordering, or missing views
- **Object geometry and spatial layout:** shape, size, articulation, and placement
- **Language and instruction:** paraphrase, ambiguity, and unseen composition
- **Task compositionality:** unseen tasks, long horizons, and subtask combinations
- **Environment and domain:** new rooms, clutter, dynamics, and sim-to-real transfer
- **Embodiment:** robot morphology, action space, and control frequency
- **Temporal dynamics:** latency, asynchronous observations, and moving objects

## 5. Evaluation Levels

- Perception and semantic correctness
- Instruction-vision-action consistency
- Action prediction quality
- Trajectory deviation and constraint violation
- Task success and unsafe success
- Physical harm, near miss, and hazardous-instruction refusal
- Interactive mitigation and recovery
- Uncertainty and calibration
- Real-robot validation

## Inclusion Criteria

Include a paper when at least one of the following holds:

1. It directly studies safety, robustness, security, privacy, misuse, or trustworthy evaluation of a VLA model.
2. It studies an embodied-agent or robot-policy failure that transfers directly to VLA perception-decision-action loops.
3. It introduces an OOD or evaluation protocol that exposes a Responsible VLA failure mode.
4. It proposes a defense, runtime monitor, guardrail, action shield, fail-safe, or recovery mechanism relevant to VLA deployment.

Generic VLM, LLM, robotics, or capability papers should not be included unless their connection to VLA risk is explicit.

## Classification Rule

List each paper once under its primary contribution. Use `risks` and `tags` for cross-cutting properties instead of duplicating the paper across sections.
