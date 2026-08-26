# Video Engineering and Scroll-Driven Frame Sequences

## Video Engineering

Do not casually place enormous source videos into a webpage. Production video assets should be: appropriately encoded, compressed, correctly sized, served through suitable infrastructure, responsive where appropriate, lazy-loaded when appropriate, poster-backed where appropriate, preload-controlled, cached, delivered from a CDN or object store.

Choose modern formats and codecs according to current browser compatibility and the project's requirements. Do not ship unnecessarily high-resolution video to small screens. Consider alternate encodes when worthwhile. The visitor should not download a cinematic master file merely to display a small background animation.

A raw AI-generated master can easily be 5MB+ for a few seconds of footage; re-encoding for web delivery (correct resolution, bitrate, codec) routinely gets this down by an order of magnitude with no visible quality loss at delivery size. Always re-encode before shipping — never link the raw generation output directly.

## Scroll-Driven Video and Image Sequences

For experiences where the user's scroll position controls an animation, consider converting source animation into an optimized image/frame sequence when that provides superior deterministic control over a video element's `currentTime` scrubbing.

Conceptually:

```
Source animation → frame extraction → optimization → sequence manifest → CDN → scroll-controlled renderer
```

Do not naïvely load hundreds of full-resolution images. Engineer the sequence. Techniques include: reducing frame count to the minimum that still reads as smooth, responsive resolutions per breakpoint, modern image formats, predictive preloading, chunked loading, nearest-frame rendering, frame caching, request cancellation, intersection-based activation, progressive loading, memory-aware eviction, fallback assets.

Determine the required visual fidelity experimentally. Do not optimize by simply making everything "extremely low quality." Optimize for: **minimum bytes required to maintain the intended perceived quality.**

## Package Frame Sequences Properly

Large animation sequences must be treated as structured assets. Do not create an unorganized CDN directory containing arbitrary millions of files. Use predictable asset namespaces such as `project / experience / asset / variant / frame`.

Maintain metadata describing the sequence — a manifest containing: version, frame count, dimensions, frame rate, naming convention, responsive variants, format, chunk boundaries, preload strategy. This allows the frontend to reason about the animation as a single logical asset.

## The Iterative Compression Loop

Treat "make it load faster" as a real, repeatable engineering step, not a one-off cleanup:

1. Ship the working version first — correctness before optimization.
2. Identify the actual weight (hero video/image size, frame sequence total payload, JS bundle).
3. Compress/re-encode/reduce frame count in one targeted pass.
4. Re-verify the visual result — masks, gradients, and cross-fade timing between sections are the first things to break during a compression pass; re-check them every time, not just at the end.
5. Repeat until perceived quality and load time are both acceptable. Two or three passes is normal, not a sign something went wrong the first time.

## Asset Infrastructure

Treat media as infrastructure. Maintain logical separation between: source assets, generated assets, production masters, optimized web assets, responsive variants, thumbnails/posters, frame sequences, deprecated versions.

Use deterministic naming or content hashing where appropriate. Design for: caching, immutable assets, invalidation, deduplication, versioning, compression, lifecycle management, observability.

The storage system should remain comprehensible even after hundreds of projects.
