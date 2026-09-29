#!/usr/bin/env python3
"""Independent English Ae-IV-4 cards, letters and email rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ae-iv-4"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "短文、對話與生活書寫"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "書信、訊息與日常溝通"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "卡片、電郵與訊息目的"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求從卡片、簡短信件與電郵判讀收件人、寫作者、目的、時間、事件與適當回應；本題採全新文本。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("Email: **Hi Emma, Thank you for the birthday card. It made me smile. Best, Lily** Why did Lily write the email?", ["To thank Emma.", "To ask for directions.", "To sell a card.", "To report the weather."], "A", "Lily says Thank you for the birthday card, so the purpose is to express thanks.", "先找明示的動作與對象，再判斷訊息目的。", ["Locate the writer Lily.", "Find what Emma sent.", "Notice the phrase Thank you.", "Choose thanking Emma.", "Reject purposes not mentioned in the email."]),
    ("Card: **Happy New Year! I hope your family has a wonderful year.** When is this card most suitable?", ["At the start of a new year.", "On a sick person's hospital visit.", "After a sports game only.", "When asking for homework."], "A", "The greeting Happy New Year identifies the occasion and timing.", "利用祝賀語判斷卡片的節日與使用時機。", ["Read the opening greeting.", "Match New Year with the occasion.", "Check which option names that time.", "Choose the start of a new year.", "Do not infer unrelated events."]),
    ("Email: **Dear Mr. Chen, I cannot come to class tomorrow because I have a fever. May I get the homework?** What does the writer want?", ["The homework information.", "A new classroom.", "A birthday cake.", "A train ticket."], "A", "The final question asks for the homework after explaining the absence.", "先看 because 的原因，再看最後的請求目的。", ["Identify the writer's absence.", "Read the reason have a fever.", "Locate the request May I get the homework.", "Choose homework information.", "Reject objects not named in the email."]),
    ("Which closing is most suitable for an email to a close friend?", ["Love, Amy", "Yours faithfully, The Bank", "Please pay this bill.", "Room 204"], "A", "Love, Amy is a friendly personal closing; the other choices are not suitable closings for that audience.", "依收件人關係選擇語氣與結尾格式。", ["Identify the audience as a close friend.", "Compare personal and formal closings.", "Choose a warm sign-off with the writer's name.", "Select Love, Amy.", "Check that the other options are instructions or labels."]),
    ("Note: **Please feed the cat at 6 p.m. I will be home late. —Dad** Why did Dad write the note?", ["To ask someone to feed the cat.", "To invite everyone to a concert.", "To describe a new cat breed.", "To cancel a flight."], "A", "The imperative Please feed the cat gives the note's main request, and the time explains when.", "找祈使句主要求，再用時間與原因補充理解。", ["Locate the action feed.", "Identify the object the cat.", "Notice the requested time 6 p.m.", "Choose asking someone to feed the cat.", "Use Dad's late arrival as supporting context."]),
    ("Email subject: **Lost Water Bottle**. The message says, **Did anyone see my green bottle after practice?** What is the writer doing?", ["Looking for a missing bottle.", "Ordering a meal.", "Announcing a test score.", "Giving a weather warning."], "A", "The subject and question both show that the writer is searching for a lost bottle.", "把主旨列與正文問題互相確認，不只翻譯單一字詞。", ["Read the subject line.", "Find the key noun water bottle.", "Read the question after practice.", "Choose looking for a missing bottle.", "Reject topics absent from both parts."]),
    ("A thank-you card says **Thank you for helping me practice the piano.** Who is the likely receiver?", ["Someone who helped with piano practice.", "A bus driver who sold a ticket.", "A doctor who closed a shop.", "A neighbor who planted a tree."], "A", "The card names help with piano practice, so the receiver is the person who provided that help.", "從 thank you for 後的行為回推收件人的角色。", ["Locate the thanking phrase.", "Identify the helpful action piano practice.", "Infer who the receiver must be.", "Choose someone who helped with piano practice.", "Do not add an unrelated relationship."]),
    ("Email: **The meeting is moved from Monday to Wednesday at 3 p.m.** What changed?", ["The day and time of the meeting.", "The writer's home address.", "The color of the invitation.", "The price of lunch."], "A", "Moved from Monday to Wednesday at 3 p.m. changes the meeting schedule.", "抓 from...to... 與時間標記，區分行程變更與其他資訊。", ["Find the original day Monday.", "Find the new day Wednesday.", "Read the new time 3 p.m.", "Choose the meeting day and time.", "Reject details not present in the email."]),
    ("Which opening is most appropriate for a formal email to a school office?", ["Dear School Office,", "Hey buddy!", "What a funny dog!", "See you last year,"], "A", "Dear School Office is a polite formal opening addressed to an institution.", "依收件人是機構而非朋友選擇正式稱呼。", ["Identify the recipient as a school office.", "Classify the relationship as formal.", "Choose a respectful salutation.", "Select Dear School Office,.", "Reject casual or unrelated openings."]),
    ("Card: **Get well soon! We are thinking of you.** What is the card's purpose?", ["To encourage a sick person.", "To announce a new address.", "To ask about a train platform.", "To complain about homework."], "A", "Get well soon and We are thinking of you are supportive words for someone who is ill.", "由固定祝福語判斷卡片對象與溝通目的。", ["Recognize the phrase Get well soon.", "Infer that the receiver is ill or recovering.", "Connect thinking of you with support.", "Choose encouraging a sick person.", "Reject purposes unrelated to health support."]),
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
    item = {"id": f"question-english-content-ae-iv-4-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ae-iv-4"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究卡片、短訊息、書信與電郵的目的、對象、時間和回應題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫實用文本題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ae-iv-4-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
