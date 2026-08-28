"""以公開考題能力方向獨立改寫坐標幾何主題題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-g"
KG_ID = "kg-math-performance-g"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("點 P(－3,4) 位於坐標平面的哪一個象限？", ["第一象限", "第二象限", "第三象限", "第四象限"], "B", "x<0 且 y>0，符合第二象限的條件。"),
    ("坐標平面上 A(1,2)、B(5,5) 兩點的距離為何？", ["4", "5", "6", "7"], "B", "距離為 √[(5－1)²＋(5－2)²]＝√(16＋9)＝√25＝5。"),
    ("線段端點為 (2,－1) 與 (6,7)，其中點坐標為何？", ["(3,3)", "(4,3)", "(4,4)", "(8,6)"], "B", "中點為 ((2＋6)/2,(－1＋7)/2)＝(4,3)。"),
    ("通過點 (－1,2) 與 (3,10) 的直線斜率為何？", ["1", "2", "3", "4"], "B", "斜率 m＝(10－2)/(3－(－1))＝8/4＝2。"),
    ("直線 y＝－x＋4 與 y 軸的交點坐標為何？", ["(4,0)", "(0,4)", "(－4,0)", "(0,－4)"], "B", "與 y 軸相交時 x＝0，代入得 y＝4，所以交點為 (0,4)。"),
    ("點 (3,－2) 對 x 軸作鏡射後的坐標為何？", ["(－3,－2)", "(3,2)", "(－3,2)", "(2,3)"], "B", "對 x 軸鏡射時 x 坐標不變、y 坐標變號，因此 (3,－2) 變為 (3,2)。"),
    ("點 (3,5) 是否在直線 y＝2x－1 上？", ["是，因為 5＝2×3－1", "是，因為 3＝2×5－1", "否，因為 5≠2×3－1", "否，因為 3≠2×5－1"], "A", "將 x＝3 代入右式：2×3－1＝5，與 y＝5 相等，所以點在直線上。"),
    ("三角形三頂點為 (0,0)、(4,0)、(0,3)，其面積為何？", ["5 平方單位", "6 平方單位", "7 平方單位", "12 平方單位"], "B", "以坐標軸上的兩邊為底與高，面積＝1/2×4×3＝6 平方單位。"),
    ("直線 y＝3x＋1 與下列哪一條直線平行？", ["y＝－3x＋1", "y＝3x－5", "y＝(1/3)x＋1", "y＝－(1/3)x－5"], "B", "平行直線斜率相同；原直線斜率為 3，y＝3x－5 的斜率也是 3。"),
    ("若圓的圓心為 (－2,3)，半徑為 4，則下列哪一點一定在此圓上？", ["(－2,7)", "(2,3)", "(－2,8)", "(0,6)"], "A", "圓心到 (－2,7) 的距離為 |7－3|＝4，等於半徑，因此該點在圓上。"),
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
        "id": f"question-math-performance-g-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考坐標、象限、距離、中點、斜率、截距、對稱、面積與圓題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "坐標幾何主題實質改寫；已重新計算象限、距離、中點、斜率、截距、鏡射、直線、三角形面積、平行線與圓，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-g-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} coordinate-geometry questions")
