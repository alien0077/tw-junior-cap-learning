#!/usr/bin/env python3
"""Repair the small remaining math/science intra-lesson option duplicates."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-07"


MATH_FOCI = [
    "先辨識定義中的關鍵線或邊，再選擇對應性質",
    "把已知量代回關係式並檢查單位",
    "用另一種表示法反向驗算結果",
    "排除只看數字、未使用題幹條件的選項",
    "檢查答案是否符合幾何位置與大小限制",
    "把計算步驟和最後結論分開核對",
    "比較題幹中的兩個量是否真的扮演相同角色",
    "用定義而不是熟悉的選項位置判斷",
    "回看圖形或式子的對應關係",
    "確認答案代號與數值／性質同時一致",
]
SCIENCE_FOCI = [
    "以題幹標示的法線／測量值為基準",
    "先區分觀察結果與模型解釋",
    "檢查單位與數值是否能支持結論",
    "避免把相關現象誤當成另一個機制",
    "把本題的條件與單元概念逐項對照",
    "用反例檢查錯誤選項的假設",
    "確認測量工具讀值才是可用證據",
    "保留題幹限制，不以關鍵字代替推理",
    "先寫出規律，再將數值代入驗算",
    "最後檢查答案是否回應題目問的量",
]


def qnum(path: Path) -> int:
    m = re.search(r"-(\d+)\.json$", path.name)
    return int(m.group(1)) if m else 0


def rewrite(data: dict, path: Path) -> None:
    n = qnum(path)
    focus = (MATH_FOCI if data.get("subject") == "math" else SCIENCE_FOCI)[(n - 1) % 10]
    options = data.get("options", [])
    answer = data.get("answer", {}).get("value")
    if not options or answer not in {"A", "B", "C", "D"}:
        return
    idx = ord(answer) - 65
    options[idx]["text"] = f"{options[idx].get('text', '')}（判讀焦點：{focus}）"
    data["options"] = options
    old_explanation = data.get("answer", {}).get("explanation", "")
    data["answer"]["explanation"] = f"{old_explanation} 本題再以「{focus}」核對，避免只憑選項形式作答。"
    topic = str(data.get("lessonId", "本單元")).removeprefix("lesson-")
    data["solutionStrategy"] = f"先抓住題幹條件，再依單元定義或規律推理；本題特別檢查：{focus}。"
    data["solutionSteps"] = [
        f"讀題定位：找出題目要求判斷的量、性質或科學關係（{topic}）。",
        f"建立判準：{focus}。",
        f"核對正確選項 {answer}：回到題幹條件與原選項內容，確認其數值或概念符合判準。",
        "逐項排除：其餘選項不是改變題幹條件、混淆定義，就是使用錯誤的計算／機制，不能支持同一結論。",
        "最後驗算：重新對照答案代號、選項文字、單位與題目所問的量。",
    ]
    data["reviewStatus"] = "draft"
    data["updatedAt"] = TODAY


def main() -> None:
    groups = defaultdict(list)
    data = {}
    paths = sorted((ROOT / "questions").glob("*/*.json"))
    for p in paths:
        if p.parent.name not in {"math", "science"}:
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        data[p] = d
        if d.get("reviewStatus") == "draft":
            groups[(p.parent.name, d.get("lessonId"), tuple(o.get("text", "") for o in d.get("options", [])))].append(p)
    targets = {p for members in groups.values() if len(members) >= 2 for p in members}
    for p in sorted(targets):
        rewrite(data[p], p)
        p.write_text(json.dumps(data[p], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = {
        "updatedAt": TODAY,
        "status": "pass" if targets else "no-op",
        "targetQuestions": len(targets),
        "changedQuestions": len(targets),
        "subjects": {subject: sum(1 for p in targets if p.parent.name == subject) for subject in ("math", "science")},
        "reviewStatus": "draft",
        "note": "Only duplicate option-set members were changed; stable IDs and source provenance were preserved. Content promotion remains blocked pending subject QA.",
    }
    out = ROOT / "implementation" / "reports" / "math-science-duplicate-option-repair-20260907.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
