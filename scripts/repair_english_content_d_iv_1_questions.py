import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "integrated information and inference"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "notices, schedules, and cross-source details"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "information integration and practical inference"),
]

DATA = [
    ("notice plus schedule", "The library notice says study rooms close at 5 p.m. on Friday. The weekly schedule says the bus leaves at 5:20 p.m. What can a student do?", ["Study until closing time and then take the 5:20 bus.", "Stay in the library until midnight.", "Take the bus at 4 p.m. because rooms close at 5.", "The schedule proves the library is closed all week."], "A", "Combining the closing notice with the bus schedule shows that the student can leave at 5 and still catch the 5:20 bus."),
    ("table plus paragraph", "A paragraph says Mia prefers quiet activities. A table lists painting at 2 p.m. in Room 1 and basketball at 2 p.m. outdoors. Which activity fits both pieces of information?", ["Painting in Room 1", "Basketball outdoors", "Both are equally quiet according to the text", "Neither activity is scheduled"], "A", "The paragraph gives Mia's preference and the table identifies painting as the indoor scheduled choice, so painting best fits both."),
    ("map plus rule", "A map places the west gate beside the bicycle path. A rule says bicycles must enter through a gate beside a bicycle path. Which entrance should a cyclist use?", ["The west gate", "The roof entrance", "Any locked gate", "The swimming-pool window"], "A", "The map supplies the location relationship and the rule supplies the requirement; together they identify the west gate."),
    ("price plus budget", "A museum page lists student tickets at $80. A notice says visitors also need a $20 activity pass. Leo has $100. What is true?", ["Leo has exactly enough for one ticket and one activity pass.", "Leo is short $20.", "Leo can buy two complete sets.", "The activity pass is free."], "A", "The two required costs total $100, matching Leo's budget exactly."),
    ("weather plus plan", "The forecast says heavy rain from 1 to 4 p.m. The club plan schedules an outdoor game at 2 and an indoor workshop at 3. What is the most sensible adjustment?", ["Move the game indoors or postpone it and keep the workshop indoors.", "Hold the game outside at 2 without checking conditions.", "Cancel every future club meeting.", "Move both activities into the rain."], "A", "The forecast conflicts with the outdoor game but not the indoor workshop, so the game needs an adjustment."),
    ("announcement plus eligibility", "An announcement says the science contest is open to Grade 8 students. The sign-up list shows Ruby is in Grade 8 and has submitted the form. What can be inferred?", ["Ruby meets the stated entry conditions.", "Ruby has already won the contest.", "Only Grade 9 students may enter.", "Ruby submitted the form for a music concert."], "A", "The announcement supplies eligibility and the list supplies Ruby's grade and submission, supporting only that she meets the conditions."),
    ("two-source travel plan", "A train timetable shows the 9:10 train arrives at 9:45. A tour note says visitors must check in by 10:00. If the station is a ten-minute walk from the tour desk, which plan works?", ["Take the 9:10 train and walk directly to check in by 9:55.", "Take a train arriving at 10:05.", "Wait at the station until 10:00 before walking.", "The timetable makes check-in unnecessary."], "A", "Arrival at 9:45 plus ten minutes of walking gives 9:55, before the 10:00 deadline."),
    ("survey plus recommendation", "A class survey shows 18 students want more shade and 4 want more benches. The yard map shows trees can be planted only along the north fence. What recommendation uses both sources?", ["Plant shade trees along the north fence first.", "Remove all trees and add benches everywhere.", "Ignore the survey because maps have no use.", "Build shade only in the south where planting is impossible."], "A", "The survey identifies the stronger need and the map identifies the feasible location, so the north fence is the evidence-based recommendation."),
    ("email plus deadline", "An email asks students to return tablets before Wednesday. The calendar shows Tuesday is the last school day before a two-day closure. When should a student return one?", ["By Tuesday, before the closure begins", "During the closure at school", "Next month", "Only after receiving a new tablet"], "A", "The email gives the requirement and the calendar shows Tuesday is the last available school day before closure."),
    ("integrated conclusion", "A poster says the market uses reusable containers. A data card reports trash fell from 120 bags to 75 bags after the program. Which conclusion is best supported?", ["The reusable-container program was followed by a 45-bag decrease in recorded trash.", "The program eliminated all waste forever.", "The market produced more trash after the program.", "The data card does not contain numbers."], "A", "The two numbers show a decrease of 45 bags, and the wording 'after' supports a careful association, not a claim that all waste disappeared or that causation is certain."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取綜合資訊與推論能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常合併公告、時間表、圖表、地圖、規則與生活情境，要求學生整合至少兩項資料後推論；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read every source and identify the integration task: {topic}.",
        "Write down the exact date, time, number, place, rule, eligibility, or requirement from each source.",
        f"Join only the compatible facts and compare each option; the correct answer is {answer}.",
        f"Explain the inference and its limit: {explanation}",
        "Check the arithmetic, time order, location, and wording one more time, then separate a supported inference from an unsupported prediction.",
    ]
    return {"id": f"question-english-content-d-iv-1-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-content-d-iv-1"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies integrated-information and inference patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; multi-source scenarios, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-d-iv-1", "examPatternRefs": refs, "solutionStrategy": "Extract exact facts from every source, align their time, place, number, and rule relationships, then choose the smallest conclusion supported by all of them.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-d-iv-1-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
