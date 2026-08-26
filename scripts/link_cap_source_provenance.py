#!/usr/bin/env python3
"""Attach the official CAP index as a scope/type reference to draft questions."""
from __future__ import annotations

import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAP_URL = "https://cap.rcpet.edu.tw/examination.html"


def main() -> int:
    changed = 0
    for filename in glob.glob(str(ROOT / "questions" / "**" / "*.json"), recursive=True):
        path = Path(filename)
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("reviewStatus") != "draft":
            continue
        provenance = data.setdefault("provenance", {})
        provenance["sourceUrl"] = CAP_URL
        provenance["sourceLocator"] = "官方歷屆試題入口：僅作命題範圍與題型查核，非本題題文來源"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    print(f"linked CAP scope provenance on {changed} draft questions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
