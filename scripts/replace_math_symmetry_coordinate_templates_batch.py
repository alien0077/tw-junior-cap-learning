#!/usr/bin/env python3
"""Replace repeated templates for line symmetry and the coordinate plane."""

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
    "s-7-5": {
        "lesson": "lesson-math-content-s-7-5",
        "kg": "kg-math-content-s-7-5",
        "title": "線對稱的基本圖形",
        "items": [
            ("圖形關於某直線鏡射後能與原圖形完全重合，這條直線稱為什麼？", ["對稱軸", "對角線", "中線", "切線"], "A", "能使圖形鏡射後重合的直線稱為對稱軸。"),
            ("點 P 到對稱軸 l 的垂直距離為 4 公分，其對稱點 P' 到 l 的距離為何？", ["2 公分", "4 公分", "8 公分", "無法判斷"], "B", "鏡射前後兩點到對稱軸的垂直距離相等，仍為 4 公分。"),
            ("點 A(－4,3) 對 y 軸鏡射後的坐標為何？", ["(－4,－3)", "(4,3)", "(4,－3)", "(－3,4)"], "B", "對 y 軸鏡射使 x 坐標變號，得 (4,3)。"),
            ("正方形共有幾條對稱軸？", ["1", "2", "4", "8"], "C", "正方形有兩條中線與兩條對角線，共 4 條對稱軸。"),
            ("一般非正方形的長方形有幾條對稱軸？", ["1", "2", "3", "4"], "B", "長方形的兩條中線是對稱軸，對角線通常不是，共 2 條。"),
            ("等邊三角形有幾條對稱軸？", ["1", "2", "3", "6"], "C", "每個頂點到對邊中點的線都是對稱軸，共 3 條。"),
            ("對稱軸上的點經關於該軸鏡射後有何變化？", ["移到軸外", "位置不變", "坐標都變號", "距離加倍"], "B", "對稱軸上的點到軸距離為 0，鏡射後仍在原位置。"),
            ("點 B(－5,4) 對 x 軸鏡射後的坐標為何？", ["(5,4)", "(－5,－4)", "(5,－4)", "(4,－5)"], "B", "對 x 軸鏡射使 y 坐標變號，得 (−5,−4)。"),
            ("鏡射變換一定保持哪項量不變？", ["點到原點的方向", "任兩點間距離", "每點的坐標", "所在象限"], "B", "鏡射是剛性變換，保持任兩點間距離。"),
            ("若一圖形只有一條對稱軸，圖形上不在對稱軸的點通常會對應到什麼？", ["另一個關於軸對稱的點", "同一點但坐標加倍", "原點", "圓心"], "A", "不在軸上的點會對應到軸另一側、距軸等距的鏡射點。"),
        ],
    },
    "g-7-1": {
        "lesson": "lesson-math-content-g-7-1",
        "kg": "kg-math-content-g-7-1",
        "title": "平面直角坐標系",
        "items": [
            ("有序數對 (－2,5) 中，第一個數代表哪一個坐標？", ["x 坐標", "y 坐標", "距離", "象限編號"], "A", "有序數對 (x,y) 中第一個數是 x 坐標。"),
            ("點 P(4,－3) 位於哪一個象限？", ["第一象限", "第二象限", "第三象限", "第四象限"], "D", "x>0 且 y<0，故 P 位於第四象限。"),
            ("坐標原點的坐標為何？", ["(1,1)", "(0,1)", "(1,0)", "(0,0)"], "D", "x 軸與 y 軸交點為原點，坐標是 (0,0)。"),
            ("點 A(－3,0) 位於哪條坐標軸上？", ["x 軸", "y 軸", "兩軸交點", "不在坐標系上"], "A", "y=0 的點位於 x 軸上。"),
            ("點 B(0,7) 到 x 軸的距離為何？", ["0", "7", "14", "49"], "B", "到 x 軸距離為 |y|=7。"),
            ("點 C(－2,6) 與 D(5,6) 的連線方向為何？", ["水平", "鉛直", "斜向且必垂直", "無法判斷"], "A", "兩點 y 坐標相同，連線為水平線。"),
            ("在坐標平面上向右移動 3 單位，哪個坐標改變？", ["x 增加 3", "y 增加 3", "x 減少 3", "x、y 都增加 3"], "A", "向右只使 x 坐標增加 3。"),
            ("點 E(－4,－1) 的 x、y 坐標符號分別為何？", ["正、正", "正、負", "負、正", "負、負"], "D", "x=−4、y=−1，兩者皆為負。"),
            ("點 F(2,3) 與 G(2,－4) 的垂直距離為何？", ["1", "5", "7", "9"], "C", "兩點 x 相同，垂直距離=|3−(−4)|=7。"),
            ("若點 H 在第二象限，則其坐標符號必為何？", ["x>0、y>0", "x<0、y>0", "x<0、y<0", "x>0、y<0"], "B", "第二象限的 x 負、y 正。"),
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
    print(f"replaced {count} symmetry/coordinate template questions")


if __name__ == "__main__":
    main()
