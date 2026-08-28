#!/usr/bin/env python3
"""Replace the math space-and-shape theme questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s"
KG_ID = "kg-math-performance-s"
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
        "prompt": "三角形的兩個內角分別為 50° 與 60°，第三個內角是多少？",
        "options": ["60°", "70°", "80°", "90°"],
        "answer": "B",
        "explanation": "三角形內角和為 180°，所以第三角為 180°−50°−60°＝70°。",
    },
    {
        "prompt": "直角三角形的兩股長為 6 公分與 8 公分，斜邊長是多少？",
        "options": ["9 公分", "10 公分", "12 公分", "14 公分"],
        "answer": "B",
        "explanation": "由畢氏定理，斜邊平方為 6²＋8²＝36＋64＝100，因此斜邊為 10 公分。",
    },
    {
        "prompt": "半徑 4 公分的圓，其面積以 π 表示為多少平方公分？",
        "options": ["4π", "8π", "16π", "32π"],
        "answer": "C",
        "explanation": "圓面積為 πr²，代入半徑 4 得 π×4²＝16π 平方公分。",
    },
    {
        "prompt": "一個長方形長 5 公分、寬 3 公分；若長與寬都放大為原來的 2 倍，面積變為原來的幾倍？",
        "options": ["2 倍", "3 倍", "4 倍", "8 倍"],
        "answer": "C",
        "explanation": "長、寬各放大 2 倍，面積倍率為 2×2＝4 倍。原面積 15 平方公分，放大後為 60 平方公分。",
    },
    {
        "prompt": "正方形有幾條對稱軸？",
        "options": ["2 條", "3 條", "4 條", "6 條"],
        "answer": "C",
        "explanation": "正方形的兩條對角線與兩條通過相對邊中點的直線都能將圖形對摺重合，共 4 條對稱軸。",
    },
    {
        "prompt": "長方體的長、寬、高分別為 3 公分、4 公分、5 公分，體積是多少立方公分？",
        "options": ["12", "20", "60", "120"],
        "answer": "C",
        "explanation": "長方體體積＝長×寬×高＝3×4×5＝60 立方公分。",
    },
    {
        "prompt": "在同一平面上，兩條直線互相垂直時，所形成的四個角各是多少度？",
        "options": ["45°", "60°", "90°", "180°"],
        "answer": "C",
        "explanation": "垂直線相交形成直角，因此四個角均為 90°。",
    },
    {
        "prompt": "一個等腰三角形的頂角為 40°，兩個底角各是多少？",
        "options": ["40°", "60°", "70°", "80°"],
        "answer": "C",
        "explanation": "等腰三角形兩底角相等，兩底角和為 180°−40°＝140°，所以各為 70°。",
    },
    {
        "prompt": "兩個相似三角形的對應邊比為 2：3，若小三角形面積為 24 平方公分，大三角形面積是多少？",
        "options": ["36 平方公分", "48 平方公分", "54 平方公分", "72 平方公分"],
        "answer": "C",
        "explanation": "面積比等於對應邊比的平方，即 2²：3²＝4：9；大三角形面積為 24×9÷4＝54 平方公分。",
    },
    {
        "prompt": "一個半徑 5 公分、圓心角 90° 的扇形，其弧長以 π 表示為多少公分？",
        "options": ["5π/2", "5π", "10π", "25π/2"],
        "answer": "A",
        "explanation": "弧長是整個圓周的 90°／360°＝1/4，因此弧長為 (2π×5)×1/4＝5π/2 公分。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-{index}",
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
                "參考空間與形狀範圍常見的角度、畢氏定理、圓、面積、體積、對稱與相似題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
