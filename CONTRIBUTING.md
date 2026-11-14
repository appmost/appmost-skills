# Contributing

## Publication boundary

Prepare every tracked change, commit message, issue and pull request for public reading even while this repository is private. Apply this rule when updating these instructions, skill metadata and examples too.

Use published Appmost contracts, public documentation and synthetic fixtures. Read access to a private repository, conversation or MCP result does not authorize publishing its contents. Never include credentials, customer data, private discussions, account-specific identifiers, internal logs, signing material or confidential implementation details. Public URLs and identifiers deliberately published by their owners are acceptable.

Keep maintenance guidance general. Put private task notes and raw captures in an appropriate private location outside the skill package. If suitability for publication is uncertain, leave out the uncertain material and ask the owner while continuing unaffected work. Do not weaken these publication rules without the owner's explicit approval.

There is intentionally no AGENTS.md or private instruction overlay in this initial repository. This document is contribution guidance, not an automatically loaded agent instruction file.

## Change the right layer

Keep workflow decisions in SKILL.md. Put substantial task-specific detail in references linked from that skill. A skill must remain useful when installed alone: do not link to sibling skills or repository-only documentation for required runtime instructions.

Prefer current MCP discovery over copied tool schemas. Tool names in guides are examples whose availability must be checked. Update a guide only against the relevant runtime contract; do not infer shipping availability from a source branch or product name.

Keep both skills scoped to creating and delivering customer apps in Appmost. Add an Appmost Design skill only after its workflows have their own verified capability baseline. Never add project-format fields or workaround models to make a skill example function.

## Verify changes

Run the validation, unit-test and packaging commands in README.md. Inspect the actual archive entries. Run the affected scenarios in evals/README.md against an isolated synthetic app when an Appmost connection and rendering are available. Record what actually ran; a written scenario is not a passed behavioral test.

Check the complete staged diff before committing and every outgoing commit before pushing. Review public suitability separately from automated secret-pattern checks. Do not bypass a secret-protection rejection without explicit owner authorization. Resolve necessary changes before making a release or changing repository visibility.

Use focused pull requests after the initial bootstrap. Assign Appmost pull requests to @appfrilans and preserve other assignees. Review changes to publication guidance and release operations explicitly. CODEOWNERS requests review when GitHub review rules support it; it does not itself enforce a protected branch.

## Maintain format compatibility

Keep the five appmost-format/document metadata values in each changed skill accurate. The installed format-compatibility reference explains version axes, host-only major detection and same-major feature checks. Update the reviewed baseline only after reviewing a published, immutable source; match the source URL to the selected release and record the actual review date. Do not label the record as runtime-certified.

Preserve the format baseline/date for unrelated wording changes. Bump the skill/package version independently when packaging changed instructions. Run repository validation, unit tests and packaging, inspect the installed reference, and record any affected behavioral checks actually executed. These offline checks do not prove a backend, renderer or release feature works.

## Updating sources

Read docs/compatibility.md for the current source baseline. Fetch changing Apple and Google requirements from their official documentation at release time. Do not copy whole policy manuals into the skills or pin account-dependent eligibility thresholds in prose.

Bump plugin.json's version when publishing a changed package. An initial private commit is not a public release, and packaging locally does not publish anything.
