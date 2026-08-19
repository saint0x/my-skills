# New Project Architecture Reference

Use this reference when the task needs more than the core skill instructions.

## Project Skeleton Checklist

Shape the skeleton around real concerns, not framework defaults.

Typical top-level categories may include:

- `src` for product code
- `test` or `tests` for automated coverage
- `scripts` for operator or development automation
- `docs` for durable project documentation when needed
- `config` for explicit configuration surfaces
- `assets` only when the project materially needs them

Do not force every project into the same tree. The important rule is that each top-level directory should earn its existence and communicate clear ownership.

Inside `src`, prefer concern-scoped modules such as:

- `api`
- `app`
- `auth`
- `cli`
- `db`
- `domain`
- `jobs`
- `queue`
- `store`
- `types`
- `ui`
- `worker`

Choose only the modules that reflect the actual system.

## Submodule and Package Rules

Introduce a distinct submodule, package, or bounded folder when one or more of these are true:

- the subsystem has its own contract with the rest of the codebase
- the subsystem could plausibly be tested in isolation
- the subsystem owns a distinct data model or execution model
- the subsystem integrates with an external system
- the subsystem is likely to grow independently

Avoid creating a separate module when the split only adds ceremony without clearer ownership.

## File Size and Splitting Rules

Target roughly 500 to 900 lines per file.

Treat that as a guardrail, not an excuse. A 350-line file can still be too large if it mixes unrelated concerns. A 950-line file might occasionally survive briefly during active refactors, but it should trigger a deliberate split review.

Split files when:

- multiple responsibilities have accumulated
- unrelated concepts share one file
- a file forces too much scrolling to understand one change
- one class or function family dominates the file
- transport, business logic, and persistence have mixed together
- tests require many fixtures because the file has too much surface area

Useful split directions:

- `routes` from `service`
- `service` from `repository`
- `schema` from `handler`
- `types` from implementation
- `client` from `adapter`
- `queue` from `worker`

## Naming Rules

Prefer names that are:

- short
- literal
- stable
- single-word when practical

Good directory names:

- `auth`
- `cache`
- `graph`
- `image`
- `queue`
- `store`
- `voice`
- `worker`

Acceptable multi-word names when clarity wins:

- `rate-limit`
- `feature-flag`
- `event-store`
- `job-runner`

Avoid:

- `misc`
- `helpers`
- `shared-stuff`
- `thing`
- `manager`
- `final`
- `new`
- `temp`

Prefer names that tell another engineer what the code owns, not what mood it was written in.

## Layering Heuristics

When the stack includes multiple concerns, default to explicit layers:

- transport layer: HTTP routes, RPC handlers, CLI entrypoints, UI event surfaces
- domain layer: business rules and orchestration
- persistence layer: repositories, queries, storage adapters
- integration layer: third-party APIs, SDK clients, provider adapters
- background layer: queues, workers, jobs, schedulers

Do not let the transport layer become the business layer.

Do not let the persistence layer leak transport details.

Keep shared types and contracts authoritative and discoverable.

## Production Standard

The architecture should survive contact with:

- more traffic
- more features
- more contributors
- operational incidents
- retries
- partial failures
- external provider drift

That does not mean overengineering.

It means making decisions that would still look reasonable after success.

## README Checklist

The README should usually answer these questions in a compact form:

- What is this project?
- What problem does it solve?
- What are the main modules?
- How do I run it?
- How do I test it?
- What configuration matters?
- What deployment or operational caveats matter?

If a section does not help a future engineer get productive faster, cut it.

## Review Questions

Ask these before finalizing the project shape:

- Would a new engineer understand the top-level layout quickly?
- Does every directory have a clear reason to exist?
- Are any files becoming catch-alls?
- Is the architecture still clean if the project doubles in scope?
- Have we hidden real complexity behind vague names?
- Did we implement the real path, or only a demo path?
- Would we feel comfortable scaling this without ripping the foundation out?
