"""以公開數學試題的數與量表示方向，獨立替換 N-7-6 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-7-6.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-7-6"
KNOWLEDGE = "kg-math-content-n-7-6"

ITEMS = [
    ("2⁴ 的值為何？", ["16", "8", "12", "24"], "A", "2⁴ 表示 2 連乘 4 次：2×2×2×2＝16。"),
    ("(－3)³ 的值為何？", ["－27", "27", "－9", "9"], "A", "(－3)³＝(－3)×(－3)×(－3)＝－27。"),
    ("不加括號的 －3²，其值為何？", ["－9", "9", "－6", "6"], "A", "指數先於前面的負號運算，－3² 是 －(3²)＝－9。"),
    ("5⁰ 的值為何？", ["1", "0", "5", "沒有意義"], "A", "任何非 0 數的 0 次方等於 1，因此 5⁰＝1。"),
    ("10³ 表示多少？", ["1000", "100", "30", "300"], "A", "10³＝10×10×10＝1000。"),
    ("下列哪個乘積可寫成 7⁴？", ["7×7×7×7", "7＋7＋7＋7", "4×4×4×4×4×4×4", "7×4"], "A", "指數 4 表示底數 7 連乘四次，即 7×7×7×7。"),
    ("(－2)⁴ 的值為何？", ["16", "－16", "8", "－8"], "A", "偶次方的負底數結果為正：(－2)⁴＝2⁴＝16。"),
    ("(1/2)³ 的值為何？", ["1/8", "1/6", "3/2", "1/4"], "A", "(1/2)³＝(1/2)×(1/2)×(1/2)＝1/8。"),
    ("比較 2³ 與 3²，何者較大？", ["3² 較大", "2³ 較大", "兩者相等", "無法比較"], "A", "2³＝8、3²＝9，所以 3² 較大。"),
    ("若 a＝－4，則 a² 的值為何？", ["16", "－16", "8", "－8"], "A", "a²＝(－4)²＝(－4)×(－4)＝16。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-7-6-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究指數表示、底數正負、次方意義與數值比較能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 exponent-meaning questions")


if __name__ == "__main__":
    main()
