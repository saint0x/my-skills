# Generative Asset Pipeline

For projects requiring custom cinematic or 3D-style assets, use **fal** (fal.ai) as the primary model-inference pipeline. Higgsfield credentials are retained in the project `.env` and can still be used for a model or workflow fal doesn't cover well, but fal is the default — it hosts the same underlying models (Kling, Nano Banana) directly, with a simpler single-token auth and a much wider model catalog to pull from as the field moves.

**Auth (fal, primary):** a single `FAL_KEY` env var, already in `ID:SECRET` form (e.g. `515b0908-...:692e4fee...`) — do not split it, pass it whole. Header: `Authorization: Key ${FAL_KEY}`. Request pattern:

```bash
curl -X POST "https://fal.run/<model-slug>" \
  -H "Authorization: Key ${FAL_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "..."}'
```

A successful call returns a JSON body with the generated asset's URL (or a `request_id` to poll for async models). There is no free/no-cost way to test a model-inference endpoint directly — it triggers a real, billed generation. To confirm a key is valid without spending credits, hit `GET https://api.fal.ai/v1/account/billing` with the key — a bad key returns `401 Invalid API key`; a valid key returns either the billing payload (if the key has Admin scope) or `403 This API key is not permitted to perform this action` (if it's a standard API-scope key, which is normal and still proves the key is valid — the 403 message differs from the 401 one). Standard API-scope keys can't read balance through the API either way; check remaining credits at the [fal dashboard](https://fal.ai/dashboard/billing) directly.

**Auth (Higgsfield, kept/secondary):** `HF_API_KEY` (a UUID) and `HF_API_SECRET`, combined as `Authorization: Key ${HF_API_KEY}:${HF_API_SECRET}` — two separate env values, not one. No credits API either; check balance at [cloud.higgsfield.ai](https://cloud.higgsfield.ai).

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

Animation should use the strongest currently appropriate video-generation model available through fal or another approved pipeline — Kling has been the strong default for cinematic pans, exploding-view product animation, and slow rotating hero loops.

Do not permanently hard-code assumptions about which generation model, version, or provider is best. Model capabilities evolve rapidly, and fal in particular adds new model tiers often (e.g. newer Kling versions, Nano Banana Pro/2 superseding the original). Research or inspect currently available models on fal's model catalog when choosing the generation pipeline. Choose based on the actual task: realism, consistency, motion quality, camera control, temporal stability, product fidelity, typography preservation, resolution, generation latency, cost.

The objective is the asset — not loyalty to a particular model or provider. That said, Nano Banana (image) and Kling (video), both served through fal, are confirmed-good current picks for this pipeline — reach for them by default, and only spend time evaluating alternatives when a specific asset's requirements (an unusual aspect ratio, a look one of them handles poorly, a cost/latency constraint) call for it.

## Current Baseline Specs (verify before use)

Known-good defaults as of this skill's last update — a starting point, not a permanent contract. Model lineups, resolution ceilings, and pricing move fast; check fal's current model catalog before assuming these still hold, especially on a project spaced months from the last one.

**Kling (via fal), last known specs:**

- Model slugs follow the pattern `fal-ai/kling-video/<version>/<tier>/<task>` — e.g. `fal-ai/kling-video/v2.6/pro/image-to-video`. Check fal's model catalog for the current newest version/tier (a v3 pro tier has appeared) before defaulting to whatever version this doc last named.
- Duration: 5s per generation is the practical default for a hero loop or scroll-source clip. Longer durations cost proportionally more and are rarely needed for a landing-page asset — a well-directed 5s clip is enough source material for both a looping hero and a frame-extracted scroll sequence.
- Aspect ratio: 16:9 for wide desktop hero placements; use 9:16 or 1:1 instead when the target placement is a mobile-first section, a square card, or a vertical panel — match the generation aspect to the actual placement rather than generating 16:9 and cropping, which wastes resolution and can reframe the composition badly.
- Resolution: 1080p has been the practical ceiling for this pipeline. Generate at 1080p even when the delivered asset will be served smaller — downsampling from 1080p during web optimization looks materially better than upsampling a lower-res generation.
- Pro/Master tiers cost more per generation than the standard tier in exchange for better motion fluidity and prompt precision — reach for standard by default, and step up to pro/master for a hero-critical asset where the extra fidelity is worth it.

**Image generation (Nano Banana or current-best equivalent, via fal):**

- Model slug: `fal-ai/nano-banana` (text-to-image) or `fal-ai/nano-banana/edit` (image-to-image); a newer, stronger `fal-ai/nano-banana-pro` tier exists — check whether it's the better default before defaulting to the original.
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
