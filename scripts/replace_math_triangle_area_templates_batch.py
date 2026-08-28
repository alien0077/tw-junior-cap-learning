#!/usr/bin/env python3
"""Replace repeated templates for triangle properties and plane area."""

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
    "s-8-8": {
        "lesson": "lesson-math-content-s-8-8",
        "kg": "kg-math-content-s-8-8",
        "title": "三角形的基本性質",
        "items": [
            ("三角形的三個內角和為何？", ["90°", "180°", "270°", "360°"], "B", "任意三角形的內角和為 180°。"),
            ("三角形兩角為 48°、67°，第三角為何？", ["55°", "65°", "75°", "85°"], "B", "第三角=180°−48°−67°=65°。"),
            ("三角形的一個外角為 125°，其兩個不相鄰內角之一為 55°，另一個為何？", ["60°", "70°", "80°", "90°"], "B", "外角等於兩個不相鄰內角和，另一角=125°−55°=70°。"),
            ("三角形三邊為 5、7、x，x 為整數時，下列何者可能是 x？", ["1", "2", "12", "10"], "D", "三角形不等式要求 2<x<12，x=10 可行。"),
            ("等腰三角形的兩腰相等，若頂角為 40°，每個底角為何？", ["40°", "60°", "70°", "80°"], "C", "兩底角相等，各為 (180°−40°)÷2=70°。"),
            ("若三角形兩邊長為 6、9，第三邊不可能是哪一個？", ["4", "6", "12", "16"], "D", "第三邊需滿足 3<x<15，16 不可能。"),
            ("三角形中，較長的邊所對的角通常有何關係？", ["較小", "較大", "必為直角", "必為 180°"], "B", "三角形中大邊對大角，小邊對小角。"),
            ("若一個三角形有兩個角相等，則其對應的兩邊有何關係？", ["相等", "互為倒數", "和為第三邊", "必垂直"], "A", "等角對等邊，所以對應兩邊相等。"),
            ("三角形的一個外角與相鄰內角的和為何？", ["90°", "180°", "270°", "360°"], "B", "外角與相鄰內角形成鄰補角，和為 180°。"),
            ("若三角形三邊為 7、8、9，則其周長為何？", ["16", "22", "24", "26"], "C", "周長=7+8+9=24。"),
        ],
    },
    "s-8-7": {
        "lesson": "lesson-math-content-s-8-7",
        "kg": "kg-math-content-s-8-7",
        "title": "平面圖形的面積",
        "items": [
            ("底 12 公分、高 5 公分的平行四邊形，面積為何？", ["17", "30", "60", "120"], "C", "平行四邊形面積=底×高=12×5=60 平方公分。"),
            ("底 10 公分、高 6 公分的三角形，面積為何？", ["16", "30", "60", "120"], "B", "三角形面積=底×高÷2=10×6÷2=30 平方公分。"),
            ("梯形上底 5、下底 11、高 4 公分，面積為何？", ["16", "24", "32", "44"], "C", "梯形面積=(5+11)×4÷2=32 平方公分。"),
            ("菱形兩條對角線長 8、12 公分，面積為何？", ["20", "40", "48", "96"], "C", "菱形面積=兩對角線乘積÷2=8×12÷2=48。"),
            ("一個長方形長 9、寬 4 公分，面積為何？", ["13", "26", "36", "72"], "C", "長方形面積=長×寬=9×4=36 平方公分。"),
            ("由一個底 6、高 4 的三角形與一個長 6、寬 3 的長方形組成的圖形，總面積為何？", ["18", "24", "30", "36"], "C", "三角形面積 12 加長方形面積 18，總面積為 30。"),
            ("平行四邊形的底固定為 8 公分，若高由 3 增為 6 公分，面積變為原來幾倍？", ["1/2", "2", "3", "4"], "B", "底不變時面積與高成正比，高變 2 倍，面積也變 2 倍。"),
            ("計算一塊花圃所占的平面大小，最合適的單位為何？", ["平方公尺", "立方公尺", "公升", "公斤"], "A", "花圃面積是二維量，適合用平方公尺表示。"),
            ("一個複合圖形可分成兩個不重疊的三角形，面積分別為 14 與 19 平方公分，總面積為何？", ["5", "19", "28", "33"], "D", "不重疊部分面積相加，14+19=33 平方公分。"),
            ("若圓周率取 π，半徑 4 公分的圓面積為何？", ["4π", "8π", "16π", "32π"], "C", "圓面積=πr²=π×4²=16π 平方公分。"),
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
    print(f"replaced {count} triangle/area template questions")


if __name__ == "__main__":
    main()
