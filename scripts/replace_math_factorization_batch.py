"""以公開國中數學段考的因式分解能力方向，獨立替換 A-8-4 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-8-4.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-8-4"
KNOWLEDGE = "kg-math-content-a-8-4"
ITEMS = [
    ("多項式 6x＋18 的最大公因式為何？", ["6", "3x", "6x", "18"], "A", "6x 與 18 的最大公因數為 6，因此最大公因式為 6。"),
    ("將 8x＋12 提出最大公因式後，結果為何？", ["4(2x＋3)", "2(4x＋6)", "8(x＋12)", "4(2x＋12)"], "A", "8x 與 12 的最大公因式是 4，提出後為 4(2x＋3)。"),
    ("下列哪一項是 3a(2a＋5) 展開後的結果？", ["6a²＋15a", "6a²＋5a", "3a²＋15", "5a²＋6a"], "A", "分配律得 3a·2a＋3a·5＝6a²＋15a。"),
    ("10y²－15y 可提出哪一個最大公因式？", ["5y", "5", "10y", "15y²"], "A", "10y² 與 15y 的最大公因式是 5y。"),
    ("x²＋7x＋12 的因式分解為何？", ["(x＋3)(x＋4)", "(x＋2)(x＋6)", "(x－3)(x－4)", "(x＋1)(x＋12)"], "A", "兩數和為 7、積為 12 的整數是 3 與 4。"),
    ("x²－25 的因式分解為何？", ["(x－5)(x＋5)", "(x－25)(x＋1)", "(x－5)²", "(x＋25)(x－1)"], "A", "平方差公式 a²－b²＝(a－b)(a＋b)，所以為 (x－5)(x＋5)。"),
    ("4m²＋12m＋9 可表示為哪個完全平方？", ["(2m＋3)²", "(4m＋3)²", "(2m＋9)²", "(m＋3)²"], "A", "(2m＋3)²＝4m²＋12m＋9。"),
    ("若 2x²＋8x＝2x(x＋4)，這一步使用了哪種方法？", ["提出公因式", "平方差公式", "完全平方公式", "分組分解"], "A", "兩項共同含有 2x，提出後得到 2x(x＋4)。"),
    ("將 (p＋2)(p－6) 展開，常數項為何？", ["－12", "－8", "12", "8"], "A", "常數項由 2×(－6) 得到 －12。"),
    ("完成等式 9t²－16＝(3t－4)(＿＿) 的空格，應填入什麼？", ["3t＋4", "3t－4", "9t＋4", "t＋4"], "A", "9t²－16 是 (3t)²－4²，依平方差公式為 (3t－4)(3t＋4)。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-8-4-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究因式分解、公式與驗算能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 factorization questions")

if __name__ == "__main__":
    main()
