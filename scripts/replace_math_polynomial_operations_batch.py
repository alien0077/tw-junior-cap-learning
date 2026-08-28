"""以公開國中數學段考的多項式運算能力方向，獨立替換 A-8-3 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-8-3.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-8-3"
KNOWLEDGE = "kg-math-content-a-8-3"
ITEMS = [
    ("整理 3x＋5x－2 後，結果為何？", ["8x－2", "8x＋2", "2x－2", "15x－2"], "A", "3x 與 5x 是同類項，相加得 8x，常數項保留為－2。"),
    ("多項式 4x³－2x²＋1 的次數為何？", ["3", "2", "1", "4"], "A", "最高次項是 4x³，因此多項式的次數為 3。"),
    ("化簡 2a＋3a－4，結果為何？", ["5a－4", "5a＋4", "a－4", "6a－4"], "A", "2a 與 3a 為同類項，係數相加得到 5a。"),
    ("計算 (3x＋2)＋(x－5)，結果為何？", ["4x－3", "4x＋7", "2x－3", "3x－3"], "A", "合併 x 項與常數項：3x＋x＝4x，2－5＝－3。"),
    ("計算 (7y－3)－(2y＋4)，結果為何？", ["5y－7", "5y＋1", "9y＋1", "9y－7"], "A", "減去括號內各項時要改變符號，得到 7y－3－2y－4＝5y－7。"),
    ("化簡 2(3m－4)＋m，結果為何？", ["7m－8", "6m－8", "7m－4", "5m－8"], "A", "先用分配律得 6m－8，再與 m 合併為 7m－8。"),
    ("展開 (x＋3)(x＋2)，結果為何？", ["x²＋5x＋6", "x²＋6x＋5", "x²＋x＋6", "2x²＋5x＋6"], "A", "逐項相乘：x²＋2x＋3x＋6＝x²＋5x＋6。"),
    ("當 x≠0 時，(6x²＋9x)÷3x 的商為何？", ["2x＋3", "2x＋9", "3x＋3", "2x²＋3x"], "A", "分子各項除以 3x，得到 6x²÷3x＋9x÷3x＝2x＋3。"),
    ("化簡 4p－(2p－7)，結果為何？", ["2p＋7", "2p－7", "6p＋7", "6p－7"], "A", "去括號後為 4p－2p＋7，合併得 2p＋7。"),
    ("若 f(x)＝3x²－x＋1，則 f(2) 為何？", ["11", "9", "13", "7"], "A", "代入 x＝2：3×2²－2＋1＝12－2＋1＝11。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-8-3-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究多項式四則運算、代入與驗算能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 polynomial-operation questions")

if __name__ == "__main__":
    main()
