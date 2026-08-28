"""以公開考題能力方向獨立改寫 f-Ⅳ-2 二次函數圖形題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-f-iv-2"
KG_ID = "kg-math-performance-f-iv-2"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("二次函數 y＝2x²－8x＋3 的對稱軸方程式為何？", ["x＝2", "x＝－2", "x＝4", "x＝－4"], "A", "將 y＝2x²－8x＋3 與 ax²＋bx＋c 比較，對稱軸為 x＝－b/(2a)＝8/4＝2。"),
    ("函數 y＝(x－3)²－4 的頂點座標為何？", ["(－3,－4)", "(3,－4)", "(3,4)", "(－3,4)"], "B", "頂點式 y＝(x－h)²＋k 的頂點是 (h,k)，所以 h＝3、k＝－4。"),
    ("若 y＝－x²＋6x－5，則此函數的最大值為何？", ["－5", "3", "4", "5"], "C", "配方得 y＝－(x－3)²＋4；因為平方項不大於 0，最大值為 4。"),
    ("拋物線 y＝x²＋2x－3 與 x 軸的交點為何？", ["(－3,0) 與 (1,0)", "(－1,0) 與 (3,0)", "(－3,0) 與 (－1,0)", "(1,0) 與 (3,0)"], "A", "令 y＝0，得 x²＋2x－3＝(x＋3)(x－1)＝0，所以 x＝－3 或 1，交點為 (－3,0) 與 (1,0)。"),
    ("將 y＝x² 的圖形向右平移 1 單位，再向上平移 2 單位，所得函數為何？", ["y＝(x＋1)²－2", "y＝(x－1)²＋2", "y＝(x＋1)²＋2", "y＝(x－1)²－2"], "B", "向右 1 單位把 x 改為 x－1，向上 2 單位在外面加 2，因此為 y＝(x－1)²＋2。"),
    ("函數 y＝2(x＋1)²－3 的開口方向與頂點為何？", ["向下，(1,3)", "向上，(1,－3)", "向下，(－1,3)", "向上，(－1,－3)"], "D", "二次項係數 2>0，開口向上；由頂點式可得頂點為 (－1,－3)。"),
    ("若二次函數 y＝ax² 通過點 (2,12)，則 a 為何？", ["2", "3", "4", "6"], "B", "代入 (2,12)：12＝a·2²＝4a，所以 a＝3。"),
    ("某二次函數的頂點為 (2,－1)，且圖形開口向上。下列哪一項必定正確？", ["其最小值為－1", "其最大值為－1", "其對稱軸為 x＝－2", "其與 x 軸沒有交點"], "A", "開口向上時頂點是最低點，因此函數最小值為頂點的 y 座標－1；其他敘述不一定成立或方向相反。"),
    ("物體高度以 h＝－t²＋10t 表示（h 為公尺，t 為秒）。物體達到的最大高度為何？", ["10 公尺", "20 公尺", "25 公尺", "100 公尺"], "C", "配方得 h＝－(t－5)²＋25，因此在 t＝5 秒時達到最大高度 25 公尺。"),
    ("函數 y＝(x－2)²＋5 的值域為何？", ["y≤5", "y≥5", "y≤2", "y≥2"], "B", "因為 (x－2)²≥0，所以 y＝(x－2)²＋5≥5，值域為 y≥5。"),
]

def rotate_options(options, answer_letter):
    answer_index = ord(answer_letter) - ord("A")
    shift = (4 - answer_index) % 4
    rotated = options[shift:] + options[:shift]
    ids = ["A", "B", "C", "D"]
    return [{"id": ident, "text": text} for ident, text in zip(ids, rotated)]

def make_question(index, prompt, options, answer_letter, explanation):
    original_index = ord(answer_letter) - ord("A")
    rotated = rotate_options(options, answer_letter)
    answer_id = next(item["id"] for item in rotated if item["text"] == options[original_index])
    return {
        "id": f"question-math-performance-f-iv-2-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考二次函數圖形、頂點、對稱軸、截距、平移與情境建模題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "二次函數圖形單元實質改寫；已重新計算頂點、對稱軸、開口、截距、平移、值域與情境最大值，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-f-iv-2-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} quadratic-graph questions")
