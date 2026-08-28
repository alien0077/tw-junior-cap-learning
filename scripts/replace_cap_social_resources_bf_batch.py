#!/usr/bin/env python3
"""Replace the natural-resources template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-geo-bf-iv-1"
KID = "kg-social-content-geo-bf-iv-1"
SOURCE = "https://www.grow22.com/download/114/114_cp/04_114P_Society.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列何者最符合『自然資源』的定義？", ["自然環境中可被人類利用以滿足需求的物質或能量", "只有經過工廠製造的商品", "只存在於城市中的建築物", "任何人類的想法或制度"], "A", "自然資源是自然環境提供、可被人類利用的物質或能量，例如水、森林、礦產與風能。"),
    ("下列哪一項屬於再生資源，但仍可能因過度使用而枯竭？", ["森林", "煤炭", "石油", "金屬礦藏"], "A", "森林在適當管理下可再生，但砍伐速度若超過恢復速度，仍會退化或枯竭。"),
    ("某地地下水抽取量長期高於自然補注量，最可能造成什麼結果？", ["地下水位下降，甚至引發地層下陷或供水風險", "地下水一定會自動增加", "所有河流流量必然上升", "土壤必然變成礦產"], "A", "抽取超過補注會使地下水存量下降，可能造成地層下陷、海水入侵或供水不穩。"),
    ("若要判斷一地適不適合發展風力發電，最需要優先分析哪項資料？", ["長期風速、風向與地形資料", "居民姓名的筆畫", "附近商店的招牌顏色", "歷年節慶的日期"], "A", "風力發電的效率與風況密切相關，需分析長期風速、風向、地形及環境限制。"),
    ("某國以進口石油為主要能源，國際油價突然上升時，最可能面臨什麼問題？", ["能源成本上升，且供應容易受外部市場影響", "國內石油儲量必然增加", "所有再生能源立即消失", "交通需求必然完全停止"], "A", "高度依賴進口能源時，價格與供應會受到國際市場或運輸情勢影響。"),
    ("下列哪項政策最符合自然資源永續利用？", ["設定捕撈限額並依族群數量監測調整", "為增加短期產量而取消所有保育規定", "只開採容易取得的資源而不記錄存量", "把污染成本完全轉嫁給下游居民"], "A", "依資源恢復能力設定限額、持續監測並調整，是兼顧利用與保育的做法。"),
    ("某地圖顯示礦產集中在山區，而工業區位於沿海平原。若礦產要運往工業區，哪項因素最值得比較？", ["交通路線、運輸成本與地形障礙", "礦石名稱的字數", "居民喜歡的運動種類", "地圖紙張的顏色"], "A", "資源運輸需考慮距離、路線、地形與成本，不能只看資源與工業區的直線位置。"),
    ("城市推動節水設備後，家庭用水量下降，但人口仍增加。若要判斷政策效果，還應比較什麼？", ["政策前後的人均用水量與降雨等外在條件", "只比較城市面積", "只看宣傳標語的數量", "只詢問一戶居民的感受"], "A", "人口變化會影響總用水量，應比較人均用水量並控制降雨等因素，才能判斷節水政策效果。"),
    ("開採礦產可能帶來工作機會，也可能破壞生態環境。評估是否開採時，哪種方法較完整？", ["同時比較經濟收益、環境成本、居民意見與復育方案", "只看短期稅收而忽略環境", "只要有人反對就不必蒐集資料", "只用礦產市場價格決定一切"], "A", "資源開發涉及多方利害與長期影響，需把經濟、環境、社會與復育資料一併評估。"),
    ("下列哪項最能說明不同地區會發展不同的資源利用方式？", ["自然條件、技術、需求與政策彼此作用", "所有地區的自然環境完全相同", "資源利用只由地名決定", "只要有資源就必然採用相同技術"], "A", "資源利用方式不只受自然分布影響，也會受到技術、社會需求、交通與政策影響。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-geo-bf-iv-1-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考社會科；自然資源分布、利用與永續發展能力方向之獨立改編；官方答案表：{ANSWER}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style social natural-resource questions")
