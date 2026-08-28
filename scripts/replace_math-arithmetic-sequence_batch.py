"""以公開數學試題的數列與規律應用方向，獨立替換 N-8-4 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-8-4.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-8-4"
KNOWLEDGE = "kg-math-content-n-8-4"

ITEMS = [
    ("等差數列 4、9、14、19、… 的公差為何？", ["5", "4", "9", "23"], "A", "相鄰兩項相減：9－4＝5，因此公差為 5。"),
    ("等差數列首項為 7、公差為－2，則第 6 項為何？", ["－3", "－5", "3", "17"], "A", "第 6 項為 7＋(6－1)×(－2)＝7－10＝－3。"),
    ("等差數列首項為 3、公差為 4，第 n 項可表示為何？", ["4n－1", "3n＋4", "4n＋3", "3n－1"], "A", "aₙ＝3＋(n－1)×4＝4n－1。"),
    ("等差數列中 a₄＝11、a₉＝26，則公差為何？", ["3", "5", "4", "15"], "A", "五個間隔增加 26－11＝15，所以公差為 15÷5＝3。"),
    ("等差數列 6、10、14、18、… 的第 12 項為何？", ["50", "48", "54", "46"], "A", "第 12 項為 6＋11×4＝50。"),
    ("等差數列公差為 4，且第 5 項為 23，則首項為何？", ["7", "3", "11", "19"], "A", "a₅＝a₁＋4×4，所以 a₁＝23－16＝7。"),
    ("在 8 與 20 之間插入 3 個數，使其成為等差數列。中間的數是多少？", ["14", "11", "12", "16"], "A", "共有 4 個等差間隔，公差為 (20－8)÷4＝3，中間數為 8＋2×3＝14。"),
    ("座位第一排有 12 個，之後每排比前一排多 3 個。第 8 排有幾個座位？", ["33 個", "30 個", "36 個", "24 個"], "A", "這是首項 12、公差 3 的等差數列，第 8 項為 12＋7×3＝33。"),
    ("小安第一個月存 100 元，之後每月比前月多存 50 元。第 6 個月存多少元？", ["350 元", "300 元", "400 元", "600 元"], "A", "第 6 個月為 100＋5×50＝350 元。"),
    ("下列哪一個數列是等差數列？", ["12、8、4、0、…", "1、2、4、8、…", "2、5、10、17、…", "3、6、12、24、…"], "A", "第一個數列相鄰兩項差都為－4，符合等差數列。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-8-4-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究等差數列公差、通項、指定項與生活情境能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 arithmetic-sequence questions")


if __name__ == "__main__":
    main()
