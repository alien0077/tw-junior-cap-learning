"""以公開國中數學段考的多項式概念方向，獨立替換 A-8-2 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-8-2.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-8-2"
KNOWLEDGE = "kg-math-content-a-8-2"
ITEMS = [
    ("多項式 7x＋3 有幾項？", ["2 項", "1 項", "3 項", "7 項"], "A", "以加減號分隔可看出 7x 與 3，共有 2 項。"),
    ("在單項式－5a² 中，a² 的係數為何？", ["－5", "5", "－2", "2"], "A", "係數是乘在字母部分前的數字，因此為－5。"),
    ("多項式 4y³－y＋2 的次數為何？", ["3", "2", "1", "4"], "A", "最高次項為 4y³，所以多項式次數是 3。"),
    ("下列哪一組是同類項？", ["3m 與－8m", "3m 與 3m²", "m² 與 m³", "4 與 4n"], "A", "同類項的字母部分與各字母次數必須相同，3m 與－8m 符合。"),
    ("若 P(x)＝2x²－3x＋1，則 P(2) 為何？", ["3", "5", "7", "11"], "A", "代入 x＝2：2×4－3×2＋1＝8－6＋1＝3。"),
    ("多項式 6b²＋4b－9 的常數項為何？", ["－9", "4", "6", "9"], "A", "不含字母的項是常數項，因此為－9。"),
    ("下列哪一個是以 x 為變數的多項式？", ["2x²－3x＋1", "1/x＋2", "√x＋1", "x⁻²＋4"], "A", "多項式的變數次方必須是非負整數，第一式符合。"),
    ("化簡 4p＋2－p，結果為何？", ["3p＋2", "3p－2", "5p＋2", "4p＋1"], "A", "合併同類項 4p－p 得 3p，常數 2 保留。"),
    ("將 5x²－7 寫成含有 x 項係數為 0 的形式，應為何？", ["5x²＋0x－7", "5x²＋7x", "5x－7", "0x²＋5x－7"], "A", "缺少的 x 項可寫成 0x，故為 5x²＋0x－7。"),
    ("在 6z²－4z＋11 中，z 項的係數為何？", ["－4", "6", "11", "4"], "A", "含 z 的項是－4z，因此其係數為－4。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-8-2-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究多項式項、係數、次數與代入能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 polynomial-meaning questions")

if __name__ == "__main__":
    main()
