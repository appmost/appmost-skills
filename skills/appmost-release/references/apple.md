# Apple and TestFlight

## Readiness

Inspect the Appmost project's final source, app/bundle identity, version/build, build environment and existing Apple organization. Use sanitized status/team/app/build reads where exposed. Do not dump Keychain data, signing keys or certificate bytes.

Fetch the relevant current [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and [App Store Connect Help](https://developer.apple.com/help/app-store-connect/) for the app's features and requested release. Verify completeness, accurate metadata and review access. Claims about privacy, payments or account behavior must match the actual app and its integrations; unresolved declarations require the owner's factual input.

## Internal TestFlight through Appmost

When exposed, testflight_publish_status supplies readiness; testflight_prepare_current_project prepares the exact current saved source and selected organization/audience. Inspect its summary. Use testflight_publish_current_project only for an already authorized build/upload with its exact required arguments and confirmation.

Read the original upload/job through the supported status operation. testflight_get_upload is a historical job receipt; use testflight_list_builds and testflight_get_build where available for current processing, expiry and group state. An upload is not proof that every requested tester can install the build now.

Keep internal and external beta audiences distinct. Do not widen an internal request into external beta distribution or App Store submission. The current host may expose TestFlight operations without a public App Store review/release operation.

## Review and public release

Discover whether the running host exposes the exact requested App Store operation. If absent, prepare the app identity, existing processed build, localized metadata, declarations and review notes for an authorized owner to complete in App Store Connect. Do not assume an unavailable command exists or create a second delivery implementation.

Treat review submission and public launch as separate effects. Read the selected release mechanism and provider status before describing a launch as held, scheduled or live. Verify the final state through the provider, including the exact app/build and check time.

## Expiry and recovery

For an explicitly requested beta expiry, use the available testflight_get_build, prepare/expire and expiry-status operations. Preserve its operation ID after uncertainty and reconcile before another write. Expiring a beta does not withdraw the public store version or remove installed copies immediately.
