# Design and rendering review

## Establish a visual direction

Identify the app's primary task and content hierarchy. Choose a coherent type scale, semantic colors, restrained surfaces and purposeful imagery. Reuse a consistent component family. Keep primary actions obvious and touch targets usable; avoid turning every section into a detached card.

Choose navigation from the content. Rich dashboards, hero sections and multi-section landing pages belong in full-width stack/tab flows. A split primary is appropriate for a compact selection list that directly drives related detail content. A wider viewport alone is not a reason to add split navigation.

## Budget actual geometry

A visible edge includes safe/content bounds, ancestor spacing, row outerMargins, row contentPadding and intrinsic template insets. Count each contribution once. Equal authored padding on different templates does not prove aligned visible content.

At a visible surface boundary, application text must never touch, cross or straddle the painted edge. Check every facing side against the actual row, card, native group or ancestor that paints the surface. Include time/value columns and nested text. Keep outer surface alignment and internal text clearance as separate constraints; moving the surface with outer margins does not add internal clearance. Count verified intrinsic template insets once.

Give each gap one owner. A card's outside alignment and its internal content padding are separate decisions. Preserve intentional carousel peeks, icon columns and media treatment. Use the actual navigation guide where measured; do not impose one hard-coded navbar margin on every device.

minCellDynamicHeight is a minimum, not the rendered height. Natural text wrapping, controls, template insets, margins and padding all matter. Let noninteractive text grow with content. Keep interactive hit areas usable; Appmost's current guidance uses at least 44 logical points. Do not enlarge every text row to a control's minimum or add padding in proportion to text length.

Do not hide excessive spacing by clipping text or applying a small maximum height. A template that renders one label does not gain a subtitle because extra label data was supplied. Confirm the selected template's content capacity.

## Review loop

1. Discover list_preview_contexts and choose supported variants for the actual target.
2. Use review_page when available. Record its revision, renderContext, model paths, measured frames and image path. Keep comparison coordinates in one logical space.
3. Inspect the complete page at readable size. Check alignment, text hierarchy, truncation, controls, contrast, media cropping, empty space and navigation. Inspect meaningful states, not just the initial populated page.
4. For supported narrow alignments/gaps, call plan_layout_adjustment with the returned nodes, exact revision and same context. Pass its plan unchanged to apply_layout_adjustment. Read the measured result and verification flags.
5. For other changes, edit existing source properties through a guarded operation. Render again and verify affected elements and surrounding content.
6. Inspect the final images after the final source edit. Keep before/after exports in separate directories when the renderer can reuse filenames.

A stale context, unsupported row relationship or verification failure calls for fresh inspection, not a modified plan. Do not infer row indexes from visual order. Resolved x/y coordinates are measurements, not a new absolute-positioning model.

## Coverage and evidence

Prioritize the narrowest supported phone, an intended wider composition, relevant light/dark appearances and long translations. Review larger system text where supported and inspect metadata for a project text-scaling lock. Use contact sheets for page coverage and individual images for detailed judgment.

Label native SwiftUI, other native renderers and web output accurately. A web render does not verify native layout. A preview image does not verify a store binary, authenticated backend or personal device. Check actual device/renderer support before proposing a matrix.

Where run_preview_test supports isolated input callbacks, exercise the relevant control and assert its effect on dependent content against the exact saved source. Logical row visibility can include offscreen content; inspect a supported scroll export before claiming the last content is reachable above floating native chrome. A separately authored empty-state fixture verifies that state, not the tap or transition that would produce it. Preserve the original source-bound receipt and identify unsupported actions explicitly.

Use app-owned rendering rather than desktop capture or UI automation. If the required renderer is unavailable, finish source checks and report the precise unverified visual variant.

Platform reference: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/). Fetch relevant current component guidance when a task depends on platform-specific behavior.

## Surface-padding corrections

Use existing inner-padding fields on the editable surface owner and render again. Preserve the card/group outer edge, natural wrapping and interactive hit areas; do not shrink or clip text to manufacture clearance. For continuous native groups, respect the group boundary and avoid inserting separate vertical gaps or rounded backgrounds between every row.

Read each automatic adjustment contract. A plan that translates a whole row while conserving total padding does not add internal space against its own background. Do not use such a plan as a surface-inset fix. Use an eligible existing edit/review operation instead. If the actual painted owner or its editable spacing cannot be established, retain the source and report that specific correction as unverified; do not claim a safe automatic fix.
