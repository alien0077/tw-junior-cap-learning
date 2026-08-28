#!/usr/bin/env python3
"""Replace the s-IV-11 triangle-center questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-11"
KG_ID = "kg-math-performance-s-iv-11"
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
        "prompt": "三角形三條中線的交點稱為什麼？",
        "options": ["重心", "外心", "內心", "垂心"],
        "answer": "A",
        "explanation": "三角形三條中線必相交於一點，該點稱為重心。",
    },
    {
        "prompt": "三角形的重心 G 在中線 AD 上，若 AG＝8 公分，則 GD 為多少？",
        "options": ["4 公分", "8 公分", "12 公分", "16 公分"],
        "answer": "A",
        "explanation": "重心將中線由頂點到邊的方向分成 2：1；AG 是較長的 2 份，故 GD＝8÷2＝4 公分。",
    },
    {
        "prompt": "三角形三條邊的垂直平分線交於哪一個三角形的心？",
        "options": ["重心", "外心", "內心", "垂心"],
        "answer": "B",
        "explanation": "三角形三邊的垂直平分線交點是外心，該點到三個頂點距離相等。",
    },
    {
        "prompt": "三角形三個內角的角平分線交於哪一個三角形的心？",
        "options": ["重心", "外心", "內心", "垂心"],
        "answer": "C",
        "explanation": "三條內角平分線交點是內心，內心到三邊的距離相等。",
    },
    {
        "prompt": "三角形頂點為 (0,0)、(6,0)、(0,3)，其重心坐標為何？",
        "options": ["(1, 2)", "(2, 1)", "(3, 1.5)", "(6, 3)"],
        "answer": "B",
        "explanation": "重心坐標是三頂點坐標的平均：( (0＋6＋0)÷3, (0＋0＋3)÷3 )＝(2,1)。",
    },
    {
        "prompt": "直角三角形的外心位於何處？",
        "options": ["直角頂點", "斜邊中點", "兩股交點外側任意處", "內角平分線交點"],
        "answer": "B",
        "explanation": "直角三角形的外心是斜邊中點；斜邊是外接圓的直徑。",
    },
    {
        "prompt": "若三角形的中線 AD＝15 公分，重心 G 到頂點 A 的距離 AG 為多少？",
        "options": ["5 公分", "7.5 公分", "10 公分", "12 公分"],
        "answer": "C",
        "explanation": "重心將中線由頂點起分成 2：1，AG＝(2/3)×15＝10 公分。",
    },
    {
        "prompt": "等邊三角形的重心、外心、內心與垂心有什麼關係？",
        "options": ["四點完全不同", "只有重心與外心重合", "四心重合為同一點", "只有內心與垂心重合"],
        "answer": "C",
        "explanation": "等邊三角形具有高度對稱性，四條重要線交於同一點，因此四心重合。",
    },
    {
        "prompt": "內心 I 到三角形三邊的距離具有哪一項性質？",
        "options": ["三個距離相等", "三個距離互為相反數", "只與最長邊距離相等", "一定有一個距離為 0"],
        "answer": "A",
        "explanation": "內心是內角平分線交點，到三邊的垂直距離相等；這個距離就是內切圓半徑。",
    },
    {
        "prompt": "外心 O 到三角形三個頂點的距離具有哪一項性質？",
        "options": ["OA、OB、OC 三者相等", "只有 OA＝OB", "OA、OB、OC 必互相垂直", "三段距離總和必為 0"],
        "answer": "A",
        "explanation": "外心在三邊垂直平分線上，因此到三個頂點距離相等，皆為外接圓半徑。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-11-{index}",
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
                "參考三角形重心、外心、內心與垂心的定義、位置及比例題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-11-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
