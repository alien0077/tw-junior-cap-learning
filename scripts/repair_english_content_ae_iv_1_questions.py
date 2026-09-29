import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "short texts, reading comprehension, and practical English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "dialogue, short passage, and contextual inference formats"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English reading, story sequence, and application tasks"),
]

DATA = [
    ("song main idea", "Read the original lyric: 'Pack a smile, take a friend, / Every road can be a bend. / Step by step, we learn to see / New surprises patiently.' What is the main idea?", ["Learning patiently can make a journey rewarding.", "Every road is perfectly straight.", "A friend should never travel.", "Surprises must be avoided."], "Learning patiently can make a journey rewarding.", "The lines connect a journey, a friend, step-by-step learning, and new surprises. Together they encourage patient learning rather than describing a straight road or avoiding discovery."),
    ("rhyme pair", "In the couplet 'The little boat can float / Beside the bright green coat,' which words create the clearest end rhyme?", ["float / coat", "little / bright", "boat / green", "the / beside"], "float / coat", "Float and coat share the long /oʊt/ ending sound. The rhyme is based on sound at the ends of the lines, not on words that merely appear close together."),
    ("story sequence", "A short story says: 'Nora found a lost key. She asked three neighbors about it. At last, Mr. Wu recognized the key and opened the community box.' What happened immediately before Mr. Wu opened the box?", ["Nora asked neighbors about the key.", "Nora found a new bicycle.", "Mr. Wu lost the key again.", "The community box disappeared."], "Nora asked neighbors about the key.", "The story presents finding the key, asking neighbors, and then Mr. Wu recognizing and using it. The asking stage comes immediately before the opening."),
    ("character intention", "In the short play, Sam says, 'I practiced the welcome line three times, but my hands are still shaking.' What does Sam most likely feel?", ["Nervous but prepared to perform.", "Angry that nobody came to school.", "Sleepy because the play ended yesterday.", "Certain that practice is useless."], "Nervous but prepared to perform.", "Shaking suggests nervousness, while practicing three times shows preparation and a wish to perform. The line does not support anger, sleepiness, or rejection of practice."),
    ("stage direction", "The script reads: 'Mia: The lantern is over there. [Mia points toward the window.]' What is the bracketed sentence for?", ["It tells the actor what movement to perform.", "It is another character's spoken line.", "It gives the audience a ticket price.", "It changes the setting to a hospital."], "It tells the actor what movement to perform.", "A bracketed stage direction describes an action or movement that accompanies the spoken line. It is not usually said aloud as dialogue."),
    ("short-text evidence", "A poem says, 'Rain taps softly on the roof; / Inside, we share warm soup.' Which setting is best supported?", ["A cozy indoor place during rainy weather.", "A dry beach under a cloudless sky.", "A crowded stadium during a race.", "A desert with no shelter."], "A cozy indoor place during rainy weather.", "The roof and warm soup indicate shelter and comfort indoors, while rain taps outside. The other settings conflict with these details."),
    ("dialogue response", "In a skit, Alex says, 'The poster fell before the show.' Bea replies, 'Let's fix it together before the audience arrives.' What does Bea do?", ["She proposes a cooperative solution.", "She blames Alex and leaves.", "She cancels every future show.", "She says the poster never fell."], "She proposes a cooperative solution.", "Let's fix it together is a proposal to solve the immediate problem cooperatively. Bea neither denies the event nor abandons the show."),
    ("sound word", "In the line 'Drip, drop, drip—the quiet rain begins,' what effect does 'drip, drop' create?", ["It imitates the small repeated sound of rain.", "It names the speaker's favorite food.", "It proves that the rain is loud thunder.", "It gives the exact temperature."], "It imitates the small repeated sound of rain.", "Drip and drop are sound-like words that help readers hear the repeated, gentle rain. They do not provide food, thunder, or a numerical temperature."),
    ("inference from ending", "At the end of a story, the lost puppy follows a familiar whistle and wags its tail when it sees the family. What is the most reasonable inference?", ["The puppy recognizes the family and is happy to return.", "The puppy has never heard the whistle.", "The family is trying to hide from the puppy.", "The puppy wants to become a whistle."], "The puppy recognizes the family and is happy to return.", "Following the familiar whistle and wagging its tail are evidence of recognition and a positive response. The conclusion stays within the story's clues."),
    ("integrated performance", "A class performs a short verse about helping a friend. Which plan best supports the meaning?", ["Use two clear voices, pause at line breaks, and show the helping action when the verse mentions it.", "Read every line faster and hide all gestures.", "Speak only the final word and skip the story.", "Change every friendly line into an angry shout."], "Use two clear voices, pause at line breaks, and show the helping action when the verse mentions it.", "Different voices identify the speakers, pauses preserve the verse structure, and a matching gesture makes the helping idea visible. The other plans reduce or contradict the meaning."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short texts, dialogues, verse or story comprehension, sequencing, and contextual inference; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the lyric, story, or script and identify the comprehension focus: {tag}.",
        f"Underline the words that show sound, sequence, setting, intention, action, or evidence, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by requiring direct support from the text; do not add events, feelings, or stage actions that the passage does not imply.",
        "Reread or perform the short text, cite the exact clue that supports the answer, and explain how the feature contributes to meaning or presentation.",
    ]
    return {
        "id": f"question-english-content-ae-iv-1-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ae-iv-1"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; lyric, story, script, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ae-iv-1", "examPatternRefs": refs,
        "solutionStrategy": "Read or perform the whole text before choosing: track explicit clues, order events, sound patterns, character purpose, and stage action, then select only the interpretation supported by those clues.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ae-iv-1-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
