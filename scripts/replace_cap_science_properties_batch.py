#!/usr/bin/env python3
"""Replace the physical/chemical-properties template set with authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-ab-iv-3"
KID = "kg-science-content-ab-iv-3"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列何者屬於物質的物理性質？", ["鋁的密度約為 2.7 g/cm³", "木材在空氣中可以燃燒", "鐵在潮濕環境中容易生鏽", "小蘇打遇醋會產生氣泡"], "A", "密度可在不改變物質種類的情況下測量，屬於物理性質；燃燒、生鏽與產氣反映化學性質或化學反應。"),
    ("研究某液體的沸點時，下列哪項最適合作為物理性質的觀察？", ["記錄液體開始沸騰時的溫度", "觀察液體是否與鎂片反應", "測試液體燃燒後的產物", "檢查液體是否使石蕊試紙變色"], "A", "沸點是物理性質，測量時不必讓液體變成另一種物質；其餘涉及化學反應或化學性質。"),
    ("一塊金屬可導電，且切成兩半後兩半仍可導電。這個例子主要說明導電性是什麼？", ["物理性質", "化學變化", "化學反應的生成物", "物質燃燒的條件"], "A", "導電性可被觀察或測量，且觀察過程不必改變物質種類，因此屬於物理性質。"),
    ("下列哪個現象最能顯示物質發生化學變化？", ["鐵釘表面生成新的紅棕色物質", "冰塊融化成水", "鋁片被剪成小片", "糖溶解在水中"], "A", "鐵生鏽會生成不同於鐵的新物質，是化學變化；其餘主要是狀態、形狀或混合狀態改變。"),
    ("若要比較甲、乙兩種固體的密度，除測量質量外，還應測量哪項資料？", ["體積", "燃燒後的火焰顏色", "與酸反應的氣味", "放置地點的名稱"], "A", "密度等於質量除以體積，因此需測量同一試樣的質量與體積。"),
    ("某白色粉末遇水溶解，但無法只依『可溶於水』判定它是哪一種物質，主要原因為何？", ["不同物質可能具有相同的物理性質", "所有物質都只具有一種性質", "溶解必然會產生新物質", "物理性質不能被觀察"], "A", "單一物理性質通常不足以唯一辨識物質，不同物質可能都能溶於水，需搭配其他證據。"),
    ("下列哪項測試最直接用來比較兩種物質的化學性質？", ["分別觀察它們與稀鹽酸是否產生氣體", "分別量取相同體積", "分別測量熔點", "分別觀察外觀顏色"], "A", "與稀鹽酸是否反應及產生氣體涉及是否形成新物質，可比較化學性質。"),
    ("將蠟燭加熱融化，冷卻後又凝固，關於此過程何者正確？", ["主要是物理變化，物質種類沒有改變", "一定生成新的氣體", "蠟變成另一種元素", "必然發生酸鹼中和"], "A", "蠟的熔化與凝固是狀態改變，若沒有燃燒等反應，物質種類仍未改變。"),
    ("某未知液體的密度、沸點與導電性都已測得，若要提高鑑定可信度，最合理的做法是什麼？", ["把多項測量結果與可靠資料或已知樣品比較", "只挑一項最符合直覺的結果", "忽略測量單位與誤差", "把液體全部倒掉後猜測名稱"], "A", "多項可量測性質與可靠資料交叉比對，並注意單位與誤差，才能提高鑑定的可信度。"),
    ("下列哪組『性質—分類』配對正確？", ["銅的延展性—物理性質", "汽油容易燃燒—物理性質", "鐵容易生鏽—形狀改變", "食醋與小蘇打反應—只有物理變化"], "A", "延展性描述物質可被拉伸或敲展而不必改變種類，屬物理性質；其餘選項分類不正確。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-ab-iv-3-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考自然科；物理與化學性質判讀能力方向之獨立改編；官方答案表：{ANSWER}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style science property questions")
