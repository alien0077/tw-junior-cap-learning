"""以公開數學試題的比例推理與情境應用方向，獨立替換 N-9-1 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-9-1.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-9-1"
KNOWLEDGE = "kg-math-content-n-9-1"

ITEMS = [
    ("三個數的連比為 2：3：4，三數總和為 45，則第二個數是多少？", ["15", "10", "20", "12"], "A", "總份數為 2＋3＋4＝9，每份 45÷9＝5，第二個數為 3×5＝15。"),
    ("若甲：乙＝2：3，乙：丙＝4：5，則甲：乙：丙可化為何者？", ["8：12：15", "2：3：5", "8：3：15", "2：12：5"], "A", "讓乙相同：2：3 擴成 8：12，4：5 擴成 12：15，所以連比為 8：12：15。"),
    ("若 x：y：z＝3：4：5，且 x＋y＋z＝48，則 x 為何？", ["12", "9", "16", "20"], "A", "總份數 12，每份 48÷12＝4，因此 x＝3×4＝12。"),
    ("三項數量比為 2：3：4，總數為 72，則中間項是多少？", ["24", "18", "32", "36"], "A", "總份數 9，每份 72÷9＝8，中間項為 3×8＝24。"),
    ("若 a：b：c＝4：5：6，且比例倍數為 3，則 a＋b＋c 為何？", ["45", "15", "30", "60"], "A", "各項為 12、15、18，總和為 12＋15＋18＝45。"),
    ("若甲：乙＝3：5，乙：丙＝2：7，則甲：乙：丙可化為何者？", ["6：10：35", "3：5：7", "6：5：14", "3：10：7"], "A", "讓乙相同：3：5 擴成 6：10，2：7 擴成 10：35，所以為 6：10：35。"),
    ("食譜中麵粉：糖：水＝4：2：3，總共使用 18 杯材料，麵粉需幾杯？", ["8 杯", "6 杯", "9 杯", "12 杯"], "A", "總份數為 9，每份 18÷9＝2，麵粉為 4×2＝8 杯。"),
    ("三人的年齡比為 2：3：4，年齡總和為 45 歲，年紀最小者幾歲？", ["10 歲", "12 歲", "15 歲", "8 歲"], "A", "總份數 9，每份 5 歲，最小者為 2×5＝10 歲。"),
    ("若三個數的比為 5：6：8，且第三個數為 24，則第一個數為何？", ["15", "18", "20", "12"], "A", "8 變成 24 是乘以 3，因此第一個數為 5×3＝15。"),
    ("下列哪一組連比與 3：4：5 相等？", ["6：8：10", "6：7：10", "3：8：5", "9：12：20"], "A", "3：4：5 的各項同乘以 2 得 6：8：10。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-9-1-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究連比整合、共同項、比例分配與生活情境能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 chain-ratio questions")


if __name__ == "__main__":
    main()
