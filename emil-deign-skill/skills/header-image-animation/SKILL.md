---
name: header-image-animation
description: Generate and integrate premium 1080p header, hero, or landing-page images, then animate them into smooth video or high-performance web motion. Use when a site needs a hero/header visual, generated cinematic asset, image-to-video treatment, FAL/Kling/Veo/Vidu-style media generation, or SVG/layered web-native animated art.
---

# Header Image And Animation

A construction skill for hero and header media. It turns "make the top of this page feel premium" into an image, video, or web-native animated scene that belongs to the page instead of sitting on top of it.

The bar is the same as the animation skills: restraint, purpose, exact constraints, and implementation that survives the page. A beautiful frame that loads slowly, crops badly on mobile, fights the headline, or ends at a hard rectangular edge is not done.

## The Gate

Before generating anything, answer in one line:

```text
Media read: <surface> for <audience>, purpose <identity|explanation|mood|product proof|delight>, format <16:9|9:16|both>, motion <none|ambient|image-to-video|web-native>.
```

If the asset does not clarify identity, explain the product, set a necessary mood, show real proof, or create a rare delight moment, do not generate it. Use stronger layout, type, or real product imagery instead.

## Non-Negotiables

1. **Resolution is fixed by intent.** Default to 16:9 at 1920x1080. Use 9:16 at 1080x1920 only when the target is vertical mobile, story, reel, app-store-style preview, or a narrow immersive panel. If both desktop and mobile matter, generate or crop both deliberately.
2. **No rectangular sticker effect.** The media must blend into the page through composition, masks, edge gradients, color matching, continuation of background texture, alpha-aware overlays, or a deliberate framed treatment. A raw image box in a hero is a miss unless the product itself is being inspected.
3. **Prompt for layout, not just subject.** Reserve negative space for the headline and controls, name the safe zone, lighting direction, color temperature, surface texture, depth, camera, and edge behavior.
4. **Generate high-quality first frames.** Image-to-video inherits the frame's flaws. Fix crop, anatomy, text artifacts, brand details, perspective, and edge continuity before animating.
5. **Motion is subtle unless the page is about the motion.** Header animation is usually ambient: parallax, light sweep, cloth/fog/water movement, camera drift, UI state demonstration. Avoid loops that pull attention away from reading.
6. **Ship fallbacks.** Videos need a poster, static image fallback, `prefers-reduced-motion` handling, and mobile bandwidth consideration.
7. **Keep keys server-side.** FAL keys belong in server routes, build scripts, CI secrets, or local env, never bundled into browser JavaScript.

## Choosing The Medium

| Need | Medium |
| --- | --- |
| Real product, place, person, interface, or object must be inspectable | Real supplied image or generated image only if accuracy can be verified |
| Cinematic hero, abstract product metaphor, editorial header | FAL text-to-image or image-to-image, 16:9 1080p minimum |
| Static art needs life but not a new interaction model | Image-to-video through FAL, 1080p, 4-8s loop target |
| The page needs crisp, controllable, responsive motion | Layered SVG/HTML/CSS/Canvas, animated with CSS/WAAPI/Motion |
| The visual must sync to scroll or pointer | Web-native layers, not baked video |
| The visual is data, UI, or product workflow | Build real DOM/canvas/Three.js; do not fake it as a flattened image |

Use SVG when shapes need to stay razor sharp, recolor with tokens, or respond to layout. Use many small layers only when each layer has a reason: depth, mask, parallax, reveal, or independent timing. Group layers into logical wrappers so the DOM stays understandable.

## FAL Workflow

Use current FAL docs before calls, because model IDs and schemas move. As of the checked docs, `@fal-ai/client` is the current JavaScript client, `FAL_KEY` is the environment variable, and queue or subscribe calls are the normal paths for long-running generation.

Preferred shape:

1. Pick the model by job, not novelty.
   - Premium image-to-video: start with `fal-ai/kling-video/v3/turbo/pro/image-to-video` when available for 1080p image-to-video.
   - Fast controllable image-to-video: consider `fal-ai/veo3.1/fast/image-to-video` when 16:9 or 9:16, 1080p output, text motion control, or short durations fit.
   - Image refinement or reference-to-image: use the best current image model that supports the required aspect ratio and reference constraints.
2. Submit a small batch of still frames first. Pick the frame with the cleanest composition, not the most dramatic one.
3. Upscale or regenerate until the source frame is at least 1920x1080 for 16:9 or 1080x1920 for 9:16.
4. Animate only after the still frame passes the hero-fit checklist.
5. Keep the final video short and loopable. Prefer 4-8 seconds for ambient hero motion; 10 seconds only when the story needs it.
6. Export MP4/WebM when possible, keep the poster image next to the video, and store source prompts in the project when the repo has an asset provenance convention.

Minimal server-side call shape, adapt to the current model schema:

```js
import { fal } from "@fal-ai/client";

const result = await fal.subscribe("fal-ai/kling-video/v3/turbo/pro/image-to-video", {
  input: {
    image_url: sourceImageUrl,
    prompt: "Subtle cinematic camera drift, soft light moving across the surface, no text, no new objects, seamless loop feeling",
    resolution: "1080p",
    aspect_ratio: "16:9",
  },
  logs: true,
});
```

If the model does not expose `resolution` or `aspect_ratio` with those exact names, stop and match the current schema. Do not guess.

## Prompt Recipe

Write prompts as production art direction, not vibes:

```text
Create a 1920x1080 cinematic website hero image for <product/brand>.
Composition: <subject placement>, <headline safe zone>, <foreground/midground/background>.
Edges: left and bottom continue into <page background>; no hard border; soft atmospheric falloff.
Lighting: <direction>, <contrast>, <color temperature>.
Material: <textures/surfaces>.
Camera: <lens/framing/depth of field>.
Palette: <tokens or color family>, avoid generic purple-blue AI glow unless the brand requires it.
Negative: no text, no logos unless supplied, no warped UI, no extra fingers, no fake metrics, no watermark.
```

For vertical:

```text
Create a 1080x1920 vertical hero/header visual. Keep the subject readable in the middle third, leave top and bottom safe areas for app chrome or captions, and make side edges extendable for responsive crop.
```

For motion:

```text
Animate the image with <one motion idea>. Preserve identity and composition. Camera movement is <slow push-in|subtle lateral drift|locked camera>. No new objects, no text, no cuts, no sudden brightness shifts. Loop should feel calm and continuous.
```

## Integration Checklist

Before calling the work done:

- Crop-check desktop, tablet, and mobile. The subject, headline safe zone, and call-to-action must not fight.
- Blend the edges with CSS masks, gradients, overlays, or continued background color. Avoid abrupt image boundaries.
- Use `object-fit: cover` with explicit `object-position` per breakpoint, or use `<picture>` with separate 16:9 and 9:16 assets.
- Put text over calmer regions. Add a scrim or gradient only where it improves readability; do not darken the whole image by habit.
- Add `width`, `height`, aspect ratio, poster, preload strategy, and lazy/eager loading appropriate to first viewport priority.
- For video: `muted`, `playsInline`, no controls for ambient media, and a static fallback when autoplay fails.
- For reduced motion: replace animated video with the poster or a short opacity-only transition.
- Compress responsibly: AVIF/WebP for stills, MP4/WebM for video, and multiple sizes if the site has an image pipeline.

## Web-Native Animation

When using SVG, DOM layers, canvas, or Three.js:

- Animate `transform` and `opacity` by default.
- Use CSS or WAAPI for predetermined loops; use Motion/springs only for interactive or interruptible motion.
- Stagger layers 30-80ms when revealing a scene. Do not delay the text or primary action.
- Use `mask-image`, `clip-path`, gradients, and alpha textures to make artwork merge with the section background.
- Avoid animating filters except subtle blur during transitions; heavy blur is expensive, especially in Safari.
- For pointer/scroll motion, cap movement to a few pixels or degrees. The asset should breathe, not chase the cursor.

## Output

When generating or integrating media, finish with:

- **Asset spec**: model/source, dimensions, aspect ratio, file paths or URLs.
- **Integration**: how it blends into the page, crop rules, fallback behavior.
- **Motion**: purpose, duration/loop, reduced-motion behavior.
- **Feel check**: what to inspect at desktop and mobile sizes, and what would make you regenerate.

Keep it brief. The artifact and the page carry the argument.
