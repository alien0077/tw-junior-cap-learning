#!/usr/bin/env python3
"""Validate an evidence result file without changing reviewStatus."""
import argparse, json, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("result", type=Path)
args = ap.parse_args()
d = json.loads(args.result.read_text())
errors = []
for i, item in enumerate(d.get("items", []), 1):
    for field in ("id", "sourceUrl", "sourceLocator", "comparisonSummary", "conclusion"):
        if not item.get(field): errors.append(f"items[{i}].{field} missing")
    if item.get("conclusion") not in {"pass", "fail", "needs-more-evidence"}:
        errors.append(f"items[{i}].conclusion invalid")
if not d.get("items"):
    errors.append("items must be non-empty")
if errors:
    print("INVALID")
    print("\n".join(errors))
    sys.exit(1)
print(f"VALID evidence results: {len(d['items'])} items; no reviewStatus changed")
