# Implementing an approved visual reference

Use this when the user has selected a sketch, screenshot or design direction to implement. It supplements native review; it does not require an exact screenshot clone where the user requested only inspiration.

## Sketch before implementation

List the affected screens and meaningful presentations, including a new sheet reached from an existing page. Match each to a saved reference in the relevant state. If the user already selected a reference, use it where it covers the scope. Sketch uncovered screens and substantial redesigns with an authorized image-generation tool before changing page source. Reuse the established direction for small layout and copy refinements. When the choice materially changes the product direction, follow the project's decision process.

Review the sketch alongside neighboring screens. Confirm which existing native components own the title, navigation, list rows and input. Save the sketch and its creation date with the affected screen and state. If generation is unavailable, record the missing sketch and continue independent work. A sketch made after a screen was built can guide a subsequent revision. Record the implementation it was compared against and retain the actual order of work.

## Compare before declaring completion

**Define what passes.** Pick three to five relationships that matter to the screen, such as an action sharing a text edge, two actions sharing a line, a title's prominence, an image crop or a repeated item interval. Give each a target, a tolerance or observable pass condition, and a baseline and current result. Choose the tolerance for the design and the precision of the inputs. Treat missing, obscured or misplaced primary actions as open findings even if other checks improve. For repeated rows, measure the same anchors across two consecutive intervals when available. Try one real row with representative long labels or multiple actions before applying the template throughout a screen.

**Use the same viewport coordinates.** Match the viewport, renderer, appearance, language, text size, scroll position, fixture content and control states across app renders. Keep full originals. For screenshots, crop each viewport once, use the same viewport origin, and apply one proportional scale per image if needed. Record crop, scale and any missing context. Use viewport coordinates to check placement and within-component deltas to check alignment or spacing, such as `action.left − label.left`. A content-aligned close-up can help diagnose a group after you record its viewport position. Inspect the complete capture for native chrome, insets and scroll reachability. Document intentional native differences with the content checks they still need to satisfy.

**Measure the visible relationship.** Prefer `review_page` and, when exposed, `compare_page_layout` for the app's before/after geometry. Bind the image to its source revision and render context, and use the returned model paths to find the relevant template or property. Verify whether a reported frame bounds the whole control, its text layout or the visible glyphs. Use comparable edges and units on both sides. For a raster-only sketch, use crop guides or a few tight regions around the same visible glyphs or edges. Record rendered image pixels or percentages of viewport width when the logical scale is unknown. Confirm estimates at readable size and allow for raster noise. Check type role, apparent size and weight, wrapping and line spacing by eye. Use source or renderer evidence for font identity, logical font size, exact baselines and touch targets.

A schedule list might use these checks.

| Relationship | Example pass condition |
| --- | --- |
| Primary action relative to item label | Visible leading edges within 3 logical points in the default native context, or a tolerance stated in normalized pixels for a raster reference |
| Primary and secondary actions | Both visible on the same line at the reference width, with readable wrapping or reflow in narrower or larger-text contexts |
| List rhythm | Both adjacent label-to-label intervals fall within the agreed range |

**Correct the biggest visible issue first.** Use the first native render as the baseline. Trace the main discrepancy to the owning row, container or native component before editing. Check template slots, default alignment and intrinsic insets against the current contract and the rendered output. Correct the most consequential fixable issue or batch changes with one cause. Remeasure every selected relationship and inspect nearby content in the fresh render. Log target, before, after and pass/open for the important checks. A shorter row can improve density while leaving both actions in the wrong positions.

**Review adaptations in their own states.** Use a narrow supported width, larger system text or a long translation when these can change the layout. Use meaningful fixtures such as both toggle states, long values and an empty or error state. Allow natural wrapping and reflow while preserving action meaning, focus order, independent touch targets and scroll access to the last important control. Verify critical activation and data-driven transitions with an applicable app-owned test.

Plan for one to three iterations per new or redesigned screen or modal, with at least one substantive source correction after the baseline. Count a round once you make the change and inspect a fresh render against the reference. If you cannot make a meaningful correction or produce a fresh render, report the incomplete round. If material differences remain at handoff, leave those acceptance checks open.

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
