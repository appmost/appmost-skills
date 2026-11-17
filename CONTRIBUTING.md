# Contributing

## Publication boundary

Prepare every tracked change, commit message and shared repository discussion for public reading even while this repository is private. Apply this rule when updating these instructions, skill metadata and examples too.

Use published Appmost contracts, public documentation and synthetic fixtures. Read access to a private repository, conversation or MCP result does not authorize publishing its contents. Never include credentials, customer data, private discussions, account-specific identifiers, internal logs, signing material or confidential implementation details. Public URLs and identifiers deliberately published by their owners are acceptable.

Keep maintenance guidance general. Put private task notes and raw captures in an appropriate private location outside the skill package. If suitability for publication is uncertain, leave out the uncertain material and ask the owner while continuing unaffected work. Do not weaken these publication rules without the owner's explicit approval.

There is intentionally no AGENTS.md or private instruction overlay in this initial repository. This document is contribution guidance, not an automatically loaded agent instruction file.

## Change the right layer

Before adding a rule, use [guidance placement](docs/skill-design.md#where-guidance-belongs) to choose its owner and affected consumers. Keep workflow decisions in SKILL.md. Put substantial task-specific detail in references linked from that skill. A skill must remain useful when installed alone: do not link to sibling skills or repository-only documentation for required runtime instructions.

Prefer current MCP discovery over copied tool schemas. Tool names in guides are examples whose availability must be checked. Update a guide only against the relevant runtime contract; do not infer shipping availability from a source branch or product name.

Keep both skills scoped to creating and delivering customer apps in Appmost. Add an Appmost Design skill only after its workflows have their own verified capability baseline. Never add project-format fields or workaround models to make a skill example function.

## Verify changes

Run the validation, unit-test and packaging commands in README.md. Inspect the actual archive entries. Run the affected scenarios in evals/README.md against an isolated synthetic app when an Appmost connection and rendering are available. Record what actually ran; a written scenario is not a passed behavioral test.

Check the complete staged diff before committing and every outgoing commit before pushing. Review public suitability separately from automated secret-pattern checks. Do not bypass a secret-protection rejection without explicit owner authorization. Resolve necessary changes before making a release or changing repository visibility.

## Development and promotion

Use staging for development and candidate testing; main is the stable installation branch. Commit and push scoped development updates to staging so candidates are preserved across machines. Do not create pull requests or require PR reviews for this repository.

Before promoting a candidate, review public suitability and the full outgoing diff, run the documented structural tests and package inspection, and run the affected behavioral checks when skill behavior changes. Record the exact tested commit or byte snapshot, renderer/context and known limitations. A one-shot API prompt comparison is a component experiment, not proof of skill discovery, reference loading or MCP use.

Promote the same verified content from staging to main with a normal direct push after validation. Recheck both branch heads first; if concurrent changes require integration, preserve them and validate the affected result on staging before promotion. Never force-push, discard concurrent work or silently promote an untested variant. If repository rules prevent the direct workflow, report the exact conflict rather than opening a PR as a fallback.

Review changes to publication safeguards, packaging and execution or release authority explicitly before promotion. This workflow does not authorize changing repository visibility, licensing, releasing packages or executing app builds, uploads or publishing; those operations retain their existing authorization requirements. Branches share the repository's visibility: staging is a development channel, not a private environment inside a public repository.

## Maintain format compatibility

Keep the five appmost-format/document metadata values in each changed skill accurate. The installed format-compatibility reference explains version axes, host-only major detection and same-major feature checks. Update the reviewed baseline only after reviewing a published, immutable source; match the source URL to the selected release and record the actual review date. Do not label the record as runtime-certified.

Preserve the format baseline/date for unrelated wording changes. Bump the skill/package version independently when packaging changed instructions. Run repository validation, unit tests and packaging, inspect the installed reference, and record any affected behavioral checks actually executed. These offline checks do not prove a backend, renderer or release feature works.

## Updating sources

Read docs/compatibility.md for the current source baseline. Fetch changing Apple and Google requirements from their official documentation at release time. Do not copy whole policy manuals into the skills or pin account-dependent eligibility thresholds in prose.

Bump plugin.json's version when publishing a changed package. An initial private commit is not a public release, and packaging locally does not publish anything.
