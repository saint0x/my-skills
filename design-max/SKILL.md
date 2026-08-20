---
name: design-max
description: Design product UI, UX systems, multimodal app surfaces, strategic slides, banners, social creatives, and media advertising with data-backed visual direction. Use when Codex needs searchable design intelligence for apps, websites, dashboards, landing pages, design tokens, typography, color systems, responsive layout, accessibility polish, Chart.js slide logic, shadcn or Tailwind implementation, ad creatives, social images, hero banners, or presentation storytelling where visual quality and conversion impact both matter.
---

# Design Max

Use this skill when the work is visual, interaction-heavy, or persuasion-heavy.

This skill combines:

- product UI and UX search intelligence
- stack-aware implementation guidance
- slide strategy and presentation logic
- token and design-system structure
- ad creative and social-asset direction

## Resolve `SKILL_DIR`

Before using any bundled script, resolve `SKILL_DIR` as the absolute path of the directory containing this `SKILL.md`.

All bundled commands assume:

```bash
SKILL_DIR="<absolute path to the directory containing this SKILL.md>"
```

## Core Workflow

1. Identify the visual job type.
2. Use the bundled search engine to generate a visual direction or design system.
3. Load only the references needed for that job.
4. Apply token, layout, typography, interaction, and accessibility rules consistently.
5. For slides or ad creatives, use the dedicated references and slide-search logic instead of improvising from generic UI instincts.

## Routing

### Product UI, app UI, websites, dashboards, and software UX

Start with:

```bash
python3 "$SKILL_DIR/scripts/search.py" "<product type> <industry> <keywords>" --design-system
```

Then supplement with focused searches:

```bash
python3 "$SKILL_DIR/scripts/search.py" "<query>" --domain style|color|typography|ux|landing|icons|chart|gsap
python3 "$SKILL_DIR/scripts/search.py" "<query>" --stack react|nextjs|vue|svelte|swiftui|react-native|flutter|html-tailwind|shadcn|angular|laravel|threejs
```

Read as needed:

- [references/quick-reference.md](references/quick-reference.md)
- [references/pro-rules.md](references/pro-rules.md)
- [references/shadcn-components.md](references/shadcn-components.md)
- [references/shadcn-theming.md](references/shadcn-theming.md)
- [references/shadcn-accessibility.md](references/shadcn-accessibility.md)
- [references/tailwind-utilities.md](references/tailwind-utilities.md)
- [references/tailwind-responsive.md](references/tailwind-responsive.md)
- [references/tailwind-customization.md](references/tailwind-customization.md)
- [references/canvas-design-system.md](references/canvas-design-system.md)

### Slides, decks, presentations, and narrative product storytelling

Use the slide search logic:

```bash
python3 "$SKILL_DIR/scripts/search-slides.py" "investor pitch"
python3 "$SKILL_DIR/scripts/search-slides.py" "problem slide" --context --position 2 --total 9
```

Use token and slide helpers when needed:

```bash
node "$SKILL_DIR/scripts/generate-tokens.cjs" --config "$SKILL_DIR/assets/templates/design-tokens-starter.json" -o tokens.css
python3 "$SKILL_DIR/scripts/slide-token-validator.py" <slide-html>
python3 "$SKILL_DIR/scripts/generate-slide.py" --help
```

Read as needed:

- [references/create.md](references/create.md)
- [references/layout-patterns.md](references/layout-patterns.md)
- [references/html-template.md](references/html-template.md)
- [references/copywriting-formulas.md](references/copywriting-formulas.md)
- [references/slide-strategies.md](references/slide-strategies.md)
- [references/token-architecture.md](references/token-architecture.md)
- [references/primitive-tokens.md](references/primitive-tokens.md)
- [references/semantic-tokens.md](references/semantic-tokens.md)
- [references/component-tokens.md](references/component-tokens.md)
- [references/component-specs.md](references/component-specs.md)
- [references/states-and-variants.md](references/states-and-variants.md)
- [references/tailwind-integration.md](references/tailwind-integration.md)

### Ad creatives, social creatives, banners, thumbnails, and media advertising

Still start with `search.py` for style, color, typography, and product reasoning, then apply the creative-specific references:

- [references/banner-sizes-and-styles.md](references/banner-sizes-and-styles.md)
- [references/social-photos-design.md](references/social-photos-design.md)

Use the design engine to choose:

- art direction
- message hierarchy
- CTA placement
- safe zones
- platform sizing
- visual tone

Do not treat ad creative as a generic landing-page crop. Respect platform-specific dimensions, text density, safe zones, and thumbnail readability.

## Working Rules

- Use the design-system search first for new visual surfaces.
- Prefer one strong visual direction over averaging many styles together.
- Keep token usage consistent once a direction is chosen.
- Respect accessibility and performance constraints even when the goal is highly visual.
- Use stack guidance when implementation details matter.
- Use slide logic for presentation sequencing, not only visual styling.
- Use creative-specific references for banners and social images instead of guessing dimensions or composition rules.

## Validation

Smoke-test bundled scripts before relying on them for a task:

```bash
python3 "$SKILL_DIR/scripts/search.py" "saas dashboard modern" --design-system
python3 "$SKILL_DIR/scripts/search-slides.py" "investor pitch"
python3 "$SKILL_DIR/scripts/validate_data.py"
```

If token generation or validation is needed:

```bash
node "$SKILL_DIR/scripts/validate-tokens.cjs" --help
node "$SKILL_DIR/scripts/embed-tokens.cjs" --help
```

## Read Next

Read [references/provenance.md](references/provenance.md) if you need the upstream source lineage for this bundled skill.
