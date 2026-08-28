#!/usr/bin/env python3
"""Replace one Chinese reading/style lesson with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-chinese-performance-5-iv-3"
KID = "kg-chinese-performance-5-iv-3"
SOURCE = "https://www.grow22.com/download/114/114_cp/01_114P_Chinese.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("短文：「校園午後常有剩食。午餐部先統計三週廚餘量，再訪談同學，最後試辦減量取餐。」這段文字主要採用哪種說明方式？", ["依資料與行動說明問題及處理流程", "只用想像描寫午後景色", "以人物對話營造懸疑", "以押韻句子抒發情感"], "A", "短文先提供統計資料，再說明訪談與試辦，重點是以資料和流程說明問題處理。", "第11至12題文意與寫作分析題型改編"),
    ("短文：「這座橋白天看來樸素，然而夜晚燈光亮起後，水面便映出一條金色長廊。」文中的「然而」最主要表示什麼關係？", ["轉折", "因果", "並列", "遞進"], "A", "前句描述白天樸素，後句改寫夜晚的不同景象，兩者形成轉折。", "第33題語意關係題型改編"),
    ("文章開頭寫「窗邊有一盆未開的蘭花」，結尾寫「花終於在雨後展開」。這種安排最可能產生什麼效果？", ["前後照應，呈現變化", "打斷文章，使主旨消失", "只增加無關的時間資訊", "把說明文改成公告"], "A", "結尾回應開頭意象，讀者可看見蘭花從未開到綻放的變化，形成照應。", "第10題與第36至37題寫作分析題型改編"),
    ("短文以「我」敘述旅行，只寫自己看見的景物與當下感受，沒有說明同行者心中的想法。這種敘述方式的特點是什麼？", ["資訊受限於敘述者的觀點", "能知道所有人物的內心", "完全沒有任何觀察", "只能用對話推進情節"], "A", "第一人稱且只呈現自己的所見所感，讀者取得的資訊受敘述者觀點限制。", "第25至26題人物與寫作分析題型改編"),
    ("詩句：「夕陽沉入遠山，歸鳥掠過空村；風停後，只有竹影在窗前搖曳。」若要概括其寫景特色，何者最恰當？", ["以景物營造寧靜而略帶孤寂的氣氛", "以熱鬧人群表現歡慶場面", "以議論說明城市交通", "以誇張語氣批評制度"], "A", "遠山、空村、歸鳥與竹影共同營造安靜且帶有孤寂感的景象。", "第17至18題詩歌分析題型改編"),
    ("說明文先定義「城市熱島」，接著列出形成原因，最後以校園操場與柏油路的溫度比較作例子。這樣安排的主要作用為何？", ["由概念到原因再到具體證據，幫助理解", "只為增加文章字數", "使讀者無法掌握主題", "把不同主題任意拼接"], "A", "先定義、再說明原因、最後以例子具體化，層次清楚且有助於理解。", "第15題說明方法題型改編"),
    ("短文：「阿哲收到錄取通知，卻想起祖父為了供他讀書而長年工作。他沒有立刻慶祝，而是先回家道謝。」若要說明人物形象，何者最恰當？", ["重視感恩，能由事件推知內心", "只在意名次，完全忽略他人", "缺乏任何情緒變化", "以冷漠拒絕家人"], "A", "人物由收到通知到回家道謝的行動，顯示他記得祖父付出並具有感恩之心。", "第20題與第25題人物理解題型改編"),
    ("文章先寫「村民都說老樹即將倒下」，後文記錄樹醫檢查後發現主幹仍健康，並提出支架加固方案。這種安排最能形成哪種效果？", ["先提出疑慮，再以證據修正判斷", "先給結論，後完全不提供資料", "以景物取代所有論證", "讓前後內容互相毫無關聯"], "A", "文章先呈現傳聞，再用檢查結果與方案補充證據，形成由猜測到較可靠判斷的轉換。", "第2題資料理解與寫作分析題型改編"),
    ("一篇文章介紹古代醫療記錄，先引用原始記載，再說明現代研究者如何比對其他史料。這樣安排最能表現作者哪種態度？", ["重視史料並保留查證意識", "只相信單一傳聞", "刻意避免任何證據", "只描述作者的旅遊心情"], "A", "同時引用原始記載並說明比對其他史料，顯示重視證據與查證限制。", "第2題與第36至37題資料分析題型改編"),
    ("文章最後一句是「所以，真正值得保存的，不只是老屋本身，還有人們在其中生活的記憶。」這句在全文中最可能具有什麼作用？", ["統整前文並提出核心觀點", "新增完全無關的角色", "只交代故事發生時間", "否定前文所有例子"], "A", "句子把老屋與生活記憶連結，統整前文並明確提出作者的核心看法。", "第37題觀點判讀題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "chinese" / f"question-chinese-performance-5-iv-3-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考國文科；{locator}；官方答案表：{ANSWER}；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style Chinese reading/style questions")
