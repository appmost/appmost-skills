# Initial synthetic skill trial

Date: 2026-11-14. Method: author-run smoke test using the candidate appmost skill, an isolated two-page Reading Room app and the connected Appmost native MCP. This is not an independent model evaluation or a controlled with/without comparison.

## Actually exercised

- Read runtime bootstrap/agent contracts and filtered template results.
- Built synthetic content with MCP scaffold and structured authoring operations.
- Ran structure, navigation, UX, viewport-fit and app-complete checks.
- Used a shipped empty native template copy after the minimal scaffold failed native opening.
- Applied changes through exact-revision native decoding and saves.
- Reviewed actual native phone, tablet, largest-text and dark-detail exports.
- Replaced an unsuitable header template after measuring a 16pt difference in leading content edges.
- Capped editorial content width for a readable tablet composition and used native selectable-row navigation.

Final native source revision: 934152fa37b1ce690cddfaf1bdd4491c207c98059b72dc10272f43605ae0237e. The five final payload checks returned no errors or warnings.

## What changed in the skill

The MCP workflow now distinguishes a working scaffold from a complete native-openable package, warns that friendly template names/fallback payloads do not establish rendered content capacity, and requires exact supported enum values. The existing design-review loop supplies the source of truth for actual alignment rather than identical padding numbers.

The phone text edges align on the intended 20pt content grid after correction. Tablet content uses an intentional common width cap rather than a screen-wide action strip.

## Limits and follow-up

The largest-text capture shows natural wrapping and content extending beyond the visible viewport. Scrolling and the below-fold action were not exercised, so this does not establish complete accessibility support. A measured native navigation title/control produced a small-target warning; the tool's reported rectangle alone does not establish the actual hit region.

A filled-button variant lost its visible caption during the wider native rendering experiment despite retaining the declared title. The final basic example uses native row navigation. This observation needs separate runtime/contract reproduction; it is not a reason to add a universal design workaround to the skill.

No real backend request, personal device, build, upload, store review or public deployment was used. The previously open project/page was restored after native trials. Screenshots and the local demo are retained outside this repository for owner feedback; no private project content is copied into this report.

The 15 scenarios remain a future behavioral evaluation set. Repository unit tests verify package structure and safety, not the quality of all generated apps.
