"""以公開數學試題的指數運算方向，獨立替換 N-7-7 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-7-7.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-7-7"
KNOWLEDGE = "kg-math-content-n-7-7"

ITEMS = [
    ("2³×2⁴ 可化簡為何者？", ["2⁷", "2¹²", "4⁷", "4¹²"], "A", "同底數相乘時指數相加：2³×2⁴＝2^(3＋4)＝2⁷。"),
    ("5⁸÷5³ 可化簡為何者？", ["5⁵", "5¹¹", "1⁵", "5³"], "A", "同底數相除時指數相減：5⁸÷5³＝5^(8－3)＝5⁵。"),
    ("(3²)⁴ 可化簡為何者？", ["3⁸", "3⁶", "3²", "12⁴"], "A", "冪的冪指數相乘：(3²)⁴＝3^(2×4)＝3⁸。"),
    ("a³×a²÷a⁴（a≠0）可化簡為何者？", ["a", "a⁹", "a⁵", "1/a"], "A", "先相乘再相除，指數為 3＋2－4＝1，因此結果為 a。"),
    ("2⁵×4² 的值為何？", ["512", "128", "256", "1024"], "A", "4²＝(2²)²＝2⁴，所以 2⁵×4²＝2⁹＝512。"),
    ("(x⁴)² 可化簡為何者？", ["x⁸", "x⁶", "x⁴", "2x⁴"], "A", "冪的冪指數相乘，(x⁴)²＝x^(4×2)＝x⁸。"),
    ("7⁰×7³ 的值為何？", ["343", "49", "7", "1"], "A", "7⁰＝1，故 7⁰×7³＝1×343＝343。"),
    ("比較 2⁶ 與 4³，下列敘述何者正確？", ["兩者相等", "2⁶ 比 4³ 大", "4³ 比 2⁶ 大", "無法比較"], "A", "4³＝(2²)³＝2⁶，所以兩者都等於 64。"),
    ("若 3²×3ᵃ＝3⁷，則 a 為何？", ["5", "9", "14", "3"], "A", "同底數相乘指數相加，2＋a＝7，因此 a＝5。"),
    ("下列哪個等式正確？", ["6⁵÷6²＝6³", "6⁵÷6²＝6⁷", "6⁵×6²＝6³", "(6⁵)²＝6⁷"], "A", "同底數相除指數相減，6⁵÷6²＝6^(5－2)＝6³。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-7-7-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究同底數運算、冪的冪、零次方與指數比較能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 exponent-law questions")


if __name__ == "__main__":
    main()
