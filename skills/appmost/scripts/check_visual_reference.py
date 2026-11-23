"""Record and check the ImageGen file selected for a visual change."""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path


def nonempty(value):
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("Expected a nonempty value.")
    return value


def image_digest(path):
    data = path.read_bytes()
    png = data.startswith(b"\x89PNG\r\n\x1a\n") and data[12:16] == b"IHDR"
    jpeg = data.startswith(b"\xff\xd8\xff") and data.endswith(b"\xff\xd9")
    webp = data.startswith(b"RIFF") and data[8:12] == b"WEBP" and len(data) > 20
    if not (png or jpeg or webp):
        raise ValueError("The reference must be a PNG, JPEG or WebP image.")
    return sha256(data).hexdigest()


def record_reference(args):
    image = args.image.resolve(strict=True)
    record = {
        "page": args.page,
        "state": args.state,
        "sourceRevision": args.revision,
        "image": str(image),
        "imageSha256": image_digest(image),
        "provenance": args.provenance,
        "targets": args.target,
        "recordedAt": datetime.now(timezone.utc).isoformat(),
    }
    with args.record.open("x", encoding="utf-8") as file:
        json.dump(record, file, indent=2, ensure_ascii=False)
        file.write("\n")


def check_reference(args):
    record = json.loads(args.record.read_text(encoding="utf-8"))
    if (record["page"], record["state"]) != (args.page, args.state):
        raise ValueError("The recorded page or state differs from the requested presentation.")
    if args.revision is not None and record["sourceRevision"] != args.revision:
        raise ValueError("The source differs from the recorded starting revision.")
    if image_digest(Path(record["image"])) != record["imageSha256"]:
        raise ValueError("The recorded reference image bytes changed.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    record = commands.add_parser("record", help="Save the reference before the first visual edit.")
    check = commands.add_parser("check", help="Verify the same presentation and image.")
    for command in (record, check):
        command.add_argument("record", type=Path)
        command.add_argument("--page", type=nonempty, required=True)
        command.add_argument("--state", type=nonempty, required=True)
        command.add_argument("--revision", type=nonempty, required=command is record)
    record.add_argument("--image", type=Path, required=True)
    record.add_argument("--provenance", type=nonempty, required=True)
    record.add_argument("--target", type=nonempty, action="append", required=True)
    args = parser.parse_args()
    try:
        action = record_reference if args.command == "record" else check_reference
        action(args)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Visual reference check failed. {error}\n")
    print("Visual reference file and record verified.")


if __name__ == "__main__":
    main()
