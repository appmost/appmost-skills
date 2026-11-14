#!/usr/bin/env python3
"""Create deterministic standalone skill ZIPs from validated source directories."""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import zipfile
from repo_checks import CheckError, skill_files, validate_repository, within

def package(root: Path, output: Path) -> dict[str, str]:
    root = root.resolve()
    output = output.absolute()
    errors = validate_repository(root)
    if errors:
        raise CheckError("\n".join(errors))
    if output.exists() or output.is_symlink():
        raise CheckError("output must be a new directory; existing output is never overwritten")
    if within(output, root / "skills") or within(root, output):
        raise CheckError("output overlaps source or is an ancestor of the repository")
    inputs = [(skill, skill_files(skill)) for skill in sorted((root / "skills").iterdir()) if skill.is_dir()]
    output.mkdir(parents=True)
    hashes = {}
    for skill, paths in inputs:
        destination = output / f"{skill.name}.zip"
        with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in paths:
                info = zipfile.ZipInfo(f"{skill.name}/{path.relative_to(skill).as_posix()}", (1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes(), compresslevel=9)
        hashes[destination.name] = hashlib.sha256(destination.read_bytes()).hexdigest()
    (output / "SHA256SUMS").write_text(
        "".join(f"{digest}  {name}\n" for name, digest in sorted(hashes.items())), encoding="utf-8")
    return hashes

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output or args.root / ".build/packages"
    try:
        hashes = package(args.root, output)
    except (CheckError, OSError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    for name, digest in hashes.items():
        print(f"{digest}  {name}")
    print(f"Created standalone skill packages in {output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
