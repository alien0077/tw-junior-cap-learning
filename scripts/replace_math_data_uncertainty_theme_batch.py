"""以公開考題能力方向獨立改寫資料與不確定性主題題。"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-d"
KG_ID = "kg-math-performance-d"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"

ITEMS = [
    ("資料 6、8、10、12 的平均數為何？", ["8", "9", "10", "11"], "B", "總和為 6＋8＋10＋12＝36，共 4 筆資料，平均數為 36÷4＝9。"),
    ("資料 3、5、7、9、11 的中位數為何？", ["5", "6", "7", "9"], "C", "資料已由小到大排列，共 5 筆，中間第 3 筆為 7，所以中位數是 7。"),
    ("資料 2、4、4、5、7、4、8 的眾數為何？", ["2", "4", "5", "8"], "B", "4 出現 3 次，比其他數值更頻繁，因此眾數為 4。"),
    ("資料 14、9、21、6、18 的全距為何？", ["12", "15", "18", "27"], "B", "全距＝最大值－最小值＝21－6＝15。"),
    ("兩組資料平均數相同，但甲組的全距比乙組小，表示哪一項較合理？", ["甲組資料較集中", "甲組平均數一定較大", "甲組資料筆數一定較多", "乙組眾數一定較大"], "A", "全距較小表示最大值與最小值的差距較小，通常可判斷甲組的資料分散程度較小、較集中；不能由此推出其他敘述。"),
    ("某次數分配中，數值 1 出現 2 次、數值 3 出現 3 次、數值 5 出現 1 次。這組資料的平均數為何？", ["2", "8/3", "3", "16/3"], "B", "總和為 1×2＋3×3＋5×1＝16，總次數為 6，平均數為 16÷6＝8/3。"),
    ("擲一枚公平骰子一次，出現偶數的機率為何？", ["1/6", "1/3", "1/2", "2/3"], "C", "偶數結果為 2、4、6，共 3 個；樣本空間有 6 個等可能結果，所以機率為 3/6＝1/2。"),
    ("連續擲一枚硬幣兩次，所有可能的結果共有幾種？", ["2 種", "3 種", "4 種", "6 種"], "C", "兩次結果可列為正正、正反、反正、反反，共 2×2＝4 種。"),
    ("某校想知道全校學生最常使用的交通方式，從七年級抽取 80 人填寫問卷。這 80 人在統計上稱為什麼？", ["母體", "樣本", "眾數", "變數值"], "B", "全校學生是研究母體，從中抽取並調查的 80 人是樣本。"),
    ("一張長條圖把縱軸從 90 分開始而非從 0 分開始。比較兩組分數時，最應注意什麼？", ["圖形高度差可能被視覺放大，不能只看柱高下結論", "只要柱子較高，差距就一定超過 50 分", "縱軸起點不影響任何判讀", "應把所有資料改成百分比才可判讀"], "A", "縱軸截斷會放大柱高的視覺差異，判讀時應查看刻度與實際數值，不能只憑柱子高度下結論。"),
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
        "id": f"question-math-performance-d-{index}",
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
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考統計量、次數分配、機率、抽樣與圖表判讀題型；本題使用全新數值、情境、選項與解析，非原題重製。",
            "authoringNote": "資料與不確定性主題實質改寫；已重新計算平均數、中位數、眾數、全距、次數分配、機率與抽樣判讀，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }

for index, item in enumerate(ITEMS, 1):
    path = TARGET / f"question-math-performance-d-{index}.json"
    path.write_text(json.dumps(make_question(index, *item), ensure_ascii=False, indent=2) + "\n")

print(f"replaced {len(ITEMS)} data-uncertainty questions")
