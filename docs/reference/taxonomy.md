# Taxonomy and Curation Policy

**English (this page)** | [Japanese](taxonomy.ja.md)

This repository uses a multi-axis taxonomy. A paper's primary section describes its main research contribution; independent metadata describes the outcomes at risk, the failure source, the mechanism, and the evaluation regime.

## 1. Empirically Evaluated Risk Outcomes

The `risks` field is evidence-coded, not a list of plausible consequences. A label is assigned only when the paper's experiments report a metric for that outcome. A survey that discusses all four risks therefore has an empty list, while an attack paper may receive both `task-reliability` and `security-privacy` when it reports task success and attack success rate. Physical deployment alone does not justify a `physical-safety` label.

| Label | Value | Qualifies when the paper reports |
|---|---|---|
| **Task & Reliability** | `task-reliability` | Task or route completion, success rate, or an equivalent end-to-end execution outcome. Action deviation, detection accuracy, calibration error, and attack success alone do not qualify. |
| **Physical Safety** | `physical-safety` | Collision, human injury, object or environment damage, unsafe force or motion, physical-harm execution, safety-constraint violation, or an explicit physical-risk proxy. |
| **Ethical & Societal** | `ethical-societal` | Compliance or refusal under harmful or prohibited instructions, policy or constitution violations, explicitly measured harmful embodied behavior, or measured disparities across people or groups in access, task success, assistance quality, or exposure to hazards. A fairness motivation, a model's inductive bias, or a benchmark's "fair evaluation" of models does not qualify without a corresponding societal-outcome metric. |
| **Security & Privacy** | `security-privacy` | Attack success, backdoor activation, unauthorized control, command hijacking, information leakage, covert communication, compromised memory or communication, and system compromise. |

### Assignment Rule

1. Identify the metrics actually reported in experiments.
2. Map only those metrics to the four outcomes above.
3. Do not assign a label from the title, motivation, deployment setting, or a hypothetical downstream consequence.
4. Use an empty `risks` list when no reported metric maps to these outcomes; the README displays `—`.

## 2. Failure Sources

A paper's `threat_model.kind` is one of three failure sources (plus `survey`/`evaluation` for records that span several threats — see [Threat Kinds](#threat-kinds)):

| Label | Value | Definition |
|---|---|---|
| **Adversarial / Malicious** | `adversarial` | An attacker intentionally manipulates inputs, training data, model states, actions, the environment, or system components. |
| **Non-Adversarial / OOD** | `non-adversarial` | The system fails under unseen viewpoints, visual appearances, objects, geometries, language, tasks, environments, embodiments, or temporal dynamics without assuming an attacker. |
| **Design, Training, or System Failure** | `system-failure` | The failure arises from objective misspecification, multimodal misalignment, reward hacking, sensor faults, planner-executor mismatch, or insufficient runtime recovery. |

## 3. Structured Threat Model

> **Status: Adopted.** All catalog records and the README generator use this schema.

The `threat_model` field should be a structured object rather than a compact free-text string. Five fields answer five questions about the threat or failure path — **when** it occurs, **where** it enters, **how** it operates, **what** it targets, and **what follows** — plus `kind`, a separate field for what broad category of record this is.

### Role Separation

Each field answers a distinct question and is assigned from distinct evidence; none is inferred from another by a fixed mapping rule:

- **`surface` (where)**: the system boundary or interface through which the threat is introduced, shifted, or observed — the entry point or delivery channel.
- **`mechanism` (how)**: the attack technique or failure mode the paper studies.
- **`target` (what is targeted)**: the component, capability, or asset the paper's stated objective, loss function, or evaluation protocol explicitly names — not every component plausibly affected along the way.
- **`consequence` (what follows)**: the specific endpoint the threat or failure path reaches.
- **`risks` (what is measured, Section 1)**: the broad empirically evaluated risk domain, independent of `threat_model`.

A perceptual delivery channel (`surface`) does not make perception the `target`; a downstream effect does not make it a second `mechanism` label; a risk domain does not determine which `consequence` occurred. See the per-field assignment rules under each vocabulary below for the concrete do/don't boundaries.

### Core Fields

| Field | Question | Type | Required for a concrete study | Meaning | Example |
|---|---|---|---:|---|---|
| `lifecycle` | When? | array of strings | Yes | Stages in which a threat is introduced or activated, or a failure is evaluated | `training`, `inference` |
| `surface` | Where? | array of strings | Yes | Direct system boundary or boundaries through which the threat, shift, or failure is introduced or observed | `visual-perception` |
| `mechanism` | How? | array of strings | Yes | How the attack, shift, or failure is produced | `adversarial-patch` |
| `target` | What is the target of attack or evaluation? | array of strings | Yes | Component, capability, or asset explicitly targeted or evaluated — not everything plausibly affected along the way | `vla-policy` |
| `consequence` | What follows? | array of strings | Yes | Concrete endpoint of the threat or failure chain | `task-failure` |
| `kind` | *(record type, not part of the five)* | string | Yes | Broad source of failure or scope of the record | `adversarial` |
| `curation_status` | *(provenance, not part of the five)* | string | Yes | How thoroughly this assignment was checked against a primary source — see [Mechanism Curation Status](#mechanism-curation-status) | `paper-verified` |

The repository uses descriptive semantic labels. Numbered surface codes defined by an individual paper or survey are not used as canonical metadata.

### Threat Kinds

| Value | Use when |
|---|---|
| `adversarial` | An attacker intentionally manipulates training, input, state, model, action, or infrastructure. |
| `non-adversarial` | The study evaluates OOD shift, ambiguity, uncertainty, or naturally occurring failure without an attacker. |
| `system-failure` | Failure originates from system design, integration, controller, recovery, or infrastructure behavior. |
| `evaluation` | A benchmark covers several distinct threats and has no single primary threat path. |
| `survey` | A survey or position paper describes a threat landscape rather than one concrete threat. |

### When? — Lifecycle Vocabulary

| Value | Definition |
|---|---|
| `training` | Data collection, pretraining, fine-tuning, post-training, model merging, or checkpoint distribution. |
| `inference` | Deployment-time perception, reasoning, planning, action generation, or runtime interaction. |
| `system` | Middleware, networking, external service, multi-agent, or execution infrastructure. |

`lifecycle` is multi-label. A backdoor can be implanted during `training` and activated during `inference`.

### Where? — Surface Vocabulary

Values are grouped below by where they sit in the perceive → reason → act pipeline, from upstream training/infrastructure through to downstream action and control.

| Value | Boundary represented |
|---|---|
| **Training & Infrastructure** | |
| `model-supply-chain` | Training data, adapters, checkpoints, pretrained components, or model distribution. |
| `middleware-network` | ROS/ROS2, DDS, drivers, credentials, cloud models, remote APIs, or transport. |
| **Perception** | |
| `visual-perception` | Images, video, cameras, visual tokens, patches, textures, or optical signals. |
| `audio-perception` | Speech, microphones, acoustic signals, or audio features. |
| `physical-semantic-environment` | Scene text, signs, labels, displays, QR codes, or other correctly perceived semantic content. |
| **Language** | |
| `user-instruction` | Authenticated text or speech accepted as the current task or control intent. |
| `context-memory-retrieval` | Interaction history, persistent memory, ICL examples, RAG documents, or tool results. |
| `multi-agent-communication` | Robot-to-robot messages, shared memory, claims, or collaborative state. |
| **Proprioception** | |
| `proprioception` | Joint state, force, tactile feedback, or internal robot sensing. |
| **Planning & State** | |
| `world-state` | Object relations, occupancy, localization, scene graphs, affordances, or predicted state. |
| `task-planning` | Goals, task decomposition, action order, paths, or recovery strategies. |
| **Reasoning** | |
| `reasoning-representation` | Hidden states, attention, chain-of-thought, or cross-modal representations. |
| **Action & Control** | |
| `action-interface` | Action tokens, action chunks, code, tool calls, APIs, skills, or continuous controls. |
| `execution-control` | Trajectories, actuator commands, safety stops, freezing, or resource availability. |

`surface` records only interfaces directly manipulated, shifted, corrupted, or evaluated by the study. It does not encode an inferred internal propagation path. Multiple values are allowed when distinct lifecycle stages use different interfaces. For example, a visually activated backdoor can use both `model-supply-chain` during training and `visual-perception` during inference.

### How? — Mechanism Vocabulary (technique-oriented)

`mechanism` classifies the concrete attack technique or failure mode a paper studies, **not** an inferred causal mechanism. It answers "how is the attack carried out, or what failure mode is investigated?" — not "what is the deepest root cause?" Concrete, recognizable research terminology (`adversarial-patch`, `typographic-injection`, `backdoor`, `membership-inference`, ...) is preserved even when it names a specific attack implementation rather than a fundamental primitive. Families group related attack techniques and failure modes, which is a deliberately different axis from `surface` (grouped by *where* it occurs in the perceive → reason → act pipeline); a family does not correspond to one surface family. **Data & Model Attacks** is an umbrella for poisoning or compromising data, models, memory, or retrieval stores, as well as inferring sensitive information from them. It does not require data or model modification; `membership-inference` remains in this family.

**Assignment rules:**

1. Assign a label only when the paper's method or experiments establish it; do not assign from the title alone.
2. Multiple labels are allowed when each is independently evidenced and conveys distinct information (e.g. an adversarial patch that also carries printed text qualifies for both `adversarial-patch` and `typographic-injection`).
3. Do not add a second label merely because the first mechanism causes a downstream effect (e.g. a jailbreak that happens to change a robot's plan is `jailbreak` alone, not `jailbreak` plus a planning-specific label; the planning impact belongs in `target`/`consequence`).
4. Do not infer an attack technique from a defense paper's motivating threat model alone; a defense evaluated only against hand-crafted or unmodeled "unsafe" examples has no demonstrated HOW and should omit the field or use a value the paper itself establishes.
5. Prefer the most specific supported label; use an empty `mechanism` list when the paper's evidence does not establish a concrete technique or failure mode. This is different from not having reviewed the record yet — see `curation_status` below.
6. A label naming direct manipulation of internal model state (e.g. `representation-manipulation`) requires the paper's optimized variable or attack target to be the internal representation itself. Using an internal-feature-based loss to optimize an input (a patch, a text prefix, a perturbation) does not qualify — that is still an input-level technique (`adversarial-patch`, `digital-perturbation`, ...), with the internal feature only serving as the loss's target.

| Value | Attack technique or failure mode |
|---|---|
| **Data & Model Attacks** | |
| `data-poisoning` | Training data is corrupted to induce a predetermined failure or behavior. |
| `backdoor` | A trigger condition is implanted to activate attacker-chosen behavior. |
| `malicious-adapter` | A fine-tuned adapter, LoRA module, or plugin is distributed with hidden harmful behavior. |
| `checkpoint-compromise` | A pretrained or shared model checkpoint is tampered with before distribution. |
| `reward-manipulation` | Training signals or reward functions are corrupted to shape unsafe behavior. |
| `memory-poisoning` | Persistent memory or long-term context store is corrupted with malicious content. |
| `retrieval-poisoning` | Documents or examples in a retrieval corpus are corrupted to bias retrieved content. |
| `membership-inference` | An adversary infers whether specific data was part of training or memory, typically via model-internal features or confidence signals, without assuming prompt-level access alone. |
| **Perturbation & Spoofing** | |
| `digital-perturbation` | Imperceptible or constrained noise is added to a digital input (image, text, audio, or another modality). |
| `adversarial-patch` | A crafted visible patch or texture is placed to fool perception. |
| `adversarial-object` | A physical object is engineered to trigger a targeted failure. |
| `sensor-spoofing` | A physical sensor (e.g. GPS, LiDAR, IMU) is fed falsified signals. |
| `feedback-spoofing` | Internal or external feedback signals are falsified to mislead the system. |
| `environment-manipulation` | Physical objects or scene layout are altered to induce a failure. |
| **Instruction & Semantic Manipulation** | |
| `direct-prompt-injection` | A malicious instruction is given directly as user input. |
| `indirect-prompt-injection` | A malicious instruction is embedded in content the system later processes. |
| `jailbreak` | Prompting or an optimized adversarial input circumvents safety training to elicit restricted or unintended behavior. |
| `typographic-injection` | Text rendered in the scene is read and acted on, either as an instruction or by overriding visual/semantic judgment. |
| `hazardous-instruction` | A benign-seeming instruction leads to a physically or socially harmful outcome; a recognized, commonly benchmarked class of instruction-following failure. |
| **Runtime & System Manipulation** | |
| `middleware-compromise` | Middleware, drivers, or transport layers are compromised. |
| `network-attack` | Network communication is intercepted, altered, or disrupted. |
| `denial-of-service` | Availability is degraded or blocked through resource exhaustion, flooding, or exploiting safety mechanisms to halt execution. |
| `covert-channel` | Hidden information is exfiltrated or communicated outside authorized channels. |
| `state-manipulation` | The system's internal belief or state representation is directly tampered with at runtime, independent of sensing — requires demonstrated direct tampering, not an inferred cause of a downstream fault. |
| `action-manipulation` | Output action tokens or commands are directly altered before execution. |
| `trajectory-manipulation` | A generated motion trajectory is itself the object of the demonstrated technique, not merely a downstream effect of an already-assigned perturbation or injection label. |
| `representation-manipulation` | Internal hidden states or cross-modal representations are the attacker's directly optimized or overwritten target — not an input optimized using an internal-feature loss (see assignment rule 6). |
| **Distribution Shift & Uncertainty** | |
| `distribution-shift` | Test-time conditions differ from the training distribution without an attacker. |
| `instruction-ambiguity` | A natural, non-malicious instruction is underspecified or vague. |
| `uncertainty-miscalibration` | The system's confidence does not match its actual reliability. |
| **Reasoning, Planning & Execution Failure** | |
| `perception-error` | Perception misidentifies or mislocalizes without adversarial cause. |
| `semantic-misalignment` | Language and visual or action grounding diverge without adversarial cause. |
| `planning-error` | The planner produces an infeasible, suboptimal, or unsafe plan without an attacker. |
| `execution-error` | Low-level execution deviates from the intended action without an attacker. |
| `self-assessment-failure` | The agent reports task completion although an independent assessment against explicit task criteria establishes that the task remains incomplete. |
| `multimodal-desynchronization` | Modalities fall out of time or semantic alignment, corrupting fused understanding. |

`self-assessment-failure` belongs to HOW / **Reasoning, Planning & Execution Failure**, not to a new family. Require evidence of both the agent's explicit completion report and an independent assessment of the corresponding task state against explicit criteria. Ordinary task failure, an external judge's error, and continued actions after success alone do not qualify. The label describes an observed failure mode; it does not establish deception, a perceptual cause, or confidence miscalibration. Add `perception-error` or `uncertainty-miscalibration` only when separately established, following the mechanism assignment rules above. Store it in `threat_model.mechanism`, or `coverage.mechanisms` for a supported broad-evaluation record, rather than duplicating it in `tags`.

[AA-Robotics v0.1](https://artificialanalysis.ai/articles/aa-robotics/) illustrates the distinction with reports of completion despite unmet placement criteria. It is a research preview, not a catalog paper record; its qualitative examples do not establish a failure rate. A paper's section/subsection (for example, `benchmarks / Failure Detection and Recovery`) is a separate classification by primary contribution and is not this HOW family.

A handful of labels are defined but may have zero current users — a label stays in the controlled vocabulary when it names a clear, reusable technique even before a catalog paper demonstrates it (`representation-manipulation` is the current example), rather than being removed and re-added each time evidence appears.

`kind` correlates loosely with mechanism family but is not a strict parent of it: `adversarial` records span most attack-technique families above (not just one), `non-adversarial`/`system-failure` records concentrate in — but aren't perfectly confined to — Distribution Shift & Uncertainty and Reasoning/Planning/Execution Failure, and `survey`/`evaluation` records can cover mechanisms from several families at once via `coverage.mechanisms`. Treat `kind` as a separate axis (what *kind* of record this is), not as a level above `mechanism`.

### Mechanism Curation Status

`threat_model.curation_status` records how thoroughly the current `mechanism` (and the rest of the structured threat model) assignment was checked against a primary source, using the same scale as the `defense`/`evaluation`/`benchmark` extensions: `paper-verified`, `abstract-verified`, `catalog-derived`, `reference-only`. This distinguishes a record that has not yet been re-checked under the current vocabulary (`catalog-derived`) from one that was reviewed and found to have no evidence-supported technique (`paper-verified` with an empty `mechanism` list) — both are valid states, but they mean different things for future curation.

### What Is the Target of Attack or Evaluation? — Target Vocabulary (objective-oriented)

`target` is the component, capability, or asset **explicitly targeted or evaluated** by the paper's stated attack objective, defense goal, or evaluation design — not every component a causal chain might plausibly pass through, and not a mechanistic claim about internal model behavior.

**Assignment rules:**

1. Identify the paper's explicitly stated attack objective, loss function, or evaluation protocol, and assign `target` from what that objective names — not from `surface` (where the attack is delivered) or `consequence` (what results).
2. Do not assign `perception-model` merely because an attack is delivered through an image, sound, or other perceptual channel; assign it only when perception/recognition accuracy is itself what the paper attacks or measures.
3. Do not assign `reasoning-process` or `task-planner` merely because the observed failure happens to look planning- or reasoning-related; assign them when the paper's objective or evaluation protocol explicitly concerns reasoning or planning (e.g. a stated goal of redirecting a task plan, or a success metric over plan/decision correctness).
4. Multiple targets are allowed only when the paper explicitly attacks, defends, or evaluates more than one component — not as a hedge.
5. `vla-policy` remains appropriate whenever the overall policy or its task-level behavior is explicitly the subject and no narrower target is established by the paper; do not replace it with a narrower label by inferring internal computation the paper does not state.

| Value | Target object |
|---|---|
| **Perception & Understanding** | |
| `perception-model` | Visual, audio, or multimodal perception component. |
| **Reasoning, Planning & Policy** | |
| `task-planner` | Goal selection, task decomposition, path, or high-level policy intent. |
| `reasoning-process` | Internal reasoning, attention, or multimodal alignment, when explicitly the stated objective or evaluation target. |
| `world-state` | Structured or predicted state used for downstream decisions, including world models used for planning. |
| `vla-policy` | End-to-end or partially exposed VLA policy, used when the overall policy or its task-level behavior is explicitly targeted and no narrower label is established. |
| **Action & System Operation** | |
| `action-generation` | Action token, chunk, trajectory, code, or tool generation. |
| `robot-executor` | Controller, actuator, safety stop, or execution process. |
| `runtime-monitor` | Guardrail, verifier, detector, or safety judge. |
| `shared-system-state` | Memory, middleware, cloud service, or multi-agent shared state. |
| **Data & Privacy Assets** | |
| `private-data` | Training membership, observations, identity, location, or other sensitive data. |

`vla-policy` sits in Reasoning, Planning & Policy rather than a model/data family: across the catalog it is overwhelmingly used for the policy's *behavior* (task success or failure under attack or shift), not for extracting or corrupting it as a stored artifact — that narrower case already has its own labels (`backdoor`, `data-poisoning`, `checkpoint-compromise`, `membership-inference` under `mechanism`). `private-data` is kept as its own single-leaf family rather than folded into another one, the same way `proprioception` stands alone in the Surface vocabulary — it names a distinct concern (data/privacy exposure) that does not fit the perception, reasoning/planning, or action/infrastructure families.



### What Follows? — Consequence Vocabulary (flat controlled vocabulary)

`consequence` is a **flat** controlled vocabulary with no family grouping. `risks` (Section 1) already gives the broad risk-domain view — Task & Reliability, Physical Safety, Ethical & Societal, Security & Privacy — so grouping `consequence` into similar families would duplicate that role rather than add information. `consequence` instead records the specific endpoint of the threat or failure path; a single risk domain routinely spans several different, non-interchangeable consequences (e.g. `security-privacy` covers `control-hijacking`, `targeted-action`, and `privacy-leakage` alike, which are different outcomes that `risks` alone cannot distinguish). `unsafe-success` and `policy-violation` both describe the agent's own behavior violating a safety or ethical norm regardless of whether an external attacker caused it, while `control-hijacking` specifically means an outside party gained influence; `ethical-societal` risk outcomes concentrate almost entirely in `policy-violation`, not in `control-hijacking` — exactly the kind of distinction `risks` alone cannot express.

| Value | Concrete endpoint |
|---|---|
| `task-failure` | The assigned task or route is not completed. |
| `recovery-failure` | Detection, mitigation, replanning, or recovery does not restore safe operation. |
| `collision` | The robot contacts an obstacle, person, or prohibited object. |
| `unsafe-motion` | Unsafe force, speed, pose, trajectory, or control behavior occurs. |
| `physical-damage` | A person, robot, object, or environment is harmed or damaged. |
| `targeted-action` | The system performs an attacker-selected action or action sequence. |
| `action-freezing` | The policy stops or produces dangerous inaction. |
| `control-hijacking` | An unauthorized source gains influence over robot behavior. |
| `unsafe-success` | The task succeeds while violating a safety property. |
| `policy-violation` | The agent performs explicitly prohibited or harmful behavior. |
| `privacy-leakage` | Sensitive information is inferred, exposed, or transmitted. |
| `availability-loss` | The system is frozen, stopped, delayed, or denied service. |

The existing `risks` field remains separate and plays a different role: `risks` records the broad, empirically evaluated risk domain (Section 1), while `consequence` records the specific endpoint represented by the threat path. Neither can be reconstructed from the other.

### Concrete Study Example

```json
"threat_model": {
  "kind": "adversarial",
  "lifecycle": ["inference"],
  "mechanism": ["adversarial-patch"],
  "surface": ["visual-perception"],
  "target": ["vla-policy"],
  "consequence": ["task-failure"],
  "curation_status": "paper-verified"
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
  "consequence": ["targeted-action", "task-failure"],
  "curation_status": "paper-verified"
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
    "curation_status": "abstract-verified",
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

### Controlled Secondary Tags

`tags` is a non-empty, duplicate-free list of strings from `data/taxonomy/tags.json`. This allow-list preserves existing descriptors, source identifiers, and curation markers unchanged; registration does not certify their scientific meaning or evidence quality. Add a new secondary descriptor to the registry in the same change that first uses it, reusing an existing value where appropriate. A concrete failure mode defined in HOW belongs in `threat_model.mechanism` (or `coverage.mechanisms`), not a duplicate secondary tag. The registry and the HOW vocabulary are separate controlled lists.

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
