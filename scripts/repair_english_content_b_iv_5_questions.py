import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "who, what, when, where, why, and how questions in context"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "descriptions, question words, details, and contextual inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English information questions, description, and application"),
]

DATA = [
    ("who", "Read: 'Jordan delivered the science posters to the office before lunch.' Who delivered the posters?", ["Jordan", "The office", "Lunch", "The posters"], "Jordan", "Who asks for a person or group. The sentence names Jordan as the subject who performed delivered."),
    ("what", "Read: 'The volunteers planted twelve trees beside the playground.' What did they plant?", ["Twelve trees", "A playground", "A group of volunteers", "A lunch box"], "Twelve trees", "What asks about the thing affected by the action. The object planted was twelve trees, while beside the playground describes location."),
    ("when", "Read: 'The art workshop begins at 2:30 on Saturday.' When does it begin?", ["At 2:30 on Saturday", "Beside the art room", "With three teachers", "Because the room is bright"], "At 2:30 on Saturday", "When asks for time or date. The sentence gives both a clock time and a day."),
    ("where", "Read: 'The chess team practices in the community library after school.' Where does it practice?", ["In the community library", "After school only", "The chess team", "At a sports stadium"], "In the community library", "Where asks for place. After school gives time, but the location is in the community library."),
    ("why", "Read: 'Nora wore a raincoat because dark clouds covered the sky.' Why did Nora wear a raincoat?", ["Because rain seemed possible.", "Because she was attending a music concert.", "Because the raincoat was a library.", "Because she had finished lunch."], "Because rain seemed possible.", "Because introduces the reason. Dark clouds suggest possible rain, which explains the raincoat."),
    ("how", "Read: 'Sam carried the fragile model with both hands and walked slowly.' How did Sam carry it?", ["With both hands and slowly", "By throwing it across the room", "At midnight in a library", "Because the model was blue"], "With both hands and slowly", "How asks about manner. The sentence gives both the physical method, with both hands, and the movement speed, slowly."),
    ("which description", "Read: 'The small silver key was under the red notebook.' Which object is described as silver?", ["The key", "The notebook", "The desk", "The room"], "The key", "The adjective silver comes directly before key and describes it. Red describes the notebook, so the colors must not be confused."),
    ("question matching", "Which question matches the answer 'At the east gate'?", ["Where should we meet?", "Who should we meet?", "Why should we meet?", "How many should we meet?"], "Where should we meet?", "At the east gate is a place answer, so it responds to Where. Who asks for a person, why for a reason, and how many for a quantity."),
    ("multi-detail answer", "Read: 'On Friday morning, Dr. Chen spoke to the class in Room 208 about safe online passwords.' What did Dr. Chen speak about?", ["Safe online passwords", "Friday morning", "Room 208", "The class itself"], "Safe online passwords", "What did ... speak about? asks for the topic. Friday morning is time, Room 208 is place, and the class is the audience."),
    ("integrated question set", "Read: 'At 5 p.m. on Sunday, Leo and his sister baked bread in their grandmother's kitchen to prepare for a family picnic.' Which answer correctly describes the event?", ["Leo and his sister baked bread in their grandmother's kitchen for a picnic.", "Their grandmother baked a picnic at 5 a.m. on Monday.", "Leo played chess alone in the school office.", "They baked bread because the kitchen was a person."], "Leo and his sister baked bread in their grandmother's kitchen for a picnic.", "The correct answer combines who, what, where, and purpose without changing the time or inventing a different event. It is a complete evidence-based description."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use question words, personal descriptions, event details, locations, time, reasons, manner, and contextual answers; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the description and identify the question-word skill: {tag}.",
        f"Match who, what, when, where, why, or how to the relevant grammatical role and detail, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by distinguishing person, object, time, place, reason, manner, and descriptive adjective instead of selecting a nearby word at random.",
        "Restate the answer as a complete sentence, point to the exact phrase that supplies the information, and check that no detail was added or changed.",
    ]
    return {
        "id": f"question-english-content-b-iv-5-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-b-iv-5"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; description contexts, question forms, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-b-iv-5", "examPatternRefs": refs,
        "solutionStrategy": "Classify the question word before reading the choices: who=person, what=thing/topic, when=time, where=place, why=reason, how=manner or method; then locate the matching phrase.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-b-iv-5-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
