#!/usr/bin/env python3
"""Replace the particle-model/states template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-science-content-ab-iv-1"
KID = "kg-science-content-ab-iv-1"
SOURCE = "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("依粒子模型比較固體、液體與氣體，下列何者正確？", ["固體粒子排列較緊密，主要在固定位置附近振動", "液體粒子完全不能移動", "氣體粒子彼此緊密且只能振動", "三態粒子的大小會因狀態改變而消失"], "A", "固體粒子排列緊密並在平衡位置附近振動；液體可流動，氣體粒子間距較大且運動較自由。"),
    ("水倒入不同形狀的容器後，水面形狀改變但體積大致不變，這最能說明液體具有何種特性？", ["沒有固定形狀但有大致固定體積", "同時沒有固定形狀與固定體積", "具有固定形狀且不能流動", "粒子間完全沒有空隙"], "A", "液體可流動並隨容器改變形狀，但在一定條件下體積大致固定。"),
    ("把裝有空氣的針筒前端封住，再推動活塞，活塞仍可向內移動，主要原因為何？", ["氣體粒子間有較大空間可被壓縮", "氣體粒子沒有質量", "氣體會自動變成固體", "針筒內沒有任何粒子"], "A", "氣體粒子間距通常較大，外力可使粒子平均距離變小，因此氣體具有可壓縮性。"),
    ("香水瓶在教室一端打開後，過一會兒另一端也能聞到香味，最適合用哪項模型解釋？", ["氣味分子在空氣中不規則運動並逐漸擴散", "氣味只沿著地板直線滑動", "空氣粒子完全靜止等待香味到達", "香味是光線反射到鼻子"], "A", "氣體粒子不斷做不規則運動，香味分子會由濃度較高處向周圍擴散。"),
    ("冰塊融化成水時，若沒有物質逸出，哪項說法最符合粒子模型？", ["粒子種類不變，排列與運動方式改變", "每個粒子都變成另一種元素", "粒子數量必然變成零", "粒子大小必然增加十倍"], "A", "熔化是物態改變，物質種類與粒子本身不變，粒子的排列及可移動程度改變。"),
    ("下列哪種狀態最容易被壓縮？", ["氣體", "液體", "固體", "三者完全相同"], "A", "氣體粒子間距較大，施加外力時平均距離較容易縮小，因此最容易被壓縮。"),
    ("在密閉容器中，水蒸氣冷凝成液態水後，關於粒子的敘述何者正確？", ["粒子仍存在，只是彼此距離與運動狀態改變", "粒子全部消失，所以質量變成零", "粒子轉換成空氣中的氧氣", "粒子數量必然增加一倍"], "A", "冷凝是氣態變液態，水分子仍存在；狀態改變主要反映粒子間距離與運動狀態改變。"),
    ("比較同一物質的固態與液態，哪項差異最合理？", ["液態粒子可彼此滑動，所以液體能流動", "固態沒有粒子而液態才有粒子", "液態粒子一定比固態粒子小", "固態粒子必然停止所有運動"], "A", "液體粒子仍相互接近，但可在一定範圍內互相滑動；固體粒子則受位置限制較大。"),
    ("將一滴紅墨水分別滴入冷水與溫水，溫水較快均勻變色，最合理的推論是什麼？", ["溫度較高時水粒子平均運動較快，擴散較快", "溫水中的水粒子完全靜止", "紅墨水在溫水中必然變成固體", "冷水沒有任何粒子"], "A", "在其他條件相近時，溫度較高通常使粒子運動更劇烈，因此擴散所需時間較短。"),
    ("若要用模型說明氣球受熱後體積可能變大，哪項敘述最適當？", ["氣體粒子運動更劇烈，碰撞氣球內壁的效果改變", "氣體粒子全部沉到氣球底部", "氣球內粒子會變成液態金屬", "受熱會使所有粒子停止運動"], "A", "加熱會使氣體粒子平均運動更劇烈；在可伸縮容器中，內外壓力平衡可能在較大體積下重新建立。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "science" / f"question-science-content-ab-iv-1-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考自然科；粒子模型與三態能力方向之獨立改編；官方答案表：{ANSWER}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style science particle/state questions")
