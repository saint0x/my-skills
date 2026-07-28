---
name: rl
description: Use when designing, running, diagnosing, or selecting reinforcement learning rounds for coding-agent models. Especially useful for preference optimization, hard-negative construction, length-normalized scoring, checkpoint selection, reward validation, avoiding shortcut wins, and preserving generation quality.
---

# RL

Use this skill when the model mostly knows the target form but chooses worse alternatives under pressure.

## Principle

RL teaches taste. Use it to make the model prefer the right completion over plausible bad completions, not to paper over missing syntax or broken data.

## Use RL When

- target generations exist but lose to shortcuts
- preference accuracy is low
- mean margin is negative or fragile
- adjacent action families beat the target
- wrong tools or wrong arguments are plausible
- unsafe direct action beats approval pause
- the model ranks generic checklists over project-specific trajectories

Use SFT first if the model cannot emit the target shape at all.

## Reward And Negative Design

Hard negatives must be credible:

- short JSON shortcut against long action chain
- correct tool with wrong arguments
- wrong tool with superficially useful arguments
- adjacent project/action family
- unsafe direct execution instead of approval
- prompt echo or instruction-tail completion
- generic checklist instead of concrete workflow

Prefer length-normalized preference when long action chains compete with short completions. Keep raw logprob for diagnosis.

## Round Workflow

1. Name the current safe checkpoint and the RL seed.
2. Run a zero-update baseline on the focused frontier.
3. Verify the hard negatives actually expose the intended failure.
4. Train with a conservative update budget.
5. Evaluate intermediate checkpoints, not just the final step.
6. Select by focused preference first, then generation preservation.
7. Reject if exact generation, tool schema, safety, or broad gates regress.

## Diagnostics

Watch for:

- preference margin improves but exact generation drops
- target logprob improves only because outputs got shorter
- shortcut completion remains preferred on hard rows
- prompt echo rises
- repeat collapse returns
- safety approval rows regress
- reward/scorer mismatch with production behavior

If RL improves ranking but not generation, classify it as diagnostic or preference-only. Feed the lesson into SFT or harness repair rather than promoting blindly.

## Checkpoint Selection

Prefer the checkpoint that maximizes the round objective while preserving gates:

- preference accuracy
- mean margin
- exact generation
- strict JSON/tool validity
- exact arguments
- workflow validity
- echo and repeat floors
- broad/OOD preservation

The final step is just another candidate.

## Reporting

Report seed, corpus, update budget, baseline metrics, best checkpoint, final checkpoint, focused delta, generation delta, preservation result, decision, and next reward/data bottleneck.
