"""以公開國中數學段考的聯立方程式幾何意義方向，獨立替換 A-7-6 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-7-6.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-7-6"
KNOWLEDGE = "kg-math-content-a-7-6"
ITEMS = [
    ("直線 x＋y＝6 在坐標平面上的兩個截距點為何？", ["(6,0) 與 (0,6)", "(6,6) 與 (0,0)", "(－6,0) 與 (0,－6)", "(3,0) 與 (0,3)"], "A", "令 y＝0 得 x＝6；令 x＝0 得 y＝6，因此截距為 (6,0)、(0,6)。"),
    ("直線 2x＋y＝4 改寫成 y＝mx＋b 後，斜率 m 為何？", ["－2", "2", "－1/2", "4"], "A", "移項得 y＝－2x＋4，所以斜率是－2。"),
    ("兩直線 x＋y＝5、x－y＝1 的交點為何？", ["(3,2)", "(2,3)", "(4,1)", "(1,4)"], "A", "兩式相加得 2x＝6，所以 x＝3；代回得 y＝2。"),
    ("兩直線 x＋y＝3 與 x＋y＝7 的圖形關係為何？", ["平行且沒有交點", "重合且有無限多交點", "垂直且有一個交點", "相交於 (3,7)"], "A", "兩式斜率相同但截距不同，代表平行直線，沒有共同解。"),
    ("兩方程式 x＋y＝4 與 2x＋2y＝8 的圖形關係為何？", ["同一直線，有無限多共同解", "平行且無共同解", "只有一個共同解", "兩條垂直線"], "A", "第二式是第一式的 2 倍，兩式代表同一直線。"),
    ("直線 y＝2x＋1 上，當 x＝3 時的點為何？", ["(3,7)", "(7,3)", "(3,5)", "(2,7)"], "A", "代入 x＝3：y＝2×3＋1＝7，所以點為 (3,7)。"),
    ("在聯立方程式的圖形中，兩條直線的交點代表什麼？", ["同時滿足兩個方程式的解", "只滿足第一式的點", "兩直線的斜率總和", "坐標軸的原點"], "A", "交點的坐標同時代入兩式都成立，因此就是聯立方程式的共同解。"),
    ("直線 y＝－x＋6 與 y＝x 的交點為何？", ["(3,3)", "(6,6)", "(0,6)", "(2,4)"], "A", "令兩式相等：－x＋6＝x，得 x＝3，再得 y＝3。"),
    ("下列哪一個方程式的圖形是通過 x＝4 的垂直直線？", ["x＝4", "y＝4", "y＝x＋4", "x＋y＝4"], "A", "x＝4 表示所有 y 值都可取，圖形是垂直線。"),
    ("下列哪一點在直線 3x＋2y＝12 上？", ["(2,3)", "(3,2)", "(0,3)", "(4,2)"], "A", "代入 (2,3)：3×2＋2×3＝12，符合方程式。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-7-6-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究聯立方程式圖形、斜率、交點與解集判讀能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 simultaneous-equation geometry questions")

if __name__ == "__main__":
    main()
