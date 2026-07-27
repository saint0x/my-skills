---
name: rlm-harness-environment-validation
description: Use when validating or repairing model evaluation harnesses, route guards, execution sandboxes, runtime dependencies, and live canaries. Especially useful when metrics look suspicious, when a route repair may mask model weakness, or when production-shaped evaluation must prove real side effects and safety boundaries.
---

# RLM Harness Environment Validation

Use this skill when the harness itself might be part of the result.

The goal is to prove that the evaluation measures the intended behavior, not a decoder artifact, stale dependency, broken environment, or overbroad route guard.

## Core Principle

Never optimize a model against an untrusted harness.

First prove the harness contract:

- what prompt is being tested
- what output is expected
- what execution means
- what side effects are allowed
- what side effects are forbidden
- which runtime routes are deterministic repairs
- which behavior belongs to the model weights

## Harness Layers

Think in layers:

1. Dataset contract
2. Prompt wrapper
3. Decoder or route policy
4. Argument repair
5. Execution sandbox
6. Scoring function
7. Artifact writer
8. Promotion decision

When a result changes, identify which layer changed.

## Route Guard Discipline

Route guards are production code, not eval hacks.

Good route guards:

- scope intent to the current live segment
- honor explicit toolcall headers before broad intent phrases
- fail closed on safety-critical requests
- avoid using stale history as current intent
- preserve selected route when it is already correct
- record guard reason and selected-before-guard tool
- have focused tests for each override

Bad route guards:

- scan the whole prompt and match incidental text
- override explicit tool headers because later notes mention another tool
- silently turn model failure into success without recording it
- make solved fixtures green while OOD rows still fail

## Execution Canary Discipline

Live canaries should execute a real workflow in a disposable workspace.

They should check:

- exact JSON
- tool name
- exact arguments
- execution contract
- allowed mutation paths
- unexpected mutations
- expected failures observed
- recovery after failure
- side-effect expectations
- approval pause behavior
- read-only deploy plans

Expected failures are useful. They prove the model can preserve and use failure signal rather than hiding it.

## Environment Validation

Before trusting a run, verify:

- correct Python/runtime path
- correct vendor torch/runtime dependency path
- correct GPU/ROCm/CUDA visibility
- correct checkpoint path
- correct adapter lineage
- local-files-only behavior when required
- no stale server process is holding memory
- output artifacts are from the run you think they are
- latest result file exists and matches stdout summary

If dependency state changed, run import and smoke tests before training.

## Scoring Discipline

Scorers should distinguish:

- exact match
- valid JSON
- schema validity
- tool-name match
- exact arguments
- execution validity
- workflow transition validity
- semantic project quality
- prompt echo
- repeat collapse

Do not let execution-valid alternative arguments hide exact-argument regressions. Do not let exact strings hide unsafe execution.

## Debug Workflow

When a gate fails:

1. Print the failing prompt, expected output, generated output, score object, execution result, and structured route.
2. Decide whether the failure is data, route, decoder, model, environment, or scorer.
3. Write a narrow test for the failure before repairing it.
4. Rerun the focused failing scenario.
5. Rerun the full suite only after the focused failure is green.

## Reporting

Always say whether a pass is:

- model-weight improvement
- runtime route improvement
- harness/scorer repair
- environment repair
- documentation-only clarification

That distinction is the difference between real model progress and operational hygiene.
