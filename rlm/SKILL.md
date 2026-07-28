---
name: rlm
description: Use when developing or validating reinforcement-learning-machine/coding-agent behavior end to end. Especially useful for agent workflow design, tool/action contracts, qualitative coding-agent generalization, project-building gates, promotion loops, and coordinating SFT, RL, eval, harness, and dataset work into one production path.
---

# RLM

Use this skill when the work concerns the full coding-agent model system, not just one training or eval component.

## Principle

RLM quality is the ability to turn a messy production request into correct bounded action: inspect, reason, edit, test, verify, document, and stop safely.

The model should learn the operating style, not just fixture strings.

## Agent Behavior Targets

Train and evaluate for:

- reading the repo before editing
- identifying the real invariant
- choosing a bounded implementation slice
- using tools with exact arguments
- preserving workspace and host boundaries
- running meaningful tests
- inspecting failures instead of guessing
- updating docs after meaningful passes
- promoting only with evidence
- stopping at a clean checkpoint

## Contract Surfaces

Keep action chains and tool calls distinct.

Action-chain rows test sequencing and judgment:

- inspect first
- isolate bottleneck
- patch narrowest useful path
- test with real signal
- verify no regression
- document decision

Tool-call rows test executable precision:

- exact tool name
- exact argument object
- strict JSON boundary
- schema validity
- safe side effects

Do not let generic prose satisfy either contract.

## Project-Building Quality

A useful RLM project task should force the model to produce a working path, not an essay.

Reward:

- concrete files or modules
- interface/contract definition
- minimal but real implementation
- deterministic tests
- endpoint, CLI, or probe surface
- user-perspective smoke
- numeric evidence where possible
- limitations and rollback notes

Reject:

- checklist-only plans
- broad claims without verification
- unsafe host access
- overfit wording
- toy examples that do not expose coding-agent quality

## End-To-End Loop

1. Identify the current bottleneck from eval and live behavior.
2. Decide whether it is data, SFT, RL, harness, runtime, or model serving.
3. Build the smallest focused round that can expose movement.
4. Preserve older gates before promotion.
5. Run qualitative live or project-shaped tests after numeric gates improve.
6. Document artifact paths, commands, metrics, and the next bottleneck.

## Quality Rubric

Score the model on:

- instruction retention
- tool exactness
- argument exactness
- workflow coherence
- repo awareness
- test selection
- debugging discipline
- safety boundary handling
- project usefulness
- concise stopping behavior

The final goal is not just exact match. The goal is a small model that can reliably help build real systems under the user’s engineering paradigms.
