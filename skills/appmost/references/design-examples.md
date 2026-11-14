# Worked design examples

These are synthetic authoring recipes, not frozen project JSON or screenshots of a verified app. Use them to reason about a design, then discover the current templates and render the actual result. Reuse the decisions that fit the user's app rather than imposing one visual theme on every project.

## Library: useful content with native tabs

Brief: help someone continue reading, browse a collection and find saved items.

Composition: native Library / Saved / Settings roots; a concise page title; one current item with relevant cover imagery; a compact progress/context line; a useful list of other items. Detail opens in the normal navigation stack. Keep settings as a native-feeling grouped form.

Common generated failure: four oversized gradient cards, a second fake tab bar at the bottom, repeated Read buttons and an unrelated hero metric. Every screen becomes the same stack of detached boxes.

Improvement: keep Appmost's native tab bar; make the current item's image/type treatment the memorable element; let each list row navigate through its supported action; keep one meaningful primary action. Use the real bottom content boundary rather than appending a tabbar-sized spacer.

Discover only the components needed, for example:

```json
{"query":"media","rowRole":"content","limit":5,"includeRowPayload":false,"includeSections":false}
```

Pass those arguments to list_row_templates after confirming its input schema. Broaden the query or remove a filter if no exact match exists. Fetch the selected payload only after choosing the appropriate template. Inspect its label/image capacity and renderer mapping.

Check: one tab bar, stable root selection/back navigation, aligned covers/headings/list text, compact repeated rows, readable long titles, and the last item's clearance above native chrome. Review the actual image; a good composition description is not a rendered result.

## Modal filter: native X and meaningful confirmation

Brief: present a short filter task from a toolbar item.

Use an existing supported modal page/sheet and native controls for the choices. Provide the native X dismissal appearance and a separate Apply action only when choices are staged. Choose whether dismissal preserves or discards unapplied changes from the user's intended interaction; make any necessary decision explicit.

Common generated failure: draw a large Close pill inside the body, add a second custom navigation header, and use X to silently submit or discard a form.

Improvement: let native chrome own title/exit/action placement. Use a standard existing picker/toggle/segmented template. Keep the body focused on the choices, not on reproducing a sheet's controls. Verify the one appropriate exit and the actual effect of Apply versus close.

## Media page: restrained glass

Brief: browse a collection and control playback.

Let the native tab/navigation/accessory host provide glass. Use strong artwork and clear content hierarchy beneath it. An exposed clearGlass control may fit over rich media, but standard readable content remains an ordinary surface. Use prominent emphasis for the most important action only.

Common generated failure: translucent material on every card, a drawn mini player over the system accessory, tinted text over bright artwork and a broad opaque plate that hides native material.

Improvement: remove duplicated chrome/material owners; keep the app's native accessory; simplify content surfaces; verify contrast over the actual artwork and the first/last visible content around the accessory. Label any untested playback behavior separately from the reviewed layout.

## Insets: equal numbers, unequal result

Suppose a plain hero owns a final 20pt leading gutter, while a text template already contributes an intrinsic 16pt inset. Giving both rows another 20pt does not align them: that text would start at 36pt.

After confirming the actual template inset, author only the remaining 4pt for that text owner. This is an illustrative budget, not a global rule that every text row needs 4pt. Another template, nested container or renderer can differ.

Use review_page to compare actual content frames. For an eligible small edge correction, use the returned node IDs with plan_layout_adjustment, then pass the returned plan unchanged to apply_layout_adjustment. Recheck the reference, translated text wrapping, row height and surrounding content.

## Dense checklist: natural content height

A checklist should support scanning, readable multiline labels and comfortable taps. A large minimum height plus vertical padding can make an ordinary list feel empty even when each number looks reasonable alone.

Discover the actual template and remove redundant spacing owners. Keep hit regions large enough, let long text grow naturally and preserve intentional section gaps. Never fix the perceived emptiness by clipping labels or shrinking every row to the same rigid height.

Check repeated rendered row frames at standard and larger text, plus translated labels. minCellDynamicHeight alone does not establish the final size.

## Wider layout: adapt the task

A rich home page keeps full-width content with appropriate readable constraints and a deliberate composition. A compact selection list with related detail can use an eligible split layout. These are different tasks, not phone versus tablet skins.

Review the actual supported wider viewport. Preserve navigation and make the main content useful without turning the page into a gallery of duplicated cards or stretching body text across the entire display.
