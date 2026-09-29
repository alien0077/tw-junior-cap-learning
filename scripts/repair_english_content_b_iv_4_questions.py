import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "needs, wants, feelings, and functional English context"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short conversations, emotion, intention, and response"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English personal expression, situation, and application"),
]

DATA = [
    ("expressing need", "Your hands are full of books and the door is closed. Which sentence clearly expresses what you need?", ["I need someone to open the door, please.", "I feel the door is a sandwich.", "I want yesterday to be a hand.", "I am needing books the color."], "I need someone to open the door, please.", "I need states a necessary condition, and the rest of the sentence identifies the requested help. The polite please makes the request suitable."),
    ("expressing want", "Which sentence tells a friend what you would like to do this weekend?", ["I would like to visit the art market.", "I must have visited it yesterday.", "I am the market's weather.", "I want to visited tomorrowing."], "I would like to visit the art market.", "I would like to + base verb politely expresses a desire or plan. The other choices misuse tense or do not state an activity."),
    ("willingness", "A teammate asks you to help decorate the classroom. You are willing. What is a natural response?", ["Sure, I'd be happy to help.", "No, happiness is a chair.", "I helped the wall next year yesterday.", "Ask the classroom to decorate me."], "Sure, I'd be happy to help.", "I'd be happy to help expresses willingness and a positive feeling toward the request. It directly answers the teammate."),
    ("feeling and reason", "Lena says, 'I am nervous because I have to speak in front of the class.' Why is Lena nervous?", ["She has to speak in front of the class.", "She is going swimming after school.", "She lost a blue pencil last year.", "She wants to sleep during lunch."], "She has to speak in front of the class.", "The conjunction because introduces the reason for Lena's nervousness. The reason is the upcoming public speaking task."),
    ("empathy", "A friend says, 'I am disappointed that our game was canceled.' Which reply shows empathy?", ["I understand. You were looking forward to it.", "Good, then you can forget every friend.", "The game is a type of sandwich.", "You should laugh at your feeling."], "I understand. You were looking forward to it.", "The reply acknowledges the feeling and explains why it makes sense. It does not dismiss or mock the friend's disappointment."),
    ("preference versus need", "A traveler says, 'I need water, but I would like a window seat.' Which statement is correct?", ["Water is necessary; the window seat is a preference.", "The window seat is necessary for survival; water is optional.", "Both statements describe past events.", "Neither statement expresses a choice."], "Water is necessary; the window seat is a preference.", "Need marks something necessary, while would like expresses a desired option. The sentence deliberately contrasts the two levels of importance."),
    ("ability and willingness", "Which reply best answers 'Can you carry this box?' when you are able and willing?", ["Yes, I can. I will help you.", "No, I am a box yesterday.", "I can to carried the weather.", "The box can be a feeling."], "Yes, I can. I will help you.", "Yes, I can expresses ability, and I will help you confirms willingness to act. Together they fully answer the question."),
    ("emotion inference", "Kai is smiling, speaking softly, and says, 'I finally finished the model.' What feeling is most likely?", ["Proud or relieved", "Furious about every success", "Confused about whether he has a model", "Afraid of speaking to anyone forever"], "Proud or relieved", "The completed model and smile support pride or relief. The inference remains cautious because a facial expression alone cannot prove one exact emotion."),
    ("polite refusal", "You want to rest and cannot join a late movie. Which response expresses a polite refusal?", ["Thanks for asking, but I need to rest tonight.", "I want to refuse you because movie is blue.", "Yes, I cannot and I will not say why.", "The movie rested me tomorrow."], "Thanks for asking, but I need to rest tonight.", "Thanks for asking keeps the relationship respectful, but introduces the refusal, and I need to rest gives a clear reason."),
    ("integrated needs and feelings", "Mia says, 'I want to join the hiking trip, but I feel worried because I do not have a rain jacket.' Which reply is most helpful?", ["We can check the weather and lend you one if needed.", "Then you should hide the feeling and go without protection.", "A jacket means the trip must be canceled forever.", "You want a rain jacket, so you cannot want the trip."], "We can check the weather and lend you one if needed.", "The reply recognizes Mia's desire and worry, then offers two practical steps: check the weather and find a jacket. It does not force a false choice between wanting the trip and needing preparation."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use personal situations, needs, wants, feelings, reasons, ability, willingness, and response selection; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the situation and identify the expression skill: {tag}.",
        f"Separate necessary needs, preferences, ability, willingness, feelings, causes, and helpful responses, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by checking whether the wording matches the speaker's intention, grammar, emotional evidence, and social situation.",
        "Say the selected sentence in context, explain what the speaker needs or feels, and show how the wording communicates that meaning clearly and respectfully.",
    ]
    return {
        "id": f"question-english-content-b-iv-4-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-b-iv-4"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; needs, wants, feelings, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-b-iv-4", "examPatternRefs": refs,
        "solutionStrategy": "Classify the speaker's need, preference, ability, willingness, or feeling, identify the evidence and reason, and choose language that expresses or responds to it accurately and respectfully.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-b-iv-4-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
