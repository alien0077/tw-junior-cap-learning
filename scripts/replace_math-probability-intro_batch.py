"""以公開數學試題的機率判讀方向，獨立替換 D-9-2 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-d-9-2.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-d-9-2"
KNOWLEDGE = "kg-math-content-d-9-2"

ITEMS = [
    ("擲一顆公平骰子，出現偶數的機率為何？", ["1/2", "1/3", "1/6", "2/3"], "A", "偶數結果為 2、4、6，共 3 個；機率為 3/6＝1/2。"),
    ("轉動等分為 1 到 8 的轉盤，指針停在 3 的倍數的機率為何？", ["1/4", "1/8", "3/8", "1/2"], "A", "3 的倍數為 3、6，共 2 個，機率為 2/8＝1/4。"),
    ("袋中有紅球 3 顆、藍球 2 顆，任取 1 顆，取到紅球的機率為何？", ["3/5", "2/5", "1/3", "3/2"], "A", "共有 5 顆球，其中 3 顆紅球，機率為 3/5。"),
    ("連續擲兩次公平硬幣，至少出現一次正面的機率為何？", ["3/4", "1/4", "1/2", "2/3"], "A", "四種等可能結果中，只有兩次反面不符合，故有利結果 3 種，機率為 3/4。"),
    ("從編號 1 到 10 的卡片中任取 1 張，抽到大於 7 的卡片機率為何？", ["3/10", "7/10", "2/10", "1/10"], "A", "大於 7 的卡片為 8、9、10，共 3 張，機率為 3/10。"),
    ("擲一顆公平骰子，出現質數的事件與其互補事件機率各為何？", ["各為 1/2", "質數為 1/3、互補為 2/3", "各為 1/6", "質數為 2/3、互補為 1/3"], "A", "骰子上的質數為 2、3、5，共 3 個，機率 1/2；互補事件也為 1－1/2＝1/2。"),
    ("同時擲兩顆公平骰子，點數和為 7 的機率為何？", ["1/6", "1/12", "1/7", "7/36"], "A", "36 種等可能結果中，和為 7 的有 (1,6) 至 (6,1) 共 6 種，機率為 6/36＝1/6。"),
    ("從一週 7 天中等可能選 1 天，選到週末的機率為何？", ["2/7", "5/7", "1/7", "1/2"], "A", "週末有星期六、星期日共 2 天，機率為 2/7。"),
    ("在一次隨機試驗中，不可能發生的事件，其機率為何？", ["0", "1", "1/2", "無法確定"], "A", "不可能事件沒有任何有利結果，因此機率為 0。"),
    ("若事件 A 的機率為 3/8，則事件 A 的互補事件機率為何？", ["5/8", "3/8", "1/8", "8/3"], "A", "事件與其互補事件機率和為 1，因此 1－3/8＝5/8。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-d-9-2-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究樣本空間、古典機率、互補事件與抽取情境能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 introductory-probability questions")


if __name__ == "__main__":
    main()
