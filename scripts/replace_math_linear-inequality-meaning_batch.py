"""以公開國中數學段考的不等式能力方向，獨立替換 A-7-7 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-7-7.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-7-7"
KNOWLEDGE = "kg-math-content-a-7-7"
ITEMS = [
    ("解不等式 2x＋3＜11，結果為何？", ["x＜4", "x＞4", "x＜7", "x＞7"], "A", "兩邊同減 3 得 2x＜8，再除以 2 得 x＜4。"),
    ("解不等式 5－x≥2，結果為何？", ["x≤3", "x≥3", "x≤－3", "x≥－3"], "A", "同減 5 得－x≥－3，再乘以－1 時方向反轉，得 x≤3。"),
    ("解不等式－3x＜9，結果為何？", ["x＞－3", "x＜－3", "x＞3", "x＜3"], "A", "兩邊除以負數－3 時不等號反向，所以 x＞－3。"),
    ("解不等式 4x－7≤13，結果為何？", ["x≤5", "x≥5", "x≤6", "x≥6"], "A", "同加 7 得 4x≤20，再除以 4 得 x≤5。"),
    ("解不等式 2(x＋1)＞8，結果為何？", ["x＞3", "x＜3", "x＞4", "x＜4"], "A", "除以 2 得 x＋1＞4，再同減 1 得 x＞3。"),
    ("解不等式 x÷2＋1≥5，結果為何？", ["x≥8", "x≤8", "x≥10", "x≤10"], "A", "同減 1 得 x÷2≥4，再乘以 2 得 x≥8。"),
    ("數線上在 2 處畫空心圓，並向右畫線，代表哪個解集？", ["x＞2", "x≥2", "x＜2", "x≤2"], "A", "空心圓表示不包含 2，向右表示大於 2，因此是 x＞2。"),
    ("解不等式 3－2x＞7，結果為何？", ["x＜－2", "x＞－2", "x＜2", "x＞2"], "A", "同減 3 得－2x＞4，除以負數－2 後方向反轉，得 x＜－2。"),
    ("小明有 120 元，每枝筆 18 元，最多可買幾枝？", ["6 枝", "7 枝", "8 枝", "5 枝"], "A", "18x≤120，得 x≤6 又 2/3；購買枝數為整數，所以最多 6 枝。"),
    ("解聯立不等式－1≤x＋2＜4，結果為何？", ["－3≤x＜2", "－1≤x＜4", "－3＜x≤2", "1≤x＜6"], "A", "不等式各部分同減 2，得到－3≤x＜2。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-7-7-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究一元一次不等式、數線、邊界與情境建模能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 linear-inequality questions")

if __name__ == "__main__":
    main()
