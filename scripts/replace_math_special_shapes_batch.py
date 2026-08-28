#!/usr/bin/env python3
"""Replace the s-IV-8 special-shape questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-8"
KG_ID = "kg-math-performance-s-iv-8"
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
        "prompt": "等腰直角三角形的兩股各長 6 公分，斜邊長是多少？",
        "options": ["6 公分", "6√2 公分", "12 公分", "18 公分"],
        "answer": "B",
        "explanation": "由畢氏定理，斜邊為 √(6²＋6²)＝√72＝6√2 公分。",
    },
    {
        "prompt": "在 30°−60°−90° 三角形中，若最短邊（對 30°）長 5 公分，斜邊長是多少？",
        "options": ["5 公分", "5√3 公分", "10 公分", "15 公分"],
        "answer": "C",
        "explanation": "30°−60°−90° 三角形中，斜邊是最短邊的 2 倍，所以為 2×5＝10 公分。",
    },
    {
        "prompt": "正方形邊長為 7 公分，其對角線長是多少？",
        "options": ["7 公分", "7√2 公分", "14 公分", "49 公分"],
        "answer": "B",
        "explanation": "對角線為兩股皆 7 的直角三角形斜邊，長度是 √(7²＋7²)＝7√2 公分。",
    },
    {
        "prompt": "正六邊形的每一個內角是多少？",
        "options": ["90°", "108°", "120°", "135°"],
        "answer": "C",
        "explanation": "六邊形內角和為 (6−2)×180°＝720°，正六邊形每角為 720°÷6＝120°。",
    },
    {
        "prompt": "菱形的兩條對角線長 6 公分與 8 公分，面積是多少平方公分？",
        "options": ["14", "24", "48", "96"],
        "answer": "B",
        "explanation": "菱形面積＝兩對角線乘積的一半，(6×8)÷2＝24 平方公分。",
    },
    {
        "prompt": "箏形的兩條對角線長 10 公分與 12 公分，且互相垂直，面積是多少平方公分？",
        "options": ["22", "60", "120", "240"],
        "answer": "B",
        "explanation": "對角線互相垂直的箏形面積為兩對角線乘積的一半，(10×12)÷2＝60 平方公分。",
    },
    {
        "prompt": "等腰梯形的一個底角為 65°，則同一底上的另一個底角是多少？",
        "options": ["55°", "65°", "115°", "130°"],
        "answer": "B",
        "explanation": "等腰梯形同一底上的兩個底角相等，因此另一個底角也是 65°。",
    },
    {
        "prompt": "一個正三角形的周長為 27 公分，每一邊長是多少？",
        "options": ["6 公分", "8 公分", "9 公分", "12 公分"],
        "answer": "C",
        "explanation": "正三角形三邊等長，每邊為周長÷3＝27÷3＝9 公分。",
    },
    {
        "prompt": "正八邊形的每一個外角是多少？",
        "options": ["30°", "45°", "60°", "135°"],
        "answer": "B",
        "explanation": "正八邊形外角和為 360°，每個外角為 360°÷8＝45°。",
    },
    {
        "prompt": "下列哪一項是正方形兼具矩形與菱形性質的原因？",
        "options": ["只有一組對邊平行", "四角為直角且四邊等長", "只有兩邊等長", "對角線一定不相交"],
        "answer": "B",
        "explanation": "正方形同時具有矩形的四個直角與菱形的四邊等長，因此兼具兩者的性質。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-8-{index}",
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
                "參考特殊三角形、特殊四邊形與正多邊形題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-8-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
