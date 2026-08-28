"""以公開考題能力方向獨立改寫 n-Ⅳ-3 指數與科學記號題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-n-iv-3"
KG_ID = "kg-math-performance-n-iv-3"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("計算 2³×2⁴ 的值為何？", ["32", "64", "128", "256"], "C", "同底數相乘指數相加：2³×2⁴＝2⁷＝128。"),
    ("計算 (3²)³ 的值為何？", ["81", "243", "729", "2187"], "C", "次方的次方指數相乘：(3²)³＝3⁶＝729。"),
    ("5⁰ 的值為何？", ["0", "1", "5", "25"], "B", "非零數的零次方等於 1，所以 5⁰＝1。"),
    ("將 0.00042 用科學記號表示，何者正確？", ["4.2×10⁻⁴", "4.2×10⁴", "42×10⁻⁵", "0.42×10⁻³"], "A", "小數點向右移 4 位得到 4.2，因此乘以 10⁻⁴；且 4.2 落在 1 到 10 之間。"),
    ("6.3×10⁵ 的一般記號為何？", ["6300", "63000", "630000", "6300000"], "C", "10⁵ 表示小數點向右移 5 位，6.3×10⁵＝630000。"),
    ("計算 10³×10⁻² 的值為何？", ["0.1", "1", "10", "100"], "C", "同底數相乘指數相加：10³×10⁻²＝10¹＝10。"),
    ("72 的質因數分解為何？", ["2²×3²", "2³×3²", "2³×3³", "2⁴×3"], "B", "72＝8×9＝2³×3²。"),
    ("計算 2⁵÷2² 的值為何？", ["4", "8", "16", "32"], "B", "同底數相除指數相減：2⁵÷2²＝2³＝8。"),
    ("計算 (2.4×10³)＋(3.1×10³) 的結果為何？", ["5.5×10²", "5.5×10³", "5.5×10⁶", "7.44×10³"], "B", "同次方的 10³ 可提出：(2.4＋3.1)×10³＝5.5×10³。"),
    ("計算 (4.8×10⁻²)×10³ 的結果為何？", ["0.48", "4.8", "48", "480"], "C", "10⁻²×10³＝10¹，所以 4.8×10¹＝48。"),
]

def rotate(options, answer_letter):
    answer_index = ord(answer_letter) - ord("A")
    shift = (4 - answer_index) % 4
    values = options[shift:] + options[:shift]
    return [{"id": ident, "text": text} for ident, text in zip("ABCD", values)]

def make_question(index, prompt, options, answer_letter, explanation):
    source_answer = options[ord(answer_letter) - ord("A")]
    rotated = rotate(options, answer_letter)
    answer_id = next(item["id"] for item in rotated if item["text"] == source_answer)
    return {
        "id": f"question-math-performance-n-iv-3-{index}",
        "subject": "math",
        "type": "single-choice",
        "prompt": prompt,
        "options": rotated,
        "knowledgeIds": [KG_ID],
        "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考非負整數次方、指數律、質因數分解與科學記號題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "非負整數次方指數律質因數與科學記號單元實質改寫；已重新計算次方、指數律、零次方、質因數分解、科學記號轉換與運算，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-n-iv-3-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} exponent-scientific questions")
