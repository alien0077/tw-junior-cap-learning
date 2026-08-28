"""以公開考題能力方向獨立改寫 n-Ⅳ-7 數列題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-n-iv-7"
KG_ID = "kg-math-performance-n-iv-7"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("等差數列 5、8、11、…… 的第 10 項為何？", ["29", "32", "35", "38"], "B", "首項為 5、公差為 3，第 10 項＝5＋(10－1)×3＝32。"),
    ("等差數列 21、16、11、…… 的公差為何？", ["－10", "－5", "5", "10"], "B", "相鄰兩項相減：16－21＝－5，因此公差為－5。"),
    ("在 7 與 19 之間插入一個數，使三數成等差數列，該數為何？", ["10", "12", "13", "14"], "C", "等差中項為兩端平均數：(7＋19)/2＝13。"),
    ("等差數列 2、5、8、…… 的前 10 項和為何？", ["145", "150", "155", "160"], "C", "第 10 項為 2＋9×3＝29，前 10 項和＝(2＋29)×10/2＝155。"),
    ("等比數列 3、6、12、…… 的第 5 項為何？", ["24", "36", "48", "96"], "C", "首項 3、公比 2，第 5 項＝3×2⁴＝48。"),
    ("等比數列 81、27、9、…… 的公比為何？", ["1/9", "1/3", "3", "9"], "B", "公比為相鄰兩項的比：27/81＝1/3，且 9/27 也等於 1/3。"),
    ("計算等比級數 2＋4＋8＋16 的和，結果為何？", ["24", "28", "30", "32"], "C", "逐項相加：2＋4＋8＋16＝30。"),
    ("某人每月存款依序為 100、150、200、…… 元，若每月增加固定金額，第 6 個月存款為何？", ["300 元", "350 元", "400 元", "450 元"], "B", "這是首項 100、公差 50 的等差數列，第 6 項＝100＋5×50＝350 元。"),
    ("下列哪一個數列是等比數列？", ["2、6、18、54", "1、3、6、10", "4、7、10、13", "5、8、12、17"], "A", "第一組相鄰兩項的比都為 3，符合固定公比；其餘各組的差或比不固定。"),
    ("等差數列首項為 4、公差為－2，則第 7 項為何？", ["－10", "－8", "8", "10"], "B", "第 7 項＝4＋(7－1)×(－2)＝4－12＝－8。"),
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
        "id": f"question-math-performance-n-iv-7-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考等差數列、等比數列、公差、公比、通項、等差中項、級數和與生活情境題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "數列等差等比單元實質改寫；已重新計算公差、公比、項值、等差中項、級數和與生活情境答案，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-n-iv-7-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} sequence questions")
