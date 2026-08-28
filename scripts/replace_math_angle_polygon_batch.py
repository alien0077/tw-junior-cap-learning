#!/usr/bin/env python3
"""Replace the s-IV-2 angle and polygon questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-2"
KG_ID = "kg-math-performance-s-iv-2"
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
        "prompt": "兩個互為鄰補角的角，其中一角為 68°，另一角是多少？",
        "options": ["102°", "112°", "122°", "128°"],
        "answer": "B",
        "explanation": "鄰補角的和為 180°，所以另一角為 180°−68°＝112°。",
    },
    {
        "prompt": "兩條直線相交形成一組對頂角，其中一角為 47°，它的對頂角是多少？",
        "options": ["43°", "47°", "133°", "137°"],
        "answer": "B",
        "explanation": "對頂角相等，因此與 47° 相對的角也是 47°。",
    },
    {
        "prompt": "三角形的一個外角為 110°，其中一個不相鄰的內角為 45°，另一個不相鄰內角是多少？",
        "options": ["55°", "65°", "75°", "85°"],
        "answer": "B",
        "explanation": "三角形外角等於兩個不相鄰內角和，所以另一角為 110°−45°＝65°。",
    },
    {
        "prompt": "四邊形的三個內角為 80°、95°、110°，第四個內角是多少？",
        "options": ["65°", "75°", "85°", "95°"],
        "answer": "B",
        "explanation": "四邊形內角和為 360°，第四角為 360°−80°−95°−110°＝75°。",
    },
    {
        "prompt": "正六邊形的每一個外角是多少？",
        "options": ["45°", "60°", "72°", "90°"],
        "answer": "B",
        "explanation": "凸多邊形外角和為 360°；正六邊形各外角相等，所以每角為 360°÷6＝60°。",
    },
    {
        "prompt": "正八邊形的每一個內角是多少？",
        "options": ["120°", "135°", "140°", "150°"],
        "answer": "B",
        "explanation": "八邊形內角和為 (8−2)×180°＝1080°，每角為 1080°÷8＝135°。",
    },
    {
        "prompt": "一個五邊形的四個外角依序為 70°、80°、90°、60°，第五個外角是多少？",
        "options": ["50°", "60°", "70°", "80°"],
        "answer": "B",
        "explanation": "多邊形外角和為 360°，第五角為 360°−70°−80°−90°−60°＝60°。",
    },
    {
        "prompt": "兩條平行線被一條截線所截，某一個銳角為 72°，與它相等的對應角是多少？",
        "options": ["72°", "108°", "118°", "288°"],
        "answer": "A",
        "explanation": "平行線被截線所截時，對應角相等，因此對應角也是 72°。",
    },
    {
        "prompt": "正多邊形的每一個內角為 150°，這個正多邊形有幾邊？",
        "options": ["10 邊", "12 邊", "15 邊", "18 邊"],
        "answer": "B",
        "explanation": "每個外角為 180°−150°＝30°；外角和 360°，邊數為 360°÷30°＝12。",
    },
    {
        "prompt": "某多邊形的內角和為 1260°，它是幾邊形？",
        "options": ["7 邊形", "8 邊形", "9 邊形", "10 邊形"],
        "answer": "C",
        "explanation": "(n−2)×180°＝1260°，所以 n−2＝7，n＝9，是九邊形。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-2-{index}",
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
                "參考角、平行線與多邊形內外角計算及推理題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-2-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
