"""以公開考題能力方向獨立改寫 n-Ⅳ-5 二次方根與根式題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-n-iv-5"
KG_ID = "kg-math-performance-n-iv-5"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("√49 的值為何？", ["－7", "－1", "1", "7"], "D", "√49 表示 49 的非負平方根，因此 √49＝7。"),
    ("將 √72 化成最簡根式，何者正確？", ["6√2", "8√2", "6√3", "12√2"], "A", "72＝36×2，所以 √72＝√36×√2＝6√2。"),
    ("計算 3√5＋2√5 的結果為何？", ["5√5", "5√10", "6√5", "6√10"], "A", "兩項是同類根式，只需相加係數：(3＋2)√5＝5√5。"),
    ("計算 √12×√3 的值為何？", ["3", "6", "√15", "2√3"], "B", "√12×√3＝√(12×3)＝√36＝6。"),
    ("將 1/√3 化為分母為有理數的等值式，何者正確？", ["√3/3", "3/√3", "√3", "1/3"], "A", "分子分母同乘 √3：1/√3＝√3/(√3×√3)＝√3/3。"),
    ("比較 √7 與 2.5 的大小，何者正確？", ["√7＜2.5", "√7＝2.5", "√7＞2.5", "無法比較"], "C", "因為 2.5²＝6.25＜7，且兩者皆為正數，所以 √7＞2.5。"),
    ("若 √x＝5，且 x 為非負數，則 x 為何？", ["5", "10", "20", "25"], "D", "兩邊平方得 x＝5²＝25，且 25 符合非負條件。"),
    ("直角三角形兩股長分別為 6 與 8，斜邊長為何？", ["√14", "√28", "10", "14"], "C", "由畢氏定理，斜邊＝√(6²＋8²)＝√100＝10。"),
    ("化簡 √50－√8 的結果為何？", ["3√2", "4√2", "√42", "7√2"], "A", "√50＝5√2、√8＝2√2，所以相減得 3√2。"),
    ("正方形邊長為 √12 公分，其面積為何？", ["6 平方公分", "12 平方公分", "24 平方公分", "√24 平方公分"], "B", "正方形面積為邊長平方：(√12)²＝12 平方公分。"),
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
        "id": f"question-math-performance-n-iv-5-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考平方根化簡、同類根式、根式運算、大小比較、方程式與幾何情境題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "二次方根與根式單元實質改寫；已重新計算平方根、最簡根式、同類根式、根式乘法、大小比較、根式方程式與幾何答案，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-n-iv-5-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} radical questions")
