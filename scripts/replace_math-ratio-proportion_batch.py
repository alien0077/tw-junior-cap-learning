"""以公開數學試題的比與比例應用方向，獨立替換 N-7-9 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-7-9.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-7-9"
KNOWLEDGE = "kg-math-content-n-7-9"

ITEMS = [
    ("比 12：18 化簡為最簡整數比為何？", ["2：3", "3：2", "4：6", "6：9"], "A", "12 與 18 同除以最大公因數 6，得 2：3。"),
    ("若甲：乙＝5：8，且甲為 20，則乙為多少？", ["32", "25", "13", "40"], "A", "5 變成 20 是乘以 4，因此乙也乘以 4：8×4＝32。"),
    ("若 x/6＝4/3，則 x 為何？", ["8", "2", "18", "24"], "A", "交叉相乘得 3x＝24，所以 x＝8。"),
    ("若 7：9＝x：27，則 x 為何？", ["21", "18", "24", "27"], "A", "9 乘以 3 得 27，因此 7 也乘以 3，x＝21。"),
    ("地圖比例尺為 1：50000，圖上距離 3 公分代表實際距離多少？", ["1.5 公里", "0.15 公里", "15 公里", "150 公里"], "A", "實際距離為 3×50000＝150000 公分＝1.5 公里。"),
    ("某班男生：女生＝3：5，全班 32 人，男生有幾人？", ["12 人", "15 人", "20 人", "8 人"], "A", "總份數 3＋5＝8，每份 32÷8＝4，男生為 3×4＝12 人。"),
    ("紅色顏料：藍色顏料＝2：3，共調配 25 杯，紅色顏料有幾杯？", ["10 杯", "12 杯", "15 杯", "5 杯"], "A", "總份數為 5，每份 25÷5＝5，紅色為 2×5＝10 杯。"),
    ("下列哪一個比和 4：7 相等？", ["20：35", "12：28", "16：21", "24：35"], "A", "4：7 的前後項同乘以 5 得 20：35。"),
    ("腳踏車 3 小時行駛 180 公里，平均每小時行駛多少公里？", ["60 公里", "90 公里", "183 公里", "540 公里"], "A", "平均速率為路程÷時間＝180÷3＝60 公里／小時。"),
    ("下列哪個比例式成立？", ["6：8＝9：12", "6：8＝8：6", "6：9＝8：12", "6：8＝9：16"], "A", "6/8＝3/4，9/12 也等於 3/4，因此比例式成立。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-7-9-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究比值化簡、比例式、單位換算與生活情境能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 ratio-proportion questions")


if __name__ == "__main__":
    main()
