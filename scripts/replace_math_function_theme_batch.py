"""以公開考題能力方向獨立改寫函數主題題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-f"
KG_ID = "kg-math-performance-f"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("下列哪一個對應關係可以表示函數？", ["同一個輸入對應到兩個不同輸出", "每個輸入恰對應一個輸出", "有些輸入沒有定義且另有輸入對應兩個輸出", "只要輸出數量比輸入數量多就是函數"], "B", "函數要求每一個定義域中的輸入值，恰好對應一個輸出值；輸出值彼此相同並不違反函數定義。"),
    ("若 f(x)＝2x－3，則 f(－4) 為何？", ["－11", "－5", "5", "11"], "A", "代入 x＝－4：f(－4)＝2(－4)－3＝－8－3＝－11。"),
    ("對應關係 {(1,4),(2,4),(3,7)} 的值域為何？", ["{1,2,3}", "{4,7}", "{1,2,3,4,7}", "{4,4,7}"], "B", "值域是所有輸出值的集合，重複的 4 只列一次，所以值域為 {4,7}。"),
    ("若函數 f 的定義域為 {－2,0,3}，下列哪一個數值不一定屬於定義域？", ["－2", "0", "1", "3"], "C", "定義域只保證包含－2、0、3；1 未列在其中，因此不一定屬於定義域。"),
    ("函數 y＝√(x－2) 的定義域條件為何？", ["x≤2", "x≥2", "x≤－2", "x≥－2"], "B", "根號內必須大於或等於 0，所以 x－2≥0，解得 x≥2。"),
    ("若 f(x)＝x²－1，則 f(2)＋f(－2) 為何？", ["2", "4", "6", "8"], "C", "f(2)＝3、f(－2)＝3，兩者相加為 6。"),
    ("某校記錄學生每天閱讀時間 x（分鐘）與理解測驗得分 y。若閱讀時間增加時，研究者觀察得分隨之改變，哪一項是較合理的變數設定？", ["x 為應變數、y 為自變數", "x 為自變數、y 為應變數", "x 與 y 都只能是常數", "x 與 y 必須代表同一件事"], "B", "研究中用閱讀時間 x 作為輸入或自變數，觀察測驗得分 y 的變化，因此 y 是應變數。"),
    ("在座標平面上判斷一條曲線是否為函數圖形，通常可使用哪一項方法？", ["水平線測試：每條水平線最多交一次", "垂直線測試：每條垂直線最多交一次", "只看曲線是否經過原點", "只看曲線是否對稱"], "B", "同一個 x 不可對應兩個 y，因此每條垂直線與函數圖形至多交於一點。"),
    ("某停車場收費函數為 C(h)＝40＋20h，其中 h 為停車小時數。停車 3 小時的費用為何？", ["60 元", "80 元", "100 元", "120 元"], "C", "代入 h＝3：C(3)＝40＋20×3＝100 元。"),
    ("若函數 g 的對應表為 g(0)＝5、g(1)＝8、g(2)＝11，符合此規律的式子為何？", ["g(x)＝2x＋5", "g(x)＝3x＋5", "g(x)＝3x＋8", "g(x)＝5x＋3"], "B", "輸出每增加 3，且 g(0)＝5，所以 g(x)＝3x＋5；代入 1、2 也分別得到 8、11。"),
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
        "id": f"question-math-performance-f-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考函數定義、對應、定義域／值域、代值、圖形判斷與生活情境題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "函數主題單元實質改寫；已重新核對函數定義、對應關係、定義域、值域、代值與函數模型，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-f-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} function-theme questions")
