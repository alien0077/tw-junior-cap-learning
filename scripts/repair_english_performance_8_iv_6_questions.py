import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "international etiquette, greetings, public behavior, and practical situations"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "travel etiquette, requests, queues, dining, gifts, and privacy"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "appropriate international behavior and context-sensitive communication"),
]

DATA = [
    ("greeting", "You meet a host family for the first time. Which action is a generally respectful beginning?", ["Greet them politely, introduce yourself, and follow their preferred form of greeting", "Ignore everyone until they leave", "Assume physical contact is always expected", "Begin by criticizing their home"], "A", "A polite introduction combined with attention to the hosts' preference is respectful and adaptable."),
    ("queue behavior", "At an international airport, many passengers are waiting at a service counter. What should you do?", ["Join the line and wait for your turn", "Move to the front because your question is important", "Stand across the entrance and block others", "Ask someone to leave the line for you"], "A", "Joining and waiting in line respects shared public space and other passengers."),
    ("dining request", "You are unsure whether a dish contains an ingredient you cannot eat. Which request is appropriate?", ["Could you please tell me whether this dish contains peanuts?", "This food is bad, and everyone must change it.", "Eat it without asking and complain afterward.", "Take another guest's dish without permission."], "A", "The clear and polite question protects the diner while respecting the host or server."),
    ("public space", "A visitor wants to listen to music on a crowded train. Which action shows consideration?", ["Use headphones at a low volume and follow the train rules", "Play music loudly so every passenger can hear", "Stand in front of the doors during every stop", "Leave bags on several seats"], "A", "Headphones, reasonable volume, and attention to rules reduce disturbance."),
    ("photography privacy", "At a cultural event, you want to photograph a performer up close. What should you do first?", ["Ask for permission and follow the event's photography rules", "Take the photo secretly because public events remove all privacy", "Step onto the performance area without asking", "Publish the photo with a made-up story"], "A", "Permission and event rules protect privacy and the dignity of participants."),
    ("gift response", "A host gives you a small gift. Which response is generally polite?", ["Thank the host and show appreciation for the thought", "Laugh at the gift before opening it", "Demand a more expensive gift", "Refuse to acknowledge the host"], "A", "Thanks and appreciation recognize the host's effort without judging the price."),
    ("punctuality", "You will be ten minutes late for an arranged meeting in another country. What should you do?", ["Contact the person promptly, apologize, and give an honest arrival estimate", "Say nothing and make the person wait indefinitely", "Blame the person for choosing a meeting time", "Arrive late and pretend the meeting was canceled"], "A", "Prompt notice and a realistic estimate allow the other person to plan."),
    ("personal space", "A new acquaintance stands farther away than you expected while talking. What is the best response?", ["Respect the distance and observe the person's comfort instead of forcing closeness", "Move closer until the person steps back", "Assume the person dislikes every visitor", "Make fun of the person's preferred distance"], "A", "Respecting personal space accommodates different comfort levels and cultural norms."),
    ("service language", "You need help at a station where staff speak another language. Which strategy is most useful?", ["Use a polite greeting, simple words, a map or translation aid, and confirm the answer", "Shout the same complex sentence repeatedly", "Point angrily and demand immediate service", "Give up without trying any respectful communication"], "A", "Simple language, tools, and confirmation support clear and courteous communication."),
    ("integrated etiquette", "A student plans an overseas visit. Which preparation is most responsible?", ["Learn local expectations, check venue rules, ask before photographing or joining customs, and adapt respectfully.", "Assume local rules do not apply to visitors.", "Copy every visible behavior without understanding its context.", "Judge customs only by whether they match the student's habits."], "A", "The plan combines research, permission, rules, privacy, and context-sensitive adaptation."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取國際生活禮儀的問候、公共空間、飲食、隱私、時間、禮物與情境溝通能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量與旅遊情境常測量問候、請求、排隊、餐飲、拍照、守時、個人空間、公共規則與合宜回應；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the international-life situation and identify the etiquette target: {topic}.",
        "Mark the people involved, local or venue rules, privacy, time, personal space, food, public behavior, and communication need.",
        f"Choose the action that is polite, safe, permission-aware, and adaptable to context; the correct answer is {answer}.",
        f"Explain why the action respects both the other person and the situation: {explanation}",
        "Reread the situation and check that the answer follows stated rules without assuming every culture or person behaves identically.",
    ]
    return {"id": f"question-english-performance-8-iv-6-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-8-iv-6"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies international daily etiquette, public behavior, privacy, dining, time, gifts, space, requests, and context-sensitive communication only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; etiquette situations, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-8-iv-6", "examPatternRefs": refs, "solutionStrategy": "Read the context and rules first, protect privacy and shared space, communicate politely, and adapt without turning one custom into a universal rule.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-8-iv-6-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
