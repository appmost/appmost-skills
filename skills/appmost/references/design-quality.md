# Design quality checks

Use this during actual image review. It is a set of decision criteria, not a requirement to emit a long report or invent measurements. Correct concrete defects and preserve the app's identity.

## 1. Task and composition

Map the real content roles and required visible affordances first. A featured item should have a deliberate headline, supporting metadata, description and primary action appropriate to its subject. Keep the useful button, meaningful color and recognizable emphasis while correcting geometry. A text-only brief can draw character from typography and composition; it does not require reducing its main item to the same small icon row as the secondary list.

Can someone identify the screen's purpose, current location and next useful action? Does the composition fit its actual content and app category? Name the one characteristic visual choice: relevant imagery, a strong content hierarchy, informative data treatment or a deliberately calm utility. Remove decoration without a purpose.

Avoid recurring generated defaults: identical card stacks on every page, excessive gradients, giant empty headers, arbitrary KPI tiles, ornamental eyebrows, repeated CTA buttons and glass on every surface. These can be appropriate only when they communicate real information; a generic style habit is not a reason.

## 2. Platform and behavior

Use native navigation, tab bars, modal dismissal, menus and available controls. Check that no custom content duplicates system chrome. Verify that X, back, cancel and confirm perform their distinct intended actions. Compare each top-bar icon and accessible name with its actual destination; follow [top-bar actions and destinations](navigation-data.md#top-bar-actions-and-destinations) rather than assuming an icon is truthful. On iOS prefer the platform's modern material when available; other platforms retain their own native conventions.

## 3. Hierarchy and density

Use a small coherent type hierarchy and semantic foreground roles. Keep body copy readable and meaningful labels visible. System typography is a strong default for controls; brand expression can live in content, imagery and limited display moments.

Check actual row heights, clear section grouping and a restrained primary action. Separate content-driven height from interactive hit regions. Avoid compensating for long text with excessive padding or truncation.

Inspect the boundary below controls such as filters, segmented controls and action buttons, including the visible distance from the control's painted edge to the next visible heading, chart or content group. Check actual visible neighbors when conditional content is shown or hidden; spacing owned only by a hidden block can disappear with it. Check painted-edge gaps between adjacent independent controls too, including filled or outlined buttons and input fields. Give each gap one owner using existing margins, container spacing or a spacer; preserve meaningful grouping and intentionally joined controls such as segmented controls and steppers. Judge the rendered result at normal and larger text sizes rather than applying a universal gap value. Absence of clipping alone does not establish balanced spacing.

For nearby secondary text-only (clear) actions, prefer a shared horizontal row when their roles belong together and complete titles and usable hit areas fit. Avoid a vertical sequence of visually identical links that obscures grouping or competes with the primary action. When narrow width, translation or larger text prevents a readable row, move actions to the content or navigation context they belong to, or use clearly separated groups. Preserve every destination and verify the actual render at normal and larger text sizes.

## 4. Geometry

Choose a final visible grid, then subtract verified template/ancestor contributions. Check the painted outside edge of a standalone button against unboxed text and headings, separately from the centered button label. Header and icon-row templates can already contain side insets; another matching outer margin can double them. Review the distance between actual text bounds across a section boundary: a header's intrinsic top spacing plus minimum height plus an authored margin can create a large hole even when each value seems modest. Use a supported content-sized label when a heading template's built-in rhythm does not fit; keep control hit areas and natural wrapping.

Text must have visible internal clearance from every facing edge where its background or border changes. This includes leading times, trailing values, wrapped descriptions and text near rounded corners. Identify the actual painted owner: the row, card, continuous native group or ancestor. Outer margins do not create an inset inside that surface. Judge the actual text and painted bounds; zero authored padding is not proof of contact when the template already supplies an inset. Correct the existing inner-spacing owner and preserve wrapping, hit areas and the intended outer grid.

Measure shared content edges, card interior versus exterior grids, image crops, repeated row frames and useful horizontal spacing. Count template/parent insets once. Use the reported unobscured content bounds and actual navigation alignment guide. Check first/last content and any floating accessory.

Fix the source owner, not a screenshot. An intended shared edge needs measured evidence; when the host cannot measure it, label the visual judgment and its limits.

## 5. Readability and adaptability

Review relevant light/dark appearances, long translations, larger text and the narrowest supported viewport. Inspect icon-only controls for meaningful accessibility labels where the contract exposes them. Verify contrast from actual colors when available rather than claiming a numeric result from a screenshot alone.

Treat reduced transparency, contrast and motion settings through the supported native behavior. Do not claim those states were exercised unless they were. An unavailable setting is a verification limit, not a fabricated pass.

Check complete values and words at larger text sizes. A multi-column metric can wrap a currency amount into misleading fragments, and a fixed-width carousel can split a person's name inside a word. Use a supported adaptive composition or enough measure for those meanings; do not solve it by disabling text scaling, truncating a key value or assuming that natural growth alone establishes readability.

## 6. Refine and stop

Rank findings by impact: unusable navigation or obscured content first, then native conventions, hierarchy/alignment, then decorative polish. Make one coherent correction batch, render again and inspect affected plus adjacent content.

Finish when requested flows work within the tested scope, critical visual defects are resolved and the design has a coherent purpose and character. Name remaining unsupported contexts. Avoid endless arbitrary restyling or adding a universal rule for every isolated observation.

A useful handoff is short: the main improvements, actual reviewed variants/artifacts, and precise verification limits.
