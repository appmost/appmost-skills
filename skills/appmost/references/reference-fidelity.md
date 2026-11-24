# Implementing an approved visual reference

Use this for visual changes to Appmost apps. Keep the selected design direction and review how the native presentation realizes it. The requested degree of fidelity determines the visual checks.

## Sketch before implementation

List the affected screens and meaningful presentations, including sheets, signed-in roles and conditional states. A visual change of any size needs a saved ImageGen image that depicts the state being changed. Open an existing matching approved original when there is one. If the user supplied another visual reference, retain it and use it as input for the ImageGen sketch. When a matching sketch is missing, use ImageGen and open the result before authoring.

For a whole-app review, account for each page and meaningful state. Open the matching ImageGen reference and compare its action roles, alignment and native chrome with the current rules. If the reference is missing or breaks a required rule, regenerate it using the existing reference and native capture as inputs where available. Preserve the essential data, actions and hierarchy. Open the revised sketch and resolve the failed visual rule before using it to guide implementation. In the whole-app inventory, pair each presentation with its specific sketch or panel, native capture, and open checks. A sibling can share a sketch when its hierarchy, data role, actions and chrome match. A container with no visible content can point to its mounted children. A sign-in gate cannot stand in for the signed-in screen. Keep any missing references or comparable renders open. Before adopting a regenerated sketch, check that each control has the same role as in the app: commands have visible surfaces, only destinations get disclosure arrows, and static facts stay static.

Before the first UI edit, save a small record in the existing task evidence. Use the exact unedited revision or immutable source snapshot, page ID, state, ImageGen artifact or approval evidence and at least one observable comparison target. Capture the unedited native baseline for the same state when it exists. Name a new presentation or an unavailable comparable baseline in the notes. Run the bundled [reference checker](../scripts/check_visual_reference.py), with the current source revision as reported by the editor or source inspection.

```sh
python3 -B scripts/check_visual_reference.py record review.json \
  --page receipt --state returned --revision SOURCE_REVISION \
  --image sketch.png --provenance 'ImageGen output and its selected reference' \
  --target 'The return date and receipt action share the summary group'
python3 -B scripts/check_visual_reference.py check review.json \
  --page receipt --state returned --revision SOURCE_REVISION
```

Run the check from the installed skill directory or use its absolute script path. Keep the record and images in the task workspace. The check requires a real local image and verifies its stored digest, declared state and starting revision. Inspect the actual distinguishing content and actions to confirm the state and ImageGen provenance. If the prerequisite is missing or the check fails, resolve it before editing that presentation. Continue independent investigation or functional verification when possible. Later rounds can run `check` without `--revision` to verify the same page, state and reference bytes against an edited source.

When generating a related or revised sketch, supply the chosen reference or relevant neighboring screens as image inputs. In the brief, say which regions, content density, relative type emphasis, shared edges, control placements and native chrome to carry over and which parts may change. With no visual input support, use a written description of those relationships and record the limitation. Open the original and candidate images together before implementing. If an essential region disappears, two controls move onto separate rows, or a focal component becomes a generic list, correct the sketch first. An approved sketch stays the target until the user or established design decision process accepts a materially different direction.

On iOS versions that support Liquid Glass, keep the applicable native navigation bar and tab bar consistent across ImageGen alternatives. Use a current native capture of the chrome when available. Before choosing a sketch, check the title and Back or Close placement, the floating tab bar, its selected tab and the content insets. Compare those same relationships in the native render. Let the system own the material and its accessibility adaptations. A presentation without a bar keeps that navigation structure. See [native design choices](native-design.md#liquid-glass-on-supported-ios).

Confirm which native components own the title, navigation, list rows and input. Save the reviewed sketch and its creation date with the screen and state it covers. If generation is unavailable, record the missing sketch and continue independent work. A sketch made after a screen was built can guide a subsequent revision. Record the implementation it was compared against and retain the actual order of work.

## Map the complete reference before building

Work screen by screen, including new modals and material states such as a selected period, a populated and empty list, or an error with a recovery action. Use the reference selected by the user. Keep a short map in the existing task notes for substantial design work.

| State | Essential part of the reference | Intended native component and data or action | Evidence or open discrepancy |
| --- | --- | --- | --- |
| Reservation ready | Time and venue, availability, ticket total, confirmation and secondary edit action | Native heading and summary, current reservation data, and the existing confirmation and edit actions | Compare the full mounted screen with a populated reservation. Check both actions in that state. |
| No times available | Empty message and a way to change the date | Native empty state and existing date selector | Verify the empty state and recover via the actual selector. |

Include structural regions such as a focal header, graph and legend, grouped details, forms, or a primary action area wherever they define the reference. Include control placement and state, reading order, grouping and emphasis. Map a useful data role to its actual source, including whether unavailable values have an intentional empty state. When a component, binding or capability is missing, record the intended result, user-visible effect and what would resolve it. Continue independently implementable work with the original reference available for review. Use clearly labeled fixtures for layout experiments and carry any unresolved essential difference into acceptance. A later sketch can explore that difference. Use it as the acceptance target only if the user selects it or the established decision process approves it.

## Prove the hardest component first

Choose the relationship the template is most likely to break, such as a dense two-column item with independently tappable actions, a chart with a legend, or a grouped form with a long field value. Render one representative populated component in its actual native screen, with realistic long content and at least two items if list rhythm matters. Open that image before reusing the layout. Verify the visible text edges and control arrangement, not just the presence of the correct slots in source. If the template centers an action or adds spacing that breaks the reference, inspect its intrinsic layout and try a supported native composition before rolling it out. Keep the essential content and controls in the design while evaluating alternatives.

## Check the first viewport

From the full reference, choose one or two landmarks that identify the main task, such as the first result, the order total or the first recent activity. Note their top edge and what is fully visible at the expected initial scroll position. When density matters, count complete repeated items. An item behind or cut by a bar does not count. Include native navigation and sheet insets. If chrome or aspect ratio differs, set the viewport expectation explicitly and compare within-content spacing as a separate check.

A layout can contain every part of the map yet push the key content out of view. Check the height contributed by headings, selectors, auxiliary actions and each template's default insets before adjusting colors or repeating the layout. Review the longest realistic label and relevant selected or toggled states. At larger text sizes allow more scrolling and reflow, and check that important content and actions remain readable and reachable.

## Compare before declaring completion

**Define what passes.** Start with the complete reference map and every visual issue the user raised. Give each issue its own check in the task notes and keep it through the final comparison. Then include the essential composition checks that the screen needs, covering placement, type hierarchy and scale, alignment, spacing or repeated-item density. Choose a target and an observable condition or tolerance before editing. Record the baseline and current observation, the image or measurement that proves it, and a status of pass, fail or unverified. For repeated rows, compare the same signed edge deltas and distances in at least two rows when available. A problem remains open if an adjacent element improves while the reported difference persists.

**Use the same viewport coordinates.** Match the viewport, renderer, appearance, language, text size, scroll position, fixture content and control states across app renders. Keep full originals. For screenshots, crop each viewport once, use the same viewport origin, and apply one proportional scale per image if needed. Record crop, scale and any missing context. Use viewport coordinates to check placement and within-component deltas to check alignment or spacing, such as `action.left − label.left`. A content-aligned close-up can help diagnose a group after you record its viewport position. Inspect the complete capture for native chrome, insets and scroll reachability. Document intentional native differences with the content checks they still need to satisfy.

**Measure the visible relationship.** Prefer `review_page` and, when exposed, `compare_page_layout` for the app's before/after geometry. Bind the image to its source revision and render context, and use the returned model paths to find the relevant template or property. Verify whether a reported frame bounds the whole control, its text layout or the visible glyphs. Use comparable edges and units on both sides. For a raster-only sketch, use crop guides or a few tight regions around the same visible glyphs or edges. Record rendered image pixels or percentages of viewport width when the logical scale is unknown. Confirm estimates at readable size and allow for raster noise. Check type role, apparent size and weight, wrapping and line spacing by eye. Use source or renderer evidence for font identity, logical font size, exact baselines and touch targets.

For example, an equipment list has a name and availability on the first line, with Details and Reserve below. Its review could use the following checks. Use the screen's own targets and units.

| Required relationship | Example pass condition | Evidence to inspect |
| --- | --- | --- |
| Details aligned with the item name | `Details.left − name.left` stays within the stated tolerance at default text size | Visible glyph edges in both rows, with one leading guide inside each item |
| Reserve aligned with availability and Details | Right edges match within tolerance and the two actions share the row at default text size | Visible labels and their vertical placement, including the Reserved state with a longer label |
| Type hierarchy | The item name remains more prominent than the metadata, and the title retains the intended prominence | Compare the visible glyph size and weight at matched scale. Verify authored type roles if available |
| List rhythm and first viewport | Repeated item intervals fit the agreed range, and the expected number of complete items clears native chrome | Same name-to-name anchors across two intervals, full viewport and last visible action |

If the images disagree with template or validator output, inspect the images at readable size and trace the owning component. Use a surgical crop, vertical guide or overlay to resolve uncertainty while retaining the full comparison.

**Correct the biggest visible issue first.** Use the first native render as the baseline. Trace the main discrepancy to the owning row, container or native component before editing. Check template slots, default alignment and intrinsic insets against the current contract and the rendered output. Correct the most consequential fixable issue or batch changes with one cause. Remeasure every selected relationship and inspect the entire affected view in the fresh render, including its lower controls and adjacent content. Record the target, observed difference, change, fresh result and pass/open state. A shorter row can leave both actions on the wrong line. Equal-width buttons can still leave an oversized gap, so compare the actual painted edges as well as the widths.

**Review adaptations in their own states.** Use a narrow supported width, larger system text or a long translation when these can change the layout. Use meaningful fixtures such as both toggle states, long values and an empty or error state. Allow natural wrapping and reflow while preserving action meaning, focus order, independent touch targets and scroll access to the last important control. Verify critical activation and data-driven transitions with an applicable app-owned test.

Plan one to three iterations per new or redesigned screen or modal, with at least one substantive source correction after the baseline. Use two or three when initial differences are substantial, a correction changes neighboring layout, or the requested quality calls for closer fidelity. A completed round requires a comparison, a source correction and inspection of a fresh full render. A repeat build or capture alone contributes no round. If a meaningful correction or comparable render is unavailable, report the incomplete round.

## Decide visual acceptance

Mark a screen visually complete only when its essential reference regions and every user-reported issue pass in the final matching-state evidence, including agreed native adaptations. Keep acceptance open for a missing or demoted key region, obscured action, incorrect selected state or data meaning, unusable text, or materially wrong placement, density or spacing. Progress on one issue cannot compensate for another failure. At the final planned round or deadline, report the exact open differences and any missing comparable capture. Check that the fix works in relevant adapted states and that final content remains reachable. A signed-in variant needs its own capture. Inspect individual screens and relevant scroll positions at readable size, even when a contact sheet documents coverage.

Record which state and source revision the image proves, the number of completed rounds, and the specific remaining discrepancies. Report visual acceptance, source checks and running-app behavior separately. A fixture screenshot can prove the intended composition. Verify a real state change or destination through the supported action in a running app or applicable app-owned test. A successful response without the intended visible result leaves the transition open.

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

Use the existing task notes for one compact record per affected presentation. Include a newly reachable materially different state even when the change was limited to navigation or data. Record the selected sketch, exact source revision and native context, full baseline and final captures, and each completed correction round. For each required relationship or reported defect, record the reference target, the final visible observation or measurement, and `pass`, `fail` or `unverified`. For nearby secondary actions, include grouping, visible text alignment, the gap between actions and the gap to the next visible section. Check the standard layout and any relevant larger-text reflow.

Show the locked ImageGen sketch, baseline and final native image together at a comparable width. Cite the record and each round that produced a fresh reviewed image. Only mark visual status complete when the required checks pass in that exact presentation. Keep missing or mismatched evidence open. A clean automatic validator, successful flow test or a shorter gap cannot resolve a visual check that still fails. State the visual and functional outcomes separately in the handoff. Keep this evidence in the app's private workspace. Explain adaptations and capability gaps. Distinguish fixture composition from the live data/navigation flow: selecting an item must populate its destination through the actual supported action before that flow can pass. Opening a destination with no selection should yield an intentional empty state, not an indefinite placeholder loader.
