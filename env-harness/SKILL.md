---
name: env-harness
description: Use when validating, repairing, or hardening evaluation harnesses, runtime environments, route guards, sandboxes, canaries, and dependency stacks for RLM or RL systems. Especially useful when metrics look suspicious, harness behavior may mask model weakness, or production-shaped tests must prove real execution and safety boundaries.
---

# Env Harness

Use this skill when the environment or harness could be part of the result.

## Principle

Never optimize a model against an untrusted harness. Prove what the harness measures before treating metrics as model truth.

## Validate The Stack

Before trusting a run, verify:

- correct repo and branch
- clean or intentionally dirty worktree
- correct Python/runtime path
- correct vendor dependency path
- correct GPU runtime visibility
- correct model and adapter lineage
- correct local-files-only behavior when required
- no stale server or trainer process owns memory
- artifacts are from the run being discussed
- stdout summary matches `results/latest.json`

## Harness Layers

Inspect changes by layer:

1. dataset contract
2. prompt wrapper
3. decoder or route policy
4. argument repair
5. sandbox/execution backend
6. scorer
7. artifact writer
8. promotion decision

When a number changes, identify which layer changed.

## Route Guard Rules

Route guards are production behavior, not eval hacks.

Good guards:

- scope intent to the active prompt segment
- honor explicit toolcall headers
- fail closed on safety-critical prompts
- record override reason
- preserve already-correct routes
- have narrow tests for each repair

Bad guards:

- scan stale context and override current intent
- silently transform model failure into success
- green a fixture while OOD remains broken
- conflate tool selection with argument correctness

## Canary Discipline

Executable canaries should prove:

- exact JSON or action tokens
- exact tool and arguments
- allowed mutations only
- expected failures observed
- recovery path works
- approval pauses happen at unsafe boundaries
- read-only plans remain read-only
- endpoint/client proof exists when user interaction matters

Expected failures are part of the signal. Do not hide them.

## Debug Workflow

When a gate fails:

1. Print prompt, expected output, generated output, score object, route details, and execution result.
2. Classify the failure as data, route, decoder, model, environment, scorer, or artifact issue.
3. Add a narrow regression test before repair.
4. Rerun the focused failing case.
5. Rerun the full gate only after the focused failure is green.

## Reporting

Always label the pass as model-weight improvement, runtime-route improvement, harness/scorer repair, environment repair, or documentation-only clarification.

That label prevents fake model progress.
