"""以公開數學試題的等差數列與求和方向，獨立替換 N-8-5 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-8-5.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-8-5"
KNOWLEDGE = "kg-math-content-n-8-5"

ITEMS = [
    ("數列 2、5、8、11、14 的和為何？", ["40", "35", "42", "45"], "A", "直接相加得 2＋5＋8＋11＋14＝40。"),
    ("等差數列首項為 3、公差為 2，前 10 項和為何？", ["120", "110", "130", "100"], "A", "第 10 項為 3＋9×2＝21，和為 10×(3＋21)÷2＝120。"),
    ("1＋2＋3＋…＋20 的和為何？", ["210", "200", "220", "190"], "A", "這是首項 1、末項 20、共 20 項的等差級數，和為 20×(1＋20)÷2＝210。"),
    ("等差數列共有 7 項，首項為 7、末項為 31，總和為何？", ["133", "126", "140", "266"], "A", "首尾平均為 (7＋31)÷2＝19，7 項和為 7×19＝133。"),
    ("前 8 個正奇數 1、3、5、…、15 的和為何？", ["64", "56", "72", "32"], "A", "這是 8 項等差數列，首尾平均為 (1＋15)÷2＝8，和為 8×8＝64。"),
    ("等差數列有 5 項，首項為 4、末項為 20，則這 5 項的和為何？", ["60", "50", "64", "100"], "A", "首尾平均為 12，5 項和為 5×12＝60。"),
    ("座位每排依序有 10、13、16、…、31 個，共 8 排，座位總數為何？", ["164 個", "152 個", "168 個", "176 個"], "A", "這是 8 項等差數列，首尾平均為 (10＋31)÷2＝20.5，總數為 8×20.5＝164。"),
    ("小安連續 6 個月每月存款依序為 200、300、…、700 元，這 6 個月共存多少元？", ["2700 元", "2400 元", "3000 元", "4200 元"], "A", "首尾平均為 (200＋700)÷2＝450，6 個月共 6×450＝2700 元。"),
    ("前 n 個正整數的和為 55，則 n 為何？", ["10", "9", "11", "55"], "A", "n(n＋1)÷2＝55，得 n(n＋1)＝110，正整數解為 n＝10。"),
    ("等差級數前 n 項和的正確公式為何？", ["Sₙ＝n(a₁＋aₙ)÷2", "Sₙ＝a₁＋(n－1)d", "Sₙ＝n(a₁＋aₙ)", "Sₙ＝(a₁＋aₙ)÷2"], "A", "等差級數的和等於項數乘以首尾平均，因此 Sₙ＝n(a₁＋aₙ)÷2。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-8-5-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究等差級數首尾平均、項數、求和公式與生活情境能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 arithmetic-series-sum questions")


if __name__ == "__main__":
    main()
