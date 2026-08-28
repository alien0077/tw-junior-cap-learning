"""以公開考題能力方向獨立改寫 g-Ⅳ-2 直線與聯立解幾何題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-g-iv-2"
KG_ID = "kg-math-performance-g-iv-2"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("通過點 (2,5) 且斜率為 3 的直線方程式為何？", ["y＝3x－1", "y＝3x＋1", "y＝2x＋3", "y＝5x－3"], "A", "點斜式 y－5＝3(x－2)，整理得 y＝3x－1。"),
    ("解聯立方程式 x＋y＝7、2x－y＝5，則 (x,y) 為何？", ["(2,5)", "(3,4)", "(4,3)", "(5,2)"], "C", "兩式相加得 3x＝12，所以 x＝4；代回 x＋y＝7 得 y＝3，解為 (4,3)。"),
    ("兩直線 y＝2x＋1 與 y＝－x＋7 的交點為何？", ["(1,3)", "(2,5)", "(3,7)", "(4,9)"], "B", "令兩式相等：2x＋1＝－x＋7，得 x＝2；代回得 y＝5，所以交點為 (2,5)。"),
    ("下列哪一組二元一次方程式沒有解？", ["x＋y＝4 與 x－y＝2", "2x－y＝3 與 4x－2y＝8", "x＝1 與 y＝2", "3x＋y＝5 與 3x－y＝1"], "B", "第二組左式第二式是第一式左邊的 2 倍，但右邊 8 不等於 3 的 2 倍 6，代表兩條平行且不重合的直線，沒有解。"),
    ("直線 x/3＋y/2＝1 與坐標軸圍成的三角形面積為何？", ["3 平方單位", "5 平方單位", "6 平方單位", "12 平方單位"], "A", "x 軸截距為 3、y 軸截距為 2，面積＝1/2×3×2＝3 平方單位。"),
    ("若點 (2,1) 是聯立方程式 3x＋y＝7、x－y＝1 的解，則下列判斷為何？", ["正確，兩式代入都成立", "錯誤，只有第一式成立", "錯誤，只有第二式成立", "錯誤，兩式都不成立"], "A", "代入第一式 3×2＋1＝7，第二式 2－1＝1，兩式都成立，所以判斷正確。"),
    ("某展覽成人票 x 張、學生票 y 張共 8 張，票價分別 120 元與 80 元，總收入 800 元。成人票與學生票各幾張？", ["成人 2 張、學生 6 張", "成人 4 張、學生 4 張", "成人 6 張、學生 2 張", "成人 8 張、學生 0 張"], "B", "由 x＋y＝8、120x＋80y＝800。第二式除以 40 得 3x＋2y＝20；與 2x＋2y＝16 相減得 x＝4，故 y＝4。"),
    ("若兩條直線的方程式聯立後唯一解為 (－1,4)，其圖形關係為何？", ["兩直線平行", "兩直線重合", "兩直線相交於 (－1,4)", "其中一條一定是坐標軸"], "C", "聯立方程式的唯一解代表兩條直線恰有一個共同點，亦即相交於 (－1,4)。"),
    ("直線 2x＋3y＝12 的 y 軸截距為何？", ["2", "3", "4", "6"], "C", "在 y 軸上 x＝0，得 3y＝12，所以 y＝4，截距點為 (0,4)。"),
    ("若兩直線 y＝ax＋2 與 y＝4x－1 平行，則 a 為何？", ["－4", "－1", "2", "4"], "D", "非垂直平行直線的斜率相同；第一條斜率為 a，第二條斜率為 4，因此 a＝4。"),
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
        "id": f"question-math-performance-g-iv-2-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考二元一次直線、聯立方程交點、幾何意義、截距與情境題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "二元一次直線與聯立解幾何單元實質改寫；已重新計算直線式、交點、聯立解、無解、截距與票券情境，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-g-iv-2-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} line-system geometry questions")
