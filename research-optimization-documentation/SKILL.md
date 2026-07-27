---
name: research-optimization-documentation
description: Use when documenting optimization passes, benchmark history, model training rounds, or research implementation status. Especially useful for deduplicating docs, preserving current truth, recording commands and artifacts, avoiding stale claims, and producing concise technical histories after each pass.
---

# Research Optimization Documentation

Use this skill when work produced learning that future engineering decisions must preserve.

The goal is to keep documentation as an operational instrument, not a museum.

## Core Principle

After every meaningful pass, document what changed, what was measured, what was learned, and what decision follows.

Do not duplicate the whole history. Add the new fact to the right single source of truth.

## What To Record

For optimization or training passes, record:

- date
- run name
- status
- code/data changes
- exact artifact paths
- exact commands when useful
- baseline metrics
- trained or repaired metrics
- deltas
- validation commands
- decision
- next bottleneck

For serving or benchmark passes, record:

- launch profile
- workload
- concurrency or cache budget
- latency and throughput metrics
- errors
- memory use
- tradeoff
- decision

## Interpretation Discipline

Separate:

- measured fact
- inference from the measurement
- speculation
- next experiment

Do not overclaim. If a pass improves ranking but not generation, say that. If a route repair makes generation green without new weights, say that. If a benchmark proves capacity but not speed, say that.

## Deduplication

Before adding docs:

1. Find the existing current-status section.
2. Find older sections that describe the same mechanism.
3. Add the new pass as a compact append-only result.
4. Update the summary paragraph if the state changed.
5. Avoid restating old details unless the new result invalidates them.
6. Remove or rewrite stale claims when they would mislead a future operator.

## Tone

Good research docs are sober and useful.

Use:

- exact numbers
- short interpretation
- clear promotion decision
- reproducible paths
- named bottlenecks

Avoid:

- hype without gates
- vague improvement language
- unstated baselines
- hiding failures
- burying the decision in prose

## After Each Pass

Run a doc hygiene check:

- no stale promoted checkpoint claim
- no duplicated current-status paragraphs
- no missing artifact path
- no missing decision
- no sensitive local-only material
- no contradiction between bench log and research summary

Then commit and push with a concise message.
