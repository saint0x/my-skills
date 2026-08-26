---
name: emil-deign-skill
description: Use Emil Kowalski's design engineering skill bundle for tasteful UI, animation, prototypes, Apple-style motion, Sonner, Swift, UI-library choices, and high-quality generated header images or animated hero media. Use for design engineering work where restraint, precise motion values, polished generated media, and implementation quality matter.
---

# Emil Deign Skill

An aggregate local skill built from Emil Kowalski's design and animation skill set, plus one added skill for high-quality generated header imagery and animated hero media.

The posture is simple: taste is trained, not guessed. Motion and imagery earn their place by making the interface clearer, more direct, more memorable, or less jarring. If the best answer is no animation or no generated media, say that and build the quieter thing.

## Source

The upstream files from `https://github.com/emilkowalski/skills/tree/main/skills` are preserved under [skills/](skills/) with the upstream MIT license included in [LICENSE](LICENSE). Treat those nested files as the authoritative instructions for their modes.

## Routing

When a request matches one of these modes, read that nested `SKILL.md` completely before acting. If it references local files such as `RECIPES.md`, `STANDARDS.md`, `AUDIT.md`, `PLAN-TEMPLATE.md`, `PICKER.md`, or `API.md`, read those only when the nested skill says they are needed.

| Need | Read |
| --- | --- |
| General UI polish, design engineering philosophy, component details | [skills/emil-design-eng/SKILL.md](skills/emil-design-eng/SKILL.md) |
| Build a web animation | [skills/animate/SKILL.md](skills/animate/SKILL.md) |
| Build React Native / Expo animation | [skills/animate-expo/SKILL.md](skills/animate-expo/SKILL.md) |
| Review animation code | [skills/review-animations/SKILL.md](skills/review-animations/SKILL.md) |
| Audit and plan animation improvements | [skills/improve-animations/SKILL.md](skills/improve-animations/SKILL.md) |
| Find places where motion would help | [skills/find-animation-opportunities/SKILL.md](skills/find-animation-opportunities/SKILL.md) |
| Name a motion effect precisely | [skills/animation-vocabulary/SKILL.md](skills/animation-vocabulary/SKILL.md) |
| Apple-style fluid interfaces, gestures, springs, materials | [skills/apple-design/SKILL.md](skills/apple-design/SKILL.md) |
| Multiple live UI variants with a picker | [skills/prototype/SKILL.md](skills/prototype/SKILL.md) |
| Sonner toast setup, styling, and troubleshooting | [skills/ask-sonner/SKILL.md](skills/ask-sonner/SKILL.md) |
| Choose a UI library instead of hand-rolling primitives | [skills/pick-ui-library/SKILL.md](skills/pick-ui-library/SKILL.md) |
| Modern Swift | [skills/write-swift/SKILL.md](skills/write-swift/SKILL.md) |
| Generate premium header images, then animate or integrate them into a website | [skills/header-image-animation/SKILL.md](skills/header-image-animation/SKILL.md) |

## Operating Rules

- Prefer the most specific nested skill. Do not load every file by default.
- When implementing, follow the existing project stack, tokens, and component conventions first.
- When using external generation APIs, verify the current model schema and costs before making calls. Do not expose API keys in client-side code.
- For motion, keep Emil's hard bar: purpose first, frequency gate second, exact values third, implementation last.
- For generated media, the asset is not the deliverable by itself. The deliverable is the asset integrated into the page with good composition, responsive crops, performance, fallbacks, and reduced-motion behavior.
