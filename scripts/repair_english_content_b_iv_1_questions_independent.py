#!/usr/bin/env python3
"""Independent English B-IV-1 self, family and friends rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-b-iv-1"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "人物、家人與朋友生活對話"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中公開英語段考", "自我介紹、關係與互動"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "家庭、朋友與日常資訊"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求理解自我資料、家庭成員、朋友關係、興趣、日常活動與人物描述；本題採全新對話與情境。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("A: **Who is the person in this photo?** B: **That's my cousin, Leo.** What is Leo to the speaker?", ["A teacher", "A cousin", "A neighbor", "A doctor"], "A", "The response directly identifies Leo as the speaker's cousin.", "先找關係名詞，再把人物對應到選項。", ["Locate the question about the person.", "Read the relationship word cousin.", "Match it to the choices.", "Choose A cousin.", "Do not infer a job from the photo."]),
    ("Mia says, **I enjoy drawing maps after school.** What does Mia enjoy?", ["Drawing maps.", "Cooking dinner.", "Running before school.", "Cleaning windows."], "A", "The verb enjoy is followed by drawing maps, which names Mia's interest.", "由 enjoy 後的動作判斷興趣，不被時間片語干擾。", ["Find the verb enjoy.", "Read the activity after it.", "Ignore after school as a time detail.", "Choose drawing maps.", "Check that no other activity appears in the sentence."]),
    ("A: **How many people are in your family?** B: **There are five.** What does five describe?", ["Family members.", "School subjects.", "Buses.", "Pets in a park."], "A", "The question asks how many people are in the family, so five refers to family members.", "讓疑問詞 how many 與名詞 people 決定數字的對象。", ["Locate how many people.", "Identify the context your family.", "Interpret five as a count.", "Choose family members.", "Reject counts with objects not mentioned."]),
    ("Ben's sister is older than he is. What is true?", ["Ben is younger than his sister.", "Ben is his sister's father.", "Ben and his sister are the same person.", "Ben has no sister."], "A", "If the sister is older, Ben is younger than her.", "比較級句型要把比較方向轉成完整關係。", ["Identify the compared people.", "Read older than he is.", "Reverse the relation from Ben's view.", "Choose younger than his sister.", "Reject family relations not stated."]),
    ("A friend asks, **Would you like to join our game?** Which answer accepts the invitation?", ["Sure, I'd love to.", "No, this is my brother.", "At eight o'clock yesterday.", "It is under the chair."], "A", "Sure, I'd love to politely accepts the invitation to join the game.", "辨認邀請句，再找表達接受的回應。", ["Identify the action join our game.", "Recognize Would you like as an invitation.", "Look for acceptance language.", "Choose Sure, I'd love to.", "Reject answers about identity, time or location."]),
    ("Lena writes, **My brother cooks, and I wash the dishes.** What do the siblings do?", ["They share household jobs.", "They both go to different planets.", "They never help at home.", "They are discussing a movie."], "A", "The two sentences name different chores done by family members, showing shared household jobs.", "整合兩個並列行動，判斷家庭成員的分工關係。", ["Identify the brother's action.", "Identify Lena's action.", "Notice both are household chores.", "Infer shared responsibility.", "Choose the household-jobs statement."]),
    ("A: **What is your best friend like?** B: **She is patient and funny.** What information does B give?", ["Her personality.", "Her address.", "Her height only.", "Her lunch time."], "A", "Patient and funny describe personality or character.", "what is ... like 問的是特質，不是地址或時間。", ["Recognize the question pattern.", "Read the adjectives patient and funny.", "Classify them as personality traits.", "Choose her personality.", "Reject answers requiring information not given."]),
    ("Kai tells his friend, **I have a test tomorrow, so I will study tonight.** Why will Kai study?", ["Because he has a test tomorrow.", "Because he lost his bicycle.", "Because his friend is cooking.", "Because the room is blue."], "A", "So connects the test tomorrow with the plan to study tonight.", "利用 so 的因果關係，區分原因與計畫。", ["Locate the cause before so.", "Read the planned action after so.", "Ask why Kai will study.", "Choose the test reason.", "Do not treat tonight as the reason."]),
    ("Which question best asks about a friend's birthday?", ["When is your birthday?", "Where is your pencil?", "Who is your teacher?", "How tall is the tree?"], "A", "When is your birthday directly asks for the date or time of a friend's birthday.", "先找關鍵名詞 birthday，再配對時間疑問詞 when。", ["Identify the target information birthday.", "Compare the question words.", "Choose when for time or date.", "Select When is your birthday?", "Reject questions about objects, people or height."]),
    ("A family member says, **Thank you for helping me carry these boxes.** What did the helper do?", ["Helped carry boxes.", "Bought a new house.", "Played a song.", "Forgot the family meeting."], "A", "The thank-you sentence names helping carry boxes as the helper's action.", "從 for 後的動作回推感謝的原因。", ["Locate Thank you for.", "Read the action carry.", "Identify the object boxes.", "Choose helped carry boxes.", "Reject actions not present in the sentence."]),
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
    item = {"id": f"question-english-content-b-iv-1-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-b-iv-1"], "difficulty": "easy", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究自我介紹、家庭、朋友、興趣、人物描述與日常互動題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫自己家人朋友主題題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-b-iv-1-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
