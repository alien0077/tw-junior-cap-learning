#!/usr/bin/env python3
"""Replace one Chinese character form/sound/meaning lesson with CAP-style adaptations."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-chinese-common-character-form-sound-meaning"
KID = "kg-chinese-content-ab-iv-1"
SOURCE = "https://www.grow22.com/download/114/114_cp/01_114P_Chinese.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列各組詞語中，標示的字音何者正確？", ["「揶」揄：ㄧㄝˊ", "「晾」晒：ㄐㄧㄥ", "藩「籬」：ㄆㄢˊ", "「栽」培：ㄗㄞˊ"], "A", "揶揄的揶讀作ㄧㄝˊ；其餘選項的讀音分別應為ㄌㄧㄤˋ、ㄌㄧˊ、ㄗㄞ。", "第14題字音題型改編"),
    ("下列詞語，何者用字完全正確？", ["有志竟成", "情不自盡", "眼不見為靜", "趕緊殺絕"], "A", "有志竟成的「竟」指終究、最後；其餘選項應寫作情不自禁、眼不見為淨、趕盡殺絕。", "第16題用字題型改編"),
    ("下列哪一組詞語中的字形都正確？", ["迫不及待、再接再厲", "相形見拙、一籌莫展", "因地制宜、按步就班", "不徑而走、名列前矛"], "A", "迫不及待與再接再厲皆為正確寫法；其餘含有絀、部、脛、茅等字的誤寫。", "第16題用字題型改編"),
    ("「他把資料分門別類，整理得井然有序。」句中的「井然」最接近下列何者？", ["整齊有條理", "非常急促", "完全沉默", "模糊不清"], "A", "井然形容整齊、有條理，井然有序即排列整齊而有秩序。", "第13題詞義題型改編"),
    ("下列文句中的字音，何者正確？", ["「倔」強：ㄐㄩㄝˊ", "「模」樣：ㄇㄛˊ", "「勉」強：ㄇㄧㄢˇ", "「給」予：ㄍㄟˇ"], "C", "勉強的勉讀作ㄇㄧㄢˇ；倔強的倔讀ㄐㄩㄝˋ，模樣的模讀ㄇㄨˊ，給予的給讀ㄐㄧˇ。", "第14題字音題型改編"),
    ("下列句子，何者沒有錯別字？", ["他不假思索地回答問題。", "我們要珍惜光陰，不能虛渡年華。", "這項規畫已經順利峻工。", "她的表現令人刮目相看，值得嘉獎與鼓厲。"], "A", "不假思索的「假」與「思索」皆用字正確；其餘應為虛度、竣工、鼓勵。", "第16題用字題型改編"),
    ("「他們在比賽中勢均力敵。」句中的「均」最接近下列何者？", ["相等", "快速", "分散", "隱密"], "A", "勢均力敵指雙方力量相當，其中均有相等、平均之意。", "第13題詞義題型改編"),
    ("下列詞語中的「」字，何者使用正確？", ["辨識方向", "辯別真偽", "辮解理由", "便認是非"], "A", "辨識是分辨、識別；其餘應分別寫作辨別、辯解、辨認。", "第16題形音義題型改編"),
    ("下列句子，何者用字完全正確？", ["他抱著破斧沉舟的決心參賽。", "這篇文章內容精僻，值得反覆閱讀。", "大家同心協力，終於克服難關。", "她以身做則，帶領同學整理校園。"], "C", "同心協力的字形正確；其餘應寫作破釜沉舟、精闢、以身作則。", "第16題用字題型改編"),
    ("下列詞語的讀音，何者標示正確？", ["「纖」維：ㄑㄧㄢ", "「憎」恨：ㄗㄥ", "「暫」時：ㄓㄢˋ", "「澄」清：ㄉㄥ"], "B", "憎恨的憎讀作ㄗㄥ；纖維讀ㄒㄧㄢ、暫時讀ㄗㄢˋ，澄清在此讀ㄔㄥ。", "第14題字音題型改編"),
]

for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "chinese" / f"question-chinese-common-character-form-sound-meaning-{index}.json"
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
print(f"replaced {len(rows)} CAP-style Chinese character questions")
