#!/usr/bin/env python3
"""Replace the Americas environment template set."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-geo-bi-iv-1"
KID = "kg-social-content-geo-bi-iv-1"
SOURCE = "https://www.grow22.com/download/114/114_cp/04_114P_Society.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/819/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E7%A4%BE%E6%9C%83%E9%A0%98%E5%9F%9F.pdf"

rows = [
    ("美洲南北跨越多種緯度，對自然環境分布最可能造成什麼影響？", ["氣候類型由寒帶到熱帶呈現多樣性", "整個美洲全年氣溫完全相同", "所有地區都具有相同的降水季節", "緯度與氣候分布沒有任何關係"], "A", "美洲南北延伸廣，跨越多種緯度，因此氣溫與氣候類型具有明顯多樣性；仍需配合地形與海陸位置分析。"),
    ("安地斯山脈大致沿南美洲西側延伸，若觀察地形圖，最合理的描述為何？", ["西部山地較集中，東部有較廣的平原與低地", "山脈平均分布在南美洲每個角落", "東部完全沒有河流與平原", "山脈位置由人口數量決定"], "A", "安地斯山脈位於南美洲西側，東側有亞馬遜盆地等低地；地形圖可支持這種相對位置判讀。"),
    ("亞馬遜盆地接近赤道且降水豐富，最可能形成哪種自然景觀？", ["熱帶雨林", "極地冰原", "全年乾燥的沙漠", "高緯度苔原"], "A", "接近赤道且高溫多雨的環境有利於熱帶雨林形成，但實際分布仍會受到地形與水氣來源影響。"),
    ("若地圖顯示亞馬遜河水系廣大，這對當地自然環境與人類活動可能有何意義？", ["提供水源與交通條件，也形成洪水與保育等議題", "代表整個流域沒有任何季節變化", "使所有土地都適合密集都市化", "河流會自動消除森林砍伐影響"], "A", "大型河流水系可提供水源與交通，但也可能帶來洪水、環境管理與森林保育等問題。"),
    ("北美洲中部平原較適合大規模農業時，最需要綜合考量哪些自然條件？", ["地形平坦、土壤、降水與灌溉條件", "只看城市名稱是否相同", "只看山脈的顏色", "人口數就能完全決定農業分布"], "A", "農業分布需綜合地形、土壤、水分與灌溉等條件，不能只靠單一地圖符號或人口數推論。"),
    ("美洲西側有高大的山脈，若比較山脈兩側的降水量，最應注意哪項可能因素？", ["地形抬升與背風側的雨影效應", "山脈會使兩側降水永遠相同", "降水只由國界線決定", "高山一定會讓兩側都變成雨林"], "A", "山脈會影響氣流抬升與水氣分布，背風側可能較乾燥；需用降水與風向資料驗證。"),
    ("若研究加勒比海島嶼的自然災害風險，哪項資料最值得優先查看？", ["颱風路徑、海岸地形、降雨與人口分布", "島名的字數", "居民最常使用的服裝顏色", "只看一張沒有日期的照片"], "A", "災害風險需結合氣象、地形、時間與人口暴露資料，不能只靠島名或單張照片判斷。"),
    ("比較北美洲高緯度地區與中美洲低緯度地區的自然環境，哪項推論最合理？", ["緯度差異可能造成溫度、植被與農業條件不同", "兩地必然有完全相同的植被", "低緯度地區一定沒有任何高地", "高緯度與低緯度不會影響生活方式"], "A", "緯度會影響熱量，進而影響植被與農業條件；但地形、海流與人類活動也需一併考量。"),
    ("某地圖把南美洲森林分布與道路建設疊圖，若道路深入森林，最適合提出哪項研究問題？", ["道路分布是否與森林開發、聚落及保育衝突有關", "道路顏色是否決定樹木種類", "森林面積增加就能證明道路沒有影響", "只要有道路就代表整片森林已消失"], "A", "疊圖可用來提出空間關聯問題，但是否存在因果仍需時間序列與其他資料檢驗。"),
    ("閱讀美洲自然環境資料時，哪種結論最為謹慎？", ["先指出資料顯示的區域與範圍，再說明可能原因及限制", "把一個國家的氣候套用到整個美洲", "忽略圖例後直接判斷資源分布", "只用單一現象斷定所有地區的自然環境"], "A", "地理資料判讀應交代範圍、證據、可能原因與限制，避免由局部資料過度推論整個洲。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-geo-bi-iv-1-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考社會科；美洲自然環境背景與地圖判讀能力方向之獨立改編；官方答案表：{ANSWER}；課綱定位：{CURRICULUM}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style Americas environment questions")
