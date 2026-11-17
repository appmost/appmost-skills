# Navigation, state and data

## Navigation

Use stable page/row/action IDs returned or accepted by the current contract. For a new destination, prefer a structured operation such as add_page_with_navigation when available so the page and link stay consistent. Check every root tab, pushed destination, back path and return-to-root action after changes.

Use ordinary pages and existing actions for stack/tab navigation. Reserve panel replacement routing for an intentionally selected detail inside an eligible split container. Do not create a parallel menu hierarchy or new serialized navigation fields to express unsupported behavior.

## Top-bar actions and destinations

Match an action's symbol and accessible name to what it actually does. A notification bell must open a real notification experience, never act as a disguised shortcut to Profile or another tab. Omit optional utility actions when the app has no useful matching destination; do not invent messages, unread badges or empty feature shells to justify an icon.

For a short, self-contained utility opened from the top bar, prefer a native modal sheet or supported popover that returns to the same context on dismissal. A notification inbox or filter task can fit this pattern when it has real content and a clear exit. Prefer push navigation for an actual detail in the current hierarchy, and a menu for immediate commands. Back, Close, Save and in-place actions retain their own semantics. Do not convert every top-bar action into a modal or add one merely because a button is in the navigation bar.

Keep peer sections in the tab bar or sidebar. An explicit, clearly labelled cross-link may select a tab when the flow needs it; do not push a duplicate tab root or use an unrelated utility symbol. Check the action destination and return path in addition to the screenshot. Respect an existing navigation choice during layout-only work; propose a flow correction separately when it changes behavior.

This is a design recommendation, not a format requirement or automatic rewrite. Use the host's existing presentation fields and native dismissal controls. Apple's [modality guidance](https://developer.apple.com/design/human-interface-guidelines/modality) limits modal presentation to a clear task benefit; its [toolbar guidance](https://developer.apple.com/design/human-interface-guidelines/toolbars) distinguishes actions and hierarchical navigation from top-level tab navigation.

## Variables and bindings

Choose root or page scope deliberately. Verify each binding against a declared variable, object model, integration and operation. Use supported upsert/binding tools and validate_data_flow_bindings or the current equivalent. A declaration is not proof of a successful request or a parsed response.

For repeated-row selection, do not assume that a similarly named root variable receives the selected item. Check the host's selection scope. Use distinct names for the row selection and shared destination state; pass the selected object through existing navigation parameters or explicitly copy it before navigation. Verify two different items and a missing selection. A separately populated destination fixture does not test that transfer.

Keep authored form values, preview values, persistent backend state and test fixtures distinct. Preserve loading, empty, error and populated states where they affect the user's flow. Do not insert real credentials, sensitive customer records or production-only identifiers into a demonstration.

## Backend work

Use the current integration and endpoint contracts. During UI generation, prefer isolated mock/test data and local validation; do not start Firebase, deploy functions, execute arbitrary JavaScript or call write-capable production endpoints merely to populate a preview.

When the user explicitly requests a real endpoint test, confirm the target, environment and effect from the existing request and contract. A network test may mutate remote state. Use the app's supported endpoint test only within that authorization, and inspect sanitized results instead of displaying secrets.

## Isolated test data

Discover list_current_project_test_data and the host's selection/testing operations. Do not assume hosted MCP or Appmost Design supports local test datasets. Preserve the normal backend selection and restore a temporary preview selection through the supported operation after testing.

If available, prepare_test_run validates an exact saved source and returns a plan; it does not prove a build ran, a simulator launched or an authenticated session exists. run_preview_test exercises only its advertised supported callbacks and conditions. Read its restrictions before proposing interactions.

Use app-provided isolated tests for the requested states. Do not drive the editor UI or inspect a personal mobile device as an implicit testing fallback. Report unsupported interactions precisely and continue feasible validation.
