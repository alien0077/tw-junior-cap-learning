#!/usr/bin/env python3
"""Independent English Ae-IV-7 narrator viewpoint, attitude and purpose rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ae-iv-7"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "短文觀點、態度與閱讀理解"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中公開英語段考", "文本目的、語氣與推論"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "作者意圖與訊息判讀"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求從敘事者用語、選材、建議、情緒詞與讀者對象推斷觀點、態度、寫作目的及證據界線；本題採全新文本。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("Text: **I was sure the old path was dangerous, so I stayed on the marked trail.** What is the narrator's attitude toward the old path?", ["Cautious.", "Excited to race there.", "Uninterested in safety.", "Proud of ignoring signs."], "A", "The narrator calls the path dangerous and chooses the marked trail, showing caution.", "把評價詞與人物選擇連在一起，從行動推論態度。", ["Find the narrator's description of the path.", "Notice the word dangerous.", "Read the decision to stay on the marked trail.", "Infer a cautious attitude.", "Reject attitudes that conflict with the safety choice."]),
    ("A poster says **Bring a reusable bottle and help our park stay clean.** What is its main purpose?", ["To encourage an environmentally friendly action.", "To sell a new phone.", "To describe a historical battle.", "To announce a cooking contest."], "A", "The imperative Bring and the reason about keeping the park clean encourage readers to act for the environment.", "由祈使句、行動對象與理由判斷宣傳目的。", ["Locate the action Bring.", "Identify the object reusable bottle.", "Read the reason park stay clean.", "Choose encouraging an environmental action.", "Reject topics absent from the poster."]),
    ("Narrator: **Fortunately, the bus arrived before the rain started.** What attitude does the word Fortunately express?", ["Relief or happiness about a good result.", "Anger about a rule.", "Doubt about a fact.", "Boredom with the trip."], "A", "Fortunately signals that the narrator views the timely bus arrival as a favorable event.", "找態度副詞，再用後面的事件驗證情緒方向。", ["Locate Fortunately.", "Read the event that follows.", "Ask whether it is favorable or unfavorable.", "Choose relief or happiness.", "Do not replace the narrator's attitude with a new problem."]),
    ("A review says **The movie has beautiful pictures, but its story moves too slowly.** What is the reviewer's viewpoint?", ["Balanced: it praises one feature and criticizes another.", "Completely positive about every part.", "Completely negative about every part.", "Unrelated to the movie."], "A", "The reviewer uses but to place praise for pictures beside criticism of the story.", "注意 but 的轉折，區分局部稱讚與整體評價。", ["Identify the praised feature.", "Identify the criticized feature.", "Notice the contrast marker but.", "Choose the balanced viewpoint.", "Avoid turning one criticism into total rejection."]),
    ("A narrator writes, **You should check the bus schedule before leaving home.** Who is the likely audience?", ["People planning to take the bus.", "People baking a cake.", "People repairing a roof.", "People studying a map of stars."], "A", "The advice about checking a bus schedule is directed to people planning a bus trip.", "由建議內容反推讀者需要與使用情境。", ["Locate the advice check the bus schedule.", "Identify the action's users.", "Connect it to planning travel.", "Choose bus travelers.", "Reject audiences without a transport connection."]),
    ("Text: **Our community garden is small, yet every family can grow something there.** What viewpoint is expressed?", ["A small space can still be useful and inclusive.", "Only large gardens are valuable.", "Families should never grow plants.", "The garden is closed to everyone."], "A", "The contrast word yet shows that small size does not prevent families from using the garden.", "由 yet 的轉折與 every family 的範圍判斷作者觀點。", ["Identify the apparent limitation small.", "Read the contrast marker yet.", "Notice every family can grow something.", "Infer a positive inclusive viewpoint.", "Reject claims that contradict the access described."]),
    ("A message says **Please do not feed the birds; it may make them sick.** What is the writer's purpose?", ["To prevent harmful behavior by giving a reason.", "To invite people to a bird-feeding party.", "To describe a bird's color.", "To report a train delay."], "A", "The prohibition is supported by a health reason, so the message aims to prevent feeding the birds.", "辨認禁止行動與後果理由，再判斷提醒目的。", ["Locate do not feed.", "Identify the object birds.", "Read the reason may make them sick.", "Choose preventing harmful behavior.", "Do not interpret it as an invitation."]),
    ("Narrator: **I tried the new route twice, and now I recommend it to families with young children.** What supports the recommendation?", ["The narrator's repeated experience.", "A weather forecast only.", "A stranger's unrelated joke.", "The route's color on a map."], "A", "Trying the route twice gives the narrator direct repeated experience behind the recommendation.", "把觀點主張與前文提供的經驗證據配對。", ["Find the recommendation recommend it.", "Look backward for supporting experience.", "Notice tried the route twice.", "Choose repeated personal experience.", "Distinguish evidence from decorative details."]),
    ("A notice explains how to return a library book and lists the due date. What is the notice mainly for?", ["To give readers instructions and a deadline.", "To tell a fictional adventure.", "To praise a singer.", "To sell a bicycle."], "A", "The return steps and due date provide practical instructions and a time limit.", "從文本形式與資訊功能判斷目的，不只看單一名詞。", ["Identify the action return a book.", "Locate the listed steps.", "Notice the due date.", "Combine them as instructions plus deadline.", "Reject entertainment and sales purposes."]),
    ("A narrator says, **I expected the hike to be easy, but the steep rocks surprised me.** What changed in the narrator's view?", ["The narrator's expectation changed after direct experience.", "The narrator never began the hike.", "The rocks became flat before the hike.", "The narrator stopped thinking about the trail."], "A", "The contrast between expected easy and surprised by steep rocks shows a revised view after experience.", "比較 but 前後的預期與實際觀察，判斷觀點如何改變。", ["Identify the original expectation.", "Find the new experience steep rocks.", "Notice the reaction surprised me.", "Infer a changed view.", "Reject outcomes not stated in the sentence."]),
]

assert len(DATA) == 10
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]
for i, (prompt, options, answer, explanation, strategy, steps) in enumerate(DATA, 1):
    target = TARGETS[i - 1]
    if target != answer:
        oi, ti = ord(answer) - 65, ord(target) - 65
        correct = options[oi]
        rest = [v for j, v in enumerate(options) if j != oi]
        options = rest[:ti] + [correct] + rest[ti:]
        answer = target
    item = {"id": f"question-english-content-ae-iv-7-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ae-iv-7"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究敘事者觀點、語氣、目的、受眾與證據推論題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫作者觀點態度目的題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ae-iv-7-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
