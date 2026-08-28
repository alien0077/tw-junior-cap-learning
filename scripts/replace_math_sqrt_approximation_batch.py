"""以公開考題能力方向獨立改寫 n-Ⅳ-6 平方根估值題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-n-iv-6"
KG_ID = "kg-math-performance-n-iv-6"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("√20 介於哪兩個連續整數之間？", ["1 與 2", "2 與 3", "3 與 4", "4 與 5"], "D", "因為 4²＝16＜20＜25＝5²，所以 4＜√20＜5。"),
    ("√50 取到小數點後第一位約為何？", ["6.9", "7.0", "7.1", "7.2"], "C", "7.0²＝49、7.1²＝50.41，而 √50 約為 7.071，因此四捨五入到十分位為 7.1。"),
    ("√80 介於哪兩個連續整數之間？", ["6 與 7", "7 與 8", "8 與 9", "9 與 10"], "C", "因為 8²＝64＜80＜81＝9²，所以 8＜√80＜9。"),
    ("下列哪一個整數平方最接近 45？", ["5²", "6²", "7²", "8²"], "C", "45 與 7²＝49 的差為 4，與 6²＝36 的差為 9，因此 7² 最接近。"),
    ("√10 取到小數點後第一位約為何？", ["3.0", "3.1", "3.2", "3.3"], "C", "3.1²＝9.61、3.2²＝10.24，√10 約為 3.162，四捨五入到十分位為 3.2。"),
    ("若 n 為整數且 5＜√n＜6，則 n 可能的最小值為何？", ["24", "25", "26", "36"], "C", "兩邊平方得 25＜n＜36；最小整數 n 為 26。"),
    ("使用計算機將 √2 取到小數點後三位，何者合理？", ["1.141", "1.414", "1.424", "2.414"], "B", "√2 約為 1.414213，取到小數點後三位為 1.414。"),
    ("一個正方形面積為 30 平方公分，則其邊長 √30 約為多少公分（取到十分位）？", ["4.5", "5.0", "5.5", "6.0"], "C", "5.4²＝29.16、5.5²＝30.25，√30 約為 5.477，取到十分位為 5.5。"),
    ("比較 √63 與 8 的大小，何者正確？", ["√63＜8", "√63＝8", "√63＞8", "無法比較"], "A", "63＜64＝8²，且兩者皆為非負數，所以 √63＜8。"),
    ("若要以十分位估計 √18，已知 4.2²＝17.64、4.3²＝18.49，則估計值為何？", ["4.1", "4.2", "4.3", "4.4"], "B", "√18 約為 4.243，與 4.2 的差較小，取到十分位為 4.2。"),
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
        "id": f"question-math-performance-n-iv-6-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考平方根夾逼、估值、四捨五入、平方數比較與正方形邊長題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "十分逼近與計算機估平方根單元實質改寫；已重新以平方值核對夾逼、估值、四捨五入、範圍與幾何情境答案，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-n-iv-6-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} square-root approximation questions")
