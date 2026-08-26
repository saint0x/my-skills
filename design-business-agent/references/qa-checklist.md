# Quality Assurance

Before considering a project complete, inspect all five categories. Do not ship known sloppiness merely because the page technically works.

Verify against a real running browser, not just a build log — use the local Aegis CLI (`aegis --mode headless serve --detach`, then `aegis navigate <deployed-url>` and `page text`/`page actions` against the live page) to confirm the deployed page actually renders, navigates, and reads correctly, the same way it's used for research browsing.

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
