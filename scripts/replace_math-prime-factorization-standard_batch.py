"""以公開數學試題的數與量計算方向，獨立替換 N-7-2 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-7-2.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-7-2"
KNOWLEDGE = "kg-math-content-n-7-2"

ITEMS = [
    ("72 的標準質因數分解式為何？", ["2³×3²", "2²×3³", "2×36", "8×9"], "A", "72＝8×9＝2³×3²，且質數底數依大小排列。"),
    ("180 的標準質因數分解式為何？", ["2²×3²×5", "2×3×30", "2³×3×5", "2²×3×15"], "A", "180＝4×45＝2²×3²×5。"),
    ("90 的標準質因數分解式為何？", ["2×3²×5", "2²×3×5", "2×3×15", "9×10"], "A", "90＝2×45＝2×3²×5。"),
    ("2³×3×5 的值是多少？", ["120", "60", "90", "150"], "A", "2³×3×5＝8×3×5＝120。"),
    ("48 的標準質因數分解式為何？", ["2⁴×3", "2³×3²", "2×24", "4×12"], "A", "48＝16×3＝2⁴×3。"),
    ("若 2ᵃ×3²＝72，則 a 為何？", ["3", "2", "4", "5"], "A", "72＝2³×3²，因此比較 2 的次方可得 a＝3。"),
    ("84 的標準質因數分解式為下列何者？", ["2²×3×7", "2×3×14", "4×21", "2³×3×7"], "A", "84＝4×21＝2²×3×7，三個底數都是質數。"),
    ("200 的標準質因數分解式為 2³×5²，其中質因數 2 的指數是多少？", ["3", "2", "5", "8"], "A", "200＝8×25＝2³×5²，所以質因數 2 的指數為 3。"),
    ("105 的標準質因數分解式為何？", ["3×5×7", "3×5²×7", "3×35", "5×21"], "A", "105＝3×35＝3×5×7，且 3、5、7 均為質數。"),
    ("下列哪一項符合標準質因數分解式的寫法？", ["質數底數由小到大排列，重複因數合併為冪次", "可以把合數當作底數", "只要乘積正確就不必使用質數", "底數必須全部相同"], "A", "標準質因數分解要求所有底數為質數，並通常由小到大排列、合併重複因數。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-7-2-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究因數分解、次方表示與數量計算能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 standard prime-factorization questions")


if __name__ == "__main__":
    main()
