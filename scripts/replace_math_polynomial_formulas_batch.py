#!/usr/bin/env python3
"""Replace generic polynomial/formula questions with independently checked items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-math-performance-a-iv-5"
KG_ID = "kg-math-performance-a-iv-5"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

items = [
    ("化簡 (2x＋3)＋(x－5)，結果為何？", ["3x－2", "3x＋8", "x－2", "2x－2"], "合併同類項：2x＋3＋x－5＝3x－2。"),
    ("化簡 (5x²－2x＋1)－(2x²＋x－4)，結果為何？", ["3x²－3x＋5", "3x²－x－3", "7x²－x＋5", "3x²＋3x－3"], "去括號後為 5x²－2x＋1－2x²－x＋4，合併得 3x²－3x＋5。"),
    ("展開 3x(2x－5)，結果為何？", ["6x²－15x", "6x²－5x", "5x²－15x", "6x－15"], "以分配律相乘：3x×2x－3x×5＝6x²－15x。"),
    ("展開 (x＋4)²，結果為何？", ["x²＋8x＋16", "x²＋16", "x²＋4x＋16", "x²＋8x＋8"], "完全平方公式 (a＋b)²＝a²＋2ab＋b²，代入 a＝x、b＝4 得 x²＋8x＋16。"),
    ("展開 (x－3)²，結果為何？", ["x²－6x＋9", "x²－9", "x²－3x＋9", "x²＋6x＋9"], "完全平方公式 (a－b)²＝a²－2ab＋b²，結果為 x²－6x＋9。"),
    ("利用平方差公式，(2x＋5)(2x－5) 等於何者？", ["4x²－25", "4x²＋25", "2x²－25", "4x²－10x＋25"], "平方差公式 (a＋b)(a－b)＝a²－b²，令 a＝2x、b＝5 得 4x²－25。"),
    ("因式分解 x²＋7x＋12，結果為何？", ["(x＋3)(x＋4)", "(x＋2)(x＋6)", "(x－3)(x－4)", "(x＋1)(x＋12)"], "尋找乘積 12、和 7 的兩數為 3 與 4，因此 x²＋7x＋12＝(x＋3)(x＋4)。"),
    ("因式分解 9x²－16，結果為何？", ["(3x－4)(3x＋4)", "(9x－4)(x＋4)", "(3x－8)(3x＋2)", "(9x－16)(x＋1)"], "9x²－16＝(3x)²－4²，依平方差公式分解為 (3x－4)(3x＋4)。"),
    ("利用乘法公式計算 99²，結果為何？", ["9801", "9901", "9810", "9999"], "99²＝(100－1)²＝10000－200＋1＝9801。"),
    ("展開 (x＋2)(x²－2x＋4)，結果為何？", ["x³＋8", "x³＋4x＋8", "x³－8", "x³＋2x²＋8"], "逐項相乘後中間項相消：x³－2x²＋4x＋2x²－4x＋8＝x³＋8。"),
]
target_indices = [3, 2, 1, 0, 3, 2, 1, 0, 3, 2]
for i, (prompt, options, explanation) in enumerate(items, start=1):
    target = target_indices[i - 1]
    shift = (4 - target) % 4
    rotated = options[shift:] + options[:shift]
    data = {
        "id": f"question-math-performance-a-iv-5-{i}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考多項式四則、分配律、完全平方、平方差與因式分解題型；本題使用全新數值、情境與選項，非原題重製。",
            "authoringNote": "多項式與乘法公式單元實質改寫；已重新展開／因式分解並核對答案，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }
    (ROOT / f"questions/math/question-math-performance-a-iv-5-{i}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"replaced {len(items)} polynomial/formula questions")
