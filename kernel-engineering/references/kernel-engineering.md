# Kernel Engineering Reference

This reference captures a repeatable engineering method for building elite production kernels.

It is written for compute-heavy runtime paths such as:

- attention kernels
- paged KV-cache kernels
- mixed-fidelity memory hierarchies
- fused recurrent kernels
- quantized read/write kernels
- reshape-and-cache kernels
- backend-native handoff surfaces

The aim is to combine low-level kernel sharpness with system-level production truth.

## Table Of Contents

- Kernel Philosophy
- The Kernel Stack
- Regime Partitioning
- Narrow Kernel Contracts
- Metadata As ABI
- Precision Contracts
- Data Movement Discipline
- Tile And Launch Discipline
- Native Handoff Discipline
- Mixed-Layout Kernel Design
- Fast-Path Design
- Benchmarking
- Validation
- Refactor Strategy
- Review Checklist
- Output Patterns

## Kernel Philosophy

The cleanest high-performance kernels share a common pattern:

- they do one thing
- they know exactly which regime they own
- their metadata is shaped for the kernel
- their numerical assumptions are explicit
- their launch rules are not accidental

Production kernel systems add another requirement:

- they must remain honest about what is safe, what is supported, and when to fail closed

The right target is not minimalism at any cost.

The right target is:

- minimal hot-path complexity
- maximal boundary clarity

## The Kernel Stack

Think in layers.

### Layer 1: Product Or Runtime Policy

This layer decides:

- what behavior is required
- what fallback is acceptable
- what shapes matter
- what production guarantees must hold

This layer should not leak into inner loops.

### Layer 2: Regime Selection

This layer decides which kernel family member should run.

Examples:

- raw-only versus mixed-layout
- prefill versus decode
- segmented versus non-segmented
- backend-native handoff versus custom path
- low-pressure versus oversubscribed memory regime

This logic should be explicit and testable.

### Layer 3: Metadata Construction

This layer builds the exact kernel-facing descriptors and tensors each regime requires.

It should remove ambiguity rather than preserve it.

### Layer 4: Kernel Execution

This layer should perform as little interpretation as possible.

The kernel should mostly execute a pre-decided contract.

## Regime Partitioning

The biggest mistake in advanced kernel systems is trying to make one universal kernel elegant.

When materially different execution regimes exist, create a kernel family.

Typical regime splits:

- raw-only prefill
- raw-only decode
- mixed-layout prefill
- mixed-layout decode
- short-context decode
- long-context decode
- single-stream
- concurrent multi-stream

When a regime can be identified before launch, it usually deserves:

- its own code path
- its own metadata contract
- its own benchmarks
- its own correctness tests

### Rule

If a branch meaningfully changes:

- memory layout
- quantization behavior
- tile choice
- synchronization strategy
- accumulator shape
- fast-path legality

then it is probably a regime boundary, not just a local conditional.

## Narrow Kernel Contracts

Each kernel should have a tiny explicit contract.

Define:

- required tensor layouts
- supported dtypes
- supported head sizes
- supported page/block sizes
- supported query/decode regime
- whether prefix caching is allowed
- whether quantized storage may appear
- whether the kernel may assume all pages are materialized

Also define what the kernel intentionally does not support.

The cleanest kernels are strong because they reject unsupported work early.

## Metadata As ABI

Kernel-facing metadata should be treated like an ABI.

Do not let scheduler truth, allocator truth, debug truth, and kernel truth collapse into one messy structure.

### Separate These Concerns

- scheduler-side planning structures
- allocation ownership structures
- canonical storage identity
- kernel-facing descriptors
- debug or diagnostic overlays

### Design Rules

- Kernel metadata should be compact.
- Fields not consumed by a regime should not be present in its hot metadata path.
- The cheapest possible representation should be chosen for hot-loop reads.
- Frequently accessed fields should be grouped for locality.
- If two regimes need different descriptors, give them different descriptor buffers.

### Good Metadata Questions

- Can the kernel infer less and read more pre-resolved truth?
- Are we passing role names when a bitfield would do?
- Are we passing tables that include information a specific path never reads?
- Are we forcing the kernel to rediscover raw-only status that was already known upstream?

## Precision Contracts

Precision choices should be justified numerically, not just historically.

For each regime, define:

- storage precision
- dequant precision
- accumulation precision
- cast boundaries
- scale encoding
- saturation assumptions
- tolerated error envelope

### Example Questions

- Why is bf16 acceptable for stored state?
- Why is fp16 acceptable for a specific transform or inverse?
- Which path needs fp32 accumulation?
- What error budget is acceptable for packed int4 value storage?
- Which quantities must remain raw?

### Numerical Contract Pattern

For every important precision choice, write:

- the assumption
- the reason
- the failure mode
- the test that would catch it

This turns “folklore optimization” into repeatable engineering.

## Data Movement Discipline

Many kernel systems lose more to movement and metadata than to math.

Optimize:

- loads
- stores
- staging
- reshapes
- layout transforms
- descriptor fetches
- synchronization

### Preferred Moves

- Reuse shared memory across non-overlapping lifetimes.
- Separate producer-heavy and recurrence-heavy stages when their parallelism differs materially.
- Avoid shared-memory round trips when register-file transforms can do the same work.
- Remove unused table reads from raw-only paths.
- Keep quantized unpacking out of regimes that cannot see quantized pages.

### Diagnostic Prompt

Ask of every kernel:

- what data is read?
- what data is interpreted?
- what data is transformed?
- what data is only there because of a more general regime?

Anything in the fourth category is a cleanup candidate.

## Tile And Launch Discipline

Tile and launch choices should not be accidental.

Define shape policy explicitly:

- supported shapes
- preferred shapes
- degraded but allowed shapes
- fallback shapes

### Encode Launch Decisions From First Principles

Launch policy should reflect:

- occupancy
- register pressure
- shared-memory pressure
- memory coalescing
- recurrence structure
- head/query parallelism
- architecture-specific backend behavior

### Avoid Opaque Heuristics

If a threshold exists, document:

- what it means
- what metric it trades off
- how it was chosen
- what cells it helps
- what cells it hurts

If possible, make launch policy table-driven by regime and shape class.

## Native Handoff Discipline

Sometimes the best kernel engineering choice is to not run your custom kernel.

When the standard backend-native path wins in a specific regime, treat that as a first-class design fact.

### Good Native Handoff Rules

- explicit legality checks
- explicit shape checks
- explicit backend checks
- fail-closed fallback when assumptions are not met
- direct tests for handoff eligibility

### Never Do This

- implicit silent fallback
- shape-insensitive global handoff
- use a native path with metadata it was not designed to consume

Native handoff is part of the kernel architecture, not an embarrassment.

## Mixed-Layout Kernel Design

Mixed-layout kernels are inherently harder and usually uglier than raw-only kernels.

The goal is not to make them tiny. The goal is to keep them disciplined.

### Techniques

- Hoist regime checks out of inner loops.
- Separate raw-page handling from warm-page handling as early as possible.
- Pre-resolve quant mode where possible.
- Prefer specialized mixed variants when a single universal mixed kernel becomes too branch-heavy.
- Keep unpack/dequant logic isolated from the rest of the math flow.

### When To Split Mixed Kernels Further

Split when one kernel is carrying materially different:

- warm value formats
- role tables
- prefix-cache rules
- segmented decode behavior
- dequant pathways

## Fast-Path Design

Every production kernel system should identify its happiest path and make it beautiful.

Usually this is something like:

- all pages raw
- standard head size
- standard block size
- common decode shape
- no unusual biasing or multimodal range logic

### Fast-Path Rules

- Remove all branches irrelevant to the fast path.
- Use the minimum metadata required.
- Choose the most native storage layout possible.
- Keep write and read kernels specialized for that path.
- Benchmark it independently.

The fast path should not merely be “the general path with fewer branches taken.”

It should feel purpose-built.

## Benchmarking

Benchmarking must happen at multiple layers.

### Layer 1: Microbench

Measure isolated kernel behavior:

- raw-only read
- raw-only write
- mixed read
- mixed write
- prefill
- decode
- segmented decode

### Layer 2: Regime Bench

Measure realistic metadata and shape regimes:

- low-pressure
- pressure-adaptive
- long-context concurrent
- single-request short context

### Layer 3: End-To-End Serving

Measure production-shaped throughput, latency, startup, warmup, and reliability.

### Benchmark Rules

- Always compare against the previous implementation.
- Always compare against the standard/native backend where relevant.
- Preserve raw artifacts.
- Tie benchmark cells to concrete regime hypotheses.

## Validation

Never trust performance work without strong validation.

### Required Validation Layers

- exact or near-exact reference correctness
- shape matrix coverage
- dtype matrix coverage
- warmup and startup stability
- deterministic scenario replay when possible
- trace verification or replay artifacts when the stack supports them

### Prefer These Test Shapes

- smallest legal shape
- common production shape
- edge head sizes
- varlen cases
- batch concurrency boundaries
- long-context boundaries
- raw-only boundaries
- mixed-layout boundaries
- native handoff boundaries

## Refactor Strategy

When a kernel already works in production, beautify it cautiously.

### Safe Refactor Sequence

1. Freeze behavior with more golden tests.
2. Add regime-local microbenches.
3. Introduce a new specialized path behind explicit gating.
4. Keep the old path available as comparison truth.
5. Require correctness parity.
6. Require no startup or warmup regression.
7. Require no production throughput regression on target cells.
8. Promote only after all pass.

### Safe Early Wins

- split raw-only and mixed-layout code paths further
- shrink kernel-facing metadata
- formalize launch policies
- isolate dequant logic
- document numerical contracts

### Risky Changes

- broad metadata refactors and kernel rewrites at the same time
- deleting fallback paths before new ones are proven
- changing launch heuristics globally
- mixing architecture cleanup with performance cleanup in one step

## Review Checklist

When reviewing a kernel or kernel family, ask:

- What regimes exist?
- Which regimes are currently entangled?
- What work is being done in the hot path that could be decided upstream?
- Is metadata shaped for the kernel or inherited from other layers?
- Are precision choices explicit and justified?
- Are fast paths truly specialized?
- Are fallback and native handoff boundaries honest?
- Are launch thresholds documented and reproducible?
- Are validation and benchmarks tied to the exact change being made?
- Is the implementation cleaner because it is narrower, or only because detail was hidden?

## Output Patterns

When responding to a kernel-engineering task, it often helps to structure the result as:

- `Regimes`
- `Current Contract`
- `Hot-Path Waste`
- `Metadata ABI`
- `Precision Contract`
- `Fast Paths`
- `Fallbacks`
- `Launch Policy`
- `Validation Plan`
- `No-Regression Rollout`

Use a more concise form when the user wants a short answer, but preserve the same reasoning structure.

## Final Rule

Do not optimize for pretty code alone.

Optimize for kernels that are:

- narrow
- explicit
- numerically justified
- metadata-efficient
- benchmarked honestly
- production-safe
- easy to specialize further

That is what makes a kernel implementation feel elite without sacrificing reality.
