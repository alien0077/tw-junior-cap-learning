#!/usr/bin/env python3
"""Replace the trade/cultural-exchange template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-hist-ia-iv-2"
KID = "kg-social-content-hist-ia-iv-2"
SOURCE = "https://www.grow22.com/download/114/114_cp/04_114P_Society.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("歷史上的商貿活動除了交換商品，也可能帶來什麼影響？", ["促進技術、宗教、語言與生活方式的交流", "使所有地區立即使用完全相同的文化", "只會改變商品價格而不影響社會", "讓不同地區永遠停止往來"], "A", "商貿往來常伴隨人員移動與資訊流通，可能促成技術、信仰、語言與生活方式的交流。"),
    ("若古代商人選擇在河流交會處設置市集，最合理的原因是什麼？", ["交通與貨物集散較便利，容易連結不同地區", "該地必然沒有任何居民", "河流會自動生產所有商品", "市集位置只由地名長短決定"], "A", "河流交會處通常有交通與集散優勢，能降低運輸與交易的阻礙；仍需配合史料判斷實際情況。"),
    ("某海港位於季風航線附近，逐漸成為區域貿易中心。下列推論何者較合理？", ["季節性風向與港口位置可能降低航行成本並增加往來", "季風會使船隻不需要任何導航", "海港只要有季風就必然統治內陸", "貿易中心的形成與交通條件無關"], "A", "季風與港口位置可影響航行時機與交通成本，但貿易中心還會受到市場、政治與安全等因素影響。"),
    ("考古發現某地陶器使用外地技術，但器形仍保留本地特色。最合理的解讀是什麼？", ["技術可能透過交流傳入，並在本地被重新調整", "外地技術傳入後本地文化必然完全消失", "陶器外形可以直接證明所有居民來自外地", "技術不可能跨地區傳播"], "A", "文化交流可能帶來技術傳播與在地轉化；單一器物不能直接證明整個人口的來源。"),
    ("研究一條古代商路的影響時，哪種證據組合最有助於建立較可靠的結論？", ["路線圖、交易紀錄、遺址出土物與不同時期的文字史料互相比對", "只看一則未標年代的傳說", "只用現代道路位置推測古代交通", "只依商路名稱猜測商品種類"], "A", "多種來源交叉比對可檢查路線、年代、商品與交流影響，避免從單一傳說過度推論。"),
    ("某地因貿易興盛而增加稅收，但港口附近也出現環境負擔。這反映商貿發展可能具有什麼特徵？", ["同一項發展可能同時帶來收益與成本", "貿易只會造成正面結果", "環境影響與人口增加必然無關", "只要稅收增加就代表所有居民受益"], "A", "商貿可帶來收入與就業，也可能增加資源、環境與分配壓力，需分別檢視不同群體的影響。"),
    ("若一項新商品沿著商路由甲地傳到乙地，再出現在丙地，最合理的歷史推論為何？", ["商路可能成為商品與相關資訊逐步傳播的管道", "商品必然由同一個人一次帶到三地", "丙地出現商品就能證明三地政治統一", "商品傳播與人員移動完全無關"], "A", "沿線出現商品可支持交流與傳播的可能性，但仍需其他史料判斷傳播方式與政治關係。"),
    ("比較兩條商路時，甲路較短但常有戰亂，乙路較長卻較安全。商人選擇路線時最可能考量什麼？", ["距離、運輸成本、安全與沿途市場等因素的整體權衡", "只看地圖上的直線長度", "只看沿途城市名稱", "假定所有商人都一定選甲路"], "A", "商路選擇不只取決於距離，還要衡量安全、成本、補給與市場需求。"),
    ("某旅行者記錄『這座城市人人都使用外地語言』，研究者發現他只訪問了港口商人。判讀時應注意什麼？", ["記錄可能只反映特定群體，不能直接代表全城居民", "旅行者到過港口就能代表所有居民", "外地語言出現就表示本地語言消失", "個人記錄不需要考慮觀察範圍"], "A", "史料的觀察對象與範圍會影響結論；港口商人的語言使用不能直接概括整座城市。"),
    ("商貿往來中，外來飲食與本地食材結合形成新料理，這種現象最適合如何描述？", ["文化在交流過程中可能融合並產生在地的新形式", "文化交流必然只會單向取代", "料理改變可以直接證明政治征服", "不同文化接觸後不可能互相影響"], "A", "文化交流可能產生融合與創新，但單一料理不能單獨證明政治征服或整體文化被取代。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-hist-ia-iv-2-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考社會科；商貿路線、商品流通與文化交流資料判讀能力方向之獨立改編；官方答案表：{ANSWER}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style social trade/exchange questions")
