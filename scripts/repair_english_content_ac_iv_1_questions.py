import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "signs, notices, and practical English reading"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short notices, public signs, and contextual meaning"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional English, directions, and sign interpretation"),
]

DATA = [
    ("prohibition sign", "You see a sign that says 'NO ENTRY.' What should you do?", ["Do not go into the area.", "Enter quickly before it closes.", "Ask the area to enter you.", "Leave the door open for others."], "Do not go into the area.", "No entry is a prohibition: people are not allowed to go into that place. The sign does not mean that entry is merely delayed."),
    ("action sign", "A door has the sign 'PUSH.' What action is required?", ["Move the door away from you with your hand.", "Pull the door toward you.", "Knock three times and wait.", "Lock the door from inside."], "Move the door away from you with your hand.", "Push means press or move something away from yourself. Pull has the opposite direction."),
    ("safety notice", "What should a visitor do after seeing 'WET FLOOR'?", ["Walk carefully because the floor may be slippery.", "Run across the floor before it dries.", "Put books on the wet area.", "Turn off every light in the building."], "Walk carefully because the floor may be slippery.", "Wet floor is a safety warning. A careful person slows down and watches their step because the surface may cause a fall."),
    ("direction sign", "A museum sign says 'EXIT →'. Where should you go?", ["Follow the arrow toward the way out.", "Go to the museum gift shop only.", "Stand under the sign and wait for a ticket.", "Turn off the emergency lights."], "Follow the arrow toward the way out.", "Exit means a way out. The arrow adds direction, so the visitor should follow it toward the building's exit."),
    ("environmental sign", "Which action follows the sign 'KEEP OFF THE GRASS'?", ["Stay on the path and do not walk on the grass.", "Sit in the middle of the grass.", "Move the sign onto the grass.", "Water the grass with a drink."], "Stay on the path and do not walk on the grass.", "Keep off means do not step on or use the named area. The safe alternative is to remain on the path."),
    ("facility label", "A door is marked 'RESTROOMS'. What is the sign telling you?", ["Bathrooms are in or behind that area.", "Food is available only there.", "The room is a classroom for science.", "No one may wash their hands there."], "Bathrooms are in or behind that area.", "Restrooms is a common public label for bathrooms. A label identifies the facility; it does not give a prohibition."),
    ("recycling sign", "A bin is labeled 'PAPER ONLY.' Which item belongs in it?", ["A clean sheet of paper.", "A glass bottle.", "A banana peel.", "A metal spoon."], "A clean sheet of paper.", "Paper only limits the bin to paper items. The other objects belong to different material categories and should not be placed there."),
    ("opening notice", "A shop window says 'CLOSED TODAY.' What can a customer infer?", ["The shop is not open for business today.", "The shop is giving every item away today.", "The shop is open only after midnight today.", "The customer must close the shop personally."], "The shop is not open for business today.", "Closed today states that the shop will not serve customers on this day. It does not identify a later opening time or a task for the customer."),
    ("permission sign", "A gallery displays 'NO PHOTOGRAPHY.' Which action follows the sign?", ["Keep the camera put away and do not take pictures.", "Take a flash photo from farther away.", "Photograph only the largest painting.", "Ask a friend to take the picture secretly."], "Keep the camera put away and do not take pictures.", "No photography prohibits taking pictures in the gallery. Changing distance or asking someone else does not remove the restriction."),
    ("transfer from sign to action", "A library notice says 'PLEASE RETURN BOOKS BY FRIDAY.' What is the best plan?", ["Bring the borrowed books back no later than Friday.", "Keep the books forever because please means optional.", "Return only the book covers and keep the pages.", "Wait until the notice is removed next month."], "Bring the borrowed books back no later than Friday.", "The notice politely gives a deadline: the borrowed books should be returned by Friday. Please makes the request courteous, not meaningless."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short functional texts, notices, directions, and context-based inference; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the sign or notice and identify its function: {tag}.",
        f"Translate the key word or phrase into an action, restriction, direction, facility, or deadline; apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by matching the notice's exact scope and force; do not add permission, remove a prohibition, or invent information not shown on the sign.",
        "Reread the complete situation, state the action a visitor should take, and explain which words in the sign provide the evidence.",
    ]
    return {
        "id": f"question-english-content-ac-iv-1-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ac-iv-1"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; sign language, contexts, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ac-iv-1", "examPatternRefs": refs,
        "solutionStrategy": "Find the operative word first, determine whether the sign warns, directs, permits, prohibits, labels, or sets a deadline, and then choose only the action supported by the exact wording.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ac-iv-1-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
