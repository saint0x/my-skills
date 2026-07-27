---
name: kernel-engineering
description: Use when the user wants to design, review, refactor, optimize, or productionize high-performance compute kernels such as attention, KV-cache, CUDA, ROCm, Triton, CUTLASS, or fused tensor kernels. Especially useful for kernel decomposition, precision policy, metadata ABI design, launch-shape selection, fast-path partitioning, correctness boundaries, benchmarking, replayable validation, and turning a working kernel into a cleaner elite implementation without regressions.
---

# Kernel Engineering

Use this skill when the task is not just to make a kernel faster, but to make it sharper, cleaner, safer, and more repeatable as an engineering discipline.

The goal is to preserve production truth while improving kernel elegance.

## Use This Skill For

- Designing a new high-performance kernel or kernel family
- Refactoring an existing kernel that already works
- Splitting a broad kernel into narrower fast paths
- Reviewing attention, KV-cache, fused recurrence, quantized, or paged-cache kernels
- Improving CUDA, ROCm, Triton, HIP, or CUTLASS kernel engineering quality
- Building a no-regression optimization roadmap
- Creating kernel validation, benchmarking, and rollout discipline

## Core Principle

Elite kernel engineering comes from combining:

- narrow kernel contracts
- explicit regime selection
- kernel-shaped metadata
- numerically justified precision choices
- launch-shape discipline
- strict correctness and replayability

Do not chase elegance by deleting production safeguards. Move safeguards out of the hot path instead.

## Workflow

1. Identify the real regimes.
2. Separate system policy from kernel hot-path work.
3. Define the kernel-facing ABI for each regime.
4. Minimize each kernel's responsibility.
5. Make precision and tile decisions explicit and falsifiable.
6. Build reference tests and narrow microbenches before changing code.
7. Refactor one regime at a time behind strict gating.
8. Require no-regression proof before promotion.

## Working Rules

- Prefer a kernel family over one universal kernel when regimes are materially different.
- Push decisions upstream when the scheduler, planner, or metadata builder already knows the answer.
- Keep hot loops free of avoidable branching, unused fields, and debug work.
- Treat metadata layout as part of kernel design, not a side detail.
- Encode supported shapes, fallback shapes, and preferred shapes explicitly.
- Preserve fail-closed behavior at every production boundary.
- Use exact or tightly bounded correctness checks, not vibes.

## Read Next

Read [references/kernel-engineering.md](references/kernel-engineering.md) before making substantial kernel design or refactor decisions.

Use it especially for:

- regime partitioning
- metadata ABI cleanup
- raw-only versus mixed-layout strategy
- numerical contract design
- launch heuristics
- benchmarking and rollout gates

