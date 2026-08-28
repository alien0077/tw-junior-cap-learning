#!/usr/bin/env python3
"""Replace the s-IV-9 triangle side-angle and congruence questions with originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-s-iv-9"
KG_ID = "kg-math-performance-s-iv-9"
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
        "prompt": "三角形三邊長為 5 公分、7 公分與 x 公分，若 x 為整數，則 x 可能是多少？",
        "options": ["1", "3", "12", "13"],
        "answer": "B",
        "explanation": "三角形不等式要求 |7−5|＜x＜7＋5，即 2＜x＜12；選項中只有 3 符合。",
    },
    {
        "prompt": "一個三角形的三邊長為 4、6、9 公分，則最大的內角是下列哪一邊所對的角？",
        "options": ["4 公分邊所對的角", "6 公分邊所對的角", "9 公分邊所對的角", "無法比較"],
        "answer": "C",
        "explanation": "三角形中，較長的邊對較大的角；最長邊為 9 公分，所以它所對的角最大。",
    },
    {
        "prompt": "若兩個三角形的三組對應邊長分別為 5、7、9 公分，則兩三角形可由哪個判定得知全等？",
        "options": ["SSS", "SAS", "ASA", "只有一組邊相等"],
        "answer": "A",
        "explanation": "三組對應邊分別相等，符合 SSS（邊邊邊）全等判定。",
    },
    {
        "prompt": "兩個三角形有兩邊及其夾角分別相等，依哪個判定可知兩三角形全等？",
        "options": ["SSS", "SAS", "AAA", "只有 AA 相似"],
        "answer": "B",
        "explanation": "兩邊及其夾角分別相等是 SAS（邊角邊）全等判定。",
    },
    {
        "prompt": "等腰三角形的兩腰各長 8 公分，底邊長 6 公分，則兩個底角具有什麼關係？",
        "options": ["一個較大、一個較小", "兩角互為補角", "兩角相等", "兩角一定都是直角"],
        "answer": "C",
        "explanation": "等腰三角形的兩腰相等，故兩腰所對的底角相等；底邊長度不改變此性質。",
    },
    {
        "prompt": "在全等三角形 ABC 與 DEF 中，若 A↔D、B↔E、C↔F，且 ∠B＝48°，則 ∠E 為多少？",
        "options": ["42°", "48°", "96°", "132°"],
        "answer": "B",
        "explanation": "全等三角形的對應角相等；B 對應 E，所以 ∠E＝∠B＝48°。",
    },
    {
        "prompt": "若兩個三角形全等，其中一個三角形周長為 26 公分，另一個三角形周長為多少？",
        "options": ["13 公分", "26 公分", "52 公分", "無法判定"],
        "answer": "B",
        "explanation": "全等圖形的對應邊等長，因此周長也相等，另一三角形周長為 26 公分。",
    },
    {
        "prompt": "三角形的兩邊長為 4 公分與 9 公分，第三邊 x 應滿足哪個範圍才能形成三角形？",
        "options": ["x＞13", "5＜x＜13", "0＜x＜5", "x＝5 或 13"],
        "answer": "B",
        "explanation": "三角形不等式為 |9−4|＜x＜9＋4，所以 5＜x＜13；等號時三點會共線，不能成三角形。",
    },
    {
        "prompt": "若 △PQR≅△XYZ，則下列哪一組對應關係正確？",
        "options": ["PQ 對應 YZ", "∠Q 對應 ∠Y", "PR 對應 XY", "∠P 對應 ∠Z"],
        "answer": "B",
        "explanation": "全等符號的頂點順序表示 P↔X、Q↔Y、R↔Z，因此 ∠Q 對應 ∠Y。",
    },
    {
        "prompt": "直角三角形的斜邊與一股分別相等，且兩者的直角也相等，依哪個判定可判定全等？",
        "options": ["ASA", "SAS", "斜邊－直角邊判定", "AAA"],
        "answer": "C",
        "explanation": "兩個直角三角形若斜邊與一股分別相等，符合斜邊－直角邊全等判定。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-s-iv-9-{index}",
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
                "參考三角形邊角關係、三角形不等式與全等判定題型"
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
        path = QUESTION_DIR / f"question-math-performance-s-iv-9-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
