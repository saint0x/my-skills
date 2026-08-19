---
name: new-project-architecture
description: Define and enforce production-grade architecture for a new greenfield project or a major structural refactor. Use when Codex needs to choose the project skeleton, directory layout, module boundaries, file decomposition, naming conventions, README shape, and implementation standards for an app, service, library, API, full-stack system, or internal tool where maintainability, scalability, and real production readiness matter more than quick placeholder code.
---

# New Project Architecture

Use this skill to set the architecture correctly from the first commit.

Default to real production structure, not demo structure.

## Core Stance

- Build production-grade architecture end to end.
- Do not introduce placeholder, fake, or knowingly disposable implementations unless the user explicitly asks for them.
- Prefer maintainable, scalable, modular systems over clever shortcuts.
- Make the codebase easy to reason about for the next engineer, not just fast to generate today.
- Solve for clean boundaries, clean names, and clean ownership.

If the requested speed or scope would force obviously throwaway architecture, pause and surface the tradeoff before locking in the wrong foundation.

## Workflow

1. Determine the product shape.
2. Choose the architectural layers and module boundaries.
3. Create the skeleton before filling in implementation details.
4. Define the canonical contracts between layers.
5. Implement real end-to-end paths instead of stubs.
6. Fill the README with the minimum high-value operating context.
7. Audit the structure against the rules before finishing.

## Structure Rules

- Organize directories by concern and ownership, not by vague convenience.
- Prefer small, clean subtrees with obvious responsibility.
- Prefer single-word names for files, directories, and subdirectories when possible.
- Use multi-word names only when they materially improve clarity.
- Avoid bloated files. Target roughly 500 to 900 lines per file.
- Split a file before it becomes a grab bag or crosses a clean reasoning boundary, even if it is still under the line target.
- Avoid massive top-level modules that mix transport, domain logic, persistence, orchestration, and formatting in one place.
- Create submodules or packages when a subsystem has distinct contracts, data flow, or lifecycle.
- Keep each directory internally coherent. Every child inside it should make sense as part of the same concern.
- Keep naming strict, plain, and legible. Prefer `auth`, `cache`, `queue`, `store`, `graph`, `voice`, `image`, `worker` over vague or ornamental names.

Do not create directories such as `misc`, `helpers`, `common`, or `utils` unless the contents are truly narrow, stable, and well-defined. Most of the time, hidden architecture debt starts there.

## Architecture Rules

- Build the canonical architecture, not the easiest temporary one.
- Keep business logic in explicit, testable modules rather than controllers, routes, views, or handlers.
- Separate transport, domain logic, persistence, background execution, and integration boundaries when those concerns exist.
- Centralize shared contracts and types where they can remain authoritative.
- Keep interfaces narrow and implementation details behind them.
- Prefer composition over monolith classes or god modules.
- Make scaling paths natural. Do not require a future rewrite just to support more traffic, more features, or more engineers.
- Choose robust implementations that can remain in place as the system grows.
- Make operational behavior legible: configuration, errors, retries, jobs, state changes, and integration boundaries should all have a clear home.

## Implementation Rules

- Ship real code paths.
- Do not leave mocked business behavior in production code.
- Do not create fake repositories, fake adapters, or TODO implementations disguised as architecture.
- Do not hardcode temporary logic that will obviously have to be ripped out for basic scale.
- Default to deterministic, explicit flows over hidden magic.
- Add abstractions only when they clarify ownership or isolate complexity, not to sound architectural.
- Keep the happy path and failure path equally intentional.

When a simpler implementation is still production-correct, prefer the simpler one.

## README Standard

Keep the README concise, direct, and high-signal.

It should usually cover:

- what the project is
- why it exists
- how it is structured
- how to run it
- how to test it
- how to configure it
- any critical operational or deployment notes

Do not turn the README into a long essay. Lead with the important facts and keep the sections short.

## Final Audit

Before finishing a new project or major scaffold, verify:

- the top-level structure reflects real system boundaries
- naming is clean and mostly single-word
- no file is becoming a dumping ground
- modules are concern-scoped
- important logic is not hiding in transport or UI layers
- the implementation is real, not placeholder architecture
- the README is concise and useful

## Read Next

Read [references/project-rules.md](references/project-rules.md) before doing substantial greenfield scaffolding or architecture refactors.

Use it for:

- module-shaping heuristics
- file-splitting rules
- naming discipline
- skeleton checklists
- production-readiness review
