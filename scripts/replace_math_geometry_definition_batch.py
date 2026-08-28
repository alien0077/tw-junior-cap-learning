#!/usr/bin/env python3
"""Replace the s-IV-1 geometry-definition questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-1"
KG_ID = "kg-math-performance-s-iv-1"
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
        "prompt": "下列哪一項是平行四邊形必定具有的性質？",
        "options": ["四個角都相等", "兩組對邊分別平行", "四邊都相等", "兩條對角線互相垂直"],
        "answer": "B",
        "explanation": "平行四邊形的定義是兩組對邊分別平行；四角相等、四邊相等或對角線垂直則不一定成立。",
    },
    {
        "prompt": "矩形的兩條對角線具有哪一項性質？",
        "options": ["長度相等且互相平分", "一定互相垂直", "一定是角平分線", "只有一條對角線"],
        "answer": "A",
        "explanation": "矩形是平行四邊形，所以對角線互相平分；矩形的對角線也等長，但不一定互相垂直。",
    },
    {
        "prompt": "菱形必定具有下列哪一項性質？",
        "options": ["四個角都是直角", "兩條對角線等長", "四邊長度相等", "只有一條對稱軸"],
        "answer": "C",
        "explanation": "菱形的定義是四邊等長；它不一定有直角，對角線也不一定等長。",
    },
    {
        "prompt": "若兩個三角形的三組對應邊長分別相等，依哪一個判定可知兩三角形全等？",
        "options": ["ASA", "SAS", "AAS", "SSS"],
        "answer": "D",
        "explanation": "三組對應邊分別相等是 SSS（邊邊邊）全等判定。",
    },
    {
        "prompt": "線段 AB 的垂直平分線上任一點 P，必定滿足哪個關係？",
        "options": ["PA＝PB", "PA＞PB", "PA＜PB", "PA＋PB＝AB"],
        "answer": "A",
        "explanation": "垂直平分線上的點到線段兩端點距離相等，因此 PA＝PB。",
    },
    {
        "prompt": "若射線 BD 是 ∠ABC 的角平分線，且 ∠ABC＝76°，則 ∠ABD 為多少？",
        "options": ["19°", "38°", "54°", "152°"],
        "answer": "B",
        "explanation": "角平分線將角分成兩個相等的角，所以 ∠ABD＝76°÷2＝38°。",
    },
    {
        "prompt": "圓的切線在切點 T 與半徑 OT 的關係為何？",
        "options": ["互相平行", "互相垂直", "長度一定相等", "夾角一定為 45°"],
        "answer": "B",
        "explanation": "圓的切線與通過切點的半徑互相垂直，因此切線與 OT 的夾角為 90°。",
    },
    {
        "prompt": "六邊形的內角和是多少？",
        "options": ["540°", "720°", "900°", "1080°"],
        "answer": "B",
        "explanation": "n 邊形內角和為 (n−2)×180°；六邊形為 (6−2)×180°＝720°。",
    },
    {
        "prompt": "正五邊形的每一個內角是多少？",
        "options": ["72°", "90°", "108°", "120°"],
        "answer": "C",
        "explanation": "五邊形內角和為 (5−2)×180°＝540°，正五邊形各角相等，所以每角為 540°÷5＝108°。",
    },
    {
        "prompt": "若一個三角形有兩邊長相等，則這兩邊所對的角具有什麼關係？",
        "options": ["一定互為補角", "一定互為餘角", "一定相等", "一定相差 90°"],
        "answer": "C",
        "explanation": "等腰三角形中，等邊所對的角相等，因此兩個對應角一定相等。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-1-{index}",
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
                "參考幾何形體定義、符號、全等判定與基本性質題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-1-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
