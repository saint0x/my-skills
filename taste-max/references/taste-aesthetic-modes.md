# Taste Aesthetic Modes

Use this reference after the main design read when the brief calls for a specific visual posture or image-first workflow. Pick one dominant mode. Do not blend modes unless the brief clearly asks for a hybrid.

## Core Dials

For taste-sensitive frontend work, set:

- `DESIGN_VARIANCE`: 1 means symmetric and conventional, 10 means highly art-directed and asymmetric.
- `MOTION_INTENSITY`: 1 means static plus hover states, 10 means cinematic scroll choreography.
- `VISUAL_DENSITY`: 1 means gallery-airy, 10 means cockpit-dense.

Default for marketing/portfolio work: `8 / 6 / 4`.

Adjust down for regulated, public-sector, form-heavy, accessibility-critical, or utilitarian workflows. Adjust up for agency, portfolio, editorial, launch, and art-directed brand surfaces.

## Soft Premium

Use for calm, high-end SaaS, AI, consumer, health, real estate, agency, or portfolio pages that should feel expensive without becoming loud.

Good signals:

- "premium", "Apple-y", "Linear-tier", "soft", "cinematic", "Awwwards", "luxury but modern"

Rules:

- Use generous section spacing and oversized, controlled typography.
- Prefer distinctive sans families such as Geist, Satoshi, Cabinet Grotesk, Outfit, Clash Display, or Plus Jakarta Sans.
- Avoid generic Inter/Roboto/Open Sans unless the existing system requires them.
- Use nested physical-feeling containers only when they clarify hierarchy; avoid cards inside cards.
- Use tactile CTAs with clear contrast and pressed/hover feedback.
- Motion should feel weighted: custom easing or spring behavior, transform/opacity only, reduced-motion fallback.
- Blur belongs on fixed/sticky overlays, not large scrolling content.

Common failures:

- Generic gray borders plus default shadows.
- Standard three-card feature rows.
- Large decorative glow blobs standing in for actual art direction.
- Every section using the same centered headline pattern.

## Minimalist Editorial

Use for Notion/Linear-like product pages, editorial tools, writing surfaces, calm portfolios, docs-adjacent marketing, and quiet premium utility.

Rules:

- Keep palette restrained: off-white or white surfaces, charcoal text, subtle borders, one muted accent.
- Prefer flat structure, precise typography, and whitespace over dramatic shadows.
- Cards use small radii, usually 8px to 12px, and only when hierarchy needs a container.
- No gradients, neon, heavy shadows, or glassmorphism except a subtle nav blur when useful.
- Use sentence-case copy, realistic content, and strong max-width discipline for paragraphs.
- Motion is quiet: small fade/translate reveals, subtle active states, no spectacle.

Common failures:

- Mistaking empty text-only pages for minimalism.
- Warm beige plus brass as the automatic "premium" palette.
- Overusing pills and tiny uppercase labels.

## Industrial Brutalism

Use only when the brief asks for brutalist, tactical, declassified, Swiss industrial, CRT, terminal, mechanical, manufacturing, aerospace, or raw experimental energy.

Choose one substrate and commit:

- Swiss Industrial Print: light paper substrate, carbon ink, one red accent, visible rigid grids.
- Tactical Telemetry: dark CRT substrate, mono-dominant data, red accent, optional single green status readout.

Rules:

- Typography is structural: huge compressed sans headers plus tight technical mono metadata.
- Use CSS Grid, visible compartment lines, 90-degree corners, and hard spatial discipline.
- Avoid gradients, soft shadows, modern translucency, and rounded cards.
- Texture can come from scanlines, halftone, grain, or 1-bit image treatment, but it must not harm readability.
- Use semantic technical elements such as `data`, `samp`, `kbd`, `output`, and `dl` when building telemetry.

Common failures:

- Mixing light Swiss print and dark CRT in one page.
- Adding soft SaaS cards or rounded pill CTAs.
- Using crosshairs and barcode strips as empty decoration instead of structural devices.

## Brandkit

Use for brand guideline boards, logo systems, identity decks, moodboards, and brand-world images.

Rules:

- Treat the board as a visual argument, not a decorative collage.
- Infer category, audience, promise, cultural position, trust level, core metaphor, and what the brand must avoid.
- Logo marks must be simple, symbolic, scalable, balanced, and meaning-based.
- Default to a clean 3 by 3 or 2 by 3 presentation grid with consistent gutters and sparse labels.
- Show the system across touchpoints: mark, wordmark, palette, type, UI/application, imagery, detail, and texture.
- Prefer one core metaphor with one optional fusion. Do not stack random symbols.

Common failures:

- Generic crests, meaningless sparks, copied famous marks, clipart icons.
- Moodboards with unrelated images and no strategic spine.
- Too much text for an image board.

## Image-First Web

Use when the user wants a premium website comp, a highly visual implementation, or an image-to-code workflow.

Rules:

- Generate image references first when image generation is available and the task is visual.
- Prefer one clear horizontal image per section. Do not cram an entire website into one unreadable board.
- For implementation, deeply inspect the generated images before coding: palette, type scale, spacing, grid, asset placement, radius, shadows, button states, responsive implications.
- Generate fresh detail images for sections that need clarity instead of cropping from a previous board.
- Use the image as source of truth, then translate it into real responsive frontend.

Common failures:

- Skipping image generation and relying on vague taste.
- Producing a pretty image that is too compressed to inspect.
- Reinterpreting the image loosely during coding.
- Building fake screenshots from styled divs.

## Mobile Image Direction

Use for mobile app screen concepts and flow images only. Do not use this mode to write code.

Rules:

- Pick platform mode first: iOS-native premium, Android-native premium, or cross-platform neutral.
- Generate enough screens for the flow to feel real.
- Keep text readable at normal viewing size.
- Use safe-area-aware composition and coherent navigation.
- Default to a subtle premium device mockup, but the app content must remain the focus.
- Maintain one palette and one product system across the screen set.

Common failures:

- Phone-sized websites.
- One strong first screen followed by filler screens.
- Random fintech charts, tiny text, and inconsistent device framing.

## Redesign Mode

Use when working on an existing site or app.

First classify:

- Greenfield: no existing visual system or overhaul approved.
- Preserve: modernize without changing recognizability.
- Overhaul: new visual language while preserving content and IA.

Audit before editing:

- Current brand tokens, typography, colors, radii, spacing, and imagery.
- IA, routes, navigation labels, and key conversion paths.
- Existing accessibility wins and failure points.
- Generic patterns to retire.
- SEO and analytics risks.

Modernize in this order:

1. Typography refresh.
2. Color and surface cleanup.
3. Hover, focus, active, loading, empty, and error states.
4. Layout rhythm and spacing.
5. Component replacement.
6. Motion layer.
7. Full block replacement only when necessary.

Never silently change route slugs, nav labels, form field names/order, brand wordmarks, legal copy, consent copy, or analytics hook names.

## Full Output Pressure

Use when the task asks for complete files, components, sections, or exhaustive artifacts.

Rules:

- Count the requested deliverables before producing.
- Do not use placeholders for omitted code or content.
- Do not write "the rest follows" when the rest was requested.
- If output is too long, stop at a clean breakpoint and resume cleanly when asked.

## Stitch / Design.md Export

Use when the output is a semantic design-system file for a generator such as Google Stitch.

The exported `DESIGN.md` should include:

- Visual atmosphere and dials.
- Palette with descriptive names, exact values, and functional roles.
- Typography rules and banned defaults.
- Component styling rules.
- Layout principles and responsive behavior.
- Motion intent.
- Anti-patterns.

Keep it semantic and agent-readable rather than implementation-code-heavy.

## Upstream Source Material

If a mode needs more detail than this router provides, read only the relevant upstream file under:

- [upstream-taste/skills/taste-skill/SKILL.md](upstream-taste/skills/taste-skill/SKILL.md)
- [upstream-taste/skills/gpt-tasteskill/SKILL.md](upstream-taste/skills/gpt-tasteskill/SKILL.md)
- [upstream-taste/skills/redesign-skill/SKILL.md](upstream-taste/skills/redesign-skill/SKILL.md)
- [upstream-taste/skills/soft-skill/SKILL.md](upstream-taste/skills/soft-skill/SKILL.md)
- [upstream-taste/skills/minimalist-skill/SKILL.md](upstream-taste/skills/minimalist-skill/SKILL.md)
- [upstream-taste/skills/brutalist-skill/SKILL.md](upstream-taste/skills/brutalist-skill/SKILL.md)
- [upstream-taste/skills/brandkit/SKILL.md](upstream-taste/skills/brandkit/SKILL.md)
- [upstream-taste/skills/image-to-code-skill/SKILL.md](upstream-taste/skills/image-to-code-skill/SKILL.md)
- [upstream-taste/skills/imagegen-frontend-web/SKILL.md](upstream-taste/skills/imagegen-frontend-web/SKILL.md)
- [upstream-taste/skills/imagegen-frontend-mobile/SKILL.md](upstream-taste/skills/imagegen-frontend-mobile/SKILL.md)
- [upstream-taste/skills/stitch-skill/SKILL.md](upstream-taste/skills/stitch-skill/SKILL.md)
- [upstream-taste/skills/output-skill/SKILL.md](upstream-taste/skills/output-skill/SKILL.md)
