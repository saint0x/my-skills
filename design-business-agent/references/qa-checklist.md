# Quality Assurance

Before considering a project complete, inspect all five categories. Do not ship known sloppiness merely because the page technically works.

## Self-QA Through Aegis

Aegis is the studio's own real browser, not just a research tool — run the finished page through it before calling a project done, the same runtime used for research browsing.

- **Self-QA (functional/structural):** `aegis --mode headless serve --detach`, then `aegis navigate <deployed-url>` followed by `page inspect`, `page actions`, `page text --scope main`, `page forms`, and `page links` against the live page. This confirms the deployed page actually renders, navigates, exposes the CTAs and forms you intended, and reads correctly — a real end-to-end check, not just "the build succeeded."
- **Visual UI testing:** run the same navigate against `--mode headful` to open a real, visible rendered browser window on the live URL and eyeball it directly — this is how layout, spacing, imagery, and animation get checked against an actual browser engine rather than assumed from code. Resize that window (or reload with the runtime's viewport set) to mobile, tablet, and desktop widths in turn so the visual pass covers every breakpoint, not just the one the dev machine happens to be at.
- **Performance smoke check:** treat a clean `navigate` + `page inspect` round trip through Aegis against the live deployed URL (not localhost) as the real-world load/render check — if the page is slow or hangs through Aegis on the actual network path, it will be slow for a visitor too. This catches real loading and responsiveness regressions; for hard numbers (Core Web Vitals, bundle size, memory profiling) still use the browser's own devtools or the project's build-level performance tooling — Aegis's job here is proving the page genuinely works end-to-end, not producing a metrics report.

Do not consider the QA gate passed on dev-server output alone — the Aegis pass against the actual deployed URL is what confirms the client's real experience, not just what worked locally.

### Visual

- typography
- spacing
- hierarchy
- alignment
- imagery
- animation
- transitions
- responsive behavior

### Functional

- navigation
- links
- forms
- buttons
- validation
- interactive states
- error states

### Performance

- loading
- responsiveness
- layout stability
- media weight
- JavaScript
- animation smoothness
- memory behavior

### Conversion

- proposition clarity
- CTA visibility
- trust
- objections
- proof
- friction
- mobile conversion path

### Technical

- console errors
- broken assets
- browser compatibility
- metadata
- semantic structure
- accessibility

## Engineering Judgment Checklist

Whenever confronted with a visual idea, ask:

1. What experience are we actually trying to create?
2. What is the simplest reliable implementation?
3. What does it cost in bytes?
4. What does it cost in CPU/GPU?
5. What happens on mobile?
6. What happens on slow networks?
7. What happens when JavaScript fails?
8. Can we achieve 95% of the visual result at 20% of the computational cost?
9. Can the asset be cached?
10. Does this materially improve the experience?

Optimize the experience, not the cleverness of the implementation.

## Continuous Improvement

Every project should improve the production system. When you discover a better rendering technique, a stronger media pipeline, a useful animation primitive, a performance optimization, a better conversion pattern, a stronger research source, a better generative model, or a recurring failure mode — capture the lesson and fold it into [component-architecture.md](component-architecture.md) or [workflow-playbook.md](workflow-playbook.md) for future projects. The studio should compound knowledge, not relearn the same lesson per client.
