---
name: advertising-imagery-agent
description: Create premium advertising image sets for products, including photoreal product shots, consistent multi-angle photoshoot systems, and lifestyle or human campaign imagery driven by campaign painpoints, marketing strategy, and design quality bars.
metadata:
  short-description: Premium ad imagery systems
---

# Advertising Imagery Agent

Use this skill when the user asks for advertising imagery, product image sets, campaign visuals, lifestyle images, photoreal product photos, ad art direction, product renders, social ad image concepts, hero image sets, or image-generation prompts for a product or campaign.

The job is not to make one pretty image. The job is to turn a product and campaign painpoint into a coherent set of persuasive images that feel like they came from one intentional photoshoot.

## Related Skills

Use `$marketing-and-advertising-agent` when the painpoint, audience, offer, campaign angle, conversion objective, or visual persuasion job is unclear. Image-set decisions should usually come from the product's most real customer pain, not from generic aesthetics.

Use `$design-loop` when the imagery is high-stakes, premium, brand-defining, or visually uncertain. Let it set or audit the quality bar, especially against `/Users/deepsaint/Desktop/design-business/inspo/` when that library is available.

Use image generation tools only after the image strategy is clear enough to brief. Do not generate a scattered pile of unrelated images.

## Painpoint-Led Visual Strategy

Every image should have a persuasion job tied to a real painkiller angle:

- Remove visible friction.
- Make the painful status quo feel costly.
- Show the product as the credible mechanism of relief.
- Make the desired future feel concrete and emotionally legible.
- Reduce risk by showing use, context, scale, quality, proof, or human confidence.

Do not build imagery around vitamin claims such as "nice to have," "more modern," "better workflow," or "elevated lifestyle" unless those are connected to a specific urgent pain and relief.

Before generating or directing images, identify:

- Product and exact object state to show.
- Target customer and painful situation.
- Conversion objective and channel.
- Primary painpoint and emotional state.
- Proof or mechanism that needs to be visible.
- Brand world, design system, and quality bar.
- Required deliverables, aspect ratios, and usage contexts.

## Image Set Architecture

Default to a coherent set, not a single angle:

- Core product hero: the cleanest iconic image of the product.
- Angle coverage: front, back, side, three-quarter, top, scale, detail, ports, texture, packaging, interface, or in-use angles as applicable.
- Macro/detail shots: materials, edges, controls, seams, finish, ingredients, interface states, or proof-bearing details.
- Context shots: product in the environment where the pain happens or relief is felt.
- Lifestyle/campaign shots: humans, emotion, use cases, social context, aspiration, tension, or transformation when relevant.
- Channel crops: compositions that survive fast-scroll, thumbnails, landing heroes, paid social, email, marketplace, or app-store placements.

Do not include unnecessary angles just to fill a grid. "All necessary angles" means all angles needed to understand, trust, desire, or buy the product.

## One Photoshoot Rule

The set must look like one production:

- Same camera language: lens family, focal length feel, perspective, depth of field, crop discipline.
- Same lighting logic: key light direction, contrast ratio, highlight behavior, shadow softness, reflections.
- Same color world: palette, white balance, contrast, saturation, grade.
- Same product truth: material, geometry, scale, labels, interface, proportions, and finish remain consistent.
- Same environment logic: surfaces, props, backgrounds, wardrobe, and location belong to one campaign world.
- Same retouching level: skin, product finish, grain, sharpness, and imperfections are consistent.

If generating images, reuse a compact visual system prompt across the set and vary only the shot-specific subject, angle, composition, and emotional moment.

## Photoreal Product Quality Bar

Product imagery should feel expensive and physically plausible:

- Real materials: metal, glass, plastic, fabric, paper, rubber, ceramic, liquid, or skin should have believable roughness, reflections, texture, translucency, and edge behavior.
- Real optics: lens compression, bokeh, focal plane, motion blur, sensor grain, chromatic behavior, and perspective should be coherent.
- Real light: highlights reveal form; shadows anchor objects; reflections match the environment.
- Real scale: hands, props, surfaces, packaging, and environment make size understandable.
- Real flaws: tiny dust, fingerprints, fabric wrinkles, skin pores, hair flyaways, product micro-scratches, uneven props, and natural asymmetry can make premium work feel human. Use restraint; flaws should add believability, not sloppiness.
- Real continuity: logos, labels, buttons, ports, UI, packaging text, and product geometry should not drift between images.

Avoid plastic-looking over-smooth surfaces, impossible lighting, warped logos, melted typography, fake hands, inconsistent product proportions, and stock-photo smiles.

## Lifestyle And Human Campaigns

Use lifestyle or human imagery when it clarifies pain, relief, identity, trust, scale, status, belonging, transformation, or use context.

Human campaign images should feel observed rather than staged:

- Natural posture, imperfect symmetry, believable expressions, and lived-in wardrobe.
- Hands and faces that look anatomically plausible.
- Realistic skin texture, hair, fabric, clutter, and environmental imperfections.
- Clear emotional proposition in the first second.
- Product causally connected to the relief or desired state.

Do not add humans when they dilute the product, create fake proof, or make the image less credible.

## Shot Planning

For each planned image, specify:

- Name or role in the set.
- Persuasion job.
- Painpoint or objection it addresses.
- Subject and product state.
- Camera angle, lens feel, crop, and composition.
- Lighting, palette, and material emphasis.
- Environment, props, and human presence if any.
- Aspect ratio and channel use.
- Negative constraints to preserve product truth and brand consistency.

For substantial sets, produce a shot list before generation. The user should be able to see why every image exists.

## Prompting Rules

When writing image prompts:

- Keep the shared campaign world consistent.
- Put product identity, material, shape, scale, and brand cues early.
- Describe camera, lens feel, lighting, surface, environment, and emotional action concretely.
- Include natural imperfections when humans or lived-in scenes are involved.
- State what must not change across the set.
- Ask for photorealistic advertising photography, not vague "high quality" output.

Prompt shape:

`[shared campaign world] + [specific shot role] + [product truth] + [painpoint/relief moment] + [camera/lens/composition] + [lighting/materials] + [human/environment details] + [brand cues] + [negative constraints]`

## Review Rubric

Before accepting an image set, check:

- Does every image serve a campaign painpoint, objection, proof need, or buying decision?
- Do all images look like the same product and the same photoshoot?
- Are all necessary product angles covered without filler?
- Are lifestyle and human shots useful, believable, and emotionally specific?
- Does the product remain causally connected to the relief being promised?
- Are materials, lighting, shadows, reflections, scale, and optics physically plausible?
- Are flaws humanizing rather than messy?
- Are crops ready for the intended channels?
- Is the set distinctive enough to belong to the brand instead of the category?

If an image fails product truth, consistency, or persuasion purpose, revise or replace it. Do not keep it because it is visually attractive.

## Output Standard

For image-set strategy, default to:

1. Campaign painpoint and conversion objective.
2. Visual persuasion model.
3. Shared photoshoot language.
4. Product-only shot list.
5. Macro/detail shot list.
6. Lifestyle or human campaign shot list, if applicable.
7. Prompt system for consistency.
8. Individual prompts or art-direction briefs.
9. Review criteria and known risks.

For a narrow request, give only the needed shot list, prompt, or critique.
