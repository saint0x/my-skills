---
name: sft
description: Use when designing, running, diagnosing, or selecting supervised fine-tuning rounds for coding-agent models. Especially useful for teaching output formats, action-chain imitation, strict tool JSON, project-building trajectories, checkpoint selection by generation quality, and stopping loss-only improvements that do not improve behavior.
---

# SFT

Use this skill when the model needs to learn the target behavior shape.

## Principle

SFT teaches form, rhythm, and contract. It is the right tool when the model cannot reliably emit the output surface needed by production.

## Use SFT When

- exact generation is weak
- the model emits prose instead of action tokens
- tool JSON is malformed
- arguments are missing or wrong-shaped
- prompt tails are echoed
- new task families need exemplars
- project trajectories are too generic
- runtime contract changed and the model needs demonstrations

Use RL after SFT when the model can emit the right form but still ranks shortcuts too highly.

## Data Requirements

SFT rows should be clean, deterministic, and contract-specific.

For action chains:

- output only target action tokens
- preserve order
- stop cleanly
- avoid extra prose
- include diverse but equivalent wording

For tool JSON:

- one object only
- exact canonical tool name
- complete argument object
- strict schema
- no prose before or after JSON

For project-building:

- inspect first
- choose bounded slice
- implement/test/expose/verify
- include user-visible proof
- preserve safety boundaries

## Training Workflow

1. Build or select a focused corpus.
2. Materialize and validate splits before GPU time.
3. Run a zero-update generation baseline.
4. Train with a small update budget first.
5. Evaluate intermediate checkpoints.
6. Select by generation metrics, not final loss.
7. Stop if loss improves but exactness, F1, echo, JSON, or schema do not.
8. Feed remaining preference failures into RL only after generation is viable.

## Metrics

Track:

- eval loss
- token accuracy
- token-F1
- exact match
- JSON validity
- schema validity
- argument match
- prompt echo overlap
- repeat collapse
- project validity/score when relevant

Loss is diagnostic. Behavior is the decision surface.

## Failure Modes

- final checkpoint has lowest loss but worse generation
- examples leak train wording into eval
- target strings include echo-prone prompt labels
- tool rows are valid JSON but wrong arguments
- action chains learn separators or wrappers instead of clean tokens
- model overfits solved fixtures and fails fresh OOD wording

## Reporting

Report corpus, seed checkpoint, train/eval counts, update budget, baseline metrics, best checkpoint, final checkpoint, selected checkpoint rationale, and next failure class.
