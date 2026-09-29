import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "story reading, character, event, and comprehension patterns"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short stories, sequence, inference, and contextual reading"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English story comprehension, character motive, and application"),
]

DATA = [
    ("setting", "Story: 'Before sunrise, Mei waited beside the quiet harbor with a red lantern. Her grandfather's fishing boat was due back after the storm.' Where and when does the story begin?", ["At a harbor before sunrise.", "At a school gym at noon.", "In a desert after lunch.", "At an airport after midnight."], "At a harbor before sunrise.", "The words harbor and before sunrise directly establish the place and time. The boat and storm add context but do not change the opening setting."),
    ("character relationship", "Story: 'Jun could not reach the high shelf, so his older sister Hana brought him a small stool. He thanked her and continued organizing the books.' What is Hana's relationship to Jun?", ["She is his older sister.", "She is his new teacher.", "She is a shop owner he has never met.", "She is the captain of a boat."], "She is his older sister.", "The story explicitly calls Hana his older sister. Her helping action supports the family relationship but the direct clue is the phrase older sister."),
    ("event cause", "Story: 'The path was covered with fallen branches after the strong wind. The hikers chose a longer road through the village.' Why did they choose the longer road?", ["The usual path was blocked by branches.", "They wanted to buy a new boat.", "The village road had disappeared.", "They were looking for a swimming pool."], "The usual path was blocked by branches.", "The fallen branches made the original path difficult to use, causing the hikers to choose another route. This is a direct cause-and-effect relationship."),
    ("character goal", "Story: 'Niko checked the clock, packed the science model carefully, and hurried toward the bus stop. Today was the school exhibition.' What was Niko most likely trying to do?", ["Bring the model to the exhibition on time.", "Hide the clock from the bus driver.", "Cancel every school activity.", "Find a beach after the exhibition ended."], "Bring the model to the exhibition on time.", "Checking the time, protecting the model, and hurrying to the bus stop all support the goal of arriving with the model for the exhibition."),
    ("problem", "Story: 'The community garden's only watering can had a hole. The vegetables were becoming dry.' What problem did the gardeners face?", ["They lacked a usable watering can.", "They had too many fresh vegetables to eat.", "The garden was covered with snow indoors.", "The gardeners could not find any seeds in a book."], "They lacked a usable watering can.", "The hole in the only watering can prevents effective watering, and the dry vegetables show the consequence. That is the central problem described."),
    ("event sequence", "Story: 'First, Ava found a note under the bench. Next, she followed its arrows to the old tree. Finally, she discovered a box of letters.' What did Ava do after finding the note?", ["She followed its arrows to the old tree.", "She discovered the box before seeing the note.", "She planted a new garden.", "She returned the note to the bench without reading it."], "She followed its arrows to the old tree.", "The sequence signal Next places following the arrows between finding the note and discovering the box. The answer preserves the story's order."),
    ("emotion evidence", "Story: 'When the team finally heard the missing dog bark, Sara smiled and held the map tightly.' How did Sara most likely feel at that moment?", ["Relieved and hopeful.", "Bored and asleep.", "Angry that the dog was safe.", "Confused about whether there was a map."], "Relieved and hopeful.", "Hearing the missing dog provides hopeful evidence, and Sara's smile signals relief or happiness. The map detail suggests she is still engaged in finding the dog."),
    ("turning point", "Story: 'The bridge contest seemed lost when the first model broke. Then Eli noticed the group had used different lengths of wood and suggested rebuilding with equal pieces.' What changed the situation?", ["Eli identified a design problem and suggested a repair.", "The contest ended before anyone acted.", "The group threw away every piece of wood.", "The bridge won without being rebuilt."], "Eli identified a design problem and suggested a repair.", "The word Then introduces the turning point: Eli explains the unequal wood lengths and proposes a specific repair, changing the team's chances."),
    ('ending inference', 'Story: "At the end, the town placed a new bench under the tree. A small sign read, \'For everyone who waits.\'" What does the ending suggest?', ["The town turned the former waiting place into a shared welcoming space.", "The tree was removed from the town.", "No one may sit near the tree.", "The sign is an instruction to cut the bench."], "The town turned the former waiting place into a shared welcoming space.", "A bench and the words For everyone who waits suggest an inclusive place for people to rest or wait together. The ending adds a positive community meaning."),
    ("integrated story structure", "Story: 'Lena wanted to enter the night-sky contest, but her telescope was blurry. She cleaned the lens, asked her neighbor to check the focus, and later observed three clear stars. Her careful preparation earned a special mention.' Which summary is best?", ["Lena solved a telescope problem through preparation and received recognition.", "Lena refused to use a telescope and left before the contest.", "Her neighbor hid the stars and ended the contest.", "The contest was about cooking rather than observing the sky."], "Lena solved a telescope problem through preparation and received recognition.", "The summary includes the goal, problem, actions, result, and ending recognition without adding events. It captures the whole story arc rather than one isolated detail."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short narrative passages, setting, characters, events, sequence, motive, emotion, and ending inference; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the story and identify the narrative skill: {tag}.",
        f"Track the setting, characters, goal, problem, actions, turning point, and result, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other choices by requiring a direct clue or a cautious inference from the story; do not import events, relationships, or emotions that are not supported.",
        "Retell the relevant part in order, cite the exact evidence, and explain how the selected detail fits the story's larger cause-and-effect structure.",
    ]
    return {
        "id": f"question-english-content-ae-iv-6-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ae-iv-6"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; story settings, characters, events, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ae-iv-6", "examPatternRefs": refs,
        "solutionStrategy": "Build a compact story map—setting, characters, goal, problem, actions, turning point, and outcome—then answer from explicit clues and carefully bounded inference.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ae-iv-6-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
