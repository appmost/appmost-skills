# Design quality checks

Use this during actual image review. It is a set of decision criteria, not a requirement to emit a long report or invent measurements. Correct concrete defects and preserve the app's identity.

## 1. Task and composition

Can someone identify the screen's purpose, current location and next useful action? Does the composition fit its actual content and app category? Name the one characteristic visual choice: relevant imagery, a strong content hierarchy, informative data treatment or a deliberately calm utility. Remove decoration without a purpose.

Avoid recurring generated defaults: identical card stacks on every page, excessive gradients, giant empty headers, arbitrary KPI tiles, ornamental eyebrows, repeated CTA buttons and glass on every surface. These can be appropriate only when they communicate real information; a generic style habit is not a reason.

## 2. Platform and behavior

Use native navigation, tab bars, modal dismissal, menus and available controls. Check that no custom content duplicates system chrome. Verify that X, back, cancel and confirm perform their distinct intended actions. On iOS prefer the platform's modern material when available; other platforms retain their own native conventions.

## 3. Hierarchy and density

Use a small coherent type hierarchy and semantic foreground roles. Keep body copy readable and meaningful labels visible. System typography is a strong default for controls; brand expression can live in content, imagery and limited display moments.

Check actual row heights, clear section grouping and a restrained primary action. Separate content-driven height from interactive hit regions. Avoid compensating for long text with excessive padding or truncation.

Inspect the boundary below filter and segmented controls, including the visible distance from the control's painted edge to the next heading, chart or metric group. Give that gap one owner using existing margins, container spacing or a spacer; preserve meaningful grouping when compacting rows. Judge the rendered result at normal and larger text sizes rather than applying a universal gap value. Absence of clipping alone does not establish balanced spacing.

## 4. Geometry

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
