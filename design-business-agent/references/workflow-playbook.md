# Workflow Playbook

This is the concrete, low-friction production loop the studio actually runs. It's simpler than it looks from the outside — a small number of steps, not a stack of separate platforms. The goal is a client-ready page in a working session, not days of back-and-forth.

## The Loop

1. **Bullet-point brief → build the base site.** State the business, audience, and desired feel in a handful of bullets and build the full first-pass site in one go, using taste-max for art direction and layout grounding. Don't wait for a perfect brief — a rough one-shot is the fast, correct starting point; refine from there.
2. **Generate the hero/signature asset.** Decide the one effect the page is built around (rotating hero object, exploding-view product animation, environmental pan, etc.). Generate a clean base image if the motion needs a controlled subject, then generate the animation from it with a tightly constrained motion prompt. Generate 2–3 takes for anything hero-critical and pick the best.
3. **Review the raw generation before integrating.** Play it back, check for drift, artifacts, and unwanted background elements. Do not integrate a first-pass generation without watching it in full.
4. **Integrate and mask.** Place the asset as a background/hero element, center and compose it correctly, and apply gradient masking so the asset blends into the page background rather than sitting as a hard-edged rectangle. Expect to iterate on mask strength — a mask that's too weak leaves a visible seam between the asset and the surrounding page color.
5. **Fix legibility immediately.** Screenshot the result and check text contrast/size against the generated background before moving on — busy generated imagery routinely swallows body copy that looked fine as a wireframe.
6. **Add scroll-driven storytelling where the concept calls for it.** For a section that should reveal detail as the user scrolls (e.g., an exploding-view product breakdown), convert the source video into an extracted, optimized frame sequence tied to scroll position rather than scrubbing a raw video element — this gives deterministic, reliably smooth control that a scrubbed `<video>` element usually can't match.
7. **Run the compression loop.** First pass will likely be heavy and choppy — that's expected, not a failure. Extract frames as optimized images, tie preloading to the sequence, and re-check the section transitions (masks/gradients/timing) after compressing. Two or three "make it load faster" passes is the normal path to a smooth result, not a sign of a mistake.
8. **Compress the hero media too.** A raw generated hero video can be several megabytes for a few seconds; re-encoding it for delivery size (not just the scroll sequence) is a separate, easy pass that's worth doing explicitly — order-of-magnitude size reductions with no visible loss are normal.
9. **Run a dedicated mobile pass.** After desktop reads correctly, explicitly revisit composition, media weight, and motion complexity for mobile — this is a distinct step, not something that falls out of responsive CSS alone.
10. **Deploy.** Default to a free/cheap static host with a global CDN unless the project specifically needs more (custom backend, auth, server rendering with dynamic data, etc.). Verify the live URL actually renders correctly post-deploy, not just that the local build succeeded.

## Cost and Speed Expectations

Treat this as roughly true and use it to calibrate ambition vs. budget, not as a hard promise to a client: a full first-pass build is closer to a working session than a multi-day engagement, and generation spend for a page's custom hero/asset work is typically a handful of dollars in credits plus a modest amount of agent token spend — cheap enough that generating multiple variants and running several optimization passes is the correct default, not a luxury to ration.

## Common Failure Modes to Catch Early

- Treating the first generation output as final without watching it end to end.
- Integrating an asset without a legibility check on overlaid text.
- Shipping the first (heavy, choppy) integration pass instead of running the compression loop.
- Fixing the frame-sequence performance but forgetting the raw hero video is still an unoptimized multi-megabyte file.
- Doing the mobile pass as an implicit side effect of desktop work instead of as its own explicit step.
- Reaching for a new platform/tool per step instead of running brief → build → generate → integrate → optimize → deploy as one continuous loop inside the same agent session.
