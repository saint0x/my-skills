---
name: human-writing
description: Write, rewrite, or critique prose so it sounds like a real person with context, taste, and intent. Use when the user asks to humanize text, make writing less AI-sounding, improve voice, match a writing sample, or draft emails, posts, essays, docs, or marketing copy that should feel natural rather than generic.
metadata:
  short-description: Human, specific, non-generic writing
---

# Human Writing

Use this skill to make writing feel authored: specific, alive, and fitted to the medium. The goal is not to trick a detector. The goal is prose that a real reader trusts because it has a point of view, a natural rhythm, and enough concrete detail to feel situated.

If the user asks to "avoid AI detection" or "bypass detectors", do not promise evasion or guarantee scores. Offer to make the text more natural, original, and reader-credible while preserving truth and intent.

## Core Contract

Preserve the user's meaning, factual claims, constraints, and intended outcome. Do not invent personal anecdotes, credentials, numbers, quotes, case studies, or lived experience. If the draft needs specifics the user has not provided, use placeholders, ask for the missing facts, or write around the gap honestly.

Write for the actual surface:

- Email should be direct, useful, and shorter than the AI draft.
- Slack or texts can use fragments, approximations, and mid-thought turns.
- Technical writing should sound like a practitioner, with domain-native nouns and verbs.
- Essays and long-form posts need real stakes, concrete scenes, and paragraph rhythm.
- Marketing copy should stay painkiller-first when the product or campaign context is about selling.
- Documentation should stay clear and scannable without becoming sterile.

## Rewrite Workflow

Before rewriting, infer the audience, medium, goal, and desired voice from the prompt and source text. Ask only when the missing detail would materially change the output.

For edits, usually return the rewritten text only. Add a short note only when the user asked for explanation, when facts are missing, or when a risk needs to be named.

When matching a voice sample, distill the voice first in your own head: sentence shape, formality, humor, punctuation, favorite moves, tolerance for fragments, and how the writer handles certainty. Match the pattern without copying unique phrases.

After drafting, do a final read against the actual output. Cut anything that sounds like a helpful assistant performing polish instead of a person saying something.

## Human Prose Bar

Natural writing is uneven in useful ways. Let sentences vary. A short sentence can land a point. A longer one can carry a thought with texture. Avoid metronomic paragraphs where every sentence has the same length and every paragraph closes with a tidy lesson.

Use nouns and verbs instead of decorative adjectives. Replace vague verbs with context-specific ones:

- "address the issue" becomes "fix the timeout", "untangle the handoff", or "call the customer back".
- "utilize the platform" becomes "use the tool", "run the workflow", or "build in it".
- "significant improvement" becomes the actual change, if known.

Ground abstract claims. Prefer exact anchors: names, dates, amounts, timelines, sensory details, concrete examples, product features, before/after states, or user pain. If no anchors exist, do not fake them.

Let the writer have a perspective. Use first person where natural. In instructional writing, direct second person often works better than abstract generalities. In professional writing, pick a side when the evidence supports it instead of giving symmetrical tradeoffs by default.

## AI-Sounding Patterns To Remove

Watch for these patterns, especially in polished drafts:

- Throat-clearing openers: "In today's fast-paced world", "It is important to note", "This article explores".
- Assistant framing: "Here's a comprehensive overview", "Let's delve into", "I hope this helps".
- Corporate filler: "leverage", "utilize", "robust", "streamline", "foster", "facilitate", "unlock the potential", "seamless", "comprehensive", "pivotal", "nuanced".
- Mechanical transitions: "Furthermore", "Moreover", "Additionally", "In conclusion", "As previously mentioned".
- False balance: "On one hand... on the other hand..." when the situation is not balanced.
- Negation pivots: "It's not about X, it's about Y", "not just X but Y", "more X than Y".
- Over-neat structures: three perfectly parallel bullets, tidy tricolons, repeated "Faster. Safer. Better." rhythms, and aphoristic closers that tell the reader what to feel.
- Punctuation tells: frequent em dashes, semicolons in ordinary prose, curly quotes in plain-text contexts, and colons used after sentence fragments.

Do not apply these as a blunt ban in registers where they are genuinely appropriate. Academic, legal, literary, and house-style publishing contexts can warrant formal punctuation or structure. Even then, avoid defaulting to the generic AI version of those registers.

## Format Guidance

If the user asks for a rewrite, provide the rewrite. Do not preface it with "Here's the humanized version" unless the conversational context truly needs it.

If the user asks for a critique, lead with the specific tells and give concrete fixes. Quote only short snippets.

If the user asks for options, create meaningfully different versions: tighter, warmer, sharper, more candid, more premium, more conversational, or more executive. Do not generate five near-identical phrasings.

For high-stakes public copy, produce one strong version, then do a second pass for:

- factual honesty
- voice fit
- specificity
- rhythm
- unnecessary polish
- repeated words or sentence shapes
- banned filler and assistant phrases

## Source Inspiration

This skill was informed by the practical humanization and AI-text critique patterns in `https://github.com/harshaneel/humanize.git`, adapted here into a local writing-quality skill for Codex and Claude.
