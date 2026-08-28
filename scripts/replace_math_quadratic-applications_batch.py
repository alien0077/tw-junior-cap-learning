"""以公開會考與公立國中段考的二次方程式應用能力方向，獨立替換 A-8-7 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-8-7.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-8-7"
KNOWLEDGE = "kg-math-content-a-8-7"

ITEMS = [
    ("方程式 x²－9x＋20＝0 的兩根為何？", ["x＝4 或 5", "x＝－4 或 －5", "x＝2 或 10", "x＝－2 或 －10"], "A", "x²－9x＋20＝(x－4)(x－5)，所以兩根為 4 與 5。"),
    ("方程式 2x²＋x－6＝0 的解為何？", ["x＝3/2 或 －2", "x＝2 或 －3/2", "x＝3 或 －2", "x＝－3/2 或 2"], "A", "2x²＋x－6＝(2x－3)(x＋2)，所以 x＝3/2 或 －2。"),
    ("使用公式法解 x²＋4x－1＝0，所得兩根為何？", ["x＝－2＋√5 或 －2－√5", "x＝2＋√5 或 2－√5", "x＝－4＋√5 或 －4－√5", "x＝2＋√3 或 2－√3"], "A", "代入 a＝1、b＝4、c＝－1，得 x＝(－4±√20)/2＝－2±√5。"),
    ("方程式 3x²－12x＋9＝0 經約分並因式分解後，解為何？", ["x＝1 或 3", "x＝－1 或 －3", "x＝2 或 6", "x＝－2 或 －6"], "A", "三項同除以 3 得 x²－4x＋3＝0，即 (x－1)(x－3)＝0。"),
    ("兩個連續正整數的乘積為 56，較大的整數是多少？", ["8", "7", "9", "56"], "A", "設較小整數為 x，則 x(x＋1)＝56，得 x＝7 或 －8；取正整數後，較大者為 8。"),
    ("一個長方形的寬為 x 公分、長為 x＋5 公分，面積為 84 平方公分。若 x 為正數，寬是多少公分？", ["7", "12", "－12", "84"], "A", "由 x(x＋5)＝84 得 (x＋12)(x－7)＝0；因寬為正，x＝7。"),
    ("某物體離地 t 秒的高度為 h＝－t²＋6t＋7 公尺。除 t＝－1 外，物體何時落地？", ["7 秒", "1 秒", "6 秒", "8 秒"], "A", "令 h＝0，得 t²－6t－7＝(t－7)(t＋1)＝0；時間不能為負，因此 t＝7。"),
    ("一個正數 x 滿足 x²＝5x＋14，則 x 為何？", ["7", "－2", "2", "14"], "A", "整理為 x²－5x－14＝0，即 (x－7)(x＋2)＝0；因 x 為正，x＝7。"),
    ("方程式 2x²＋4x＋5＝0 有幾個實數解？", ["沒有實數解", "有一個實數解", "有兩個相異實數解", "有三個實數解"], "A", "判別式為 4²－4×2×5＝－24＜0，所以沒有實數解。"),
    ("方程式 x²－2x＝15 的所有解為何？", ["x＝5 或 －3", "x＝3 或 －5", "x＝15 或 －2", "x＝－15 或 2"], "A", "整理為 x²－2x－15＝0，即 (x－5)(x＋3)＝0，所以 x＝5 或 －3。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-8-7-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究一元二次方程式的因式分解、公式法、整數根與情境應用能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 quadratic-application questions")


if __name__ == "__main__":
    main()
