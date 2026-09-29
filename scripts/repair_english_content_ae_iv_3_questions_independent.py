#!/usr/bin/env python3
"""Independent English Ae-IV-3 public announcement rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ae-iv-3"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "聽力、生活對話與訊息辨識"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "公共情境、時間與地點資訊"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "廣播、公告與行動判讀"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求從公共場所廣播或短公告擷取地點、時間、人物、原因、限制及下一步行動；本題採全新廣播稿。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("Announcement: **The 10:15 train to Hsinchu will leave from Platform 3.** Where should passengers go?", ["Platform 1", "Platform 2", "Platform 3", "The ticket office"], "A", "The announcement directly says the train will leave from Platform 3.", "先抓交通工具與出發地點，再把數字對應到選項。", ["Identify the train time.", "Locate the departure platform.", "Ignore the destination when answering where.", "Choose Platform 3.", "Check that the ticket office is not the departure platform."]),
    ("Airport announcement: **Flight 208 is delayed because of heavy rain.** Why is it delayed?", ["A lost passport", "Heavy rain", "A full bus", "A closed restaurant"], "A", "The announcement explicitly gives heavy rain as the reason for the delay.", "看到 because of 後直接找原因，避免把航班編號當答案。", ["Find the flight number.", "Look for the reason marker because of.", "Match the following weather condition.", "Choose heavy rain.", "Reject unrelated airport services."]),
    ("Library announcement: **The library will close at 6 p.m. today.** What should visitors remember?", ["They can stay until midnight.", "They should leave before or at closing time.", "They must buy a ticket.", "They should go to Platform 6."], "A", "Visitors need to plan to leave by the stated closing time.", "先讀 will close at 的時間，再推回聽眾需要採取的行動。", ["Identify the place library.", "Locate the closing time 6 p.m.", "Infer the action visitors need to take.", "Choose leaving by closing time.", "Reject answers about tickets or transport."]),
    ("School announcement: **The basketball game has moved to the gym because the field is wet.** Where is the game now?", ["The field", "The gym", "The library", "The parking lot"], "A", "The game moved to the gym, and the wet field is the reason for the change.", "分開判斷原地點、改後地點與原因，回答現在的位置。", ["Find the original place field.", "Notice the movement phrase moved to.", "Identify the new location gym.", "Choose the gym.", "Use the wet field only as the reason, not the answer."]),
    ("Station announcement: **Please keep your ticket until you leave the station.** What should passengers do?", ["Throw the ticket away immediately.", "Keep the ticket with them.", "Give the ticket to a friend.", "Buy a sandwich."], "A", "The instruction says passengers should keep the ticket until they leave.", "辨認祈使句與時間界線 until，再轉成實際行動。", ["Locate the action keep.", "Identify the object ticket.", "Notice the time limit until leaving.", "Choose keeping the ticket.", "Reject actions that discard or change the object."]),
    ("Museum announcement: **The west gallery is closed for cleaning. Please use the east entrance.** Which entrance should visitors use?", ["The west entrance", "The east entrance", "The roof", "The gift shop"], "A", "The announcement directs visitors to use the east entrance because the west gallery is closed.", "先找禁止或關閉的區域，再找 Please use 的替代行動。", ["Identify the closed area west gallery.", "Find the explicit direction use.", "Match it with east entrance.", "Choose the east entrance.", "Do not confuse the gallery with the entrance."]),
    ("Bus announcement: **The next stop is City Hall. Passengers for the hospital should get off there.** Who should get off at the next stop?", ["Passengers going to the hospital.", "Passengers going to the airport only.", "The bus driver only.", "People who are not on the bus."], "A", "The announcement names hospital passengers as the group that should get off at City Hall.", "把 next stop 的地點與 for the hospital 的乘客條件連接起來。", ["Locate the next stop City Hall.", "Identify the passenger condition for the hospital.", "Match the condition to the action get off.", "Choose hospital passengers.", "Reject groups not mentioned in the announcement."]),
    ("Park announcement: **For safety, please do not enter the lake after dark.** When is entry not allowed?", ["Before breakfast only", "After dark", "At noon only", "During the morning class"], "A", "The time condition after dark marks when entering the lake is not allowed.", "從 for safety 找規則，再用 after dark 定位時間條件。", ["Identify the prohibited action enter the lake.", "Find the safety reason.", "Locate the time phrase after dark.", "Choose after dark.", "Do not replace the time with an unrelated daily activity."]),
    ("Shopping-center announcement: **A blue backpack was found at the information desk.** Where can its owner ask about it?", ["The information desk", "The cinema screen", "The parking exit", "The food court kitchen"], "A", "The backpack was found at the information desk, so the owner should ask there.", "將 found at 的地點和失物處理行動配對。", ["Identify the lost item blue backpack.", "Locate where it was found.", "Infer where the owner should ask.", "Choose the information desk.", "Reject other shopping-center locations."]),
    ("Hospital announcement: **Visitors for Room 405 may enter between 2 and 4 p.m.** When may they enter?", ["Before 8 a.m.", "Between 2 and 4 p.m.", "At midnight only", "After the hospital closes"], "A", "The announcement gives a permitted time window from 2 to 4 p.m.", "看到 between A and B 時，保留完整時間區間。", ["Identify the visitors' purpose.", "Locate Room 405.", "Read both ends of the time window.", "Choose between 2 and 4 p.m.", "Reject times outside the stated interval."]),
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
    item = {"id": f"question-english-content-ae-iv-3-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ae-iv-3"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究公共場所廣播的地點、時間、原因、限制與行動題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫公共場所廣播題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ae-iv-3-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
