import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "public announcements, locations, times, and actions"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "listening-style notices and practical detail"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional English, safety notices, and audience"),
]

DATA = [
    ("announcement purpose", "Announcement: 'Attention, visitors. The west entrance is closed for repairs. Please use the main entrance.' What is the purpose?", ["To tell visitors where to enter.", "To announce a new concert.", "To sell repair tools.", "To ask visitors to leave the city."], "A", "The announcement gives a closure and directs visitors to the main entrance, so its purpose is to guide entry."),
    ("location detail", "Announcement: 'The blue backpack was found near the second-floor science lab. Please ask at the office.' Where was it found?", ["Near the second-floor science lab", "Inside the office", "On the first-floor playground", "At the train station"], "A", "The location is stated directly as near the second-floor science lab; the office is where people should ask."),
    ("time change", "Station announcement: 'The 3:15 train to Harbor Town will leave at 3:35 from Platform 4.' What has changed?", ["The train leaves 20 minutes later from Platform 4.", "The train leaves 20 minutes earlier from Platform 3.", "The destination changes to the airport.", "The train is canceled."], "A", "The new time is 3:35 instead of 3:15, and the announcement gives Platform 4."),
    ("required action", "Library announcement: 'Please return all borrowed tablets to the service desk before closing at 6 p.m.' What should users do?", ["Return the tablets before 6 p.m.", "Take the tablets home overnight.", "Leave the tablets at the entrance next week.", "Return only books to the service desk."], "A", "The announcement names the object, place, and deadline: tablets must go to the service desk before 6 p.m."),
    ("safety reason", "Airport announcement: 'Because of strong winds, outdoor boarding at Gate 6 is temporarily suspended. Follow staff directions.' Why is the procedure changed?", ["Strong winds make the outdoor boarding unsafe.", "The gate has sold all its tickets.", "The airport wants to close every flight.", "Passengers forgot their luggage."], "A", "The announcement explicitly gives strong winds as the reason and asks passengers to follow staff instructions."),
    ("audience", "A museum announcement says, 'School groups, please meet your guides in the lobby at 10:00.' Who should follow this instruction?", ["School groups", "All drivers on the highway", "Only museum cleaners", "People who are not at the museum"], "A", "The direct address school groups identifies the intended audience."),
    ("lost item description", "A station announcement says, 'A small red wallet with a silver star was found on a bench by Exit B.' Which detail helps identify it?", ["A silver star", "A large blue handle", "Exit D", "A green suitcase"], "A", "The silver star is one of the announced identifying details of the wallet."),
    ("closure and alternative", "School broadcast: 'The gym is closed today. Basketball practice will take place in Room 204 at 4:00.' Where should players go?", ["Room 204 at 4:00", "The gym at 4:00", "Room 204 at 8:00", "The library immediately"], "A", "The announcement replaces the gym with Room 204 and keeps the practice time at 4:00."),
    ("deadline detail", "Park announcement: 'The north trail will close at sunset. Hikers already on the trail should return to the visitor center now.' What should hikers do?", ["Return to the visitor center now.", "Enter the north trail after sunset.", "Wait until midnight to leave.", "Ignore the closing notice."], "A", "The broadcast gives a direct safety instruction to hikers already on the trail."),
    ("integrated broadcast", "A ferry announcement says the 5:00 boat is delayed to 5:30 because of fog, passengers should keep their tickets, and boarding will be at Dock 2. Which summary is correct?", ["Keep the ticket, board at Dock 2, and wait for the 5:30 departure.", "Throw away the ticket and board at Dock 1 at 5:00.", "The ferry is canceled and moves to another city.", "Board at Dock 2 immediately at 4:00."], "A", "The summary combines the new time, unchanged ticket instruction, and new boarding location without adding a cancellation."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取公共場所廣播與功能聽讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以校園、車站、機場、圖書館與安全廣播測量目的、對象、地點、時間、行動與整合細節；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the announcement and identify the broadcast skill: {topic}.",
        "Circle who is addressed, where the event occurs, when it happens, what changed, why it changed, and what action is required.",
        f"Match every detail to the choices; the correct answer is {answer}.",
        f"Explain the announcement evidence: {explanation}",
        "Repeat the action, place, time, and safety condition in your own words, checking that no detail was swapped or invented.",
    ]
    return {"id": f"question-english-performance-1-iv-11-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-1-iv-11"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies public announcements and functional listening-reading patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; announcements, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-1-iv-11", "examPatternRefs": refs, "solutionStrategy": "Extract the audience, location, time, change, reason, and required action from the announcement, then select the option that preserves all relevant details.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-1-iv-11-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
