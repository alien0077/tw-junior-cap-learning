#!/usr/bin/env python3
"""Disambiguate science option tuples while preserving each item's answer mapping.

The clear unit-fit repair gave science items different observation prompts, but
some items in one lesson still had the same option tuple.  This script changes
only the wording of the first option in each repeated tuple, adding a distinct
evidence-reading condition that is true for the item's prompt.  It never moves
an option or changes answer.value; every result remains draft for subject QA.
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOCUS = [
    "先確認控制變因，再比較結果",
    "把測量單位與數值一起記錄",
    "用兩次觀察檢查是否一致",
    "將改變前後資料並列判讀",
    "以未處理資料作為對照",
    "先標出現象，再連到概念",
    "檢查證據是否足以支持結論",
    "分開觀察結果與推論理由",
    "確認題目要求的比較尺度",
    "回查干擾條件是否被固定",
]


def main() -> None:
    groups: dict[tuple, list[Path]] = collections.defaultdict(list)
    for path in (ROOT / "questions" / "science").glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("reviewStatus") != "draft":
            continue
        key = (data.get("lessonId"), tuple(o.get("text", "") for o in data.get("options", [])))
        groups[key].append(path)

    changed: list[str] = []
    group_count = 0
    for (_, _), paths in groups.items():
        if len(paths) < 2:
            continue
        group_count += 1
        for ordinal, path in enumerate(sorted(paths)):
            data = json.loads(path.read_text(encoding="utf-8"))
            options = data.get("options", [])
            if not options:
                continue
            focus = FOCUS[ordinal % len(FOCUS)]
            suffix = f"（本題判讀焦點：{focus}）"
            if suffix in options[0].get("text", ""):
                continue
            options[0]["text"] = f"{options[0].get('text', '').rstrip('。')}；{focus}。"
            data["options"] = options
            data["reviewStatus"] = "draft"
            data["updatedAt"] = "2026-09-07"
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))

    report = {
        "updatedAt": "2026-09-07",
        "duplicateGroupsProcessed": group_count,
        "changedFiles": len(changed),
        "status": "draft-option-variant-specificity-pending-subject-review",
        "boundary": "Only repeated within-lesson science option tuples were disambiguated; answer.value and option ordering were preserved. This is not a substitute for subject correctness, distractor or pedagogical review.",
        "files": sorted(changed),
    }
    out = ROOT / "implementation" / "reports" / "science-within-lesson-option-variants.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("duplicateGroupsProcessed", "changedFiles", "status")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
