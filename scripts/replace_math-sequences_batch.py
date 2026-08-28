"""以公開數學試題的規律辨識與數列計算方向，獨立替換 N-8-3 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-8-3.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-8-3"
KNOWLEDGE = "kg-math-content-n-8-3"

ITEMS = [
    ("數列 3、7、11、15、… 的下一項為何？", ["19", "18", "20", "22"], "A", "每一項比前一項多 4，因此下一項為 15＋4＝19。"),
    ("數列 2、4、8、16、… 的第 5 項為何？", ["32", "24", "30", "64"], "A", "每一項是前一項的 2 倍，第 5 項為 16×2＝32。"),
    ("等差數列首項為 5、公差為 3，則第 10 項為何？", ["32", "30", "35", "27"], "A", "第 n 項為 5＋(n－1)×3，所以第 10 項為 5＋27＝32。"),
    ("數列 5、8、11、14、… 的第 n 項可表示為何？", ["3n＋2", "3n－2", "5n＋3", "8n－3"], "A", "首項 5、公差 3，通項為 5＋(n－1)×3＝3n＋2。"),
    ("數列 1、3、5、7、9 的前 5 項和為何？", ["25", "20", "24", "30"], "A", "逐項相加：1＋3＋5＋7＋9＝25。"),
    ("數列首項 a₁＝4，且 aₙ₊₁＝aₙ＋6，則 a₄ 為何？", ["22", "16", "24", "28"], "A", "依遞推關係，a₂＝10、a₃＝16、a₄＝22。"),
    ("數列 1、4、9、16、… 的第 6 項為何？", ["36", "25", "30", "49"], "A", "各項依序為 1²、2²、3²、4²，因此第 6 項為 6²＝36。"),
    ("數列 2、5、10、17、26、… 的下一項為何？", ["37", "35", "36", "39"], "A", "相鄰差為 3、5、7、9，下一個差為 11，因此 26＋11＝37。"),
    ("等差數列首項為 3、公差為 2，前 8 項和為何？", ["80", "64", "72", "88"], "A", "第 8 項為 3＋7×2＝17，首尾平均為 10，前 8 項和為 8×10＝80。"),
    ("下列哪一個數列是等差數列？", ["4、9、14、19、…", "2、4、8、16、…", "1、4、9、16、…", "3、6、12、24、…"], "A", "第一個數列相鄰兩項差都為 5，符合等差數列定義。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-8-3-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究數列規律、通項、遞推、等差數列與求和能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 sequence questions")


if __name__ == "__main__":
    main()
