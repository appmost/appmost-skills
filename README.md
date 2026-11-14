# Appmost skills

Practical agent workflows for creating, reviewing and delivering apps through Appmost's MCP tools.

| Skill | Use it for |
| --- | --- |
| [appmost](skills/appmost/SKILL.md) | Build and edit Appmost apps; choose components; connect navigation and data; validate and improve actual rendered pages. |
| [appmost-release](skills/appmost-release/SKILL.md) | Prepare store material, verify exact source and build evidence, and carry out explicitly authorized distribution operations. |

The skills target **Appmost**. Appmost Design is a separate product with a different capability set; a dedicated Design skill is outside this initial package. These workflows do not develop the Appmost editor's implementation.

## Install

An existing Appmost MCP connection is required. A skill supplies workflow knowledge; it does not start Appmost, grant account access or install an MCP server.

In Codex, ask the built-in skill installer:

```text
Install the appmost skill from https://github.com/appmost/appmost-skills/tree/main/skills/appmost
Install the appmost-release skill from https://github.com/appmost/appmost-skills/tree/main/skills/appmost-release
```

The repository is initially private, so installation requires GitHub access and authorization from the rights holder. All rights are reserved; no open-source license is granted. For other Agent Skills hosts, install the complete selected skill directory using that host's supported mechanism. Read [installation](docs/installation.md) for local folders, private-repository access and the optional plugin package.

Example requests:

```text
Use $appmost to build a small library app with a searchable list and a detail page.
Use $appmost to review the current app on a phone and tablet and fix the measured layout issues.
Use $appmost-release to prepare an internal TestFlight release; inspect readiness before starting a build.
```

## What the workflows improve

- Discover the connected host's actual tools and current schemas before authoring.
- Use focused template queries and structured edits instead of repeatedly transmitting an entire project.
- Review actual images and layout measurements, then make narrow revision-guarded corrections.
- Distinguish a preview image, a build receipt, review acceptance and current store availability.
- Preserve existing authorization boundaries, project data and concurrent changes.

The appmost skill includes native-control preferences, modern iOS Liquid Glass guidance, Appmost-specific inset rules, worked design recipes and a measured visual-review routine.

The skills use public MCP contracts and synthetic examples. They neither copy the full format specification nor guarantee that a renderer, backend or store review will succeed.

## Validate and package

Python 3.10 or later is sufficient; repository tooling has no third-party Python dependencies.

```sh
python3 -B scripts/validate.py
python3 -B -m unittest discover -s tests -v
python3 -B scripts/package.py
```

The packager creates reproducible skill ZIPs under `.build/packages/`, includes only validated skill contents and never overwrites an existing output. Use a fresh `--output` directory for a new packaging run. Tests keep temporary files under `.build/tests/` unless `TMPDIR` selects another project-local location.

The root [plugin.json](plugin.json) and [marketplace catalog](.agents/plugins/marketplace.json) offer an optional skills-only plugin. They contain no credentials or bundled MCP connection. Nothing in this repository installs itself or changes global agent settings.

Read [the initial synthetic trial](evals/initial-trial.md) for actual findings and verification limits.

See [compatibility and sources](docs/compatibility.md), [evaluation scenarios](evals/README.md), and [contribution and publication rules](CONTRIBUTING.md). Repository checks validate structure and packaging; meaningful skill quality still needs the documented behavioral and visual evaluation.
