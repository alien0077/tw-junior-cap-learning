"""以公開考題能力方向獨立改寫 f-Ⅳ-3 二次函數極值題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-f-iv-3"
KG_ID = "kg-math-performance-f-iv-3"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("函數 y＝－2(x－1)²＋7 的頂點與最大值為何？", ["頂點 (1,7)，最大值 7", "頂點 (－1,7)，最大值 7", "頂點 (1,－7)，最大值 －7", "頂點 (－1,－7)，最大值 －7"], "A", "由頂點式可知頂點為 (1,7)；因二次項係數為負，開口向下，所以最大值是 7。"),
    ("二次函數 y＝3x²－12x＋5 的對稱軸為何？", ["x＝－2", "x＝2", "x＝4", "x＝－4"], "B", "對稱軸 x＝－b/(2a)＝12/6＝2。"),
    ("函數 y＝x²－4x＋1 的最小值為何？", ["－4", "－3", "1", "3"], "B", "配方得 y＝(x－2)²－3；平方項最小為 0，因此最小值為－3。"),
    ("函數 y＝－x²－4x＋6 的最大值為何？", ["6", "8", "10", "12"], "C", "配方得 y＝－(x＋2)²＋10；開口向下，故最大值為 10。"),
    ("函數 y＝2(x＋3)²－8 的值域為何？", ["y≤－8", "y≥－8", "y≤8", "y≥8"], "B", "因 2(x＋3)²≥0，所以 y≥－8；頂點 y 座標－8 是最小值。"),
    ("拋物線 y＝－(x－4)²＋2 在 x＝0 時的函數值為何？", ["－18", "－14", "2", "18"], "B", "代入 x＝0：y＝－(0－4)²＋2＝－16＋2＝－14。"),
    ("一個長方形周長為 20 公分，若長為 x 公分、寬為 (10－x) 公分，則面積的最大值為何？", ["20 平方公分", "24 平方公分", "25 平方公分", "50 平方公分"], "C", "面積 A＝x(10－x)＝－(x－5)²＋25，因此 x＝5 時面積最大為 25 平方公分。"),
    ("若二次函數 y＝a(x－2)²＋3 通過點 (4,11)，則 a 為何？", ["1", "2", "3", "4"], "B", "代入 (4,11)：11＝a(4－2)²＋3＝4a＋3，所以 a＝2。"),
    ("函數 y＝2x²－4x－6 的頂點座標為何？", ["(1,－8)", "(－1,－8)", "(1,8)", "(－1,8)"], "A", "對稱軸 x＝4/4＝1，代入得 y＝2－4－6＝－8，所以頂點為 (1,－8)。"),
    ("若拋物線 y＝－x²＋6x－8 與 x 軸交於兩點，兩交點的 x 坐標為何？", ["1 與 8", "2 與 4", "－2 與－4", "3 與 5"], "B", "令 y＝0，得 x²－6x＋8＝(x－2)(x－4)＝0，所以 x＝2 或 4。"),
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
        "id": f"question-math-performance-f-iv-3-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考二次函數標準式、開口、頂點、極值與情境建模題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "二次函數極值單元實質改寫；已重新計算對稱軸、頂點、最大／最小值、值域與情境面積，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-f-iv-3-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} quadratic-extreme questions")
