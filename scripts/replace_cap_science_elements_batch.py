#!/usr/bin/env python3
"""Replace one science chemistry lesson with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-aa-iv-3"
KID = "kg-science-content-aa-iv-3"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列物質中，何者屬於元素？", ["氧氣 O₂", "水 H₂O", "二氧化碳 CO₂", "食鹽水"], "A", "氧氣只由氧元素組成，屬於元素；水與二氧化碳是化合物，食鹽水是混合物。", "第4題物質分類題型改編"),
    ("下列何者屬於化合物？", ["鐵 Fe", "氮氣 N₂", "水 H₂O", "空氣"], "C", "水由氫、氧兩種元素以固定比例組成，屬於化合物。", "第4題物質分類題型改編"),
    ("某中性鈣原子的原子序為 20，則其質子數與電子數分別為何？", ["20、18", "18、20", "20、20", "40、20"], "C", "原子序等於質子數；中性原子的質子數等於電子數，因此皆為 20。", "第17題原子序與粒子數題型改編"),
    ("氯原子原子序為 17，形成 Cl⁻ 後，其電子數為何？", ["16", "17", "18", "34"], "C", "氯原子得到 1 個電子形成負一價離子，因此電子數為 17+1=18。", "第17題離子粒子數題型改編"),
    ("下列哪一組物質都屬於混合物？", ["氧氣與鐵", "水與二氧化碳", "空氣與食鹽水", "氯化鈉與銅"], "C", "空氣含多種氣體，食鹽水含水與溶解的食鹽，兩者都是混合物。", "第4題物質分類題型改編"),
    ("一個水分子 H₂O 中，含有幾個氫原子與幾個氧原子？", ["1 個氫、2 個氧", "2 個氫、1 個氧", "2 個氫、2 個氧", "3 個氫、1 個氧"], "B", "化學式下標表示原子數；H₂O 含 2 個氫原子與 1 個氧原子。", "第4題化學式判讀題型改編"),
    ("下列關於元素與化合物的敘述，何者正確？", ["化合物可用物理方法分解成元素", "元素一定由兩種以上原子組成", "化合物由兩種以上元素以固定比例組成", "混合物的組成比例永遠固定"], "C", "化合物由兩種以上元素以固定比例組成；其餘敘述混淆元素、化合物與混合物的定義。", "第4題物質分類題型改編"),
    ("某粒子有 11 個質子、10 個電子，關於此粒子的判斷何者正確？", ["它是帶一個正電的鈉離子", "它是中性的氖原子", "它是帶一個負電的鈉離子", "它是帶兩個正電的鎂離子"], "A", "質子數 11 對應鈉；電子比質子少 1 個，因此帶一個正電。", "第17題離子判讀題型改編"),
    ("下列哪一項可用物理方法分離？", ["氧氣中的氧原子", "水分子中的氫與氧", "食鹽水中的食鹽與水", "二氧化碳中的碳與氧"], "C", "食鹽水是混合物，可利用蒸發等物理方法分離；化合物需用化學方法分解。", "第4題混合物分離題型改編"),
    ("某粒子含有 8 個質子與 8 個電子，則它最可能是什麼？", ["中性的氧原子", "帶一個正電的氧離子", "帶一個負電的氟離子", "中性的碳原子"], "A", "質子數 8 是氧的原子序，且質子數等於電子數，故為中性氧原子。", "第17題原子序與粒子數題型改編"),
]

for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-aa-iv-3-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
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
print(f"replaced {len(rows)} CAP-style science chemistry questions")
