#!/usr/bin/env python3
"""Replace the s-IV-3 perpendicular and parallel questions with originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-3"
KG_ID = "kg-math-performance-s-iv-3"
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
        "prompt": "直線 y＝2x＋1 與直線 y＝2x−3 的關係為何？",
        "options": ["互相垂直", "互相平行", "完全重合", "沒有共同方向"],
        "answer": "B",
        "explanation": "兩直線斜率都為 2，且截距不同，因此是互相平行的兩條直線。",
    },
    {
        "prompt": "斜率為 3 的直線，若與另一條直線垂直，另一條直線的斜率是多少？",
        "options": ["−3", "−1/3", "1/3", "3"],
        "answer": "B",
        "explanation": "非水平、垂直的兩直線若垂直，斜率乘積為 −1；所以另一斜率為 −1÷3＝−1/3。",
    },
    {
        "prompt": "若直線 L 與 y＝−2x＋5 平行，則直線 L 的斜率為何？",
        "options": ["−5", "−2", "1/2", "2"],
        "answer": "B",
        "explanation": "平行直線的斜率相等，所以 L 的斜率也是 −2。",
    },
    {
        "prompt": "直線 x＝4 與直線 y＝−1 的關係為何？",
        "options": ["互相平行", "互相垂直", "完全重合", "斜率相同但不相交"],
        "answer": "B",
        "explanation": "x＝4 是垂直線，y＝−1 是水平線；垂直線與水平線互相垂直。",
    },
    {
        "prompt": "兩條水平平行線 y＝3 與 y＝−2 之間的距離是多少？",
        "options": ["1", "5", "6", "−5"],
        "answer": "B",
        "explanation": "兩條水平線的距離是 y 座標差的絕對值：|3−(−2)|＝5。",
    },
    {
        "prompt": "通過點 (1, 2) 與 (4, 8) 的直線斜率是多少？",
        "options": ["1", "2", "3", "6"],
        "answer": "B",
        "explanation": "斜率＝(8−2)÷(4−1)＝6÷3＝2。",
    },
    {
        "prompt": "斜率為 −1 且通過 (0, 3) 的直線方程式為何？",
        "options": ["y＝x＋3", "y＝−x＋3", "y＝−x−3", "y＝3x−1"],
        "answer": "B",
        "explanation": "直線式 y＝mx＋b 中 m＝−1；通過 (0,3) 表示截距 b＝3，因此 y＝−x＋3。",
    },
    {
        "prompt": "若兩條相異直線的斜率分別為 1/2 與 −2，則這兩條直線必定如何？",
        "options": ["互相平行", "互相垂直", "完全重合", "都為水平線"],
        "answer": "B",
        "explanation": "兩斜率乘積為 (1/2)×(−2)＝−1，所以兩條直線互相垂直。",
    },
    {
        "prompt": "直線 y＝4x−7 的一條平行線可能是哪一條？",
        "options": ["y＝−4x＋2", "y＝4x＋2", "y＝(1/4)x＋2", "y＝−(1/4)x−7"],
        "answer": "B",
        "explanation": "平行線需有相同斜率 4；y＝4x＋2 與原直線截距不同，所以是平行線。",
    },
    {
        "prompt": "在坐標平面上，線段 AB 的端點為 A(−2, 5)、B(3, 5)，AB 的方向為何？",
        "options": ["水平，且長度為 5", "垂直，且長度為 5", "水平，且長度為 7", "垂直，且長度為 7"],
        "answer": "A",
        "explanation": "兩端點 y 座標相同，所以 AB 為水平線段；長度為 |3−(−2)|＝5。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-3-{index}",
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
                "參考垂直、平行、斜率與坐標幾何題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-3-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
