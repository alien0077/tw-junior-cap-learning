import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "reading viewpoint, attitude, purpose, and contextual English comprehension"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short passage inference, tone, and writer intention"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English reading perspective, evidence, and application"),
]

DATA = [
    ("first-person viewpoint", "Text: 'I tucked the seed packet into my notebook because I wanted to remember the garden project.' Who tells this sentence?", ["A participant speaking as I", "A weather reporter speaking about a storm", "A machine with no connection to the project", "A crowd speaking only about tomorrow"], "A participant speaking as I", "The pronoun I shows first-person narration, and the action of tucking the packet indicates that the narrator participates in the garden project."),
    ("third-person viewpoint", "Text: 'Mara opened the window. She saw a kite above the trees and smiled.' Which viewpoint is used?", ["Third person, because the narrator refers to Mara as she.", "First person, because Mara says I.", "Second person, because the reader opens the window.", "No viewpoint, because there is no verb."], "Third person, because the narrator refers to Mara as she.", "The narrator names Mara and uses she rather than I. That is a third-person account of her action and response."),
    ("attitude", "Text: 'The repair team arrived before sunrise, carried every box carefully, and stayed until the playground was safe again. We are grateful for their patience.' What is the writer's attitude?", ["Appreciative", "Hostile", "Indifferent", "Mocking"], "Appreciative", "The careful description and We are grateful express respect and thanks toward the repair team. Nothing in the passage supports hostility or mockery."),
    ("purpose", "Text: 'Turn off the lights when you leave an empty room. This small habit saves energy every day.' What is the writer mainly trying to do?", ["Encourage an energy-saving action", "Tell a fantasy adventure", "Describe a new musical instrument", "Invite readers to ignore electricity use"], "Encourage an energy-saving action", "The imperative Turn off and the reason about saving energy show that the writer wants readers to adopt a habit."),
    ("tone", "Text: 'The puppy wore a tiny raincoat and marched proudly through the puddle while everyone laughed.' What tone is most likely?", ["Light and amused", "Angry and threatening", "Formal and legal", "Sad and hopeless"], "Light and amused", "Tiny raincoat, marched proudly, and everyone laughed create a playful, amused tone. The wording does not signal threat, law, or despair."),
    ("audience", "Text: 'Remember to bring your student ID and permission form on Monday. The bus leaves at 7:20.' Who is the most likely audience?", ["Students joining the trip", "People who repair buses in another city", "A cookbook editor", "Visitors buying movie tickets"], "Students joining the trip", "Student ID, permission form, Monday, and a bus departure time point to students preparing for a school trip."),
    ("attitude evidence", "Text: 'Some people call the old bridge useless, but its stone arches have carried neighbors safely for a hundred years.' What attitude does the writer show toward the bridge?", ["Respectful and supportive", "Completely uninterested", "Certain that it is dangerous", "Eager to destroy it"], "Respectful and supportive", "The writer counters the negative claim with a long history of safe service. That evidence shows respect for the bridge's value."),
    ("purpose distinction", "Text: 'Our survey found that 18 of 25 students prefer a quiet study corner. The results may help us plan the library.' What is the main purpose?", ["Report findings to support a library decision", "Make readers laugh at a fictional character", "Teach the steps of baking bread", "Advertise a new pair of shoes"], "Report findings to support a library decision", "The numbers report survey findings, and the final sentence connects them to planning. The purpose is informational and decision-supporting."),
    ("viewpoint limitation", "A first-person narrator says, 'I heard a crash behind the door, but I could not see what happened inside.' What should readers conclude?", ["The narrator knows a crash occurred but cannot confirm what happened inside.", "The narrator saw every detail inside the room.", "The crash definitely came from a falling tree outside.", "The narrator is describing another person's private thoughts."], "The narrator knows a crash occurred but cannot confirm what happened inside.", "The narrator reports hearing but explicitly says I could not see. A careful reader respects that limit instead of inventing unseen details or thoughts."),
    ("integrated analysis", "Text: 'I used to think the river was only a line on the map. After I helped collect plastic from its bank, I understood how many lives depend on clean water.' Which analysis is best?", ["A first-person narrator describes a changed attitude to encourage care for the river.", "A third-person narrator gives a neutral train schedule.", "The writer wants readers to buy a map and ignore pollution.", "The text proves that every river is already clean."], "A first-person narrator describes a changed attitude to encourage care for the river.", "I and my experience mark first person, while used to think and understood show changed attitude. The reflection on clean water supports an encouraging environmental purpose."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short passages, narrator viewpoint, attitude, purpose, audience, tone, and evidence-limited inference; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the passage and identify the interpretation skill: {tag}.",
        f"Mark pronouns, evaluative words, commands, reasons, audience clues, and limits of knowledge, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by requiring textual evidence and by separating the narrator's attitude or purpose from facts the passage does not establish.",
        "Restate who is speaking, to whom, with what attitude and purpose, cite the key phrase, and explain why the evidence supports the selected interpretation.",
    ]
    return {
        "id": f"question-english-content-ae-iv-7-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ae-iv-7"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; passage voice, attitudes, purposes, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ae-iv-7", "examPatternRefs": refs,
        "solutionStrategy": "Separate the narrator's voice from the topic: identify person, audience, purpose, evaluative language, and knowledge limits, then support every conclusion with a phrase from the passage.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ae-iv-7-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
