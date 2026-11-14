"""Portable validation and package boundaries."""
from __future__ import annotations
import json
import os
from pathlib import Path
import re
import subprocess

SKILL_TOP_LEVEL = {"SKILL.md", "LICENSE.txt", "references", "agents", "scripts", "assets"}
TEXT_SUFFIXES = {".md", ".txt", ".py", ".json", ".yaml", ".yml", ".svg", ".toml", ".sh"}
SECRET_PATTERNS = [
    ("private key", re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})")),
    ("OpenAI-style secret", re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{24,}")),
    ("AWS access key", re.compile(r"(?:AKIA|ASIA)[A-Z0-9]{16}")),
    ("bearer credential", re.compile(r"(?i)authorization:\s*bearer\s+[A-Za-z0-9._~-]{20,}")),
    ("credential-bearing URL", re.compile(r"https?://[^/\s:@]+:[^/\s@]+@")),
    ("private workstation path", re.compile("/" + "Users/" + r"[^\s/]+/|/" + "home/" + r"[^\s/]+/|/" + "private/var/folders/")),
]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
VERSION = re.compile(r"\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?")

class CheckError(ValueError):
    pass

def within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False

def visible_files(root: Path) -> list[Path]:
    """Include tracked ignored files; otherwise include unignored sources."""
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    try:
        top = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, env=env, check=True)
        if Path(top.stdout.strip()).resolve() == root.resolve():
            result = subprocess.run(
                ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
                capture_output=True, env=env, check=True)
            return sorted({root / os.fsdecode(p) for p in result.stdout.split(b"\0") if p})
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    result = []
    for base, dirs, names in os.walk(root, followlinks=False):
        for name in list(dirs):
            path = Path(base) / name
            if path.is_symlink():
                result.append(path)
                dirs.remove(name)
            elif name in {".git", ".build", "__pycache__"}:
                dirs.remove(name)
        result.extend(Path(base) / name for name in names if name != ".DS_Store")
    return sorted(result)

def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    parts = path.read_text(encoding="utf-8").split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise CheckError("SKILL.md requires YAML frontmatter")
    result = {}
    for line in parts[1].splitlines():
        match = re.fullmatch(r"([a-z][a-z0-9_-]*):\s*(.+)", line)
        if match:
            key, value = match.groups()
            if key in result:
                raise CheckError(f"duplicate frontmatter key: {key}")
            if value.startswith('"'):
                try:
                    value = json.loads(value)
                except json.JSONDecodeError as exc:
                    raise CheckError(f"invalid quoted scalar: {key}") from exc
            result[key] = value
    return result, parts[2]

def skill_files(skill: Path) -> list[Path]:
    result = []
    for path in sorted(skill.rglob("*")):
        relative = path.relative_to(skill)
        if path.is_symlink():
            raise CheckError(f"symlink in skill: {relative}")
        if not path.is_file():
            continue
        if relative.parts[0] not in SKILL_TOP_LEVEL:
            raise CheckError(f"unexpected packaged path: {relative}")
        if any(part in {".git", ".build", "__pycache__"} or part.startswith(".env")
               for part in relative.parts):
            raise CheckError(f"private/generated packaged path: {relative}")
        if not within(path, skill):
            raise CheckError(f"packaged path escapes skill: {relative}")
        if path.suffix not in TEXT_SUFFIXES:
            raise CheckError(f"unreviewed binary/type in skill: {relative}")
        result.append(path)
    return result

def check_links(path: Path, boundary: Path) -> list[str]:
    errors = []
    for target in LINK.findall(path.read_text(encoding="utf-8")):
        target = target.strip().split(" ", 1)[0].strip("<>")
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        destination = path.parent / target
        if not within(destination, boundary):
            errors.append(f"link escapes install boundary: {target}")
        elif not destination.exists():
            errors.append(f"missing link target: {target}")
    return errors

def scan_text(text: str) -> list[str]:
    return [name for name, expression in SECRET_PATTERNS if expression.search(text)]

def validate_repository(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    try:
        manifest = json.loads((root / "plugin.json").read_text())
        if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            errors.append("plugin.json: unexpected schema")
        if not NAME.fullmatch(manifest.get("name", "")):
            errors.append("plugin.json: invalid name")
        if not VERSION.fullmatch(manifest.get("version", "")):
            errors.append("plugin.json: invalid version")
        if not manifest.get("description"):
            errors.append("plugin.json: missing description")
        catalog = json.loads((root / ".agents/plugins/marketplace.json").read_text())
        entries = catalog.get("plugins", [])
        if len(entries) != 1:
            errors.append("marketplace: expected this repository's one plugin")
        for entry in entries:
            source = entry.get("source", {})
            if entry.get("name") != manifest.get("name"):
                errors.append("marketplace: plugin identity mismatch")
            if source.get("source") != "local" or source.get("path") != "./":
                errors.append("marketplace: plugin must resolve from this repository root")
            if entry.get("policy") != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
                errors.append("marketplace: unexpected installation policy")
    except (OSError, ValueError, TypeError) as exc:
        errors.append(f"plugin/catalog: {exc}")
        manifest = {}

    skills_root = root / "skills"
    skills = sorted(path for path in skills_root.iterdir() if path.is_dir()) if skills_root.exists() else []
    if not skills:
        errors.append("no skills found")
    for skill in skills:
        try:
            metadata, body = frontmatter(skill / "SKILL.md")
            if metadata.get("name") != skill.name or not NAME.fullmatch(skill.name) or len(skill.name) > 64:
                errors.append(f"{skill.name}: invalid or mismatched skill name")
            description = metadata.get("description", "")
            if not description or len(description) > 1024:
                errors.append(f"{skill.name}: description must contain 1-1024 characters")
            if len(body.splitlines()) >= 500:
                errors.append(f"{skill.name}: move detail out of the entrypoint (500 lines)")
            version = re.search(r'^  version:\s*"([^"]+)"\s*$', (skill / "SKILL.md").read_text(), re.M)
            if not version or version[1] != manifest.get("version"):
                errors.append(f"{skill.name}: skill/package version mismatch")
            if (skill / "LICENSE.txt").read_bytes() != (root / "LICENSE").read_bytes():
                errors.append(f"{skill.name}: packaged license differs from repository license")
            ui = (skill / "agents/openai.yaml").read_text()
            short = re.search(r'^  short_description:\s*"([^"]+)"\s*$', ui, re.M)
            if not short or not 25 <= len(short[1]) <= 64:
                errors.append(f"{skill.name}: UI description must contain 25-64 characters")
            if not re.search(r'^  display_name:\s*"[^"]+"\s*$', ui, re.M):
                errors.append(f"{skill.name}: missing display name")
            for path in skill_files(skill):
                if path.suffix == ".md":
                    errors.extend(f"{path.relative_to(root)}: {message}" for message in check_links(path, skill))
        except (OSError, ValueError) as exc:
            errors.append(f"{skill.name}: {exc}")

    for path in visible_files(root):
        relative = path.relative_to(root)
        if path.is_symlink():
            errors.append(f"{relative}: repository source symlink")
            continue
        if not path.is_file():
            errors.append(f"{relative}: missing source file")
            continue
        if any(part in {".build", "__pycache__"} or part.startswith(".env") for part in relative.parts):
            errors.append(f"{relative}: private/generated source is tracked")
            continue
        if path.stat().st_size > 512_000:
            errors.append(f"{relative}: oversized source requires explicit review")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"{relative}: binary source requires explicit review")
            continue
        errors.extend(f"{relative}: possible {finding}" for finding in scan_text(text))
        if path.suffix == ".md" and relative.parts[0] != "skills":
            errors.extend(f"{relative}: {message}" for message in check_links(path, root))
    return errors
