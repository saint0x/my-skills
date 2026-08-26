# Generative Asset Pipeline

For projects requiring custom cinematic or 3D-style assets, use the available Higgsfield pipeline and its supported generation models. `HIGGSFIELD_API_KEY` is read from the project `.env`.

The conceptual workflow:

```
Art Direction
  → Image / Asset Generation
  → Animation / Video Generation
  → Post-processing
  → Web Optimization
  → CDN / Object Storage
  → Frontend Rendering
```

Nano Banana or the strongest currently available appropriate image model may be used to generate highly realistic visual assets, product scenes, environmental imagery, 3D-style compositions, textures, or landing-page graphics.

Animation should use the strongest currently appropriate video-generation model available through Higgsfield or another approved pipeline — Cling 3.0 has been the strong default for cinematic pans, exploding-view product animation, and slow rotating hero loops (5s clips, 16:9 for wide hero placement, 1080p as the practical ceiling).

Do not permanently hard-code assumptions about which generation model is best. Model capabilities evolve rapidly. Research or inspect currently available models when choosing the generation pipeline. Choose based on the actual task: realism, consistency, motion quality, camera control, temporal stability, product fidelity, typography preservation, resolution, generation latency, cost.

The objective is the asset — not loyalty to a particular model.

## Practical Generation Notes

- Generate 2–3 variants of a hero-critical asset when budget allows, and pick the best rather than accepting the first output. This materially improves hit rate on camera motion, artifact-freedom, and composition.
- For a controlled subject (e.g., a rotating product/globe), generate a clean base image first (e.g., via Nano Banana), then feed that image into the video model with a tightly constrained motion prompt (e.g., "rotating in place, center of mass fixed, no drift") rather than prompting video generation from text alone.
- White or neutral backgrounds on generated assets make them dramatically easier to composite into a hero section via masking/blending — prefer this unless the concept requires an environmental background.
- Cost is genuinely low relative to traditional production — think single-digit dollars in generation credits per asset, plus a few dollars of agent token spend for integration. This does not license carelessness; it licenses generating more variants and iterating more, not skipping review.

## Generated Assets Are Raw Materials

Never assume generated output is production-ready. Inspect assets for: visual artifacts, inconsistent geometry, malformed objects, unintended text, temporal instability, flicker, color inconsistency, compression, poor looping, incorrect branding, unrealistic motion, visible generation artifacts.

Process and optimize assets before deployment. Generation is part of the production pipeline, not the final step.
