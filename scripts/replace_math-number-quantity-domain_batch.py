"""以公開數學試題的數與量能力方向，獨立替換 N 領域彙整題。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n"
KNOWLEDGE = "kg-math-content-n"

ITEMS = [
    ("(-3)^2+4 的值為何？", ["13", "1", "-5", "-13"], "A", "先算乘方，(-3)^2＝9，再加 4 得 13。"),
    ("0.75 化為最簡分數為何？", ["3/4", "1/3", "75/10", "4/3"], "A", "0.75＝75/100，約分得 3/4。"),
    ("若 a=2、b=-5，則 |a|+|b| 為何？", ["7", "-3", "3", "-7"], "A", "|2|＝2、|-5|＝5，所以和為 7。"),
    ("下列哪個數最接近 √50？", ["7", "5", "8", "10"], "A", "49＜50＜64，因此 √50 介於 7 與 8 之間且較接近 7。"),
    ("2^3×2^4 的結果可表示為何？", ["2^7", "2^12", "4^7", "2"], "A", "同底數相乘時指數相加，2^(3＋4)＝2^7。"),
    ("若 3x=18，則 x 為何？", ["6", "15", "21", "54"], "A", "等式兩邊同除以 3，得 x＝18÷3＝6。"),
    ("一件物品原價 800 元，打 75 折後售價為何？", ["600 元", "200 元", "725 元", "1,000 元"], "A", "75 折表示原價的 0.75 倍，800×0.75＝600 元。"),
    ("若 1 公里=1000 公尺，2.35 公里等於多少公尺？", ["2350 公尺", "235 公尺", "23.5 公尺", "23500 公尺"], "A", "2.35×1000＝2350，所以是 2350 公尺。"),
    ("科學記號 4.2×10^3 等於何者？", ["4200", "420", "42", "42000"], "A", "10^3＝1000，因此 4.2×1000＝4200。"),
    ("若 x 是整數且 -2＜x≤3，符合條件的 x 共有幾個？", ["5 個", "4 個", "6 個", "3 個"], "A", "整數為 -1、0、1、2、3，共 5 個。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究數與量的運算、數線、根號、指數、比例與單位轉換能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 number-and-quantity domain questions")


if __name__ == "__main__":
    main()
