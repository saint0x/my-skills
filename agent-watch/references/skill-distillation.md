# Learned Skill Distillation

## Contents

- When to Distill
- Core Rule
- Evidence Standard
- Naming
- Scope
- Required Files
- Distillation Workflow
- Authenticity Rules
- Example Shape
- Installation

## When to Distill

Distill a learned skill only when the watched source teaches a repeatable procedure, taste system, workflow, or decision pattern that is worth reusing.

Good examples:

- a chef demonstrating a specific authentic fettuccine method
- a designer showing a distinctive thumbnail workflow
- a founder walking through one exact sales teardown method
- an engineer demonstrating a concrete debugging ritual

Weak examples:

- general motivation
- broad commentary
- fluff without operational detail
- mixed-source synthesis pretending to come from one video

## Core Rule

The new skill must reflect what was learned from that watch session, not what the internet in general says about the topic.

If the watched source taught:

- a specific sequence
- a specific ratio
- a specific tool choice
- a specific failure pattern
- a specific sensory cue
- a specific phraseology

then preserve that specificity.

## Evidence Standard

Before writing the new skill, capture:

- the source video or file
- the relevant timestamps
- the sequence of actions
- critical materials, tools, or settings
- observable quality cues
- mistakes to avoid
- any implied decision logic

Write those into `references/source-notes.md` for the new skill.

## Naming

Prefer a narrow name that reflects the actual learned method.

Good:

- `authentic-fettuccine`
- `loom-bug-triage`
- `podcast-hook-breakdown`
- `terminal-demo-voiceover`

Bad:

- `cooking`
- `video-learning`
- `watch-notes`
- `general-content-analysis`

## Scope

Keep the new skill tightly bounded.

It should usually answer one of these shapes:

- "do this one process correctly"
- "apply this one method repeatedly"
- "reproduce this one style"
- "use this one evaluation framework"

Do not bloat the learned skill into an encyclopedia.

## Required Files

Every learned skill should usually contain:

- `SKILL.md`
- `agents/openai.yaml`
- `references/source-notes.md`

Only add scripts when the same deterministic transformation would otherwise be rewritten repeatedly.

## Distillation Workflow

1. Run `agent-watch` and inspect the source thoroughly.
2. Decide whether the source contains a durable, reusable method.
3. Create a scaffold:

```bash
python3 "<skill-dir>/scripts/init_learned_skill.py" "<skill-name>"
```

4. Fill `references/source-notes.md` with watch-session evidence.
5. Rewrite `SKILL.md` so it teaches the exact learned method in imperative form.
6. Make the trigger description specific enough that the skill fires only for the right jobs.
7. Install the skill locally.

## Authenticity Rules

Do not flatten the watched source into generic best practices.

Preserve:

- ordering
- terminology
- materials or tools
- cues for judging success
- failure modes
- timing windows
- visual indicators
- style or taste constraints

If the watched source is opinionated, let the learned skill stay opinionated.

## Example Shape

If the source is "agent watch go learn how to make authentic fettuccine", the resulting skill should not become a broad pasta skill.

It should instead preserve things like:

- the exact dough ratio used
- whether the chef rested the dough and for how long
- whether the sheet thickness was visibly demonstrated
- the cue used to judge texture
- the pan-finishing sequence
- the specific avoid-these-mistakes guidance

That is what makes the new skill learned rather than generic.

## Installation

Default install location:

- `~/.codex/skills/<skill-name>`

If also keeping the learned skill in the repo, write it under:

- `/Users/deepsaint/Desktop/work/my-skills/<skill-name>`

Then sync or copy it into `~/.codex/skills/<skill-name>` so it is available locally.
