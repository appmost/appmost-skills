# Operation safety and recovery

## Separate the effects

| Operation | Typical effect | Required understanding |
| --- | --- | --- |
| Status/list/detail | Reads current readiness or provider facts. | The exact account and whether the result is current or historical. |
| Prepare | Validates and returns a bound plan/token; some workflows present native approval. | Destination, source, audience, costs/effects and expiry. It is not execution. |
| Build/upload/submit/release | May spend build credits, sign, distribute, request review or publish. | User authorization covering the exact effect plus the valid protocol confirmation. |
| Expire/halt/cancel/rollback | Changes an existing delivery or workflow. | The exact target and consequences; related installations or store versions may remain. |
| Status/reconcile/readback | Resolves the original operation and fresh provider state. | A failed response is not proof that the preceding write failed. |

Names and available operations differ by host. Discover exact schemas instead of constructing calls from this table. Keep dependent operations sequential and preserve the provider's concurrency locks.

## Confirmation and source guards

Read the current payload and source identity through the supported operation. Supply the exact document path/revision required by the tool. Do not fabricate a fingerprint or infer source-to-binary identity from matching version numbers.

Read the prepared summary and verify all bound fields against the requested release. Pass the returned IDs, immutable plan and one-use confirmation unchanged. Tokens can expire or be invalidated by an account/source/destination change. Never log their values or put them in public artifacts.

If the request already authorizes the exact operation, continue using that authorization. If it authorizes only preparation or an internal audience, obtain approval for any further effect before executing it. Complete the preparation first so that approval refers to a concrete result.

## Uncertain responses

A network timeout, startUnconfirmed, submissionUnconfirmed or equivalent result can mean the write was accepted. Preserve the original operation ID and read/reconcile that operation. Do not retry the start, automatically prepare a replacement or switch accounts.

After a definitive rejection, correct the identified cause and follow the supported recovery contract. After a confirmed provider receipt, use fresh reads for current state rather than treating a later transport error as proof the delivery disappeared. Bound polling and stop on a terminal result; report an unresolved operation precisely without looping unchanged requests indefinitely.

## Destructive delivery controls

TestFlight expiry affects the exact beta build, not the public App Store version. A Google Play halt changes a specific release/track and may require a serving fallback; installed copies remain installed. A build-job cancellation can stop the workflow but does not promise a refund or withdraw an already delivered artifact.

Discover and follow the exact read/prepare/execute/readback contracts for these controls. Never substitute credential extraction, a hand-written provider API client or a different operation to bypass an Appmost denial.
