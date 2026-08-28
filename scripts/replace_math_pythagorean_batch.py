#!/usr/bin/env python3
"""Replace the s-IV-7 Pythagorean-theorem questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-7"
KG_ID = "kg-math-performance-s-iv-7"
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
        "prompt": "直角三角形的兩股長為 9 公分與 12 公分，斜邊長是多少？",
        "options": ["13 公分", "15 公分", "17 公分", "21 公分"],
        "answer": "B",
        "explanation": "由畢氏定理，斜邊平方為 9²＋12²＝81＋144＝225，因此斜邊為 15 公分。",
    },
    {
        "prompt": "直角三角形斜邊長 13 公分、一股長 5 公分，另一股長是多少？",
        "options": ["8 公分", "10 公分", "12 公分", "18 公分"],
        "answer": "C",
        "explanation": "另一股平方為 13²−5²＝169−25＝144，因此另一股為 12 公分。",
    },
    {
        "prompt": "正方形邊長為 6 公分，其對角線長以根式表示為何？",
        "options": ["6 公分", "6√2 公分", "12 公分", "36√2 公分"],
        "answer": "B",
        "explanation": "對角線是兩股皆為 6 的直角三角形斜邊，長度為 √(6²＋6²)＝6√2 公分。",
    },
    {
        "prompt": "一支長 15 公尺的梯子靠在垂直牆面上，梯腳離牆 9 公尺，梯頂離地多高？",
        "options": ["6 公尺", "9 公尺", "12 公尺", "18 公尺"],
        "answer": "C",
        "explanation": "牆、地面與梯子形成直角三角形，高度平方為 15²−9²＝225−81＝144，所以高度為 12 公尺。",
    },
    {
        "prompt": "坐標平面上 A(1, 2)、B(7, 10)，線段 AB 的長度是多少？",
        "options": ["8", "10", "12", "14"],
        "answer": "B",
        "explanation": "水平差為 6、垂直差為 8，距離為 √(6²＋8²)＝√100＝10。",
    },
    {
        "prompt": "長方形的長、寬分別為 15 公分與 8 公分，對角線長是多少？",
        "options": ["16 公分", "17 公分", "18 公分", "23 公分"],
        "answer": "B",
        "explanation": "對角線平方為 15²＋8²＝225＋64＝289，因此對角線為 17 公分。",
    },
    {
        "prompt": "下列哪一組邊長可以組成直角三角形？",
        "options": ["7、24、25", "6、8、11", "5、6、8", "8、10、15"],
        "answer": "A",
        "explanation": "7²＋24²＝49＋576＝625＝25²，符合畢氏定理，因此 7、24、25 可以組成直角三角形。",
    },
    {
        "prompt": "等腰直角三角形的兩股各長 5 公分，斜邊長是多少？",
        "options": ["5 公分", "5√2 公分", "10 公分", "25√2 公分"],
        "answer": "B",
        "explanation": "斜邊為 √(5²＋5²)＝√50＝5√2 公分。",
    },
    {
        "prompt": "直角三角形的斜邊長 10 公分，一股長 6 公分，另一股長是多少？",
        "options": ["4 公分", "6 公分", "8 公分", "16 公分"],
        "answer": "C",
        "explanation": "另一股平方為 10²−6²＝100−36＝64，所以另一股為 8 公分。",
    },
    {
        "prompt": "直角三角形的兩股長為 10 公分與 24 公分，面積是多少平方公分？",
        "options": ["120", "144", "240", "340"],
        "answer": "A",
        "explanation": "直角三角形面積為兩股乘積的一半，(10×24)÷2＝120 平方公分。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-7-{index}",
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
                "參考畢氏定理、坐標距離與生活情境題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-7-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
