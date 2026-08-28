"""以公開數學試題的資料判讀方向，獨立替換 D-7-1 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-d-7-1.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-d-7-1"
KNOWLEDGE = "kg-math-content-d-7-1"

ITEMS = [
    ("某社團一週借閱量如下：週一 12 本、週二 18 本、週三 15 本、週四 9 本。哪一天借閱量最多？", ["週二", "週一", "週三", "週四"], "A", "四個數值中 18 最大，因此週二借閱量最多。"),
    ("根據「週一 12 本、週二 18 本、週三 15 本、週四 9 本」的資料，四天總借閱量為何？", ["54 本", "45 本", "48 本", "60 本"], "A", "總量為 12＋18＋15＋9＝54 本。"),
    ("根據「週一 12 本、週二 18 本」的資料，週二比週一多借閱幾本？", ["6 本", "5 本", "30 本", "差 2 倍"], "A", "差量為 18－12＝6 本。"),
    ("資料 12、18、15、9 的平均數為何？", ["13.5", "12", "15", "54"], "A", "總和 54 除以 4 個資料值，平均數為 13.5。"),
    ("長條圖縱軸每一格代表 5 人，某柱高為 7 格，代表多少人？", ["35 人", "12 人", "30 人", "40 人"], "A", "每格 5 人，7 格就是 5×7＝35 人。"),
    ("折線圖顯示週一 20 件、週二 16 件、週三 24 件，週二到週三增加幾件？", ["8 件", "4 件", "40 件", "增加 50%"], "A", "增加量為 24－16＝8 件。"),
    ("四天總借閱量為 54 本，其中週二 18 本，週二占總量的幾分之幾？", ["1/3", "1/2", "1/4", "2/3"], "A", "比例為 18/54，約分後為 1/3。"),
    ("某問卷共有 50 人，圓餅圖顯示選擇甲占 40%，選擇甲有幾人？", ["20 人", "10 人", "25 人", "40 人"], "A", "50×40%＝50×0.4＝20 人。"),
    ("閱讀統計圖表時，哪一項最能避免誤判？", ["先確認標題、單位與坐標軸刻度，再比較數值", "只比較柱子的外觀高度", "忽略坐標軸是否從 0 開始", "只看最大的一根柱子就下結論"], "A", "標題、單位與刻度決定資料意義，必須先核對才能正確解讀。"),
    ("四筆資料排序後為 9、12、15、18，其中位數為何？", ["13.5", "12", "15", "54"], "A", "偶數筆資料的中位數是中間兩數平均：(12＋15)÷2＝13.5。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-d-7-1-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究統計圖表讀值、刻度、比例、平均數與中位數能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 statistical-chart questions")


if __name__ == "__main__":
    main()
