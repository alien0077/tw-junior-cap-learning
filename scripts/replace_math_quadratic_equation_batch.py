#!/usr/bin/env python3
"""Replace generic quadratic-equation questions with independently checked items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-math-performance-a-iv-6"
KG_ID = "kg-math-performance-a-iv-6"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

items = [
    ("方程式 x²－5x＋6＝0 的兩根為何？", ["2、3", "－2、－3", "1、6", "－1、－6"], "x²－5x＋6＝(x－2)(x－3)，所以兩根為 2、3。"),
    ("方程式 2x²－8＝0 的解為何？", ["x＝2 或 x＝－2", "x＝4 或 x＝－4", "x＝2", "x＝－2"], "2x²－8＝0 可化為 x²＝4，因此 x＝2 或 x＝－2。"),
    ("方程式 x²－6x＋5＝0 的判別式為何？", ["16", "－16", "56", "25"], "判別式 Δ＝b²－4ac＝(－6)²－4×1×5＝36－20＝16。"),
    ("方程式 x²＋4x＋1＝0 的解為何？", ["－2＋√3、－2－√3", "2＋√3、2－√3", "－4＋√3、－4－√3", "2＋√5、2－√5"], "套用公式 x＝[－4±√(16－4)]/2＝[－4±2√3]/2，得 x＝－2±√3。"),
    ("因式分解 x²－9x＋20＝0 後，方程式的兩根為何？", ["4、5", "－4、－5", "2、10", "－2、－10"], "x²－9x＋20＝(x－4)(x－5)，所以兩根為 4、5。"),
    ("一個長方形長為 x＋4、公分寬為 x 公分，面積 48 平方公分且 x＞0，x 為何？", ["6", "8", "4", "－8"], "x(x＋4)＝48，得 x²＋4x－48＝(x＋8)(x－6)＝0；因 x＞0，取 x＝6。"),
    ("若一元二次方程式的兩根為－2 與 5，且二次項係數為 1，方程式為何？", ["x²－3x－10＝0", "x²＋3x－10＝0", "x²－7x＋10＝0", "x²＋7x＋10＝0"], "根為－2、5 的方程式為 (x＋2)(x－5)＝0，展開得 x²－3x－10＝0。"),
    ("方程式 x²＋2x－8＝0 的解為何？", ["x＝2 或 x＝－4", "x＝4 或 x＝－2", "x＝8 或 x＝－1", "x＝－8 或 x＝1"], "x²＋2x－8＝(x＋4)(x－2)，所以 x＝－4 或 x＝2。"),
    ("方程式 x²＋4x＋8＝0 有幾個實數解？", ["0 個", "1 個", "2 個", "無限多個"], "判別式 Δ＝4²－4×1×8＝16－32＝－16＜0，因此沒有實數解。"),
    ("若方程式 x²－(a＋3)x＋3a＝0 的兩根為 3 與 a，當 a＝5 時兩根的和為何？", ["8", "15", "5", "3"], "方程式可分解為 (x－3)(x－a)＝0；a＝5 時兩根為 3、5，和為 8。"),
]
target_indices = [3, 2, 1, 0, 3, 2, 1, 0, 3, 2]
for i, (prompt, options, explanation) in enumerate(items, start=1):
    target = target_indices[i - 1]
    shift = (4 - target) % 4
    rotated = options[shift:] + options[:shift]
    data = {
        "id": f"question-math-performance-a-iv-6-{i}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考一元二次方程、因式分解、公式法、判別式、根與係數及幾何情境題型；本題使用全新數值、情境與選項，非原題重製。",
            "authoringNote": "一元二次方程單元實質改寫；已重新解方程並核對判別式、根與正值限制，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }
    (ROOT / f"questions/math/question-math-performance-a-iv-6-{i}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"replaced {len(items)} quadratic-equation questions")
