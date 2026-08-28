"""以公開數學試題的空間與形狀能力方向，獨立替換 S 領域彙整題。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-s.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-s"
KNOWLEDGE = "kg-math-content-s"

ITEMS = [
    ("三角形的兩個內角為 50° 與 70°，第三個內角為何？", ["60°", "50°", "70°", "120°"], "A", "三角形內角和為 180°，所以第三角為 180°－50°－70°＝60°。"),
    ("直角三角形兩股長為 6 與 8，斜邊長為何？", ["10", "12", "14", "√28"], "A", "由畢氏定理，斜邊平方為 6^2＋8^2＝100，所以斜邊為 10。"),
    ("半徑為 5 的圓，其直徑為何？", ["10", "5", "25", "2.5"], "A", "直徑是半徑的 2 倍，因此為 2×5＝10。"),
    ("平行線被一條截線所截時，一對同位角的關係為何？", ["相等", "互為補角", "一定互為餘角", "無法比較"], "A", "兩條平行線被截線截出的一對同位角相等。"),
    ("底為 12、高為 7 的平行四邊形面積為何？", ["84", "42", "19", "168"], "A", "平行四邊形面積為底×高，12×7＝84。"),
    ("相似三角形的對應邊比為 2:3，若小三角形對應邊長為 8，大三角形為何？", ["12", "10", "16", "24"], "A", "大三角形對應邊為 8×(3/2)＝12。"),
    ("點 A(1,2) 向右平移 3 單位後的座標為何？", ["(4,2)", "(1,5)", "(-2,2)", "(4,5)"], "A", "向右平移只增加 x 座標，得到 (1＋3,2)＝(4,2)。"),
    ("正方形周長為 28，則其面積為何？", ["49", "28", "14", "196"], "A", "邊長為 28÷4＝7，面積為 7^2＝49。"),
    ("圓周率取 3.14，半徑 3 的圓周長約為何？", ["18.84", "9.42", "28.26", "6.28"], "A", "圓周長＝2πr＝2×3.14×3＝18.84。"),
    ("從同一點向圓作切線，兩條切線段長度的關係為何？", ["相等", "一長一短", "和等於半徑", "乘積等於直徑"], "A", "同一外點向同一圓所作的兩條切線段長相等。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-s-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究空間與形狀的角度、幾何量、相似、座標變換與圓幾何能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 space-and-shape domain questions")


if __name__ == "__main__":
    main()
