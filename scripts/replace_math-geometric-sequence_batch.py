"""以公開數學試題的數列與倍增應用方向，獨立替換 N-8-6 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-8-6.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-8-6"
KNOWLEDGE = "kg-math-content-n-8-6"

ITEMS = [
    ("等比數列 3、6、12、24、… 的下一項為何？", ["48", "36", "30", "72"], "A", "每一項是前一項的 2 倍，因此下一項為 24×2＝48。"),
    ("等比數列首項為 1、公比為 3，則第 5 項為何？", ["81", "27", "243", "15"], "A", "第 5 項為 1×3⁴＝81。"),
    ("等比數列首項為 5、公比為 2，則第 6 項為何？", ["160", "80", "320", "64"], "A", "第 6 項為 5×2⁵＝160。"),
    ("等比數列 81、27、9、… 的下一項為何？", ["3", "6", "1", "－3"], "A", "公比為 1/3，所以下一項為 9×1/3＝3。"),
    ("等比數列中 a₂＝12、a₃＝36，且公比為正數，則 a₁ 為何？", ["4", "3", "6", "24"], "A", "公比為 36÷12＝3，因此 a₁＝12÷3＝4。"),
    ("培養皿開始有 5 個細胞，每次分裂後數量變成 2 倍；連續分裂 6 次後有幾個細胞？", ["320 個", "160 個", "64 個", "30 個"], "A", "每次乘以 2，6 次後為 5×2⁶＝320 個。"),
    ("某數列首項為 2、公比為 4，則前 4 項為何？", ["2、8、32、128", "2、6、10、14", "4、8、16、32", "2、4、8、16"], "A", "依序乘以 4，得到 2、8、32、128。"),
    ("三個正數 2、x、18 成等比數列，則 x 為何？", ["6", "4", "9", "10"], "A", "中項平方等於兩旁乘積：x²＝2×18＝36；因 x 為正，x＝6。"),
    ("等比數列首項為 64、公比為 1/2，則第 4 項為何？", ["8", "16", "32", "4"], "A", "第 4 項為 64×(1/2)³＝8。"),
    ("下列哪一個數列是等比數列？", ["5、10、20、40、…", "5、10、15、20、…", "1、4、9、16、…", "2、5、9、14、…"], "A", "第一個數列相鄰兩項的比都為 2，符合等比數列定義。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-8-6-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究等比數列公比、通項、指定項與倍增情境能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 geometric-sequence questions")


if __name__ == "__main__":
    main()
