#!/usr/bin/env python3
"""Independent English B-IV-2 everyday communication rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-b-iv-2"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "日常問答與溝通句型"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中公開英語段考", "生活情境與對話回應"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "請求、建議、時間與活動"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求在日常對話中理解請求、建議、邀請、同意拒絕、時間、活動與簡短回應；本題採全新情境。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("A: **Would you like to walk to the park?** B: ______", ["Yes, that sounds fun.", "It is under the desk.", "I was there yesterday.", "No, I am a student."], "A", "Yes, that sounds fun accepts the invitation and responds naturally.", "先判斷邀請功能，再找接受且與活動相符的回應。", ["Identify the proposed activity walk to the park.", "Recognize Would you like as an invitation.", "Look for an acceptance response.", "Choose Yes, that sounds fun.", "Reject location, past-time and identity answers."]),
    ("A: **Could you lend me your notes?** B: ______", ["Of course, but please return them tomorrow.", "At the corner.", "I am eating breakfast.", "It was cloudy."], "A", "The response grants the request and adds a clear condition for returning the notes.", "將 lend 的借用請求與允許、歸還條件配對。", ["Identify the requested object notes.", "Recognize Could you as a polite request.", "Find permission language.", "Choose Of course with the return condition.", "Reject answers unrelated to borrowing."]),
    ("A: **I feel nervous about the presentation.** B: ______", ["You can practice with me.", "The bus leaves at six.", "I bought two apples.", "Turn right at the bank."], "A", "Offering practice directly responds to nervousness about presenting.", "由感受判斷需要支持或建議，不選無關資訊。", ["Identify the feeling nervous.", "Locate its cause presentation.", "Find a supportive action.", "Choose You can practice with me.", "Check that time, food and directions do not address the feeling."]),
    ("A: **What should we bring to the picnic?** B: ______", ["Some water and a blanket.", "I met him last week.", "It is my favorite color.", "No, she isn't."], "A", "The question asks what items to bring, and water and a blanket answer it.", "用 what should 判斷要列物品，不被其他句型干擾。", ["Find the action bring.", "Identify the picnic context.", "Look for nouns naming useful items.", "Choose water and a blanket.", "Reject personal history, color and yes/no responses."]),
    ("A: **I can't find the bus stop.** B: ______", ["Let me show you on the map.", "I like buses.", "It is seven years old.", "Please close your lunch."], "A", "Showing the location on a map offers practical help for finding the bus stop.", "從問題找需要的協助，再選能直接解決的回應。", ["Identify the problem cannot find.", "Locate the place bus stop.", "Find an action that gives directions.", "Choose showing it on the map.", "Reject statements that do not provide location help."]),
    ("A: **Are you free after practice?** B: ______", ["Yes, I can meet you at five.", "It is a blue jacket.", "I practice the piano yesterday.", "Because the room is small."], "A", "The reply answers availability and supplies a possible meeting time.", "先回應是否有空，再看是否補充時間與活動安排。", ["Recognize Are you free as an availability question.", "Notice the time after practice.", "Find an affirmative response.", "Choose meeting at five.", "Reject object, past and reason statements."]),
    ("A: **Please remember to lock the door.** B: ______", ["I will.", "Where is your cousin?", "It tastes sweet.", "No, I was late."], "A", "I will confirms that the speaker accepts the reminder and plans to do it.", "辨認提醒或指示，再選表示承諾的簡短回應。", ["Identify the requested action lock the door.", "Recognize Please remember as a reminder.", "Find a response promising action.", "Choose I will.", "Reject questions and unrelated descriptions."]),
    ("A: **Why don't we study together tonight?** B: ______", ["Good idea. I can bring my notes.", "It is next to the lamp.", "I have a younger sister.", "No, it was Tuesday."], "A", "Good idea accepts the suggestion and the notes sentence makes the plan concrete.", "先判斷 Why don't we 是建議，再找接受與補充計畫的回應。", ["Identify the proposed activity study together.", "Recognize the suggestion form.", "Look for agreement.", "Choose Good idea with the practical plan.", "Reject location, family and past-date answers."]),
    ("A: **I am sorry for being late.** B: ______", ["That's okay. Please come in.", "What time is lunch?", "I have a new phone.", "The movie is funny."], "A", "That's okay accepts the apology, and Please come in fits the immediate situation.", "回應道歉時要先表示接受，再接合當下行動。", ["Identify the apology.", "Find an accepting phrase.", "Check the next instruction fits the room.", "Choose That's okay. Please come in.", "Reject unrelated questions and descriptions."]),
    ("A: **How about meeting at the cafe at two?** B: ______", ["That works for me.", "I am taller than him.", "It is a rainy story.", "No, I don't like yellow."], "A", "That works for me accepts the proposed place and time.", "從 How about 判斷提議，再找同意安排的慣用回應。", ["Identify the proposed place and time.", "Recognize How about as a suggestion.", "Look for agreement language.", "Choose That works for me.", "Reject comparison, story and color responses."]),
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
    item = {"id": f"question-english-content-b-iv-2-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-b-iv-2"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究日常溝通中的邀請、請求、建議、支持、提醒與同意拒絕題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫日常溝通字彙句型題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-b-iv-2-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
