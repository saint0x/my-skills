---
name: agent-watch
description: Watch a video or screen recording, ground answers in what was actually shown and said, and optionally distill the watch session into a new installed hyper-specific skill. Use when Codex needs to analyze a YouTube video, local `.mp4` or `.mov`, product demo, course lesson, bug repro recording, presentation, tutorial, cooking video, workflow walkthrough, or any visual process where transcript-only reasoning is insufficient and the resulting learning may need to become a reusable skill.
---

# Agent Watch

Use this skill when the model needs real video eyes and ears, not guesses from a title or transcript alone.

Keep the upstream watch runtime intact. Extend it by turning durable lessons from a watch session into a new local skill only when the user wants that outcome.

## Core Workflow

1. Resolve the absolute path of this skill directory.
2. Run the bundled setup preflight before the first watch run.
3. Run the bundled `watch.py` pipeline against the URL or local file.
4. Inspect the returned frames and transcript together.
5. Answer the user from observed evidence, with timestamps when helpful.
6. If requested, distill the watch session into a new hyper-specific skill and install it locally.

## Working Rules

- Treat the bundled scripts in `scripts/` as the canonical runtime.
- Prefer what was actually seen and heard over inferred summaries.
- Use focused re-runs for specific moments instead of sparse whole-video rescans.
- Do not create a learned skill from vague inspiration alone.
- Only create a learned skill when the video yields a repeatable, operational pattern that would help future work.
- When creating a learned skill, make it specific to the observed method, style, sequence, tools, constraints, cues, and failure modes from that source.
- Do not genericize the learned skill into broad internet advice unless the user explicitly asks for abstraction.

## Setup and Execution

Read [references/watch-operations.md](references/watch-operations.md) before substantial use.

Use it for:

- setup and preflight flow
- detail modes and token tradeoffs
- focused-window re-runs
- transcript-cue frames
- failure handling

## Distilling a Learned Skill

When the user wants the watch session converted into a reusable skill, read [references/skill-distillation.md](references/skill-distillation.md) and follow it strictly.

Default behavior:

- create a new skill scaffold with `scripts/init_learned_skill.py`
- write the new skill in the repo or install root the user wants
- include only knowledge actually learned from the watched source
- make the skill narrow, operational, and non-generic
- install it locally after writing it

## Bundled Helper

Use `scripts/init_learned_skill.py` when you need a fast local scaffold for a new learned skill. It creates:

- `SKILL.md`
- `agents/openai.yaml`
- `references/source-notes.md`

Then replace the scaffold text with the actual learned procedure from the watch session.

## Read Next

Read these only as needed:

- [references/watch-operations.md](references/watch-operations.md)
- [references/skill-distillation.md](references/skill-distillation.md)
