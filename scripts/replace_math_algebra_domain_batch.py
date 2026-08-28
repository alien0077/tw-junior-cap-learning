#!/usr/bin/env python3
"""Replace the generic algebra-domain questions with independently authored items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-math-performance-a"
KG_ID = "kg-math-performance-a"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CAP_SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"

items = [
    ("化簡 3x＋2x－4 後，結果為何？", ["5x－4", "5x＋4", "x－4", "6x－4"], "3x 與 2x 是同類項，相加為 5x，常數項－4 保留，所以結果是 5x－4。"),
    ("若 2x＋5＝17，則 x 為何？", ["6", "11", "8", "4"], "等式兩邊先減 5 得 2x＝12，再除以 2，得到 x＝6。"),
    ("當 a＝3 時，2a²－a 的值為何？", ["15", "9", "12", "18"], "代入 a＝3：2×3²－3＝18－3＝15。"),
    ("利用分配律展開 4(x－3)，結果為何？", ["4x－12", "4x－3", "x－12", "4x＋12"], "4 乘入括號內各項，得到 4×x－4×3＝4x－12。"),
    ("多項式 6x＋9 的公因式分解結果為何？", ["3(2x＋3)", "6(x＋9)", "9(6x＋1)", "3(2x＋9)"], "6x 與 9 的最大公因數是 3，提出 3 後得 3(2x＋3)。"),
    ("長方形長為 x＋2、寬為 x，若 x＝5，則其周長為何？", ["24", "35", "14", "12"], "代入後長為 7、寬為 5，周長為 2(7＋5)＝24。"),
    ("化簡 2(x＋3)－(x－1)，結果為何？", ["x＋7", "x＋5", "3x＋5", "x－5"], "展開並合併同類項：2x＋6－x＋1＝x＋7。"),
    ("若 3m－2＝10，則 m＋4 為何？", ["8", "6", "10", "12"], "由 3m＝12 得 m＝4，因此 m＋4＝8。"),
    ("下列哪一組是同類項？", ["3a² 與－5a²", "3a 與 3a²", "x y 與 x²y", "7 與 7b"], "同類項必須含有相同的變數且各變數次方相同；3a² 與－5a² 符合。"),
    ("展開 (x＋2)(x＋3)，結果為何？", ["x²＋5x＋6", "x²＋6x＋5", "x²＋x＋6", "x²＋6"], "逐項相乘：x²＋3x＋2x＋6，合併後為 x²＋5x＋6。"),
]
target_indices = [3, 2, 1, 0, 3, 2, 1, 0, 3, 2]
for i, (prompt, options, explanation) in enumerate(items, start=1):
    target = target_indices[i - 1]
    shift = (4 - target) % 4
    rotated = options[shift:] + options[:shift]
    data = {
        "id": f"question-math-performance-a-{i}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考代數式、同類項、分配律、代入、方程式與因式分解題型；另參考 114 年國中教育會考數學科；本題使用全新數值、情境與選項，非原題重製。",
            "authoringNote": "代數單元實質改寫；已重新計算答案與解析，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }
    (ROOT / f"questions/math/question-math-performance-a-{i}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"replaced {len(items)} algebra questions")
