---
name: inference-serving-benchmarking
description: Use when benchmarking or tuning inference serving systems. Especially useful for separating single-user streaming tokens/sec from aggregate throughput, measuring memory-pressure benefits, saturation behavior, queueing, latency percentiles, concurrency, allocator headroom, and production inference experience.
---

# Inference Serving Benchmarking

Use this skill when the question is how inference actually feels and scales.

The goal is to separate capacity, speed, latency, queueing, and user experience instead of collapsing them into one tokens/sec number.

## Core Principle

There are multiple truths in inference benchmarking:

- `single-user streaming speed`: visible output tokens per second for one chat user
- `aggregate throughput`: completed tokens per second across many requests
- `capacity`: maximum admitted context/concurrency before OOM or rejection
- `latency`: p50/p90/p99 first-token and end-to-end timings
- `queueing`: time spent waiting before decode
- `efficiency`: tokens/sec per GiB, per watt, or per allocated cache budget

Do not use one number to answer all of these.

## Benchmark Types

Run the benchmark that matches the claim.

For user chat speed:

- streaming only
- one user-visible request path
- measure first token latency
- measure output tokens/sec after first token
- avoid batch-only conclusions

For saturation:

- sweep concurrency near the frontier
- record successful requests
- record failed requests and error types
- record p50/p90/p99 latency
- record queue delay
- record completed tokens/sec
- record tokens/sec/GiB

For memory-pressure features:

- compare admission frontier at fixed budgets
- compare latency and failures under pressure
- distinguish startup allocation headroom from live successful inference
- report capacity lift and throughput tradeoff separately

For engine comparison:

- use identical model, prompt set, cache budget, dtype, context length, and sampling settings
- warm up both engines
- report variance across repeated runs
- keep server logs and exact launch commands

## Measurement Rules

- Prefer streaming measurements for user-perceived speed.
- Measure first-token latency separately from decode tokens/sec.
- Report generated tokens, not prompt tokens, when discussing chat output speed.
- Use large enough samples for saturation claims.
- Include errors and timeouts in the result, not just successful requests.
- Avoid changing memory features while claiming raw decode speed improvements.
- Separate prefill-bound, decode-bound, and queue-bound regimes.

## Tuning Workflow

1. Establish a stable baseline launch profile.
2. Identify the goal: single-user speed, aggregate throughput, capacity, or latency under load.
3. Change one serving variable at a time.
4. Run a small smoke to ensure the endpoint is healthy.
5. Run the target benchmark sweep.
6. Compare against the baseline with confidence intervals or repeated runs.
7. Keep the fastest stable profile for that specific goal.
8. Document what got faster and what did not.

## Common Pitfalls

- Reporting aggregate throughput when the user asked for single-user tokens/sec
- Reporting allocator headroom as if it were decode speed
- Ignoring queueing until p90 latency is already bad
- Comparing engines with different sampling or context settings
- Letting speculative decoding add overhead for a model/regime where it does not pay off
- Treating one successful frontier request as robust capacity
- Hiding failed requests from the denominator

## Output Shape

When reporting, use:

- `Question being answered`
- `Launch profile`
- `Workload`
- `Concurrency/context/cache budget`
- `First-token latency`
- `Output tokens/sec`
- `Completed tokens/sec`
- `Errors/timeouts`
- `Memory use`
- `Tradeoff`
- `Decision`

Be precise about whether the win helps the person chatting, the batch workload, or the allocator frontier.
