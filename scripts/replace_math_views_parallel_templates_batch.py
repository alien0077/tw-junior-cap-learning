#!/usr/bin/env python3
"""Replace repeated templates for orthographic views and parallel lines."""

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
    "s-7-2": {
        "lesson": "lesson-math-content-s-7-2",
        "kg": "kg-math-content-s-7-2",
        "title": "三視圖",
        "items": [
            ("同一個長方體的前視圖主要呈現哪一組尺寸？", ["長與高", "長與寬", "寬與高", "只有體積"], "A", "前視圖呈現物體的水平長度與垂直高度。"),
            ("從正上方觀察一個長方體，俯視圖主要呈現哪一組尺寸？", ["長與高", "長與寬", "寬與高", "斜邊與高"], "B", "俯視圖由上方觀察，呈現長與寬。"),
            ("一個長方體長 6、寬 4、高 3，若畫前視圖，矩形尺寸為何？", ["6×4", "6×3", "4×3", "6×6"], "B", "前視圖呈現長與高，所以尺寸為 6×3。"),
            ("右視圖可用來判讀長方體的哪一組尺寸？", ["長與寬", "長與高", "寬與高", "只有表面積"], "C", "右視圖呈現物體的寬與高。"),
            ("若物體的前視圖與右視圖高度相同，這個高度代表什麼？", ["物體的共同垂直高度", "物體的總表面積", "物體的重量", "俯視圖的面積"], "A", "不同側視圖中的垂直尺寸都反映物體高度。"),
            ("一個由兩個相同正方體上下疊成的立體，前視圖最可能是什麼形狀？", ["寬 1、高 2 的長方形", "寬 2、高 1 的長方形", "圓形", "三角形"], "A", "上下疊放使高度為兩個單位、寬度為一個單位。"),
            ("判讀三視圖時，前視圖、俯視圖與右視圖最重要的共同條件是什麼？", ["尺寸與位置彼此一致", "三圖顏色必須相同", "三圖面積必須相等", "每圖都必須是正方形"], "A", "三視圖是同一物體的不同方向投影，對應尺寸與位置需一致。"),
            ("一個正方體每邊 5 公分，其前視圖與俯視圖各為何？", ["都是邊長 5 的正方形", "一個圓和一個正方形", "都是長方形但邊長不同", "只能畫出一個點"], "A", "正方體從各正交方向看都是邊長 5 的正方形。"),
            ("若俯視圖顯示兩個並排的正方形，但前視圖只顯示一個正方形，最可能表示什麼？", ["兩個方塊左右排列且高度相同", "兩個方塊上下排列", "物體是球體", "視圖一定畫錯"], "A", "俯視圖的左右排列與前視圖重疊成同一高度輪廓。"),
            ("三視圖中若某一視圖的寬度與另一視圖的深度不一致，應先做什麼？", ["檢查投影方向與對應尺寸", "直接增加物體高度", "把所有線改成曲線", "忽略差異"], "A", "不同視圖需依投影方向核對共同尺寸，不能任意修改物體。"),
        ],
    },
    "s-8-3": {
        "lesson": "lesson-math-content-s-8-3",
        "kg": "kg-math-content-s-8-3",
        "title": "平行",
        "items": [
            ("兩條平行線被截線所截，一個同位角為 68°，另一個同位角為何？", ["68°", "112°", "122°", "180°"], "A", "平行線的同位角相等，因此為 68°。"),
            ("兩條平行線被截線所截，某內錯角為 75°，另一個內錯角為何？", ["15°", "75°", "105°", "150°"], "B", "平行線的內錯角相等，因此為 75°。"),
            ("若同側內角互為補角，其中一角為 113°，另一角為何？", ["57°", "67°", "77°", "113°"], "B", "平行線同側內角和為 180°，另一角=180°−113°=67°。"),
            ("斜率為 4 的直線與哪條直線平行？", ["y=4x−7", "y=−4x+1", "y=1/4x+2", "x=4"], "A", "平行直線斜率相等，y=4x−7 的斜率也是 4。"),
            ("過點 (2,5) 作水平線，其方程式為何？", ["x=2", "y=2", "y=5", "x=5"], "C", "水平線上 y 值固定，因此方程式為 y=5。"),
            ("若兩直線斜率分別為 －3 與 －3，且截距不同，兩線的關係為何？", ["平行且不重合", "垂直", "重合", "必互相垂直"], "A", "斜率相同且截距不同，表示兩線平行且不重合。"),
            ("一條截線與兩平行線交會，若某銳角為 52°，相鄰鈍角為何？", ["52°", "90°", "128°", "180°"], "C", "相鄰角互補，180°−52°=128°。"),
            ("判定兩直線平行時，哪項條件足夠？", ["一組同位角相等", "兩線長度相等", "兩線顏色相同", "只知道一條線斜率"], "A", "截線形成一組相等同位角即可判定兩線平行。"),
            ("若直線 y=－2x+6 與 y=－2x−1，兩線的距離關係為何？", ["平行不重合", "互相垂直", "重合", "必相交於原點"], "A", "兩線斜率同為 −2、截距不同，所以平行不重合。"),
            ("一條直線垂直於其中一條平行線，則它與另一條平行線的關係為何？", ["也垂直", "必平行", "必重合", "無法判斷"], "A", "同一直線垂直於兩條平行線，因此也垂直於另一條。"),
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
    print(f"replaced {count} views/parallel template questions")


if __name__ == "__main__":
    main()
