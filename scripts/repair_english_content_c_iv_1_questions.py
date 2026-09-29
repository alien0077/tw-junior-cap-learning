import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "festivals, notices, dates, and contextual reading"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short cultural texts, schedules, and detail inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional English, comparison, and audience-aware response"),
]

DATA = [
    ("festival purpose", "Read the notice: 'The Lantern Walk begins at 6:30 p.m. Families carry handmade lanterns and share wishes for the new year.' What is the main purpose of the event?", ["To welcome the new year through a community activity.", "To teach families how to repair cars.", "To choose the fastest runner.", "To close every shop for a month."], "A", "The notice connects lanterns, families, and new-year wishes, so welcoming the new year through a shared activity is the best purpose."),
    ("date and time", "A school poster says: 'International Food Day is Friday, October 18. The tasting booths open at noon and close at 2 p.m.' When can students taste the food?", ["Before school on Thursday", "From noon to 2 p.m. on Friday", "At 6:30 p.m. on October 18", "All day on Saturday"], "B", "The date and the booth hours are stated directly: students can visit from noon to 2 p.m. on Friday, October 18."),
    ("festival detail", "A short text explains that people in one town hang colorful flags, play drums, and thank farmers after the harvest. Which detail belongs to the celebration?", ["Thanking farmers after the harvest", "Holding a winter exam", "Repairing a school bus", "Buying a train ticket"], "A", "Thanking farmers after the harvest is the cultural detail stated in the text; the other choices belong to unrelated situations."),
    ("schedule inference", "A festival program lists: 10:00 craft workshop, 12:00 lunch, 2:00 dance show. A visitor arrives at 1:30. What can the visitor attend next?", ["The craft workshop", "Lunch only at 12:00", "The dance show at 2:00", "A midnight parade"], "C", "The visitor misses the earlier activities but can still attend the dance show beginning at 2:00."),
    ("invitation response", "Your exchange partner invites you to a school celebration, but you have a family appointment. Which reply is polite and clear?", ["Thanks for inviting me, but I cannot come that day.", "Festivals are a blue pencil.", "I came tomorrow because no.", "You must cancel your celebration."], "A", "The reply thanks the inviter, gives a clear refusal, and avoids blaming the celebration."),
    ("cultural practice", "A text says that people decorate doors with red paper during a spring celebration. What can a reader safely infer?", ["The decoration is one practice associated with that celebration.", "Every person in every country must use red paper.", "The celebration lasts exactly one hour.", "Red paper is the only food served."], "A", "The text supports only that decorating doors with red paper is a practice connected with the celebration, not the wider claims."),
    ("comparison", "Festival A has a family parade in Taiwan. Festival B has a community parade in another country. What is a supported similarity?", ["Both include a parade involving the community.", "Both always happen on the same date.", "Both use exactly the same music.", "Neither allows families to attend."], "A", "The shared feature given in the two descriptions is a community parade; the other details are not supported."),
    ("appropriate behavior", "During a cultural ceremony, a visitor is unsure whether photography is allowed. What should the visitor do first?", ["Ask the organizer or follow the posted rule before taking photos.", "Photograph people closely without asking.", "Mock the ceremony loudly.", "Change the ceremony's schedule."], "A", "Checking the organizer or notice respects the participants and avoids assuming that photography is permitted."),
    ("audience and message", "A bilingual festival card says, 'Please bring a reusable cup. The event aims to reduce trash.' Who is the message mainly for?", ["People attending the festival", "Only astronauts", "People who never enter the event", "A repair shop's mechanics"], "A", "The request to bring a cup is an instruction for festival attendees and supports the event's environmental goal."),
    ("integrated cultural reading", "A travel note says: 'On Saturday morning, Mei will visit a temple fair, observe the opening ceremony, and join a paper-cutting workshop. She will not touch displays without permission.' Which summary is best?", ["Mei will attend a cultural event, take part respectfully, and follow its schedule.", "Mei will skip the event and change every display.", "Mei will only shop at a supermarket at night.", "Mei will run the ceremony without the organizers."], "A", "The summary includes the event, the scheduled activities, and Mei's respectful behavior without adding unsupported details."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{
        "url": url, "title": f"{title}；僅取節慶與情境閱讀能力方向，未複製原題、選項、圖表或答案。",
        "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "公開英文評量常以公告、行程表、文化短文、邀請與跨文化情境測量日期、主旨、細節、推論及合宜回應；本題為獨立改寫。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper",
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the festival text and identify the task: {topic}.",
        "Circle the dates, times, people, actions, cultural practice, and any explicit rule or purpose.",
        f"Compare each option with the stated evidence; the correct answer is {answer}.",
        f"Use the key evidence to explain the choice: {explanation}",
        "State only what the passage supports, and distinguish a cultural practice or event detail from a claim about every person or every country.",
    ]
    return {
        "id": f"question-english-content-c-iv-1-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-c-iv-1"], "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
            "sourceLocator": "Public-school English assessment materials; this item studies festival and cultural-context reading patterns only and does not reproduce an original question, option, image, or answer.",
            "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; festival contexts, options, explanations, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-c-iv-1", "examPatternRefs": refs,
        "solutionStrategy": "Read the cultural text as evidence: locate time, place, purpose, participants, practices, and rules, then choose the option that is directly supported without overgeneralizing.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-c-iv-1-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
