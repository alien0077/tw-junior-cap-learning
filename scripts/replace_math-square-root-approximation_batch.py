"""以公開數學試題的根式估算方向，獨立替換 N-8-2 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-8-2.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-8-2"
KNOWLEDGE = "kg-math-content-n-8-2"

ITEMS = [
    ("√10 的值介於哪兩個相鄰整數之間？", ["3 與 4", "2 與 3", "4 與 5", "9 與 10"], "A", "因 3²＝9＜10＜16＝4²，所以 √10 介於 3 與 4 之間。"),
    ("√20 的值介於哪兩個相鄰整數之間？", ["4 與 5", "3 與 4", "5 與 6", "19 與 21"], "A", "因 4²＝16＜20＜25＝5²，所以 √20 介於 4 與 5 之間。"),
    ("√7 四捨五入到小數第一位約為多少？", ["2.6", "2.5", "2.7", "3.0"], "A", "√7 約為 2.645，四捨五入到小數第一位為 2.6。"),
    ("√30 四捨五入到最接近的整數約為多少？", ["5", "4", "6", "30"], "A", "√30 約為 5.477，最接近的整數是 5。"),
    ("√50 四捨五入到小數第一位約為多少？", ["7.1", "7.0", "7.2", "5.0"], "A", "√50 約為 7.071，四捨五入到小數第一位為 7.1。"),
    ("已知 3.1²＝9.61、3.2²＝10.24，則 √10 落在哪個範圍？", ["3.1＜√10＜3.2", "3.0＜√10＜3.1", "3.2＜√10＜3.3", "9.61＜√10＜10.24"], "A", "因 9.61＜10＜10.24，開平方後得 3.1＜√10＜3.2。"),
    ("下列哪個數值比 √2 更接近？", ["1.4", "1.3", "1.5", "1.6"], "A", "√2 約為 1.414，與 1.4 的差約 0.014，小於與其他選項的差。"),
    ("若以 2.24 近似 √5，則此近似值與 √5 的誤差小於多少？", ["0.01", "0.1", "1", "2"], "A", "√5 約為 2.236，|2.24－√5| 約為 0.004，小於 0.01。"),
    ("比較 √18 與 4，下列何者正確？", ["√18＞4", "√18＜4", "√18＝4", "無法比較"], "A", "因 4²＝16＜18，所以 √18＞√16＝4。"),
    ("正方形面積為 20 平方公分，邊長四捨五入到小數第一位約為多少公分？", ["4.5", "4.4", "5.0", "20.0"], "A", "邊長為 √20 約 4.472 公分，四捨五入到小數第一位為 4.5 公分。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-8-2-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究平方根夾逼、近似值、四捨五入與誤差判斷能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 square-root approximation questions")


if __name__ == "__main__":
    main()
