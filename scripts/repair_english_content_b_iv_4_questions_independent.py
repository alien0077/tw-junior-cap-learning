#!/usr/bin/env python3
"""Independent English B-IV-4 needs, wants and feelings rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-b-iv-4"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "生活需求、喜好與感受"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中公開英語段考", "對話、意願與情緒"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "請求、偏好與情境推理"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求理解 want、need、would like、feel、prefer 等需求意願感受字句，並依情境選擇合宜回應；本題採全新情境。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("A: **I need a quiet place to study.** B: ______", ["The library may be a good choice.", "I want a red bicycle.", "It was sunny yesterday.", "My brother is tall."], "A", "A library is a plausible quiet place for studying and directly responds to the stated need.", "先辨認 need 的目標，再找能滿足需求的建議。", ["Identify the need quiet place.", "Identify the activity study.", "Look for a place that fits both.", "Choose the library suggestion.", "Reject unrelated preferences and facts."]),
    ("A: **Would you like tea or juice?** B: **______**", ["Juice, please.", "I am at the station.", "I felt tired yesterday.", "The cup is blue."], "A", "Juice, please chooses one of the offered drinks politely.", "由選擇問句判斷要回答其中一個選項，並保持禮貌。", ["Identify the two choices tea and juice.", "Look for a direct selection.", "Add a polite word.", "Choose Juice, please.", "Reject place, past feeling and color statements."]),
    ("Maya says, **I am excited because my team reached the final.** How does Maya feel?", ["Excited.", "Bored.", "Angry.", "Sleepy."], "A", "The sentence directly uses excited to describe Maya's feeling.", "抓明示情緒詞，再用 because 後的事件確認。", ["Locate the feeling word.", "Read the reason her team reached the final.", "Match the word to the choices.", "Choose excited.", "Do not replace the stated feeling with an invented one."]),
    ("A: **Can you help me carry this box?** B: **______**", ["Sure. It looks heavy.", "I prefer winter.", "It is my birthday.", "No, the movie starts at eight."], "A", "Sure accepts the request and the second sentence shows awareness of the box's weight.", "辨認 can you 的請求，再選接受並與物品情境相符的回應。", ["Identify the requested action carry.", "Find acceptance language.", "Check the comment relates to the box.", "Choose Sure. It looks heavy.", "Reject preferences, dates and unrelated schedules."]),
    ("Leo wants a warm drink, but the cafe only has cold juice and water. What does Leo need to do?", ["Choose an available drink or ask about another warm option.", "Pretend the juice is hot.", "Leave the cafe without speaking.", "Order a bicycle."], "A", "Leo's need is a warm drink, so he should choose a realistic available option or ask whether another warm option exists.", "區分需求與現有選項，再提出能解決落差的行動。", ["Identify Leo's need warm drink.", "List the available drinks.", "Notice the mismatch.", "Choose a realistic choice or clarification.", "Reject pretending and unrelated orders."]),
    ("A: **Which activity do you prefer, drawing or dancing?** B: **______**", ["I prefer drawing.", "I need a pencil yesterday.", "It feels rainy.", "She is my aunt."], "A", "I prefer drawing directly answers the choice question about activity preference.", "由 prefer 問句找出表達偏好的句型。", ["Identify the two activities.", "Find a response containing prefer.", "Choose one activity.", "Select I prefer drawing.", "Reject time, weather and relationship statements."]),
    ("After missing the bus, Nina says, **I feel frustrated.** What does frustrated most likely mean here?", ["Annoyed or upset about a problem.", "Very hungry for lunch.", "Certain about a plan.", "Happy about a surprise."], "A", "Missing the bus creates a problem, so frustrated means upset or annoyed in this context.", "用事件線索推定感受詞，而不是只靠孤立翻譯。", ["Identify the event missing the bus.", "Ask what emotion a problem can cause.", "Compare the meanings in the options.", "Choose annoyed or upset.", "Reject feelings not supported by the situation."]),
    ("A friend says, **I want to join, but I need to finish my homework first.** What is true?", ["The friend wants to join but has a prior need.", "The friend dislikes the activity completely.", "The homework is already finished.", "The friend is asking for a new phone."], "A", "The sentence states a desire to join and a condition that must be completed first.", "用 but 區分意願與先決需求，兩部分都要保留。", ["Identify the desired action join.", "Find the contrast marker but.", "Identify the prior task homework.", "Choose the combined statement.", "Reject conclusions that erase either side."]),
    ("A: **I feel cold. Could we close the window?** What does the speaker want?", ["The window closed.", "A larger classroom.", "A new jacket for someone else.", "The lights turned on at noon."], "A", "The speaker's feeling cold leads to a request to close the window.", "把感受與後面的請求連成需求—行動關係。", ["Identify the feeling cold.", "Locate the request Could we.", "Find the requested action close the window.", "Choose the desired result.", "Reject options not connected to the window."]),
    ("A: **Do you want to watch the documentary?** B: **Not tonight; I have an exam tomorrow.** Why does B decline?", ["Because of the exam tomorrow.", "Because the documentary is in a museum.", "Because B wants a bicycle.", "Because tonight is a holiday."], "A", "B gives the exam tomorrow as the reason for declining tonight.", "先判斷意願回應，再從後句找拒絕的原因。", ["Identify the invitation watch the documentary.", "Notice Not tonight as a decline.", "Read the reason after the semicolon.", "Choose the exam reason.", "Reject details not stated in the dialogue."]),
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
    item = {"id": f"question-english-content-b-iv-4-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-b-iv-4"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究需求、意願、感受、請求與情境回應題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫需求意願感受題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-b-iv-4-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
