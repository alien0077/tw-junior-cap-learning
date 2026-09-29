import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "dialogue, role-play, functional English, and contextual response"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short exchanges, social roles, and practical communication"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English conversation, requests, and situation-based application"),
]

DATA = [
    ("restaurant role", "Role-play: You are a customer in a cafe. Which sentence best orders a sandwich politely?", ["Could I have a sandwich, please?", "Sandwich me yesterday.", "You must be the sandwich's teacher.", "Where does the sandwich study?"], "Could I have a sandwich, please?", "Could I have ...? is a polite customer request. It names the desired item and includes please."),
    ("shop role", "Role-play: You are a shopper looking for a blue notebook. Which question should you ask the clerk?", ["Excuse me, where can I find blue notebooks?", "Why did the notebook eat lunch?", "I am finding the clerk yesterday.", "Please sell me a weather."], "Excuse me, where can I find blue notebooks?", "Excuse me gains attention politely, and where can I find ...? asks the clerk for the item's location."),
    ("asking directions role", "Role-play: You are a visitor at a station and need to reach the museum. Which opening is appropriate?", ["Excuse me, could you show me the way to the museum?", "Museum, please become a station.", "I showed the way tomorrow yesterday.", "You are the map because I am late."], "Excuse me, could you show me the way to the museum?", "The sentence politely requests directions and identifies the destination. It fits the visitor's role and immediate need."),
    ("school mediation", "Role-play: Two classmates want the same computer. Which line begins a fair solution?", ["Let's take turns so we can both finish our work.", "I will hide the computer and end the discussion.", "You must lose because I spoke first.", "The computer should choose the louder person."], "Let's take turns so we can both finish our work.", "Taking turns recognizes both classmates' needs and proposes a practical, fair arrangement. The other lines escalate or avoid the conflict."),
    ("travel check-in", "Role-play: At a hotel, you want to confirm the time for breakfast. What should you ask?", ["Could you tell me what time breakfast starts?", "Breakfast, why did it travel?", "I started the hotel next year yesterday.", "The room is a question mark."], "Could you tell me what time breakfast starts?", "The polite question identifies the information needed: the start time of breakfast. It suits a guest speaking to hotel staff."),
    ("help in an emergency", "Role-play: Your friend falls and says that an ankle hurts badly. Which response is most responsible?", ["Stay still; I will call an adult or emergency help.", "Run away and turn off the lights.", "Tell the ankle to walk faster.", "Take a photo and laugh."], "Stay still; I will call an adult or emergency help.", "The response offers calm immediate care and seeks appropriate adult or emergency assistance. It does not move, mock, or ignore an injured person."),
    ("agreeing in character", "Role-play: Your teammate suggests making a poster about saving water. You support the idea. What should you say?", ["That sounds good. I can design the title.", "Your idea is a spoon yesterday.", "No, and I will do nothing forever.", "Posters cannot have any words."], "That sounds good. I can design the title.", "That sounds good expresses agreement, and I can design the title assigns a useful contribution. The response moves the team toward action."),
    ("polite disagreement", "Role-play: A partner proposes meeting at midnight, but you think it is too late. Which response is respectful?", ["I see your idea, but could we meet earlier?", "Your idea is stupid; leave.", "Midnight is a banana, so yes.", "I disagree and will never explain why."], "I see your idea, but could we meet earlier?", "The response acknowledges the partner, states disagreement without insult, and proposes a workable adjustment."),
    ("interview role", "Role-play: In a club interview, the leader asks, 'Why do you want to join?' Which answer gives a relevant reason?", ["I enjoy building things, and I want to learn with the team.", "Because the chair is blue yesterday.", "I am joining a reason at seven.", "No, the club is a weather report."], "I enjoy building things, and I want to learn with the team.", "The answer gives two relevant motivations: interest in building and a desire to learn with others. It responds to why rather than changing the topic."),
    ("integrated role-play", "Role-play: You are a visitor whose bus is delayed. You must inform a tour guide, ask for the new meeting place, and remain polite. Which line does all three?", ["Excuse me, my bus is delayed. Could you tell me where we should meet now?", "The bus is late, so nobody can help me ever.", "You must move the bus to the museum because I am a ticket.", "I will say nothing and follow a stranger."], "Excuse me, my bus is delayed. Could you tell me where we should meet now?", "The line politely gains attention, explains the problem, and asks for updated location information. It fits the visitor's role and the guide's role as an information source."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short dialogues, requests, roles, social situations, conflict solutions, and practical response selection; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the role-play situation and identify the role and communication goal: {tag}.",
        f"Determine who is speaking, to whom, what action or information is needed, and what tone is appropriate, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other lines by checking role, relevance, grammar, politeness, safety, and whether the response actually advances the scene.",
        "Perform both sides of the exchange aloud, explain the speaker's goal, and show which words make the selected line natural and responsible.",
    ]
    return {
        "id": f"question-english-content-b-iv-7-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-b-iv-7"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies role-play and functional communication patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; role-play situations, roles, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-b-iv-7", "examPatternRefs": refs,
        "solutionStrategy": "Enter the speaker's role, identify the immediate goal and listener, then choose a line that is relevant, grammatical, socially appropriate, safe, and capable of moving the scene forward.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-b-iv-7-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
