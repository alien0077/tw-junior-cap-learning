"""以公開數學試題的數與量計算方向，獨立替換 N-7-3 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-7-3.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-7-3"
KNOWLEDGE = "kg-math-content-n-7-3"

ITEMS = [
    ("計算 (－8)＋13 的值為何？", ["5", "－5", "21", "－21"], "A", "負 8 加上 13，相當於 13－8，所以結果為 5。"),
    ("計算 (－6)－(－9) 的值為何？", ["3", "－3", "15", "－15"], "A", "減去負數等於加上其相反數：(－6)＋9＝3。"),
    ("計算 (－4)×7 的值為何？", ["－28", "28", "－11", "11"], "A", "負數乘正數結果為負，4×7＝28，因此結果為－28。"),
    ("計算 (－45)÷9 的值為何？", ["－5", "5", "－36", "36"], "A", "負數除以正數結果為負，45÷9＝5，因此結果為－5。"),
    ("計算 3－2×(－4) 的值為何？", ["11", "－5", "－11", "5"], "A", "先算乘法：2×(－4)＝－8，再算 3－(－8)＝11。"),
    ("計算 (－3/4)＋(1/2) 的值為何？", ["－1/4", "1/4", "－5/4", "5/4"], "A", "1/2＝2/4，所以 (－3/4)＋(2/4)＝－1/4。"),
    ("計算 1.2－3.5 的值為何？", ["－2.3", "2.3", "－4.7", "4.7"], "A", "將小數對齊後，1.2－3.5＝－2.3。"),
    ("計算 [ (－2)²－3 ]×(－5) 的值為何？", ["－5", "5", "－25", "25"], "A", "先算 (－2)²＝4，再得 (4－3)×(－5)＝－5。"),
    ("計算 (－18)÷3＋2×(－4) 的值為何？", ["－14", "－2", "14", "2"], "A", "先算除法與乘法：－18÷3＝－6、2×(－4)＝－8，合計為－14。"),
    ("清晨氣溫為－3.5℃，白天上升 6.2℃，白天氣溫為多少？", ["2.7℃", "－2.7℃", "9.7℃", "－9.7℃"], "A", "氣溫變化為 (－3.5)＋6.2＝2.7，所以白天為 2.7℃。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-7-3-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        rotated = options[shift:] + options[:shift]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + j), "text": value} for j, value in enumerate(rotated)]
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["knowledgeIds"] = [KNOWLEDGE]
        data["lessonId"] = LESSON
        data["difficulty"] = "medium"
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究負數、分數、小數、括號與四則混合運算能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 integer mixed-operation questions")


if __name__ == "__main__":
    main()
