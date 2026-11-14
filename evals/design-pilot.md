# Reading Room multi-page design pilot

Date: 2026-11-14. Method: author-run smoke test through connected Appmost native MCP, using the appmost skill. This extends the first synthetic trial; it is not an independent evaluation or a with/without comparison.

## Scope

A fictional reading app with native Library, Saved and Settings tabs, three pushed book details, native switch bindings, a bookmark toolbar declaration and an empty Saved state. Original synthetic text and native geometric jacket artwork; no customer material or backend connection.

The design continues the first trial's calm, content-led direction. Native tab/navigation ownership, content gutters, a common wider-content cap and text growth are exercised. The example's palette, artwork and density are not universal design rules.

Default source revision: ace099da28855101370f1542af4baa085fa2ae125f02696eddfe2ffa91dd2e1e

Empty-state source revision: e2bba838c011317e47d6539d74c0ab006b7e8eb37af71355ec2071be9ef30b36

## Actual evidence

- Four final payload gates passed without errors or warnings: app complete, references, data bindings and navigation.
- Six phone pages rendered in both light and dark, with native SwiftUI rendering and English content.
- Library/detail rendered in iPad portrait and landscape, both appearances.
- Twelve source-bound native test exports: six switch/conditional-visibility checks, three largest-text captures, two bottom-scroll captures and one empty-state capture.
- Native switches drove progress and description bindings off, then on; the dependent rows were asserted absent, then present.
- Largest text used the actual accessibility XXXL category with scaling unlocked. Bottom-scroll exports reached the last collection item and the end of the reading excerpt.
- Empty-state assertions used a separate default-value source variant. No bookmark tap was simulated or claimed.
- Ordinary test-data selection and the previous editor context were restored.

Selected source packages, images and original receipts are retained privately outside this skill repository for owner feedback.

## Reusable lesson

Use supported isolated input callbacks and inspect their effects on the dependent page. A static binding check and a picture of an enabled switch do not establish behavior.

Distinguish logical conditional visibility from the current viewport. For large text, exercise supported scrolling and inspect the last content above native floating chrome. Distinguish an authored state fixture from a tested state transition.

This produced a focused addition to references/design-review.md. It did not require a longer SKILL.md, a new design skill or new format fields.

## Limits and next decision

Bookmark taps, return-to-root actions and persistent saved state were not executed by the available bounded transport. VoiceOver, measured hit regions, keyboard access, reduced transparency/motion, long translations, Android, web, store binaries and backend behavior remain unverified.

The tablet is intentionally sparse; the owner should assess density, hierarchy, typography and cover treatment before any subjective choice becomes reusable guidance. This trial does not prove the skills improve every generated app. The broader 15-scenario behavioral set remains unevaluated.

## Owner feedback: adjacent settings rows

The owner found the initial Settings rows looked like separately rounded cards. The page already used inset grouped; explicit row backgrounds opted those rows out of continuous grouping. Static validation and the prior review did not catch that visual defect.

The corrected authoring removes row surface overrides, uses a real footer role and draws one divider between the two switches. Native light/dark, larger-text and iPad portrait/landscape exports show one shared outer contour. Eight focused native callback/text-size exports pass, including the switch effects on dependent pages. The footer remains caption-sized in the largest-text export, so full text adaptation is not established.

Corrected default revision: 6c52d61baf9502f375d7da78c71a3187ddda9a581e6301028347c719099d309c

Corrected empty-example revision: 184bbc45b0b5171a9b361f4204c60673e9e41fa973aee0a6610a86587c3fc5d4

The reusable guidance lives in native-design.md, linked from the worked example. The new settings-grouping scenario brings the set to 16; this guided author-run correction does not establish a blind evaluation of that set.
