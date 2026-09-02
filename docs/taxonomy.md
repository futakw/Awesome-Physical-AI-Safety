# Taxonomy and Curation Policy

This repository uses a multi-axis taxonomy. A paper's primary section describes its main research contribution; independent metadata describes the outcomes at risk, the failure source, the mechanism, and the evaluation regime.

## 1. Empirically Evaluated Risk Outcomes

The `risks` field is evidence-coded, not a list of plausible consequences. A label is assigned only when the paper's experiments report a metric for that outcome. A survey that discusses all four risks therefore has an empty list, while an attack paper may receive both `Task Success` and `Security & Privacy` when it reports task success and attack success rate. Physical deployment alone does not justify a `Physical Safety` label.

### Task and Reliability Risk

Task or route completion, success rate, or an equivalent end-to-end execution outcome. Action deviation, detection accuracy, calibration error, and attack success alone do not qualify.

### Physical Safety Risk

Collision, human injury, object or environment damage, unsafe force or motion, physical-harm execution, safety-constraint violation, or an explicit physical-risk proxy.

### Ethical and Societal Risk

Compliance or refusal under harmful or prohibited instructions, policy or constitution violations, and explicitly measured harmful embodied behavior.

### Security and Privacy Risk

Attack success, backdoor activation, unauthorized control, command hijacking, information leakage, covert communication, compromised memory or communication, and system compromise.

### Assignment Rule

1. Identify the metrics actually reported in experiments.
2. Map only those metrics to the four outcomes above.
3. Do not assign a label from the title, motivation, deployment setting, or a hypothetical downstream consequence.
4. Use an empty `risks` list when no reported metric maps to these outcomes; the README displays `—`.

## 2. Failure Sources

### Adversarial or Malicious

An attacker intentionally manipulates inputs, training data, model states, actions, the environment, or system components.

### Non-Adversarial or OOD

The system fails under unseen viewpoints, visual appearances, objects, geometries, language, tasks, environments, embodiments, or temporal dynamics without assuming an attacker.

### Design, Training, or System Failure

The failure arises from objective misspecification, multimodal misalignment, reward hacking, sensor faults, planner-executor mismatch, or insufficient runtime recovery.

## 3. Threat Mechanisms

Each catalog record uses the compact notation `Category (primary mechanism or shift)`. The parenthetical detail is omitted when the category is already specific. Defense papers describe the threat being mitigated, not the defense method; experimental settings such as real-robot evaluation belong in `tags`.

### Controlled Threat Categories

| Family | Allowed categories |
|---|---|
| Adversarial | `Training-time attack`, `Inference-time attack`, `System-level attack` |
| Non-adversarial failure | `Non-adversarial OOD`, `Execution failure`, `Planning failure`, `Policy failure`, `Uncertainty failure` |
| Unsafe intent or outcome | `Hazardous instruction`, `Physical safety violation`, `Semantic safety violation`, `System-level misuse` |
| Broad coverage | `Survey scope`, `Evaluation scope` |

Use only the primary discriminating detail. For example, a poisoned training set that installs a backdoor is `Training-time attack (backdoor)`, not `Training-time attack (backdoor, training data)`. Multiple OOD axes may be grouped as `Non-adversarial OOD (viewpoint, language, object geometry)`.

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
