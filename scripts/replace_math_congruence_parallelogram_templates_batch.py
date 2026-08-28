#!/usr/bin/env python3
"""Replace repeated templates for congruent figures and parallelograms."""

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
    "s-8-4": {
        "lesson": "lesson-math-content-s-8-4",
        "kg": "kg-math-content-s-8-4",
        "title": "全等圖形",
        "items": [
            ("兩個圖形能完全重合，則兩圖形的關係為何？", ["相似", "全等", "平行", "對稱但大小必不同"], "B", "能完全重合表示形狀與大小都相同，兩圖形全等。"),
            ("全等圖形的對應邊有何關係？", ["相等", "互為倒數", "只差一倍", "必互相垂直"], "A", "全等圖形的對應邊長相等。"),
            ("一個三角形經旋轉 90° 後得到另一個圖形，旋轉前後的面積關係為何？", ["前者較大", "後者較大", "兩者相等", "無法判斷"], "C", "旋轉是剛性變換，不改變面積，因此兩者面積相等。"),
            ("若矩形甲長 8、寬 5，矩形乙與甲全等，乙的周長為何？", ["13", "26", "40", "80"], "B", "全等矩形邊長相同，周長=2×(8+5)=26。"),
            ("兩個全等三角形的對應角分別為 42°、73°、65°，其中一個三角形的第三角為何？", ["42°", "65°", "73°", "180°"], "B", "對應角相等，第三角為 65°。"),
            ("下列哪一種變換一定保持圖形的邊長與角度？", ["平移", "任意放大", "單方向拉伸", "投影縮小"], "A", "平移是剛性變換，保留邊長與角度。"),
            ("若兩個正方形邊長分別為 6 與 6 公分，且方向不同，兩正方形可判定為何？", ["全等", "一定不相似", "面積不同", "無法比較任何性質"], "A", "正方形邊長相同即形狀與大小相同，方向不同仍可全等。"),
            ("判定兩三角形全等時，『兩邊及夾角相等』對應哪種判定？", ["SSS", "SAS", "ASA", "AA"], "B", "兩邊及其夾角相等是 SAS 全等判定。"),
            ("兩個全等圖形的周長比為何？", ["1：2", "2：1", "1：1", "依圖形顏色決定"], "C", "全等圖形所有對應長度相等，周長比為 1：1。"),
            ("若圖形甲平移後完全重合於圖形乙，哪項必成立？", ["甲乙面積相等", "乙比甲大兩倍", "甲乙一定互相垂直", "只能知道位置不同"], "A", "平移不改變圖形大小，兩圖形面積相等。"),
        ],
    },
    "s-8-9": {
        "lesson": "lesson-math-content-s-8-9",
        "kg": "kg-math-content-s-8-9",
        "title": "平行四邊形的基本性質",
        "items": [
            ("平行四邊形的兩組對邊有何關係？", ["分別平行且等長", "必互相垂直", "只有一組等長", "四邊都不相等"], "A", "平行四邊形的兩組對邊分別平行且相等。"),
            ("平行四邊形一個內角為 65°，其相鄰內角為何？", ["65°", "90°", "115°", "130°"], "C", "相鄰內角互補，180°−65°=115°。"),
            ("平行四邊形一個內角為 72°，其對角為何？", ["36°", "72°", "108°", "144°"], "B", "平行四邊形對角相等，所以為 72°。"),
            ("平行四邊形兩鄰邊長為 7、11 公分，周長為何？", ["18", "36", "77", "121"], "B", "周長=2×(7+11)=36 公分。"),
            ("平行四邊形底 9 公分、高 4 公分，面積為何？", ["13", "18", "36", "72"], "C", "面積=底×高=9×4=36 平方公分。"),
            ("平行四邊形的兩條對角線相交於 O，則 O 對每條對角線有何作用？", ["平分對角線", "使對角線垂直且等長", "只平分一條", "不在對角線上"], "A", "平行四邊形的對角線互相平分。"),
            ("若平行四邊形 ABCD 中 AB=13，則 CD 為何？", ["6.5", "13", "26", "無法判斷"], "B", "對邊相等，CD=AB=13。"),
            ("平行四邊形的面積若底固定為 12，高由 3 增為 5，面積增加多少？", ["2", "12", "24", "60"], "C", "面積增加=12×(5−3)=24 平方單位。"),
            ("若四邊形的兩組對邊分別平行，最合理的判定是什麼？", ["它是平行四邊形", "它必是正方形", "它必是梯形但非平行四邊形", "無法判定"], "A", "兩組對邊分別平行符合平行四邊形定義。"),
            ("平行四邊形可分割成兩個三角形，若其中一個三角形面積為 18，整個平行四邊形面積為何？", ["9", "18", "36", "54"], "C", "對角線將平行四邊形分成兩個等面積三角形，總面積=2×18=36。"),
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
    print(f"replaced {count} congruence/parallelogram template questions")


if __name__ == "__main__":
    main()
