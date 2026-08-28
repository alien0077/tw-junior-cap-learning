#!/usr/bin/env python3
"""Replace the Southern Africa environment/resources template set."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-geo-bg-iv-1"
KID = "kg-social-content-geo-bg-iv-1"
SOURCE = "https://www.grow22.com/download/114/114_cp/04_114P_Society.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/819/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E7%A4%BE%E6%9C%83%E9%A0%98%E5%9F%9F.pdf"

rows = [
    ("漢南非洲內陸部分地區降水較少，若地圖顯示沿海與內陸降水量不同，最合理的分析方法為何？", ["比較緯度、距海遠近、地形與風向等條件", "只看地名是否含有『海』字", "假定整個漢南非洲降水量完全相同", "只用人口數推算降水量"], "A", "自然環境分析需綜合位置、距海遠近、地形與大氣運動等因素，不能只依地名或人口推論。"),
    ("漢南非洲部分草原地區有明顯乾濕季，居民安排放牧活動時最需要參考什麼？", ["季節降水與水源分布", "城市招牌顏色", "海港的建築高度", "礦石名稱的字數"], "A", "乾濕季會影響牧草與水源，放牧安排需參考季節降水及水源位置。"),
    ("某地發現礦產後修築鐵路連接港口，最可能的主要目的為何？", ["便於礦產運往外地市場，降低運輸阻礙", "使該地降水量立即增加", "讓所有居民改住港口", "消除礦產開採的環境成本"], "A", "鐵路連接礦區與港口可改善資源運輸，但不會自動消除開採造成的環境與社會成本。"),
    ("比較漢南非洲兩地的資源利用時，甲地有礦產但交通不便，乙地礦產較少卻鄰近港口。下列推論何者合理？", ["交通與市場條件會影響資源開發，不只看資源是否存在", "甲地一定比乙地更富裕", "乙地因鄰近港口就必然沒有資源", "資源開發完全與交通無關"], "A", "資源能否開發與運輸、技術、市場及政策有關，不能只由資源存量判定結果。"),
    ("若草原地區長期過度放牧，最可能出現哪項環境問題？", ["植被減少、土壤侵蝕與土地退化", "地下水必然無限增加", "所有野生動物數量必然上升", "降水會立刻固定增加"], "A", "牲畜數量與放牧強度超過土地承載力，可能造成植被破壞、土壤侵蝕與土地退化。"),
    ("某統計表顯示一國礦產出口增加，但當地居民平均收入沒有同步增加。研究者應如何解讀？", ["檢查收益分配、就業型態、外資比例與統計範圍", "直接結論是礦產出口完全沒有價值", "只要出口增加就代表人人受益", "只比較國土面積即可解釋收入"], "A", "出口總額不等於居民平均受益，需檢查收益分配、產業結構與統計對象。"),
    ("在水資源有限的地區興建大型灌溉農場前，最應先評估哪項資料？", ["可用水量、補注速度、作物需水量與旱季風險", "農場名稱是否好記", "只看雨季一天的降雨量", "只比較農場圍牆顏色"], "A", "水資源規劃要考慮長期供需、補注、作物用水與旱季風險，不能只看單日降雨。"),
    ("某地同時有野生動物棲地與礦產開採計畫，較完整的地理評估應包含什麼？", ["比較經濟收益、棲地影響、居民需求與替代方案", "只計算礦石重量", "只看野生動物照片而不查位置", "認定保育與發展必然無法協商"], "A", "地理議題需把資源利用、環境保育、居民需求與替代方案放在同一分析架構中。"),
    ("若地圖顯示沙漠邊緣的聚落多分布在河流或地下水附近，最合理的推論為何？", ["水源是限制聚落分布與生活活動的重要因素", "沙漠地區完全沒有任何人口", "河流會使所有地區變成熱帶雨林", "聚落位置只由國界決定"], "A", "在乾燥環境中，穩定水源會影響聚落、農業與交通分布，但仍需配合地圖和其他資料確認。"),
    ("面對漢南非洲自然資源開發議題，哪項做法最符合永續發展的觀點？", ["依環境承載力規劃開採，並保留復育、收益分配與長期監測", "只追求短期出口量而不記錄環境變化", "把所有資源一次開採完再處理後果", "只由外地企業決定而不詢問當地居民"], "A", "永續利用要考量承載力、復育、監測與公平分配，不能只追求短期產量或出口。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-geo-bg-iv-1-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考社會科；漢南非洲自然環境與資源資料判讀能力方向之獨立改編；官方答案表：{ANSWER}；課綱定位：{CURRICULUM}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style Southern Africa environment/resource questions")
