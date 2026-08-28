"""以公開考題能力方向獨立改寫 n-Ⅳ-2 負數與四則運算題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-n-iv-2"
KG_ID = "kg-math-performance-n-iv-2"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("計算 (－7)＋12 的值為何？", ["－19", "－5", "5", "19"], "C", "在數線上從－7 向右 12 格，或直接計算－7＋12，結果為 5。"),
    ("計算 (－3)－8 的值為何？", ["－11", "－5", "5", "11"], "A", "減去正數 8 等於向左移 8 格，所以 (－3)－8＝－11。"),
    ("計算 (－4)×(－6) 的值為何？", ["－24", "－10", "10", "24"], "D", "負數乘負數得正數，且 4×6＝24，所以結果為 24。"),
    ("計算 45÷(－9) 的值為何？", ["－9", "－5", "5", "9"], "B", "正數除以負數為負數，45÷9＝5，因此結果為－5。"),
    ("下列哪一個數較大？", ["－8", "－3", "兩者相等", "無法比較"], "B", "在數線上越右邊的數越大；－3 位於－8 的右側，所以－3 較大。"),
    ("某地清晨氣溫為－2°C，中午上升 5°C，中午氣溫為何？", ["－7°C", "－3°C", "3°C", "7°C"], "C", "氣溫變化為 (－2)＋5＝3，因此中午為 3°C。"),
    ("數值 |－9| 的值為何？", ["－9", "0", "9", "18"], "C", "絕對值表示數到 0 的距離，|－9|＝9。"),
    ("計算 (－2)³ 的值為何？", ["－8", "－6", "6", "8"], "A", "(－2)³＝(－2)×(－2)×(－2)＝4×(－2)＝－8。"),
    ("將 －5、3、－1、0 由小到大排列，何者正確？", ["3、0、－1、－5", "－5、－1、0、3", "－1、－5、0、3", "0、－1、－5、3"], "B", "數線上由左到右遞增，因此順序為－5、－1、0、3。"),
    ("計算 18－[(－4)＋7] 的值為何？", ["7", "11", "15", "29"], "C", "先算括號：(－4)＋7＝3，再算 18－3＝15。"),
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
        "id": f"question-math-performance-n-iv-2-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考負數數線、整數四則、絕對值、排序與溫度情境題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "負數數線與四則運算單元實質改寫；已重新計算整數加減乘除、絕對值、數線比較、排序與溫度情境，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-n-iv-2-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} negative-arithmetic questions")
