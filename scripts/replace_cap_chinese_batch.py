#!/usr/bin/env python3
"""Replace one Chinese vocabulary lesson with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-chinese-common-phrases-usage"
KID = "kg-chinese-content-ab-iv-2"
SOURCE = "https://www.grow22.com/download/114/114_cp/01_114P_Chinese.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列句子中的詞語，何者使用最恰當？", ["這項工程延宕多時，終於在本月竣工。", "他把房間整理得井然有序，顯得十分凌亂。", "聽到好消息後，他不禁忍俊不禁地哭泣。", "這篇報告內容空泛，資料十分充實。"], "A", "延宕指延遲，竣工指工程完成，前後語意搭配正確。", "第13題題型改編"),
    ("下列句子中的成語，何者使用最恰當？", ["面對突如其來的提問，他一時張皇失措。", "他做事總是按部就班，因此常常毫無章法。", "這家店的服務差強人意，表示令人非常滿意。", "她對公益活動漠不關心，卻積極投入志工服務。"], "A", "張皇失措形容慌張而不知所措，符合突然被提問的情境。", "第19題題型改編"),
    ("「經過多次討論，團隊終於找到可行方案。」句中的「可行」最接近下列何者？", ["能夠實行", "不必說明", "容易遺忘", "完全相同"], "A", "可行是可以實行、做得通的意思。", "第13題詞義題型改編"),
    ("下列哪一句的「不置可否」使用正確？", ["評審聽完兩案後不置可否，沒有表示贊成或反對。", "他不置可否地大聲歡呼，顯然非常興奮。", "雨勢不置可否，因此街道全部淹水。", "她不置可否地完成作業，速度非常快。"], "A", "不置可否是既不表示贊成，也不表示反對。", "第19題詞語題型改編"),
    ("下列哪一項最適合用「不言而喻」？", ["努力的重要性不言而喻，大家都明白。", "他不言而喻地朗讀文章，聲音十分洪亮。", "不言而喻是一種需要查字典的工具。", "她把不言而喻的禮物放在桌上。"], "A", "不言而喻指不用說明就能明白，適合描述明顯的道理。", "第19題詞語題型改編"),
    ("下列哪一句的「不可名狀」使用正確？", ["那片星空帶來的震撼，令人感到不可名狀。", "他不可名狀地準時抵達教室。", "不可名狀是指姓名已經寫在名冊上。", "這支筆不可名狀，所以很容易書寫。"], "A", "不可名狀形容難以用言語形容，常用來表達強烈或複雜的感受。", "第19題詞語題型改編"),
    ("「校方決定暫緩施工，以確認安全措施。」句中的「暫緩」最接近下列何者？", ["暫時延後", "立即完成", "完全取消", "加速進行"], "A", "暫緩是暫時延後辦理，並不等於永久取消。", "第13題詞義題型改編"),
    ("下列哪一句的「相得益彰」使用正確？", ["圖文互相配合，使展覽內容相得益彰。", "兩人互相爭吵，因此相得益彰地離開。", "相得益彰是指彼此毫無關係。", "他獨自完成工作，與同伴相得益彰。"], "A", "相得益彰指彼此配合，使優點更加顯著。", "第13題詞語題型改編"),
    ("下列哪一句的「首當其衝」使用正確？", ["位於河岸低窪處的村落，暴雨時往往首當其衝。", "他首當其衝地獲得第一名，大家都稱讚他。", "首當其衝表示最後才開始行動。", "她首當其衝地安靜閱讀，沒有受到打擾。"], "A", "首當其衝指最先受到衝擊或遭遇災害，符合低窪村落的情境。", "第19題詞語題型改編"),
    ("下列哪一句的「按圖索驥」使用最恰當？", ["只依舊地圖尋找新路線，可能像按圖索驥而忽略現場變化。", "他按圖索驥地關心朋友，主動傾聽對方感受。", "按圖索驥表示不看任何資料便能找到目標。", "她按圖索驥地完成歌唱，音色十分優美。"], "A", "按圖索驥比喻拘泥成法或依線索尋找；句中提醒只依舊圖而忽略現況，使用恰當。", "第13題詞語題型改編"),
]

for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "chinese" / f"question-chinese-common-phrases-usage-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
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
print(f"replaced {len(rows)} CAP-style Chinese questions")
