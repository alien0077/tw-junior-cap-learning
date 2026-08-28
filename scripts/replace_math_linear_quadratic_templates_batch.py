#!/usr/bin/env python3
"""Replace repeated templates for linear and quadratic functions."""

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
    "f-8-1": {
        "lesson": "lesson-math-content-f-8-1",
        "kg": "kg-math-content-f-8-1",
        "title": "一次函數",
        "items": [
            ("下列哪個關係是一次函數？", ["y=2x+3", "y=x²+1", "y=1/x", "xy=4"], "A", "一次函數可寫成 y=ax+b 且 a、b 為常數，y=2x+3 符合。"),
            ("若 y=－4x+7，當 x=2 時 y 為何？", ["－1", "－8", "1", "15"], "A", "代入得 y=−4×2+7=−1。"),
            ("直線 y=5x−2 的斜率與截距分別為何？", ["5、－2", "－2、5", "5、2", "－5、2"], "A", "y=mx+b 中 m=5、b=−2。"),
            ("若一次函數通過 (0,6) 與 (3,12)，其斜率為何？", ["1", "2", "3", "6"], "B", "斜率=(12−6)/(3−0)=2。"),
            ("下表 x=0,1,2 時 y=－3,0,3，符合哪個函數？", ["y=3x−3", "y=−3x−3", "y=3x+3", "y=x−3"], "A", "每增加 1，y 增加 3，且截距 −3，所以 y=3x−3。"),
            ("若兩條一次函數圖形斜率相等、截距也相等，兩圖形的關係為何？", ["平行不重合", "重合", "互相垂直", "只交於一點"], "B", "斜率與截距都相同，代表是同一條直線，圖形重合。"),
            ("一次函數 y=8 的圖形有何特徵？", ["水平線", "鉛直線", "通過原點的斜線", "圓"], "A", "y 值固定為 8，圖形是水平線。"),
            ("若函數 y=ax+4 通過點 (2,10)，a 為何？", ["2", "3", "4", "5"], "B", "10=2a+4，得 2a=6，所以 a=3。"),
            ("某水箱原有 20 公升，每分鐘流入 3 公升，t 分鐘後水量 V 為何？", ["V=20t+3", "V=3t+20", "V=17t", "V=60t"], "B", "初始量是截距 20，每分鐘增加 3，故 V=3t+20。"),
            ("一次函數斜率為負時，x 增加會使 y 如何變化？", ["增加", "減少", "保持不變", "先增後減"], "B", "斜率為負代表 x 增加時 y 會減少。"),
        ],
    },
    "f-9-1": {
        "lesson": "lesson-math-content-f-9-1",
        "kg": "kg-math-content-f-9-1",
        "title": "二次函數的意義",
        "items": [
            ("下列哪個式子是二次函數？", ["y=3x+1", "y=x²−4x+2", "y=5/x", "y=7"], "B", "含有 x² 且可寫成 y=ax²+bx+c、a≠0 的式子是二次函數。"),
            ("函數 y=−2x²+5x−1 的二次項係數為何？", ["－2", "5", "－1", "2"], "A", "x² 的係數是 −2。"),
            ("拋物線 y=3x²−2 的開口方向為何？", ["向上", "向下", "向左", "向右"], "A", "二次項係數 3>0，拋物線開口向上。"),
            ("函數 y=(x−4)²+1 的對稱軸為何？", ["x=－4", "x=1", "x=4", "y=4"], "C", "頂點式 y=(x−h)²+k 的對稱軸是 x=h，因此為 x=4。"),
            ("函數 y=(x−2)²+3 的頂點坐標為何？", ["(−2,3)", "(2,3)", "(2,−3)", "(3,2)"], "B", "頂點式直接讀得頂點為 (2,3)。"),
            ("y=x²−6x+8 的對稱軸為何？", ["x=2", "x=3", "x=6", "x=8"], "B", "對稱軸 x=−b/(2a)=6/2=3。"),
            ("函數 y=−(x−1)²+5 的最大值為何？", ["－1", "1", "5", "6"], "C", "開口向下，頂點 y 坐標 5 即為最大值。"),
            ("若二次函數圖形與 x 軸交於 x=2、x=7，則其對稱軸為何？", ["x=2", "x=4.5", "x=5", "x=7"], "B", "兩根中點為 (2+7)/2=4.5，亦為對稱軸。"),
            ("二次函數 y=2x²+4x+1 中，當 x=0 時 y 為何？", ["0", "1", "2", "4"], "B", "代入 x=0，y=1。"),
            ("二次函數圖形的頂點是 (−3,4)，且開口向上，則頂點代表什麼？", ["最大值點", "最小值點", "x 軸截距", "y 軸截距"], "B", "開口向上的拋物線在頂點取得最小值。"),
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
    print(f"replaced {count} linear/quadratic template questions")


if __name__ == "__main__":
    main()
