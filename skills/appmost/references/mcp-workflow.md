# Efficient Appmost MCP workflow

## Choose the correct editing surface

| Surface | Typical operations | Effect |
| --- | --- | --- |
| Supplied payload | scaffold_appmost_bundle, bundle_to_payload, structured page/row/variable tools, apply_appmost_patch | Returns transformed data. It does not establish that the user's open document changed or that assets were saved. |
| Open Appmost document | get_current_project_payload, apply_current_project_patch and supported editor domain operations | Can save the original document and register Undo. Bind to the document and current revision required by the tool. |
| Output bundle | payload_to_bundle or the supported bundle I/O adapter | Writes the selected payload/assets using that adapter's actual contract. Verify the resulting path. |
| External delivery | Platform-specific status, prepare, execute and readback | May build, spend credits or distribute. Requires authorization for the actual effect. |

Discover tools/list first. list_edit_capabilities describes authoring capabilities; it does not prove the running host exposes every runtime, billing or distribution operation.

## Limit context and calls

Read bootstrap/agent guidance once per relevant host/context. Query the template catalog by content role or supported filter, inspect the shortlisted results and use their returned payloads. Read exact input schemas before composing arguments. A friendly template title or supportsChildRows flag does not guarantee that the returned fallback row has that content capacity. Inspect its actual type, labels and children; verify the native result. Keep exact returned enum values rather than deriving a plausible token from a number. Avoid transmitting full catalogs or whole documents for a row-level question.

Batch independent, read-only discovery when the client supports it. Keep edits, save operations, revision reads and dependent rendering sequential. Do not run concurrent mutations against the same document or derive a second patch from a revision already consumed by the first.

Use structured page/row/action/binding tools when they enforce the relationship being changed. A validated tool is preferable to a raw path edit. For a necessary path edit, use returned model paths and exact existing field types; preserve unrelated properties. Validate its result before saving or rendering.

## Existing document transaction

1. Inspect the intended document and its revision, including unsaved work.
2. Identify only the source owners needed for the change.
3. Prepare a narrow patch against that revision; include expectedDocumentPath and expectedRevision wherever the operation requires them.
4. Apply once. Inspect the returned saved path/revision and validation result.
5. Render or test the new source. If a guard fails, inspect fresh source and recompute the change.

A returned revision is opaque; do not construct one or assume that matching filenames establish identity. Failed or uncertain saves are not permission to switch to an unguarded path. Preserve the user's concurrent edits.

## New app

For a native-openable document, prefer a supported native starter/template copy that supplies the existing document metadata. A minimal scaffold is a working authoring payload, not proof of an openable native package. If opening reports missing metadata, preserve the original project and use the supported creation path; do not invent ownership fields or copy an account identity. Define pages, stable IDs, root navigation and shared variables with the current schema. Add real content and useful states. Keep bundle assets beside the output using the supported adapter. Do not infer current semantic format support from an example or skill version.

## Final verification

Select checks based on the changed content: structure and references; navigation; data-flow and integration bindings; assets; localization; viewport fit and UX. Report warnings according to their meaning. Layout warnings are review signals, not permission for indiscriminate normalization.

Use a fresh app-owned render after the final relevant source change. Keep screenshot paths, source revision and context together. Readbacks and image inspection establish only the behavior they actually exercise.
