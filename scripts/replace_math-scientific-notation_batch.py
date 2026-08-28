"""以公開數學試題的數與量表示方向，獨立替換 N-7-8 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-7-8.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-7-8"
KNOWLEDGE = "kg-math-content-n-7-8"

ITEMS = [
    ("0.00045 的科學記號表示法為何？", ["4.5×10⁻⁴", "45×10⁻⁵", "0.45×10⁻³", "4.5×10⁴"], "A", "小數點向右移 4 位得到 4.5，因此 0.00045＝4.5×10⁻⁴。"),
    ("7.2×10⁵ 的一般數字表示為何？", ["720000", "72000", "7200000", "0.00072"], "A", "10⁵ 表示小數點向右移 5 位，7.2×10⁵＝720000。"),
    ("3.08×10⁻³ 的一般數字表示為何？", ["0.00308", "0.0308", "0.000308", "3080"], "A", "10⁻³ 表示小數點向左移 3 位，所以結果為 0.00308。"),
    ("計算 (6.4×10⁴)×(2×10³)，並寫成科學記號，結果為何？", ["1.28×10⁸", "12.8×10⁷", "1.28×10⁷", "12.8×10⁸"], "A", "係數 6.4×2＝12.8，次方相加得 10⁷；再將 12.8×10⁷ 正規化為 1.28×10⁸。"),
    ("計算 (8.4×10⁷)÷(2×10³)，結果為何？", ["4.2×10⁴", "4.2×10¹⁰", "16.8×10⁴", "4.2×10⁻⁴"], "A", "係數 8.4÷2＝4.2，次方相減得 10^(7－3)，所以為 4.2×10⁴。"),
    ("下列哪一個是符合標準格式的科學記號？", ["9.3×10⁶", "93×10⁵", "0.93×10⁷", "930×10⁴"], "A", "標準格式要求係數大於等於 1 且小於 10，只有 9.3×10⁶ 符合。"),
    ("比較 5.1×10⁴ 與 4.9×10⁵，何者較大？", ["4.9×10⁵", "5.1×10⁴", "兩者相等", "無法比較"], "A", "先比較 10 的次方，10⁵ 大於 10⁴，因此 4.9×10⁵ 較大。"),
    ("2,500,000 的科學記號表示法為何？", ["2.5×10⁶", "25×10⁵", "0.25×10⁷", "2.5×10⁵"], "A", "小數點向左移 6 位成為 2.5，所以為 2.5×10⁶。"),
    ("0.00000072 的科學記號表示法為何？", ["7.2×10⁻⁷", "7.2×10⁻⁶", "0.72×10⁻⁷", "72×10⁻⁸"], "A", "小數點向右移 7 位得到 7.2，原數小於 1，指數為－7。"),
    ("計算 (2.4×10³)＋(3.1×10³)，結果為何？", ["5.5×10³", "5.5×10⁶", "0.55×10³", "5.5×10²"], "A", "同次方可先相加係數：(2.4＋3.1)×10³＝5.5×10³。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-7-8-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究科學記號轉換、位數、乘除、加法與量級判斷能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 scientific-notation questions")


if __name__ == "__main__":
    main()
