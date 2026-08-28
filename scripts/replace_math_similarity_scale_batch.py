#!/usr/bin/env python3
"""Replace the s-IV-6 similarity and scale questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-6"
KG_ID = "kg-math-performance-s-iv-6"
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
        "prompt": "兩個相似圖形的對應邊比為 3：5，若小圖形的一邊長為 6 公分，則大圖形的對應邊長為多少？",
        "options": ["8 公分", "10 公分", "12 公分", "15 公分"],
        "answer": "B",
        "explanation": "大：小＝5：3，所以大邊長為 6×5÷3＝10 公分。",
    },
    {
        "prompt": "一個三角形的周長為 24 公分，放大為原來的 1.5 倍後，新的周長是多少？",
        "options": ["30 公分", "36 公分", "40 公分", "48 公分"],
        "answer": "B",
        "explanation": "相似放大時周長也乘以長度倍率，24×1.5＝36 公分。",
    },
    {
        "prompt": "相似圖形的對應邊長倍率為 2，則其面積倍率為多少？",
        "options": ["2 倍", "3 倍", "4 倍", "8 倍"],
        "answer": "C",
        "explanation": "面積倍率是長度倍率的平方，故為 2²＝4 倍。",
    },
    {
        "prompt": "若兩個三角形有兩組對應角分別相等，依哪一個判定可知兩三角形相似？",
        "options": ["AA", "SSS", "SAS 全等", "HL"],
        "answer": "A",
        "explanation": "兩組對應角相等即可使用 AA（角角）相似判定。",
    },
    {
        "prompt": "同一時間測得旗杆高 2 公尺、影長 3 公尺；一棵樹的影長為 12 公尺，估計樹高是多少？",
        "options": ["6 公尺", "8 公尺", "10 公尺", "18 公尺"],
        "answer": "B",
        "explanation": "陽光角度相同形成相似三角形，樹高÷12＝2÷3，所以樹高＝12×2÷3＝8 公尺。",
    },
    {
        "prompt": "地圖比例尺為 1：50,000，地圖上兩地相距 3 公分，實際距離約為多少公里？",
        "options": ["0.15 公里", "1.5 公里", "15 公里", "150 公里"],
        "answer": "B",
        "explanation": "實際長度為 3×50,000＝150,000 公分；換算為公里是 1.5 公里。",
    },
    {
        "prompt": "小正方形邊長為 4 公分，大正方形邊長為 10 公分，兩者的面積比（小：大）為何？",
        "options": ["2：5", "4：10", "4：25", "16：100"],
        "answer": "C",
        "explanation": "面積分別為 4²＝16 與 10²＝100，約成最簡比為 16：100＝4：25。",
    },
    {
        "prompt": "兩個相似立體的對應長度倍率為 3，則其體積倍率為多少？",
        "options": ["3 倍", "6 倍", "9 倍", "27 倍"],
        "answer": "D",
        "explanation": "相似立體的體積倍率是長度倍率的三次方，3³＝27 倍。",
    },
    {
        "prompt": "兩個相似三角形的對應邊比（小：大）為 4：7，小三角形周長為 20 公分，則大三角形周長為多少？",
        "options": ["28 公分", "30 公分", "35 公分", "40 公分"],
        "answer": "C",
        "explanation": "周長比等於對應邊比，所以大周長為 20×7÷4＝35 公分。",
    },
    {
        "prompt": "下列哪一組條件足以判定兩個三角形相似？",
        "options": ["三組對應邊都相等", "兩組對應角相等", "只有一組對應邊相等", "周長相等"],
        "answer": "B",
        "explanation": "兩組對應角相等符合 AA 相似判定；三邊全等則是全等，其他條件不足以判定相似。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-6-{index}",
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
                "參考相似、縮放、比例尺、面積／體積倍率與生活情境題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-6-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
