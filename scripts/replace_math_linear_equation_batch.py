#!/usr/bin/env python3
"""Replace generic one-variable-equation questions with solvable items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-math-performance-a-iv-2"
KG_ID = "kg-math-performance-a-iv-2"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

items = [
    ("解方程式 3x＋4＝19，x 為何？", ["5", "4", "6", "7"], "兩邊減 4 得 3x＝15，再除以 3，所以 x＝5。"),
    ("解方程式 5x－7＝18，x 為何？", ["5", "4", "6", "7"], "兩邊加 7 得 5x＝25，再除以 5，所以 x＝5。"),
    ("解方程式 2(x＋3)＝18，x 為何？", ["6", "9", "12", "3"], "兩邊除以 2 得 x＋3＝9，再減 3，所以 x＝6。"),
    ("解方程式 7－2x＝15，x 為何？", ["－4", "4", "－11", "11"], "兩邊減 7 得－2x＝8，再除以－2，所以 x＝－4。"),
    ("解方程式 4x＋3＝2x＋15，x 為何？", ["6", "9", "4", "12"], "移項得 4x－2x＝15－3，即 2x＝12，所以 x＝6。"),
    ("解方程式 0.5x＋2＝5，x 為何？", ["6", "4", "3", "8"], "兩邊減 2 得 0.5x＝3，再除以 0.5，所以 x＝6。"),
    ("一本筆記本售價 x 元，一枝筆比筆記本貴 10 元；買 1 本與 1 枝共 50 元，筆記本售價為何？", ["20 元", "25 元", "15 元", "30 元"], "依題意 x＋(x＋10)＝50，得 2x＝40，所以筆記本售價為 20 元。"),
    ("長方形長為 x＋4 公分、寬為 x 公分，周長為 40 公分，x 為何？", ["8", "6", "10", "12"], "2[(x＋4)＋x]＝40，得 4x＋8＝40，所以 x＝8。"),
    ("女兒今年 x 歲，媽媽年齡是女兒的 3 倍多 4 歲；兩人年齡和為 44 歲，女兒幾歲？", ["10 歲", "12 歲", "8 歲", "14 歲"], "x＋(3x＋4)＝44，得 4x＝40，所以女兒為 10 歲。"),
    ("方程式 2x＋3＝2x＋7 的解為何？", ["無解", "x＝2", "x＝4", "所有數都是解"], "兩邊同減 2x 後得到 3＝7，矛盾，因此此方程式無解。"),
]
target_indices = [3, 2, 1, 0, 3, 2, 1, 0, 3, 2]
for i, (prompt, options, explanation) in enumerate(items, start=1):
    target = target_indices[i - 1]
    shift = (4 - target) % 4
    rotated = options[shift:] + options[:shift]
    data = {
        "id": f"question-math-performance-a-iv-2-{i}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考一元一次方程式、移項、括號、分數小數與生活情境題型；本題使用全新數值、情境與選項，非原題重製。",
            "authoringNote": "一元一次方程單元實質改寫；已重新解方程式並核對代回結果，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }
    (ROOT / f"questions/math/question-math-performance-a-iv-2-{i}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"replaced {len(items)} linear-equation questions")
