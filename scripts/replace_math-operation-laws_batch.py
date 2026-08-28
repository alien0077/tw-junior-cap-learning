"""以公開數學試題的數與量運算方向，獨立替換 N-7-4 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-7-4.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-7-4"
KNOWLEDGE = "kg-math-content-n-7-4"

ITEMS = [
    ("下列哪個等式可由加法交換律得到？", ["8＋(－3)＝(－3)＋8", "8－3＝3－8", "8÷(－3)＝(－3)÷8", "8×(－3)＝8＋(－3)"], "A", "加法交換律是 a＋b＝b＋a，因此 8＋(－3)＝(－3)＋8。"),
    ("下列哪個等式正確呈現加法結合律？", ["(－2＋5)＋7＝－2＋(5＋7)", "(－2－5)－7＝－2－(5－7)", "(－2×5)×7＝－2×(5＋7)", "(－2÷5)÷7＝－2÷(5÷7)"], "A", "加法結合律允許改變括號位置而不改變順序：(a＋b)＋c＝a＋(b＋c)。"),
    ("計算 (4×(－3))×2 時，利用乘法結合律可改寫為何者？", ["4×((－3)×2)＝－24", "(4×(－3))＋2＝－10", "4×(－3＋2)＝－4", "4＋((－3)×2)＝－2"], "A", "乘法結合律可移動括號；4×((－3)×2)＝4×(－6)＝－24。"),
    ("利用分配律計算 6×(9＋4)，結果為何？", ["78", "54", "24", "58"], "A", "6×(9＋4)＝6×9＋6×4＝54＋24＝78。"),
    ("利用分配律，25×48＋25×52 的值為何？", ["2500", "2400", "2600", "1250"], "A", "提出共同因數 25：25×(48＋52)＝25×100＝2500。"),
    ("利用 17×(100－1) 計算 17×99，結果為何？", ["1683", "1700", "1717", "183"], "A", "17×99＝17×100－17×1＝1700－17＝1683。"),
    ("計算 (－6)×(8－3) 的值為何？", ["－30", "30", "－66", "66"], "A", "先算括號 8－3＝5，再算 (－6)×5＝－30；也可用分配律驗算。"),
    ("利用分配律計算 (3/4)×(8＋4)，結果為何？", ["9", "6", "12", "3"], "A", "(3/4)×12＝9；或分配為 (3/4)×8＋(3/4)×4＝6＋3。"),
    ("下列哪個等式使用了加法逆元素的性質？", ["(－15)＋15＝0", "(－15)＋15＝30", "(－15)×15＝0", "(－15)－15＝0"], "A", "任何數與其相反數相加等於 0，－15 與 15 互為相反數。"),
    ("利用分配律，49×101 可改寫為何者？", ["49×100＋49＝4949", "49×100－49＝4851", "50×100＋1＝5001", "49×(100＋1)＝4901"], "A", "101＝100＋1，所以 49×101＝49×100＋49＝4949。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-7-4-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究交換律、結合律、分配律與運算策略能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 operation-law questions")


if __name__ == "__main__":
    main()
