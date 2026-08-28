"""以公開數學試題的函數能力方向，獨立替換 F 領域彙整題。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-f.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-f"
KNOWLEDGE = "kg-math-content-f"

ITEMS = [
    ("若對應規則 f(x)=2x+3，則 f(4) 為何？", ["11", "8", "10", "14"], "A", "將 x＝4 代入，f(4)＝2×4＋3＝11。"),
    ("若 y=3x-2，當 x 增加 1 時，y 增加多少？", ["3", "1", "2", "-2"], "A", "x 的係數 3 是斜率，表示 x 增加 1 時 y 增加 3。"),
    ("直線 y=-2x+5 與 y 軸的交點為何？", ["(0,5)", "(5,0)", "(0,-2)", "(-2,5)"], "A", "與 y 軸相交時 x＝0，代入得 y＝5，所以交點為 (0,5)。"),
    ("若一次函數圖形通過 (1,4) 與 (3,10)，其斜率為何？", ["3", "2", "6", "7"], "A", "斜率為 (10－4)÷(3－1)＝6÷2＝3。"),
    ("下列哪一組有序對可同時滿足 y=2x+1？", ["(2,5)", "(1,4)", "(0,0)", "(3,8)"], "A", "x＝2 時，y＝2×2＋1＝5，因此 (2,5) 符合。"),
    ("若 y=4x-7，當 y=9 時 x 為何？", ["4", "2", "16", "-4"], "A", "由 4x－7＝9 得 4x＝16，所以 x＝4。"),
    ("某計程車車資 y 元由起跳價 70 元及每公里 25 元組成，行駛 x 公里時的函數關係為何？", ["y=25x+70", "y=70x+25", "y=25(x+70)", "y=70-25x"], "A", "每公里費用是 x 的係數，起跳價是常數項，所以 y＝25x＋70。"),
    ("若函數 f(x)=x+6 的反函數為 f⁻¹(x)，則 f⁻¹(10) 為何？", ["4", "10", "16", "-4"], "A", "令 y＝x＋6，交換 x、y 後得 y＝x－6，因此 f⁻¹(10)＝4。"),
    ("在同一座標平面上，直線 y=2x+1 與 y=2x-4 的關係為何？", ["平行且不重合", "相交於原點", "完全重合", "互相垂直"], "A", "兩直線斜率同為 2，但截距不同，故平行且不重合。"),
    ("若函數圖形在 x=0 時 y=6，且 x 每增加 1，y 減少 2，則其函數式為何？", ["y=-2x+6", "y=2x+6", "y=-2x-6", "y=6x-2"], "A", "斜率為 -2，y 截距為 6，因此函數式為 y＝-2x＋6。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-f-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究函數代值、斜率、截距、圖形與情境建模的能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 function domain questions")


if __name__ == "__main__":
    main()
