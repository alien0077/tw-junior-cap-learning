"""以公開國中數學段考的聯立方程式能力方向，獨立替換 A-7-4 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-7-4.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-7-4"
KNOWLEDGE = "kg-math-content-a-7-4"
ITEMS = [
    ("聯立方程式 x＋y＝11、x－y＝3 的解為何？", ["x＝7，y＝4", "x＝4，y＝7", "x＝8，y＝3", "x＝6，y＝5"], "A", "兩式相加得 2x＝14，所以 x＝7；代回得 y＝4。"),
    ("成人票 x 張、學生票 y 張共 8 張，票價分別 40、25 元且總額 260 元。x、y 為何？", ["x＝4，y＝4", "x＝3，y＝5", "x＝5，y＝3", "x＝6，y＝2"], "A", "x＋y＝8 且 40x＋25y＝260，聯立解得 x＝4、y＝4。"),
    ("若 2x＋y＝11 且 y＝3，x 為何？", ["4", "3", "5", "7"], "A", "把 y＝3 代入 2x＋y＝11，得 2x＋3＝11，所以 x＝4。"),
    ("聯立方程式 x＋y＝9、x－y＝1 的解為何？", ["x＝5，y＝4", "x＝4，y＝5", "x＝6，y＝3", "x＝3，y＝6"], "A", "兩式相加得 2x＝10，所以 x＝5；再得 y＝4。"),
    ("解聯立方程式 2x＋3y＝13、x＋y＝5，x、y 為何？", ["x＝2，y＝3", "x＝3，y＝2", "x＝1，y＝4", "x＝4，y＝1"], "A", "由 x＝5－y 代入第一式，得 10＋y＝13，所以 y＝3、x＝2。"),
    ("『兩種文具共 20 件』若以 x、y 分別代表兩種文具數量，最適合的方程式為何？", ["x＋y＝20", "x－y＝20", "xy＝20", "x÷y＝20"], "A", "總數是兩種數量相加，因此應寫成 x＋y＝20。"),
    ("下列哪一組數是聯立方程式 2x＋y＝8、x－y＝1 的解？", ["x＝3，y＝2", "x＝2，y＝3", "x＝4，y＝1", "x＝1，y＝4"], "A", "代入 (3,2)：2×3＋2＝8 且 3－2＝1，兩式都成立。"),
    ("有 5 元硬幣 x 枚、10 元硬幣 y 枚，共 12 枚且合計 90 元。x、y 為何？", ["x＝6，y＝6", "x＝8，y＝4", "x＝4，y＝8", "x＝10，y＝2"], "A", "x＋y＝12、5x＋10y＝90，解得 y＝6、x＝6。"),
    ("聯立方程式 x＋2y＝14、3x＋2y＝18 的解為何？", ["x＝2，y＝6", "x＝6，y＝2", "x＝4，y＝5", "x＝1，y＝7"], "A", "兩式相減得 2x＝4，所以 x＝2；代回得 y＝6。"),
    ("聯立方程式 x－y＝4、2x＋y＝11 的解為何？", ["x＝5，y＝1", "x＝1，y＝5", "x＝4，y＝0", "x＝6，y＝2"], "A", "兩式相加得 3x＝15，所以 x＝5；代回得 y＝1。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-7-4-{i}.json"
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
            "sourceLocator": f"鹽埕國中公開數學段考；研究聯立方程式、代入法、消去法與情境建模能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 simultaneous-equation questions")

if __name__ == "__main__":
    main()
