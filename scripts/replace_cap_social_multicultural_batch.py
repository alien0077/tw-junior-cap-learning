#!/usr/bin/env python3
"""Replace the multiculturalism template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-geo-be-iv-2"
KID = "kg-social-content-geo-be-iv-2"
SOURCE = "https://www.grow22.com/download/114/114_cp/04_114P_Society.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列哪項最能說明『多元文化』的意義？", ["同一社會中存在不同群體的語言、信仰、生活方式與價值觀", "所有人都必須使用完全相同的語言與習俗", "只有人口最多的群體才有文化", "不同文化之間不能有任何交流"], "A", "多元文化指社會中存在多種文化樣貌；不同群體可以保有特色，也可能彼此交流。"),
    ("班級舉辦文化交流活動，最符合尊重多元文化的做法是什麼？", ["讓各組說明自己的文化經驗，並以平等態度互相理解", "要求少數群體只能介紹多數群體的習俗", "先用刻板印象替每個群體下結論", "禁止同學提出不同看法"], "A", "文化交流應提供平等表達與理解的機會，不能以人數或權力決定誰可以發聲。"),
    ("觀察到某地的飲食習慣與自己不同時，哪種判斷方式較恰當？", ["先了解其歷史、環境與社會脈絡，再以證據分析", "直接認定自己的飲食習慣一定比較進步", "只依網路留言判定整個群體", "把單一個人的選擇當成所有人的共同特徵"], "A", "分析文化現象需放回其歷史與環境脈絡，並避免以單一案例或自身標準概括整個群體。"),
    ("某城市同時可見傳統市場、外籍移民商店與不同語言的招牌，這種現象最可能反映什麼？", ["人口流動與文化交流使城市呈現多元樣貌", "城市居民必然沒有任何共同規範", "不同文化一定彼此衝突而無法共存", "招牌語言可以直接決定居民的國籍"], "A", "人口移動與交流會使城市出現多種語言、飲食與生活樣貌，但不能由單一現象推論所有居民的身分。"),
    ("下列哪項資料最適合用來判斷某校學生的語言文化多樣性？", ["匿名且經同意蒐集的語言使用調查與訪談資料", "一名學生的穿著印象", "社群平台未查證的留言", "校外人士對學生的猜測"], "A", "要分析群體文化樣貌，需使用有適當範圍、來源與方法的資料，不能以個人印象取代調查。"),
    ("若新聞把少數個案的行為描述成整個族群的共同特徵，讀者應優先注意什麼？", ["樣本是否足以代表整個族群，以及是否有刻板化推論", "標題是否使用醒目的顏色", "文章分享次數是否很多", "作者是否使用很長的句子"], "A", "從少數個案推論整個族群可能造成刻板印象，應檢查樣本、證據與推論範圍。"),
    ("兩個文化群體因公共空間使用方式不同而發生爭議，較合理的處理方式是什麼？", ["了解雙方需求，依共同規則協商可兼顧的方案", "要求其中一方完全放棄自己的文化需求", "以人數多寡直接否定少數意見", "不蒐集資訊便在社群公開指責"], "A", "多元文化社會的爭議可透過理解需求、共同規則與協商處理，兼顧權利與公共秩序。"),
    ("某項外來節慶在本地流行，並與原有習俗結合形成新的活動，這最能說明什麼？", ["文化會在接觸與交流中變遷並產生新的形式", "文化一旦交流就會完全消失", "文化只能由政府單方面創造", "外來文化必然比本地文化優越"], "A", "文化接觸可能帶來調整、融合與創新，不能簡化為一方必然取代另一方。"),
    ("比較不同地區的宗教建築時，哪種說法較符合多元文化觀點？", ["描述各自的功能與脈絡，不以單一文化標準判定高下", "只要外觀不同就認定其中一方錯誤", "以建築大小判斷信仰價值", "假定所有宗教建築功能完全相同"], "A", "比較文化現象應說明其脈絡與功能，避免以單一標準作武斷的價值排序。"),
    ("學校要設計多元文化課程，哪項做法最能避免流於表面？", ["使用可追溯資料，呈現群體內部差異並讓相關人士參與", "只安排服飾展示而不說明歷史背景", "用幾個固定標籤代表所有成員", "只選最容易被嘲笑的習俗作為話題"], "A", "完整的多元文化學習需有來源、脈絡與群體內部差異，也應避免把文化簡化成標籤或獵奇展示。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-geo-be-iv-2-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考社會科；多元文化、文化交流與資料判讀能力方向之獨立改編；官方答案表：{ANSWER}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style social multicultural questions")
