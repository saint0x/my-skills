---
name: rlm-model-evaluation-promotion
description: Use when evaluating, comparing, promoting, or rejecting coding-agent model checkpoints. Especially useful for separating preference/ranking movement from generation movement, preserving a safe baseline, running broad and OOD gates, interpreting live canaries, and deciding whether a model is actually production-ready.
---

# RLM Model Evaluation Promotion

Use this skill when a model appears better and the question is whether that improvement is real enough to promote.

The goal is not to find one flattering number. The goal is to decide whether the candidate is safer, stronger, and more useful than the current promoted model without hiding regressions.

## Core Principle

Promotion requires two different wins:

- `ranking win`: the model assigns higher likelihood or preference to the right completion than to hard negatives.
- `generation win`: the model actually emits the right artifact under the production decoding path.

Do not confuse the two. A checkpoint can rank correctly and still fail live generation. A runtime route can generate perfectly while the underlying model preference frontier remains weak.

## Workflow

1. Name the safe baseline and keep it fixed.
2. Name the candidate checkpoint, adapter, runtime route layer, and exact command surface.
3. Run the focused frontier gate that the candidate is meant to improve.
4. Run broad preservation gates that the candidate is not allowed to regress.
5. Run at least one OOD gate with fresh problems, not only a solved fixture.
6. Run a live or executable canary when the model is meant to operate tools, files, tests, or endpoints.
7. Compare ranking metrics and generation metrics separately.
8. Promote only when the candidate improves the target frontier and preserves the non-negotiable floors.
9. Document the exact artifact paths, commands, metrics, and decision.

## Required Metrics

Always track:

- preference accuracy
- mean preference margin
- target logprob mean
- best-bad or shortcut logprob mean
- exact generation
- token-F1
- JSON validity and strict boundary rate
- tool schema validity
- tool-name match
- exact argument match
- execution validity and execution score
- workflow transition validity
- prompt echo overlap
- repeat collapse
- unexpected mutation count
- unexpected side-effect count

For project-building gates, also track:

- project-builder validity
- project-builder score
- instruction echo
- unexpected tool output on action-chain prompts
- endpoint, client, or smoke-test evidence when available

## Promotion Rules

- Keep the existing promoted model until the candidate beats it without regressions.
- Do not promote on final-step margin alone.
- Do not promote because loss improved if generation stayed broken.
- Do not promote because exact generation improved on a narrow fixture if OOD or live gates regressed.
- Treat runtime route repairs as production wins, but label them as runtime wins rather than weight wins.
- Treat zero-update evals as legitimate when validating a runtime or harness change.
- Prefer a mid-run checkpoint over the final checkpoint when the selector and metrics show it is better.

## Interpretation

When reading results, classify the candidate as one of these:

- `diagnostic only`: reveals a bottleneck but does not improve the promoted surface.
- `ranking candidate`: improves preference but not production generation.
- `runtime candidate`: improves generation through decode or route contracts without new model weights.
- `training candidate`: improves model weights on the target frontier.
- `promotion candidate`: improves the target frontier and preserves broad, OOD, and live gates.

Do not collapse these categories. They answer different questions.

## Failure Patterns

Watch for:

- short JSON shortcuts beating long action chains under raw summed logprob
- exact tool selection with wrong arguments
- execution-valid but exact-argument-wrong outputs
- prompt-tail echo that looks like useful reasoning but is just copied instruction text
- repeated numeric or action-step collapse
- live tool headers overridden by later incidental text
- hidden route repair making a weak model look stronger than its logprobs are
- overfitting to a solved gate while fresh OOD rows stay weak

## Output Shape

When reporting status, use:

- `Safe baseline`
- `Candidate`
- `Target frontier`
- `Focused result`
- `Preservation result`
- `Live/OOD result`
- `Regression risks`
- `Decision`
- `Next round`

Be blunt. If the model is not promotable, say why.
