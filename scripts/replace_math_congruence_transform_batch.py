#!/usr/bin/env python3
"""Replace the s-IV-4 congruence and transformation questions with originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-4"
KG_ID = "kg-math-performance-s-iv-4"
SOURCE_URL = (
    "https://www.yacjh.kh.edu.tw/upload/221/101_30637/"
    "114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83"
    "%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
)


def rotate_options(options, answer_letter):
    answer_index = ord(answer_letter) - ord("A")
    shift = (4 - answer_index) % 4
    rotated = options[shift:] + options[:shift]
    return [{"id": chr(ord("A") + i), "text": text} for i, text in enumerate(rotated)]


QUESTIONS = [
    {
        "prompt": "點 P(1, 4) 向右平移 3 單位、向下平移 2 單位後，坐標為何？",
        "options": ["(4, 2)", "(4, 6)", "(−2, 2)", "(−2, 6)"],
        "answer": "A",
        "explanation": "向右 3 使 x 變為 1＋3＝4，向下 2 使 y 變為 4−2＝2，所以新點為 (4,2)。",
    },
    {
        "prompt": "點 A(2, −5) 對 x 軸作鏡射後，像 A′ 的坐標為何？",
        "options": ["(−2, −5)", "(2, 5)", "(−2, 5)", "(5, 2)"],
        "answer": "B",
        "explanation": "對 x 軸鏡射時 x 不變、y 變號，因此 (2,−5) 變為 (2,5)。",
    },
    {
        "prompt": "點 B(−3, 4) 對 y 軸作鏡射後，像 B′ 的坐標為何？",
        "options": ["(−3, −4)", "(3, 4)", "(3, −4)", "(4, 3)"],
        "answer": "B",
        "explanation": "對 y 軸鏡射時 x 變號、y 不變，因此 (−3,4) 變為 (3,4)。",
    },
    {
        "prompt": "點 C(5, −2) 對原點作中心對稱後，像 C′ 的坐標為何？",
        "options": ["(5, 2)", "(−5, −2)", "(−5, 2)", "(2, −5)"],
        "answer": "C",
        "explanation": "對原點中心對稱時兩個坐標都變號，故 (5,−2) 變為 (−5,2)。",
    },
    {
        "prompt": "點 D(2, 1) 以原點為中心逆時針旋轉 90° 後，像 D′ 的坐標為何？",
        "options": ["(1, −2)", "(−1, 2)", "(−2, −1)", "(2, −1)"],
        "answer": "B",
        "explanation": "逆時針旋轉 90° 的坐標規則為 (x,y)→(−y,x)，所以 (2,1)→(−1,2)。",
    },
    {
        "prompt": "平移、旋轉與鏡射都屬於平面上的剛性變換，下列哪一項一定保持不變？",
        "options": ["圖形在坐標平面的位置", "圖形的面積與邊長", "每個點的坐標數值", "圖形朝向一定不變"],
        "answer": "B",
        "explanation": "剛性變換保持距離、角度與面積；位置和坐標會改變，鏡射也可能改變圖形朝向。",
    },
    {
        "prompt": "三角形 ABC 平移後得到 A′B′C′。若 AB＝7 公分，則 A′B′ 為多少？",
        "options": ["3.5 公分", "7 公分", "14 公分", "無法判定"],
        "answer": "B",
        "explanation": "平移是剛性變換，會保留對應邊長，因此 A′B′＝AB＝7 公分。",
    },
    {
        "prompt": "點 E(3, −1) 對直線 y＝x 作鏡射後，像 E′ 的坐標為何？",
        "options": ["(−3, 1)", "(1, −3)", "(−1, 3)", "(3, 1)"],
        "answer": "C",
        "explanation": "對 y＝x 鏡射會交換 x、y 坐標，(3,−1) 變為 (−1,3)。",
    },
    {
        "prompt": "點 F(4, −3) 以原點為中心旋轉 180° 後，像 F′ 的坐標為何？",
        "options": ["(−4, 3)", "(4, 3)", "(−3, 4)", "(3, −4)"],
        "answer": "A",
        "explanation": "繞原點旋轉 180° 的規則為 (x,y)→(−x,−y)，所以 (4,−3)→(−4,3)。",
    },
    {
        "prompt": "兩個圖形若能透過平移、旋轉或鏡射完全重合，則它們一定是什麼關係？",
        "options": ["相似但不全等", "全等", "只有面積相等", "只有周長相等"],
        "answer": "B",
        "explanation": "剛性變換不改變邊長與角度，能完全重合的兩個圖形符合全等的定義。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-4-{index}",
        "subject": "math",
        "type": "single-choice",
        "prompt": item["prompt"],
        "options": rotate_options(item["options"], item["answer"]),
        "knowledgeIds": [KG_ID],
        "difficulty": "medium",
        "answer": {"value": item["answer"], "explanation": item["explanation"]},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE_URL,
            "sourceLocator": (
                "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；"
                "參考全等、平移、旋轉與鏡射的坐標變換及性質題型"
            ),
            "authoringNote": (
                "Substantive rewrite with new values, contexts, options, and explanations; "
                "no reproduction of public-exam wording, figures, or answer key. "
                "待第二輪 AI／Terra 內容複核。"
            ),
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }


def main():
    for index, item in enumerate(QUESTIONS, start=1):
        path = QUESTION_DIR / f"question-math-performance-s-iv-4-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
