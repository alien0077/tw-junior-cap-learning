import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "who, what, when, where, and functional responses"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "dialogue details, descriptions, and information exchange"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "everyday descriptions, question words, and application"),
]

DATA = [
    ("person", "Mia is carrying a yellow umbrella and waiting beside the school gate. Who is waiting there?", ["Mia", "The bus driver", "The principal", "A shopkeeper"], "A", "The sentence names Mia as the person carrying the umbrella and waiting by the gate."),
    ("action", "A notice says, 'Leo returned the borrowed camera to the library desk.' What did Leo do?", ["He returned a camera.", "He bought a desk.", "He photographed the library.", "He borrowed a notice."], "A", "Returned the borrowed camera is the action stated in the notice."),
    ("time", "The art club meets every Wednesday at 4:10 p.m. When does it meet?", ["Every Wednesday at 4:10 p.m.", "Every Friday at noon", "Only on the first day of summer", "Before the school opens on Monday"], "A", "The schedule gives both the repeating day and the exact time."),
    ("place", "The lost-and-found box is next to the nurse's office on the first floor. Where is the box?", ["On the first floor next to the nurse's office", "Inside the gym locker room", "Behind the library on the third floor", "Outside the school bus"], "A", "The location includes the floor and the office beside it."),
    ("object description", "A student describes a small silver key with a red tag marked 'Lab 2.' Which object matches the description?", ["A small silver key with a red Lab 2 tag", "A large black book with a blue label", "A red umbrella without a tag", "A silver coin marked 'Gym 1'"], "A", "The correct object matches size, color, type, tag color, and label."),
    ("reason", "Nora moved the meeting indoors because strong wind began. Why did she move it?", ["Because strong wind began", "Because the meeting had already ended", "Because she lost the indoor room", "Because the calendar was blank"], "A", "The because-clause directly gives the reason for moving the meeting."),
    ("sequence", "First Ken printed the form; then he signed it and placed it in the office tray. What did he do after printing?", ["He signed the form and put it in the tray.", "He threw away the printer.", "He went home before writing anything.", "He printed the form for the second time only."], "A", "After printing, the next two actions were signing and placing the form in the tray."),
    ("appropriate reply", "A classmate asks, 'Where is the science fair?' Which reply gives the needed information?", ["It is in the auditorium beside the main hall.", "I went there yesterday with my cousin.", "Science is a very interesting subject.", "The fair has many colors."], "A", "The reply answers where by naming the venue and a nearby landmark."),
    ("correct a detail", "The message says, 'The blue backpack is under the bench, not on it.' Which statement is accurate?", ["The blue backpack is under the bench.", "The blue backpack is on top of the bench.", "A red backpack is under the desk.", "The bench is inside the backpack."], "A", "The correction changes the relationship from on the bench to under the bench."),
    ("integrated description", "A report says, 'At 7:30, three volunteers planted herbs behind the cafeteria because the garden team needed help.' Which summary is complete?", ["At 7:30, three volunteers planted herbs behind the cafeteria to help the garden team.", "The cafeteria served herbs to three volunteers at noon.", "The garden team planted trees in front of the library alone.", "Three volunteers met somewhere but did not do anything."], "A", "The summary preserves the time, people, action, place, and purpose from the report."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取人事時地物資訊擷取與回應能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以短訊息、公告、對話與描述題測量 who/what/when/where、細節配對、順序及功能性回應；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the message and identify the information target: {topic}.",
        "Mark the exact person, action, time, place, object feature, reason, or order word that the question asks about.",
        f"Match every detail in the choices with the message and select the complete, accurate response; the correct answer is {answer}.",
        f"Explain the match from the wording: {explanation}",
        "Put the answer back into the original question, check that no detail was changed, and say which extra detail would be needed if the situation changed.",
    ]
    return {"id": f"question-english-performance-2-iv-6-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-2-iv-6"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies information-description and functional-response patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; prompts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-2-iv-6", "examPatternRefs": refs, "solutionStrategy": "Identify the question word, extract only the matching detail from the description, compare all choices against the source wording, and preserve the complete set of who/what/when/where information.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-2-iv-6-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
