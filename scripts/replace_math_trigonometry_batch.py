#!/usr/bin/env python3
"""Replace the s-IV-12 trigonometry questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-12"
KG_ID = "kg-math-performance-s-iv-12"
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
        "prompt": "sin 30° 的值是多少？",
        "options": ["1/2", "√2/2", "√3/2", "1"],
        "answer": "A",
        "explanation": "由 30°−60°−90° 三角形的邊長比，sin 30°＝對邊／斜邊＝1/2。",
    },
    {
        "prompt": "cos 60° 的值是多少？",
        "options": ["0", "1/2", "√2/2", "√3/2"],
        "answer": "B",
        "explanation": "cos 60°＝鄰邊／斜邊；在特殊直角三角形中比值為 1/2。",
    },
    {
        "prompt": "tan 45° 的值是多少？",
        "options": ["0", "1/2", "1", "√3"],
        "answer": "C",
        "explanation": "45°−45°−90° 三角形的兩股等長，所以 tan 45°＝對邊／鄰邊＝1。",
    },
    {
        "prompt": "直角三角形中，某銳角 θ 的對邊長 6 公分、斜邊長 10 公分，sin θ 為何？",
        "options": ["3/5", "4/5", "5/3", "5/4"],
        "answer": "A",
        "explanation": "sin θ＝對邊／斜邊＝6/10＝3/5。",
    },
    {
        "prompt": "直角三角形中，某銳角 θ 的鄰邊長 12 公分、斜邊長 13 公分，cos θ 為何？",
        "options": ["5/13", "12/13", "13/12", "12/5"],
        "answer": "B",
        "explanation": "cos θ＝鄰邊／斜邊＝12/13。",
    },
    {
        "prompt": "直角三角形中，某銳角 θ 的對邊長 9 公分、鄰邊長 12 公分，tan θ 為何？",
        "options": ["3/4", "4/3", "3/5", "4/5"],
        "answer": "A",
        "explanation": "tan θ＝對邊／鄰邊＝9/12＝3/4。",
    },
    {
        "prompt": "若直角三角形斜邊長 10 公分，且一銳角為 30°，則 30° 所對的邊長是多少？",
        "options": ["5 公分", "5√2 公分", "5√3 公分", "10√3 公分"],
        "answer": "A",
        "explanation": "30° 所對的邊是斜邊的一半，因此邊長為 10÷2＝5 公分。",
    },
    {
        "prompt": "觀察一棵樹的仰角為 45°，觀察點到樹底的水平距離為 8 公尺，忽略眼睛高度，樹高約為多少？",
        "options": ["4 公尺", "8 公尺", "8√2 公尺", "16 公尺"],
        "answer": "B",
        "explanation": "tan 45°＝樹高／水平距離＝1，所以樹高＝8 公尺。",
    },
    {
        "prompt": "若銳角 θ 滿足 sin θ＝3/5，且 θ 為銳角，則 cos θ 為何？",
        "options": ["3/5", "4/5", "5/3", "5/4"],
        "answer": "B",
        "explanation": "可視為對邊 3、斜邊 5 的直角三角形，另一股為 4，因此 cos θ＝鄰邊／斜邊＝4/5。",
    },
    {
        "prompt": "若銳角 θ 滿足 tan θ＝1，則 θ 為多少？",
        "options": ["30°", "45°", "60°", "90°"],
        "answer": "B",
        "explanation": "tan 45°＝1，而 θ 是銳角，因此 θ＝45°。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-12-{index}",
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
                "參考直角三角形銳角邊長比、sin／cos／tan 與仰角情境題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-12-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
