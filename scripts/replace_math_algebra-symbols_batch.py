"""以公開國中數學段考的代數符號能力方向，獨立替換 A-7-1 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-7-1.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-7-1"
KNOWLEDGE = "kg-math-content-a-7-1"
ITEMS = [
    ("在式子 3x＋2 中，代表可變數值的符號是哪一個？", ["x", "3", "2", "＋"], "A", "x 可以代表不同數值，是此式的變數。"),
    ("在單項式－5a 中，a 的係數為何？", ["－5", "5", "－a", "a"], "A", "係數是乘在變數前的數字，因此 a 的係數為－5。"),
    ("在式子 7y－4 中，常數項為何？", ["－4", "7", "y", "4y"], "A", "不含變數的項是常數項，所以為－4。"),
    ("每盒彩筆有 x 枝，買 4 盒共有幾枝？", ["4x", "x＋4", "x⁴", "4＋x"], "A", "每盒 x 枝買 4 盒，使用乘法得到 4x 枝。"),
    ("當 x＝3 時，2x＋5 的值為何？", ["11", "10", "8", "6"], "A", "代入 x＝3：2×3＋5＝11。"),
    ("當 a＝－2 時，a² 的值為何？", ["4", "－4", "2", "－2"], "A", "(－2)²＝4，平方後結果為正。"),
    ("下列哪一項與 3x 是同類項？", ["7x", "7x²", "7", "7y"], "A", "3x 與 7x 的變數相同且次數相同，屬於同類項。"),
    ("將 2(x＋3) 展開，結果為何？", ["2x＋6", "2x＋3", "x＋6", "2x＋5"], "A", "用分配律將 2 乘入括號，得到 2x＋6。"),
    ("當 x＝2 時，3＋x² 的值為何？", ["7", "10", "25", "5"], "A", "先算平方：2²＝4，再加 3 得 7。"),
    ("原有 n 元，花去 35 元後剩下多少元？", ["n－35", "35－n", "n＋35", "35n"], "A", "從原有金額 n 扣除 35，代數式為 n－35。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-7-1-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究代數符號、代入、同類項與分配律能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 algebra-symbol questions")

if __name__ == "__main__":
    main()
