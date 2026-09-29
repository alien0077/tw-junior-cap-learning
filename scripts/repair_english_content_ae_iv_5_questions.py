import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "short passages, genres, reading comprehension, and practical English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "text purpose, genre, details, and contextual inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English reading, short genres, and application tasks"),
]

DATA = [
    ("narrative genre", "Text: 'At first, Leo was afraid to enter the dark garden. Then he heard a kitten meow, followed the sound, and carried the kitten home.' What kind of text is this mainly?", ["A short narrative story", "A recipe", "A train schedule", "A dictionary entry"], "A short narrative story", "The text presents a character, a sequence of actions, and an event with a result. Those features identify a short narrative story."),
    ("informational purpose", "Text: 'Bees help many plants grow by carrying pollen from flower to flower. Without this process, some plants would produce fewer fruits.' What is the main purpose?", ["To explain how bees help plants.", "To invite readers to a birthday party.", "To sell a new backpack.", "To give directions to a station."], "To explain how bees help plants.", "The sentences give information about pollination and its effect on fruit production. They explain a process rather than invite, advertise, or direct."),
    ("notice genre", "Text: 'School garden volunteers meet beside the greenhouse at 3:30 on Wednesday. Bring gloves.' Which genre best fits this text?", ["A school notice", "A personal diary", "A fairy tale", "A restaurant review"], "A school notice", "The text gives a group, place, time, and required item for an event. That practical public information is typical of a notice."),
    ("diary viewpoint", "Text: 'I finally finished my model bridge today. It fell once, but I learned where to add support.' Why is this most likely a diary entry?", ["It records the writer's personal experience and reflection.", "It lists all trains leaving a station.", "It gives a public safety law.", "It compares prices in two shops."], "It records the writer's personal experience and reflection.", "The first-person I, a specific day, and reflection on learning show a personal diary voice and purpose."),
    ("advertisement purpose", "Text: 'Try the new SunTrail bottle! It keeps drinks cool for eight hours and fits in a school bag. Order this week for a free name label.' What is the text trying to do?", ["Persuade readers to buy a product.", "Report yesterday's weather.", "Tell a story about a lost bottle.", "Explain how to plant a tree."], "Persuade readers to buy a product.", "Positive product claims and a limited-time offer encourage readers to purchase the bottle. This is advertising language."),
    ("instruction text", "Text: 'First wash the apples. Next cut them into small pieces. Finally mix them with yogurt.' What is the best description of this text?", ["Instructions for preparing food", "A description of a historical battle", "A letter thanking a friend", "A chart of monthly temperatures"], "Instructions for preparing food", "First, next, and finally mark ordered steps, and the actions concern apples and yogurt. The text tells readers how to prepare food."),
    ("opinion evidence", "Text: 'I think our class should plant herbs by the window. They would make the room smell fresh, and we could use them in science observations.' Which sentence states the writer's opinion?", ["I think our class should plant herbs by the window.", "They would make the room smell fresh.", "We could use them in science observations.", "The window is in the classroom."], "I think our class should plant herbs by the window.", "I think and should signal the writer's recommendation. The following sentences give supporting reasons for that opinion."),
    ("report detail", "Text: 'The clean-up team collected 18 kilograms of paper on Saturday. This was 6 kilograms more than it collected in May.' What is the report's key comparison?", ["Saturday's collection was 6 kilograms higher than May's.", "May's collection was 18 kilograms higher than Saturday's.", "No paper was collected on Saturday.", "The team collected only plastic."], "Saturday's collection was 6 kilograms higher than May's.", "The phrase 6 kilograms more directly states the comparison and identifies Saturday as the larger amount."),
    ("genre and audience", "Which text is most suitable for telling parents the exact time and place of a school performance?", ["A short event notice with date, time, place, and ticket information", "A fantasy story with a talking moon", "A private diary entry about breakfast", "A dictionary list of unrelated verbs"], "A short event notice with date, time, place, and ticket information", "Parents need practical event details, so a notice organized around date, time, place, and tickets is the suitable genre and audience match."),
    ("integrated genre comparison", "Text A is a personal account of a student testing a solar oven. Text B lists the oven's materials and numbered building steps. Which statement is correct?", ["Text A mainly shares an experience, while Text B mainly gives instructions.", "Both texts are only advertisements for a restaurant.", "Text A is a timetable, while Text B is a birthday card.", "Text A gives no event and Text B gives no action."], "Text A mainly shares an experience, while Text B mainly gives instructions.", "A personal account focuses on what happened to the writer, while numbered materials and steps guide a reader through a process. The genres serve different purposes."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short passages, genre, purpose, audience, details, comparison, and inference; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the passage and identify the genre skill: {tag}.",
        f"Notice the writer, audience, organization, signal words, purpose, and evidence, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by comparing the passage's actual function and structure with each proposed genre or interpretation; do not decide from one isolated word.",
        "Summarize what the passage is doing, cite the clue that proves the answer, and explain how a different audience or purpose would require a different genre.",
    ]
    return {
        "id": f"question-english-content-ae-iv-5-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ae-iv-5"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; genre passages, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ae-iv-5", "examPatternRefs": refs,
        "solutionStrategy": "Identify who is writing to whom and why, then use organization, signal words, evidence, and expected reader action to distinguish genre from topic alone.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ae-iv-5-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
