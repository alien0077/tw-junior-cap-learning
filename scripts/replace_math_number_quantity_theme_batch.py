#!/usr/bin/env python3
"""Replace the math number-and-quantity theme questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-n"
KG_ID = "kg-math-performance-n"
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
        "prompt": "早晨氣溫為 −3°C，中午上升 8°C，晚上又下降 5°C。晚上氣溫為多少？",
        "options": ["−16°C", "0°C", "5°C", "10°C"],
        "answer": "B",
        "explanation": "依序計算 −3＋8−5＝0，因此晚上氣溫為 0°C。",
    },
    {
        "prompt": "計算 3/4＋5/8 的結果，最簡分數為何？",
        "options": ["8/12", "9/8", "11/8", "13/8"],
        "answer": "C",
        "explanation": "3/4＝6/8，所以 3/4＋5/8＝6/8＋5/8＝11/8，且 11 與 8 互質。",
    },
    {
        "prompt": "果汁與水的比例為 2：3，混合後共有 25 杯，其中果汁有幾杯？",
        "options": ["8 杯", "10 杯", "12 杯", "15 杯"],
        "answer": "B",
        "explanation": "總份數為 2＋3＝5，每份是 25÷5＝5 杯；果汁占 2 份，所以是 2×5＝10 杯。",
    },
    {
        "prompt": "一件標價 800 元的外套打 85 折，折扣後售價是多少元？",
        "options": ["640 元", "680 元", "720 元", "760 元"],
        "answer": "B",
        "explanation": "85 折表示原價的 0.85 倍，800×0.85＝680，因此售價為 680 元。",
    },
    {
        "prompt": "√50 介於哪兩個連續整數之間？",
        "options": ["5 與 6", "6 與 7", "7 與 8", "8 與 9"],
        "answer": "C",
        "explanation": "因為 7²＝49＜50＜64＝8²，所以 7＜√50＜8。",
    },
    {
        "prompt": "將 0.00045 用科學記號表示，結果為何？",
        "options": ["4.5×10⁻⁵", "4.5×10⁻⁴", "45×10⁻⁴", "45×10⁻⁵"],
        "answer": "B",
        "explanation": "小數點向右移 4 位得到 4.5，因此要乘上 10⁻⁴：0.00045＝4.5×10⁻⁴。",
    },
    {
        "prompt": "4 本筆記本共 180 元，若每本價格相同，買 7 本需要多少元？",
        "options": ["280 元", "315 元", "360 元", "420 元"],
        "answer": "B",
        "explanation": "每本 180÷4＝45 元，7 本需 45×7＝315 元；這是正比關係。",
    },
    {
        "prompt": "數列 2、5、8、11、⋯ 的第 20 項是多少？",
        "options": ["56", "59", "62", "65"],
        "answer": "B",
        "explanation": "首項 2、公差 3，第 20 項為 2＋(20−1)×3＝59。",
    },
    {
        "prompt": "某班 40 人中有 26 人參加校外教學，參加比例約為多少？",
        "options": ["52%", "60%", "65%", "75%"],
        "answer": "C",
        "explanation": "參加比例為 26÷40＝0.65，換成百分率為 65%。",
    },
    {
        "prompt": "一個長方形長 12.5 公分、寬 8 公分，面積是多少平方公分？",
        "options": ["90", "100", "105", "120"],
        "answer": "B",
        "explanation": "長方形面積＝長×寬＝12.5×8＝100 平方公分。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-n-{index}",
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
                "參考數與量範圍常見的整數、分數、比例、百分率、根式、科學記號、數列與幾何量題型"
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
        path = QUESTION_DIR / f"question-math-performance-n-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
