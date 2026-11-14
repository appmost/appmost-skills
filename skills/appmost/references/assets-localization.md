# Assets and localization

## Choose imagery for the app

Photography and cover art can carry an app's identity and help people recognize content. Use meaningful image assets when the brief calls for them; do not silently replace requested photography or artwork with generic shapes. Simple geometry is appropriate for an intentional graphic treatment or an explicitly provisional layout.

Choose by role: food/venue photography for discovery, recognizable cover art for a library, accurate supplied assets for an actual product or place, and native icons/clear data presentation for a work-focused utility. An operations dashboard does not need a decorative hero photo.

Keep changing titles, prices, timing, controls and state as native content. Text intrinsic to artwork, such as book-cover lettering, can stay in the image; retain a readable native title separately.

## Choose by available capability

Discover the tools in the current session rather than assuming a client or model can generate images.

- Use supplied or approved existing assets when identity and factual accuracy matter.
- When an authorized image-generation tool is available, use it for suitable original imagery. It may be built in, connected through another provider, or exposed by a local workflow. Follow that tool's current skill/contract for execution.
- When generation is unavailable, use suitable licensed existing imagery or an available approved image search. If no appropriate asset can be obtained, give a concrete image brief and identify the remaining asset need while continuing independent app work.
- Keep provider setup, API syntax and credentials in the relevant provider workflow. Treat image generation as an optional capability and keep the Appmost workflow portable across clients.

Illustrative generated imagery is suitable for a fictional prototype. It is not evidence of an actual venue, person, inventory item or product appearance. Prefer supplied accurate photography for those factual roles.

## Art direction and real files

Before generating or selecting assets, identify their roles and intended crops: hero, thumbnail, detail, background or supporting illustration. Choose a coherent subject, lighting/material treatment and framing across a related set. Leave useful room around the focal subject when the same asset must serve different ratios.

A useful image brief includes subject, intended UI role, aspect ratio, focal area, style and text/brand constraints. Do not bake application controls or changing labels into a mockup and use that as a content image.

Move selected files into the supported project asset location. Keep their identity, provenance and usage rights, and identify generated demo material honestly. Optimize the delivery format and resolution for the rendered size; retain a useful editable/source master when appropriate.

List referenced targets and actual bundle files separately. Bind the exact resource identity expected by the current contract, including its real extension where required. add_asset_and_bind_image can declare/bind an asset; a tool whose name includes fetch may still only transform a payload. A binding does not establish that bytes exist or were downloaded.

Use the host's supported importer or the existing bundle resource convention. Do not invent a new asset mapping field, embed credentials in an image URL or copy private customer imagery into shared examples. Keep source assets separate from screenshots and review exports.

## Cropping, themes and verification

Use the actual Appmost image fields available in the current contract, such as scaleMode and focalPointX/focalPointY where exposed. Inspect the image in its real card, detail and thumbnail, not only as a standalone file.

Check both the width and height of the image owner. A fixed phone-height hero stretched across a tablet can turn a well-framed photo into a severely cropped strip. Choose a coherent wider composition and supported dimensions; a width cap is useful only if the resulting image ratio and neighboring content also work.

Photographs can usually keep their natural colors in both appearances while surrounding UI adapts. When replacing an asset, update a deliberate darkModeTarget variant too, or remove that stale override if the same new photograph should serve both appearances. Do not silently show the previous image in dark mode.

Review the actual decoded image, visible subject, stretching, crop, native text/overlay contrast and relevant light/dark/wider contexts. Check carousel bounds and intentional peeks after changing a parent width. Use an existing clipping option only when the composition requires it and its behavior is verified.

Validate actual file references and confirm the final native render. Treat file assets, native icon names and navigation targets according to their types; a broad validator's error is not a reason to create fake image files for page IDs or symbols. Check actual file presence even when a validator reports success. Preserve unresolved tool findings and report the independent evidence accurately.

## Localized content

Use English localization source text and keys, with translations in the relevant localization resources. Reuse an existing English key with the same meaning. When replacing a key, update callers and preserve/migrate its translations.

Use the current translation tools to synchronize referenced keys and supported languages. Validate missing entries, unused keys and language declarations; an automatic key sync does not supply correct translated copy.

Review real localized renders, especially long labels, buttons, narrow columns and multiline text. Let text wrap and grow. Use the same language and text-size context for before/after comparisons. Inspect applied text-size metadata rather than assuming a requested size overrides a project lock.

## Export

Save only to an explicitly selected, app-accessible location. Respect the renderer's new/empty-directory and overwrite contract. Keep individual images plus the returned manifest when a contact sheet alone cannot establish content, source and context.

A screenshot used in store material must depict the actual requested app and state. Use synthetic demonstration data and review surrounding context as well as visible labels for privacy. Never paint moved controls into an exported image and present that as a corrected app layout.
