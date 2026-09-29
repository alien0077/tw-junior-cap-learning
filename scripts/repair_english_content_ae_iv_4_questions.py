import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "cards, letters, emails, and functional English reading"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short messages, email details, and contextual response"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English correspondence, purpose, tone, and application"),
]

DATA = [
    ("message purpose", "Read the card: 'Happy birthday, Ella! I hope your day is full of music and laughter. — Ben' Why did Ben write it?", ["To wish Ella a happy birthday.", "To ask Ella to return a library book.", "To announce a train delay.", "To describe a science experiment."], "To wish Ella a happy birthday.", "The greeting Happy birthday and the good wishes show that the card celebrates Ella's birthday. The other purposes are unrelated to the message."),
    ("email subject", "Which subject line best matches an email asking a teacher about tomorrow's homework?", ["Question About Tomorrow's Homework", "My Favorite Animal", "Welcome to the Airport", "A Recipe for Soup"], "Question About Tomorrow's Homework", "An email subject should summarize its purpose. This subject clearly tells the teacher that the message contains a homework question."),
    ("salutation", "Which opening is most appropriate for a polite email to a teacher named Ms. Chen?", ["Dear Ms. Chen,", "Hey you,", "Goodbye Ms. Chen,", "Dear homework, please"], "Dear Ms. Chen,", "Dear plus the teacher's title and name is a polite written salutation. It belongs at the beginning, before the message body."),
    ("sign-off", "Which closing best completes a polite email to a school office?", ["Sincerely, / Alex Lin", "See you yesterday, / Alex Lin", "Open the door, / Alex Lin", "No name needed, / Alex Lin"], "Sincerely, / Alex Lin", "Sincerely is a conventional polite sign-off, and the writer's name identifies who sent the email."),
    ("detail location", "Read the note: 'Hi Jo, The art club meets in Room 305 at 4:10 on Thursday. Please bring colored paper. — May' Where does the club meet?", ["Room 305", "Room 410", "The cafeteria", "May's house"], "Room 305", "The phrase meets in Room 305 gives the location. The other numbers and places are not stated as the meeting room."),
    ("time detail", "According to the same note, when does the art club meet?", ["At 4:10 on Thursday", "At 3:05 on Friday", "At 4:10 on Tuesday", "Every morning at 8:00"], "At 4:10 on Thursday", "The note gives both the time, 4:10, and the day, Thursday. A complete answer should preserve both details."),
    ("appropriate reply", "Email: 'Could you send me the photos from the field trip?' Which reply is most useful?", ["Sure. I will send them tonight.", "The field trip is a pencil.", "No, photos are yesterday.", "Please close the email's window."], "Sure. I will send them tonight.", "The reply accepts the request and gives a clear time for the action. It responds to the requested photos rather than changing the topic."),
    ("formal tone", "Which sentence is most suitable in a formal request to a community center?", ["Could you please tell me whether the room is available?", "Yo, is the room free or what?", "Give room now!!!", "Room, room, room."], "Could you please tell me whether the room is available?", "Could you please ...? is polite and complete for a formal request. The other choices are too casual, aggressive, or incomplete."),
    ("message sequence", "Which order makes the most sense for a short email?", ["Greeting → purpose and details → polite closing → name", "Name → closing → greeting → unrelated story", "Closing → purpose → greeting → name", "Details only → no reader or purpose"], "Greeting → purpose and details → polite closing → name", "A short email normally opens by addressing the reader, gives its purpose and details, and then closes politely with the sender's name."),
    ("integrated correspondence", "A friend writes, 'Thanks for lending me your umbrella. I will return it at school on Monday.' Which response is most appropriate?", ["You're welcome. Monday is fine.", "Happy birthday to the umbrella yesterday.", "Please mail me a train station.", "I cannot return the weather."], "You're welcome. Monday is fine.", "You're welcome responds to thanks, and Monday is fine confirms the proposed return time. The reply should address both the gratitude and the plan."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short messages, letters, emails, purpose, details, sequence, tone, and response selection; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the card, letter, or email and identify the correspondence skill: {tag}.",
        f"Mark the writer, reader, purpose, format, tone, time, place, or requested action, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by matching the exact written details and by checking whether the wording suits the relationship and the position in the message.",
        "Reread the complete correspondence, restate its purpose or response in your own words, and cite the phrase that proves the answer.",
    ]
    return {
        "id": f"question-english-content-ae-iv-4-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ae-iv-4"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; correspondence contexts, details, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ae-iv-4", "examPatternRefs": refs,
        "solutionStrategy": "Identify the message's purpose and audience, then inspect format markers, details, tone, and requested action before choosing the answer that fits both the text and the relationship.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ae-iv-4-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
