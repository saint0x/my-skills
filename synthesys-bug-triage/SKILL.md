---
name: synthesys-bug-triage
description: Use when triaging, reproducing, fixing, and shipping a Synthesys backend bug that may involve database truth, telemetry, provider drift, runtime behavior, or cross-system contract mismatches. Especially useful for issues spanning Supabase, Vapi, Twilio, Stripe, ElevenLabs, notifications, deployment state, or backend/frontend/provider disagreement where factual findings, root-cause repair, and production-safe verification matter more than quick patches.
---

# Synthesys Bug Triage

Use this skill when the job is not just to make the symptom disappear, but to prove what is true across code, database, telemetry, providers, and runtime behavior, then heal the bug class from the core.

## Principle

Triage starts with evidence, not theory.

Do not guess from one log line.

Do not trust one layer in isolation.

Do not paper over drift in the controller, frontend, or prompt layer when the real defect lives in the canonical contract, synchronization path, repository, service, job flow, or provider-state projection.

If the bug is real, reproduce it, inspect every relevant source of truth, state the factual findings clearly, fix the root cause architecturally, verify the exact path, then promote and redeploy cleanly.

## Canonical Operating Surface

Work from the canonical local checkout only:

- `/Users/deepsaint/Desktop/work/synthesys-backend`

Honor the backend architecture:

- `src/api`: transport, validation, orchestration
- `src/services`: business logic and invariants
- `src/db/repositories`: persistence and typed data access
- `src/api/schemas` and `src/api/validation`: request and contract boundaries
- `src/types`: canonical shared types
- `src/services/job`: async execution backbone
- `src/telemetry`: runtime observability and incident evidence

Read `AGENTS.md` before substantial bug work if the active context does not already include it.

## Workflow

1. Rewrite the bug report as a concrete failing contract.
2. Reproduce the symptom locally or against the relevant live surface.
3. Inspect the code path end to end before changing code.
4. Inspect database truth with `admin-scripts/db.sh`.
5. Inspect telemetry truth with `admin-scripts/db.sh telem ...`.
6. Inspect every relevant provider or operator surface with the matching `admin-scripts/*.sh` script.
7. Compare code, database, telemetry, provider, and user-visible behavior directly.
8. State factual findings first. Separate confirmed facts from inferences.
9. Fix the root cause in the canonical layer instead of adding a compatibility bandage.
10. Add or extend regression coverage with Bun tests and Fozzy when runtime behavior is affected.
11. Verify the repaired path, including at least one recorded deterministic Fozzy trace when feasible.
12. Promote through `staging`, then `main`, then redeploy with the canonical deploy script when the shipped backend state changed.

## Working Rules

- Start from the real contract, not from the loudest symptom.
- Use the repo’s admin scripts as the primary investigative tooling.
- If a provider could be involved, inspect provider truth directly instead of inferring from application logs.
- If telemetry could explain the failure, query telemetry before speculating.
- Treat database state as canonical unless the architecture explicitly defines another source of truth.
- Prefer proving mismatches with side-by-side evidence: code path, row state, telemetry event, provider object, and visible symptom.
- Present findings as facts, including IDs, timestamps, statuses, and exact mismatches when available.
- If the bug spans multiple repos, repair and ship every affected repo coherently rather than leaving the system half-migrated.
- Do not ship frontend, prompt, or controller workarounds for a backend contract bug.
- Do not normalize provider drift into a permanent contract unless that is the explicit product decision.
- Fail closed at spend, execution, or routing boundaries when parity or capability truth is missing.

## Investigative Defaults

Always inspect these first unless the bug is obviously narrower:

- the relevant controller or route
- the owning service
- the backing repository and SQL shape
- the shared types and validation schema
- the job handler if async execution is involved
- telemetry logs, spans, events, incidents, and provider interactions when available
- the matching provider script under `admin-scripts/`

Use Aegis CLI only for browser or web-flow validation.

Use Fozzy first for system-level verification, replay, trace capture, shrinking, and deterministic runtime confidence.

## Required Evidence Standard

A solid triage result should usually include:

- exact reproduction steps or the reason repro is currently blocked
- relevant code-path location
- relevant database rows or query results
- telemetry evidence
- provider-side evidence when applicable
- a clear root-cause statement
- why the chosen fix removes the bug class instead of hiding the symptom
- verification evidence after the fix

## Delivery Standard

If the user did not explicitly limit the task to investigation only, default to finishing the job:

1. investigate
2. reproduce
3. repair architecturally
4. verify
5. push `staging`
6. promote to `main`
7. redeploy with `admin-scripts/deploy.sh` when backend runtime or deployed config changed
8. perform post-deploy verification

## Read Next

Read [references/synthesys-bug-triage.md](references/synthesys-bug-triage.md) before substantial triage work.

Use it especially for:

- admin-script selection by provider or failure class
- factual findings format
- database and telemetry query workflow
- reproduction and validation discipline
- root-cause repair rules
- `staging -> main -> redeploy` promotion flow
