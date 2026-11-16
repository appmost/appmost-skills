# Implementing an approved visual reference

Use this when the user has selected a sketch, screenshot or design direction to implement. It supplements native review; it does not require an exact screenshot clone where the user requested only inspiration.

## Compare before declaring completion

Identify the reference's defining choices: display versus body typography, hierarchy and line breaks, density, shared edges, image crop, colors, content grouping and visible actions. Record intentional native adaptations separately from accidental differences. Do not silently replace the selected composition with a convenient template.

Use comparable viewport, language, text size, state and content. Keep the original reference and native capture intact. If normalization or a difference image is useful, make a separate analysis artifact and record crops, alignment, excluded chrome and resizing. Do not present altered UI pixels as the implemented result.

Inspect the pair side by side at readable size. Check font family/design, weight, size, line height and actual wrapping separately. A declared font or force-system-font flag is insufficient if the renderer ignores it. Treat an unavailable rendering capability as an explicit discrepancy, not a fidelity pass or a reason to invent document fields.

Rank discrepancies by impact, correct a coherent batch in the source, then render and compare again. Continue while material differences remain fixable within scope. Avoid a fixed minimum iteration count or arbitrary restyling after the target is met. Count a design iteration as a comparison that leads to a source correction and a reviewed new render; builds, repeated exports and validator calls alone are not design iterations.

## Disclosure on rich content

A hero, image-led feature or multi-section container should not acquire a trailing chevron solely because it is tappable. Its position can float beside the image and consume the intended media/text width. Omit it by default and retain the navigation action and accessible interaction. Use the current supported disclosure setting on the actual owner; do not remove navigation to hide its arrow.

Compact single-destination list rows may retain native chevrons. A user-requested visible CTA should remain visible; hiding a chevron does not authorize replacing the CTA or adding a duplicate action. If the user explicitly requests another affordance, follow that choice and inspect its full component bounds.

## Optional fidelity score

A numeric score can make successive reviews comparable, but it is a declared review rubric, not an objective percentage of visual sameness. Choose weights before scoring and keep them fixed across a comparison. For example:

| Dimension | Example weight |
| --- | --- |
| Typography and wrapping | 30 |
| Composition and hierarchy | 25 |
| Spacing and alignment | 20 |
| Imagery and crop | 15 |
| Colors and component details | 10 |

Rate each dimension 0–4: absent/incompatible, major differences, several material differences, minor differences, or close within the stated adaptations. Compute `sum(weight × rating / 4)` on a 0–100 scale. Preserve per-dimension observations, context and unverified items; do not invent scores for unseen states. Report measured geometry separately from visual judgments. A high total cannot cancel a missing primary action, unreadable text, incorrect font role or broken flow. Agree any pass threshold with the task rather than making one universal.

Pixel differences or SSIM can flag changed regions when images are aligned. LPIPS provides a learned perceptual distance. Neither alone proves that an interface matches its hierarchy, type roles or behavior, and neither should be relabeled as a percentage of design fidelity. Reference: [SSIM example](https://scikit-image.org/docs/stable/auto_examples/transform/plot_ssim.html), [LPIPS research](https://richzhang.github.io/PerceptualSimilarity/).

## Evidence and handoff

Keep the selected reference, final native render, source revision and a brief discrepancy/iteration record together in the app's private workspace. Explain adaptations and capability gaps. Distinguish fixture composition from the live data/navigation flow: selecting an item must populate its destination through the actual supported action before that flow can pass. Opening a destination with no selection should yield an intentional empty state, not an indefinite placeholder loader.
