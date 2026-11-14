# Delivery evidence

Record evidence in ordinary project notes or the tool's existing receipt format. Do not add evidence fields to the .appmostapp document schema.

| Claim | Evidence needed | Insufficient substitute |
| --- | --- | --- |
| Source prepared | Intended saved document, exact revision/fingerprint and validation result. | Filename or matching marketing version alone. |
| Layout reviewed | Actual reviewed image, renderer/device/appearance/language/text-size context and source identity. | Static JSON validation or an uninspected export. |
| Inputs tested | Supported isolated test receipt tied to exact source and dataset. | A test plan that was merely prepared. |
| Build complete | Owned build job and actual artifact/provenance receipt. | A queued workflow or a preview render. |
| Upload accepted | Verified provider receipt for the exact app/artifact/audience. | Successful local packaging. |
| Available now | Fresh provider read of processing, expiry, audience/track and release state, with check time. | Historical upload completion. |

Use get_delivery_evidence if exposed to join supported source/render/build/provider receipts. Inspect missing evidence and caveats. A tool accepting an image receipt does not make it visually approved; local integrity metadata is not a signed store attestation.

A concise report can say:

```text
Source: final saved revision and fingerprint from the tool.
Reviewed: actual image paths and applied renderer/context.
Tested: supported scenarios and dataset; unavailable checks named.
Build/upload: exact original job and provider artifact identity.
Current state: fresh provider status and check time, or explicitly unknown.
Remaining action: the precise manual or newly authorized next step.
```

Keep confidential details in the appropriate private project record. For a public example, use synthetic names and remove account-specific identifiers and raw logs. Report only what the actual evidence supports.
