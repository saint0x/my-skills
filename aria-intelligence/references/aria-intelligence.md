# Aria Intelligence Reference

## Goal

Turn a concept into the smallest correct Aria runtime artifact, then prove it on the live runtime.

## Canonical Path

Default to the SDK path:

1. create or open the SDK project
2. define typed tools, agents, teams, or pipelines in source
3. run `arc check`
4. run `arc build`
5. select the right profile with `arc config profile local` or `arc config profile cloud`
6. run `arc upload dist/<bundle>.aria`
7. verify with `arc run ...` or the runtime `/api/v1/run/*` surface

Use raw registry HTTP only when debugging the runtime, testing the registry directly, or repairing SDK drift.

## Surface Selector

### Tool

Choose a tool when:

- one call should do the job
- inputs can be expressed as a typed JSON object
- success is grounded in a concrete output
- you need strict handler behavior or deterministic verification

Design rules:

- keep the input schema small and explicit
- require fields that materially affect correctness
- return machine-checkable output where possible
- include version markers or activation markers when verifying hot updates

### Agent

Choose an agent when:

- the concept needs persistent role behavior
- prompt policy matters across runs
- the model must decide how to use one or more tools
- success depends on tool choice plus reasoning style

Design rules:

- give the agent the narrowest useful tool allowlist
- keep the system prompt operational rather than ornamental
- define what the agent must do when a tool fails
- verify that the agent actually produced tool traces instead of answering from memory

### Team

Choose a team when:

- roles differ materially
- delegation or coordination is itself part of the behavior
- a single agent prompt would collapse distinct responsibilities

Design rules:

- make each member role legible
- keep member count small unless the collaboration pattern is the product
- ensure the top-level objective belongs to the team, not just one member
- verify member outputs or delegated tool traces, not just the final prose

### Pipeline

Choose a pipeline when:

- the orchestration graph is deterministic
- step dependencies matter
- tool, agent, or team steps should be wired explicitly
- input mapping and output flow are part of correctness

Design rules:

- keep step IDs stable and descriptive
- model dataflow explicitly in `input_mapping`
- only use pipeline steps that correspond to a real runtime boundary
- verify step results, step health, and final output

## Typed Contract Checklist

Before implementation, write down:

- artifact kind
- name
- user-visible purpose
- exact input object
- exact output object or text contract
- allowed side effects
- failure conditions
- live verification probe

If any of these are vague, tighten the contract before writing code.

## SDK Discipline

### Profiles

Use the active SDK profile deliberately.

- `arc config profile local` for local or LAN AFW runtimes
- `arc config profile cloud` for the hosted runtime
- `arc config profile show` or `arc config show` to confirm target state before upload

Do not keep passing ad hoc flags when a stable profile should own the target.

### Build And Upload

Run the narrowest clean loop:

- `arc check`
- `arc build`
- `arc upload dist/<bundle>.aria`

If upload fails, fix schema or bundle truth first. Do not patch the registry database to fake success.

## Live Verification

Prefer the runtime endpoint that matches the artifact:

- tool: `POST /api/v1/run/tool`
- agent: `POST /api/v1/run/agent`
- team: `POST /api/v1/run/team`
- pipeline: `POST /api/v1/run/pipeline`

What to inspect:

- status
- execution health
- raw output
- tool traces
- provenance
- whether the latest handler or prompt revision is the one actually executed

For hot-update testing, use a changed marker in the uploaded logic and verify the live response reflects it immediately.

## Runtime Truth Rules

- The runtime database being updated is not enough; the execution path must reflect the new logic.
- Prefer registry APIs and SDK upload paths over direct mutation.
- If behavior differs from expectation, inspect AFW source and the real runtime path before changing prompts.
- If a local-machine tool fails, distinguish runtime registry issues from local bridge attestation issues.

## Acceptance Bar

Do not call it done unless all are true:

- source is typed and coherent
- bundle builds
- upload succeeds on the intended target
- live run succeeds on the intended target
- latest logic is visible in execution output
- no false success or generic fallback text hides a real failure

## Reporting Pattern

When delivering Aria intelligence work, report:

- chosen surface and why
- schema or role contract
- build/upload target
- live verification command or endpoint
- proof that the current uploaded logic ran
- any remaining runtime or bridge limitation
