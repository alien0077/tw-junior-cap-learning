import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "picture description, visual details, and practical English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "visual scenes, prepositions, actions, and contextual inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English image-based description, detail, and application"),
]

DATA = [
    ("location", "Picture description: A red ball is under the wooden table, while a blue bag is beside the chair. Where is the red ball?", ["Under the table", "Beside the chair", "Inside the blue bag", "On the roof"], "Under the table", "The preposition under places the red ball below the table. Beside the chair describes the blue bag, so the two objects must not be confused."),
    ("count", "Picture description: Three children are flying kites in a field. How many children are in the picture?", ["Three", "Two", "Four", "One"], "Three", "The description explicitly says three children. The kites are objects and should not be counted as children."),
    ("color and object", "Picture description: A yellow bird sits on a green fence. What color is the fence?", ["Green", "Yellow", "Blue", "Red"], "Green", "The adjective green modifies fence, while yellow modifies bird. The answer must follow the noun being asked about."),
    ("action", "Picture description: A boy is holding an umbrella, and rain is falling around him. What is the boy doing?", ["Holding an umbrella", "Riding a bicycle", "Reading under a tree", "Cooking soup"], "Holding an umbrella", "The present participle holding identifies the visible action. Falling rain gives the setting but does not replace the boy's action."),
    ("comparison", "Picture description: The elephant is taller than the dog, but the dog is faster. Which statement is correct?", ["The elephant is taller than the dog.", "The dog is taller than the elephant.", "The elephant is faster than the dog.", "They are both the same height and speed."], "The elephant is taller than the dog.", "The description directly compares height and speed: elephant is taller, dog is faster. The answer preserves the correct comparison."),
    ("spatial relation", "Picture description: A clock hangs above the classroom door, and a plant stands near the window. What is above the door?", ["A clock", "A plant", "A window", "A desk"], "A clock", "Above identifies the vertical relationship, and the description says the clock hangs above the door. The plant is near the window."),
    ("scene purpose", "Picture description: At a park, a woman is putting bottles into a recycling bin while two children read the sign beside it. What are they most likely learning about?", ["Recycling", "Cooking noodles", "Train schedules", "Playing chess"], "Recycling", "The recycling bin, bottles, and sign form a clear visual group of clues about recycling. The scene does not mention the other activities."),
    ("negative detail", "Picture description: The kitchen has two cups and one plate on the table. There is no spoon. Which object is missing?", ["A spoon", "A cup", "A plate", "A table"], "A spoon", "The phrase there is no spoon explicitly marks the missing item. The cups, plate, and table are present."),
    ("sequence from scene", "Picture description: In the first frame, a girl holds an empty basket. In the second, she picks apples. In the third, the basket is full. What happened in the second frame?", ["She picked apples.", "She ate all the apples.", "She washed the basket in a river.", "She left the basket at home."], "She picked apples.", "The second frame is described directly as the moment when she picks apples. The full basket in the third frame supports the sequence."),
    ("integrated picture description", "Picture description: In a sunny park, two friends sit on a bench, a dog sleeps beside them, and a kite is caught in a tree. Which statement is supported?", ["Two friends are sitting on a bench while a dog sleeps nearby.", "Three dogs are flying a kite in the rain.", "The friends are inside a dark classroom.", "The kite is under the bench and the dog is in the tree."], "Two friends are sitting on a bench while a dog sleeps nearby.", "The answer combines the number of people, their position, and the dog's action and location without changing the sunny park scene. The other choices reverse or invent details."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use visual scenes, location, count, color, action, comparison, sequence, and inference; this is an independent text-based rewrite of picture-reading ability without copying images, wording, options, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the picture description and identify the visual-reading skill: {tag}.",
        f"Map each noun to its color, position, number, action, or frame before choosing, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by checking object identity, preposition, quantity, action, comparison, and frame order; do not swap details between objects.",
        "Describe the relevant part of the scene in a full sentence, cite the exact visual clue, and verify that the selected answer preserves the scene rather than inventing a detail.",
    ]
    return {
        "id": f"question-english-content-b-iv-6-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-b-iv-6"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies picture-reading patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; scene descriptions, values, options, explanation, and transfer task are original; no protected picture is copied; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-b-iv-6", "examPatternRefs": refs,
        "solutionStrategy": "Inventory the scene before interpreting it: identify each object, its attributes, location, action, and frame position, then answer only from the stated visual evidence.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-b-iv-6-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
