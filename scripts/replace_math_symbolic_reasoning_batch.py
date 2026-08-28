#!/usr/bin/env python3
"""Replace the generic symbolic-reasoning questions with checkable algebra items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-math-performance-a-iv-1"
KG_ID = "kg-math-performance-a-iv-1"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

items = [
    ("若 n 為偶數，下列哪一種表示法正確？", ["n＝2k（k 為整數）", "n＝2k＋1（k 為整數）", "n＝k/2（k 為整數）", "n＝k²＋1（k 為整數）"], "偶數可表示為 2k，其中 k 為整數；2k＋1 是奇數的一般表示。"),
    ("長方形長為 x＋3、寬為 x，以下哪個式子表示其周長？", ["4x＋6", "2x＋3", "x²＋3x", "4x＋3"], "周長為 2[(x＋3)＋x]＝2(2x＋3)＝4x＋6。"),
    ("若 a＋b＝10 且 a－b＝4，則 a 的值為何？", ["7", "6", "3", "14"], "兩式相加得 2a＝14，因此 a＝7。"),
    ("要證明兩個奇數的和一定是偶數，哪一個代數式最適合作為開頭？", ["(2m＋1)＋(2n＋1)", "2m＋2n", "(m＋1)(n＋1)", "2m＋1＋n"], "任意奇數可寫成 2m＋1、2n＋1，將兩者相加即可化為 2(m＋n＋1)，顯示結果為偶數。"),
    ("連續三個整數若以 n 表示最小者，哪一組表示正確？", ["n、n＋1、n＋2", "n、2n、3n", "n－1、n、n＋1", "n²、n²＋1、n²＋2"], "相鄰整數每次相差 1；若最小者為 n，另外兩個就是 n＋1、n＋2。"),
    ("若 x＞0，哪一項必定為正數？", ["x²", "－x", "x－x", "－x²"], "正數的平方 x² 必為正；－x 為負，x－x 等於 0。"),
    ("下列哪個等式可直接說明 n(n＋1) 一定是偶數？", ["n(n＋1) 是兩個連續整數的乘積，其中一個必為偶數", "n 與 n＋1 都一定是奇數", "n(n＋1) 一定等於 2n", "n＋1 一定大於 2n"], "連續兩個整數中必有一個是偶數，所以乘積含有因數 2，必為偶數。"),
    ("若正方形邊長為 x＋2，哪個式子表示其面積？", ["x²＋4x＋4", "4x＋8", "x²＋2", "x²＋4"], "面積為 (x＋2)²＝x²＋4x＋4。"),
    ("若某數的 3 倍比它大 10，設該數為 x，哪個方程式正確？", ["3x＝x＋10", "3x＋10＝x", "x＝3x＋10", "3(x＋10)＝x"], "「3 倍比它大 10」表示 3x＝x＋10。"),
    ("若 m、n 為整數，哪一個式子一定是偶數？", ["2m＋2n", "2m＋2n＋1", "m＋n＋1", "m²＋n"], "2m＋2n＝2(m＋n)，可提出因數 2，因此一定是偶數。"),
]
target_indices = [3, 2, 1, 0, 3, 2, 1, 0, 3, 2]
for i, (prompt, options, explanation) in enumerate(items, start=1):
    target = target_indices[i - 1]
    shift = (4 - target) % 4
    rotated = options[shift:] + options[:shift]
    data = {
        "id": f"question-math-performance-a-iv-1-{i}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考代數表示、符號運算、連續整數與推理證明題型；本題使用全新數值、情境與選項，非原題重製。",
            "authoringNote": "符號文字表達與推理單元實質改寫；已重新推導答案與解析，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }
    (ROOT / f"questions/math/question-math-performance-a-iv-1-{i}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"replaced {len(items)} symbolic reasoning questions")
