# Taxonomy and Curation Policy

**English (this page)** | [Japanese](taxonomy.ja.md)

This repository uses a multi-axis taxonomy. A paper's primary section describes its main research contribution; independent metadata describes the outcomes at risk, the failure source, the mechanism, and the evaluation regime.

## 1. Empirically Evaluated Risk Outcomes

The `risks` field is evidence-coded, not a list of plausible consequences. A label is assigned only when the paper's experiments report a metric for that outcome. A survey that discusses all four risks therefore has an empty list, while an attack paper may receive both `Task Success` and `Security & Privacy` when it reports task success and attack success rate. Physical deployment alone does not justify a `Physical Safety` label.

### Task and Reliability Risk

Task or route completion, success rate, or an equivalent end-to-end execution outcome. Action deviation, detection accuracy, calibration error, and attack success alone do not qualify.

### Physical Safety Risk

Collision, human injury, object or environment damage, unsafe force or motion, physical-harm execution, safety-constraint violation, or an explicit physical-risk proxy.

### Ethical and Societal Risk

Compliance or refusal under harmful or prohibited instructions, policy or constitution violations, explicitly measured harmful embodied behavior, or measured disparities across people or groups in access, task success, assistance quality, or exposure to hazards. A fairness motivation, a model's inductive bias, or a benchmark's "fair evaluation" of models does not qualify without a corresponding societal-outcome metric.

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

## 3. Structured Threat Model

> **Status: Adopted.** All catalog records and the README generator use this schema.

The `threat_model` field should be a structured object rather than a compact free-text string. It separates when a threat occurs, how it operates, which system boundary or boundaries it uses, what it targets, and what consequence it produces.

### Core Fields

| Field | Type | Required for a concrete study | Meaning | Example |
|---|---|---:|---|---|
| `kind` | string | Yes | Broad source of failure or scope of the record | `adversarial` |
| `lifecycle` | array of strings | Yes | Stages in which a threat is introduced or activated, or a failure is evaluated | `training`, `inference` |
| `mechanism` | array of strings | Yes | How the attack, shift, or failure is produced | `adversarial-patch` |
| `surface` | array of strings | Yes | Direct system boundary or boundaries through which the threat, shift, or failure is introduced or observed | `visual-perception` |
| `target` | array of strings | Yes | Component, representation, or asset affected or evaluated | `vla-policy` |
| `consequence` | array of strings | Yes | Concrete endpoint of the threat or failure chain | `task-failure` |

The repository uses descriptive semantic labels. Numbered surface codes defined by an individual paper or survey are not used as canonical metadata.

### Threat Kinds

| Value | Use when |
|---|---|
| `adversarial` | An attacker intentionally manipulates training, input, state, model, action, or infrastructure. |
| `non-adversarial` | The study evaluates OOD shift, ambiguity, uncertainty, or naturally occurring failure without an attacker. |
| `system-failure` | Failure originates from system design, integration, controller, recovery, or infrastructure behavior. |
| `evaluation` | A benchmark covers several distinct threats and has no single primary threat path. |
| `survey` | A survey or position paper describes a threat landscape rather than one concrete threat. |

### Lifecycle Vocabulary

| Value | Definition |
|---|---|
| `training` | Data collection, pretraining, fine-tuning, post-training, model merging, or checkpoint distribution. |
| `inference` | Deployment-time perception, reasoning, planning, action generation, or runtime interaction. |
| `system` | Middleware, networking, external service, multi-agent, or execution infrastructure. |

`lifecycle` is multi-label. A backdoor can be implanted during `training` and activated during `inference`.

### Surface Vocabulary

| Value | Boundary represented |
|---|---|
| `model-supply-chain` | Training data, adapters, checkpoints, pretrained components, or model distribution. |
| `user-instruction` | Authenticated text or speech accepted as the current task or control intent. |
| `context-memory-retrieval` | Interaction history, persistent memory, ICL examples, RAG documents, or tool results. |
| `physical-semantic-environment` | Scene text, signs, labels, displays, QR codes, or other correctly perceived semantic content. |
| `visual-perception` | Images, video, cameras, visual tokens, patches, textures, or optical signals. |
| `audio-perception` | Speech, microphones, acoustic signals, or audio features. |
| `proprioception` | Joint state, force, tactile feedback, or internal robot sensing. |
| `world-state` | Object relations, occupancy, localization, scene graphs, affordances, or predicted state. |
| `reasoning-representation` | Hidden states, attention, chain-of-thought, or cross-modal representations. |
| `task-planning` | Goals, task decomposition, action order, paths, or recovery strategies. |
| `action-interface` | Action tokens, action chunks, code, tool calls, APIs, skills, or continuous controls. |
| `middleware-network` | ROS/ROS2, DDS, drivers, credentials, cloud models, remote APIs, or transport. |
| `multi-agent-communication` | Robot-to-robot messages, shared memory, claims, or collaborative state. |
| `execution-control` | Trajectories, actuator commands, safety stops, freezing, or resource availability. |

`surface` records only interfaces directly manipulated, shifted, corrupted, or evaluated by the study. It does not encode an inferred internal propagation path. Multiple values are allowed when distinct lifecycle stages use different interfaces. For example, a visually activated backdoor can use both `model-supply-chain` during training and `visual-perception` during inference.

### Mechanism Vocabulary

| Family | Example values |
|---|---|
| Training and supply chain | `data-poisoning`, `backdoor`, `malicious-adapter`, `checkpoint-compromise`, `reward-manipulation` |
| Visual and physical input | `digital-perturbation`, `adversarial-patch`, `adversarial-object`, `typographic-injection`, `environment-manipulation` |
| Language and context | `jailbreak`, `direct-prompt-injection`, `indirect-prompt-injection`, `command-hijacking`, `memory-poisoning`, `retrieval-poisoning` |
| Sensor and state | `sensor-spoofing`, `state-manipulation`, `feedback-spoofing`, `multimodal-desynchronization` |
| Reasoning, planning, and action | `representation-hijacking`, `planning-hijacking`, `action-manipulation`, `action-freezing`, `trajectory-manipulation` |
| System and communication | `middleware-compromise`, `network-attack`, `multi-agent-propagation`, `denial-of-service`, `sensitive-data-exposure`, `memorized-data-retention`, `covert-channel` |
| Non-adversarial and system failure | `distribution-shift`, `instruction-ambiguity`, `perception-error`, `semantic-misalignment`, `planning-error`, `execution-error`, `constraint-violation`, `uncertainty-miscalibration`, `unsafe-policy-behavior` |

### Target Vocabulary

| Value | Target object |
|---|---|
| `perception-model` | Visual, audio, or multimodal perception component. |
| `world-state` | Structured or predicted state used for downstream decisions. |
| `reasoning-process` | Internal reasoning, attention, or multimodal alignment. |
| `task-planner` | Goal selection, task decomposition, path, or high-level policy intent. |
| `vla-policy` | End-to-end or partially exposed VLA policy. |
| `action-generation` | Action token, chunk, trajectory, code, or tool generation. |
| `runtime-monitor` | Guardrail, verifier, detector, or safety judge. |
| `robot-executor` | Controller, actuator, safety stop, or execution process. |
| `shared-system-state` | Memory, middleware, cloud service, or multi-agent shared state. |
| `private-data` | Training membership, observations, identity, location, or other sensitive data. |

### Consequence Vocabulary

| Value | Concrete endpoint |
|---|---|
| `task-failure` | The assigned task or route is not completed. |
| `targeted-action` | The system performs an attacker-selected action or action sequence. |
| `action-freezing` | The policy stops or produces dangerous inaction. |
| `unsafe-success` | The task succeeds while violating a safety property. |
| `collision` | The robot contacts an obstacle, person, or prohibited object. |
| `unsafe-motion` | Unsafe force, speed, pose, trajectory, or control behavior occurs. |
| `physical-damage` | A person, robot, object, or environment is harmed or damaged. |
| `control-hijacking` | An unauthorized source gains influence over robot behavior. |
| `policy-violation` | The agent performs explicitly prohibited or harmful behavior. |
| `privacy-leakage` | Sensitive information is inferred, exposed, or transmitted. |
| `availability-loss` | The system is frozen, stopped, delayed, or denied service. |
| `recovery-failure` | Detection, mitigation, replanning, or recovery does not restore safe operation. |

The existing `risks` field remains separate. `risks` records empirically evaluated outcome families, while `consequence` records the specific endpoint represented by the threat path.

### Concrete Study Example

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

### Backdoor Example

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

### Survey and Broad-Evaluation Records

Surveys and broad benchmarks should not be assigned an invented single target or consequence. They use a coverage variant instead. A general survey that does not analyze safety mechanisms may use an empty `mechanisms` list; a broad safety or security survey may use `["multiple"]`.

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

### README Rendering

The README retains one `Threat Model` column. The generator renders structured metadata as a compact two-line summary using a clear jewel-tone palette: periwinkle blue for lifecycle, coral for surface, mint teal for mechanism, violet for target, and pink-raspberry for consequence. A `+N` suffix reports additional values stored in `data/papers.json`.

| Study type | Proposed display |
|---|---|
| Adversarial patch | `Inference` `Visual Perception`<br>`Adversarial Patch` → `VLA Policy` → `Task Failure` |
| Backdoor | `Training → Inference` `Model Supply Chain +1`<br>`Backdoor` → `Action Generation` → `Targeted Action` |
| OOD evaluation | `Inference` `Visual Perception`<br>`Distribution Shift` → `VLA Policy` → `Task Failure` |
| Runtime defense | `Inference` `Action Interface`<br>`Unsafe Policy Behavior` → `Runtime Monitor` → `Collision` |
| Survey | `Cross-lifecycle` `Multiple surfaces`<br>`Survey coverage` |

Detailed attack chains belong in the corresponding paper notes or source material rather than catalog metadata. This avoids encoding propagation steps that a paper did not explicitly establish.

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

Include a paper when it studies physical-AI safety or trustworthy deployment and at least one of the following holds:

1. It directly studies safety, robustness, security, privacy, misuse, ethics, fairness, or trustworthy evaluation of a VLA, robot policy, autonomous system, or embodied agent.
2. It analyzes an embodied failure, attack, or human impact relevant to physical interaction or deployment.
3. It introduces an OOD, safety, or societal evaluation protocol for physical-AI behavior.
4. It proposes a defense, runtime monitor, guardrail, action shield, fail-safe, or recovery mechanism for an embodied system.

Generic VLM, LLM, robotics, or capability papers should not be included unless their connection to physical-AI risk or trustworthy deployment is explicit.

## Classification Rule

Assign each paper one catalog record and one primary-contribution section. Use `risks` and `tags` for cross-cutting properties; generated thematic tables may display the same record without creating a duplicate entry.

Evaluation records that study human perceptions, trust, or fairness without establishing a specific threat or failure mechanism may use an empty `coverage.mechanisms` list. This leaves the mechanism unasserted rather than inventing an attack or causal failure path.

### Subsection

Within its primary `section`, assign each record one `subsection` — a second, finer-grained grouping used for browsing within that section's table. Like `section`, `subsection` is a closed vocabulary: the current, authoritative list lives in `SUBSECTIONS[section]` in `scripts/validate_catalog.py`, reproduced here for reference.

**surveys**: Domain-Specific Surveys · Embodied AI Safety and Security · General VLA Surveys · Governance and Deployment Assurance · Position Papers and Research Agendas · Privacy, Fairness, and Human-Robot Trust · Training and Adaptation Surveys · World Model Safety and Security

**ood-generalization**: Action and Spatial Generalization · Driving Robustness and Generalization · Language and Instruction Generalization · OOD and Generalization · Open-World Evaluation · Reliability-Oriented Policy Refinement · Representation and Language-Action Generalization

**training-attacks**: Backdoors and Data Poisoning · Privacy and Data Leakage

**inference-attacks**: Jailbreaks and Prompt Injection · Planning, Action, and Trajectory Manipulation · Privacy and Data Leakage · Sensor, State, and Physical Interventions · Upstream VLM Attacks · Visual Perturbations and Patches

**defenses**: Failure Detection, Shielding, and Recovery · Model Unlearning and Data Governance · Multimodal Perception and Physical Safeguards · Privacy-Preserving Perception · Representation Steering and Inference-Time Defense · Runtime Monitoring and Guardrails · Safety Requirements and Assurance · Safety-Aligned and Robust Policy Training · System and Communication Defenses · Uncertainty, Abstention, and Human Oversight

**benchmarks**: Adversarial and Physical Robustness · Evaluation Infrastructure · Failure Detection and Recovery · Governance and Deployment Assurance · Human-Robot Trust and Fairness · Privacy and Data Leakage · Robustness, Uncertainty, and OOD Generalization · Safety-Critical Perception Evaluation · Semantic and Ethical Safety · Task and Physical Safety

**system-security**: Cross-Layer System Security · Privacy, Misuse, and Covert Channels

The same subsection name can legitimately recur under more than one section (e.g. "Failure Detection and Recovery" under both `defenses` and `benchmarks`, or "Privacy and Data Leakage" under three attack/benchmark sections) — these describe the same topic approached as a different contribution type (defending against it vs. benchmarking it vs. attacking via it) and are not duplicates of each other.

When curating a record, reuse an existing subsection whenever the paper reasonably fits one; only add a new value when it genuinely doesn't fit any existing option for that section, and do so by adding it to both `SUBSECTIONS[section]` in `scripts/validate_catalog.py` and `SUBSECTIONS_JA` in `scripts/labels_ja.py` in the same commit — see [the metadata schema](metadata-schema.md#subsection) for the full operational rule.
