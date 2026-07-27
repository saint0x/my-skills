---
name: production-checkpoint-export-serving
description: Use when exporting, packaging, registering, serving, or rolling back model checkpoints and adapters. Especially useful for generic export commands, checkpoint lineage, adapter manifests, serving bundle validation, SOCK/vLLM registration, interactive chat smoke tests, and promotion-safe rollout discipline.
---

# Production Checkpoint Export Serving

Use this skill when turning a trained candidate into something a user can actually run.

The goal is to preserve checkpoint truth from training through export, serving, chat smoke, and rollback.

## Core Principle

A model is not production-ready because a checkpoint exists. It is production-ready when the checkpoint can be reproduced, exported, loaded, served, tested, and rolled back with exact lineage.

## Export Contract

Every export should record:

- trainer kind
- base model path or model id
- checkpoint path
- adapter rank and alpha
- target modules
- tokenizer files
- model format
- serving format
- manifest hash
- publication assets
- creation command
- source git commit when available

Use generic export commands where possible. Do not bake RL-only or SFT-only assumptions into the CLI if the operation is fundamentally checkpoint export.

## Serving Contract

Before serving, verify:

- base model loads
- adapter tensors match checkpoint tensors
- tokenizer sidecars exist
- serving engine can import required extensions
- runtime uses the intended vendor dependency stack
- model registration points to the exported artifact, not a stale work dir
- launch settings are recorded
- rollback model/profile is known

## Smoke Tests

Run both mechanical and user-shaped tests.

Mechanical:

- import runtime modules
- load model and adapter
- one-token generate
- simple tool JSON prompt
- model metadata endpoint

User-shaped:

- streaming chat
- project prompt
- tool/harness prompt if applicable
- refusal or approval-boundary prompt
- latency and tokens/sec sample

If the user will interact through a harness, smoke through that harness, not only raw text generation.

## Rollout Discipline

1. Export candidate artifact.
2. Validate artifact manifest and lineage.
3. Register under a non-destructive candidate name.
4. Launch serving profile.
5. Run local smoke.
6. Run user-path smoke.
7. Run benchmark or canary appropriate to the deployment.
8. Promote only after the current safe model remains available for rollback.
9. Document the exact served path and rollback command.

## Failure Modes

- Export path silently uses the wrong checkpoint.
- Adapter shape matches but lineage is stale.
- Runtime imports from a different torch or dependency stack.
- Serving path works raw but fails through the intended harness.
- Chat endpoint is non-streaming when the product path needs streaming.
- Candidate overwrites the safe model before gates finish.
- Rollback exists in theory but not as a tested command.

## Output Shape

Report:

- `Export artifact`
- `Base model`
- `Checkpoint`
- `Serving profile`
- `Validation commands`
- `Smoke results`
- `Benchmark or canary results`
- `Rollback path`
- `Promotion decision`
