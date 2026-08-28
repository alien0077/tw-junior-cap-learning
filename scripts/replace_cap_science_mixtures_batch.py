#!/usr/bin/env python3
"""Replace one mixtures lesson with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-ab-iv-4"
KID = "kg-science-content-ab-iv-4"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列物質中，何者屬於混合物？", ["蒸餾水", "氧氣", "空氣", "純銅"], "C", "空氣含有多種氣體，組成比例可變，屬於混合物。", "第4題物質分類題型改編"),
    ("下列何者屬於純物質中的化合物？", ["氮氣", "食鹽水", "二氧化碳", "黃銅"], "C", "二氧化碳由碳、氧兩種元素以固定比例組成，是化合物；黃銅與食鹽水是混合物。", "第4題物質分類題型改編"),
    ("要從泥水中分離泥沙與水，最適合先使用哪種方法？", ["過濾", "蒸餾後燃燒", "電解", "化學合成"], "A", "泥沙不溶於水，可利用過濾使固體與液體分離。", "第4題混合物分離題型改編"),
    ("下列哪項證據最能支持某試樣是純物質？", ["外觀透明", "在固定壓力下具有固定沸點", "氣味明顯", "顏色鮮豔"], "B", "純物質在固定壓力下通常具有固定的沸點；外觀、氣味與顏色不足以單獨判定。", "第4題物質判定題型改編"),
    ("食鹽完全溶於水形成食鹽水後，這個系統屬於哪一類？", ["元素", "化合物", "混合物", "單一原子"], "C", "食鹽水同時含水與食鹽，且可用物理方法分離，屬於混合物。", "第4題溶液分類題型改編"),
    ("下列哪一組都是元素？", ["氫氣與氧氣", "水與二氧化碳", "食鹽與水", "空氣與銅"], "A", "氫氣與氧氣各只由一種元素組成，都是元素；其餘組合含有化合物或混合物。", "第4題元素與物質分類題型改編"),
    ("用蒸餾法分離酒精與水，主要利用兩者哪項性質不同？", ["沸點", "原子序", "質子數", "顏色必然不同"], "A", "蒸餾利用混合物成分沸點不同的特性進行分離。", "第4題混合物分離題型改編"),
    ("某金屬樣品由銅與鋅組成，且比例可依製程改變。此樣品較適合分類為何者？", ["元素", "化合物", "混合物", "單一分子"], "C", "銅鋅合金的組成比例可變，且由兩種金屬混合而成，屬於混合物。", "第4題合金分類題型改編"),
    ("下列何者最能區分化合物與混合物？", ["化合物成分以固定比例結合，混合物比例可變", "兩者都只能用化學方法分離", "兩者都只含一種元素", "兩者外觀一定不同"], "A", "化合物具有固定組成與性質，混合物的成分比例可變且通常可用物理方法分離。", "第4題物質分類比較題型改編"),
    ("研究者以色層分析分離墨水中的不同色素，這項結果最能支持墨水是什麼？", ["元素", "化合物", "混合物", "真空"], "C", "色層分析分出多種色素，表示墨水含有多種成分，屬於混合物。", "第4題資料判讀與混合物分類題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-ab-iv-4-{index}.json"
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
print(f"replaced {len(rows)} CAP-style science mixture questions")
