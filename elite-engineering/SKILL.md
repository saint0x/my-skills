---
name: elite-engineering
description: Apply a high-quality engineering bar to code changes by preserving the project mental model, choosing simple optimized implementations, removing dead or false code, adding strong error handling, and validating with the right tests.
metadata:
  short-description: High-bar engineering discipline
---

# Elite Engineering

Use this skill when the user asks for elite engineering, strong architecture, production-quality code, maintainability, scalable implementation, cleanup, refactoring, hardening, or when a coding task would benefit from an explicit quality bar.

The goal is to engineer for the current change and the future reader at the same time. The implementation should be easy for another agent, teammate, or future self to ingest without reconstructing the whole project from scratch.

## Operating Bar

Keep two scales in mind at all times:

- Local shape: the immediate module, function, data flow, error path, and tests should be clear and correct.
- Project mental model: the change should fit the architecture, ownership boundaries, naming, runtime assumptions, and existing abstractions.

Prefer cutting down over adding on. Remove unnecessary branches, stale compatibility paths, false abstractions, unused helpers, no-ops, placeholder code, and dead code in full. Do not leave misleading scaffolding behind just because it is harmless at runtime.

## Architectural Fit

Before editing, read enough surrounding code to understand the intended design. Use existing patterns, helpers, data models, and module boundaries unless there is a clear reason to change them.

Choose the smallest implementation that solves the real problem while preserving future flexibility. Small does not mean clever; it means fewer moving parts, less duplicated state, fewer invalid states, and clearer ownership.

Do not add abstractions speculatively. Add one only when it removes real complexity, gives a name to a stable concept, or matches an established project pattern.

## Implementation Discipline

Prefer optimized implementations in the practical engineering sense:

- Use the right data structure or API rather than doing expensive or fragile work manually.
- Avoid repeated work, hidden quadratic paths, needless network calls, unnecessary renders, and broad invalidation.
- Keep hot paths explicit and easy to reason about.
- Make failure states visible and actionable instead of silently swallowing them.

Strong error handling is part of the feature. Handle expected failures at the boundary where they can be explained or recovered from. Preserve useful context in errors and logs without leaking secrets.

Avoid fake completion. No placeholder logic, inert flags, empty catch blocks, TODOs that stand in for behavior, no-op adapters, dead feature switches, or code that pretends a case is handled when it is not.

## Maintainability

Code should teach the project model as it is read:

- Names should reflect domain meaning, not implementation trivia.
- File placement should make ownership obvious.
- Functions should expose clear contracts and keep side effects legible.
- Comments should explain non-obvious decisions, not restate syntax.
- Tests should describe important behavior and protect the contract that matters.

When changing behavior, remove the old behavior completely unless backward compatibility is required. If compatibility is required, make the boundary explicit and tested.

## Validation

Run the tests that map to the change. Start narrow, then broaden when the blast radius touches shared behavior, contracts, build tooling, routing, persistence, security, performance, or user-facing workflows.

If tests are not needed for a tiny documentation-only or metadata-only change, say why. If tests cannot be run, report the blocker and the remaining risk.

For bug fixes, prefer reproducing the failure first or proving the root cause through code, logs, traces, or a focused test. Do not ship a plausible patch without verifying the real path when verification is feasible.

## Review Before Done

Before finishing, check:

- The code fits the local module and the broader project mental model.
- Dead, false, placeholder, and no-op code introduced or made obsolete by the change is removed.
- Error handling covers expected failure modes with useful context.
- The implementation is simpler or more direct than the state it replaces, unless added complexity is justified.
- Tests or validation match the real risk.
- A future agent can understand what changed, why it belongs there, and how to extend it safely.

Report the final result in plain engineering terms: what changed, what was removed or simplified, what validation ran, and any residual risk.
