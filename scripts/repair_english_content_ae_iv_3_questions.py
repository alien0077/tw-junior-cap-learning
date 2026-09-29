import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "public announcements, listening-style comprehension, and practical English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short notices, announcements, and information extraction"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional English, public information, and contextual inference"),
]

DATA = [
    ("announcement purpose", "Announcement: 'Attention, visitors. The museum will close at 5:00 p.m. today for staff training.' Why is this announcement made?", ["To tell visitors the museum's closing time and reason.", "To invite visitors to train the staff.", "To announce that the museum opens at midnight.", "To ask visitors to paint the building."], "To tell visitors the museum's closing time and reason.", "The announcement gives a time, 5:00 p.m., and a reason, staff training. Its purpose is to help visitors plan around the early closing."),
    ("location", "Announcement: 'The lost-and-found desk has moved from the lobby to Room 204.' Where should someone look for a lost item?", ["Room 204", "The lobby only", "The museum roof", "The school cafeteria"], "Room 204", "The announcement states that the desk moved from the lobby to Room 204. The new location is the information needed."),
    ("time change", "Announcement: 'Due to heavy rain, Bus 7 will arrive ten minutes later than usual.' What should passengers expect?", ["Bus 7 will be delayed by ten minutes.", "Bus 7 will arrive ten minutes early.", "Bus 7 has changed into a train.", "Bus 7 will never run again."], "Bus 7 will be delayed by ten minutes.", "Later than usual means a delay. The notice gives the reason, heavy rain, and the amount, ten minutes."),
    ("required action", "Announcement: 'Passengers for Flight 208, please proceed to Gate 6 now.' What should those passengers do?", ["Go to Gate 6 now.", "Wait at Gate 1 tomorrow.", "Leave the airport and find a bus.", "Ask Flight 208 to come to their house."], "Go to Gate 6 now.", "Proceed to means go toward a place, and now gives the time. The flight number identifies the group of passengers who should act."),
    ("safety reason", "Announcement: 'Please hold the handrail while using the stairs.' Why is this instruction given?", ["To help people stay safe on the stairs.", "To make the stairs disappear.", "To tell people to run faster.", "To announce a change in the weather."], "To help people stay safe on the stairs.", "Holding a handrail is a safety action that can help prevent a fall. The announcement does not concern speed, weather, or the existence of the stairs."),
    ("object description", "Announcement: 'A blue backpack with a yellow key ring was found near the reading area.' What item was found?", ["A blue backpack with a yellow key ring.", "A yellow backpack with a blue ring.", "A blue book with a yellow cover.", "A key ring without a backpack."], "A blue backpack with a yellow key ring.", "The announcement gives two identifying details: the backpack is blue and its key ring is yellow. Both details must be preserved."),
    ("deadline", "Announcement: 'Students joining the science trip must submit permission forms by Friday.' When is the deadline?", ["Friday", "After the trip next month", "Every Monday morning", "There is no deadline"], "Friday", "By Friday sets the latest submission time. The announcement does not say next month or remove the deadline."),
    ("change of place", "Announcement: 'Today's school concert will be held in the gym instead of the auditorium.' Where will the concert take place?", ["In the gym", "In the auditorium", "On the school bus", "At the train station"], "In the gym", "Instead of marks a change from the auditorium to the gym. The new location is the gym."),
    ("speaker and audience", "Announcement: 'Library members, please return borrowed tablets to the front desk before closing.' Who should act?", ["People who borrowed library tablets.", "Every person in the city.", "Only the front-desk computer.", "Visitors who never entered the library."], "People who borrowed library tablets.", "The phrase library members identifies the audience, and borrowed tablets identifies the people responsible for returning them."),
    ("integrated announcement", "Announcement: 'The north entrance is closed for repairs. Visitors may enter through the west entrance, and the information desk will remain open until 8 p.m.' Which statement is correct?", ["Visitors should use the west entrance, and the information desk is open until 8 p.m.", "Visitors must use the north entrance before 8 a.m.", "Both entrances are closed and the desk is removed.", "The west entrance is open only for repairs."], "Visitors should use the west entrance, and the information desk is open until 8 p.m.", "The announcement gives a closed entrance, an alternative entrance, and the desk's closing time. The correct choice keeps all three pieces of information together."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short notices, announcements, schedules, locations, actions, and information extraction; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the announcement and identify the information function: {tag}.",
        f"Mark the named people, place, time, object, reason, or action, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by matching every detail to the announcement and by distinguishing the old location, new location, cause, audience, and deadline.",
        "Restate the announcement in your own words, cite the exact phrase that proves the answer, and check that no extra fact has been invented.",
    ]
    return {
        "id": f"question-english-content-ae-iv-3-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ae-iv-3"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; announcement contexts, details, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ae-iv-3", "examPatternRefs": refs,
        "solutionStrategy": "Extract the announcement's five Ws and one H—who, what, where, when, why, and how—then choose the action or conclusion that preserves the stated details exactly.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ae-iv-3-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
