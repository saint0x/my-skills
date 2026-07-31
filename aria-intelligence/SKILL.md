---
name: aria-intelligence
description: Use when the user wants to turn a concept into a canonical Aria intelligence surface such as a tool, agent, team, or pipeline. Especially useful for surface selection, typed schemas, bundled handler design, SDK profile selection, local versus cloud upload, registry hot-update verification, and converting vague product ideas into production-safe Aria runtime artifacts.
---

# Aria Intelligence

Use this skill when the job is not just to write code, but to produce a real Aria intelligence artifact that can be built, uploaded, run, and verified.

## Principle

Do not start from implementation syntax. Start from the runtime surface.

A good Aria artifact is chosen by execution shape first, then expressed through the canonical SDK path with typed contracts, a buildable bundle, a real registry upload, and a live `/api/v1/run/*` verification.

## Choose The Right Surface

Use a tool when the unit of value is one callable capability with explicit typed inputs and a bounded result.

Use an agent when the unit of value is one role with prompt policy, model behavior, and a controlled tool allowlist.

Use a team when multiple agents should collaborate with distinct roles or routing logic.

Use a pipeline when the work is a deterministic multi-step graph that wires tools, agents, or teams together.

If the concept can be one grounded tool, do not inflate it into an agent first.

## Workflow

1. Rewrite the user idea as an execution contract.
2. Pick tool, agent, team, or pipeline based on the smallest faithful surface.
3. Define the typed schema and success shape before writing handlers.
4. Implement through the SDK project structure, not ad hoc database edits.
5. Run `arc check`, then `arc build`, then `arc upload` against the correct profile.
6. Verify the exact live path with `arc run` or `/api/v1/run/tool`, `/api/v1/run/agent`, `/api/v1/run/team`, or `/api/v1/run/pipeline`.
7. Reject the artifact if upload succeeds but the live run does not prove the intended behavior.

## Working Rules

- Prefer canonical SDK definitions and bundle upload over direct SQL writes.
- Keep schemas strict, typed, and minimal.
- Make handler output easy to verify programmatically.
- Give agents the narrowest tool allowlist that still satisfies the task.
- Use teams only when role separation matters materially.
- Use pipelines for deterministic orchestration, not for prompt-only delegation.
- Verify hot updates on the live runtime after upload; do not assume persistence implies execution freshness.
- For runtime bugs, inspect AFW source before trusting docs.
- For local versus cloud work, choose the SDK profile first so commands, auth, and upload target stay coherent.

## Surface Design Heuristics

A tool should answer: what are the inputs, what side effects are allowed, what exact result proves success, and what failure should be surfaced verbatim.

An agent should answer: what role is stable across runs, what toolset is allowed, what prompt policy is mandatory, and what evidence proves the agent truly used the tool path.

A team should answer: why more than one agent is necessary, how members differ, and what output the overall team must own.

A pipeline should answer: what step graph is deterministic, what data flows between steps, what dependencies are explicit, and which step type each node really is.

## Verification Standard

A finished artifact must prove all of the following:

- the bundle builds
- the upload lands on the intended runtime
- the registry entry is visible
- the run endpoint succeeds on the real runtime
- the output reflects the latest uploaded logic
- failures are concrete rather than hidden behind generic assistant fallback text

## Read Next

Read [references/aria-intelligence.md](references/aria-intelligence.md) before implementing substantial Aria intelligence work.

Use it especially for:

- tool versus agent versus team versus pipeline selection
- typed contract design
- SDK project and profile flow
- upload and hot-update discipline
- live run verification
- production-safe acceptance criteria
