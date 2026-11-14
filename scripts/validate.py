#!/usr/bin/env python3
"""Validate the skill package without network, Appmost or account access."""
import argparse
from pathlib import Path
from repo_checks import validate_repository

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_repository(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: structure, install boundaries, links, metadata and limited public-content checks")
    print("Behavioral, visual and confidentiality review require the documented evaluation.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
