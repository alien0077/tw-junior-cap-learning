#!/usr/bin/env python3
"""Give the second member of each exact duplicate prompt a distinct question."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "questions/math/question-math-performance-d-2.json": (
        "一組資料 4、8、9、13、16 的中位數為何？",
        ["8", "9", "10", "13"],
        "B",
        "資料共有五筆，先排序後取第三筆，故中位數為 9。",
    ),
    "questions/math/question-math-performance-a-9.json": (
        "若 3x²y 與 －5x²y 為同類項，兩者的共同變數部分為何？",
        ["x+y", "x²y", "3x²", "－5y"],
        "B",
        "同類項需有相同的變數及其指數，共同變數部分是 x²y。",
    ),
    "questions/math/question-math-performance-n-iv-5-8.json": (
        "直角三角形兩股長為 9 與 12，斜邊長為何？",
        ["13", "15", "18", "21"],
        "B",
        "由畢氏定理，斜邊=√(9²+12²)=√225=15。",
    ),
    "questions/math/question-math-performance-d-1.json": (
        "資料 5、7、12、16、20 的平均數為何？",
        ["10", "12", "14", "16"],
        "B",
        "平均數=(5+7+12+16+20)÷5=60÷5=12。",
    ),
    "questions/math/question-math-performance-n-iv-5-1.json": (
        "√121 的值為何？",
        ["－11", "5", "11", "121"],
        "C",
        "√121 表示非負平方根，因此 √121=11。",
    ),
    "questions/math/question-math-performance-s-iv-11-6.json": (
        "一個三角形三頂點的外接圓圓心，到三頂點的距離有何關係？",
        ["三段皆相等", "只有最長邊相等", "三段和為周長", "皆為零"],
        "A",
        "外心到三個頂點等距，這個共同距離就是外接圓半徑。",
    ),
    "questions/math/question-math-performance-n-iv-7-9.json": (
        "數列 3、6、12、24、… 的第 6 項為何？",
        ["48", "72", "96", "192"],
        "C",
        "這是首項 3、公比 2 的等比數列，第 6 項=3×2⁵=96。",
    ),
    "questions/math/question-math-performance-n-iv-3-3.json": (
        "2⁵ 的值為何？",
        ["10", "16", "25", "32"],
        "D",
        "2⁵=2×2×2×2×2=32。",
    ),
}


def main():
    for relative, (prompt, options, answer, explanation) in REPLACEMENTS.items():
        path = ROOT / relative
        data = json.loads(path.read_text(encoding="utf-8"))
        data["prompt"] = prompt
        data["options"] = [
            {"id": chr(ord("A") + i), "text": text}
            for i, text in enumerate(options)
        ]
        data["answer"] = {"value": answer, "explanation": explanation}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        note = data.setdefault("provenance", {}).get("authoringNote", "")
        marker = " exact duplicate prompt replaced 2026-08-28"
        if marker.strip() not in note:
            data["provenance"]["authoringNote"] = f"{note}{marker}."
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"replaced {len(REPLACEMENTS)} exact duplicate questions")


if __name__ == "__main__":
    main()
