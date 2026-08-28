"""以公開考題能力方向獨立改寫 n-Ⅳ-4 比例題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-n-iv-4"
KG_ID = "kg-math-performance-n-iv-4"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("比 12：18 化成最簡整數比為何？", ["1：2", "2：3", "3：4", "6：9"], "B", "12 與 18 的最大公因數為 6，同除以 6 得最簡比 2：3。"),
    ("將 450 元依 2：3 分給甲、乙，乙分得多少元？", ["180 元", "225 元", "270 元", "300 元"], "C", "總份數為 2＋3＝5，乙得 450×3/5＝270 元。"),
    ("若 y 與 x 成正比，且 x＝3 時 y＝12，則 x＝7 時 y 為何？", ["21", "24", "28", "36"], "C", "正比係數 k＝12/3＝4，所以 x＝7 時 y＝4×7＝28。"),
    ("若 x 與 y 成反比，且 xy＝48，當 x＝6 時 y 為何？", ["6", "8", "12", "288"], "B", "反比乘積保持 48，因此 y＝48÷6＝8。"),
    ("若 A：B＝2：3 且 B：C＝4：5，則 A：B：C 為何？", ["2：3：5", "8：12：15", "8：3：5", "2：4：5"], "B", "讓兩個比的 B 同為 12：A：B＝8：12，B：C＝12：15，所以 A：B：C＝8：12：15。"),
    ("地圖比例尺為 1：50000，圖上 3 公分代表實際距離多少公里？", ["0.15 公里", "1.5 公里", "15 公里", "150 公里"], "B", "實際為 3×50000＝150000 公分＝1.5 公里。"),
    ("一份食譜供 4 人使用 3 杯米，若按比例供 10 人使用，需要幾杯米？", ["6 杯", "7.5 杯", "8 杯", "10 杯"], "B", "每人 3/4 杯，10 人需要 10×3/4＝7.5 杯。"),
    ("固定距離下，車速 60 公里／小時需 3 小時；若車速提高到 90 公里／小時，需幾小時？", ["1.5 小時", "2 小時", "3.5 小時", "4.5 小時"], "B", "固定距離為 60×3＝180 公里，所需時間為 180÷90＝2 小時，速度與時間成反比。"),
    ("某班男生與女生人數比為 5：7，全班共 36 人，男生有幾人？", ["12 人", "15 人", "20 人", "21 人"], "B", "總份數 5＋7＝12，每份 36÷12＝3 人，男生 5×3＝15 人。"),
    ("若 x/8＝15/20，則 x 為何？", ["4", "6", "8", "10"], "B", "15/20＝3/4，所以 x/8＝3/4，x＝8×3/4＝6。"),
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
        "id": f"question-math-performance-n-iv-4-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考比、比例、正比、反比、連比、比例尺與生活情境題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "比比例正反比與連比單元實質改寫；已重新計算最簡比、比例分配、正反比、連比、比例尺、單位換算與情境答案，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-n-iv-4-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} ratio-proportion questions")
