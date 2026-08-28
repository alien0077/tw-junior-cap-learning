#!/usr/bin/env python3
"""Replace one science structure/function topic with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-cb"
KID = "kg-science-content-cb"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列何者最能表示分子是由原子組成？", ["一個水分子由氫原子與氧原子組成", "空氣看起來透明", "鐵片可以反光", "水會流動"], "A", "水分子由氫、氧原子組成，直接呈現分子與原子的組成關係。", "第17題粒子結構判讀題型改編"),
    ("氧氣 O₂ 與臭氧 O₃ 都只含有氧元素，這項資料說明什麼？", ["不同分子可由同一元素組成，但原子數不同", "所有分子都只含一個原子", "元素一定只能形成一種物質", "氧氣與臭氧必然是混合物"], "A", "O₂ 與 O₃ 的元素種類相同，但分子中氧原子數不同，可能形成不同物質。", "第4題物質組成題型改編"),
    ("某中性氖原子有 10 個質子，則其電子數為何？", ["8", "9", "10", "20"], "C", "中性原子的質子數與電子數相等，因此電子數為 10。", "第17題原子粒子數題型改編"),
    ("下列何者是由許多原子排列形成的物質，而不是單一分子？", ["金屬銅的固體", "一個水分子", "一個二氧化碳分子", "一個氧分子"], "A", "金屬固體由大量金屬原子以結構排列形成，不以獨立分子作為基本單位。", "第17題粒子模型題型改編"),
    ("若一氧化碳 CO 與二氧化碳 CO₂ 的元素種類相同但性質不同，最合理的原因為何？", ["分子中原子的數目與排列不同", "兩者都沒有原子", "兩者一定是同一種物質", "性質只由顏色決定"], "A", "CO 與 CO₂ 的分子組成與排列不同，會造成結構與性質差異。", "第4題與第17題分子結構題型改編"),
    ("下列哪項變化主要是分子運動狀態改變，而非產生新物質？", ["冰融化成水", "木材燃燒成灰", "鐵生鏽", "食物腐敗"], "A", "冰與水都是 H₂O，融化主要改變狀態與分子運動，沒有產生新物質。", "第4題物質變化題型改編"),
    ("某粒子有 12 個質子與 10 個電子，最合理的判斷為何？", ["帶 2 個正電的鎂離子", "帶 2 個負電的鎂離子", "中性碳原子", "帶 1 個正電的鈉離子"], "A", "質子數 12 對應鎂，且質子比電子多 2 個，所以是 Mg²⁺。", "第17題原子與離子結構題型改編"),
    ("下列何者最能支持『物質的性質與微觀結構有關』？", ["石墨與鑽石都由碳組成但硬度不同", "所有透明物質都能導電", "物質顏色相同就一定相同", "只要質量相同性質就相同"], "A", "石墨與鑽石元素相同但原子排列不同、性質不同，支持結構影響性質。", "第17題原子排列與性質題型改編"),
    ("化學式 H₂SO₄ 中，總共有幾個原子？", ["3", "5", "6", "7"], "D", "下標表示原子數：2 個氫、1 個硫、4 個氧，共 7 個原子。", "第4題化學式與粒子組成題型改編"),
    ("下列哪項敘述符合原子、分子與物質的關係？", ["分子可由原子組成，物質的性質與其微觀結構有關", "原子只能存在於液體中", "分子一定比原子小", "所有物質都由相同排列方式組成"], "A", "原子可組成分子，微觀結構與排列會影響物質的性質，這是本單元的核心關係。", "第4題與第17題粒子結構整合題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-cb-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    target = ord(answer_positions[index - 1]) - ord("A")
    options = options[1:target + 1] + options[:1] + options[target + 1:]
    answer = answer_positions[index - 1]
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考自然科；{locator}；官方答案表：{ANSWER}；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style science structure/function questions")
