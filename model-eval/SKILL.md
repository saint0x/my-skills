---
name: model-eval
description: Use when evaluating, comparing, promoting, or rejecting model checkpoints for coding-agent work. Especially useful for separating ranking from generation, designing promotion gates, interpreting OOD/live canaries, preserving safe baselines, and deciding whether a candidate is production-ready.
---

# Model Eval

Use this skill when a model appears better and the real question is whether the improvement is promotable.

## Principle

Evaluate the surface the user will actually run. Keep ranking, generation, execution, and safety as separate facts until the final decision.

A strong eval answers:

- Does the model prefer the right answer over plausible hard negatives?
- Does the model generate the right answer under the production decode path?
- Does it execute the workflow safely and exactly?
- Does it preserve older solved behavior?
- Does it generalize outside the training distribution?

## Baseline Discipline

Always name:

- safe promoted checkpoint
- candidate checkpoint or route surface
- base model and adapter lineage
- runtime route/decoder settings
- exact eval corpus and split
- exact command and artifact path

Keep the safe baseline fixed. A candidate is not the new baseline until focused, broad, OOD, and live gates agree.

## Required Metrics

Track ranking metrics separately from generation metrics.

Ranking:

- preference accuracy
- mean preference margin
- target logprob mean
- best-bad or shortcut logprob mean
- length-normalized and raw interpretation when chains compete with short JSON

Generation:

- exact match
- token-F1
- JSON validity
- strict JSON boundary
- tool schema validity
- tool-name match
- exact argument match
- execution validity
- workflow transition validity
- prompt echo overlap
- repeat collapse

For project-building or agentic gates, also track project validity, project score, endpoint/client proof, unexpected mutations, expected failures, and side effects.

## Promotion Workflow

1. Define the hypothesis and the specific frontier the candidate should improve.
2. Run a zero-update or current-surface baseline on that frontier.
3. Run the candidate with identical decode and scoring settings.
4. Inspect every failure class before summarizing.
5. Run preservation gates only when the focused frontier moved.
6. Run OOD gates with fresh wording and fresh problem families.
7. Run live or executable canaries for tool, endpoint, file, or sandbox behavior.
8. Classify the win as model-weight, runtime-route, harness/scorer, environment, or documentation.
9. Promote only when the candidate improves the target frontier and does not regress non-negotiable gates.

## Failure Interpretation

Be precise:

- Ranking win without generation win means the model has better taste but is not yet useful.
- Generation win through route repair is production progress, not weight progress.
- Exact tool with wrong arguments is still a production failure.
- Execution-valid but non-exact arguments can hide contract drift.
- Loss improvement without generation improvement is not promotion signal.
- A narrow green fixture without broad/OOD preservation is not enough.

## Reporting

Report:

- safe baseline
- candidate
- target frontier
- focused metrics
- broad/OOD/live metrics
- regression risks
- decision
- next bottleneck

Use sober language. Say `not promotable` when the evidence says so.
