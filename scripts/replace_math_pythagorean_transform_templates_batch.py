#!/usr/bin/env python3
"""Replace repeated templates for Pythagorean theorem and transformations."""

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
    "s-8-6": {
        "lesson": "lesson-math-content-s-8-6",
        "kg": "kg-math-content-s-8-6",
        "title": "畢氏定理",
        "items": [
            ("直角三角形兩股長為 5、12，斜邊長為何？", ["11", "12", "13", "17"], "C", "斜邊=√(5²+12²)=√169=13。"),
            ("直角三角形斜邊 15、一股 9，另一股為何？", ["6", "8", "10", "12"], "B", "另一股=√(15²−9²)=√144=12；因此應選 12。"),
            ("邊長 6、8、10 的三角形屬於哪一種？", ["銳角三角形", "直角三角形", "鈍角三角形", "無法形成三角形"], "B", "6²+8²=10²，符合畢氏定理，為直角三角形。"),
            ("長方形長 9、寬 12 公分，其對角線長為何？", ["15", "18", "21", "24"], "A", "對角線=√(9²+12²)=15 公分。"),
            ("梯子底端離牆 5 公尺、頂端高 12 公尺，梯長為何？", ["10 公尺", "12 公尺", "13 公尺", "17 公尺"], "C", "梯長是斜邊，√(5²+12²)=13 公尺。"),
            ("等腰直角三角形兩股各為 4 公分，斜邊為何？", ["4", "4√2", "8", "16"], "B", "斜邊=√(4²+4²)=4√2 公分。"),
            ("若三角形三邊為 7、24、25，最大角為何？", ["銳角", "直角", "鈍角", "無法判斷"], "B", "7²+24²=25²，最大邊所對角為直角。"),
            ("坐標平面上 A(－1,2)、B(5,10)，兩點距離為何？", ["8", "10", "12", "14"], "B", "距離=√(6²+8²)=10。"),
            ("正方形邊長 6 公分，其對角線長為何？", ["6", "6√2", "12", "36"], "B", "對角線=√(6²+6²)=6√2 公分。"),
            ("若直角三角形斜邊為 17、一股為 8，另一股為何？", ["9", "12", "15", "16"], "C", "另一股=√(17²−8²)=√225=15。"),
        ],
    },
    "s-7-4": {
        "lesson": "lesson-math-content-s-7-4",
        "kg": "kg-math-content-s-7-4",
        "title": "平移、旋轉與鏡射",
        "items": [
            ("點 A(2,3) 向右平移 4 單位後坐標為何？", ["(2,7)", "(6,3)", "(－2,3)", "(6,7)"], "B", "向右只增加 x 坐標，A'=(2+4,3)=(6,3)。"),
            ("點 P(－1,5) 對 x 軸鏡射後坐標為何？", ["(1,5)", "(－1,－5)", "(1,－5)", "(－5,－1)"], "B", "對 x 軸鏡射使 y 坐標變號，得 (−1,−5)。"),
            ("點 Q(3,－2) 對 y 軸鏡射後坐標為何？", ["(3,2)", "(－3,－2)", "(－3,2)", "(2,－3)"], "B", "對 y 軸鏡射使 x 坐標變號，得 (−3,−2)。"),
            ("點 R(4,1) 繞原點旋轉 180° 後坐標為何？", ["(－4,1)", "(4,－1)", "(－4,－1)", "(1,4)"], "C", "繞原點旋轉 180° 時 (x,y)→(−x,−y)，得 (−4,−1)。"),
            ("下列哪一種變換會保持圖形的面積與邊長？", ["平移", "只沿 x 軸拉長", "不等比例縮放", "投影"], "A", "平移是剛性變換，面積、邊長與角度都保持不變。"),
            ("三角形經鏡射後，鏡射前後的對應角有何關係？", ["相等", "互為補角", "必差 90°", "無法比較"], "A", "鏡射保持距離與角度，對應角相等。"),
            ("將圖形向上平移 3 單位，坐標變化為何？", ["x 加 3", "y 加 3", "x、y 都加 3", "x、y 都減 3"], "B", "向上平移只增加 y 坐標 3。"),
            ("矩形經旋轉 90° 後，哪項一定保持不變？", ["每個頂點的坐標", "長與寬的數值及面積", "每個點到 x 軸距離", "圖形在第一象限"], "B", "旋轉保持長度與面積，雖然坐標與位置可能改變。"),
            ("點 S(－2,4) 先對 x 軸鏡射，再向右平移 3 單位，結果為何？", ["(1,－4)", "(－5,4)", "(1,4)", "(－2,7)"], "A", "先得 (−2,−4)，再增加 x 3，結果為 (1,−4)。"),
            ("若圖形經平移後與原圖形完全重合，平移前後兩圖形的關係為何？", ["全等", "只有面積相等", "一定相似但不全等", "必互相垂直"], "A", "平移保留形狀與大小，前後圖形全等。"),
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
    print(f"replaced {count} Pythagorean/transformation template questions")


if __name__ == "__main__":
    main()
