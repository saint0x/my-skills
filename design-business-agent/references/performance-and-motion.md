# Performance, Motion, Mobile, and Accessibility

## Performance Is Part of Design

> A good design with bad performance is bad design.

Performance is not a cleanup task performed after design. It is a design constraint from the beginning. Animations, 3D elements, video, typography, imagery, shaders, scroll effects, transitions, parallax, and interactions must be selected and implemented with their computational and network costs in mind.

Never sacrifice usability or perceived quality simply to demonstrate technical sophistication. The most sophisticated implementation is often the one where the user cannot perceive how much engineering was required.

## Progressive Enhancement

A premium experience should degrade gracefully. Think in layers:

1. **Semantic content** — the page works.
2. **Styling** — the page looks excellent.
3. **Imagery** — the art direction appears.
4. **Motion** — the experience becomes cinematic.
5. **Advanced interaction / 3D** — capable devices receive the complete experience.

The fundamental proposition and conversion path should not depend entirely on the most computationally expensive layer.

## Mobile Is Not Desktop Shrunk Down

Design mobile intentionally, as its own pass after desktop is right. Reconsider: composition, typography, interaction, animation, image crops, 3D complexity, navigation, information density, video resolution, scroll behavior.

Some desktop effects should be simplified or replaced entirely on mobile. That is not a compromise — it is good design.

## Motion Philosophy

Motion should communicate. Good motion can establish: hierarchy, causality, spatial relationships, continuity, feedback, emphasis, progression, atmosphere.

Avoid animation merely because an element can animate. Prefer coherent motion systems over dozens of unrelated effects. Animations should feel responsive rather than ornamental. Honor reduced-motion preferences.

## Rendering Strategy

Choose rendering technology based on the experience rather than habit: CSS, DOM transforms, SVG, Canvas, WebGL, WebGPU, video, image sequences, shaders, true 3D scenes.

Do not render something through WebGL merely because WebGL sounds sophisticated if CSS can achieve the same result more reliably. Likewise, do not force DOM techniques onto experiences where GPU rendering provides a substantial advantage. Choose the simplest architecture capable of delivering the intended experience at excellent quality.

## Performance Budgets

Before implementing unusually expensive experiences, establish reasonable budgets for: initial transfer, critical assets, JavaScript, fonts, imagery, video, animation frames, memory, CPU usage, GPU usage, interaction latency.

Measure rather than assume. Pay particular attention to current Core Web Vitals and relevant browser performance metrics. Optimize for both measured and perceived performance.

## Perceived Performance

The user should rarely stare at an empty page waiting for the "premium experience" to arrive. Use: meaningful first paint, skeleton states when appropriate, poster frames, progressive imagery, staged asset loading, strategic prefetching, preload only when justified, smooth transitions from static to interactive states.

Make loading itself feel intentional when unavoidable.

## Fonts

Typography is central to elite design, but fonts can easily damage performance. Optimize: number of families, number of weights, subsets, loading strategy, fallback metrics, caching.

Avoid invisible text and unnecessary layout movement. Never compromise the typography unnecessarily, but do not load an entire type library to use two weights.

## Accessibility

Accessibility is part of craftsmanship. Account for: semantic structure, keyboard navigation, focus states, readable contrast, labels, alternative text, motion sensitivity, responsive type, touch targets, screen-reader behavior.

Cinematic design and accessible design are not opposites.

## Avoid Layout Instability

Reserve space for asynchronous media. Know image dimensions. Know video aspect ratios. Manage font behavior. Do not allow lazy-loaded visual effects to cause the page to jump around. The interface should feel physically stable.

## Test the Actual Experience

Never judge performance exclusively from a powerful development machine on fast internet. Test representative desktop devices, mobile devices, viewport sizes, slower networks, slower CPUs, touch interaction, browsers. Pay particular attention to mobile Safari and other environments where sophisticated experiences can behave differently.
