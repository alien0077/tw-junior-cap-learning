#!/usr/bin/env python3
"""Replace repeated templates for linear-function graphs and angles."""

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
    "f-8-2": {
        "lesson": "lesson-math-content-f-8-2",
        "kg": "kg-math-content-f-8-2",
        "title": "一次函數的圖形",
        "items": [
            ("直線通過 (1,3) 與 (4,9)，其斜率為何？", ["1", "2", "3", "4"], "B", "斜率=(9−3)/(4−1)=6/3=2。"),
            ("直線 y=3x−5 的 y 截距為何？", ["－5", "－3", "3", "5"], "A", "令 x=0 得 y=−5，因此 y 截距為 −5。"),
            ("下表中 x=0,1,2 時 y=4,7,10，對應的一次函數斜率為何？", ["2", "3", "4", "7"], "B", "x 每增加 1，y 增加 3，斜率為 3。"),
            ("兩條不重合的一次函數圖形互相平行時，兩直線的斜率有何關係？", ["互為倒數", "相等", "相差 1", "乘積為 0"], "B", "非垂直的平行直線斜率相等。"),
            ("若 y=2x+1，當 x=3 時 y 為何？", ["5", "6", "7", "8"], "C", "代入 x=3，y=2×3+1=7。"),
            ("下列哪一條直線的圖形由左向右下降？", ["y=4x+1", "y=−2x+3", "y=1/2x−4", "y=7"], "B", "斜率為負時，x 增加而 y 減少；y=−2x+3 符合。"),
            ("直線 y=2x−6 與 x 軸交於何點？", ["(0,−6)", "(2,0)", "(3,0)", "(6,0)"], "C", "與 x 軸交點 y=0，0=2x−6 得 x=3。"),
            ("直線 y=−x+4 與 y 軸的交點為何？", ["(−4,0)", "(0,−4)", "(0,4)", "(4,0)"], "C", "y 軸上 x=0，代入得 y=4，所以交點為 (0,4)。"),
            ("某計程車車資 y（元）與里程 x（公里）符合 y=25x+70，25 在此式中代表什麼？", ["起跳價", "每公里增加的費用", "總里程", "終點座標"], "B", "x 的係數 25 表示每增加 1 公里，車資增加 25 元。"),
            ("下列哪一組資料可由一次函數表示？", ["x=1,2,3 時 y=2,4,8", "x=1,2,3 時 y=5,8,11", "x=1,2,3 時 y=1,4,9", "x=1,2,3 時 y=1,2,4"], "B", "第二組 y 的一階差都是 3，符合固定斜率的一次函數。"),
        ],
    },
    "s-8-1": {
        "lesson": "lesson-math-content-s-8-1",
        "kg": "kg-math-content-s-8-1",
        "title": "角",
        "items": [
            ("一個角的兩邊是什麼幾何元素？", ["兩條不共端點的直線", "兩條有共同端點的射線", "兩條平行線", "一條線段與一個圓"], "B", "角由兩條有共同端點的射線組成，共同端點是頂點。"),
            ("38° 的餘角為何？", ["42°", "52°", "132°", "142°"], "B", "餘角和為 90°，所以 90°−38°=52°。"),
            ("117° 的補角為何？", ["53°", "63°", "73°", "83°"], "B", "補角和為 180°，所以 180°−117°=63°。"),
            ("兩直線相交，其中一個角為 64°，其對頂角為何？", ["26°", "64°", "116°", "128°"], "B", "對頂角相等，因此也是 64°。"),
            ("若兩個角互為鄰補角，其中一角為 125°，另一角為何？", ["45°", "55°", "65°", "75°"], "B", "鄰補角和為 180°，另一角=180°−125°=55°。"),
            ("時鐘分針從 12 走到 3，旋轉的最小角度為何？", ["45°", "60°", "90°", "120°"], "C", "鐘面 12 等分，每格 30°；走 3 格為 90°。"),
            ("若 ∠A=3x、∠B=2x，且兩角互餘，x 為何？", ["15", "18", "20", "30"], "B", "3x+2x=90，5x=90，所以 x=18。"),
            ("一個角大於 90° 且小於 180°，稱為什麼角？", ["銳角", "直角", "鈍角", "周角"], "C", "介於 90° 與 180° 的角是鈍角。"),
            ("兩條互相垂直的直線形成的每一個角是多少度？", ["45°", "90°", "180°", "360°"], "B", "垂直線形成直角，每角為 90°。"),
            ("一個周角的角度是多少？", ["90°", "180°", "270°", "360°"], "D", "繞一點旋轉一周形成周角，角度為 360°。"),
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
        "updatedAt": "2026-08-28",
        "lessonId": config["lesson"],
    }


def main():
    count = 0
    for unit, config in UNITS.items():
        for index, item in enumerate(config["items"], start=1):
            path = QUESTION_DIR / f"question-math-content-{unit}-{index}.json"
            path.write_text(json.dumps(build_question(unit, index, item), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            count += 1
    print(f"replaced {count} function/angle template questions")


if __name__ == "__main__":
    main()
