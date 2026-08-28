"""以公開國中數學段考的一元一次方程式能力方向，獨立替換 A-7-2 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-7-2.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-7-2"
KNOWLEDGE = "kg-math-content-a-7-2"
ITEMS = [
    ("方程式 x＋7＝19 的解為何？", ["12", "10", "13", "26"], "A", "等式兩邊同減 7，得到 x＝12。"),
    ("方程式 3x＝27 的解為何？", ["9", "8", "24", "30"], "A", "等式兩邊同除以 3，得到 x＝9。"),
    ("方程式 2x＋5＝17 的解為何？", ["6", "5", "11", "12"], "A", "先同減 5 得 2x＝12，再同除以 2 得 x＝6。"),
    ("方程式 5x－8＝22 的解為何？", ["6", "4", "14", "30"], "A", "先同加 8 得 5x＝30，再同除以 5 得 x＝6。"),
    ("方程式 4(x－2)＝20 的解為何？", ["7", "5", "6", "8"], "A", "兩邊同除以 4 得 x－2＝5，因此 x＝7。"),
    ("方程式 x÷3＋4＝9 的解為何？", ["15", "5", "13", "27"], "A", "先同減 4 得 x÷3＝5，再乘以 3 得 x＝15。"),
    ("方程式 7－2x＝－5 的解為何？", ["6", "－6", "1", "12"], "A", "同減 7 得－2x＝－12，再除以－2 得 x＝6。"),
    ("方程式 3x＋4＝2x＋11 的解為何？", ["7", "5", "15", "－7"], "A", "兩邊同減 2x、同減 4，得到 x＝7。"),
    ("長為 x＋2、寬為 x 的長方形周長是 28，x 為何？", ["6", "5", "7", "12"], "A", "2[(x＋2)＋x]＝28，化簡 4x＋4＝28，得 x＝6。"),
    ("方程式 (2/5)x＝14 的解為何？", ["35", "28", "14/5", "70"], "A", "等式兩邊乘以 5/2，得到 x＝14×5/2＝35。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-7-2-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究一元一次方程式、移項、驗算與情境建模能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 linear-equation questions")

if __name__ == "__main__":
    main()
