#!/usr/bin/env python3
"""Independent English Ac-IV-4 core vocabulary rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ac-iv-4"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "核心字彙、詞義與情境"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "基本字詞、對話與閱讀"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "生活詞彙與語境推理"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求從完整句與生活對話推斷核心字詞的詞義、詞性、搭配和語境，而非只背單一中文翻譯；本題採全新句子。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("The sky is dark, and rain is falling. You should take an ______ with you.", ["umbrella", "engine", "island", "pillow"], "A", "An umbrella is used to protect a person from rain; the other choices do not fit the weather context.", "先讀完整情境，再用功能與搭配排除不合語意的字。", ["Notice the clues dark sky and rain.", "Ask what object protects someone from rain.", "Compare the four nouns.", "Choose umbrella.", "Read the completed sentence to confirm natural meaning."]),
    ("Mia was very ______ after running five kilometers, so she drank two bottles of water.", ["tired", "quiet", "empty", "early"], "A", "Running a long distance and drinking water suggest that Mia felt tired.", "從事件與結果推回形容詞描述的狀態。", ["Find the event running five kilometers.", "Find the following action drinking water.", "Infer the physical condition.", "Choose tired.", "Reject words that describe sound, amount or time."]),
    ("Please ______ the lights before you leave the room.", ["turn off", "look for", "take care of", "wait for"], "A", "Turn off means stop a light from shining, which fits leaving the room.", "辨認動詞片語與 lights 的常見搭配。", ["Identify the object lights.", "List what actions can be done to lights.", "Match the leaving-room instruction.", "Choose turn off.", "Check that the other phrases require different objects or meanings."]),
    ("The museum is ______ the bank and the post office, so you can walk there in two minutes.", ["between", "during", "without", "against"], "A", "Between describes a location in the middle of two places.", "看到兩個地點並列時，優先檢查位置介系詞。", ["Locate the two reference places.", "Ask what word describes a middle position.", "Choose between.", "Insert it into the sentence.", "Confirm the time phrase supports a nearby location."]),
    ("Kevin forgot his lunch, so his sister ______ hers with him.", ["shared", "borrowed", "closed", "invited"], "A", "Shared means used or divided something together, which fits giving part of lunch to Kevin.", "由事件結果判斷動詞的互動關係，不只看字面。", ["Notice Kevin forgot his lunch.", "Infer that his sister provided part of hers.", "Compare the possible verbs.", "Choose shared.", "Explain why borrowed would require returning the same item."]),
    ("The road was blocked by a fallen tree, so the driver had to find another ______.", ["route", "habit", "promise", "message"], "A", "A route is a way from one place to another, so another route solves the blocked-road problem.", "先找問題類型，再選能解決交通路線問題的名詞。", ["Identify the obstacle on the road.", "Ask what a driver can change.", "Match another route to a different way.", "Choose route.", "Reject abstract nouns that do not describe a path."]),
    ("Please speak ______ because the baby is sleeping.", ["quietly", "heavily", "suddenly", "finally"], "A", "Quietly describes speaking with little noise, which matches the sleeping baby.", "將副詞和動詞 speak 的搭配與情境需求連結。", ["Find the action speak.", "Find the reason: a baby is sleeping.", "Choose the manner that reduces noise.", "Select quietly.", "Check that the other adverbs do not address sound level."]),
    ("The science team will ______ the results before writing its report.", ["compare", "invite", "repair", "celebrate"], "A", "Compare means examine similarities and differences, an appropriate step before reporting results.", "由 report 前的研究流程判斷動詞功能。", ["Notice the object results.", "Think about what researchers do with results.", "Match the analysis action.", "Choose compare.", "Reject social, maintenance and celebration actions."]),
    ("Lena saved money for months because she wanted to ______ a new bicycle.", ["buy", "lend", "lose", "hide"], "A", "Saving money for a desired bicycle indicates the purpose is to buy it.", "用 because 連接原因和目的，再判斷動詞方向。", ["Identify what Lena did: saved money.", "Identify the desired object: a bicycle.", "Ask what saving money makes possible.", "Choose buy.", "Reject lend, lose and hide because they do not express the purpose."]),
    ("The sign says the beach is closed ______ the storm.", ["because of", "next to", "instead of", "across from"], "A", "Because of introduces the reason for the beach being closed: the storm.", "看前後句的因果關係，再選原因片語。", ["Read the result: the beach is closed.", "Read the following noun: the storm.", "Identify a phrase that introduces a reason.", "Choose because of.", "Check that the location and substitution phrases do not fit."]),
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
    item = {"id": f"question-english-content-ac-iv-4-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ac-iv-4"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究基本字彙的語境、搭配、詞義與推理題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫核心字彙情境題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ac-iv-4-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
