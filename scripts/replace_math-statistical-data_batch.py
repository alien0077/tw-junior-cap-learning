"""以公開數學試題的資料分析方向，獨立替換 D-7-2 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-d-7-2.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-d-7-2"
KNOWLEDGE = "kg-math-content-d-7-2"

ITEMS = [
    ("資料 4、6、8、10 的平均數為何？", ["7", "6", "8", "28"], "A", "總和為 28，共 4 筆資料，平均數為 28÷4＝7。"),
    ("資料 3、5、7、9、12 的中位數為何？", ["7", "5", "9", "12"], "A", "資料已由小到大排列，中間的第三筆 7 就是中位數。"),
    ("資料 2、4、4、5、7、4 的眾數為何？", ["4", "2", "5", "7"], "A", "4 出現 3 次，比其他數值都多，因此眾數為 4。"),
    ("資料 12、8、15、10 的全距為何？", ["7", "5", "8", "23"], "A", "全距為最大值減最小值：15－8＝7。"),
    ("資料 6、8、10、12 的平均數為何？", ["9", "8", "10", "36"], "A", "總和為 36，除以 4 得平均數 9。"),
    ("一組資料的每個數值都加上 3，原平均數為 10，新的平均數為何？", ["13", "10", "30", "7"], "A", "每筆資料都增加 3，平均數也增加 3，因此新平均數為 13。"),
    ("資料 4、7、9、12 的全距為 8。若將最大值 12 改為 10，新全距為何？", ["6", "8", "3", "10"], "A", "新資料最大值 10、最小值 4，全距為 10－4＝6。"),
    ("5 筆資料的平均數為 10，其中 4 筆總和為 34，剩下的一筆是多少？", ["16", "14", "50", "6"], "A", "5 筆總和為 5×10＝50，剩下一筆為 50－34＝16。"),
    ("資料 3、5、7、9 的平均數與中位數各為何？", ["平均數 6，中位數 6", "平均數 6，中位數 5", "平均數 7，中位數 6", "平均數 24，中位數 6"], "A", "平均數為 24÷4＝6，中位數為中間兩數 5 與 7 的平均，也是 6。"),
    ("關於平均數、中位數與眾數的敘述，下列何者正確？", ["眾數是出現次數最多的數值", "平均數一定是資料中的某一筆", "中位數一定是最大值與最小值的平均", "每組資料只能有一個眾數"], "A", "眾數的定義就是出現次數最多的數值；其他敘述並非一般必然成立。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-d-7-2-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        rotated = options[shift:] + options[:shift]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + j), "text": value} for j, value in enumerate(rotated)]
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["knowledgeIds"] = [KNOWLEDGE]
        data["lessonId"] = LESSON
        data["difficulty"] = "medium"
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究平均數、中位數、眾數、全距與資料變動能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 statistical-data questions")


if __name__ == "__main__":
    main()
