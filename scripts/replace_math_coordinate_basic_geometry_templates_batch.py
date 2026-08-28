#!/usr/bin/env python3
"""Replace repeated templates for coordinate geometry and basic symbols."""

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
    "g": {
        "lesson": "lesson-math-content-g",
        "kg": "kg-math-content-g",
        "title": "坐標幾何",
        "items": [
            ("點 A(2,3) 與 B(7,3) 的水平距離為何？", ["3", "5", "7", "10"], "B", "兩點 y 坐標相同，距離為 |7−2|=5。"),
            ("直線 y=－2x+5 的斜率為何？", ["－5", "－2", "2", "5"], "B", "直線式 y=mx+b 中 x 的係數 m 即為斜率，故為 −2。"),
            ("點 P(－3,4) 關於原點的對稱點為何？", ["(3,4)", "(－3,－4)", "(3,－4)", "(4,－3)"], "C", "關於原點對稱時 x、y 坐標同時變號，得 (3,−4)。"),
            ("兩點 (1,2)、(5,10) 所在直線的斜率為何？", ["1", "2", "4", "8"], "B", "斜率=(10−2)/(5−1)=8/4=2。"),
            ("矩形四頂點為 (0,0)、(6,0)、(6,4)、(0,4)，其面積為何？", ["10", "20", "24", "48"], "C", "長 6、寬 4，面積=6×4=24。"),
            ("直線 y=3x−7 與 y 軸的截距為何？", ["－7", "－3", "3", "7"], "A", "令 x=0，y=−7，因此 y 截距為 −7。"),
            ("點 A(－2,1)、B(4,7) 的中點坐標為何？", ["(1,4)", "(2,3)", "(3,4)", "(1,3)"], "A", "中點=((−2+4)/2,(1+7)/2)=(1,4)。"),
            ("若一條直線斜率為 0，這條直線的圖形有何特徵？", ["水平線", "鉛直線", "必通過原點", "與 x 軸垂直"], "A", "斜率為 0 表示 y 值固定，是水平線。"),
            ("點 (3,4) 到原點的距離為何？", ["4", "5", "7", "12"], "B", "距離=√(3²+4²)=5。"),
            ("若兩條非鉛直直線斜率相等且截距不同，則兩線為何？", ["平行不重合", "互相垂直", "重合", "必交於原點"], "A", "斜率相同、截距不同代表兩條平行且不重合的直線。"),
        ],
    },
    "s-7-1": {
        "lesson": "lesson-math-content-s-7-1",
        "kg": "kg-math-content-s-7-1",
        "title": "簡單圖形與幾何符號",
        "items": [
            ("幾何中的點通常用什麼表示？", ["大寫英文字母", "小寫希臘字母只限角", "一個方程式", "一段數值"], "A", "幾何中的點通常以大寫英文字母命名，例如點 A。"),
            ("通過兩點 A、B 的直線，通常記作什麼？", ["線段 AB", "直線 AB", "射線 AB", "角 AB"], "B", "兩點決定一條直線，記作直線 AB。"),
            ("射線 AB 的端點與方向為何？", ["端點 B，經過 A", "端點 A，經過 B 延伸", "沒有端點", "兩端都固定"], "B", "射線 AB 以 A 為端點，經過 B 向一側無限延伸。"),
            ("線段 AB 的長度為 9 公分，則 BA 長度為何？", ["－9 公分", "4.5 公分", "9 公分", "18 公分"], "C", "同一線段反向命名不改變長度，BA=AB=9 公分。"),
            ("若 ∠ABC 的頂點是哪一點？", ["A", "B", "C", "無法判斷"], "B", "角的命名中間字母代表頂點，所以頂點是 B。"),
            ("兩條線段長度分別為 5、8 公分，哪項可判定它們不全等？", ["方向不同", "長度不同", "位置不同", "顏色不同"], "B", "全等需對應長度相等，5 與 8 不同即可判定不全等。"),
            ("以 A 為端點、經過 B 向外無限延伸的圖形稱為什麼？", ["線段 AB", "射線 AB", "直線 AB", "角 ABC"], "B", "以 A 為端點並經過 B 向一側無限延伸的是射線 AB。"),
            ("若兩條線段有共同端點且形成 90°，這兩線段的關係為何？", ["平行", "垂直", "重合", "相等但不相交"], "B", "相交形成直角的線段所在直線互相垂直。"),
            ("三點 A、B、C 不共線時，能形成哪一種基本圖形？", ["三角形", "一條直線", "一個點", "兩條平行線"], "A", "三個不共線點互相連結可形成三角形。"),
            ("若點 M 在線段 AB 上且 AM=4、MB=6，則 AB 為何？", ["2", "6", "10", "24"], "C", "M 在 AB 上，AB=AM+MB=4+6=10。"),
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
    print(f"replaced {count} coordinate/basic geometry template questions")


if __name__ == "__main__":
    main()
