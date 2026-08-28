#!/usr/bin/env python3
"""Replace the n-IV-9 calculator and error questions with substantive originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_ID = "lesson-math-performance-n-iv-9"
KG_ID = "kg-math-performance-n-iv-9"
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
        "prompt": "使用計算機計算 3.7²，結果為多少？",
        "options": ["12.69", "13.69", "14.49", "15.29"],
        "answer": "B",
        "explanation": "3.7²＝3.7×3.7＝13.69；輸入次方或先做乘法都應得到相同結果。",
    },
    {
        "prompt": "使用計算機估算 √7，四捨五入到小數第一位應為多少？",
        "options": ["2.5", "2.6", "2.7", "2.8"],
        "answer": "B",
        "explanation": "√7 約為 2.6457，四捨五入到小數第一位時，百分位是 4，因此為 2.6。",
    },
    {
        "prompt": "將計算機算出的 18.746 四捨五入到小數第二位，結果是多少？",
        "options": ["18.74", "18.75", "18.76", "18.70"],
        "answer": "B",
        "explanation": "保留到小數第二位要看小數第三位；18.746 的小數第三位是 6，所以 18.74 進位為 18.75。",
    },
    {
        "prompt": "計算機顯示 2÷3＝0.666666⋯，若答案要求取到小數第三位，應寫成多少？",
        "options": ["0.660", "0.666", "0.667", "0.670"],
        "answer": "C",
        "explanation": "2÷3 是循環小數 0.666⋯；取到小數第三位時，看下一位仍是 6，因此 0.666 進位成 0.667。",
    },
    {
        "prompt": "某物的真實長度為 10.0 公分，量得 9.8 公分，這次測量的絕對誤差是多少？",
        "options": ["0.02 公分", "0.2 公分", "1.02 公分", "19.8 公分"],
        "answer": "B",
        "explanation": "絕對誤差是測量值與真實值差的絕對值：|9.8－10.0|＝0.2 公分。",
    },
    {
        "prompt": "承上題，若以真實長度 10.0 公分為基準，相對誤差是多少？",
        "options": ["0.2%", "2%", "20%", "98%"],
        "answer": "B",
        "explanation": "相對誤差＝絕對誤差÷真實值×100%＝0.2÷10.0×100%＝2%。",
    },
    {
        "prompt": "計算機以小數顯示 1÷3 為 0.333333，對這個顯示最合理的說法是什麼？",
        "options": ["1÷3 的精確值就是有限小數 0.333333", "計算機必定算錯了", "畫面只顯示近似值，1÷3 的精確值是循環小數", "只要再按一次等號就會變成整數"],
        "answer": "C",
        "explanation": "1÷3＝0.333⋯ 是無限循環小數，計算機畫面位數有限，因此顯示的是近似值，不是有限小數的精確值。",
    },
    {
        "prompt": "不按計算機，先估算 49.8×2.01 的結果，哪一個最接近？",
        "options": ["10", "50", "100", "200"],
        "answer": "C",
        "explanation": "49.8 約為 50，2.01 約為 2，因此乘積約為 50×2＝100；實際值 100.098 也接近 100。",
    },
    {
        "prompt": "圓半徑為 5 公分，若計算機取 π≈3.14，圓周長約為多少？",
        "options": ["15.7 公分", "31.4 公分", "62.8 公分", "78.5 公分"],
        "answer": "B",
        "explanation": "圓周長＝2πr，代入 π≈3.14、r＝5，得 2×3.14×5＝31.4 公分；這是近似值。",
    },
    {
        "prompt": "計算機算得某數值為 6.247，題目要求答案精確到小數第一位，應如何處理？",
        "options": ["直接寫 6.247，保留所有畫面位數", "捨去成 6.2，不必看下一位", "四捨五入成 6.2，因為小數第二位是 4", "進位成 7.0，因為有小數"],
        "answer": "C",
        "explanation": "保留小數第一位要觀察小數第二位；6.247 的小數第二位是 4，小於 5，所以四捨五入後為 6.2。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-math-performance-n-iv-9-{index}",
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
                "參考計算機操作、估算、四捨五入、近似值與誤差判讀題型"
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
        path = QUESTION_DIR / f"question-math-performance-n-iv-9-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()
