# Generative Asset Pipeline

For projects requiring custom cinematic or 3D-style assets, use the available Higgsfield pipeline and its supported generation models.

**Auth:** Higgsfield requires a key ID *and* a secret, not a single token — `HF_API_KEY` (the ID, a UUID) and `HF_API_SECRET` (the secret) are read from the project `.env`. The request header is `Authorization: Key ${HF_API_KEY}:${HF_API_SECRET}`. A single value with no colon is not valid credentials by itself — if a project's `.env` only has one Higgsfield value, get the missing half before assuming the integration works. There is no dedicated credits/balance API endpoint; check remaining credits at [cloud.higgsfield.ai](https://cloud.higgsfield.ai) directly, not through the API.

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

Animation should use the strongest currently appropriate video-generation model available through Higgsfield or another approved pipeline — Kling 3.0 has been the strong default for cinematic pans, exploding-view product animation, and slow rotating hero loops.

Do not permanently hard-code assumptions about which generation model is best. Model capabilities evolve rapidly. Research or inspect currently available models when choosing the generation pipeline. Choose based on the actual task: realism, consistency, motion quality, camera control, temporal stability, product fidelity, typography preservation, resolution, generation latency, cost.

The objective is the asset — not loyalty to a particular model. That said, Nano Banana (image) and Kling 3.0 (video) are both confirmed-good current picks for this pipeline — reach for them by default, and only spend time evaluating alternatives when a specific asset's requirements (an unusual aspect ratio, a look one of them handles poorly, a cost/latency constraint) call for it.

## Current Baseline Specs (verify before use)

Known-good defaults as of this skill's last update — a starting point, not a permanent contract. Model lineups, resolution ceilings, and pricing move fast; check what Higgsfield currently exposes before assuming these still hold, especially on a project spaced months from the last one.

**Kling 3.0 (via Higgsfield), last known specs:**

- Duration: 5s per generation is the practical default for a hero loop or scroll-source clip. Longer durations cost proportionally more and are rarely needed for a landing-page asset — a well-directed 5s clip is enough source material for both a looping hero and a frame-extracted scroll sequence.
- Aspect ratio: 16:9 for wide desktop hero placements; use 9:16 or 1:1 instead when the target placement is a mobile-first section, a square card, or a vertical panel — match the generation aspect to the actual placement rather than generating 16:9 and cropping, which wastes resolution and can reframe the composition badly.
- Resolution: 1080p has been the practical ceiling for this pipeline. Generate at 1080p even when the delivered asset will be served smaller — downsampling from 1080p during web optimization looks materially better than upsampling a lower-res generation.
- Cost: roughly 7.5 Higgsfield credits per 5s/1080p generation as of last check — cheap enough that generating 2–3 takes of a hero-critical asset and picking the best is the correct default, not an indulgence.

**Image generation (Nano Banana or current-best equivalent):**

- Generate at the highest resolution the model offers when the image will be either a video-generation seed or a large hero background — upscaling a low-res generation later is a visible downgrade; generating high and downsampling is not.
- White or neutral flat backgrounds by default (see Practical Generation Notes below) unless the concept requires an environmental background.

**Web-delivery targets after optimization** (these apply post-compression, not to the raw generation):

- Hero video, re-encoded for delivery: aim for the low hundreds of KB up to a few MB for a several-second loop, not the 5MB+ a raw generation export commonly lands at. Re-encode resolution and bitrate for the actual rendered size on screen, not the source 1080p.
- Frame-sequence images: modern compressed format (WebP/AVIF over PNG/JPEG), sized to the actual rendered dimensions per breakpoint, with frame count trimmed to the minimum that still reads as smooth — extract a full-framerate source once, then subsample down.
- Treat these numbers as a sanity check to catch an obviously bloated export, not a strict spec to hit at all costs — the real target is always "minimum bytes required to maintain the intended perceived quality," verified visually, not just by file size.

## Practical Generation Notes

- Generate 2–3 variants of a hero-critical asset when budget allows, and pick the best rather than accepting the first output. This materially improves hit rate on camera motion, artifact-freedom, and composition.
- For a controlled subject (e.g., a rotating product/globe), generate a clean base image first (e.g., via Nano Banana), then feed that image into the video model with a tightly constrained motion prompt (e.g., "rotating in place, center of mass fixed, no drift") rather than prompting video generation from text alone.
- White or neutral backgrounds on generated assets make them dramatically easier to composite into a hero section via masking/blending — prefer this unless the concept requires an environmental background.
- Cost is genuinely low relative to traditional production — think single-digit dollars in generation credits per asset, plus a few dollars of agent token spend for integration. This does not license carelessness; it licenses generating more variants and iterating more, not skipping review.

## Generated Assets Are Raw Materials

Never assume generated output is production-ready. Inspect assets for: visual artifacts, inconsistent geometry, malformed objects, unintended text, temporal instability, flicker, color inconsistency, compression, poor looping, incorrect branding, unrealistic motion, visible generation artifacts.

Process and optimize assets before deployment. Generation is part of the production pipeline, not the final step.
