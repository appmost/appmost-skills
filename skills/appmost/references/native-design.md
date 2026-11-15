# Native Appmost design choices

This guide states the Appmost package's design preferences, supported authoring choices and current Apple guidance separately. Apply iOS conventions to iOS; use the target platform's own rendering and conventions for Android and web.

## Native controls first

| Intent | Prefer in Appmost | Avoid |
| --- | --- | --- |
| Top-level sections | Existing native tab/page navigation and supported tabbar settings. | A row of bottom buttons that duplicates or hides the real tab bar. |
| Hierarchical detail | Ordinary push navigation and system back behavior. | A drawn back button inside page content plus the native back control. |
| Modal exit | The page's native dismissal control, using the standard X appearance where supported. | A custom Close text row added solely to imitate navigation chrome. |
| Save / finish | A distinct native confirmation action where the contract supports it. | Treating an X as an implicit save or destructive cancellation. |
| Current-page actions | Native navigation/toolbar items or an anchored native menu when suitable. | A permanent stack of large CTA cards for every action. |
| Choice / input | The corresponding supported picker, toggle, stepper, segmented control or text input template. | Simulated native controls built from decorative labels and images. |
| Temporary feedback | Existing native dialogs or an appropriate existing toast. | Adding temporary status rows to unrelated configuration/content panels. |

Apple's current toolbar guidance favors standard Back and Close symbols. The package preference is an X for a modal close. Keep its action semantics correct: close preserves progress, cancel may discard, confirm commits, and back traverses navigation. If unsaved changes need a decision, use the supported confirmation flow rather than silently discarding them. [Apple toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [close role](https://developer.apple.com/documentation/swiftui/buttonrole/close).

A SwiftUI API being available does not mean that an Appmost payload exposes it. Use the existing page dismissal and bar-item contract first. If the required native option is not exposed, report that capability gap instead of inventing a field or rewriting the runtime.

## Group settings at the page or container level

For a standard settings form, prefer the page's inset grouped list style. Let that style own the shared group background and outer corners. In Appmost, explicit row backgrounds, corner radii, borders or vertical outer margins can make adjacent rows render as independent cards even when the page already uses inset grouped. Keep those overrides unset on ordinary grouped rows.

Use actual header/footer roles for section titles and supporting text. A hidden-background content label is not automatically a section footer. Put separators between related rows and leave the final row's lower edge clear.

For a group that needs custom composition or a custom surface, use one container row per group with child rows. Give the background and rounding to that parent; keep child surfaces neutral. Choose either page-owned grouping or an intentionally composed group.

Inspect at least two adjacent settings rows together. They should share one continuous surface, with rounded corners only on the group's outer contour. Check the group boundary, footer and separator alignment in light/dark and larger text.

## Liquid Glass on supported iOS

Modern standard bars and controls adopt the platform appearance through the host/runtime. Let that native layer own its material. Keep ordinary content surfaces, cards and lists readable and restrained; a modern app does not need glass on every section.

Where the current Appmost button contract exposes glassEffect, its choices can include glass, clearGlass and prominentGlass. Verify those values and actual renderer support before authoring:

- glass: a restrained functional control requiring a legible material.
- clearGlass: a functional control over rich imagery/media when readability holds.
- prominentGlass: the primary functional action that needs emphasis.

These are supported-style choices, not instructions to convert every button. Do not place an opaque rounded fill or a second faux-glass capsule behind a system glass control. Do not hide the native shared background merely to force a static color match. A mini player or tab accessory should use its supported native host rather than duplicate the tab bar.

Use platform-appropriate fallback styling on older iOS and other renderers. Prefer semantic colors and inspect light/dark, bright media, larger text and available contrast/transparency settings. Do not disable system adaptation or claim an accessibility variant was tested without evidence. [Apple materials](https://developer.apple.com/design/human-interface-guidelines/materials), [Liquid Glass adoption](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass).

## Discover the actual Appmost choices

Check the current schema/contract for these existing concepts before editing. Names below identify fields to look up, not a complete ready-to-apply payload:

| Concern | Contract concepts to inspect | Verification |
| --- | --- | --- |
| Dismissal | allowDismissButton, modal presentation and existing dismissal actions. | Exactly one appropriate visible exit, correct action and no lost edits. |
| Toolbar appearance | Existing bar items, appearanceStyle, grouping/spacing and hidesSharedBackground where exposed. | Native spacing/material preserved; primary emphasis intentional. |
| Glass buttons | glassEffect and supported renderer/OS behavior. | Actual native material rather than an image or translucent fill. |
| Top-level navigation | tabbarItems, page relationships and upsert_tabbar_settings where exposed. | Tab selection reaches tab roots; tabs are not ordinary push targets. |
| Readable wide content | maxCellWidth where exposed, applied coherently to the relevant row family. | Phone still fits; tablet content has an intentional shared readable width. |
| Content spacing | outerMargins, contentPadding, template insets and container spacing. | Actual measured edges and natural text growth. |
| Content clearance | review_page safeAreaFrame, navigationAlignmentFrame, visible accessory/sticky frames. | Important content clears the real chrome without double subtraction. |

## Insets have owners

The reported content bounds account for native navigation, tab bars, supported accessories and sticky content in that preview. Treat that as the baseline. Do not add a guessed tabbar-height spacer or another hardware safe-area inset to every row.

For short decision, onboarding or account screens, prefer a supported native pinned action area when primary and subordinate secondary actions should stay reachable while content scrolls. Discover the current host fields and count the actual footer and safe-area clearance once so the last content scrolls clear. Check long text, accessibility sizes, keyboard and compact heights; use a supported adaptive fallback if the footer would consume the viewport. Keep contextual list actions with their content.

Background imagery may extend under translucent chrome while readable content and tappable controls remain clear. These are different layout decisions. Check the first and last scrollable rows, keyboard/form state and any active player/accessory in the actual render.

Use native adaptation on wider layouts only where supported and appropriate. A rich full-width landing page should remain full-width; do not put it into a narrow split primary simply because the device is wider.
