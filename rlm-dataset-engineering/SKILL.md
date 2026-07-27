---
name: rlm-dataset-engineering
description: Use when designing, auditing, or extending SFT/RL datasets for coding-agent training. Especially useful for held-out split design, OOD gates, hard negatives, balanced tool coverage, prompt leakage prevention, project-builder tasks, and datasets that expose real production behavior instead of memorization.
---

# RLM Dataset Engineering

Use this skill when the dataset is the product surface.

For coding-agent models, weak data creates fake progress. Strong data exposes exact failure modes: wrong tool, wrong arguments, wrong action family, unsafe side effect, shallow project plan, or overfit fixture behavior.

## Core Principle

A good RLM dataset is an experiment, not a pile of examples.

Every split should answer one question:

- Can the model execute the known contract?
- Can it generalize to new wording?
- Can it reject a tempting shortcut?
- Can it preserve safety boundaries?
- Can it build a useful project slice rather than recite a checklist?

## Dataset Types

Use distinct datasets for distinct questions:

- `contract gate`: exact known tool/action format
- `generalization gate`: fresh wording for the same production behavior
- `OOD gate`: new problem families with the same high-level categories
- `hard-contrast gate`: target plus tempting wrong choices
- `preservation gate`: old solved behaviors that must not regress
- `live canary`: executable workflow with real side-effect checks
- `project-builder gate`: broad task converted into inspect/build/test/expose/verify trajectory

Do not merge these into one blurry score.

## Split Discipline

Train/eval leakage invalidates the signal.

Require:

- disjoint prompt strings between train and eval
- fresh wording in OOD evals
- stable target categories across related gates
- balanced canonical tool coverage
- equal or deliberate weighting across tools
- action/tool ratio stated explicitly
- stable seeds or deterministic generation when expanding variants

If a tool prompt is reused between train and eval with only metadata changed, treat it as leakage until proven otherwise.

## Hard Negatives

Hard negatives should be plausible, not random.

Good negatives include:

- short tool JSON shortcut against a long action chain
- adjacent action family with similar language
- correct tool with wrong argument object
- wrong tool that would still look superficially useful
- unsafe direct action instead of approval pause
- generic checklist instead of project-specific trajectory
- prompt echo or instruction-tail completion

Use hard negatives to train taste. The model should learn why the right answer is right, not just memorize its spelling.

## Tool Balance

For tool-call rows, verify:

- every canonical tool appears
- each tool appears the intended number of times
- schema is complete
- exact argument object is known
- execution validity is independently checkable
- unsafe tools have explicit approval or denial examples

Tool routing can look perfect while exact arguments are weak. Track both.

## Project-Builder Rows

Project-builder data should reward working trajectories.

A strong target includes:

- inspect current repo or workspace
- choose a bounded project slice
- define the interface or contract
- implement the core
- add deterministic tests
- expose an endpoint, CLI, probe, or measurable surface
- smoke from the user/client perspective
- report numeric signal and limitations

Reject:

- generic advice
- toy output
- checklist-only plans
- prompt label echo
- unsafe host access
- unverified implementation claims

## Validation

Before training, validate:

- sample counts
- tool counts
- action/tool split
- prompt disjointness
- JSON parseability
- schema validity
- expected argument objects
- target-family coverage
- absence of echo-prone instruction tails

Do this before GPU time. Bad data is the most expensive bug.

## Documentation

Every new corpus should record:

- why it exists
- train/eval counts
- tool/action split
- held-out families
- hard-negative design
- materialization command
- expected failure mode it should expose
- exact artifact path
