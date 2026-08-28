#!/usr/bin/env python3
"""Replace one probability lesson with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-math-content-d-9-3"
KID = "kg-math-content-d-9-3"
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("公平骰子擲一次，出現大於 4 點的機率為何？", ["1/2", "1/3", "2/3", "1/6"], "B", "樣本空間有 6 個等可能結果，5、6 共 2 個有利結果，因此機率為 2/6=1/3。", "第11題等可能抽取題型改編"),
    ("同時擲兩顆公平骰子，點數和為 7 的機率為何？", ["1/12", "1/4", "1/6", "1/3"], "C", "兩顆骰子共有 36 種等可能結果，和為 7 的組合有 6 種，機率為 6/36=1/6。", "第11題等可能結果比較題型改編"),
    ("袋中有編號 1 至 8 的八顆球，隨機取一顆，取到偶數球的機率為何？", ["1/2", "1/4", "3/8", "5/8"], "A", "偶數球為 2、4、6、8，共 4 顆；機率為 4/8=1/2。", "第11題等可能抽取題型改編"),
    ("轉盤分成 5 個大小相同區域，其中 2 區標示獎品。隨機轉一次得到獎品的機率為何？", ["2/5", "1/5", "3/5", "1/2"], "A", "五區等可能，兩區是有利結果，所以機率為 2/5。", "第11題等可能結果比較題型改編"),
    ("從編號 1 至 10 的卡片中隨機抽 1 張，抽到質數的機率為何？", ["1/5", "2/5", "1/2", "3/5"], "B", "1 至 10 的質數為 2、3、5、7，共 4 張，機率為 4/10=2/5。", "第11題卡片抽取題型改編"),
    ("公平硬幣連續投擲兩次，至少出現一次正面的機率為何？", ["1/4", "1/2", "2/3", "3/4"], "D", "四種等可能結果中，只有反反沒有正面，其餘三種符合條件，因此為 3/4。", "第11題多次等可能結果題型改編"),
    ("從 1 至 12 的整數中隨機選取一個，選到 3 的倍數的機率為何？", ["1/4", "1/3", "1/2", "2/3"], "B", "3 的倍數有 3、6、9、12，共 4 個；機率為 4/12=1/3。", "第11題等可能抽取題型改編"),
    ("袋中有紅球 3 顆、藍球 2 顆，隨機取出 1 顆，取到紅球的機率為何？", ["2/5", "3/5", "1/2", "3/2"], "B", "共有 5 顆球，其中 3 顆紅球，機率為 3/5。", "第11題不同類別卡片比較題型改編"),
    ("從 1 至 6 的卡片中隨機抽 1 張，抽到不是 1 的機率為何？", ["1/6", "1/3", "2/3", "5/6"], "D", "不是 1 的卡片有 5 張，全部有 6 張，機率為 5/6。", "第11題有利與不利結果比較題型改編"),
    ("一個袋子中有 4 顆白球與 6 顆黑球，隨機取 1 顆，取到白球的機率為何？", ["3/5", "2/5", "1/4", "4/6"], "B", "共有 10 顆球，白球 4 顆，機率為 4/10=2/5。", "第11題不同類別卡片比較題型改編"),
]

for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "math" / f"question-math-content-d-9-3-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考數學科；{locator}；官方答案表：{ANSWER}；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style math probability questions")
