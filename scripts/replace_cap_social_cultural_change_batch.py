#!/usr/bin/env python3
"""Replace the social/cultural-change template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-hist-eb"
KID = "kg-social-content-hist-eb"
SOURCE = "https://www.grow22.com/download/114/114_cp/04_114P_Society.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列哪項最能說明社會文化會產生變遷？", ["科技、經濟、政治與人口流動等因素可能共同影響生活方式", "文化一旦形成就永遠不會改變", "只有自然環境能改變文化", "文化變遷只由單一人物決定"], "A", "社會文化變遷通常受到多項因素交互影響，例如技術、經濟制度、政治環境與人口移動。"),
    ("研究某地百年前後的家庭生活時，哪項資料最有助於比較變化？", ["不同時期的日記、照片、統計或訪談等可追溯資料", "現在一名居民的印象", "未標示年代的網路圖片", "只看地名是否相同"], "A", "跨時期比較需要確認年代與來源，並使用多種可追溯資料，避免以現代個人印象代替歷史證據。"),
    ("工業化後許多人由鄉村移居城市，城市人口增加，這種現象最可能帶來什麼影響？", ["工作型態、居住型態與公共設施需求可能改變", "所有傳統文化立即消失", "城市與鄉村的距離必然變成零", "人口移動不會影響社會關係"], "A", "工業化與都市化會影響就業、居住、交通、家庭與公共服務，但不代表所有傳統都立即消失。"),
    ("印刷技術與網路讓資訊更容易傳播，最合理的歷史解讀是什麼？", ["資訊傳播速度與範圍擴大，可能加速觀念交流與社會變化", "所有人接收的資訊必然完全相同", "技術會自動決定每個人的想法", "資訊傳播越快就沒有錯誤資訊"], "A", "傳播技術會改變資訊流通條件，但人們的接收、判斷與社會制度仍會影響結果。"),
    ("某地保留傳統節慶，同時加入新的音樂與環保做法，這最能說明什麼？", ["文化可能在延續中調整與創新", "傳統與創新必然互相排斥", "只要加入新元素就不再是文化", "文化只能由政府規定"], "A", "文化變遷不一定等於完全取代，原有傳統也可能在新情境中調整、融合與創新。"),
    ("大量移民進入一座城市後，飲食、語言與商業活動出現新的樣貌。分析此現象時，最應注意什麼？", ["移民帶來交流，也要區分不同群體內部的差異", "把所有移民視為完全相同的群體", "認定外來文化必然取代本地文化", "只用一家餐廳推論整座城市"], "A", "人口移動可能帶來文化交流，但不同群體內部仍有差異，不能以單一案例或刻板印象概括。"),
    ("某項新交通工具出現後，通勤時間縮短，但沿線房價上升。這個案例提醒我們如何理解科技變遷？", ["科技可能帶來便利，也可能伴隨不同群體受到的成本與影響", "科技只會產生正面結果", "房價與交通完全沒有關聯", "只要有新科技所有人都會同樣受益"], "A", "社會變遷的影響可能同時有利有弊，且不同群體承受的成本與獲益不一定相同。"),
    ("時間軸顯示某制度先改變，數十年後家庭分工才逐漸改變。最合理的解讀為何？", ["制度變化與生活文化變化可能有時間差，不能假定同時發生", "後發生的事件一定造成先發生的事件", "時間軸無法用來比較先後", "兩項變化必然完全無關"], "A", "制度、經濟與生活文化的變化可能不同步，需依時間順序與其他證據分析因果，不能只看先後。"),
    ("比較不同年代女性受教育比例時，若比例上升，哪項結論較謹慎？", ["資料顯示受教育機會可能擴大，但仍需檢查地區、階級與資料範圍", "因此所有女性的生活都完全相同", "比例上升代表其他不平等已全部消失", "只要一項統計就能說明所有社會面向"], "A", "統計可支持特定範圍的結論，但仍要注意樣本、地區與其他社會條件，避免過度推論。"),
    ("地方青年把傳統工藝與現代設計結合，並透過網路銷售。這種現象最適合如何描述？", ["在全球交流與新技術條件下，地方文化可能重新詮釋並擴大傳播", "地方文化因此必然失去所有特色", "網路只能傳播相同文化", "現代設計與傳統工藝不可能同時存在"], "A", "文化可在交流與科技條件下重新詮釋；傳統與現代不必然互斥，也不能直接推論特色消失。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-hist-eb-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考社會科；社會文化變遷、資料判讀與因果分析能力方向之獨立改編；官方答案表：{ANSWER}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style social cultural-change questions")
