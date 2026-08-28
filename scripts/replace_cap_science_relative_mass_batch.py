#!/usr/bin/env python3
"""Replace the relative atomic/molecular mass template set with authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-aa-iv-2"
KID = "kg-science-content-aa-iv-2"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("已知氧的相對原子質量為 16，氧氣 O₂ 的相對分子質量為何？", ["32", "16", "8", "2"], "A", "O₂ 由 2 個氧原子組成，因此相對分子質量為 2 × 16 = 32。"),
    ("已知氫的相對原子質量為 1、氧為 16，水 H₂O 的相對分子質量為何？", ["18", "17", "16", "19"], "A", "H₂O 含 2 個氫原子與 1 個氧原子，計算為 2 × 1 + 16 = 18。"),
    ("已知碳的相對原子質量為 12、氧為 16，二氧化碳 CO₂ 的相對分子質量為何？", ["44", "28", "40", "48"], "A", "CO₂ 含 1 個碳原子與 2 個氧原子，計算為 12 + 2 × 16 = 44。"),
    ("若氮的相對原子質量為 14、氫為 1，氨 NH₃ 的相對分子質量為何？", ["17", "15", "16", "18"], "A", "NH₃ 含 1 個氮原子與 3 個氫原子，計算為 14 + 3 × 1 = 17。"),
    ("已知鈉的相對原子質量為 23、氯為 35.5，氯化鈉 NaCl 的相對式量為何？", ["58.5", "46", "35.5", "81.5"], "A", "NaCl 含 1 個鈉與 1 個氯，計算為 23 + 35.5 = 58.5。"),
    ("化學式 H₂SO₄ 中的下標 ₂ 主要表示什麼？", ["每個硫酸分子含有 2 個氫原子", "硫酸分子有 2 個硫原子", "硫酸的相對分子質量是 2", "有 2 種不同的元素"], "A", "元素符號右下角的下標表示該分子中該元素原子的個數；H₂ 表示 2 個氫原子。"),
    ("若某化合物的化學式為 X₂Y₃，X 的相對原子質量為 10、Y 為 16，則其相對分子質量為何？", ["68", "26", "48", "96"], "A", "依化學式計算：2 × 10 + 3 × 16 = 20 + 48 = 68。"),
    ("同溫度、同壓力下，比較一個 CO₂ 分子與一個 O₂ 分子的相對質量，何者正確？（C＝12、O＝16）", ["CO₂ 分子較重，因為 44 大於 32", "O₂ 分子較重，因為氧原子數較多", "兩者相對質量一定相同", "無法依化學式計算"], "A", "CO₂ 的相對分子質量為 44，O₂ 為 32，因此一個 CO₂ 分子的相對質量較大。"),
    ("關於相對原子質量與相對分子質量，下列何者正確？", ["相對分子質量可由化學式中各原子的相對原子質量相加求得", "相對分子質量只由分子體積決定", "相對原子質量一定要用克表示", "只要分子中原子數相同，分子質量就一定相同"], "A", "相對分子質量依化學式把組成原子的相對原子質量加總；它是相對值，不是直接以克表示的單一分子質量。"),
    ("某物質由 1 個碳原子、4 個氫原子組成，若 C＝12、H＝1，下列哪個化學式與相對分子質量配對正確？", ["CH₄，16", "C₄H，13", "CH₄，13", "C₄H，16"], "A", "1 個碳與 4 個氫的化學式為 CH₄，相對分子質量為 12 + 4 × 1 = 16。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-aa-iv-2-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    target = ord(answer_positions[index - 1]) - ord("A")
    rotated = options[1:target + 1] + options[:1] + options[target + 1:]
    answer = answer_positions[index - 1]
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(rotated)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考自然科；相對原子與分子質量計算及化學式判讀能力方向之獨立改編；官方答案表：{ANSWER}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style science relative-mass questions")
