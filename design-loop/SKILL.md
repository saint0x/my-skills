---
name: design-loop
description: Run a fresh-context design critique loop for important UI, visual, document, animation, or hero-asset work by interviewing, extracting a checkable reference bar, then iterating builder output through independent critics until the piece wins.
metadata:
  short-description: Fresh-context design critique loop
---

# Design Loop

Use this skill when the user wants a design loop, critic loop, gauntlet loop, iterative taste loop, or asks to improve an important visual artifact against a real-world reference. This is best for hero assets, landing pages, flagship screens, carousels, motion pieces, brand moments, PDFs, or other work where taste and visual judgment matter enough to justify a token-heavy process.

The method is adapted from Matt Shumer's Gauntlet Loop. The core idea: the context that builds a piece should not be the context that grades it. Fresh-context critics judge rendered output, not builder intent.

## When To Use

Use this skill for high-leverage design work where the user wants a stronger result than a single-pass implementation or review. Do not use it for routine bug fixes, broad whole-site redesigns, or large multi-surface projects unless the user explicitly accepts the cost. If the scope is broad, choose or ask for the hero piece first.

Default to three or four pieces at most. Every extra piece multiplies builder and critic work.

## Phase 1: Interview

Ask these three questions together, then wait:

1. What are you building, and how long or how big?
2. Name something that already does this brilliantly. A site, video, document, app screen, deck, or other reference I can open. If nothing comes to mind, say skip.
3. Any files I should work from, such as a design system, brand doc, script, existing draft, screenshots, or source files?

If the reference is vague, push once for a specific URL, file, page, screen, or timestamp. A vague bar makes the critic invent the comparison and approve weak work.

If the user says skip for the reference, propose three strong candidate bars with one line each explaining why each would be a hard reference. Wait when practical. If the user does not choose and the work can proceed, take the hardest relevant bar and say so.

## Phase 2: Preflight

Before building, verify the loop can actually judge the work. Report the preflight in one concise block:

- Fetch or open the reference. Screenshot visual references, read document references, or capture frames for motion/video references. If the reference is blocked or missing, ask for another.
- Confirm the output can be rendered: screenshots for a site or app, frames/filmstrip for animation or video, PDF render for documents, image export for visual assets.
- Name any generation tools required, such as image, video, voice, browser, screenshot, design, or rendering tools, and whether they are available.
- Confirm input files exist, including `design-system.md`, brand docs, scripts, existing drafts, screenshots, or source files.

Then state what is working, what is missing, and which critic would be blind if something is missing. Do not continue quietly with a critic that cannot see the evidence it needs.

## Phase 3: Teardown

Study the reference before building. Write 5 to 7 concrete mechanisms to `bar.md` in the active workspace or project artifact directory.

Mechanisms must be checkable by looking at the rendered output. Avoid adjectives.

Useful mechanisms look like:

- Headline is about 5x body size, with no more than three type sizes visible.
- One accent color appears at most twice per screen.
- Motion resolves in one direction and lasts at least 400 ms.
- Above-the-fold whitespace takes at least 40% of the frame.
- Primary call to action sits inside the first viewport without covering the subject.

Useless mechanisms look like:

- Feels premium.
- Clean and modern.
- Strong hierarchy.
- Good use of whitespace.

Show or summarize `bar.md` before continuing. The user does not need to approve every line unless the reference choice or bar is uncertain, but they should be able to see what the critics will enforce.

## Phase 4: Loop

Split the goal into the smallest independently improvable pieces. For each piece:

1. Send a builder brief that includes the goal, relevant inputs, selected piece, output requirements, and current gap history.
2. Render the result.
3. Run three critics in fresh context, with no knowledge of how the builder worked.
4. If any critic fails, send the single biggest named gap back to the builder and repeat.
5. Exit when all three critics pass, or when the user stops the run.

Critic roles:

- Brief critic: judges only against the user's stated goal. It ignores aesthetics and answers whether the piece does the job.
- System critic: judges only against the design system, brand doc, or explicit local constraints. It checks objective adherence.
- Craft critic: judges rendered output against `bar.md` and the reference. It sees ours next to the reference, with labels stripped where practical, chooses which is better, and names the single biggest gap.

Write each critic brief for the specific goal and artifact. Do not reuse generic critic wording when the medium changes.

## Critic Rules

Critics should be harsh and binary. Use `pass` or `fail`, not scores. Scores drift upward and make the loop soft.

Critics judge rendered output, never code. Reading implementation makes a critic evaluate intent instead of result.

All three critics must pass. Any fail returns to the builder with one highest-impact gap, not a pile of suggestions.

There is no fixed round count. The exit condition is winning the comparison, or the user stopping the loop.

Keep a visible progress note or local progress file with: piece status, each critic verdict, gap history, and round count.

## Cost Controls

Do not pretend to know exact token spend. Report round count, elapsed pieces, and remaining planned pieces.

If the user gives a ceiling, treat it as a checkpoint. Pause and ask before continuing past it. The reliable brake is the user watching the loop and stopping it.

Use the strongest available visual/design judgment for the craft critic. Mechanical checks can use cheaper or faster contexts when available; craft judgment is the one that should not be downgraded.

## Common Failures

- The reference bar is vague.
- The builder judges its own work.
- The critic sees code instead of rendered output.
- The critic gives a score instead of a binary verdict.
- The loop stops at a fixed round count instead of a quality threshold.
- The scope includes too many pieces.
