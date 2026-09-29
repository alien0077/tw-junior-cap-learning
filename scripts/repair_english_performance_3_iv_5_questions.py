import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "everyday expressions, dialogue purpose, and responses"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "functional phrases, social situations, and context"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "daily language, politeness, and application"),
]

DATA = [
    ("greeting", "A classmate says, 'Good morning!' Which response is natural?", ["Good morning!", "Good night yesterday.", "I am a morning desk.", "No, the morning is a color."], "A", "Good morning is the conventional response to the same greeting."),
    ("thanks", "A friend lends you a pen and says, 'Here you are.' What should you say?", ["Thanks, that helps a lot.", "You are a pen yesterday.", "No one may lend anything.", "The pen should thank me."], "A", "The response acknowledges the favor and expresses appreciation."),
    ("apology", "You step on someone's foot by accident. Which expression is appropriate?", ["I'm sorry. Are you okay?", "Congratulations on your foot.", "Please step on me again.", "The accident is a birthday."], "A", "The speaker apologizes and checks the other person's condition."),
    ("offer", "Your classmate is carrying too many books. Which sentence offers help?", ["Let me carry some of those books for you.", "You must carry every book alone.", "The books are carrying me tomorrow.", "I will hide the books without asking."], "A", "Let me...for you is a direct, polite offer of assistance."),
    ("accept invitation", "A friend invites you to a study session, and you are available. Which reply accepts?", ["Sure, I'd be happy to join you.", "I cannot join because I am already there yesterday.", "Study sessions are not people.", "Please invite someone who is not me."], "A", "The reply clearly accepts and shows willingness to attend."),
    ("decline politely", "You cannot attend a movie because of a family appointment. Which response is polite?", ["Thanks, but I can't go tonight. Maybe another day?", "No, your movie is a bad idea.", "I will accept and never arrive.", "The appointment is the movie's actor."], "A", "The response thanks the friend, gives a brief reason, and suggests a future possibility."),
    ("preference", "A server asks, 'Would you like tea or juice?' You prefer juice. What should you say?", ["Juice, please.", "Either the chair or tomorrow.", "I would like the question.", "Tea is a location."], "A", "Juice, please states the choice and remains polite."),
    ("clarification", "You do not understand a new word in a conversation. Which phrase asks for meaning?", ["What does that word mean?", "The word should explain me.", "I understand every word by guessing.", "Meaning is a kind of weather."], "A", "The question directly asks for the definition of the unfamiliar word."),
    ("agreement", "A partner suggests checking the directions before leaving. You agree. Which reply fits?", ["That's a good idea.", "No idea can be good because it is an object.", "I agree yesterday tomorrow.", "Directions should check themselves."], "A", "That's a good idea expresses agreement with the suggestion."),
    ("integrated exchange", "A guest arrives late, apologizes, explains the bus delay, and asks whether the meeting has started. Which opening is best?", ["Sorry I'm late. The bus was delayed. Has the meeting started yet?", "I am late, so nobody may speak about the bus.", "The meeting is a bus and the delay is a guest.", "I arrived yesterday and will ask tomorrow."], "A", "The exchange apologizes, gives the relevant reason, and asks the needed question."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取簡易生活用語與情境回應能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以問候、道謝、道歉、邀請、偏好、澄清與生活對話測量功能語言及禮貌回應；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the exchange and identify the everyday-language function: {topic}.",
        "Identify the speaker's intention, the listener's previous line, the relationship, and the politeness level needed.",
        f"Choose the response that completes the social exchange naturally; the correct answer is {answer}.",
        f"Explain the phrase's function and context fit: {explanation}",
        "Say both lines aloud and check that the response acknowledges the situation, answers the need, and does not introduce an unrelated claim.",
    ]
    return {"id": f"question-english-performance-3-iv-5-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-5"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies everyday functional-expression patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; situations, expressions, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-5", "examPatternRefs": refs, "solutionStrategy": "Identify the social purpose of the previous line, select the expression that is semantically relevant and appropriately polite, and test it by continuing the dialogue.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-5-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
