#!/usr/bin/env python3
"""Replace one global-warming lesson with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-me-iv-4"
KID = "kg-science-content-me-iv-4"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("工廠將排放的二氧化碳注入地下，使其與礦物反應形成碳酸鹽。此方法的主要目的為何？", ["增加大氣中的二氧化碳", "將二氧化碳長期封存", "使氧氣變成燃料", "提高化石燃料用量"], "B", "將二氧化碳轉成岩石中的碳酸鹽，可把碳長期固定，降低進入大氣的量。", "第19題二氧化碳礦化封存題型改編"),
    ("下列哪項活動通常會增加溫室氣體排放？", ["燃燒煤炭發電", "搭乘大眾運輸", "植樹造林", "使用太陽能發電"], "A", "煤炭燃燒會排放二氧化碳等溫室氣體；其餘選項通常有助於減少排放或增加碳匯。", "第19題溫室氣體來源題型改編"),
    ("若某地森林面積增加且其他條件相近，最可能造成哪項變化？", ["碳匯能力增加", "大氣氧氣立即歸零", "地球停止吸收輻射", "所有溫度立即相同"], "A", "植物生長可吸收並儲存二氧化碳，因此森林增加通常會提升碳匯能力。", "第19題碳匯概念題型改編"),
    ("下列何者最適合用來比較兩種交通工具的減碳效果？", ["只比較車身顏色", "記錄相同距離的燃料或能源消耗與排放量", "只詢問駕駛喜好", "只看車輛大小"], "B", "比較減碳效果需控制行駛距離等條件，並記錄能源消耗或排放量。", "第41題資訊圖表判讀題型改編"),
    ("標示「低碳」的燃料，若要判斷其減碳效果，最需要查閱哪項資料？", ["燃料包裝顏色", "單位能源的生命週期排放量", "車輛座位數", "駕駛人的年齡"], "B", "低碳判斷需比較從生產、運輸到使用的排放，不能只看標籤或外觀。", "第41題燃料資訊判讀題型改編"),
    ("某校以踩踏腳踏車帶動發電機，並記錄發電量。若要比較不同學生的發電效率，還應控制哪項條件？", ["踩踏時間與阻力設定", "學生喜歡的顏色", "教室牆面材質", "當天午餐內容"], "A", "比較效率時應控制踩踏時間、阻力等條件，才可將差異歸因於研究因素。", "第42題節能活動與變因題型改編"),
    ("下列哪項最能直接降低家庭使用電力造成的二氧化碳排放？", ["長時間開啟不使用的電器", "以高耗能模式運轉", "關閉不使用的電器並選擇高效率設備", "增加待機設備數量"], "C", "減少不必要用電並提高能源效率，可降低發電所需燃料與相關排放。", "第42題節能行動題型改編"),
    ("溫室氣體濃度上升與全球暖化的關係，何者最合理？", ["溫室氣體可吸收部分地表放出的紅外線，使熱能較不易散失", "溫室氣體會阻止所有陽光進入地表", "溫室氣體只存在於水中", "溫室氣體增加必然使每一天都更冷"], "A", "溫室氣體吸收地表放出的部分紅外線，會影響地球能量收支，濃度增加可能造成暖化。", "第19題溫室效應概念題型改編"),
    ("某城市植樹、改善大眾運輸並提高建築節能標準。這些措施分別可能對應哪種方向？", ["增加排放、增加排放、增加排放", "增加碳匯、減少燃料使用、提高能源效率", "減少碳匯、增加燃料使用、降低效率", "都與氣候沒有關係"], "B", "植樹可增加碳匯，大眾運輸可減少單人交通排放，節能標準可提高能源使用效率。", "第41至42題減碳措施整合題型改編"),
    ("若實驗想研究不同植物數量對二氧化碳濃度的影響，哪項設計最合理？", ["只改變植物數量並控制光照、時間與容器條件", "同時改變植物種類、光照和溫度", "不測量二氧化碳濃度", "只觀察研究者的感覺"], "A", "一次主要改變一項變因並控制其他條件，才能判斷植物數量的影響。", "第42題科學探究與變因題型改編"),
]

for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-me-iv-4-{index}.json"
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
print(f"replaced {len(rows)} CAP-style science global-warming questions")
