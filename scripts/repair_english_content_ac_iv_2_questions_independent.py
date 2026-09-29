#!/usr/bin/env python3
"""Independent English Ac-IV-2 classroom expressions rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ac-iv-2"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "教室用語、基礎句型與問答"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "課堂指令、請求與回應"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "教室互動與生活英語辨識"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求理解課堂開始、請求澄清、借用物品、回答指令、合作與課堂結束等常見用語；本題採全新對話。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("Teacher: **Good morning, class.** Students should most naturally say:", ["Good morning, teacher.", "Good night, teacher.", "See you yesterday.", "I am a pencil."], "A", "Good morning is the appropriate greeting for the start of a morning class.", "先判斷時間與對話角色，再選擇相應的回應。", ["Identify the classroom setting.", "Notice the greeting contains morning.", "Choose a polite greeting that matches the time.", "Use Good morning, teacher.", "Reject night, past-time and unrelated replies."]),
    ("Student: **May I borrow a ruler?** Which reply gives permission?", ["Sure. Here you are.", "No, it is Monday.", "I am thirteen.", "Close the window."], "A", "Sure. Here you are accepts the request and offers the ruler.", "辨認 May I 的請求功能，再找允許並交付物品的回應。", ["Identify the request verb borrow.", "Find the object ruler.", "Look for a reply that grants permission.", "Choose Sure. Here you are.", "Check that the other replies do not answer the request."]),
    ("A student says **I don't understand this word.** What is the most useful classroom response?", ["Please explain it again.", "Open the door yesterday.", "It is under the desk.", "I like blue."], "A", "Please explain it again directly asks for clarification when the student does not understand.", "從困難陳述判斷需要的是澄清、重說或示範，而非無關資訊。", ["Find the problem: don't understand.", "Decide what help is needed.", "Look for a polite clarification request.", "Choose Please explain it again.", "Reject answers about time, location or color."]),
    ("Teacher: **Work with a partner.** What should students do?", ["Work alone without speaking.", "Leave the classroom.", "Put the book in the trash.", "Work together with one classmate."], "A", "Work with a partner asks students to cooperate with one classmate.", "把祈使句的動作 work 與對象 partner 合併理解。", ["Locate the action Work.", "Interpret partner as another student.", "Combine the action and the person.", "Choose working together with one classmate.", "Explain why leaving or working alone changes the instruction."]),
    ("Which expression politely asks the teacher to say something again?", ["Could you say that again, please?", "Turn off the lights now.", "I have two brothers.", "This is my lunch."], "A", "Could you say that again, please? is a polite request for repetition.", "找出疑問句中的 say again 與禮貌請求形式。", ["Identify the goal: hear the message again.", "Look for a repeated-speech phrase.", "Check for a polite request marker.", "Choose Could you say that again, please?", "Reject instructions and personal information sentences."]),
    ("Teacher: **Please hand in your homework.** What should a student do?", ["Keep the homework at home.", "Give the homework to the teacher.", "Draw a new classroom.", "Ask for a birthday gift."], "A", "Hand in means submit or give the homework to the teacher.", "先辨認片語 hand in，再把它對應到交作業的行動。", ["Locate the object homework.", "Interpret hand in as submit.", "Identify the receiver from the classroom context.", "Choose giving the homework to the teacher.", "Reject actions unrelated to submitting work."]),
    ("Student: **Can I use your eraser?** A helpful classmate may answer:", ["Of course. Here it is.", "It is raining outside.", "I finished lunch.", "Stand behind the chair."], "A", "Of course. Here it is grants permission and identifies the item being lent.", "將 Can I use 的借用請求與允許、交付物品的回應配對。", ["Identify the requested object eraser.", "Look for permission language.", "Look for an offer or handoff.", "Choose Of course. Here it is.", "Check that weather, lunch and position do not respond to borrowing."]),
    ("At the end of class, which expression is most appropriate?", ["See you next class.", "Open your book at the beginning.", "May I borrow your pen?", "What color is the wall?"], "A", "See you next class closes the lesson with a suitable farewell.", "先判斷課堂階段，再選擇道別而不是開始活動或提問的用語。", ["Notice the phrase at the end of class.", "List which choices are instructions or requests.", "Find the farewell expression.", "Choose See you next class.", "Explain why the other choices fit different moments."]),
    ("Teacher: **Look at the board and circle the answer.** Which action is correct?", ["Look at the board and circle the answer.", "Look away and erase every word.", "Close the book without reading.", "Run outside."], "A", "The student should perform both actions in order: look at the board, then circle the answer.", "把 and 連接的兩個動作依序讀完整，不只挑其中一個。", ["Find the first action look at the board.", "Find the second action circle the answer.", "Notice and connects both actions.", "Choose the option that performs both.", "Reject choices that omit or reverse the instructions."]),
    ("Student: **I'm sorry I'm late.** Which reply is most appropriate from the teacher?", ["That's all right. Please sit down.", "Here is a banana yesterday.", "Write the word blue loudly.", "No, I am a window."], "A", "That's all right acknowledges the apology, and Please sit down gives a clear classroom next step.", "先回應道歉，再看是否提供符合課堂情境的下一步。", ["Identify I'm sorry as an apology.", "Find an accepting response.", "Check for a relevant classroom instruction.", "Choose That's all right. Please sit down.", "Reject unrelated objects, colors and statements."]),
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
    item = {"id": f"question-english-content-ac-iv-2-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ac-iv-2"], "difficulty": "easy", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究課堂指令、請求、澄清、借用與回應題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫常見教室用語題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ac-iv-2-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
