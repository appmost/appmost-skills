---
name: appmost-release
description: "Prepare and verify delivery of apps built with Appmost: App Store/TestFlight and Google Play readiness, store material, exact build evidence, and explicitly authorized uploads or publishing. Use for Appmost customer-app releases; not Appmost Design releases or ordinary app layout editing."
license: "Appmost Skills Limited Use License 1.0. See LICENSE.txt."
metadata:
  author: "Appmost"
  version: "0.1.9"
  appmost-document-version: "2"
  appmost-format-reviewed: "2.2.0"
  appmost-format-review-date: "2026-11-14"
  appmost-format-reference: "https://github.com/appmost/project-format/blob/ba2dd848a8ee36864fbdc4c275f8df1e22851a6c/spec/2.2.0.md"
  appmost-format-review-kind: "reference-review"
---

# Deliver an Appmost app

Requires an existing Appmost MCP connection. Discover actual host, tool and renderer support; store operations also require access to the selected account.

Read [format compatibility](references/format-compatibility.md) before changing or delivering a document. The metadata records the targeted document major and exact public format reference reviewed; it does not certify every feature or renderer. Check current host capabilities as well as the document version.

Prepare a reviewable, source-specific release and carry out only the external effects authorized by the user. Preserve existing account authentication and provider safeguards. A request to inspect readiness does not authorize a build or upload.

## Identify the requested outcome

Determine the target app, platform, account/organization, environment, version/build and audience from the request and current read-only state. Distinguish preparation, build, internal distribution, store review and public launch. For Apple builds, resolve export eligibility separately from the tester audience, following the user's instructions and workspace policy; internal tester groups do not imply an internal-only export. App Store eligibility alone does not authorize review submission or public launch. Reuse authorization already present in the conversation; ask only when a required action or destination remains unapproved or ambiguous.

Discover the current host's tools. A source-code capability, historical job or other Appmost product does not establish an executable tool. Read [operation safety and recovery](references/operations.md) before any build, upload, review submission, release, expiry, halt or cancellation.

## Prepare a concrete release

1. Inspect the exact intended saved document and revision. Preserve unsaved or concurrent work. Delivery operations must use the final source required by their contract; do not silently save, migrate, bump versions or change signing metadata as a side effect of preparation.
2. Run relevant app/source validation. Inspect representative actual app renders and important states, then confirm that assets and localized copy reflect that source.
3. Inspect existing account, signing and destination readiness through sanitized read-only status tools. Do not retrieve credentials or replace the user's identity.
4. Prepare store copy, truthful screenshots, review access/instructions, declarations and release notes for the applicable platform. Read [store material](references/store-material.md) and fetch current official requirements.
5. Bind source, preview context, build and provider evidence using [delivery evidence](references/delivery-evidence.md). Mark missing links explicitly.

Read only the relevant platform guide:

- [Apple and TestFlight](references/apple.md)
- [Google Play](references/google-play.md)
- [Web hosting](references/web.md), when the user requests an Appmost web deployment

## Execute within the approved scope

Use the exact discovered prepare/execute/readback sequence. Inspect the prepared summary before consuming its confirmation. Match the account, source, destination, audience and effect to the user's existing authorization. A protocol token is not a substitute for that authorization.

Use the same operation ID after a timeout, lost response or uncertain provider result. Reconcile/read status before considering another write. Do not create a new plan merely to escape a consumed token or an uncertain start.

If source or destination changes after preparation, inspect the new state and prepare again only after resolving any earlier uncertain operation. Continue independent metadata or evidence work while an external path is blocked.

## Report what actually happened

Separate local validation, visual review, build completion, upload acceptance, provider processing, review acceptance and current availability. Give the exact operation/build identity and provider check time where available. Use fresh provider reads for present-tense availability; label historical receipts as historical.

Do not describe a pending review as published, a local preview as a store binary, or a cancelled workflow as a store withdrawal or credit refund. If the host lacks a requested review/public-launch operation, provide the exact prepared manual handoff instead of implementing a second publishing client.

Keep credentials and private account/customer information out of reusable reports. Use app-owned domain tools and existing authentication; do not use computer control, mailbox inspection or personal-device access as an implicit verification fallback.
