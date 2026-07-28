---
name: inference-engineering
description: Use when building, tuning, serving, or benchmarking inference engines and model runtime paths. Especially useful for streaming tokens/sec, aggregate throughput, KV/cache pressure, allocator headroom, saturation, queueing, latency percentiles, checkpoint export, serving profiles, and rollback-safe deployment.
---

# Inference Engineering

Use this skill when the goal is to make inference faster, larger, more reliable, or more useful to a real user.

## Principle

Do not collapse inference into one tokens/sec number. Separate user-visible speed, aggregate throughput, memory capacity, latency, queueing, and serving reliability.

## Measurement Surfaces

Single-user streaming:

- streaming only
- first-token latency
- output tokens/sec after first token
- generated tokens, not prompt tokens
- stable sampling settings
- multiple repeated prompts

Aggregate serving:

- completed tokens/sec
- successful requests
- failed requests and error types
- concurrency sweep
- p50/p90/p99 latency
- queue delay
- tokens/sec/GiB or tokens/sec/watt when relevant

Memory pressure:

- admitted context frontier
- live successful requests near the frontier
- allocator budget and observed allocation
- OOM/rejection behavior
- throughput tradeoff at the new frontier

## Engine Tuning Workflow

1. Define the goal: chat speed, aggregate throughput, capacity, latency, or stability.
2. Record the exact launch profile: engine, dtype, cache budget, context, batching, scheduling, speculative settings, and environment variables.
3. Warm up the server.
4. Run a tiny streaming smoke before the large test.
5. Change one meaningful variable at a time.
6. Benchmark the regime the user cares about.
7. Inspect server logs for queueing, fallback paths, memory pressure, and kernel/runtime warnings.
8. Keep goal-specific profiles instead of pretending one profile wins every workload.

## Serving And Export

For production model handoff, record:

- base model
- adapter/checkpoint path
- manifest hash or lineage metadata
- tokenizer sidecars
- dependency stack and vendor torch/runtime path
- serving bundle path
- registered model/profile name
- launch command
- smoke prompts
- rollback path

Smoke through the path the user will actually use. If the product uses a harness, test through the harness. If chat must stream, do not accept a non-streaming smoke.

## Optimization Rules

- Optimize single-user streaming and batch saturation differently.
- Treat speculative decoding as workload-dependent, not automatically faster.
- Measure prefill-bound and decode-bound regimes separately.
- Do not claim a memory feature improves decode speed unless measured directly.
- Include errors in the denominator.
- Re-run after warmup and after server restart when comparing profiles.
- Keep rollback profiles available before replacing a safe serving path.

## Reporting

Report:

- question answered
- launch profile
- workload
- concurrency/context/cache budget
- first-token latency
- output tokens/sec
- completed tokens/sec
- errors/timeouts
- memory use
- tradeoff
- decision

State whether the win helps the person chatting, the saturated batch workload, or the allocator frontier.
