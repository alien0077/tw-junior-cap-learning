#!/usr/bin/env python3
"""Independent English Ab-IV-1 sentence stress and intonation rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ab-iv-1"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "基礎英語句子朗讀與聽辨"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "問答、語句理解與聽力辨識"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "句子聽辨、問句與語意判斷"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求從句型、問答和聽辨情境判斷重讀資訊、語調功能與句意；本題採全新句子與情境。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("In the sentence **I want the BLUE notebook**, which word should receive extra stress if the speaker is correcting the color?", ["I", "want", "the", "BLUE"], "D", "If the correction is about color, BLUE carries the new or contrasted information, so it receives extra stress.", "先找說話者要修正或對比的資訊，再把重音放在關鍵字。", ["Read the sentence without guessing the context.", "Identify the corrected detail: the color.", "Match that detail to BLUE.", "Place the strongest stress on BLUE.", "Check that stressing I or want would change a different focus."]),
    ("Which intonation is most natural for the yes/no question **Are you ready?**", ["A falling tone at the end", "A rising tone at the end", "No change in pitch", "A long pause before every word"], "B", "A yes/no question commonly ends with rising intonation in basic conversational English, signaling that an answer is expected.", "先辨認句型，再依問句功能判斷句尾語調。", ["Locate the question mark and auxiliary verb Are.", "Classify the sentence as a yes/no question.", "Recall the usual conversational contour.", "Raise the pitch toward the end.", "Contrast it with a statement that normally falls."]),
    ("In **Mia bought a new guitar**, which word is most likely stressed as the main new information in a neutral sentence?", ["Mia", "bought", "a", "guitar"], "D", "In a neutral statement, the final content word guitar commonly carries the main sentence stress because it presents the new item.", "先找句中的內容詞，再觀察中性陳述常把主要重音放在哪裡。", ["Separate the function words from content words.", "Identify guitar as the final content noun.", "Treat the sentence as neutral, with no correction context.", "Give guitar the main stress.", "Explain that a different context could move the stress."]),
    ("A speaker says **You finished the project?** with a rising tone. What does the intonation most likely show?", ["A question or surprise seeking confirmation", "A final command", "A completed list with no response needed", "A spelling mistake"], "A", "The rising tone turns the statement-shaped words into a confirmation question and may also express surprise.", "把字面句型和實際語調一起判讀，不只看字面排列。", ["Notice that the words look like a statement.", "Hear the rising movement at the end.", "Infer that the speaker seeks confirmation.", "Allow surprise as an additional attitude.", "Reject command or spelling interpretations because they do not explain the tone."]),
    ("If a listener hears **I said Thursday, not Tuesday**, which contrast should be clearest?", ["I / said", "Thursday / Tuesday", "not / the", "said / not"], "B", "The meaning contrasts two days, so Thursday and Tuesday should receive the clearest contrastive stress.", "先找 not 所否定或更正的兩個對象，再成對標出重音。", ["Find the correction marker not.", "Identify the two compared days.", "Mark Thursday and Tuesday as the contrast pair.", "Stress both words clearly.", "Check that stressing I or said would not highlight the corrected information."]),
    ("Which sentence ending most likely has falling intonation because it gives information rather than asking a question?", ["Where is the bus?", "Did Lee call?", "The bus is here.", "Are they home?"], "C", "The bus is here is a statement that gives information, so a falling ending is the most likely neutral contour.", "先辨識陳述句與疑問句，再判斷中性句尾語調。", ["Read each sentence for its communicative purpose.", "Separate the three questions from the statement.", "Identify The bus is here as information.", "Use a falling contour at the end.", "Remember that emotion or special context can modify the contour."]),
    ("In **Can you bring my BAG?**, the speaker stresses BAG. What is being emphasized?", ["The ability to bring something", "The identity of the object to bring", "The person being addressed", "The time of the request"], "B", "Stress on BAG highlights which object the listener should bring, rather than ability, person, or time.", "把重音字詞換成問題『哪一部分被突出？』來判讀焦點。", ["Locate the stressed word BAG.", "List the possible information categories in the sentence.", "Match BAG to the object category.", "Choose the object identity as the focus.", "Compare with stress on Can or you to see how focus would change."]),
    ("A teacher says **Please open your books.** Which delivery best matches a polite classroom instruction?", ["Clear stress on open, with a calm falling tone", "A rising tone on every word", "Whispering the final word", "Stress only your and omit open"], "A", "The action word open needs clear prominence, while a calm falling tone makes the instruction complete and controlled rather than uncertain.", "先找指令的動作詞，再搭配清楚而完成的語調。", ["Identify the polite marker Please.", "Find the action the students must perform.", "Stress open enough to make the task clear.", "Use a calm falling ending.", "Check that the delivery remains polite rather than angry."]),
    ("Which change in stress best answers the question **Who borrowed the key?**", ["SAM borrowed the key.", "Sam BORROWED the key.", "Sam borrowed THE key.", "Sam borrowed the KEY."], "A", "The question asks for a person, so SAM should receive the strongest stress in the answer.", "讓回答的重音對應疑問詞 who 所要求的資訊類別。", ["Identify the question word Who.", "Decide that a person's name is required.", "Locate SAM in the answer.", "Stress SAM most strongly.", "Explain that stress on borrowed or key would answer a different question."]),
    ("A speaker says **You are coming.** with a strong falling tone. Which interpretation is most likely without extra context?", ["A confident statement or firm confirmation", "A yes/no question asking for the first answer", "A list of three items", "A spelling exercise"], "A", "The falling ending makes the utterance sound complete and assertive; a rising tone would more strongly invite confirmation.", "將語調視為說話者態度與句子完成度的線索。", ["Recognize the words as a statement-shaped sentence.", "Notice the strong falling ending.", "Infer completion or firmness.", "Compare it with the rising version.", "Keep the interpretation tentative because context can add emotion."]),
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
    item = {"id": f"question-english-content-ab-iv-1-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ab-iv-1"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究句子朗讀、問答、重音與語調辨識題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫句子重音語調題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ab-iv-1-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
