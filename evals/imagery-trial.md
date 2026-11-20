# Imagery and varied native examples

Date: 2026-11-14. This was a guided, author-run native trial.

## Coverage

The trial exercised image consistency across views, readable content over photography, horizontal collections, and data-heavy layouts. Three generated raster assets were optimized as JPEG at their original dimensions, added as app resources and inspected in native output.

## Observed corrections

- A fixed-height image cropped too tightly on a wider viewport. Limiting content width and increasing the image area's height preserved the focal content.
- Replacing an image required checking appearance-specific overrides so light and dark mode used the intended resource.
- A horizontal collection inside a width-constrained parent needed its clipping behavior reviewed. At the largest text size, wider items preserved whole words and a single column kept long values readable.
- Removing a decorative block brought the primary data into view earlier.
- Guarded edits to the affected fields let the trial verify the changes against existing source.

## Evidence and limits

The final review covered 30 standard-text native variants across phone and tablet, including light and dark appearance. Nine larger-text and scroll exports supplemented that review. The exports established visual coverage. Interaction, full accessibility, Android, web, physical devices, store binaries and provider-backed behavior remain unverified.

Two hash seeds produced identical edit operations. Applying the operations to fresh copies and reading the saved source back reproduced the final payloads and revisions.

App-complete, navigation and binding checks passed. The asset validator reported missing images for non-image values and accepted a deliberately absent image in a negative control. Independent checks verified the actual image references on disk, and native exports showed that the new images decoded.

The guided trial did not independently evaluate the broader behavioral scenario set. Original source packages, captures and receipts are retained privately.
