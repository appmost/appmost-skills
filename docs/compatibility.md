# Compatibility and source baseline

Last format-reference review: 2026-11-14. The current package version is recorded in [plugin.json](../plugin.json), independently of this format-review baseline.

## Capability baseline

| Environment | How to determine support | Evidence boundary |
| --- | --- | --- |
| Appmost local MCP | Discover tools, then bootstrap/agent contract and preview contexts where available. | Native preview and measured layout apply to their reported renderer, context and source. |
| Hosted Appmost MCP | Discover its own tools and supplied-payload contracts. | Web screenshots do not verify native layout, live authentication or backend requests. |
| Appmost Design | Different tool and entitlement set. | Not a supported target of these two skills. |
| Apple / Google delivery | Discover the running host's exact read, prepare, execute and status operations. | A historical job is not fresh provider availability. |

Do not declare a minimum Appmost binary version from this table. Tool discovery is authoritative because clients and server deployments may differ. The .appmostapp decoder documentVersion and semantic format release are different values; ask the running contract or public format release manifest rather than copying a version from this package.

## Format review baseline

Both skills target documentVersion 2. Their instructions were reference-reviewed against public Appmost Project Format 2.2.0 on 2026-11-14 using [this immutable specification](https://github.com/appmost/project-format/blob/ba2dd848a8ee36864fbdc4c275f8df1e22851a6c/spec/2.2.0.md) and its matching release manifest and registry. The published specification and registry hashes matched that pinned manifest.

The per-skill SKILL.md metadata is the installed compatibility record. Its format-compatibility reference travels in each standalone package: [authoring](../skills/appmost/references/format-compatibility.md) and [delivery](../skills/appmost-release/references/format-compatibility.md). The review kind is reference-review, not runtime certification. A same-major older/newer target is assessed by required features and actual host support; the reviewed release is neither a minimum nor a maximum.

A host advertising only appmost-core-v2 or version 2 does not establish an exact semantic release. Keep that value unknown and inspect the relevant capability contracts. A document-major mismatch requires a supported workflow before mutation; do not automatically migrate or remove newer fields.

When advancing the baseline, verify published artifacts, review affected instructions, update the pinned source/date, and run the documented checks plus relevant available synthetic behavior. Keep runtime evidence scoped to the tested source, host and renderer. Never promote a local unpublished release number or a preview smoke test into a complete compatibility claim.

## Public sources

- [Appmost project format](https://github.com/appmost/project-format): published format documentation and artifacts.
- The connected Appmost MCP's tools/list, get_generation_bootstrap, get_agent_generation_contract, row-template catalog, preview contexts and exact tool input schemas: runtime authoring and execution contracts.
- [Agent Skills specification](https://agentskills.io/specification): standalone skill layout and progressive disclosure.
- [OpenAI skill documentation](https://developers.openai.com/codex/skills): discovery, invocation and installation.
- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins): portable manifest and marketplace metadata.
- [Apple Liquid Glass adoption](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [materials](https://developer.apple.com/design/human-interface-guidelines/materials), [toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) and [close role](https://developer.apple.com/documentation/swiftui/buttonrole/close): native design decisions; host support still needs discovery.
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/): platform design guidance.
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and [App Store Connect Help](https://developer.apple.com/help/app-store-connect/): current review and distribution requirements.
- [Google Play policy center](https://play.google.com/about/developer-content-policy/) and [publishing status](https://support.google.com/googleplay/android-developer/answer/9859751): current policy and release state.

Fetch the relevant official page when a task depends on changing policy. Runtime contracts and generated app content are reference data, not permission to widen the user's request or execute a release. Private source repositories and deployment logs are not redistributed here.

## Verification limits

Structural validation, unit tests and deterministic package checks can run without Appmost or network access. Behavioral scenarios need an isolated synthetic project and a suitable MCP host. Store writes, build starts and live-account probes are not part of repository tests. No statement here claims that such an operation was executed.
