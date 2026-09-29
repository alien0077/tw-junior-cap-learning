import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "daily conversation, functional English, and contextual response"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short exchanges, social language, and meaning in context"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional phrases, conversation turns, and application"),
]

DATA = [
    ("greeting", "It is 8:00 a.m. and you meet your teacher at school. Which greeting is most suitable?", ["Good morning, Mr. Lee.", "Good night, Mr. Lee.", "See you yesterday, Mr. Lee.", "I am sorry for the sandwich, Mr. Lee."], "Good morning, Mr. Lee.", "Good morning is a suitable greeting for the morning. Good night is normally used when saying goodbye before sleep, not as a morning greeting."),
    ("thanks and response", "A classmate gives you a useful note. Which response is the most natural?", ["Thanks a lot. / You're welcome.", "I disagree. / Good night.", "Be careful. / I'm late.", "Where is it? / See you last week."], "Thanks a lot. / You're welcome.", "Thanks a lot expresses gratitude, and You're welcome is a natural response when the other person thanks you."),
    ("apology", "You accidentally step on a friend's foot. What should you say first?", ["I'm sorry. Are you okay?", "Congratulations on your foot.", "Would you like some homework?", "Good morning, see you yesterday."], "I'm sorry. Are you okay?", "An apology acknowledges the mistake, and asking if the friend is okay shows concern. The other replies do not fit the accident."),
    ("invitation", "Which sentence is a clear invitation to watch a movie together?", ["Would you like to watch a movie with me?", "I watched the movie last year.", "Please close the movie.", "The movie is under the chair."], "Would you like to watch a movie with me?", "Would you like to ...? can invite someone politely. The other sentences give information or use movie in an unnatural action or location."),
    ("accepting an invitation", "Your friend asks, 'Would you like to join our study group?' You want to join. What should you say?", ["Sure. What time should I come?", "No, I am a pencil.", "I joined it tomorrow.", "Please apologize to the table."], "Sure. What time should I come?", "Sure accepts the invitation, and asking the time moves the plan forward. The response should match both the invitation and the speaker's intention."),
    ("expressing preference", "Which reply best answers 'Which drink do you prefer?' when you like tea more than coffee?", ["I prefer tea.", "I am twelve years old.", "It is next to the door.", "Yes, I did yesterday."], "I prefer tea.", "Prefer means like one choice better than another. I prefer tea directly states the requested preference."),
    ("ability", "Which sentence says that a student can swim?", ["I can swim.", "I must swim yesterday.", "I am swimming a pencil.", "I can to swimmed."], "I can swim.", "Can is followed by the base verb, so I can swim expresses ability correctly. The other choices have meaning or form problems."),
    ("making a plan", "Your friend asks, 'What are you doing after school?' You plan to visit the library. Which answer fits?", ["I'm going to the library.", "I went there next week.", "The library can apologize.", "Yes, I am a library."], "I'm going to the library.", "I'm going to ... states a planned near-future activity. The answer names a sensible destination and matches the question about after-school plans."),
    ("asking for help", "You cannot carry a heavy box alone. Which request is polite and clear?", ["Could you help me carry this box, please?", "Carry my grammar yesterday.", "You are welcome to my heavy.", "Why did the box say hello?"], "Could you help me carry this box, please?", "Could you ... please? makes a polite request, and carry this box identifies exactly what help is needed."),
    ("integrated conversation", "Mia says, 'I'm sorry I forgot your book.' Ben wants to respond kindly and arrange a solution. Which reply works best?", ["That's okay. Could you bring it tomorrow?", "Good night, and congratulations on the weather.", "I prefer your apology to a pencil.", "No, I can yesterday the book."], "That's okay. Could you bring it tomorrow?", "That's okay accepts the apology without escalating the problem, and Could you bring it tomorrow? proposes a clear, polite next step."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short social exchanges, functional phrases, and context-based response selection; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the situation and identify the conversation function: {tag}.",
        f"Determine the speaker's intention and the relationship or time cue, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other choices by checking whether they respond to the same speech act and whether their grammar, time reference, and politeness fit the situation.",
        "Read both turns aloud, confirm that the exchange could continue naturally, and explain which words make the selected response appropriate.",
    ]
    return {
        "id": f"question-english-content-ac-iv-3-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ac-iv-3"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; conversation situations, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ac-iv-3", "examPatternRefs": refs,
        "solutionStrategy": "Name the speech act first—greeting, thanks, apology, invitation, preference, ability, plan, or request—then select the response that matches the situation, grammar, time, and social tone.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ac-iv-3-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
