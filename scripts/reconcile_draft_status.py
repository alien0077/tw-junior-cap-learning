#!/usr/bin/env python3
"""Align lesson/coverage review status with explicit draft lesson titles."""
from __future__ import annotations

import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    draft_ids: set[str] = set()
    changed = 0
    for filename in glob.glob(str(ROOT / "lessons" / "**" / "*.json"), recursive=True):
        path = Path(filename)
        data = json.loads(path.read_text(encoding="utf-8"))
        if str(data.get("title", "")).startswith("草稿"):
            draft_ids.add(data["id"])
            if data.get("reviewStatus") != "draft":
                data["reviewStatus"] = "draft"
                path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                changed += 1

    matrix_path = ROOT / "data/m4-coverage-matrix.json"
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    matrix_changed = 0
    for row in matrix["rows"]:
        if row.get("lessonId") in draft_ids:
            if row.get("reviewStatus") != "draft" or row.get("contentStatus") != "draft":
                row["reviewStatus"] = "draft"
                row["contentStatus"] = "draft"
                matrix_changed += 1
    matrix_path.write_text(json.dumps(matrix, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"downgraded {changed} lessons and {matrix_changed} coverage rows to draft; explicit drafts={len(draft_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
