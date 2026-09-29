import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "grammar patterns, sentence completion, and contextual English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "English grammar, sentence forms, and context-based selection"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "grammar structures, word order, and functional application"),
]

DATA = [
    ("present simple agreement", "Choose the sentence that correctly describes a regular habit.", ["Ken walks to school every day.", "Ken walk to school every day.", "Ken is walk to school every day.", "Ken walking to school every day."], "Ken walks to school every day.", "The time phrase every day describes a habit, so the present simple is needed. With the singular subject Ken, the verb walk takes -s: walks."),
    ("past-time verb", "Yesterday, the children ____ a kite in the park.", ["flew", "fly", "are flying", "will fly"], "flew", "Yesterday signals a completed past action. The past form of fly is flew, not the present fly or a future form."),
    ("be verb and adjective", "The soup ____ too hot to eat now.", ["is", "are", "be", "am"], "is", "Soup is treated as a singular uncountable noun, and the sentence describes its current state, so the correct be verb is is."),
    ("there is and there are", "Which sentence correctly describes two books on the desk?", ["There are two books on the desk.", "There is two books on the desk.", "There be two books on the desk.", "There are a book on the desk."], "There are two books on the desk.", "The noun phrase two books is plural, so the existence pattern requires There are. The article and verb in the other choices do not agree with the quantity."),
    ("question word order", "Which question correctly asks about the time of the train?", ["What time does the train leave?", "What time the train does leave?", "What time do the train leaves?", "What time is the train leave?"], "What time does the train leave?", "A present-simple wh-question uses wh-word plus does, subject, and base verb: What time does the train leave?"),
    ("comparative", "The blue backpack is ____ than the black one, so it can hold more books.", ["larger", "large", "largest", "more large"], "larger", "The sentence compares two backpacks, so a comparative form is needed. Large usually becomes larger, not more large."),
    ("modal plus base verb", "You ____ wear a helmet when riding this bike; it is a safety rule.", ["must", "must to", "must wearing", "must wore"], "must", "A modal such as must is followed directly by the base verb: must wear. It expresses a strong rule in this context."),
    ("conjunction contrast", "Lina wanted to go hiking, ____ it started raining heavily.", ["but", "because", "so that", "and then why"], "but", "The second clause contrasts with Lina's plan, so but connects the two ideas. Because would give a cause rather than a contrast."),
    ("infinitive purpose", "Tom went to the library ____ a quiet place to study.", ["to find", "finding", "found", "for found"], "to find", "To find introduces the purpose of going to the library. The verb after to stays in the base form."),
    ("integrated sentence choice", "The sign says the pool is closed because workers are cleaning it. Which sentence reports the information correctly?", ["The pool is closed, so visitors cannot swim there now.", "The pool closed because visitors are swimming tomorrow.", "The pool is cleaning the workers now.", "Visitors must swam in the closed pool."], "The pool is closed, so visitors cannot swim there now.", "The first sentence preserves the cause-and-result relationship and uses the present forms correctly. The other choices reverse roles, misuse tense, or contradict the notice."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use sentence completion, word order, tense, agreement, and context-based grammar application; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the sentence and identify the grammar focus: {tag}.",
        f"Mark the subject, time cue, clause relationship, or purpose phrase, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by checking tense, subject-verb agreement, word order, auxiliary selection, and whether the completed sentence matches the meaning.",
        "Reread the full sentence aloud, explain why the selected form fits both grammar and context, and state what change would be needed in a different time or subject situation.",
    ]
    return {
        "id": f"question-english-content-ad-iv-1-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ad-iv-1"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; grammar contexts, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ad-iv-1", "examPatternRefs": refs,
        "solutionStrategy": "Identify the sentence's time, subject, relationship, and purpose before choosing a form; then check agreement, auxiliary order, verb form, and whole-sentence meaning.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ad-iv-1-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
