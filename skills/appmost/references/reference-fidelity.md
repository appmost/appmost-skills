# Implementing an approved visual reference

Use this when the user has selected a sketch, screenshot or design direction to implement. It supplements native review; it does not require an exact screenshot clone where the user requested only inspiration.

## Sketch before implementation

List the affected screens and meaningful presentations, including a new sheet reached from an existing page. Match each to a saved reference in the relevant state. If the user already selected a reference, use it where it covers the scope. Sketch uncovered screens and substantial redesigns with an authorized image-generation tool before changing page source. Reuse the established direction for small layout and copy refinements. When the choice materially changes the product direction, follow the project's decision process.

Review the sketch alongside neighboring screens. Confirm which existing native components own the title, navigation, list rows and input. Save the sketch and its creation date with the affected screen and state. If generation is unavailable, record the missing sketch and continue independent work. A sketch made after a screen was built can guide a subsequent revision. Record the implementation it was compared against and retain the actual order of work.

## Compare before declaring completion

**Choose the relationships that define the design.** Start with three to five when the screen supports them. Choose visible actions, shared edges, typographic roles, gaps or a focal image crop that affect the main task. For a repeated row, check shared text edges and action placement, gaps within the row and the distance between matching points across two consecutive row intervals when available. For a form, check label-to-field spacing, error placement and primary action reachability. If a component must fit multiple actions or long labels, try it in an isolated preview before committing to the full composition.

**Match the state and scale.** Keep viewport, renderer, language, appearance, text size, scroll position, content and control states stable across app renders. Use comparable content in the reference and deterministic app test data. Keep both original images and label any derived comparison image. For a local comparison, use a common content anchor and a single proportional scale. Record any crop, alignment and intentional native chrome differences. Keep the complete app capture and check safe-area clearance and scroll reachability in it.

**Inspect and rank before editing.** View both images at readable size. Check font family or design, weight, visible size, line height and actual wrapping. For each important discrepancy, record the target, observed difference, effect on the task and what to recheck after a correction. Prioritize missing or unusable actions and repeated layout or hierarchy errors. For example, if a booking list still stacks two intended side-by-side actions, shorter rows alone leave the main composition error open. Once the actions align, check that the row rhythm and title prominence still match.

**Correct and compare again.** Use the first native render after implementation as the baseline. Correct the most consequential fixable discrepancy or a small group with the same cause. Remeasure the selected relationships in the same context, then inspect the complete fresh render and nearby content. This is the mandatory first iteration for each new or redesigned screen or modal. Record unsupported render variants and use existing supported properties.

**Review adaptations in their own states.** Use a narrow supported width, larger system text or a long translation when these can change the layout. Use meaningful fixtures such as both toggle states, long values and an empty or error state. Allow natural wrapping and reflow while preserving action meaning, focus order, independent touch targets and scroll access to the last important control. Verify critical activation and data-driven transitions with an applicable app-owned test.

Use one to three iterations per screen or modal. Use two or three when material gaps remain or the requested quality calls for closer fidelity. If material differences remain after the available rounds, record them and keep visual acceptance open. If a meaningful correction or fresh render is unavailable, record the incomplete iteration.

Count a design iteration as a comparison that leads to a substantive source correction and a reviewed new render. Another build, a repeat export, a validator result or an unrelated change does not count.

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
