#!/usr/bin/env python3
"""Replace generic one-variable-inequality questions with checkable items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-math-performance-a-iv-3"
KG_ID = "kg-math-performance-a-iv-3"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

items = [
    ("解不等式 3x＋2＜14，解集為何？", ["x＜4", "x＞4", "x≤4", "x≥4"], "兩邊減 2 得 3x＜12，再除以正數 3，得到 x＜4。"),
    ("解不等式－2x＋5≥11，解集為何？", ["x≤－3", "x≥－3", "x≤3", "x≥3"], "兩邊減 5 得－2x≥6；除以負數－2 時不等號反向，得到 x≤－3。"),
    ("解不等式 4－x＞1，解集為何？", ["x＜3", "x＞3", "x≤3", "x≥3"], "兩邊減 4 得－x＞－3；乘以－1 時不等號反向，得到 x＜3。"),
    ("解不等式 2(x－1)≤8，解集為何？", ["x≤5", "x≥5", "x≤3", "x≥3"], "兩邊除以 2 得 x－1≤4，再加 1，得到 x≤5。"),
    ("遊樂園門票每張 6 元，另收固定入場費 5 元；預算不超過 35 元，最多可買幾張票？", ["5 張", "4 張", "6 張", "3 張"], "設票數為 x，6x＋5≤35，得 x≤5；因票數為整數，最多 5 張。"),
    ("若 x 為整數且－2＜x≤3，下列何者可能是 x 的最大值？", ["3", "2", "4", "－2"], "條件包含 x≤3，且 3 符合－2＜3，因此最大整數值為 3。"),
    ("數線上要表示不等式 x≥－1，應如何畫？", ["在－1 畫實心點並向右延伸", "在－1 畫空心點並向右延伸", "在－1 畫實心點並向左延伸", "在 1 畫實心點並向右延伸"], "≥ 包含邊界，所以－1 要畫實心點；大於－1 的數在右側，應向右延伸。"),
    ("解不等式 5x－7＞3x＋1，解集為何？", ["x＞4", "x＜4", "x≥4", "x≤4"], "移項得 2x＞8，再除以正數 2，得到 x＞4。"),
    ("現在氣溫為 12°C，每小時下降 3°C。至少經過幾小時後，氣溫會低於 0°C？", ["超過 4 小時", "4 小時", "3 小時", "12 小時"], "設經過 h 小時，12－3h＜0，得 h＞4；所以必須超過 4 小時。"),
    ("不等式 x≤2 在數線上的表示方式為何？", ["2 畫實心點，向左延伸", "2 畫空心點，向左延伸", "2 畫實心點，向右延伸", "2 畫空心點，向右延伸"], "≤ 包含 2，所以畫實心點；小於 2 的數在左側，應向左延伸。"),
]
target_indices = [3, 2, 1, 0, 3, 2, 1, 0, 3, 2]
for i, (prompt, options, explanation) in enumerate(items, start=1):
    target = target_indices[i - 1]
    shift = (4 - target) % 4
    rotated = options[shift:] + options[:shift]
    data = {
        "id": f"question-math-performance-a-iv-3-{i}",
        "subject": "math",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(rotated)],
        "knowledgeIds": [KG_ID],
        "difficulty": ("easy", "medium", "hard")[(i - 1) % 3],
        "answer": {"value": chr(65 + target), "explanation": explanation},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考一元一次不等式、負數除法、數線邊界與預算／變化情境題型；本題使用全新數值、情境與選項，非原題重製。",
            "authoringNote": "一元一次不等式單元實質改寫；已重新解不等式並核對邊界與整數限制，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }
    (ROOT / f"questions/math/question-math-performance-a-iv-3-{i}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"replaced {len(items)} linear-inequality questions")
