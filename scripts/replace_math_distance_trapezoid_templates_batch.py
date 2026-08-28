#!/usr/bin/env python3
"""Replace repeated templates for coordinate distance and trapezoids."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
SOURCE_URL = (
    "https://www.yacjh.kh.edu.tw/upload/221/101_30637/"
    "114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83"
    "%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
)


UNITS = {
    "g-8-1": {
        "lesson": "lesson-math-content-g-8-1",
        "kg": "kg-math-content-g-8-1",
        "title": "直角坐標系上兩點距離公式",
        "items": [
            ("點 A(1,2) 與 B(1,8) 的距離為何？", ["5", "6", "7", "10"], "B", "兩點 x 相同，距離為 |8−2|=6。"),
            ("點 P(－3,4) 位於哪一個象限？", ["第一象限", "第二象限", "第三象限", "第四象限"], "B", "x<0 且 y>0，所以 P 在第二象限。"),
            ("點 C(－2,－5) 到 x 軸的距離為何？", ["2", "3", "5", "7"], "C", "到 x 軸的距離是 |y|=5。"),
            ("點 D(6,－1) 到 y 軸的距離為何？", ["1", "5", "6", "7"], "C", "到 y 軸的距離是 |x|=6。"),
            ("點 A(0,0) 與 B(3,4) 的距離為何？", ["3", "4", "5", "7"], "C", "距離=√(3²+4²)=5。"),
            ("點 P(－2,3) 與 Q(4,3) 的中點坐標為何？", ["(1,3)", "(2,3)", "(1,0)", "(－1,3)"], "A", "中點=((−2+4)/2,(3+3)/2)=(1,3)。"),
            ("若兩點的 y 坐標相同，連結兩點的線段與哪條坐標軸平行？", ["x 軸", "y 軸", "兩軸都平行", "不一定是直線"], "A", "y 固定表示水平線，與 x 軸平行。"),
            ("點 R(－1,－4) 與 S(5,4) 的距離為何？", ["6", "8", "10", "12"], "C", "距離=√(6²+8²)=10。"),
            ("若線段端點為 (2,1)、(8,7)，其中點為何？", ["(5,4)", "(4,5)", "(6,6)", "(10,8)"], "A", "中點=((2+8)/2,(1+7)/2)=(5,4)。"),
            ("點 T(－4,0) 對 y 軸的對稱點為何？", ["(4,0)", "(－4,0)", "(0,4)", "(4,－4)"], "A", "對 y 軸鏡射會使 x 變號，故為 (4,0)。"),
        ],
    },
    "s-8-11": {
        "lesson": "lesson-math-content-s-8-11",
        "kg": "kg-math-content-s-8-11",
        "title": "梯形的基本性質",
        "items": [
            ("梯形的定義是什麼？", ["兩組對邊都平行", "至少一組對邊平行", "四邊都相等", "四角都相等"], "B", "梯形具有至少一組平行的對邊。"),
            ("梯形上底 6、下底 14、高 5 公分，面積為何？", ["25", "40", "50", "70"], "C", "梯形面積=(6+14)×5÷2=50 平方公分。"),
            ("等腰梯形的兩腰有何關係？", ["相等", "互相垂直", "互為平行線", "和為上底"], "A", "等腰梯形的兩腰長相等。"),
            ("等腰梯形的一個底角為 68°，同一底上的另一個底角為何？", ["22°", "68°", "112°", "136°"], "B", "等腰梯形同底角相等，因此為 68°。"),
            ("梯形兩底長 8、16，高 7，梯形面積為何？", ["42", "56", "84", "112"], "C", "面積=(8+16)×7÷2=84。"),
            ("梯形的中線長度等於什麼？", ["兩腰和的一半", "兩底和的一半", "兩底差", "高的兩倍"], "B", "梯形中線=（上底+下底）÷2。"),
            ("梯形上、下底長分別為 5、13 公分，其中線長為何？", ["8", "9", "18", "65"], "B", "中線=(5+13)÷2=9。"),
            ("若梯形高固定，兩底同時增加 2 公分，面積會如何變化？", ["增加高×2 平方公分", "減少高×2 平方公分", "一定不變", "變為原來一半"], "A", "面積變化=((2+2)×高)/2=2×高。"),
            ("等腰梯形的兩條對角線有何關係？", ["相等", "互相垂直", "一長一短", "和等於高"], "A", "等腰梯形的對角線相等。"),
            ("梯形面積公式中的高，應指哪一段距離？", ["兩底所在平行線的垂直距離", "任一腰長", "兩底長度相加", "對角線長"], "A", "高度是兩條平行底邊所在直線間的垂直距離。"),
        ],
    },
}


def build_question(unit, index, item):
    prompt, options, answer, explanation = item
    config = UNITS[unit]
    return {
        "id": f"question-math-content-{unit}-{index}",
        "subject": "math",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": chr(ord("A") + i), "text": text} for i, text in enumerate(options)],
        "knowledgeIds": [config["kg"]],
        "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE_URL,
            "sourceLocator": (
                "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；"
                f"參考 {config['title']} 題型與官方課綱 KG {config['kg']}"
            ),
            "authoringNote": (
                "Substantive rewrite with new values, contexts, options, and explanations; "
                "no reproduction of public-exam wording, figures, or answer key. "
                "待第二輪 AI／Terra 內容複核。"
            ),
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-29",
        "lessonId": config["lesson"],
    }


def main():
    count = 0
    for unit, config in UNITS.items():
        for index, item in enumerate(config["items"], start=1):
            path = QUESTION_DIR / f"question-math-content-{unit}-{index}.json"
            path.write_text(json.dumps(build_question(unit, index, item), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            count += 1
    print(f"replaced {count} distance/trapezoid template questions")


if __name__ == "__main__":
    main()
