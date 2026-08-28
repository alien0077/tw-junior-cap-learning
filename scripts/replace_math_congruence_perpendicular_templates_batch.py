#!/usr/bin/env python3
"""Replace repeated congruence and perpendicular-geometry templates."""

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
    "s-8-5": {
        "lesson": "lesson-math-content-s-8-5",
        "kg": "kg-math-content-s-8-5",
        "title": "三角形的全等性質",
        "items": [
            ("兩三角形的三組對應邊分別相等，應使用哪種全等判定？", ["SSS", "SAS", "ASA", "AA"], "A", "三組對應邊相等符合 SSS 全等判定。"),
            ("兩三角形有兩邊及其夾角分別相等，應使用哪種全等判定？", ["AA", "SSS", "SAS", "SSA"], "C", "兩邊及夾角相等符合 SAS 全等判定。"),
            ("若 △ABC≅△DEF，且 A↔D、B↔E、C↔F，AB=8，則 DE 為何？", ["4", "8", "16", "無法判斷"], "B", "全等三角形的對應邊相等，DE=AB=8。"),
            ("兩三角形有一邊及其兩端角分別相等，應使用哪種判定？", ["SSS", "SAS", "ASA", "只有一邊相等即可"], "C", "一邊及其兩端角相等符合 ASA 全等判定。"),
            ("全等三角形的對應角有何關係？", ["必互為餘角", "必相等", "總和必為 180°", "只差一倍"], "B", "全等圖形的對應角相等。"),
            ("若一個三角形經平移後得到另一個三角形，兩者的關係為何？", ["一定相似但不全等", "必定全等", "必定面積不同", "無法判斷"], "B", "平移是剛性變換，保留長度與角度，因此圖形全等。"),
            ("直角三角形兩股分別為 6、8，另一個直角三角形斜邊為 10 且一股為 6，依何條件可判定全等？", ["AA", "HL（斜邊直角邊）", "只有一角相等", "面積相等"], "B", "兩直角三角形斜邊及一股相等，符合 HL 判定。"),
            ("若 △ABC≅△PQR，且 ∠A=47°、∠B=68°，則 ∠R 為何？", ["47°", "65°", "68°", "115°"], "B", "∠C=180°−47°−68°=65°，C 對應 R。"),
            ("下列哪項資料不足以單獨判定兩三角形全等？", ["三組對應邊相等", "兩邊及夾角相等", "兩角及一邊相等", "只有一組對應邊相等"], "D", "只有一組對應邊相等，無法確定三角形形狀與大小。"),
            ("若兩個三角形全等，其中一個面積為 24 平方公分，另一個面積為何？", ["12", "24", "48", "需知道周長"], "B", "全等圖形大小相同，面積也相等，為 24 平方公分。"),
        ],
    },
    "s-7-3": {
        "lesson": "lesson-math-content-s-7-3",
        "kg": "kg-math-content-s-7-3",
        "title": "垂直",
        "items": [
            ("兩條直線相交形成的四個角都是 90°，這兩條直線的關係為何？", ["平行", "垂直", "重合", "歪斜"], "B", "相交成直角的兩直線互相垂直。"),
            ("斜率為 2 的直線，其垂線斜率為何？", ["－2", "－1/2", "1/2", "2"], "B", "非水平或鉛直線的垂線斜率為負倒數，故為 −1/2。"),
            ("點 P(3,－2) 到 x 軸的垂直距離為何？", ["1", "2", "3", "5"], "B", "到 x 軸的距離為 y 坐標絕對值 |−2|=2。"),
            ("點 Q(－4,5) 到 y 軸的垂直距離為何？", ["4", "5", "9", "20"], "A", "到 y 軸的距離為 x 坐標絕對值 |−4|=4。"),
            ("直線 y=3x+1 與哪條直線垂直？", ["y=3x−4", "y=−1/3x+2", "y=1/3x+2", "y=−3x+2"], "B", "垂直線斜率為 3 的負倒數 −1/3。"),
            ("線段 AB 的垂直平分線上任一點 P，必滿足哪項？", ["PA=PB", "PA+PB=AB", "P 在 AB 上", "∠APB=90°"], "A", "垂直平分線上的點到線段兩端等距。"),
            ("若兩條直線的斜率乘積為 −1，且兩者皆非鉛直線，則兩直線關係為何？", ["平行", "垂直", "重合", "必相交於 y 軸"], "B", "斜率乘積為 −1 是兩非鉛直直線互相垂直的判定。"),
            ("通過點 (2,1) 且與 x 軸垂直的直線方程式為何？", ["y=2", "x=2", "y=x+1", "x=1"], "B", "與 x 軸垂直的直線是鉛直線，固定 x=2。"),
            ("若直線 l 與平面圖上的直線 m 垂直，兩線交點處的夾角為何？", ["0°", "45°", "90°", "180°"], "C", "垂直直線的交角定義為 90°。"),
            ("兩條直線都垂直於同一直線，且位於同一平面，則兩條直線彼此為何？", ["垂直", "平行或重合", "必相交", "歪斜"], "B", "同平面內垂直於同一直線的兩線平行或重合。"),
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
    print(f"replaced {count} congruence/perpendicular template questions")


if __name__ == "__main__":
    main()
