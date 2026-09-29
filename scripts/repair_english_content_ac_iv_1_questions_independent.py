#!/usr/bin/env python3
"""Independent English Ac-IV-1 simple signs rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ac-iv-1"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "校園情境、基礎字彙與簡易標示"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "生活標示、字詞辨識與閱讀"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "公共場所標示與情境理解"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求從校園、公共場所及生活標示判讀簡短英文的對象、地點、允許或禁止行為與安全訊息；本題採全新標示與情境。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("A sign says **KEEP THE DOOR CLOSED**. What should people do?", ["Leave the door open.", "Close the door and keep it closed.", "Paint the door.", "Move the door outside."], "B", "The sign gives an instruction to close the door and maintain that condition.", "先找動作詞與受詞，再判斷標示要求的行為。", ["Locate the action word KEEP.", "Identify the object THE DOOR.", "Read CLOSED as the required state.", "Choose the action that follows all three words.", "Reject choices that change the object or action."]),
    ("Which sign tells visitors where they can get help?", ["EXIT", "HELP DESK", "NO PHOTOS", "WET FLOOR"], "B", "HELP DESK identifies a place where visitors can ask for assistance.", "先判斷標示是地點、禁止事項或警告，再對應問題目的。", ["Read each sign as a short phrase.", "Classify EXIT, NO PHOTOS and WET FLOOR.", "Find the phrase naming a service place.", "Match HELP DESK with getting help.", "Check that it is not merely an exit or warning."]),
    ("You see **NO FOOD OR DRINK** in a computer room. Which action is allowed by the sign?", ["Eat at the computer.", "Drink beside the keyboard.", "Keep food and drinks outside the room.", "Pour water on the desk."], "C", "The sign prohibits food and drinks in the room, so keeping them outside follows the instruction.", "把禁止的對象 food/drink 和場所範圍一起讀，避免只看單字。", ["Identify the location: a computer room.", "Read NO as a prohibition marker.", "List the two prohibited items.", "Choose the action that keeps them outside.", "Confirm that eating or drinking inside would break the rule."]),
    ("A library sign says **QUIET ZONE**. What is the best behavior?", ["Speak very loudly.", "Play music without headphones.", "Use a quiet voice.", "Shout for a friend."], "D", "A quiet zone asks people to reduce noise, so using a quiet voice best matches the sign.", "先辨認區域名稱，再由 quiet 推出適合的行為。", ["Locate the place word ZONE.", "Interpret quiet as low noise.", "Compare the four behaviors.", "Choose the quiet voice behavior.", "Explain why loud actions conflict with the sign."]),
    ("Which sign is most useful near a staircase when the floor may be slippery?", ["SLIPPERY FLOOR", "OPEN 24 HOURS", "FREE WIFI", "BUS STOP"], "A", "SLIPPERY FLOOR warns people about a possible hazard near the stairs.", "將地點的安全需求與標示功能配對，不被其他生活資訊干擾。", ["Identify the risk near a staircase.", "Read each sign for its purpose.", "Find the warning about the floor.", "Choose SLIPPERY FLOOR.", "Explain why opening hours or Wi-Fi do not warn about the hazard."]),
    ("A museum sign says **TOUCHING NOT ALLOWED**. Which sentence matches it?", ["You may touch every object.", "Please do not touch the objects.", "You must move the objects.", "The objects are for sale."], "B", "NOT ALLOWED means visitors must not do the action, so the matching sentence is a prohibition against touching.", "辨認 not allowed 的禁止功能，再轉成完整句意。", ["Find the action word TOUCHING.", "Interpret NOT ALLOWED as prohibited.", "Rewrite the meaning in a polite sentence.", "Choose Please do not touch the objects.", "Reject choices that allow moving, touching or selling."]),
    ("Which sign helps a traveler find a place to wait for a bus?", ["BUS STOP", "FIRST AID", "STAFF ONLY", "NO ENTRY"], "C", "BUS STOP names the place where passengers wait for a bus.", "先抓交通工具與場所的核心名詞，再排除醫療、限制和禁止標示。", ["Identify the travel goal: wait for a bus.", "Read the main noun in each sign.", "Match bus with the transport location.", "Choose BUS STOP.", "Check that FIRST AID and STAFF ONLY serve different purposes."]),
    ("A classroom label says **RECYCLE PAPER HERE**. What is its purpose?", ["To show where paper should be recycled.", "To tell students to throw away all books.", "To mark a place for eating.", "To announce a sports game."], "A", "The label combines the action recycle, the material paper and the location here, so it directs students to recycle paper at that spot.", "拆解動作、對象和地點三個部分，再合成標示功能。", ["Find the action RECYCLE.", "Find the material PAPER.", "Interpret HERE as the labeled location.", "Combine the three parts into one instruction.", "Choose the recycling-purpose description."]),
    ("Which sign tells people that only workers may enter?", ["WELCOME", "STAFF ONLY", "PLEASE SIT", "OPEN WINDOW"], "B", "STAFF ONLY limits entry to staff members, so it communicates a restricted area.", "找出身分限制詞 only，再判斷誰能進入。", ["Read each sign as a short instruction or label.", "Identify STAFF as a group of workers.", "Interpret ONLY as a restriction.", "Choose STAFF ONLY.", "Explain why welcome or sit does not control entry."]),
    ("A sign at a park says **TAKE YOUR TRASH HOME**. Which choice follows it?", ["Leave bottles on the grass.", "Put all trash in a river.", "Carry your trash away when you leave.", "Hide trash under a bench."], "C", "The sign asks visitors to take their rubbish away, so carrying it when leaving follows the instruction.", "先找祈使句動作，再把 trash 與 home 的方向轉成實際行為。", ["Locate the action TAKE.", "Identify the object YOUR TRASH.", "Interpret HOME as away from the park.", "Choose carrying the trash away.", "Reject hiding or leaving trash because they do not remove it responsibly."]),
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
    item = {"id": f"question-english-content-ac-iv-1-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ac-iv-1"], "difficulty": "easy", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究簡易英文標示、公共場所情境與行為判讀題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫簡易英文標示題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ac-iv-1-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
