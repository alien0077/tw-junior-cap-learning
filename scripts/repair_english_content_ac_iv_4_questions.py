import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "vocabulary in context, collocation, and practical English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "basic vocabulary, word forms, and contextual inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English vocabulary, sentence meaning, and usage application"),
]

DATA = [
    ("context meaning", "The trail was very narrow, so only one person could walk on it at a time. What does narrow mean here?", ["not wide", "very noisy", "full of water", "easy to see"], "not wide", "The sentence contrasts the trail with the number of people who can use it side by side. Narrow means having little width, not noisy or wet."),
    ("verb collocation", "Which word best completes the sentence: 'Please ____ a photo of our team before the game.'?", ["take", "do", "make", "put"], "take", "English commonly says take a photo. The other verbs can be used with different nouns, but they do not form the natural collocation in this sentence."),
    ("adjective contrast", "The classroom was noisy before the teacher arrived, but it became ____ during the test.", ["quiet", "heavy", "expensive", "early"], "quiet", "Quiet is the opposite of noisy and describes the sound level expected during a test."),
    ("word family", "Which form correctly completes the sentence: 'The weather report was ____ useful for our trip.'?", ["especially", "especial", "specialness", "specialize"], "especially", "Especially is an adverb that modifies useful. The sentence needs an adverb, not the adjective special or unrelated noun and verb forms."),
    ("noun in context", "Mia put the warm soup in a bowl and used a ____ to eat it.", ["spoon", "blanket", "helmet", "ticket"], "spoon", "A spoon is an eating utensil that fits the action and soup context. The other objects do not serve that purpose."),
    ("preposition collocation", "Which word completes the natural phrase: 'interested ____ science'?", ["in", "on", "at", "to"], "in", "The adjective interested is followed by in when naming the subject of interest: interested in science."),
    ("meaning from consequence", "Leo forgot his umbrella and arrived home with wet clothes. What can we infer?", ["It probably rained.", "He probably baked a cake.", "He probably bought dry sand.", "He probably closed the library."], "It probably rained.", "Wet clothes plus a forgotten umbrella strongly support the inference that Leo was outside in rain. The other choices do not explain the consequence."),
    ("countable noun", "Which sentence uses the word 'advice' correctly?", ["My coach gave me some useful advice.", "My coach gave me two advices.", "My coach advised a advice.", "My coach gave me an advices."], "My coach gave me some useful advice.", "Advice is normally an uncountable noun in English, so some useful advice is correct. We do not usually make it plural as advices."),
    ("prefix meaning", "If a student is unhappy, what does the prefix 'un-' help show?", ["not happy", "very happy", "happy again", "able to make happy"], "not happy", "The prefix un- often gives a negative meaning. Unhappy therefore means not happy in this context."),
    ("integrated vocabulary", "The notice says, 'Bring a reusable bottle. The park has no drinking-water station.' Which action best follows the notice?", ["Carry a bottle that can be used again because no water station is available.", "Leave every bottle at home and expect the park to provide water.", "Bring a single-use bottle and throw it on the path.", "Bring a blanket instead of any container."], "Carry a bottle that can be used again because no water station is available.", "Reusable describes an item that can be used again, and the second sentence explains why visitors need to bring their own container: the park has no drinking-water station."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use basic vocabulary in context, collocation, word forms, and short-text inference; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the sentence or notice and identify the vocabulary skill: {tag}.",
        f"Use nearby grammar, collocation, contrast, consequence, or prefix evidence, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by testing both their dictionary meaning and their fit with the sentence's grammar and real-world situation.",
        "Reread the complete sentence with the selected word, explain the evidence in your own words, and note how the word could transfer to a new context.",
    ]
    return {
        "id": f"question-english-content-ac-iv-4-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ac-iv-4"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; vocabulary contexts, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ac-iv-4", "examPatternRefs": refs,
        "solutionStrategy": "Read vocabulary through the whole sentence: check grammar and collocation first, then use contrast, cause, word formation, and real-world context to select the only meaning that fits.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ac-iv-4-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
