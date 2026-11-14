# Format compatibility

## Read the version axes

The frontmatter metadata in [this skill](../SKILL.md) is the compatibility record:

| Value | Meaning |
| --- | --- |
| metadata.version | Version of the skill instructions/package. |
| metadata.appmost-document-version | Document major this workflow targets. |
| metadata.appmost-format-reviewed | Exact public semantic format release reviewed when maintaining the instructions. |
| metadata.appmost-format-review-date | Date of that reference review. |
| metadata.appmost-format-reference | Immutable public specification URL used for the review. |
| metadata.appmost-format-review-kind | Evidence scope; reference-review is not a full runtime certification. |

A stored project version such as versions/1, the app's marketing/build version, the skill version and the semantic format release are separate. The review baseline is neither a minimum nor a maximum supported minor release. It does not certify every feature or renderer. An app need not store its semantic reference release; never invent a formatVersion field or infer one from the skill metadata.

## Check before changing or delivering a document

1. Inspect the intended document's documentVersion, the applicable public format release/registry when a semantic target is specified, and the running MCP's schema and capability contracts. When available, list_appmost_schemas identifies the host's schema family; bootstrap/agent contracts describe its current authoring operations.
2. Compare the document major with metadata.appmost-document-version. If it differs or cannot be established, preserve the document and keep the work read-only until an appropriate supported workflow is established. Do not stamp a new documentVersion, migrate, strip fields or downgrade the app to match this skill.
3. A host that advertises only v2 or appmost-core-v2 establishes a major, not an exact 2.x release. Report the semantic host version as unknown unless the contract actually supplies it. A public reference release alone does not prove a production binary or deployed MCP implements it.
4. Check each needed field, row/action/value type, integration and operation against the chosen target and the current host. Use public introducedIn and per-platform support metadata where available; confirm newer or host-specific capabilities through their actual contracts. A newer reviewed/public release does not make older hosts support its additions.
5. Older or newer minor releases with the same major do not automatically block useful work. Use the confirmed compatible subset, preserve unrelated existing content, and validate the changed scope. If a required feature is unavailable, explain that specific gap and continue independent work. Agree on an alternative when it materially changes the requested behavior.
6. Keep declared format validity, MCP edit capability, preview behavior and target runtime/build evidence separate. Run the available checks relevant to the change; report missing target-platform or exact-release evidence explicitly. Delivery still requires source-bound build/provider evidence and the user's existing authorization.

For example, maxCellWidth is introduced in public format 2.2.0. When targeting an older reference, do not emit it merely because the skill was reviewed against 2.2.0. A newer same-major host may expose additional capabilities; inspect those contracts rather than claiming the entire newer release is verified.

## Maintain the compatibility record

Review a published specification, its release manifest and relevant registry/schema changes before advancing the baseline. Pin the specification URL to a public commit, verify the selected release's artifact hashes, and update the reference/date together with affected guidance. Do not copy an unpublished local release or a private source revision into this record.

Run repository validation, unit tests and standalone packaging. Exercise affected synthetic behavior where suitable tools are available and record its exact source, host and renderer separately. Keep reference-review as the evidence kind unless a separately reviewed verification policy supports a stronger claim. A smoke test does not certify every feature of a format release.

A wording-only skill update may change the skill/package version while leaving the format baseline/date untouched. Do not automatically synchronize the baseline with the latest release number. The repository checks verify metadata consistency and packaging; they do not contact the host, certify runtime compatibility or prove that a newer format was tested.
