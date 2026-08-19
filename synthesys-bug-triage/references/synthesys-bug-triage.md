# Synthesys Bug Triage Reference

Use this reference when the bug touches live state, provider drift, async execution, production verification, or more than one architecture layer.

## Triage Goal

The outcome is not "I changed something."

The outcome is:

- we know what was actually wrong
- we know which layer owned the defect
- the fix lives in the canonical place
- the user-visible symptom is gone
- the broader bug class is materially reduced
- the shipped system was verified after promotion

## Start With The Bug Contract

Rewrite the issue in explicit terms:

- expected behavior
- observed behavior
- who is affected
- when it started
- whether it is deterministic, intermittent, or provider/data dependent
- whether the failure is read-path, write-path, async, sync, deployment, billing, routing, or provider parity

Good example:

- "Outbound campaign launch should reject stale phone-to-assistant bindings before spend, but calls are still being created when `phone_numbers.vapi_assistant_id` disagrees with the assigned agent assistant."

Weak example:

- "Campaigns are weird."

## Architecture Walk

Before editing code, walk the real path:

1. API route or webhook entry
2. request validation schema
3. controller orchestration
4. service invariant
5. repository reads and writes
6. job submission and handler execution
7. telemetry emission
8. provider sync or external API interaction
9. frontend or operator-visible result

If the symptom is downstream, walk upstream until you find the earliest layer where truth diverges.

## Admin Script Matrix

Use the repo-owned scripts first.

### Database And Telemetry

- `admin-scripts/db.sh sql '<query>'`
- `admin-scripts/db.sh sql-file <file>`
- `admin-scripts/db.sh query <table> [filters]`
- `admin-scripts/db.sh assistant-links [userId]`
- `admin-scripts/db.sh user <email>`
- `admin-scripts/db.sh user-id <id>`
- `admin-scripts/db.sh telem`
- `admin-scripts/db.sh telem logs 'limit=50'`
- `admin-scripts/db.sh telem spans 'limit=50'`
- `admin-scripts/db.sh telem events 'limit=50'`
- `admin-scripts/db.sh telem incidents 'limit=20'`
- `admin-scripts/db.sh telem providers 'limit=50'`
- `admin-scripts/db.sh telem raw '/api/telemetry/...'`

Use `db.sh` whenever you need canonical row truth, operator-only telemetry endpoints, assistant/phone linkage inspection, or production evidence tied to exact IDs and timestamps.

### Vapi

- `admin-scripts/vapi.sh assistants`
- `admin-scripts/vapi.sh assistant <id>`
- `admin-scripts/vapi.sh assistant-exists <id>`
- `admin-scripts/vapi.sh phones`
- `admin-scripts/vapi.sh phones-by-assistant <id>`
- `admin-scripts/vapi.sh calls <limit>`
- `admin-scripts/vapi.sh call <id>`
- `admin-scripts/vapi.sh metrics [assistantId]`
- `admin-scripts/vapi.sh health`

Use this when the bug may involve assistant payload drift, first-message behavior, runtime prompt mismatch, phone binding mismatch, call outcomes, or provider object absence.

### Twilio

- `admin-scripts/twilio.sh phones [limit]`
- `admin-scripts/twilio.sh phone <sid>`
- `admin-scripts/twilio.sh calls [limit]`
- `admin-scripts/twilio.sh call <sid>`
- `admin-scripts/twilio.sh messages [limit]`
- `admin-scripts/twilio.sh bundles <scope> [limit]`
- `admin-scripts/twilio.sh bundle <scope> <sid>`
- `admin-scripts/twilio.sh bundle-evaluate <scope> <sid>`
- `admin-scripts/twilio.sh health`

Use this when the bug may involve phone capabilities, routing, carrier or regulatory state, message delivery, call state, or subaccount-specific provider truth.

### Stripe

- `admin-scripts/stripe.sh customers [limit]`
- `admin-scripts/stripe.sh customer <id>`
- `admin-scripts/stripe.sh customer-email <email>`
- `admin-scripts/stripe.sh subscriptions [limit]`
- `admin-scripts/stripe.sh invoices [limit]`
- `admin-scripts/stripe.sh payment-intents [limit]`
- `admin-scripts/stripe.sh balance`
- `admin-scripts/stripe.sh health`

Use this when the bug may involve subscription state, billing locks, wallet funding, invoice/payment transitions, or balance-based assumptions.

### ElevenLabs

- `admin-scripts/elevenlabs.sh voices`
- `admin-scripts/elevenlabs.sh voice <id>`
- `admin-scripts/elevenlabs.sh voice-settings <id>`
- `admin-scripts/elevenlabs.sh history [limit]`
- `admin-scripts/elevenlabs.sh history-item <id>`
- `admin-scripts/elevenlabs.sh models`
- `admin-scripts/elevenlabs.sh health`

Use this when the bug may involve voice configuration, generated audio drift, model availability, or provider-level generation history.

### Notifications

- `admin-scripts/notifications.sh count --email <email>`
- `admin-scripts/notifications.sh list --email <email> --limit 20`
- `admin-scripts/notifications.sh send ... --dry-run`

Use this when the bug touches inbox state, unread counts, archived visibility, or admin notification delivery.

### Deployment

- `admin-scripts/deploy.sh status`
- `admin-scripts/deploy.sh targets`
- `admin-scripts/deploy.sh logs [minutes] [lines]`
- `admin-scripts/deploy.sh health [base_url]`
- `admin-scripts/deploy.sh observe [base_url]`
- `admin-scripts/deploy.sh runtime-diff`
- `admin-scripts/deploy.sh runtime-sync`
- `admin-scripts/deploy.sh backend-deploy`
- `admin-scripts/deploy.sh redeploy`

Use this when the bug could be environment drift, rollout skew, unhealthy tasks, stale runtime config, or when a verified backend fix needs deployment.

## Factual Findings Format

Present findings in this order:

1. confirmed symptom
2. relevant identifiers
3. database truth
4. telemetry truth
5. provider truth
6. code-path truth
7. mismatch summary
8. root-cause statement

Example format:

- Confirmed symptom: outbound call creation still proceeds for user `...` despite stale phone/assistant parity.
- Database truth: `phone_numbers.vapi_assistant_id = X`, assigned agent assistant = `Y`.
- Provider truth: Vapi phone still references assistant `X`.
- Telemetry truth: launch span shows parity was not revalidated after job enqueue.
- Code-path truth: service validated parity at request time but job handler recreated provider payload from stale row data.
- Root cause: canonical parity invariant was enforced before enqueue but not at the execution boundary where spend actually occurs.

Facts first. Interpretation second.

## Root-Cause Repair Rules

Prefer fixes like these:

- move invariants into the owning service
- make repository returns explicit and typed
- validate again at irreversible execution boundaries
- repair the synchronization path between database and provider
- remove ambiguous fields and legacy fallbacks
- centralize mapping logic used by more than one path
- add fail-closed behavior where drift should block execution

Avoid fixes like these:

- controller-only guards for domain invariants
- frontend-only remapping for backend truth problems
- prompt hacks for data or provider bugs
- silently accepting multiple competing field shapes
- retry loops that hide deterministic contract failures
- ad hoc scripts as the permanent solution to a code-path defect

If a remediation script is needed, use it as an operational recovery tool, not as a substitute for the underlying code fix.

## Reproduction Discipline

If the bug is reproducible, capture:

- exact request, mutation, or operator action
- relevant IDs
- timestamp window
- expected result
- actual result
- any provider object created or skipped

If the bug is intermittent:

- narrow the affected time window
- collect telemetry around the exact IDs
- compare passing and failing traces
- look for state drift, retries, stale cache, queue timing, or deploy skew

Use Aegis CLI only for browser-facing reproduction or frontend-visible verification.

## Test And Verification Discipline

Use the narrowest proof that actually covers the changed invariant.

For backend code:

- run targeted Bun tests
- add a focused regression test when the issue was missing coverage
- run Fozzy for runtime or system-path changes

Preferred Fozzy flow:

1. `fozzy doctor --deep --scenario <scenario> --runs 5 --seed <seed> --json`
2. `fozzy test --det --strict <scenarios...> --json`
3. `fozzy run ... --det --record <trace.fozzy> --json`
4. `fozzy trace verify <trace.fozzy> --strict --json`
5. `fozzy replay <trace.fozzy> --json`
6. `fozzy ci <trace.fozzy> --json`

If host-backed validation matters, include:

- `fozzy run ... --proc-backend host --fs-backend host --http-backend host --json`

Testing is not complete when only a superficial happy-path check exists and a real deterministic runtime path could have been proven.

## Promotion And Deploy Flow

When the fix is ready:

1. ensure the work is in the canonical local checkout
2. review diff for architecture drift and accidental compatibility hacks
3. commit on `staging`
4. run targeted verification on `staging`
5. push `staging`
6. promote the exact verified result to `main`
7. push `main`
8. run `admin-scripts/deploy.sh redeploy` if backend runtime or runtime config changed
9. run `admin-scripts/deploy.sh health` or `observe`
10. recheck the user-visible or provider-visible path after deploy

If multiple repos are affected, do not stop after fixing only one side of the contract.

## Post-Fix Acceptance Bar

Do not call the bug finished unless most of these are true:

- repro is gone or a previously failing invariant now holds
- database truth is correct
- provider truth matches the canonical backend state
- telemetry shows the repaired path behaving correctly
- regression coverage exists
- the fix lives in the right layer
- `staging` and `main` both carry the intended change
- the deployed backend was revalidated when applicable

## Useful Search Targets

When orienting quickly, search for:

- route path or controller name
- service method owning the domain action
- repository methods touching the relevant table
- telemetry event or span name
- provider client or sync helpers
- `script_definition`
- `vapi_assistant_id`
- parity, canonical, reconcile, remediate, backfill
- job payload type and handler name
