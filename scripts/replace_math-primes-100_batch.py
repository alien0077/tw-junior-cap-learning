"""以公開數學試題的數與量判讀方向，獨立替換 N-7-1 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-7-1.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-7-1"
KNOWLEDGE = "kg-math-content-n-7-1"

ITEMS = [
    ("下列哪一個數是質數？", ["37", "39", "51", "57"], "A", "37 除了 1 和 37 外沒有其他正因數，因此是質數；其餘數字都可再分解。"),
    ("下列哪一個數不是質數？", ["49", "47", "53", "59"], "A", "49＝7×7，有 1、7、49 三個正因數，因此不是質數。"),
    ("84 的標準質因數分解式為何？", ["2²×3×7", "2×3×14", "4×21", "2³×3×7"], "A", "84＝2×42＝2²×21＝2²×3×7，且每個因數都是質數。"),
    ("20 到 40 之間（不含 20 與 40）共有幾個質數？", ["4", "5", "6", "7"], "A", "這些質數為 23、29、31、37，共 4 個。"),
    ("若質數 p 是 30 的因數，下列哪一個數可能是 p？", ["2", "4", "6", "10"], "A", "30 的質因數為 2、3、5；四個選項中只有 2 是質數。"),
    ("77 可表示為兩個相異質數的乘積。這兩個質數中較大者是多少？", ["11", "7", "14", "77"], "A", "77＝7×11，兩個質數為 7 與 11，較大者是 11。"),
    ("91 是下列哪一個質數的倍數？", ["7", "3", "5", "11"], "A", "91＝7×13，所以 91 是 7 的倍數。"),
    ("下列哪一個數是大於 50 且小於 60 的質數？", ["53", "51", "55", "57"], "A", "53 只有 1 與 53 兩個正因數；51、55、57 都能分解為較小整數的乘積。"),
    ("下列哪一個數恰好有兩個正因數？", ["29", "27", "21", "1"], "A", "29 的正因數只有 1 和 29，恰好有兩個，因此是質數。"),
    ("關於質數的敘述，下列何者正確？", ["2 是唯一的偶質數", "1 是最小的質數", "所有奇數都是質數", "每個質數都大於 2"], "A", "2 是偶數且只有 1 和 2 兩個正因數，是唯一的偶質數；1 不是質數。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-7-1-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究數與量判讀、質數、因數與標準分解式能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 prime-number questions")


if __name__ == "__main__":
    main()
