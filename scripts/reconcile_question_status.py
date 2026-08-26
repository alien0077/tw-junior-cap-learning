#!/usr/bin/env python3
"""Keep questions under draft lessons in draft status."""
from __future__ import annotations

import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    lesson_status = {}
    for filename in glob.glob(str(ROOT / "lessons" / "**" / "*.json"), recursive=True):
        data = json.loads(Path(filename).read_text(encoding="utf-8"))
        lesson_status[data["id"]] = data.get("reviewStatus")
    changed = 0
    for filename in glob.glob(str(ROOT / "questions" / "**" / "*.json"), recursive=True):
        path = Path(filename)
        data = json.loads(path.read_text(encoding="utf-8"))
        if lesson_status.get(data.get("lessonId")) == "draft" and data.get("reviewStatus") != "draft":
            data["reviewStatus"] = "draft"
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    print(f"downgraded {changed} questions attached to draft lessons")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
