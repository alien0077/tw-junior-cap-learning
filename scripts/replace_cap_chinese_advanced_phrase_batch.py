#!/usr/bin/env python3
"""Replace one advanced Chinese vocabulary lesson with CAP-style adaptations."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-chinese-common-phrases-advanced"
KID = "kg-chinese-content-ab-iv-5"
SOURCE = "https://www.grow22.com/download/114/114_cp/01_114P_Chinese.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列句子中的成語，何者使用最恰當？", ["這項新措施成效差強人意，仍有許多問題待改善。", "他差強人意地獲得冠軍，表示表現完美無缺。", "差強人意是指完全不能接受，因此大家都稱讚這場演出。", "她差強人意地保持沉默，表示非常善於溝通。"], "A", "差強人意指大致令人滿意，但仍非十分完美，符合仍有問題待改善的語境。", "第13題詞語使用題型改編"),
    ("「兩項方案各有支持者，評審一時莫衷一是。」句中的「莫衷一是」是指什麼？", ["各有意見，無法得到一致結論", "大家立刻達成共識", "所有人拒絕發表意見", "只有一個人提出主張"], "A", "莫衷一是指各有各的意見，不能得到一致的結論。", "第19題詞義辨析題型改編"),
    ("下列哪一句最適合使用「不置可否」？", ["主持人聽完雙方說明後，暫時不置可否。", "他不置可否地衝過終點，速度非常快。", "植物不置可否地吸收陽光，順利生長。", "她不置可否地完成畫作，色彩十分鮮豔。"], "A", "不置可否表示不表示贊成或反對，適合描述主持人暫不表態。", "第19題詞語使用題型改編"),
    ("下列哪一句的「相得益彰」使用正確？", ["音樂與燈光互相配合，使演出相得益彰。", "他獨自一人工作，與同伴相得益彰。", "兩個方案互相矛盾，因而相得益彰。", "相得益彰表示彼此毫無關聯。"], "A", "相得益彰指彼此配合，使優點更加顯著。", "第13題詞語搭配題型改編"),
    ("「山路狹窄又逢大雨，位於下游的村落首當其衝。」此處的「首當其衝」是指什麼？", ["最先受到衝擊", "最後完成任務", "主動發起攻擊", "完全不受影響"], "A", "首當其衝指最先受到衝擊或災害影響，下游村落符合此意。", "第19題成語語境題型改編"),
    ("下列哪一項最能說明「按圖索驥」的限制？", ["只依舊地圖找路，卻忽略道路已經改變", "依照地圖與現場資料更新路線", "先確認方向再比較多張地圖", "使用定位工具並實地觀察路況"], "A", "按圖索驥常比喻拘泥成法；只依舊圖而忽略現況正是其限制。", "第13題成語語境題型改編"),
    ("「他的努力與成果不言而喻。」句中的「不言而喻」最接近下列何者？", ["不用說明就能明白", "必須反覆爭辯才能確定", "完全沒有任何證據", "只能靠猜測理解"], "A", "不言而喻指不必說明就能明白，成果明顯即可使用。", "第19題詞義辨析題型改編"),
    ("下列哪一句的「不可名狀」使用最恰當？", ["登上山頂看見雲海時，他感到一種不可名狀的感動。", "他不可名狀地準時到校，沒有遲到。", "不可名狀的尺長二十公分，適合畫線。", "她不可名狀地整理書桌，分類十分清楚。"], "A", "不可名狀形容難以用言語說明的感受，適合描述看見雲海的感動。", "第19題詞語使用題型改編"),
    ("「這項技術仍在測試階段，距離普遍使用還一蹴可幾。」若要修正語意，應如何改寫？", ["改為『還不是一蹴可幾』，表示不容易很快達成", "改為『已經一蹴可幾』，表示完全不可能", "改為『一蹴可幾地失敗』，表示很快失敗", "不用修改，原句表示很難達成"], "A", "一蹴可幾指一下子就可以成功，原句否定詞缺漏；改為還不是一蹴可幾才符合距離普及仍遠。", "第13題詞語修訂題型改編"),
    ("下列哪一句的「耳提面命」使用正確？", ["教練多次耳提面命，提醒隊員遵守安全規則。", "耳提面命是一種不必說話的沉默。", "他耳提面命地跑步，速度比昨天快。", "這場雨耳提面命地落下，造成積水。"], "A", "耳提面命比喻懇切地教導與提醒，符合教練反覆提醒隊員。", "第13題成語搭配題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "chinese" / f"question-chinese-common-phrases-advanced-{index}.json"
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
print(f"replaced {len(rows)} CAP-style advanced Chinese vocabulary questions")
