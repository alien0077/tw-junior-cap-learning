#!/usr/bin/env python3
"""Replace the atomic-model template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-aa-iv-1"
KID = "kg-science-content-aa-iv-1"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("在α粒子散射實驗中，大多數α粒子穿過金箔、少數大角度偏轉，最支持哪項結論？", ["原子大部分是空間，正電荷與大部分質量集中在很小的原子核", "原子內部完全沒有帶電粒子", "電子集中在原子核內且不會運動", "原子的質量平均分布在整個範圍"], "A", "大多數粒子直穿表示原子大部分是空間；少數大角度偏轉則表示正電荷與質量集中在小區域的原子核。"),
    ("陰極射線實驗使科學家推論原子內含有哪種粒子？", ["電子", "中子以外的分子", "水分子", "只有正電荷而沒有粒子"], "A", "陰極射線可被電場與磁場偏轉，研究結果支持原子內含帶負電的電子。"),
    ("若某原子模型能解釋氫原子的特定光譜線，這表示模型至少具有什麼價值？", ["能以模型與證據說明部分可觀察現象", "已證明模型永遠不必修正", "模型就是原子的直接照片", "所有元素都必然只有相同光譜"], "A", "模型能解釋可觀察的光譜證據，就具有科學用途；但仍須接受其他證據檢驗，不能宣稱永遠正確。"),
    ("中性原子中，若質子數為 8，電子數通常為多少？", ["8", "0", "16", "4"], "A", "中性原子的正電荷總量與負電荷總量相等，因此質子數 8 時通常有 8 個電子。"),
    ("下列何者最適合描述原子核？", ["體積很小，含有帶正電的質子與不帶電的中子", "占原子大部分體積且只含電子", "完全不含質量", "只由帶負電的電子組成"], "A", "原子核位於原子中心，體積很小，主要由質子與中子組成；電子分布在核外。"),
    ("科學家從新實驗發現原有原子模型無法解釋的結果時，最合理的做法是什麼？", ["檢查證據與假設，修正或建立能解釋新結果的模型", "忽略結果以維持原模型不變", "只挑符合原模型的數據", "宣布所有實驗都沒有價值"], "A", "科學模型須與證據相互檢驗；若新證據不符合原模型，就應檢查方法並修正模型或提出新模型。"),
    ("氯原子得到一個電子成為帶負電的氯離子，這個模型中改變的是哪項？", ["電子數增加，質子數通常不變", "質子數增加一個且電子數不變", "中子全部變成電子", "原子核消失"], "A", "陰離子通常是原子得到電子形成，原子核中的質子數不因一般得失電子而改變。"),
    ("用球棒模型表示原子時，下列哪項是正確的科學解讀？", ["模型是依證據建立的表示方式，不等於原子的實際照片", "模型中的球一定與真實粒子大小相同", "模型畫得漂亮就代表結論正確", "模型一旦建立便不可更改"], "A", "科學模型用來表示不易直接觀察的對象，須依證據檢驗，不能把圖示外觀當成實體本身。"),
    ("比較兩個原子示意圖時，若它們質子數相同、電子數不同，最可能表示什麼？", ["它們是同一元素的不同離子", "它們一定是兩種不同元素", "它們一定沒有原子核", "它們的中子數必然相同"], "A", "元素種類由質子數決定；質子數相同而電子數不同，通常表示同一元素的不同電荷狀態。"),
    ("下列哪項最能呈現原子模型演變的科學特徵？", ["模型會隨新證據與新觀測結果修正", "後提出的模型只靠作者喜好決定", "所有模型都只描述外觀而不需證據", "早期模型被修正後就完全沒有學習價值"], "A", "原子模型演變顯示科學知識會根據證據修正；早期模型仍可能在適用範圍內提供重要基礎。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-aa-iv-1-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    target = ord(answer_positions[index - 1]) - ord("A")
    rotated = options[1:target + 1] + options[:1] + options[target + 1:]
    answer = answer_positions[index - 1]
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(rotated)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考自然科；原子模型與證據判讀能力方向之獨立改編；官方答案表：{ANSWER}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style science atomic-model questions")
