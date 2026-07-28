---
name: dataset-engineering
description: Use when designing, auditing, expanding, or materializing datasets for SFT, RL, RLM, or coding-agent evals. Especially useful for held-out split design, OOD generalization, hard negatives, balanced tool coverage, leakage prevention, project-builder data, and datasets that expose real production behavior.
---

# Dataset Engineering

Use this skill when data quality determines the model signal.

## Principle

A dataset is an experiment. Each corpus should expose one clear behavior, failure mode, or generalization question.

## Dataset Types

- contract gate: exact known output format
- generalization gate: new wording, same behavior
- OOD gate: new problem families, same production bar
- hard-contrast gate: target against plausible wrong choices
- preservation gate: solved behavior that must not regress
- live canary: executable workflow and side-effect proof
- project-builder gate: inspect/build/test/expose/verify trajectories

Do not merge these into a blurry aggregate until each component is understood.

## Split Discipline

Require:

- disjoint prompts between train and eval
- fresh OOD wording
- stable category labels across related gates
- balanced canonical tool coverage
- explicit action/tool ratio
- deterministic materialization
- known expected outputs
- no duplicated prompt tails that teach echo

If eval differs from train only by metadata, treat it as leakage.

## Hard Negatives

Good negatives are tempting:

- correct tool with wrong arguments
- wrong tool with plausible arguments
- adjacent action family
- unsafe action instead of approval pause
- short shortcut against longer target
- generic checklist instead of project-specific plan
- prompt echo or wrapper continuation

Random bad answers teach little. Plausible bad answers teach taste.

## Tool Data

For each canonical tool, verify:

- count per split
- schema completeness
- exact argument object
- execution validity
- safety side-effect expectations
- route ambiguity cases

Tool selection and argument exactness must be scored separately.

## Project Data

Strong project-builder targets include:

- repo/workspace inspection
- bounded slice selection
- interface or contract definition
- implementation step
- deterministic tests
- endpoint/CLI/probe exposure
- user-perspective smoke
- numeric evidence or measurable signal
- limitations and rollback notes

Reject generic plans, toy-only tasks, unsafe host access, and unverified claims.

## Pre-Training Validation

Before GPU time, check:

- sample counts
- split disjointness
- tool counts
- action/tool balance
- JSON parseability
- schema validity
- target family coverage
- hard-negative coverage
- expected failure mode
- artifact path and materialization command

## Documentation

Record why the corpus exists, counts, split rules, held-out families, hard-negative design, validation commands, artifact path, baseline failure, and intended next training action.
