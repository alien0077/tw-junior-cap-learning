"""以公開數學試題的數與量根式計算方向，獨立替換 N-8-1 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-8-1.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-8-1"
KNOWLEDGE = "kg-math-content-n-8-1"

ITEMS = [
    ("√49 的值為何？", ["7", "－7", "49", "14"], "A", "√49 表示 49 的算術平方根，取非負值，所以 √49＝7。"),
    ("√(25/36) 的值為何？", ["5/6", "－5/6", "25/6", "5/36"], "A", "√(25/36)＝√25/√36＝5/6，算術平方根取正值。"),
    ("√72 化簡後為何？", ["6√2", "2√18", "8√9", "36√2"], "A", "72＝36×2，因此 √72＝√36×√2＝6√2。"),
    ("√12＋√27 化簡後為何？", ["5√3", "7√3", "√39", "5√9"], "A", "√12＝2√3、√27＝3√3，合併同類根式得 5√3。"),
    ("比較 √50 與 7，下列何者正確？", ["√50＞7", "√50＜7", "√50＝7", "無法比較"], "A", "因 7²＝49＜50，所以 √50＞√49＝7。"),
    ("(√3)² 的值為何？", ["3", "√6", "9", "－3"], "A", "平方根與平方互相抵消，(√3)²＝3。"),
    ("√8×√2 的值為何？", ["4", "2√2", "√10", "16"], "A", "√8×√2＝√16＝4。"),
    ("√18÷√2 的值為何？", ["3", "9", "√16", "√20"], "A", "√18÷√2＝√(18÷2)＝√9＝3。"),
    ("√81 的值為何？", ["9", "－9", "81", "18"], "A", "√81 是 81 的算術平方根，因 9²＝81，所以值為 9。"),
    ("直角三角形兩股長分別為 6 與 8，斜邊長為何？", ["10", "14", "√14", "48"], "A", "由畢氏定理，斜邊為 √(6²＋8²)＝√100＝10。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-8-1-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究平方根定義、根式化簡、四則運算與幾何應用能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 square-root questions")


if __name__ == "__main__":
    main()
