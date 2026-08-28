"""以公開考題能力方向獨立改寫 g-Ⅳ-1 直角坐標點與距離題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-g-iv-1"
KG_ID = "kg-math-performance-g-iv-1"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("點 P(－4,3) 位於哪一個象限？", ["第一象限", "第二象限", "第三象限", "第四象限"], "B", "x 坐標為負、y 坐標為正，所以 P 位於第二象限。"),
    ("下列哪一個點位於 x 軸上？", ["(0,－5)", "(5,0)", "(3,2)", "(－2,4)"], "B", "x 軸上所有點的 y 坐標都是 0，因此 (5,0) 位於 x 軸上。"),
    ("A(2,－1) 與 B(8,－1) 的距離為何？", ["5", "6", "7", "8"], "B", "兩點 y 坐標相同，是水平線段，距離為 |8－2|＝6。"),
    ("C(3,2) 與 D(3,9) 的距離為何？", ["6", "7", "8", "11"], "B", "兩點 x 坐標相同，是垂直線段，距離為 |9－2|＝7。"),
    ("坐標平面上 A(1,1)、B(4,5) 的距離為何？", ["4", "5", "6", "7"], "B", "AB＝√[(4－1)²＋(5－1)²]＝√(9＋16)＝5。"),
    ("線段端點為 (－2,4) 與 (6,－2)，其中點坐標為何？", ["(2,1)", "(4,2)", "(－4,6)", "(8,－6)"], "A", "中點為 ((－2＋6)/2,(4－2)/2)＝(2,1)。"),
    ("在 x 軸上有一點 Q，且 Q 到 A(1,2)、B(5,2) 的距離相等，則 Q 的坐標為何？", ["(2,0)", "(3,0)", "(4,0)", "(5,0)"], "B", "A、B 的中垂線為 x＝3；與 x 軸 y＝0 相交於 Q(3,0)，故兩段距離相等。"),
    ("矩形四頂點為 (0,0)、(5,0)、(5,3)、(0,3)，其面積為何？", ["8 平方單位", "15 平方單位", "16 平方單位", "30 平方單位"], "B", "矩形的長為 5、寬為 3，面積＝5×3＝15 平方單位。"),
    ("點 (－3,4) 對 y 軸鏡射後的坐標為何？", ["(3,4)", "(－3,－4)", "(3,－4)", "(4,－3)"], "A", "對 y 軸鏡射時 y 坐標不變、x 坐標變號，所以得到 (3,4)。"),
    ("若點 R(2,y) 與 S(2,－3) 的距離為 8，且 R 在 S 的上方，則 y 為何？", ["3", "5", "－5", "11"], "B", "兩點同 x 坐標且 R 在上方，所以 y－(－3)＝8，解得 y＝5。"),
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
        "id": f"question-math-performance-g-iv-1-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考直角坐標點、象限、坐標軸、距離、中點、對稱與坐標情境題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "直角坐標點與距離單元實質改寫；已重新計算象限、坐標軸、水平／垂直距離、兩點距離、中點、對稱與幾何情境答案，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-g-iv-1-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} coordinate-point questions")
