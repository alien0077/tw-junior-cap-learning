#!/usr/bin/env python3
"""Replace one Social Studies geography lesson with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-geo-be-iv-1"
KID = "kg-social-content-geo-be-iv-1"
SOURCE = "https://www.grow22.com/download/114/114_cp/04_114P_Society.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("某沿海聚落位於河口沖積平原，地勢低平。若颱風帶來豪雨，該聚落最需要優先注意哪項自然風險？", ["河川洪水", "火山噴發", "沙漠化", "極光干擾"], "A", "河口沖積平原地勢低平，豪雨時排水與河川水位上升容易造成洪水。", "第1題地形與環境風險題型改編"),
    ("同一地區冬季降雨主要來自東北季風迎風面。若山脈阻擋水氣，背風側通常較可能出現哪種現象？", ["降雨增加", "降雨減少", "全年無風", "海水結冰"], "B", "水氣在迎風側抬升降雨，越過山脈後背風側水氣較少，通常較乾燥。", "第5題季風與地形題型改編"),
    ("某山區坡度大且植被被大量移除，豪雨後發生土石流。下列何者最能說明自然環境與災害的關聯？", ["坡度與植被狀況會影響土砂移動", "植被越少越能固定土壤", "豪雨與坡地災害沒有關係", "地勢越陡排水一定越慢且不會沖刷"], "A", "坡度、降雨與植被共同影響坡地穩定，植被移除會降低土壤保持能力。", "第1題自然災害與環境題型改編"),
    ("某地年降水量集中在夏季，冬季乾燥。居民興建水庫調節供水，這項做法主要是在回應哪項自然條件？", ["降水時間分布不均", "地球自轉停止", "潮汐完全消失", "日夜長度固定"], "A", "水庫可在降水較多時蓄水，支應降水較少的季節，回應降水時間分布不均。", "第41題水資源資料題型改編"),
    ("某島嶼位於板塊交界附近，地震頻繁且溫泉資源豐富。下列推論何者最合理？", ["地殼活動可能同時形成地震與地熱現象", "溫泉必然由海水蒸發形成", "板塊活動只會影響氣候", "地震頻繁表示沒有任何地形變化"], "A", "板塊活動會造成地震，也可能提供地熱能與溫泉形成的地質條件。", "第17題自然環境與地質題型改編"),
    ("某地森林可吸收並儲存二氧化碳。若大規模砍伐森林，最可能造成哪項影響？", ["碳匯能力下降", "大氣二氧化碳必然歸零", "降雨與植被完全無關", "所有地區氣溫立即相同"], "A", "森林是碳匯之一，砍伐會減少吸收與儲存碳的能力。", "第30題碳匯與環境題型改編"),
    ("某地日照充足、空曠少遮蔽物，政府規劃設置太陽能發電。此規劃主要利用哪項自然條件？", ["穩定的日照資源", "頻繁的地震", "高山低溫", "地下水鹽化"], "A", "太陽能發電需要利用日照；日照充足是此規劃的主要自然條件。", "第28題能源與自然環境題型改編"),
    ("研究者比較兩地降水資料：甲地全年分布平均，乙地集中於夏季。若其他條件相近，哪項判斷較合理？", ["乙地較需要季節性水資源調度", "甲地一定沒有河流", "乙地全年降水量必定較少", "兩地水資源管理完全相同"], "A", "降水季節集中會造成供水時段差異，因此較需要調度與儲水。", "第29題降水資料判讀題型改編"),
    ("某海岸有強風與飛砂，居民在聚落外圍種植防風林。這項措施主要是利用植被的哪項功能？", ["降低風速並固定部分砂土", "增加海水鹽度", "使潮汐停止", "讓所有降雨變成地下水"], "A", "防風林可降低近地面風速，根系也有助於固定土砂。", "第4題聚落與自然環境題型改編"),
    ("某地因長期乾旱而限制用水，居民改用耐旱作物。這項調整最能表現哪種人地關係？", ["人類依自然條件調整生產方式", "人類完全不受自然環境影響", "自然環境只由人口決定", "生產方式與水資源無關"], "A", "乾旱限制水資源，居民因此改種耐旱作物，呈現人類對自然條件的調適。", "第1題自然環境與人類活動題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-geo-be-iv-1-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考社會科；{locator}；官方答案表：{ANSWER}；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style Social Studies geography questions")
