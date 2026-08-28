#!/usr/bin/env python3
"""Replace generic simultaneous-equation questions with solvable items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-math-performance-a-iv-4"
KG_ID = "kg-math-performance-a-iv-4"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

items = [
    ("若 x＋y＝10 且 x－y＝2，則 (x,y) 為何？", ["(6,4)", "(4,6)", "(8,2)", "(5,5)"], "兩式相加得 2x＝12，所以 x＝6；代回 x＋y＝10 得 y＝4。"),
    ("解聯立方程式 2x＋y＝11、x－y＝1，x 的值為何？", ["4", "3", "5", "6"], "兩式相加得 3x＝12，所以 x＝4；再由 x－y＝1 得 y＝3。"),
    ("成人票每張 8 元、學生票每張 5 元，共售出 32 張、收入 214 元。成人票售出幾張？", ["18 張", "14 張", "16 張", "20 張"], "設成人票 x、學生票 y，x＋y＝32、8x＋5y＝214；代入 y＝32－x 得 3x＝54，所以 x＝18。"),
    ("兩直線 y＝2x＋1 與 y＝x＋4 的交點為何？", ["(3,7)", "(7,3)", "(2,5)", "(4,9)"], "交點滿足 2x＋1＝x＋4，得 x＝3；代回 y＝x＋4 得 y＝7，所以交點為 (3,7)。"),
    ("2 枝相同原子筆與 3 本相同筆記本共 96 元；1 枝原子筆與 1 本筆記本共 37 元。1 枝原子筆多少元？", ["15 元", "22 元", "18 元", "12 元"], "設筆價 x、筆記本 y，2x＋3y＝96、x＋y＝37；由 x＝37－y 代入得 y＝22，故 x＝15。"),
    ("下列哪一組數是聯立方程式 x＋y＝9、2x－y＝6 的解？", ["(5,4)", "(4,5)", "(3,6)", "(6,3)"], "(5,4) 代入第一式得 9，代入第二式得 10－4＝6，兩式皆成立。"),
    ("兩個數的和為 45，較大數比小數多 9，較大數為何？", ["27", "18", "24", "30"], "設大數 x、小數 y，x＋y＝45、x－y＝9；相加得 2x＝54，所以 x＝27。"),
    ("聯立方程式 2x＋4y＝8、x＋2y＝5 的解有幾組？", ["無解", "一組解", "兩組解", "無限多組解"], "第一式左邊是第二式左邊的 2 倍，但右邊 8 不等於 5 的 2 倍 10，因此兩直線平行且無解。"),
    ("若 3x＋2y＝16 且 x＋y＝6，則 y 為何？", ["2", "4", "3", "1"], "由 x＝6－y 代入第一式：3(6－y)＋2y＝16，得 y＝2。"),
    ("某停車場汽車與機車共 20 輛，輪子共 56 個。汽車有幾輛？", ["8 輛", "12 輛", "6 輛", "10 輛"], "設汽車 x、機車 y，x＋y＝20、4x＋2y＝56；代入 y＝20－x 得 2x＝16，所以汽車有 8 輛。"),
]
target_indices = [3, 2, 1, 0, 3, 2, 1, 0, 3, 2]
for i, (prompt, options, explanation) in enumerate(items, start=1):
    target = target_indices[i - 1]
    shift = (4 - target) % 4
    rotated = options[shift:] + options[:shift]
    data = {
        "id": f"question-math-performance-a-iv-4-{i}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考代入法、消去法、交點、票券價格與數量情境題型；本題使用全新數值、情境與選項，非原題重製。",
            "authoringNote": "二元一次聯立單元實質改寫；已重新解聯立方程式並核對代回結果，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }
    (ROOT / f"questions/math/question-math-performance-a-iv-4-{i}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"replaced {len(items)} simultaneous-equation questions")
