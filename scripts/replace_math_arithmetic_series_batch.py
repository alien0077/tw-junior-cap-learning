#!/usr/bin/env python3
"""Replace the n-IV-8 arithmetic-series question batch with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-n-iv-8"
KG_ID = "kg-math-performance-n-iv-8"
SOURCE_URL = (
    "https://www.yacjh.kh.edu.tw/upload/221/101_30637/"
    "114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83"
    "%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
)


def rotate_options(options, answer_letter):
    answer_index = ord(answer_letter) - ord("A")
    shift = (4 - answer_index) % 4
    rotated = options[shift:] + options[:shift]
    return [
        {"id": chr(ord("A") + index), "text": text}
        for index, text in enumerate(rotated)
    ]


QUESTIONS = [
    {
        "prompt": "數列 1、4、7、⋯、28 的前 10 項和是多少？",
        "options": ["135", "140", "145", "150"],
        "answer": "C",
        "explanation": "首項為 1、末項為 28、共有 10 項，因此總和為 (1＋28)×10÷2＝145。",
    },
    {
        "prompt": "等差級數 3＋6＋9＋⋯＋30 的和是多少？",
        "options": ["150", "165", "180", "195"],
        "answer": "B",
        "explanation": "這個級數有 10 項，首末項平均為 (3＋30)÷2＝16.5，所以總和為 16.5×10＝165。",
    },
    {
        "prompt": "一個等差數列首項為 5、公差為 4，前 8 項的和是多少？",
        "options": ["144", "152", "160", "168"],
        "answer": "B",
        "explanation": "第 8 項為 5＋7×4＝33，前 8 項和為 (5＋33)×8÷2＝152。",
    },
    {
        "prompt": "前 12 個正偶數的和是多少？",
        "options": ["132", "144", "156", "168"],
        "answer": "C",
        "explanation": "前 12 個正偶數是 2 到 24，為等差級數；總和為 (2＋24)×12÷2＝156。",
    },
    {
        "prompt": "階梯座位有 10 排，第 1 排有 8 個座位，每往後一排增加 3 個座位。全部座位共有多少個？",
        "options": ["205", "215", "225", "235"],
        "answer": "B",
        "explanation": "第 10 排有 8＋9×3＝35 個座位，因此總數為 (8＋35)×10÷2＝215。",
    },
    {
        "prompt": "小安連續存款 10 天，第 1 天存 20 元，之後每天比前一天多存 10 元。10 天共存多少元？",
        "options": ["600", "650", "700", "750"],
        "answer": "B",
        "explanation": "第 10 天存 20＋9×10＝110 元，10 天總和為 (20＋110)×10÷2＝650 元。",
    },
    {
        "prompt": "等差級數 7＋10＋13＋⋯＋52 的和是多少？",
        "options": ["448", "460", "472", "496"],
        "answer": "C",
        "explanation": "項數為 (52－7)÷3＋1＝16，首末項平均為 (7＋52)÷2＝29.5，所以總和為 29.5×16＝472。",
    },
    {
        "prompt": "等差級數 4＋9＋14＋⋯ 的前 15 項和是多少？",
        "options": ["555", "570", "585", "600"],
        "answer": "C",
        "explanation": "第 15 項為 4＋14×5＝74，前 15 項和為 (4＋74)×15÷2＝585。",
    },
    {
        "prompt": "若 1＋2＋3＋⋯＋n＝210，則 n 為多少？",
        "options": ["18", "19", "20", "21"],
        "answer": "C",
        "explanation": "由 n(n＋1)÷2＝210，得 n(n＋1)＝420；因為 20×21＝420，所以 n＝20。",
    },
    {
        "prompt": "一個等差級數首項為 12、公差為 −2，前 9 項的和是多少？",
        "options": ["30", "36", "42", "48"],
        "answer": "B",
        "explanation": "第 9 項為 12＋8×(−2)＝−4，前 9 項和為 (12＋(−4))×9÷2＝36。",
    },
]


def build_question(index, item):
    question_id = f"question-math-performance-n-iv-8-{index}"
    answer_id = item["answer"]
    return {
        "id": question_id,
        "subject": "math",
        "type": "single-choice",
        "lessonId": LESSON_ID,
        "knowledgeIds": [KG_ID],
        "prompt": item["prompt"],
        "options": rotate_options(item["options"], answer_id),
        "answer": {"value": answer_id, "explanation": item["explanation"]},
        "difficulty": "medium",
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceLocator": (
                "高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；"
                "參考等差級數求和、首尾平均、項數與生活情境題型"
            ),
            "sourceUrl": SOURCE_URL,
            "authoringNote": (
                "Substantive rewrite with new values, contexts, options, and explanations; "
                "no reproduction of public-exam wording, figures, or answer key. "
                "待第二輪 AI／Terra 內容複核。"
            ),
        },
    }


def main():
    for index, item in enumerate(QUESTIONS, start=1):
        path = QUESTION_DIR / f"question-math-performance-n-iv-8-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
