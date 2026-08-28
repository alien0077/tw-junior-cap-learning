"""以公開國中數學段考的因式分解方法方向，獨立替換 A-8-5 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-8-5.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-8-5"
KNOWLEDGE = "kg-math-content-a-8-5"
ITEMS = [
    ("將 12x＋18 提出最大公因式，結果為何？", ["6(2x＋3)", "3(4x＋6)", "12(x＋18)", "6(2x＋18)"], "A", "12x 與 18 的最大公因式為 6，提出後得 6(2x＋3)。"),
    ("因式分解 x²＋9x＋20，結果為何？", ["(x＋4)(x＋5)", "(x＋2)(x＋10)", "(x－4)(x－5)", "(x＋1)(x＋20)"], "A", "兩數和為 9、積為 20 的數是 4 與 5。"),
    ("因式分解 2x²＋7x＋3，結果為何？", ["(2x＋1)(x＋3)", "(2x＋3)(x＋1)", "(x＋1)(x＋3)", "(2x－1)(x－3)"], "A", "交叉相乘得 2x²＋6x＋x＋3＝2x²＋7x＋3。"),
    ("將 6a²－15a 完全分解，結果為何？", ["3a(2a－5)", "3(2a²－5)", "a(6a－15a)", "6a(a－15)"], "A", "兩項共同含有 3a，提出後為 3a(2a－5)。"),
    ("利用分組分解，x²＋3x＋2x＋6 可化為何？", ["(x＋2)(x＋3)", "(x＋1)(x＋6)", "(x＋3)(x＋6)", "(x－2)(x－3)"], "A", "分組為 x(x＋3)＋2(x＋3)，再提出 (x＋3)，得 (x＋2)(x＋3)。"),
    ("因式分解 4y²－25，結果為何？", ["(2y－5)(2y＋5)", "(4y－5)(y＋5)", "(2y－5)²", "(4y－25)(y＋1)"], "A", "這是平方差 (2y)²－5²，結果為 (2y－5)(2y＋5)。"),
    ("將 9m²＋12m＋4 因式分解，結果為何？", ["(3m＋2)²", "(9m＋2)²", "(3m＋4)²", "(m＋2)²"], "A", "符合 (3m)²＋2(3m)(2)＋2²，因此為 (3m＋2)²。"),
    ("將 3p²－12 完全分解，結果為何？", ["3(p－2)(p＋2)", "3(p－4)(p＋4)", "(3p－2)(p＋2)", "3(p－2)²"], "A", "先提出 3 得 3(p²－4)，再用平方差得 3(p－2)(p＋2)。"),
    ("下列哪個乘積展開後等於 z²＋3z－4？", ["(z＋4)(z－1)", "(z＋3)(z－4)", "(z＋1)(z－4)", "(z－4)²"], "A", "(z＋4)(z－1)＝z²＋3z－4。"),
    ("因式分解 5t²＋15t＋10，結果為何？", ["5(t＋1)(t＋2)", "5(t＋3)(t＋2)", "(5t＋1)(t＋10)", "5(t－1)(t－2)"], "A", "先提出 5 得 5(t²＋3t＋2)，再分解為 5(t＋1)(t＋2)。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-8-5-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        rotated = options[shift:] + options[:shift]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + j), "text": value} for j, value in enumerate(rotated)]
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["knowledgeIds"] = [KNOWLEDGE]
        data["lessonId"] = LESSON
        data["difficulty"] = "medium"
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中公開數學段考；研究因式分解方法、公因式、分組、乘法公式與驗算能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 factorization-method questions")

if __name__ == "__main__":
    main()
