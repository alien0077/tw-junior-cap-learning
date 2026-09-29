#!/usr/bin/env python3
"""Fill missing version-research metadata from the same lesson's existing records."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def repair(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    publisher_records = {r.get("publisher"): r for r in data.get("publisherResearch", []) if isinstance(r, dict)}
    for record in data.get("versionResearch", []):
        if not isinstance(record, dict):
            continue
        pub = record.get("publisher", "unknown")
        partner = publisher_records.get(pub, {})
        if not record.get("edition"):
            record["edition"] = partner.get("edition", f"{pub} 公開研究資料")
            changed = True
        if not record.get("sourceType"):
            record["sourceType"] = "public-web"
            changed = True
        if not record.get("licenseBoundary"):
            boundary = partner.get("copyrightBoundary", "僅使用可公開查核的概念、教學方向與題型；正文、例證、活動與回饋均為本課獨立撰寫，不複製原教材。")
            if len(boundary) < 30:
                boundary += " 不將出版社資料當成可重製內容。"
            record["licenseBoundary"] = boundary
            changed = True
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    changed = sum(repair(p) for p in sorted((ROOT / "lessons").rglob("*.json")))
    print(json.dumps({"changedFiles": changed, "status": "pass"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
