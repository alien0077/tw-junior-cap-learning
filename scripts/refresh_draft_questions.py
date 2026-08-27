#!/usr/bin/env python3
"""Replace identical batch-draft prompts with concept-specific draft variants.

This deliberately keeps every item in ``draft`` status.  It improves coverage
of cognitive task types but is not a substitute for subject-matter review.
"""
from __future__ import annotations

import glob
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TASKS = [
    ("概念辨識", "下列哪一項最直接表達「{concept}」的學習重點？", "能用自己的話說明並辨認「{concept}」"),
    ("關鍵證據", "要判斷是否掌握「{concept}」，最適合先檢查哪一項證據？", "能以「{concept}」相關證據支持判斷"),
    ("步驟安排", "學習「{concept}」時，哪個順序最有助於形成可檢查的理解？", "先界定概念，再整理證據，最後檢查結論"),
    ("情境應用", "遇到新的生活或學習情境時，如何運用「{concept}」？", "把「{concept}」的原理套用到新情境並說明理由"),
    ("比較辨析", "若要區分「{concept}」與相近概念，最需要注意什麼？", "指出兩者的判準與適用條件"),
    ("資料表徵", "整理「{concept}」的資料時，哪種做法能讓推論更容易被核對？", "選擇合適的表格、圖示或文字並標明資料依據"),
    ("錯誤診斷", "同學解釋「{concept}」時出現錯誤，最先應檢查哪個環節？", "回到定義與證據，找出推論跳躍的位置"),
    ("理由說明", "完整回答「{concept}」的問題時，除了結論還應補上什麼？", "補充與概念相符的理由或可查核依據"),
    ("遷移練習", "哪一種練習最能確認「{concept}」不是只靠記憶？", "在變化情境中重新解釋、計算或提出證據"),
    ("自我檢核", "完成「{concept}」學習後，哪一項自我檢核最有價值？", "說明概念、展示依據，並檢查答案是否符合條件"),
]

DISTRACTORS = [
    "只背頁碼，不說明概念或依據",
    "只挑看起來熟悉的選項，不檢查條件",
    "把不同概念混在一起而不提出判準",
]


def concept_for(data: dict) -> str:
    prompt = str(data.get("prompt", ""))
    match = re.search(r"「(.*?)」", prompt)
    if match:
        return match.group(1)
    return data.get("lessonId", "本單元").removeprefix("lesson-")


def main() -> int:
    changed = 0
    for filename in sorted(glob.glob(str(ROOT / "questions" / "**" / "*.json"), recursive=True)):
        path = Path(filename)
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("reviewStatus") != "draft":
            continue
        try:
            index = int(path.stem.rsplit("-", 1)[1]) - 1
        except (ValueError, IndexError):
            continue
        if not 0 <= index < len(TASKS):
            continue
        task, prompt_template, answer_text = TASKS[index]
        concept = concept_for(data)
        data["prompt"] = prompt_template.format(concept=concept)
        options = [{"id": "A", "text": answer_text.format(concept=concept)}]
        for option_id, distractor in zip(("B", "C", "D"), DISTRACTORS):
            options.append({"id": option_id, "text": distractor})
        data["options"] = options
        data["answer"] = {
            "value": "A",
            "explanation": f"本題以「{concept}」檢查{task}；正式發布前仍需學科審閱。",
        }
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    print(f"refreshed {changed} draft questions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
