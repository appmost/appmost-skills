#!/usr/bin/env python3
"""Compare selected rendered text gaps with declared targets from a review_page report."""
import argparse
import json
import math
from pathlib import Path


def bounds(node, tolerance=0.5):
    frame = node["frame"]
    visible = node["visibleFrame"]
    top = frame["y"]
    bottom = top + frame["height"]
    if (frame["height"] <= 0 or visible["height"] <= 0
            or visible["y"] - top > tolerance
            or bottom - visible["y"] - visible["height"] > tolerance):
        raise ValueError(f"{node['id']} is not fully visible vertically")
    return top, bottom


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--surface", required=True, help="Exact row node ID of the painted surface")
    parser.add_argument("--surface-margins", type=float, nargs=2, default=(0, 0),
                        metavar=("TOP", "BOTTOM"),
                        help="Only supply margins verified to be included in the reported surface frame")
    parser.add_argument("--line", action="append", required=True,
                        help="One or more exact text node IDs, comma-separated; repeat in visible order")
    parser.add_argument("--expected", type=float, nargs="+", required=True,
                        help="Top inset, consecutive text gaps and bottom inset, in report units")
    parser.add_argument("--tolerance", type=float, default=2)
    args = parser.parse_args()
    if (len(args.expected) != len(args.line) + 1
            or not all(math.isfinite(v) and v >= 0
                       for v in [*args.expected, *args.surface_margins, args.tolerance])):
        parser.error("Supply one finite nonnegative target per gap, including both surface insets.")

    try:
        result = json.loads(args.report.read_text(encoding="utf-8"))
        layout = result["layout"]
        if not result["ok"] or not layout.get("coordinateUnit"):
            raise ValueError("Expected a successful review_page result with measured coordinates")
        nodes = layout["nodes"]

        def selected(node_id, role):
            matches = [node for node in nodes if node["id"] == node_id and node["role"] == role]
            if len(matches) != 1:
                raise ValueError(f"Expected one {role} node with ID {node_id}")
            return bounds(matches[0])

        top, bottom = selected(args.surface, "row")
        top += args.surface_margins[0]
        bottom -= args.surface_margins[1]
        lines = [[selected(node_id.strip(), "text") for node_id in line.split(",")]
                 for line in args.line]
        starts = [min(start for start, _ in line) for line in lines]
        ends = [max(end for _, end in line) for line in lines]
        measured = [start - end for start, end in zip([*starts, bottom], [top, *ends])]
        checks = [{"measured": round(actual, 2), "target": target,
                   "ok": actual >= 0 and abs(actual - target) <= args.tolerance}
                  for actual, target in zip(measured, args.expected)]
    except (KeyError, TypeError, ValueError, OSError) as error:
        parser.error(str(error))

    passed = all(check["ok"] for check in checks)
    print(json.dumps({"ok": passed, "unit": layout["coordinateUnit"],
                      "pageId": result["pageId"], "revision": result["revision"],
                      "gaps": checks}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
