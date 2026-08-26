# Taste Max Provenance

Taste Max merges the local Design Max engine with upstream Taste Skill material.

The Design Max side was extracted and reformatted from:

- repo: `https://github.com/nextlevelbuilder/ui-ux-pro-max-skill`
- commit: `bc826e2267a36d98a2dcf5231e16c30ff546770f`

Vendored source areas:

- `.claude/skills/ui-ux-pro-max`
- `.claude/skills/design-system`
- `.claude/skills/ui-styling`
- selected references from `.claude/skills/design`
- selected references from `.claude/skills/slides`

The Design Max side intentionally focuses on:

- product UI and UX intelligence
- multimodal visual systems
- slide and deck logic
- design tokens and implementation guidance
- banner and social creative direction

It does not attempt to vendor the entire upstream repository surface such as the gallery app, docs site, CI workflows, or unrelated packaging machinery.

The Taste side was cannibalized from:

- repo: `https://github.com/Leonxlnx/taste-skill`
- cloned during this merge as a shallow checkout
- retained source: [upstream-taste/skills](upstream-taste/skills)
- retained research: [upstream-taste/research](upstream-taste/research)

Taste contributes the anti-slop frontend posture, brief inference, design dials, aesthetic modes, image-first workflow, redesign discipline, AI-tell bans, and full-output pressure.
