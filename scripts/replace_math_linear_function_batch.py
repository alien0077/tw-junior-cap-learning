"""以公開考題能力方向獨立改寫 f-Ⅳ-1 常數與一次函數題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-f-iv-1"
KG_ID = "kg-math-performance-f-iv-1"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("若一次函數 f(x)＝3x＋2，則 f(4) 為何？", ["10", "12", "14", "16"], "C", "將 x＝4 代入：f(4)＝3×4＋2＝14。"),
    ("直線 y＝－2x＋5 的斜率為何？", ["－5", "－2", "2", "5"], "B", "一次函數 y＝mx＋b 的斜率是 x 的係數，因此斜率為－2。"),
    ("下列哪一個關係是常數函數？", ["y＝4", "y＝4x", "y＝x＋4", "y＝x²＋4"], "A", "常數函數的函數值不隨 x 改變；y＝4 對所有 x 都固定為 4。"),
    ("通過點 (1,3) 與 (3,7) 的一次函數，其斜率為何？", ["1", "2", "3", "4"], "B", "斜率 m＝(7－3)/(3－1)＝4/2＝2。"),
    ("直線 y＝2x－6 與 x 軸的交點，其 x 坐標為何？", ["－3", "0", "3", "6"], "C", "與 x 軸相交時 y＝0，故 2x－6＝0，解得 x＝3。"),
    ("某計程車車資為起跳 70 元，每行駛 1 公里加收 15 元。行駛 4 公里時車資為何？", ["85 元", "115 元", "130 元", "145 元"], "C", "車資 y＝70＋15x；代入 x＝4 得 y＝70＋60＝130 元。"),
    ("若一次函數的部分對應表為 x＝0 時 y＝5、x＝2 時 y＝9，則此函數為何？", ["y＝x＋5", "y＝2x＋5", "y＝4x＋5", "y＝2x＋9"], "B", "兩點 (0,5)、(2,9) 的斜率為 (9－5)/2＝2，且 y 截距為 5，所以 y＝2x＋5。"),
    ("常數函數 y＝－3 的圖形是何種直線？", ["通過原點的斜直線", "水平直線 y＝－3", "垂直直線 x＝－3", "拋物線"], "B", "函數值永遠是－3，因此圖形為與 x 軸平行的水平直線 y＝－3。"),
    ("若 y＝－3x＋12，則圖形與 x 軸交點的 x 坐標為何？", ["－4", "0", "3", "4"], "D", "令 y＝0：－3x＋12＝0，移項得 3x＝12，所以 x＝4。"),
    ("正比關係 y＝kx 通過點 (3,12)。當 x＝5 時，y 為何？", ["15", "18", "20", "24"], "C", "由 12＝3k 得 k＝4，因此 x＝5 時 y＝4×5＝20。"),
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
        "id": f"question-math-performance-f-iv-1-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考常數函數、一次函數、斜率、截距、對應表與生活情境題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "常數與一次函數單元實質改寫；已重新計算代值、斜率、截距、函數式、圖形與情境答案，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-f-iv-1-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} linear-function questions")
