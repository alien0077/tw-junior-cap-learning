#!/usr/bin/env python3
"""Replace the periodic-properties template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-aa-iv-4"
KID = "kg-science-content-aa-iv-4"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("現代週期表排列元素時，主要依據元素的哪項順序？", ["原子序由小到大", "物質的顏色由深到淺", "密度一律由小到大", "發現年代由早到晚"], "A", "現代週期表主要依原子序由小到大排列，元素性質也會隨排列呈現週期性變化。"),
    ("週期表中同一週期的元素，通常具有哪項共同特徵？", ["電子層數相同", "質子數完全相同", "都是金屬", "相對原子質量完全相同"], "A", "同一週期代表原子具有相同的電子層數；元素種類與質子數仍各不相同。"),
    ("若某元素在週期表中位於第二週期，關於其原子模型的合理推論為何？", ["原子有兩層電子層", "原子一定有兩個質子", "原子一定是氣體", "原子核沒有中子"], "A", "週期數可用來判斷原子的電子層數；第二週期元素具有兩層電子層。"),
    ("下列哪項最能呈現元素性質具有『週期性』？", ["元素依原子序排列後，某些性質會按規律重複出現", "每個元素的性質都完全沒有規律", "所有元素的熔點都相同", "元素只依發現者姓名排列"], "A", "週期性表示性質會隨原子序增加呈現規律性的重現，不表示所有元素性質相同。"),
    ("在簡化週期表中，氦、氖、氬同屬性質相近的一群，最合理的解釋是什麼？", ["它們位於同一族，最外層電子排列具有相似性", "它們的原子序完全相同", "它們都是由同一個原子組成", "它們必然有相同的質量"], "A", "同族元素常因最外層電子排列相近而具有相似的化學性質；原子序與質量仍各有差異。"),
    ("若要比較同一週期中兩種元素的位置，哪項資料最可靠？", ["元素的原子序與週期表位置", "元素名稱的筆畫數", "樣品包裝的顏色", "發現者的出生地"], "A", "原子序與週期表位置是判斷元素排列與週期關係的科學資料，其他項目與週期性無關。"),
    ("下列何者最可能是週期表右側常見的非金屬元素特徵？", ["通常不具金屬光澤，且部分元素容易形成共價化合物", "一定能延展成金屬薄片", "一定能導電且有金屬光澤", "一定在室溫下都是固體"], "A", "右側多為非金屬，常缺乏金屬光澤；但不同非金屬的狀態與反應方式仍可能不同。"),
    ("若一組元素在週期表中由上而下排列，且它們屬於同一族，最合理的比較方法為何？", ["比較它們最外層電子與反應性是否呈現規律變化", "直接假定它們的原子序相同", "只比較元素符號的長短", "忽略週期表位置而猜測顏色"], "A", "同族元素可從最外層電子與相關性質比較規律；不可把同族誤解成原子序相同。"),
    ("某元素的原子序為 12，另一元素的原子序為 13。關於兩者在週期表中的關係，何者最合理？", ["兩元素相鄰排列，但不代表它們的化學性質完全相同", "兩元素一定是同一種元素", "兩元素一定位於不同週期", "兩元素的質子數都為 12"], "A", "原子序連續的元素通常在週期表相鄰，但每增加一個質子就成為不同元素，性質不會完全相同。"),
    ("使用週期表預測未知元素性質時，哪種做法最符合科學探究？", ["先依位置找同族或同週期元素，再用資料檢驗推論", "只依元素名稱猜測", "把一個元素的所有性質直接套給其他元素", "不查原子序便下定論"], "A", "週期表可提供比較與預測的線索，但預測仍須用可靠資料與實驗結果檢驗。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-aa-iv-4-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考自然科；元素週期表與性質規律判讀能力方向之獨立改編；官方答案表：{ANSWER}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style science periodicity questions")
