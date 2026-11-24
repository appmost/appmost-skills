# Apple and TestFlight

## Readiness

Inspect the Appmost project's final source, app/bundle identity, version/build, build environment and existing Apple organization. Use sanitized status/team/app/build reads where exposed. Do not dump Keychain data, signing keys or certificate bytes.

Fetch the relevant current [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and [App Store Connect Help](https://developer.apple.com/help/app-store-connect/) for the app's features and requested release. Verify completeness, accurate metadata and review access. Claims about privacy, payments or account behavior must match the actual app and its integrations; unresolved declarations require the owner's factual input.

## Transfer a project and connect Apple credentials

Share the saved `.appmostapp` package through the authorized private repository or file channel. Include the intended bundle identifier, Apple Developer Team ID, and the Appmost build needed for the workflow. Export project files and non-secret setup details separately from signing credentials.

For a different operator publishing to the same Apple team, confirm the authorization and scope first. An App Store Connect Team Key applies to all apps in that team within its role. For access limited to one app, use an app-scoped publishing connection that keeps the team's key on the operator's server when that capability is available. Otherwise the credential owner can perform the upload. An app-scoped individual Apple API key does not support Apple's provisioning endpoints. [Apple API key scope and limitations](https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api)

For a move between Macs under the same authorized team custody, use the original Apple-issued `.p8` through the organization's approved secret store. Provide the Team ID, Issuer ID and Key ID as setup metadata. Keep the private key out of project archives, repositories, chats, and MCP arguments or results. Avoid extracting an existing key from Keychain to assemble an export. Apple makes each key available for download once. If the original is unavailable or a separately authorized operator needs team-level access, the credential owner can provision a dedicated key and manage its revocation.

On the receiving Mac:

1. Sign in to Appmost and discover its live MCP tools. Use a user-owned local `.p8` file with private permissions such as `0600`. Pass its absolute path as `keyPath` along with `organizationId`, `teamId`, `issuerId`, and `keyId` to `app_store_prepare_import_credentials` when available. The organization name must be new or have no Apple credentials.
2. Check the returned organization, team and key ID. After the authorized operator confirms the destination, call `app_store_import_credentials` with the same inputs and the one-use confirmation token. Require `savedReadbackVerified`. If the save response is uncertain, read `testflight_publish_status` and check the organization and `hasAppStoreConnectCredentials` before retrying.
3. If the host lacks the import tools, use Appmost's **Build credentials → Manage organisations → Open from file**. After either import, check that the saved organization can read the intended app through `testflight_list_apps` when available. Local import verifies the saved credentials. Apple access, distribution signing and Appmost plan and licence eligibility require their own checks.

## App Privacy

Check the privacy policy URL and the Apple data disclosure as separate fields. Base the disclosure on the selected build's behavior, bundled SDKs, and verified handling by the app's services and partners. Resolve unknown retention or collection with the owner before declaring `DATA_NOT_COLLECTED`. [Apple App Privacy details](https://developer.apple.com/app-store/app-privacy-details/)

Use an available App Privacy tool that can read answers and publication state for the exact app. If the host has the App Store Connect CLI's `asc web privacy` commands, they use a separate Apple web session. Check it with `asc web auth status`. If sign-in is needed, prefill the known Apple Account and verified organization where possible and let the owner enter the password and two-factor code in the interactive terminal. For accounts with multiple organizations, match the intended organization to the CLI's provider list and pass its numeric ID with `--provider-id`. The signing team identifier is a separate value. After a provider selection error, check session status before restarting sign-in.

Read the current answers and publication state, then inspect the change plan before saving. If a read displays `DATA_NOT_COLLECTED` with an unpublished or unknown state, use the plan to determine whether the answer still needs to be created. After an authorized save, read the answers back. When authorized to publish the disclosure, publish it and verify both the exact answers and the published state on a fresh read. App Privacy publication, App Review submission and public app release are independent operations. If the web session is unavailable, give the owner the direct App Privacy page and the prepared answers. [Apple's publishing steps](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/) · [App Store Connect CLI workflow](https://github.com/rorkai/app-store-connect-cli-skills/blob/main/skills/asc-submission-health/references/app-privacy.md)

## TestFlight through Appmost

Resolve two independent choices before preparation: the authorized tester audience (internal or external) and export eligibility (`APP_STORE_ELIGIBLE` or `INTERNAL_ONLY`). Follow the user's instructions and workspace policy. A request for internal testers does not itself select the restricted internal-only export.

When App Store eligibility is required, explicitly pass `allowAppStorePublicRelease: true` to both testflight_prepare_current_project and testflight_publish_current_project. Verify the prepared summary and Apple's processed `buildAudienceType` before reporting the requested delivery complete. Do not omit the flag and rely on a default. If the selected account, plan or host cannot provide the requested eligibility, report that blocker rather than falling back to internal-only or bypassing entitlements. Use the restricted export only when the requested workflow and applicable owner policy permit it; preserve its intended availability for supported plans.

When exposed, testflight_publish_status supplies readiness; testflight_prepare_current_project prepares the exact current saved source and selected organization/audience. Inspect its summary. Use testflight_publish_current_project only for an already authorized build/upload with its exact required arguments and confirmation.

Read the original upload/job through the supported status operation. testflight_get_upload is a historical job receipt; use testflight_list_builds and testflight_get_build where available for current processing, expiry and group state. An upload is not proof that every requested tester can install the build now.

Keep internal and external beta audiences distinct. Do not widen an internal request into external beta distribution or App Store submission. The current host may expose TestFlight operations without a public App Store review/release operation.

## Review and public release

Discover whether the running host exposes the exact requested App Store operation. If absent, prepare the app identity, existing processed build, localized metadata, declarations and review notes for an authorized owner to complete in App Store Connect. Do not assume an unavailable command exists or create a second delivery implementation.

Treat review submission and public launch as separate effects. Read the selected release mechanism and provider status before describing a launch as held, scheduled or live. Verify the final state through the provider, including the exact app/build and check time.

## Expiry and recovery

For an explicitly requested beta expiry, use the available testflight_get_build, prepare/expire and expiry-status operations. Preserve its operation ID after uncertainty and reconcile before another write. Expiring a beta does not withdraw the public store version or remove installed copies immediately.
