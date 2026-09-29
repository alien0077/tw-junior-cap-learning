#!/usr/bin/env python3
"""Independent English Ac-IV-3 everyday expressions rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ac-iv-3"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "日常問答與基礎生活字彙"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "生活情境、問候與請求"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "生活對話與情境理解"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求理解問候、感謝、道歉、購物、時間、喜好、邀請與求助等日常用語；本題採全新對話與情境。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("A: **How are you today?** B: ______", ["I'm fine, thank you.", "It is a pencil.", "At seven o'clock.", "No, I don't."], "A", "I'm fine, thank you is a natural response about how someone feels.", "先辨認疑問詞 how 與話題，再配對描述狀態的回應。", ["Identify how as a question about condition.", "Look for an answer about a person's state.", "Choose I'm fine, thank you.", "Check that time and objects answer different questions.", "Notice the polite thank-you closing."]),
    ("A: **Thank you for your help.** B: ______", ["You're welcome.", "I'm twelve.", "Turn left.", "It is cloudy."], "A", "You're welcome is the standard response to thanks.", "辨認感謝語，再找禮貌回應而非年齡、方向或天氣。", ["Locate Thank you.", "Recognize it as gratitude.", "Recall the matching polite response.", "Choose You're welcome.", "Reject answers that change the topic."]),
    ("A: **I'm sorry I broke the cup.** B: ______", ["That's all right. Please be careful next time.", "I like the cup.", "It is on Tuesday.", "Open your book."], "A", "That's all right acknowledges the apology, and the second sentence gives a reasonable next reminder.", "先回應道歉，再判斷後續語句是否符合事件。", ["Identify I'm sorry as an apology.", "Find a reply that acknowledges it.", "Check whether the advice fits the broken cup.", "Choose the complete apology response.", "Reject unrelated time, book and preference statements."]),
    ("A: **How much is this notebook?** B: ______", ["It's fifty dollars.", "It's next to the lamp.", "I am reading.", "Yes, I can swim."], "A", "How much asks about price, so the amount in dollars is the matching answer.", "從 how much 判斷價格問題，再排除位置、活動與能力。", ["Find the question phrase How much.", "Interpret it as price.", "Look for a number and money unit.", "Choose It's fifty dollars.", "Confirm the other choices answer different topics."]),
    ("A: **Would you like some orange juice?** B: ______", ["Yes, please.", "At the bus stop.", "Because it is big.", "I went yesterday."], "A", "Yes, please politely accepts an offer of orange juice.", "辨認 Would you like 的邀請或提供，再選接受或拒絕的回應。", ["Identify the offered item orange juice.", "Recognize Would you like as an offer.", "Find a polite acceptance.", "Choose Yes, please.", "Note that location, reason and past time do not respond to the offer."]),
    ("A: **What time does the movie start?** B: ______", ["At 7:30.", "In the kitchen.", "With my sister.", "No, it isn't."], "A", "What time asks for a clock time, so At 7:30 is appropriate.", "抓 what time 的時間資訊，再配對時刻表達。", ["Locate What time.", "Decide that a clock time is needed.", "Find the option with a time.", "Choose At 7:30.", "Reject place, companion and yes/no answers."]),
    ("A: **Could you show me the way to the station?** B: ______", ["Sure. Go straight and turn left.", "I am hungry.", "It is my station.", "No, I was late."], "A", "The reply gives directions, which directly helps someone asking for the way.", "辨認 show me the way 的問路功能，再選含方向的回答。", ["Identify the destination station.", "Recognize the request for directions.", "Look for movement instructions.", "Choose Go straight and turn left.", "Reject feelings and unrelated personal statements."]),
    ("A: **What do you like to do after school?** B: ______", ["I like playing basketball.", "At the library door.", "It is five meters.", "No, she isn't."], "A", "The question asks about an activity or preference, and playing basketball answers it.", "從 what do you like to do 判斷要回答喜好活動。", ["Find like to do after school.", "Classify it as an activity preference.", "Locate an answer beginning I like.", "Choose playing basketball.", "Reject place, distance and third-person answers."]),
    ("A: **Are you free this Saturday?** B: ______", ["Yes, I can join you.", "It is a sandwich.", "At the corner.", "I am from Canada."], "A", "Yes, I can join you confirms availability and responds to a possible invitation.", "先辨認 yes/no 的空閒詢問，再判斷回應是否能接續邀請。", ["Identify Are you as a yes/no question.", "Notice the time this Saturday.", "Find an answer about availability.", "Choose Yes, I can join you.", "Reject food, place and origin answers."]),
    ("A: **Where can I buy a ticket?** B: ______", ["At the ticket counter.", "Because I am tired.", "I can play tennis.", "It starts at noon."], "A", "Where asks for a place, and the ticket counter is the relevant location.", "由 where 判斷地點問題，再配對能買票的場所。", ["Locate Where.", "Identify the action buy a ticket.", "Find a place connected to ticket purchase.", "Choose At the ticket counter.", "Reject reason, ability and time answers."]),
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
    item = {"id": f"question-english-content-ac-iv-3-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ac-iv-3"], "difficulty": "easy", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究生活問候、感謝、道歉、購物、時間、邀請、問路與喜好題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫常見生活用語題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ac-iv-3-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
