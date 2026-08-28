#!/usr/bin/env python3
"""Replace the s-IV-5 line-symmetry questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-5"
KG_ID = "kg-math-performance-s-iv-5"
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
        "prompt": "點 P(4, 1) 對直線 x＝2 作鏡射後，像 P′ 的坐標為何？",
        "options": ["(0, 1)", "(−4, 1)", "(4, −1)", "(2, 1)"],
        "answer": "A",
        "explanation": "點到對稱軸 x＝2 的水平距離為 2，鏡射後位於 x＝0，y 不變，所以 P′＝(0,1)。",
    },
    {
        "prompt": "點 A(3, −2) 對 x 軸作鏡射後，像 A′ 的坐標為何？",
        "options": ["(−3, −2)", "(3, 2)", "(−3, 2)", "(2, 3)"],
        "answer": "B",
        "explanation": "對 x 軸鏡射時 x 坐標不變、y 坐標變號，因此 (3,−2) 變為 (3,2)。",
    },
    {
        "prompt": "點 B(−2, 5) 對 y 軸作鏡射後，像 B′ 的坐標為何？",
        "options": ["(−2, −5)", "(2, 5)", "(2, −5)", "(5, −2)"],
        "answer": "B",
        "explanation": "對 y 軸鏡射時 x 坐標變號、y 坐標不變，所以 (−2,5) 變為 (2,5)。",
    },
    {
        "prompt": "圖形沿某一直線對摺後兩半完全重合，這條直線稱為什麼？",
        "options": ["平行線", "對稱軸", "中線段", "切線"],
        "answer": "B",
        "explanation": "能使圖形對摺後完全重合的直線稱為對稱軸，這是線對稱的定義。",
    },
    {
        "prompt": "等邊三角形有幾條對稱軸？",
        "options": ["1 條", "2 條", "3 條", "6 條"],
        "answer": "C",
        "explanation": "等邊三角形從每個頂點向對邊中點的直線都是對稱軸，共有 3 條。",
    },
    {
        "prompt": "一般矩形（不是正方形）有幾條對稱軸？",
        "options": ["1 條", "2 條", "3 條", "4 條"],
        "answer": "B",
        "explanation": "一般矩形沿水平、垂直方向通過中心的兩條直線對摺會重合；對角線不是對稱軸，因此共有 2 條。",
    },
    {
        "prompt": "若點 Q 在某圖形的對稱軸上，Q 經對稱變換後的位置為何？",
        "options": ["一定移到對稱軸另一側", "仍是 Q 本身", "一定移到原點", "無法判斷且不可能固定"],
        "answer": "B",
        "explanation": "對稱軸上的點到軸的距離為 0，鏡射後不移動，所以像仍是 Q 本身。",
    },
    {
        "prompt": "點 C(3, −4) 對直線 x＝3 作鏡射後，像 C′ 的坐標為何？",
        "options": ["(−3, −4)", "(3, 4)", "(3, −4)", "(−3, 4)"],
        "answer": "C",
        "explanation": "C 的 x 坐標正好等於對稱軸 x＝3，C 位於對稱軸上，因此鏡射後仍為 (3,−4)。",
    },
    {
        "prompt": "點 D(3, −1) 對直線 y＝x 作鏡射後，像 D′ 的坐標為何？",
        "options": ["(−3, 1)", "(−1, 3)", "(1, −3)", "(3, 1)"],
        "answer": "B",
        "explanation": "對 y＝x 鏡射會交換 x、y 坐標，因此 (3,−1) 變為 (−1,3)。",
    },
    {
        "prompt": "點 E(1, 2) 與點 E′(−1, 2) 關於哪一條坐標軸互為對稱點？",
        "options": ["x 軸", "y 軸", "直線 y＝x", "直線 y＝−x"],
        "answer": "B",
        "explanation": "兩點的 y 坐標相同、x 坐標互為相反數，故關於 y 軸對稱。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-5-{index}",
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
                "參考線對稱、對稱軸與坐標鏡射題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-5-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
