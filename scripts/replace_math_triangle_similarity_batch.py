#!/usr/bin/env python3
"""Replace the s-IV-10 triangle-similarity questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-10"
KG_ID = "kg-math-performance-s-iv-10"
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
        "prompt": "若兩個三角形有兩組對應角分別相等，則兩三角形一定相似。這個判定稱為什麼？",
        "options": ["AA", "SSS 全等", "SAS 全等", "HL 全等"],
        "answer": "A",
        "explanation": "兩組對應角相等即可判定三角形相似，稱為 AA（角角）判定。",
    },
    {
        "prompt": "三角形甲的三邊為 6、8、10 公分，三角形乙的三邊為 9、12、15 公分。乙與甲的對應邊長倍率為多少？",
        "options": ["1.25", "1.5", "2", "2.5"],
        "answer": "B",
        "explanation": "對應邊比為 9÷6＝12÷8＝15÷10＝1.5，因此乙是甲的 1.5 倍。",
    },
    {
        "prompt": "兩個相似三角形的對應邊比（小：大）為 4：7，若小三角形一邊長 12 公分，大三角形對應邊長是多少？",
        "options": ["18 公分", "21 公分", "24 公分", "28 公分"],
        "answer": "B",
        "explanation": "大邊長＝12×7÷4＝21 公分。",
    },
    {
        "prompt": "在 △ABC 中，D 在 AB 上、E 在 AC 上，且 DE∥BC。若 AD＝3、DB＝2、AE＝6，則 EC 為多少？",
        "options": ["2", "3", "4", "5"],
        "answer": "C",
        "explanation": "由 DE∥BC，△ADE∼△ABC；AD／AB＝AE／AC，即 3／5＝6／AC，所以 AC＝10，EC＝10−6＝4。",
    },
    {
        "prompt": "兩個相似三角形的對應邊長倍率為 3，則大三角形與小三角形的面積比為何？",
        "options": ["3：1", "6：1", "9：1", "27：1"],
        "answer": "C",
        "explanation": "相似三角形面積比等於對應邊倍率的平方，因此為 3²：1²＝9：1。",
    },
    {
        "prompt": "同一時間測得一根 1.5 公尺竹竿影長 2 公尺；建築物影長 16 公尺，估計建築物高多少？",
        "options": ["10 公尺", "12 公尺", "14 公尺", "16 公尺"],
        "answer": "B",
        "explanation": "由相似三角形，建築物高／16＝1.5／2，所以建築物高＝16×1.5÷2＝12 公尺。",
    },
    {
        "prompt": "若 △ABC∼△DEF，且 A↔D、B↔E、C↔F，AB＝8 公分、DE＝12 公分，則對應邊 BC＝10 公分時，EF 為多少？",
        "options": ["12 公分", "15 公分", "18 公分", "20 公分"],
        "answer": "B",
        "explanation": "放大倍率為 DE／AB＝12／8＝1.5，所以 EF＝10×1.5＝15 公分。",
    },
    {
        "prompt": "下列哪一組條件足以判定兩三角形相似，而不必知道三邊長？",
        "options": ["一組對應邊相等", "兩組對應角相等", "只有周長相等", "一個角相等"],
        "answer": "B",
        "explanation": "AA 判定只需兩組對應角相等即可判定相似，其餘條件都不足。",
    },
    {
        "prompt": "相似三角形甲、乙的周長比（甲：乙）為 2：5，若甲的周長為 18 公分，乙的周長是多少？",
        "options": ["30 公分", "36 公分", "45 公分", "50 公分"],
        "answer": "C",
        "explanation": "相似三角形周長比等於對應邊比，乙周長＝18×5÷2＝45 公分。",
    },
    {
        "prompt": "若兩個三角形的三組對應邊長成比例，則可依哪個判定得知兩三角形相似？",
        "options": ["AA", "SAS", "SSS 相似判定", "只有一角相等"],
        "answer": "C",
        "explanation": "三組對應邊長成比例，符合 SSS 相似判定；這裡要求的是比例，不是三邊分別相等。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-10-{index}",
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
                "參考三角形相似判定、比例、平行線截比與生活情境題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-10-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
