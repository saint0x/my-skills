# Component Architecture and Reusable Design Systems

Build reusable primitives without making every project look identical.

Reuse **engineering systems** rather than blindly reusing **visual compositions.**

Reusable infrastructure can include: media loaders, typography primitives, animation utilities, scroll controllers, video components, frame-sequence renderers, responsive containers, analytics hooks, form infrastructure, accessibility primitives, performance instrumentation.

The underlying engine should become increasingly powerful while the visual output remains bespoke.

## Reusable Design Systems, Bespoke Art Direction

Treat this as an explicit split, not a tension to resolve case-by-case:

- **What should be a reusable system:** token plumbing (spacing scale, type scale, motion easing curves, breakpoints), the scroll/frame-sequence engine, media loading and compression pipeline, form and validation infrastructure, accessibility primitives (focus management, reduced-motion handling), analytics/event wiring, deploy tooling.
- **What must stay bespoke per client:** the actual color palette, typography choice, imagery/generated assets, copy, composition, and which single effect carries the page.

When starting a new project, first check whether the studio's existing engineering primitives (scroll controller, frame-sequence renderer, media loader, etc.) already solve part of the problem before building new versions. When a genuinely new, reusable primitive is built for one project, treat extracting it into the shared system as part of finishing that project — not a separate task for later. This is how the studio compounds speed across projects instead of re-solving the same engineering problem every time while keeping every client's site visually distinct.
