"""以公開國中數學段考的乘法公式能力方向，獨立替換 A-8-1 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-8-1.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-8-1"
KNOWLEDGE = "kg-math-content-a-8-1"
ITEMS = [
    ("展開 (x＋5)²，結果為何？", ["x²＋10x＋25", "x²＋25", "x²＋5x＋25", "x²－10x＋25"], "A", "平方和公式 (a＋b)²＝a²＋2ab＋b²，代入 x 與 5 得 x²＋10x＋25。"),
    ("展開 (a－3)²，結果為何？", ["a²－6a＋9", "a²－9", "a²－3a＋9", "a²＋6a＋9"], "A", "平方差的平方公式為 a²－2ab＋b²，因此得到 a²－6a＋9。"),
    ("化簡 (y＋4)(y－4)，結果為何？", ["y²－16", "y²＋16", "y²－8y＋16", "y²＋8y＋16"], "A", "這是平方差公式 (a＋b)(a－b)＝a²－b²，結果為 y²－16。"),
    ("展開 (2m＋1)²，結果為何？", ["4m²＋4m＋1", "4m²＋1", "2m²＋4m＋1", "4m²＋2m＋1"], "A", "(2m＋1)²＝(2m)²＋2(2m)(1)＋1²＝4m²＋4m＋1。"),
    ("展開 (3p－2)²，結果為何？", ["9p²－12p＋4", "9p²－4", "9p²－6p＋4", "3p²－12p＋4"], "A", "(3p－2)²＝9p²－12p＋4。中間項不可漏掉或誤用符號。"),
    ("將 x²＋12x＋36 寫成完全平方，結果為何？", ["(x＋6)²", "(x＋12)²", "(x＋3)²", "(x－6)²"], "A", "36＝6²，且中間項 12x＝2×x×6，所以為 (x＋6)²。"),
    ("因式分解 n²－49，結果為何？", ["(n－7)(n＋7)", "(n－49)(n＋1)", "(n－7)²", "(n＋49)(n－1)"], "A", "49＝7²，使用平方差公式得到 (n－7)(n＋7)。"),
    ("展開 (q＋7)(q＋2)，結果為何？", ["q²＋9q＋14", "q²＋14q＋9", "q²＋5q＋14", "q²＋9q＋9"], "A", "逐項相乘並合併同類項：q²＋2q＋7q＋14＝q²＋9q＋14。"),
    ("將 4r²－20r＋25 因式分解，結果為何？", ["(2r－5)²", "(2r＋5)²", "(4r－5)²", "(r－5)²"], "A", "4r²－20r＋25 符合 (2r)²－2(2r)(5)＋5²，故為 (2r－5)²。"),
    ("展開 (z－8)²，結果為何？", ["z²－16z＋64", "z²－64", "z²＋16z＋64", "z²－8z＋64"], "A", "平方差的平方公式給出 z²－2×z×8＋8²，即 z²－16z＋64。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-8-1-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        rotated = options[shift:] + options[:shift]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + j), "text": value} for j, value in enumerate(rotated)]
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["knowledgeIds"] = [KNOWLEDGE]
        data["lessonId"] = LESSON
        data["difficulty"] = "medium"
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中公開數學段考；研究乘法公式、展開、因式分解與驗算能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 multiplication-formula questions")

if __name__ == "__main__":
    main()
