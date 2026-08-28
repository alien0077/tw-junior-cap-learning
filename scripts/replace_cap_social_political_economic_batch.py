#!/usr/bin/env python3
"""Replace one Social Studies history topic with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-hist-ea"
KID = "kg-social-content-hist-ea"
SOURCE = "https://www.grow22.com/download/114/114_cp/04_114P_Society.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("某國政府以法律保障不同信仰者在城市中依自身習俗生活，這項制度最能反映哪種政治變遷？", ["統治者對多元社會的治理調整", "封建制度更加封閉", "取消所有地方自治", "禁止跨文化交流"], "A", "保障不同信仰者的生活習俗，表示統治者因應多元社會而調整治理方式。", "第8題制度與社會變遷題型改編"),
    ("第一次世界大戰後，戰勝國召開國際會議處理戰敗國問題。這類會議主要反映哪種政治現象？", ["戰後國際秩序的重新安排", "工業革命尚未開始", "地方市集的形成", "宗教改革的起源"], "A", "戰爭結束後由各國協商領土與國際關係，屬於戰後國際秩序重組。", "第9題國際會議與政治變遷題型改編"),
    ("某統治者透過官僚制度將地方稅收與行政權集中到中央，這項措施最可能造成什麼結果？", ["中央對地方的控制增強", "地方完全脫離國家", "商業活動必然消失", "所有人民取得相同官職"], "A", "稅收與行政權集中，通常會提高中央政府對地方的控制能力。", "第21題制度變遷題型改編"),
    ("一座港口位於兩個海域之間的狹窄水道，控制該處可影響船舶往來。此地的政治經濟重要性主要來自什麼？", ["交通位置與貿易通道", "全年沒有居民", "完全不受地形影響", "只能發展牧業"], "A", "狹窄水道是船舶往來的通道，位置會影響貿易與政治控制。", "第27題交通位置與經濟互動題型改編"),
    ("某地大量出口加工食品，主要進口機械設備；多年後工廠使用新技術提高產量。這最能說明哪項經濟變遷？", ["國際貿易與產業技術互相影響", "貿易會使所有國家停止生產", "進口設備與產量沒有關係", "出口只能交換文化用品"], "A", "出口產業、進口設備與技術升級之間有關聯，反映國際分工與產業變化。", "第33題貿易資料判讀題型改編"),
    ("政府修築鐵路連接農業區與港口，農產品較快運往外地。此建設最可能帶來哪項影響？", ["降低運輸阻礙並擴大市場", "使農業區與市場完全隔離", "使交通時間必然增加", "禁止商品跨區流通"], "A", "鐵路連接產地與港口，可降低運輸成本與時間，擴大商品市場。", "第35題公共建設與經濟變遷題型改編"),
    ("若某地因勞動人口不足而引進外地勞工，政策討論最需要同時考量哪兩方面？", ["勞動需求與勞工權益", "只考量企業利潤而不看法律", "只限制交通而不看工作", "只看人口年齡而不看產業"], "A", "引進勞工同時涉及產業人力需求與勞動條件、權益保障。", "第39題勞動市場與政策題型改編"),
    ("數個國家降低彼此關稅並建立共同市場，最可能促成哪種變化？", ["區域內商品與資本往來增加", "所有國家停止對外貿易", "各國邊界完全消失", "區域內產業必然全部相同"], "A", "降低關稅與共同市場通常會增加區域內的商品與資本流動。", "第40題區域整合與經濟互動題型改編"),
    ("某地出土的商品同時具有本地工藝與外來原料特色，研究者據此推測該地曾與外地往來。這項推論主要依據什麼？", ["物質文化可作為交流與貿易的證據", "外來原料必然由本地製造", "工藝特色不能反映任何互動", "考古資料只能判斷氣候"], "A", "外來原料與工藝混合可作為人口、商品或技術交流的線索，但需配合其他證據。", "第3題跨文化交流資料題型改編"),
    ("政府設置公共回饋管道，蒐集居民對市場改建的意見，再依資料調整方案。此做法最能反映哪項變遷？", ["公共政策逐漸重視民眾參與", "政策完全不需要證據", "居民意見不能影響公共建設", "市場改建與政治無關"], "A", "蒐集居民意見並用於調整政策，反映公共治理與民眾參與的關係。", "第13題公共治理與政策資料題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-hist-ea-{index}.json"
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
print(f"replaced {len(rows)} CAP-style Social Studies political-economic questions")
