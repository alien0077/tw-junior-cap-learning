"""以公開數學試題的資料整理與分布分析方向，獨立替換 D-8-1 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-d-8-1.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-d-8-1"
KNOWLEDGE = "kg-math-content-d-8-1"

ITEMS = [
    ("五位同學分數為 60、70、70、80、90，分數 70 的次數為何？", ["2 次", "1 次", "3 次", "4 次"], "A", "70 在資料中出現兩次，因此次數為 2 次。"),
    ("某類別有 8 筆資料，全部資料共 20 筆，該類別的相對次數為何？", ["40%", "20%", "60%", "80%"], "A", "相對次數為 8÷20＝0.4＝40%。"),
    ("一份次數分配表中，四類次數依序為 5、12、8、5，資料總數為何？", ["30", "25", "35", "40"], "A", "資料總數為各類次數相加：5＋12＋8＋5＝30。"),
    ("資料值 10 出現 2 次、20 出現 3 次，這 5 筆資料的平均數為何？", ["16", "15", "18", "30"], "A", "加權總和為 10×2＋20×3＝80，再除以 5 得 16。"),
    ("資料值 2 出現 1 次、4 出現 3 次、6 出現 1 次，其中位數為何？", ["4", "2", "6", "12"], "A", "排序後為 2、4、4、4、6，中間第三筆是 4。"),
    ("某次數分配表中，數值 1、2、3、4 的次數分別為 2、5、3、1，眾數為何？", ["2", "1", "3", "4"], "A", "數值 2 的次數 5 最大，因此眾數為 2。"),
    ("某分組資料前兩組的次數分別為 4 與 6，前兩組的累積次數為何？", ["10", "2", "6", "24"], "A", "累積次數是截至該組的次數總和：4＋6＝10。"),
    ("長條圖四類人數為 6、9、5、10，若要表示總人數，應為多少？", ["30 人", "24 人", "25 人", "40 人"], "A", "四類人數相加為 6＋9＋5＋10＝30 人。"),
    ("某類別占全部資料的 25%，該類別有 5 筆，則全部資料共有幾筆？", ["20 筆", "10 筆", "25 筆", "125 筆"], "A", "5÷總數＝25%＝1/4，因此總數為 5×4＝20 筆。"),
    ("若要比較不同類別的出現次數，哪一種圖表最直接？", ["長條圖", "只列一個平均數", "只畫一條數線", "只寫文字結論"], "A", "長條圖以柱高直接比較各類別次數，適合呈現類別分布。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-d-8-1-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究次數分配、相對次數、累積次數與統計量能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 statistical-processing questions")


if __name__ == "__main__":
    main()
