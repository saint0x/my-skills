---
name: rlm-sft-rl-round-control
description: Use when planning or running sequential SFT and RL improvement rounds for a coding-agent model. Especially useful for one-round-at-a-time optimization, choosing SFT versus RL, setting conservative update budgets, selecting checkpoints, stopping bad runs, and preserving promotion gates.
---

# RLM SFT RL Round Control

Use this skill when improving a model through SFT, RL, or mixed SFT/RL rounds.

The goal is to make one measurable improvement per round and keep only changes that survive evaluation.

## Core Principle

SFT teaches the model what the target shape is. RL teaches the model to prefer that target over tempting alternatives.

Use SFT when the model cannot reliably emit the right form. Use RL when the model knows the form but ranks shortcuts, adjacent families, or unsafe alternatives too highly.

## Round Shape

Each round should have one named frontier:

- exact argument fidelity
- workflow transition correctness
- hard-negative preference
- OOD project planning
- free-generation termination
- tool-family disambiguation
- live recovery behavior
- long-context constraint retention

Then run:

1. Build or select the focused train/eval data.
2. Run a zero-update baseline from the current best checkpoint.
3. Choose SFT, RL, or SFT then RL based on the failure mode.
4. Use a conservative update budget for the first pass.
5. Select the best checkpoint by the metric that matches the round goal.
6. Run focused eval again.
7. Run preservation gates only if the focused result improved.
8. Document and push after the pass.

## Choosing SFT

Prefer SFT when:

- exact generation is near zero
- the model emits prose instead of action tokens
- the model emits malformed tool JSON
- the model repeats instruction tails
- the target format changed
- the desired behavior is not present in raw generations

SFT settings should be small until direction is proven. Watch loss, token accuracy, token-F1, prompt echo, JSON validity, and repeat collapse.

Do not continue SFT just because loss improves. If exact generation, token-F1, or echo move the wrong way, stop.

## Choosing RL

Prefer RL when:

- the target form exists but loses to shortcuts
- preference accuracy is below target
- mean margin is negative or barely positive
- wrong adjacent action families beat the target
- hard negatives reveal the model has bad taste, not bad syntax

Use length-normalized preference when long action chains compete against short tool JSON. Preserve raw logprob in artifacts for diagnosis, but do not let raw length bias dominate the decision.

## Checkpoint Selection

Never assume the final checkpoint is best.

Select by:

- focused preference accuracy, then mean margin for preference rounds
- exact generation, then token-F1, then echo for generation rounds
- project-builder validity, then project-builder score for project rounds
- broad gate preservation for promotion rounds

If an intermediate checkpoint is better, use it.

## Stopping Rules

Stop or branch the round when:

- a focused metric improves but a non-negotiable gate regresses
- SFT improves loss but not generation
- RL improves margin but worsens exact generation or safety behavior
- prompt echo rises materially
- repeat collapse returns
- tool schema or exact arguments regress
- the round reveals a harness/data bug rather than a model weakness

## Practical Loop

Use a fast inner loop and a full outer loop.

Inner loop:

- smaller generation slice
- faster checkpoint selection
- enough samples to catch direction

Outer loop:

- full held-out eval
- broad preservation gates
- OOD gate
- live canary
- docs and push

Do not spend full live-suite time on candidates that did not first move the focused frontier.

## Reporting

Report each round as:

- `Round name`
- `Seed checkpoint`
- `Data/corpus`
- `Training settings`
- `Baseline`
- `Best checkpoint`
- `Focused delta`
- `Preservation result`
- `Decision`
- `Next bottleneck`
