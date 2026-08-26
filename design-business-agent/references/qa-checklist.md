# Quality Assurance

Before considering a project complete, inspect all five categories. Do not ship known sloppiness merely because the page technically works.

## Self-QA Through Aegis and CUA

Aegis is the studio's own real browser, not just a research tool — run the finished page through it before calling a project done, the same runtime used for research browsing. CUA (`~/Desktop/cua`, a local computer-use runtime — invoke via `cargo run -p cua --` from that directory, or the built binary under `target/<triple>/release/cua` once compiled) supplies the piece Aegis doesn't: an actual pixel screenshot, since Aegis reads and acts on the DOM but has no screenshot command of its own.

- **Self-QA (functional/structural):** `aegis --mode headless serve --detach`, then `aegis navigate <deployed-url>` followed by `page inspect`, `page actions`, `page text --scope main`, `page forms`, and `page links` against the live page. This confirms the deployed page actually renders, navigates, exposes the CTAs and forms you intended, and reads correctly — a real end-to-end check, not just "the build succeeded."
- **Visual UI testing:** open the live URL through Aegis in `--mode headful` so there's a real, visible rendered browser window, then capture it with CUA — `cua serve --addr 127.0.0.1:8765` once, then `cua screenshot --out <path>.png --json --max-width <N>` — to get an actual saved image rather than just an on-screen glance. Resize the Aegis window to mobile, tablet, and desktop widths and take one CUA screenshot at each so the visual pass produces reviewable artifacts for every breakpoint, not just an impression from one.
- **Performance smoke check:** treat a clean `navigate` + `page inspect` round trip through Aegis against the live deployed URL (not localhost) as the real-world load/render check — if the page is slow or hangs through Aegis on the actual network path, it will be slow for a visitor too. This catches real loading and responsiveness regressions; for hard numbers (Core Web Vitals, bundle size, memory profiling) still use the browser's own devtools or the project's build-level performance tooling. (CUA's own `perf bench screenshot|stream|input` benchmarks CUA's capture/input latency, not the website — don't mistake it for a site performance report.)

Do not consider the QA gate passed on dev-server output alone — the Aegis-plus-CUA pass against the actual deployed URL is what confirms the client's real experience, not just what worked locally.

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
