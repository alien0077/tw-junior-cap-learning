import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "daily communication, functional phrases, and contextual English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short conversations, time, directions, and response selection"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "everyday English vocabulary, sentence patterns, and application"),
]

DATA = [
    ("asking directions", "You are lost near the station. Which question politely asks for the library's location?", ["Could you tell me how to get to the library?", "Do you enjoy reading the library?", "How many books is the library?", "Please library me yesterday."], "Could you tell me how to get to the library?", "Could you tell me how to get to ...? is a polite way to request directions. It asks about the route rather than the number of books or a personal preference."),
    ("making an appointment", "Which sentence best suggests a meeting time after school?", ["How about meeting at four?", "How many meetings are four?", "Meetings were under four yesterday.", "Four is meeting a pencil."], "How about meeting at four?", "How about + -ing suggests a plan or time. The phrase at four supplies a possible meeting time."),
    ("telephone opening", "You call a friend's home and her brother answers. Which opening is most appropriate?", ["Hello, may I speak to Emma, please?", "Give Emma the phone yesterday.", "I am the telephone's homework.", "Where is your birthday?"], "Hello, may I speak to Emma, please?", "A polite phone opening greets the person and asks to speak with the intended caller. The other sentences are unclear or unrelated."),
    ("weather plan", "The forecast says there will be heavy rain all afternoon. Which suggestion fits the information?", ["Let's visit the indoor museum instead.", "Let's have a picnic in the heaviest rain.", "Let's leave all umbrellas at home and swim on the road.", "The forecast means the sun will be very strong."], "Let's visit the indoor museum instead.", "Heavy rain makes an indoor activity a sensible alternative. The other options ignore or contradict the forecast and safety needs."),
    ("polite request", "Your classmate is using the only dictionary. Which request is most appropriate?", ["Could I use it when you finish, please?", "Give it now because I am dictionary.", "Why did the book eat lunch?", "You must borrow my yesterday."], "Could I use it when you finish, please?", "Could I ...? please requests permission politely and when you finish respects the classmate's current use of the dictionary."),
    ("agreement", "Your friend says, 'This route is safer.' You agree. Which response fits?", ["I agree. Let's take it.", "I agree yesterday was a sandwich.", "No, the route is a color.", "Please ask the weather to sit."], "I agree. Let's take it.", "I agree shows the same opinion, and Let's take it turns that agreement into a plan. The response remains connected to the route."),
    ("problem solution", "A visitor says, 'I cannot open this map on my phone.' Which reply offers useful help?", ["Let me show you how to download it.", "The map is delicious at noon.", "You should close your shoes.", "I cannot help because the phone is blue."], "Let me show you how to download it.", "Let me ... offers immediate assistance, and the proposed action addresses the problem of accessing the map."),
    ("time expression", "A sign says 'The clinic opens at 9:00 and closes at 5:00.' When can a visitor normally make an appointment there?", ["Between 9:00 a.m. and 5:00 p.m.", "Only at midnight.", "Before the clinic opens at 8:00.", "After it closes at 6:00."], "Between 9:00 a.m. and 5:00 p.m.", "The opening and closing times define the normal service period. The answer must fall between 9:00 and 5:00, not before opening or after closing."),
    ("clarifying meaning", "Someone says, 'The meeting is next Friday.' You are unsure which date that means. What should you ask?", ["Could you tell me the exact date, please?", "Can Friday tell me the meeting?", "Why is the date a chair?", "I know every date in the world."], "Could you tell me the exact date, please?", "The polite clarification question asks for the missing information directly: the calendar date of next Friday."),
    ("integrated conversation", "A friend says, 'The bus is late, and we will miss the movie.' Which reply is most useful?", ["Let's check the next bus or call a taxi, then tell the theater we may be late.", "The movie is a color, so do nothing.", "We should arrive yesterday without transport.", "The bus is late because the theater is a sandwich."], "Let's check the next bus or call a taxi, then tell the theater we may be late.", "The reply acknowledges the transport problem, proposes two realistic alternatives, and communicates with the theater. It turns daily language into a workable plan."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use daily communication, directions, time, telephone exchanges, requests, plans, and context-based response; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the daily situation and identify the communication function: {tag}.",
        f"Mark the purpose, key time or place, social relationship, and practical problem, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other choices by checking grammar, politeness, time, relevance, and whether the response actually advances the conversation.",
        "Read both turns aloud, explain what the speaker needs, and show how the selected phrase responds naturally and usefully.",
    ]
    return {
        "id": f"question-english-content-b-iv-2-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-b-iv-2"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; daily situations, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-b-iv-2", "examPatternRefs": refs,
        "solutionStrategy": "Identify the speaker's immediate communication goal, then choose language that is grammatically correct, socially appropriate, relevant to the details, and capable of moving the situation forward.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-b-iv-2-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
