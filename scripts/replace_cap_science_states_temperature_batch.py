#!/usr/bin/env python3
"""Replace the temperature/states template set with independently authored CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-ab-iv-2"
KID = "kg-science-content-ab-iv-2"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("在標準大氣壓下加熱一杯含冰塊的水，冰尚未完全融化時，溫度計讀數最可能如何變化？", ["大致維持在 0°C", "持續降到 -20°C", "立即升到 100°C", "每分鐘固定上升 10°C"], "A", "冰水混合物熔化時，吸收的熱量主要用於改變狀態，因此溫度大致維持在熔點。", "物質狀態與溫度變化題型改編"),
    ("在標準大氣壓下，水沸騰一段時間後，若火力維持不變，水的溫度通常如何？", ["大致維持在 100°C", "不斷升高到 150°C", "降到 0°C", "變成和室溫完全相同"], "A", "標準大氣壓下水的沸點約為 100°C；沸騰時熱量主要用於液態轉氣態。", "物質狀態與溫度變化題型改編"),
    ("關於固體內粒子的排列與運動，下列何者正確？", ["粒子大致在固定位置附近振動", "粒子彼此距離很大且可任意流動", "粒子完全靜止，不受溫度影響", "粒子只能沿同一方向快速移動"], "A", "固體粒子排列較緊密，主要在平衡位置附近振動；溫度升高時振動通常更劇烈。", "粒子模型與溫度題型改編"),
    ("運動後在皮膚上擦拭酒精，感覺變涼的主要原因為何？", ["酒精蒸發時吸收皮膚表面的熱量", "酒精凝固時放出大量熱量", "皮膚把所有熱量轉成光", "酒精使周圍空氣停止運動"], "A", "蒸發需要吸收熱量，酒精從皮膚表面蒸發時帶走熱能，所以皮膚感到變涼。", "蒸發吸熱題型改編"),
    ("相同質量的水與食用油接受相同加熱功率，若食用油溫度上升較快，最合理的解釋是什麼？", ["食用油在此條件下每升高 1°C 所需熱量較少", "食用油一定比水的沸點低", "水完全不會吸收熱量", "兩者的質量其實必然不同"], "A", "在質量與加熱條件相同時，升溫較快表示每升高相同溫度所需的熱量可能較少；不能僅由此判定沸點。", "比熱與升溫資料判讀題型改編"),
    ("冰塊放在室內桌面上逐漸融化，從固態變成液態的過程需要哪種能量變化？", ["吸收周圍熱量", "向周圍放出全部熱量", "完全不涉及能量", "只改變質量而不改變狀態"], "A", "熔化是固態變液態的吸熱相變，冰會從周圍環境吸收熱量。", "熔化能量變化題型改編"),
    ("將水加熱並記錄溫度，若溫度—時間圖在一段時間出現水平線，且液體持續產生氣泡，該段最可能代表什麼？", ["液體正在沸騰，熱量用於汽化", "溫度計一定已經損壞", "水正在凝固且沒有能量變化", "容器內完全沒有水"], "A", "沸騰時溫度在一定條件下大致不變，持續輸入的熱量用於液體汽化。", "溫度—時間圖表判讀題型改編"),
    ("在高山上煮水時，水可能在低於 100°C 時就沸騰，主要原因是什麼？", ["高山的大氣壓通常較低", "高山的水分子全部消失", "重力在高山完全不存在", "水在高山必然變成固體"], "A", "外界大氣壓降低時，液體較容易達到沸騰條件，因此沸點可能降低。", "沸點與外界壓力題型改編"),
    ("把 80°C 的金屬塊放入 25°C 的水中並隔絕外界熱交換，最後兩者溫度相同，這表示什麼？", ["熱量由金屬傳給水直到達到熱平衡", "水把熱量傳給金屬直到金屬更熱", "金屬與水都沒有發生能量交換", "最後溫度必然仍是 80°C"], "A", "在隔絕外界的條件下，較熱物體把熱量傳給較冷物體，直到兩者達到相同溫度。", "熱傳與熱平衡題型改編"),
    ("下列哪項現象最能支持「溫度升高時，物質粒子平均運動較劇烈」的模型？", ["溫水中的色素擴散通常比冷水快", "冰塊的形狀固定不會改變", "量筒有刻度可以讀取體積", "金屬匙有固定的長度"], "A", "溫度較高時粒子運動較劇烈，會使色素在水中較快擴散；這是模型對可觀察現象的解釋。", "粒子模型與擴散現象題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-ab-iv-2-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考自然科；{locator}；官方答案表：{ANSWER}；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style science temperature/state questions")
