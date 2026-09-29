import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "dialogue roles, intentions, and functional language"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "role-play situations, requests, and appropriate responses"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "social exchanges, problem solving, and spoken application"),
]

DATA = [
    ("role and goal", "In a role-play, you are a customer whose drink order is wrong. What should your first line do?", ["Politely identify the order problem and ask for help.", "Blame every worker before describing the problem.", "Leave without speaking or checking the order.", "Change the conversation to tomorrow's weather."], "A", "The customer must state the specific problem and request a useful correction."),
    ("library role", "You play a librarian helping a student find a book. Which line fits your role?", ["Let me check the catalogue for you.", "I forgot every book, so do not ask me.", "You should repair the school bus.", "The catalogue is a sandwich."], "A", "Offering to check the catalogue is an action a librarian can reasonably take."),
    ("doctor-patient", "You play a patient describing a sore throat to a doctor. Which information is most relevant first?", ["When it started and whether you have a fever", "The color of your backpack", "The score of yesterday's game", "A stranger's home address"], "A", "Onset and fever are relevant health details for the doctor to understand the complaint."),
    ("tourist and guide", "You are a tourist who cannot find the train station. Which line best advances the role-play?", ["Excuse me, could you point me toward the train station?", "The station should find me by itself.", "I will ask the map to speak louder.", "You are a train because I am late."], "A", "The tourist politely states the need and asks the guide for directions."),
    ("class representative", "As the class representative, you need to announce a room change. Which message is complete?", ["Today's meeting is in Room 305 at four, not in Room 201.", "The room is a meeting and the meeting is a room.", "Everyone must guess the new place.", "I changed something but will not say what."], "A", "The message identifies the event, new place, time, and correction to the old place."),
    ("shop assistant", "You play a shop assistant and a customer asks for a cheaper option. Which reply is appropriate?", ["This model costs less; would you like to compare its features?", "You cannot ask about prices here.", "Buy the most expensive item without looking.", "The price is a type of weather."], "A", "The reply offers a lower-cost option and invites a relevant comparison."),
    ("misunderstanding", "In a role-play, your partner misunderstands your invitation. What should you do?", ["Restate the time and activity clearly, then check their understanding.", "Repeat the same unclear sentence louder forever.", "End the role-play by blaming your partner.", "Change the invitation into a math equation."], "A", "Restating the missing details and checking understanding repairs the exchange."),
    ("emergency response", "You play a student who sees water on the classroom floor. Which line is safest?", ["Please stay away from the wet area; I will tell the teacher.", "Run across it so everyone can see it.", "Hide the water under a bag.", "Invite younger students to slide on it."], "A", "The line warns others away and reports the hazard to a responsible adult."),
    ("turn-taking", "During a two-person interview role-play, what should the interviewer do after asking a question?", ["Listen to the answer and ask a relevant follow-up.", "Answer every question for the guest.", "Interrupt immediately with an unrelated topic.", "Leave before the guest speaks."], "A", "Listening and following up keep the interview connected to the guest's response."),
    ("integrated scene", "In a hotel role-play, a guest needs to report a missing key card and ask for breakfast time. Which line handles both purposes?", ["Excuse me, my key card is missing. Could you replace it and tell me when breakfast starts?", "Breakfast is a key card, so no one needs to help.", "I lost something yesterday; please answer every question.", "The hotel should guess whether I need a room."], "A", "The guest reports the concrete problem, requests replacement, and asks the separate time question politely."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取角色扮演與功能溝通能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以人物角色、溝通目的、問題處理、禮貌請求與追問測量情境口語應用；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the scene and identify the role-play focus: {topic}.",
        "Name the speaker's role, listener's role, immediate goal, and any safety or politeness requirement.",
        f"Choose the line that a person in that role could naturally say and that moves the scene forward; the correct answer is {answer}.",
        f"Explain why the line fits the role and purpose: {explanation}",
        "Perform the exchange with the partner, add one relevant reply, and check that the conversation remains respectful and connected to the original goal.",
    ]
    return {"id": f"question-english-performance-2-iv-9-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-2-iv-9"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies role-play and functional spoken-communication patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; roles, lines, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-2-iv-9", "examPatternRefs": refs, "solutionStrategy": "Identify each speaker's role and communicative goal, select a line that is relevant and polite, then continue the exchange to test whether it genuinely solves the scene's problem.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-2-iv-9-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
