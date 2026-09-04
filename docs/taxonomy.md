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

## 3. Structured Threat Model

> **Status: Proposed.** This schema is presented for review before the catalog records and README generator are migrated.

The `threat_model` field should be a structured object rather than a compact free-text string. It separates when a threat occurs, how it operates, where it first enters the system, what it targets, and what consequence it produces.

### Core Fields

| Field | Type | Required for a concrete study | Meaning | Example |
|---|---|---:|---|---|
| `kind` | string | Yes | Broad source of failure or scope of the record | `adversarial` |
| `lifecycle` | array of strings | Yes | Stages in which compromise is introduced or activated | `training`, `inference` |
| `mechanism` | array of strings | Yes | How the attack, shift, or failure is produced | `adversarial-patch` |
| `primary_surface` | string | Yes | First system boundary directly compromised or affected | `visual-perception` |
| `target` | array of strings | Yes | Component or representation the threat is intended to alter | `vla-policy` |
| `consequence` | array of strings | Yes | Concrete endpoint of the threat or failure chain | `task-failure` |
| `trigger` | array of strings | No | Condition that activates a previously implanted threat | `visual-trigger` |
| `propagation_surfaces` | ordered array of strings | No | Important boundaries crossed after the primary surface | `reasoning-representation`, `action-interface` |

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

### Primary Surface Vocabulary

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

The primary surface records the first affected boundary, not the final location where harm becomes visible. For example, a visual patch that eventually causes an unsafe action starts at `visual-perception`, not `execution-control`.

### Mechanism Vocabulary

| Family | Example values |
|---|---|
| Training and supply chain | `data-poisoning`, `backdoor`, `malicious-adapter`, `checkpoint-compromise`, `reward-manipulation` |
| Visual and physical input | `digital-perturbation`, `adversarial-patch`, `adversarial-object`, `typographic-injection`, `environment-manipulation` |
| Language and context | `jailbreak`, `direct-prompt-injection`, `indirect-prompt-injection`, `command-hijacking`, `memory-poisoning`, `retrieval-poisoning` |
| Sensor and state | `sensor-spoofing`, `state-manipulation`, `feedback-spoofing`, `multimodal-desynchronization` |
| Reasoning, planning, and action | `representation-hijacking`, `planning-hijacking`, `action-manipulation`, `action-freezing`, `trajectory-manipulation` |
| System and communication | `middleware-compromise`, `network-attack`, `multi-agent-propagation`, `denial-of-service`, `privacy-leakage`, `covert-channel` |
| Non-adversarial | `distribution-shift`, `instruction-ambiguity`, `perception-error`, `planning-error`, `execution-error`, `uncertainty-miscalibration` |

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
  "primary_surface": "visual-perception",
  "target": ["vla-policy"],
  "consequence": ["task-failure"],
  "trigger": [],
  "propagation_surfaces": [
    "reasoning-representation",
    "action-interface"
  ]
}
```

### Backdoor Example

```json
"threat_model": {
  "kind": "adversarial",
  "lifecycle": ["training", "inference"],
  "mechanism": ["backdoor"],
  "primary_surface": "model-supply-chain",
  "target": ["action-generation"],
  "consequence": ["targeted-action", "task-failure"],
  "trigger": ["visual-trigger"],
  "propagation_surfaces": [
    "visual-perception",
    "action-interface"
  ]
}
```

### Survey and Broad-Evaluation Records

Surveys and broad benchmarks should not be assigned an invented single target or consequence. They use a coverage variant instead.

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

### Proposed README Rendering

The README should retain one `Threat Model` column. The generator will render structured metadata as a compact two-line threat path rather than creating five additional columns.

| Study type | Proposed display |
|---|---|
| Adversarial patch | `Inference · Visual Perception`<br>Adversarial patch → VLA policy → Task failure |
| Backdoor | `Training → Inference · Model Supply Chain`<br>Backdoor / visual trigger → Action generation → Targeted action |
| OOD evaluation | `Inference · Visual Perception`<br>Distribution shift → VLA policy → Task failure |
| Runtime defense | `Inference · Action Interface`<br>Unsafe action → Runtime monitor → Collision prevention |
| Survey | `Cross-lifecycle · Multiple surfaces`<br>Survey coverage |

Detailed triggers and propagation paths remain available in `data/papers.json`; the README displays only the primary path.

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
