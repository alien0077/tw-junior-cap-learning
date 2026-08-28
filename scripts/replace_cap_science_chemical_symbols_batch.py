#!/usr/bin/env python3
"""Replace the element/compound-symbol template set with authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-aa-iv-5"
KID = "kg-science-content-aa-iv-5"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列元素名稱與化學符號的配對，何者正確？", ["鈉—Na", "氧—Ox", "氯—C", "鐵—Ir"], "A", "鈉的化學符號為 Na；氧為 O、氯為 Cl、鐵為 Fe。"),
    ("化學式 CO₂ 最能表示下列哪項資訊？", ["每個二氧化碳分子含 1 個碳原子與 2 個氧原子", "二氧化碳由 2 個碳原子組成", "二氧化碳含有 2 種碳元素", "每個二氧化碳分子只有 1 個氧原子"], "A", "CO₂ 中 C 的下標省略代表 1 個碳原子，O₂ 表示 2 個氧原子。"),
    ("下列哪一個化學式代表由兩種元素組成的化合物？", ["H₂O", "O₂", "Fe", "N₂"], "A", "H₂O 含氫、氧兩種元素且以固定比例組成，屬於化合物；O₂、Fe、N₂ 都只含一種元素。"),
    ("化學式 3H₂O 中，總共含有多少個氫原子？", ["6 個", "3 個", "5 個", "9 個"], "A", "每個 H₂O 含 2 個氫原子，前面的係數 3 表示 3 個水分子，所以氫原子共 3 × 2 = 6 個。"),
    ("若要表示 2 個氧分子，哪種寫法正確？", ["2O₂", "O₄", "2O", "O₂²"], "A", "O₂ 表示 1 個氧分子，前面的係數 2 表示 2 個氧分子；O₄ 是不同的化學式寫法，不能代替係數。"),
    ("水的化學式為 H₂O，若只看元素種類與原子個數，下列何者正確？", ["含氫、氧兩種元素，氫氧原子個數比為 2∶1", "只含有氫元素", "氫氧原子個數比為 1∶2", "每個水分子含 2 個氧原子"], "A", "H₂O 表示每個水分子含 2 個氫原子與 1 個氧原子，因此氫氧原子個數比為 2∶1。"),
    ("下列哪一組化學式都只代表元素，不代表化合物？", ["O₂、Fe、S₈", "H₂O、CO₂、NaCl", "NH₃、O₂、HCl", "CaCO₃、Fe、N₂"], "A", "O₂、Fe、S₈ 各自只含一種元素，雖可由多個原子組成，仍屬元素；其他組含有化合物。"),
    ("化學式 H₂SO₄ 中，1 個分子共有多少個原子？", ["7 個", "3 個", "6 個", "8 個"], "A", "H₂SO₄ 含 2 個氫、1 個硫與 4 個氧，總數為 2 + 1 + 4 = 7 個原子。"),
    ("若某化合物由 1 個鈉原子與 1 個氯原子組成，最適合表示它的化學式為何？", ["NaCl", "Na₂Cl", "NCl", "SCl"], "A", "鈉的符號是 Na、氯的符號是 Cl，各 1 個時寫成 NaCl。"),
    ("比較 2CO₂ 與 CO₂，下列敘述何者正確？", ["2CO₂ 表示二氧化碳分子數是 CO₂ 的 2 倍，但每個分子的組成不變", "2CO₂ 表示每個分子有 2 個碳原子", "2CO₂ 表示氧元素改成另一種元素", "兩者都只含 1 個氧原子"], "A", "化學式前的係數表示粒子數量；2CO₂ 是 2 個 CO₂ 分子，每個分子仍含 1 個碳與 2 個氧。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-aa-iv-5-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考自然科；元素與化合物符號及化學式判讀能力方向之獨立改編；官方答案表：{ANSWER}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style science chemical-symbol questions")
