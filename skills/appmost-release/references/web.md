# Appmost web hosting

Use this guide only when the user requests web deployment. A local web screenshot is not a deployed site.

Discover web_publish_status and the available destination/list/setup operations. Reuse the app's existing account and Google/Firebase connection. Authentication setup is a separate user flow; do not extract provider credentials or create a second Firebase publishing implementation.

Confirm the intended existing destination. Creating a site or changing a saved destination requires the corresponding user authorization and the exact prepare/execute protocol where exposed. Do not select a guessed project or site because a name looks similar.

For a preview, inspect the prepared source snapshot, destination, lifetime and effect. Use the available web_publish_prepare_preview and web_publish_create_preview contract only within the approved scope, then poll the original job with web_publish_get_job. A preview deploy is an external deployment even when it has an expiry.

For live promotion, verify the exact successful preview, saved source relationship and current live state. Where exposed, web_publish_prepare_release and web_publish_release promote the bound preview without rebuilding. A request for a preview does not authorize promotion to live.

Rollback uses the exact supported previous deployment and current-state plan. It is a live-site change. Use web_publish_list_deployments and the prepare/rollback contract where available, and read back the destination/version afterward.

Keep the returned job/version and checked URL together. Read freshness matters: a historical deployment receipt does not prove that a URL currently serves that version. Missing tools or provider access call for a precise prepared handoff, not a parallel CLI deployment.
