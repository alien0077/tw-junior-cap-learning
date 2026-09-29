#!/usr/bin/env python3
"""Independent English B-IV-3 verbal and nonverbal communication strategy rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-b-iv-3"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "日常對話與溝通理解"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中公開英語段考", "語意、語氣與溝通情境"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "對話策略、請求與回應"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求依對話目的選擇澄清、確認、禮貌請求、重述、肢體提示與語氣調整等語言或非語言策略；本題採全新情境。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("You cannot hear a friend in a noisy room. What is the best first strategy?", ["Move closer and ask, Could you say that again?", "Pretend to understand.", "Walk away without a word.", "Change the topic to lunch."], "A", "Moving closer and politely asking for repetition combines a useful nonverbal adjustment with a clear language strategy.", "先改善聽覺條件，再用禮貌語句確認訊息。", ["Identify the communication problem noise.", "Choose a physical adjustment closer.", "Add a request for repetition.", "Select the combined strategy.", "Reject pretending because it risks misunderstanding."]),
    ("A classmate looks confused after your explanation. What should you do?", ["Use simpler words and ask if the explanation is clear.", "Speak faster and louder without checking.", "Turn your back.", "Stop helping immediately."], "A", "Simpler language plus a check for understanding adapts the message and confirms whether it worked.", "同時調整語言難度與確認理解，不只重複原句。", ["Notice the listener's confused expression.", "Reduce vocabulary or sentence complexity.", "Ask a checking question.", "Choose the adaptive response.", "Avoid equating louder speech with clearer meaning."]),
    ("Which nonverbal action best shows that you are listening during a conversation?", ["Face the speaker, make natural eye contact and nod when appropriate.", "Look at your phone throughout.", "Turn away and cover your ears.", "Point to the exit immediately."], "A", "Facing the speaker, appropriate eye contact and nodding signal attention without interrupting.", "辨認能表達注意與理解的整組肢體線索。", ["Identify the goal showing attention.", "Compare the body positions.", "Choose the actions that face and acknowledge the speaker.", "Keep eye contact natural rather than staring.", "Reject actions that signal distraction or rejection."]),
    ("You need to borrow a classmate's calculator. Which wording is most polite?", ["Could I borrow your calculator, please?", "Give me that now.", "Your calculator is bad.", "I take it without asking."], "A", "Could I... please? makes the request respectful and gives the owner a chance to agree.", "用疑問句與 please 表達請求，避免命令或未經同意。", ["Identify the goal borrow a calculator.", "Look for a request form.", "Check for permission and politeness.", "Choose Could I borrow... please?", "Reject commands and taking without asking."]),
    ("A friend says, **I think the meeting is at three**, but you are unsure. What should you say?", ["Do you mean three o'clock? Let me check the message.", "Yes, definitely, without checking.", "I don't care.", "Change the meeting to yesterday."], "A", "The response confirms the time and proposes checking evidence instead of guessing.", "遇到不確定資訊時，用確認問題加上查證行動。", ["Identify the uncertain time.", "Form a focused confirmation question.", "Add a way to verify the message.", "Choose the evidence-based response.", "Reject confident guessing and unrelated replies."]),
    ("A visitor does not understand your directions. Which combination can help?", ["Point toward the entrance and repeat the key direction slowly.", "Use only a silent shrug.", "Speak in a different unrelated language and leave.", "Hide the map."], "A", "Pointing gives a visual cue and slow repetition reinforces the key spoken direction.", "把視覺提示和簡短語言結合，而不是只靠單一手勢。", ["Identify the failed directions.", "Choose the destination cue point toward the entrance.", "Repeat only the key information.", "Slow the speech for processing.", "Check that the combination remains helpful and respectful."]),
    ("Someone crosses their arms and avoids eye contact while you speak. What is the safest interpretation?", ["They may feel uncomfortable or unsure, so check in rather than assume.", "They definitely agree with every word.", "They are certainly asleep.", "Their body language proves they are angry."], "A", "Nonverbal cues can suggest discomfort or uncertainty, but they are not proof; a respectful check-in avoids overclaiming.", "把肢體線索當成可能訊號，再用語言確認，不直接貼標籤。", ["Observe the crossed arms and avoided eye contact.", "Treat them as possible signals, not certain facts.", "Ask a gentle checking question.", "Choose the cautious interpretation.", "Avoid claiming a single emotion is proven."]),
    ("You disagree with a friend's plan. Which response keeps the conversation constructive?", ["I see your idea, but could we compare both plans?", "That is stupid.", "I will leave before you finish.", "Everyone must use my plan."], "A", "Acknowledging the idea and proposing comparison expresses disagreement without attacking the person.", "先承認對方觀點，再提出可共同檢查的下一步。", ["Identify the disagreement.", "Separate the idea from the person.", "Use a soft contrast but.", "Suggest comparing evidence or plans.", "Choose the constructive response."]),
    ("A phone call has a bad connection. What should you do after saying **Could you repeat that?**?", ["Wait, listen carefully and summarize what you heard.", "Talk over the other person.", "Hang up without explanation.", "Answer a different question."], "A", "Waiting, listening and summarizing can reveal whether the repeated message was understood.", "請對方重說後，還要用摘要確認自己是否正確理解。", ["Recognize the first repair request.", "Give the other person time to respond.", "Listen for the key information.", "Summarize it for confirmation.", "Avoid speaking over the repaired message."]),
    ("Which strategy is best when speaking to a younger learner?", ["Use short sentences, gestures and a quick check for understanding.", "Use the longest words possible.", "Give many instructions at once without pauses.", "Refuse to show an example."], "A", "Short language, gestures and checking comprehension adapt both verbal and nonverbal communication to the listener.", "依對象調整語句長度、視覺提示與確認方式。", ["Consider the listener's age and likely vocabulary.", "Reduce the sentence length.", "Add a gesture or demonstration.", "Ask the learner to show or repeat the task.", "Choose the multi-strategy response."]),
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
    item = {"id": f"question-english-content-b-iv-3-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-b-iv-3"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究語言與非語言的澄清、確認、請求、聆聽、肢體提示與語氣策略題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫溝通策略題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-b-iv-3-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
