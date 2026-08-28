"""以公開國中數學段考的一元一次方程式應用題方向，獨立替換 A-7-3 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-7-3.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-7-3"
KNOWLEDGE = "kg-math-content-a-7-3"
ITEMS = [
    ("小芸原有一些貼紙，送出 9 張後剩 24 張。她原有幾張？", ["33", "15", "27", "216"], "A", "設原有 x 張，x－9＝24，所以 x＝33。"),
    ("解方程式 4x－7＝21，x 為何？", ["7", "5", "14", "28"], "A", "同加 7 得 4x＝28，再除以 4 得 x＝7。"),
    ("三盒彩筆每盒有 x 枝，另外有 6 枝，共有 27 枝。x 為何？", ["7", "8", "9", "25"], "A", "3x＋6＝27，得 3x＝21，所以 x＝7。"),
    ("計程車起程費 70 元，每公里 15 元；車資共 220 元時，行駛幾公里？", ["10", "11", "15", "150"], "A", "設里程 x，70＋15x＝220，得 15x＝150，所以 x＝10。"),
    ("兩個連續整數的和為 41，較小的整數為何？", ["20", "19", "21", "40"], "A", "設較小者為 x，x＋(x＋1)＝41，得 2x＝40，所以 x＝20。"),
    ("一本筆記本比一枝筆貴 18 元，兩者共 62 元。筆的價格為何？", ["22 元", "40 元", "18 元", "44 元"], "A", "設筆價 x，筆記本為 x＋18；2x＋18＝62，得 x＝22。"),
    ("三角形三邊長分別為 x、x＋2、x＋4 公分，周長 30 公分。x 為何？", ["8", "6", "10", "12"], "A", "x＋(x＋2)＋(x＋4)＝30，得 3x＋6＝30，所以 x＝8。"),
    ("兒子今年 x 歲，父親年齡是兒子的 2 倍再多 5 歲；父親 29 歲時，兒子幾歲？", ["12", "10", "17", "24"], "A", "2x＋5＝29，得 2x＝24，所以 x＝12。"),
    ("某數的 3 倍再加 5 等於 26，某數為何？", ["7", "9", "21", "31"], "A", "設某數為 x，3x＋5＝26，得 3x＝21，所以 x＝7。"),
    ("班費每人繳 x 元，18 人共收 540 元；每人應繳多少元？", ["30 元", "18 元", "36 元", "540 元"], "A", "18x＝540，兩邊同除以 18，得到 x＝30。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-7-3-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究一元一次方程式列式、求解與應用能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 linear-equation application questions")

if __name__ == "__main__":
    main()
