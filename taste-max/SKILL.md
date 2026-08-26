---
name: taste-max
description: Design premium, non-generic product UI, websites, dashboards, brands, slides, social creatives, and image-first interfaces by combining Taste Skill's strict anti-slop art direction with Design Max's searchable design intelligence, token systems, stack guidance, and presentation logic. Use for visual, interaction-heavy, or persuasion-heavy work where both taste and implementation quality matter; do not use for unrelated backend, data, or infrastructure tasks.
---

# Taste Max

Taste Max is the merged successor to `design-max` and the Taste Skill family.

Use it when the work has a meaningful visual, interaction, brand, presentation, or conversion surface. The core posture is Taste first, evidence second, implementation third:

1. Read the brief and infer the visual job.
2. Choose the strictest applicable mode and state the design read.
3. Use the bundled Design Max search/data tools for grounding.
4. Load only the references needed for that mode.
5. Ship the full artifact with visual polish, accessibility, responsive behavior, and stack correctness.

## Resolve `SKILL_DIR`

Before using any bundled script, resolve `SKILL_DIR` as the absolute path of the directory containing this `SKILL.md`.

```bash
SKILL_DIR="<absolute path to the directory containing this SKILL.md>"
```

## Design Read

Before making visual decisions, state one concise line:

```text
Reading this as: <surface type> for <audience>, with a <visual language>, leaning toward <system or aesthetic family>.
```

If that read could go two genuinely different ways, ask one clarifying question. Otherwise proceed.

## Mode Boundaries

### 1. Taste Frontend

Use for landing pages, portfolios, editorial pages, marketing sites, product pages, and redesigns where the first impression matters.

Start with:

```bash
python3 "$SKILL_DIR/scripts/search.py" "<page type> <industry> <visual language>" --design-system
python3 "$SKILL_DIR/scripts/search.py" "<query>" --domain style|color|typography|ux|landing|icons|gsap
python3 "$SKILL_DIR/scripts/search.py" "<query>" --stack react|nextjs|vue|svelte|astro|html-tailwind|shadcn|threejs
```

Read:

- [references/taste-frontend.md](references/taste-frontend.md)
- [references/taste-aesthetic-modes.md](references/taste-aesthetic-modes.md) when the brief names minimalist, soft premium, brutalist, brandkit, image-to-code, or mobile image direction
- [references/pro-rules.md](references/pro-rules.md)
- [references/quick-reference.md](references/quick-reference.md)
- Stack-specific references only when implementation details matter

Strict boundary: Taste Frontend is not the right primary mode for dense dashboards, multi-step app workflows, data tables, code editors, or native mobile implementation. For those, use Product UI / App Systems below and apply Taste only to brand, landing, onboarding, empty states, and visual polish.

### 2. Product UI, App Systems, Dashboards, And Tools

Use when the surface is a software product, admin panel, SaaS dashboard, internal tool, editor, settings surface, or repeated workflow.

Start with:

```bash
python3 "$SKILL_DIR/scripts/search.py" "<product type> <industry> <keywords>" --design-system
python3 "$SKILL_DIR/scripts/search.py" "<query>" --domain style|color|typography|ux|icons|chart
python3 "$SKILL_DIR/scripts/search.py" "<query>" --stack react|nextjs|vue|svelte|swiftui|react-native|flutter|html-tailwind|shadcn|angular|laravel|threejs
```

Read as needed:

- [references/design-routing.md](references/design-routing.md)
- [references/canvas-design-system.md](references/canvas-design-system.md)
- [references/component-specs.md](references/component-specs.md)
- [references/states-and-variants.md](references/states-and-variants.md)
- [references/shadcn-components.md](references/shadcn-components.md)
- [references/shadcn-theming.md](references/shadcn-theming.md)
- [references/shadcn-accessibility.md](references/shadcn-accessibility.md)
- [references/tailwind-utilities.md](references/tailwind-utilities.md)
- [references/tailwind-responsive.md](references/tailwind-responsive.md)
- [references/tailwind-customization.md](references/tailwind-customization.md)

System boundary: if the brief maps to Fluent, Material, Carbon, Polaris, Atlassian, Primer, GOV.UK, USWDS, Bootstrap, Radix, or shadcn/ui, prefer the real package and its official patterns. Do not fake a design system by hand when an official one is the point.

### 3. Design Systems And Tokens

Use when creating, auditing, or implementing token architecture, themes, component contracts, Tailwind integration, or reusable visual systems.

Use token helpers when useful:

```bash
node "$SKILL_DIR/scripts/generate-tokens.cjs" --config "$SKILL_DIR/assets/templates/design-tokens-starter.json" -o tokens.css
node "$SKILL_DIR/scripts/validate-tokens.cjs" --help
node "$SKILL_DIR/scripts/embed-tokens.cjs" --help
```

Read:

- [references/token-architecture.md](references/token-architecture.md)
- [references/primitive-tokens.md](references/primitive-tokens.md)
- [references/semantic-tokens.md](references/semantic-tokens.md)
- [references/component-tokens.md](references/component-tokens.md)
- [references/tailwind-integration.md](references/tailwind-integration.md)

### 4. Slides, Decks, And Narrative Storytelling

Use for strategic decks, presentation slides, pitch narratives, Chart.js slide logic, and story sequencing.

Start with:

```bash
python3 "$SKILL_DIR/scripts/search-slides.py" "investor pitch"
python3 "$SKILL_DIR/scripts/search-slides.py" "problem slide" --context --position 2 --total 9
python3 "$SKILL_DIR/scripts/slide-token-validator.py" <slide-html>
python3 "$SKILL_DIR/scripts/generate-slide.py" --help
```

Read:

- [references/create.md](references/create.md)
- [references/layout-patterns.md](references/layout-patterns.md)
- [references/html-template.md](references/html-template.md)
- [references/copywriting-formulas.md](references/copywriting-formulas.md)
- [references/slide-strategies.md](references/slide-strategies.md)
- [references/token-architecture.md](references/token-architecture.md)

### 5. Ads, Social Creatives, Banners, Thumbnails

Use for platform-specific creative, campaigns, thumbnails, banners, social assets, and media advertising.

Start with `search.py` for style, color, typography, and product reasoning, then read:

- [references/banner-sizes-and-styles.md](references/banner-sizes-and-styles.md)
- [references/social-photos-design.md](references/social-photos-design.md)

Do not treat ad creative as a landing-page crop. Respect platform dimensions, safe zones, thumbnail readability, message hierarchy, and CTA placement.

### 6. Image-First Web, Mobile Concepts, And Brand Kits

Use when image generation is the design source of truth: web comps, mobile flows, brand boards, or image-to-code workflows.

Read:

- [references/taste-aesthetic-modes.md](references/taste-aesthetic-modes.md)

If image generation is available and the user asks for a visual website, comp, brand board, or mobile screen, generate section-specific or screen-specific images before implementation unless the user explicitly asks to skip images.

## Taste Rules That Always Matter

- One strong visual direction beats averaging multiple trends.
- State the design read and choose dials for variance, motion, and density when doing taste-sensitive frontend work.
- Avoid generic AI tells: default purple-blue glows, centered dark mesh heroes, three equal feature cards, fake dashboards made from divs, section-number eyebrows, decorative status dots, invented precision metrics, and "elevate/seamless/unleash" copy.
- Use real assets or generated assets for visual websites. Text plus decorative gradients is not a finished hero.
- Use one accent system, one shape system, and one page theme unless the brief explicitly calls for a controlled exception.
- Buttons, forms, focus states, loading states, empty states, and error states must be designed, not left as browser defaults.
- Motion must communicate hierarchy, storytelling, feedback, or state change. Honor reduced motion and animate only transform/opacity for high-frequency animation.
- For implementation, check existing dependencies before importing new packages.
- For existing projects, audit before changing. Preserve IA, routes, nav labels, brand wordmark, legal copy, form field names, analytics hooks, and accessibility wins unless the user explicitly approves changes.

## Validation

Smoke-test the engine before relying on it:

```bash
python3 "$SKILL_DIR/scripts/search.py" "saas dashboard modern" --design-system
python3 "$SKILL_DIR/scripts/search.py" "premium editorial landing page" --domain typography
python3 "$SKILL_DIR/scripts/search-slides.py" "investor pitch"
python3 "$SKILL_DIR/scripts/validate_data.py"
```

For frontend delivery, run the project's available checks and visually inspect responsive viewports. For browser behavior, use the local Aegis CLI when available.

## Source Lineage

Taste Max cannibalizes:

- local `design-max`: data-backed search, stack guidance, token architecture, slide logic, ad/social references, and helper scripts
- `Leonxlnx/taste-skill`: anti-slop frontend discipline, brief inference, design dials, AI-tell bans, image-first workflow, aesthetic submodes, redesign audit discipline, and full-output pressure

Read [references/provenance.md](references/provenance.md) for upstream Design Max lineage.
