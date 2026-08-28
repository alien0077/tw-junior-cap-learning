"""以公開會考與公立國中段考的二次方程式能力方向，獨立替換 A-8-6 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-8-6.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-8-6"
KNOWLEDGE = "kg-math-content-a-8-6"

ITEMS = [
    ("方程式 x²－5x＋6＝0 的解為何？", ["x＝2 或 3", "x＝－2 或 －3", "x＝1 或 6", "x＝－1 或 －6"], "A", "將 x²－5x＋6 分解為 (x－2)(x－3)，所以 x＝2 或 3。"),
    ("方程式 2x²－8＝0 的所有實數解為何？", ["x＝2 或 －2", "x＝4 或 －4", "x＝2", "x＝－2"], "A", "2x²－8＝0 可整理為 x²＝4，因此 x＝2 或 －2。"),
    ("將 3x²－7x＋2＝0 與 ax²＋bx＋c＝0 比較，a、b、c 各為何？", ["a＝3、b＝－7、c＝2", "a＝－7、b＝3、c＝2", "a＝3、b＝7、c＝－2", "a＝2、b＝－7、c＝3"], "A", "依 x²、x、常數項的係數順序比較，可得 a＝3、b＝－7、c＝2。"),
    ("方程式 x²＋7x＋12＝0 的解為何？", ["x＝－3 或 －4", "x＝3 或 4", "x＝－2 或 －6", "x＝2 或 6"], "A", "x²＋7x＋12＝(x＋3)(x＋4)，所以 x＝－3 或 －4。"),
    ("使用公式法解 x²－4x－5＝0，所得兩根為何？", ["x＝5 或 －1", "x＝4 或 －5", "x＝－5 或 1", "x＝2 或 －3"], "A", "代入公式或分解為 (x－5)(x＋1)，可得 x＝5 或 －1。"),
    ("方程式 x²＋2x＋5＝0 的判別式 b²－4ac 為何？", ["－16", "16", "－6", "6"], "A", "a＝1、b＝2、c＝5，所以判別式為 2²－4×1×5＝－16。"),
    ("將 x²＋6x＋5＝0 配方後，哪一個等式正確？", ["(x＋3)²＝4", "(x＋6)²＝31", "(x＋3)²＝14", "(x－3)²＝4"], "A", "移項並加上 9：x²＋6x＋9＝4，因此 (x＋3)²＝4。"),
    ("下列哪一個數是方程式 2x²－3x－2＝0 的解？", ["2", "－2", "1", "1/2"], "A", "把 x＝2 代入得 2×2²－3×2－2＝8－6－2＝0，所以 2 是解。"),
    ("一個長方形寬為 x 公分、長為 x＋2 公分，面積為 15 平方公分。若 x 為正數，寬為多少公分？", ["3", "－3", "5", "15"], "A", "由 x(x＋2)＝15 得 x²＋2x－15＝0，即 (x＋5)(x－3)＝0；因寬為正，x＝3。"),
    ("若一元二次方程式的兩根為－2 與 5，且首項係數為 1，方程式可寫成下列何者？", ["x²－3x－10＝0", "x²＋3x－10＝0", "x²－7x＋10＝0", "x²＋7x＋10＝0"], "A", "由兩根可寫成 (x＋2)(x－5)＝0，展開得 x²－3x－10＝0。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-8-6-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究一元二次方程式的結構、解法、判別式、配方與情境建模能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 quadratic-meaning questions")


if __name__ == "__main__":
    main()
