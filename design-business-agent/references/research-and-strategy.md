# Research and Strategy

## Research Before Designing

Never assume existing knowledge represents current best practice. For every substantial project, research the current state of: the client's industry, the client's competitors, category-leading websites, high-performing landing pages in the niche, current conversion practices, current interface patterns, contemporary visual language, consumer expectations, mobile behavior, current frontend capabilities, current browser capabilities, accessibility expectations, current performance practices.

When reliable information exists, investigate conversion benchmarks and behavioral research relevant to the niche.

Distinguish between:

- **evidence** — supported by experiments, behavioral research, analytics, or credible case studies
- **heuristics** — generally useful conversion principles
- **trends** — currently fashionable visual or interaction patterns
- **taste** — aesthetic judgment

Do not confuse one for another. Research informs the work. It does not dictate it.

## Standing Inspiration Source

Always check [refero.design](https://refero.design/) during research — it's the studio's default source for premium landing-page and web-design inspiration, alongside whatever live competitor/category sites the project calls for. Treat what you find there as **trend and taste input**, not evidence — pull directional cues (composition, motion language, hero patterns) from it, but still ground the actual conversion structure in the visitor's journey below, not in whatever looks good on a gallery site.

Browse it (and any live competitor site) with the local Aegis CLI — see [Browser Tooling](#browser-tooling) below — rather than reasoning from memory or a static screenshot alone.

## Browser Tooling

The studio agent has its own browser via the local `aegis` CLI — use it for research crawls, not just QA. Typical flow:

```bash
aegis --mode headless serve --addr 127.0.0.1:7878 --detach
aegis --server-addr 127.0.0.1:7878 navigate https://refero.design/
aegis --server-addr 127.0.0.1:7878 page text --scope main
aegis --server-addr 127.0.0.1:7878 page find <what you're looking for>
aegis --server-addr 127.0.0.1:7878 search <query>
```

Use `navigate` + `page text`/`page find`/`page open-link` to actually read competitor and inspiration sites rather than guessing at their content, and `search` for general web research from inside the same runtime. This is the same runtime taste-max points to for verifying real browser behavior — reuse one running `serve` instance across a research pass instead of starting a new one per lookup.

## Understand the User Before the Interface

Before designing, determine:

- Who is arriving?
- Where did they come from?
- What do they already know?
- What do they want?
- What are they afraid of?
- What objections exist?
- What information would increase confidence?
- What action should they take?
- What is that action economically worth?
- What must they understand before taking it?

Design the information architecture around this journey. The landing page is not a collection of sections. It is a deliberately constructed sequence of beliefs.

A useful abstraction: **Attention → Understanding → Desire → Trust → Objection Resolution → Action.**

Every section must have a job. If a section does not advance the visitor toward understanding, confidence, desire, or action, question why it exists.

## Conversion Psychology

Understand and deliberately apply: information hierarchy, cognitive load reduction, processing fluency, visual salience, attention direction, social proof, authority, specificity, credibility, risk reversal, loss aversion, anchoring, contrast, framing, commitment, consistency, progressive disclosure, curiosity, uncertainty reduction, objection handling, urgency when legitimate, scarcity when legitimate.

Never manufacture false scarcity, fake testimonials, fabricated statistics, deceptive urgency, or misleading social proof. High conversion should come from superior communication — not deception.

## Instrumentation

When appropriate, make conversion surfaces measurable. Track meaningful interactions such as: CTA clicks, form starts, form completion, checkout progression, scheduling, important section engagement, qualified lead events.

Do not measure everything simply because it can be measured. Analytics should answer business questions.
