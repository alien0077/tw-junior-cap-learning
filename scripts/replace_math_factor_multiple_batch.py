"""以公開考題能力方向獨立改寫 n-Ⅳ-1 因數倍數題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-n-iv-1"
KG_ID = "kg-math-performance-n-iv-1"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("84 的質因數分解為何？", ["2²×3×7", "2×3²×7", "2²×3²×7", "2×3×14"], "A", "84＝4×21＝2²×3×7，且 2、3、7 都是質數。"),
    ("36 與 48 的最大公因數為何？", ["6", "8", "12", "16"], "C", "36＝2²×3²、48＝2⁴×3，共同質因數的最低次方為 2²×3＝12。"),
    ("12 與 18 的最小公倍數為何？", ["24", "30", "36", "54"], "C", "12＝2²×3、18＝2×3²，取各質因數最高次方得 2²×3²＝36。"),
    ("18、30、42 的最大公因數為何？", ["3", "6", "9", "12"], "B", "18、30、42 的共同因數中，6 可整除三者，且沒有更大的共同因數，所以最大公因數為 6。"),
    ("甲鈴每 8 分鐘響一次，乙鈴每 12 分鐘響一次。兩鈴同時響後，至少再過幾分鐘會再次同時響？", ["16 分鐘", "20 分鐘", "24 分鐘", "48 分鐘"], "C", "要找 8 與 12 的最小公倍數；LCM(8,12)＝24，所以 24 分鐘後再次同時響。"),
    ("有一面 24 公分×36 公分的長方形牆面，要用邊長相同且不裁切的最大正方形磁磚鋪滿，磁磚邊長為何？", ["6 公分", "8 公分", "12 公分", "18 公分"], "C", "正方形邊長須同時整除 24 與 36，最大值為 gcd(24,36)＝12 公分。"),
    ("正整數 24 共有幾個正因數？", ["6 個", "8 個", "10 個", "12 個"], "B", "24＝2³×3¹，正因數個數為 (3＋1)(1＋1)＝8 個。"),
    ("下列哪一組數互質？", ["14 與 21", "15 與 25", "16 與 27", "18 與 24"], "C", "16 的質因數只有 2，27 的質因數只有 3，最大公因數為 1，因此互質。"),
    ("將 42/56 約成最簡分數後為何？", ["2/3", "3/4", "4/5", "5/6"], "B", "42 與 56 的最大公因數為 14，分子分母同除以 14 得 3/4。"),
    ("最小的正整數中，同時為 6、8、15 的倍數者為何？", ["60", "90", "120", "240"], "C", "6＝2×3、8＝2³、15＝3×5，最小公倍數為 2³×3×5＝120。"),
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
        "id": f"question-math-performance-n-iv-1-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考因數、倍數、質因數分解、最大公因數、最小公倍數、互質與週期情境題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "因數倍數質數與最大公因數最小公倍數單元實質改寫；已重新計算質因數分解、GCD、LCM、因數個數、互質、約分與週期情境，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-n-iv-1-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} factor-multiple questions")
