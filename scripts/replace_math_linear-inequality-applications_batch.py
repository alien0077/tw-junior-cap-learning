"""以公開國中數學段考的一元一次不等式應用方向，獨立替換 A-7-8 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-7-8.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-7-8"
KNOWLEDGE = "kg-math-content-a-7-8"
ITEMS = [
    ("解不等式 3x－4≥11，結果為何？", ["x≥5", "x≤5", "x≥7/3", "x≤7/3"], "A", "同加 4 得 3x≥15，再除以 3 得 x≥5。"),
    ("禮堂已有 32 人，最多容納 45 人，若再進入 x 人，x 應符合哪個條件？", ["x≤13", "x≥13", "x＜13", "x＞13"], "A", "32＋x≤45，所以 x≤13。"),
    ("每本講義 80 元，預算 500 元，最多可買幾本？", ["6 本", "5 本", "7 本", "8 本"], "A", "80x≤500，得 x≤6.25；購買本數為整數，最多 6 本。"),
    ("解不等式 3(x－2)＜12，結果為何？", ["x＜6", "x＞6", "x＜4", "x＞4"], "A", "除以正數 3 得 x－2＜4，再同加 2 得 x＜6。"),
    ("某校規定跑步時間 t 分鐘不得超過 18 分鐘，若訓練後比原時間少 3 分鐘，原時間至少需符合什麼條件才可能達標？", ["t－3≤18", "t＋3≤18", "t－3≥18", "3t≤18"], "A", "達標後時間是 t－3，不能超過 18，因此不等式為 t－3≤18。"),
    ("解不等式－2x＋7≤15，結果為何？", ["x≥－4", "x≤－4", "x≥4", "x≤4"], "A", "同減 7 得－2x≤8，除以負數－2 後方向反轉，得 x≥－4。"),
    ("數線上在 3 處畫實心圓，並向左畫線，代表哪個解集？", ["x≤3", "x＜3", "x≥3", "x＞3"], "A", "實心圓包含 3，向左表示小於，因此是 x≤3。"),
    ("兩個連續整數的和小於 15，較小的整數 x 為何？", ["x≤6", "x＜6", "x≤7", "x＜7"], "A", "x＋(x＋1)＜15 得 2x＜14，所以 x＜7；x 為整數，故 x≤6。"),
    ("車資為基本費 50 元加上每公里 12 元，若車資不超過 200 元，最多可行駛幾公里？", ["12 公里", "13 公里", "12.5 公里", "15 公里"], "A", "50＋12x≤200，得 x≤12.5；以完整公里計算，最多 12 公里。"),
    ("解聯立不等式 1≤2x＋3＜11，結果為何？", ["－1≤x＜4", "－2≤x＜5", "1≤x＜4", "－1＜x≤4"], "A", "各部分同減 3 得－2≤2x＜8，再除以 2 得－1≤x＜4。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-7-8-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究一元一次不等式解法、數線與生活情境能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 linear-inequality application questions")

if __name__ == "__main__":
    main()
