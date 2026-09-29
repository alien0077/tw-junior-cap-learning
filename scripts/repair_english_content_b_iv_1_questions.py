import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "family, friends, personal information, and contextual English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "people, relationships, routines, and short-text inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "English personal topics, family details, and application"),
]

DATA = [
    ("family relationship", "Read: 'My mother's brother visits us every Sunday. He brings a book for me.' Who is he?", ["My uncle", "My cousin", "My grandfather", "My neighbor"], "My uncle", "Your mother's brother is your uncle. The Sunday visits and book describe what he does, but the family relationship gives the answer."),
    ("possessive relationship", "Read: 'This is Grace's backpack. It has a small star on the front.' Whose backpack is it?", ["Grace's", "The speaker's teacher's", "The star's", "Nobody's"], "Grace's", "The possessive form Grace's shows ownership. The star is a decoration on the backpack, not its owner."),
    ("daily routine", "Read: 'Every weekday, Leo feeds the dog before he leaves for school.' What does Leo do before school?", ["He feeds the dog.", "He visits a museum.", "He buys a new bicycle.", "He sleeps until noon."], "He feeds the dog.", "Every weekday and before he leaves for school describe a repeated routine, and the action is feeds the dog."),
    ("friend trait", "Read: 'When Nina forgot her notes, Amy shared hers and explained the difficult part again.' What kind of friend is Amy?", ["Helpful", "Careless", "Unfriendly", "Impatient"], "Helpful", "Sharing notes and explaining a difficult part are actions that support Nina. They provide evidence that Amy is helpful."),
    ("introduction", "Which introduction gives the clearest information about a family member?", ["This is my cousin Evan. He enjoys drawing and lives near our school.", "This is cousin. He is thing.", "My family is yesterday near.", "Evan, cousin, drawing, school, maybe."], "This is my cousin Evan. He enjoys drawing and lives near our school.", "The sentence identifies the relationship and name, then adds interests and location in complete, understandable sentences."),
    ("pronoun reference", "Read: 'Maya lent her brother a blue jacket because he forgot his coat.' Who does he refer to?", ["Maya's brother", "Maya", "The jacket", "The coat"], "Maya's brother", "The masculine pronoun he matches Maya's brother, the person who forgot a coat. It does not refer to an object or to Maya."),
    ("shared preference", "Read: 'Tom likes basketball, while his sister prefers swimming. They both enjoy outdoor activities.' What do Tom and his sister share?", ["They both enjoy outdoor activities.", "They both prefer swimming.", "They both dislike sports.", "They play basketball every morning."], "They both enjoy outdoor activities.", "The final sentence explicitly states their shared interest. Their different favorite sports do not mean they dislike activities."),
    ("family schedule inference", "Read: 'Dad is cooking, Mom is setting the table, and Ben is carrying plates. Their grandparents will arrive at six.' What is the family probably preparing for?", ["A family meal", "A swimming lesson", "A train repair", "A library exam"], "A family meal", "Cooking, setting a table, carrying plates, and grandparents arriving together strongly support a family meal."),
    ("friendship action", "A friend says, 'I cannot finish this project alone.' Which reply best shows cooperation?", ["Let's divide the tasks and work together.", "That is not my problem; leave now.", "I will hide your materials.", "Projects should never be finished."], "Let's divide the tasks and work together.", "Dividing tasks and working together directly addresses the friend's need and demonstrates cooperative friendship."),
    ("integrated family text", "Read: 'On Saturday, Mei and her two friends visited her grandmother. They repaired a loose shelf, listened to her stories, and left a note with their next visit date.' Which statement is best supported?", ["The visitors helped her grandmother and planned to return.", "Mei visited alone and refused to help.", "The shelf was new and needed no repair.", "They forgot where the grandmother lived."], "The visitors helped her grandmother and planned to return.", "Repairing the shelf shows help, listening shows attention, and the note with a next date shows a plan to return. The other choices contradict the text."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use personal information, family and friend relationships, routines, pronoun reference, and short contextual inference; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the personal-context sentence and identify the skill: {tag}.",
        f"Mark relationship words, possessives, pronouns, routines, actions, and shared details, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by matching grammar and relationship evidence, and by distinguishing what the passage states from what it merely could mean.",
        "Restate the relationship or action in a complete sentence, cite the exact clue, and explain why the selected answer fits the people and situation.",
    ]
    return {
        "id": f"question-english-content-b-iv-1-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-b-iv-1"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; family contexts, relationships, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-b-iv-1", "examPatternRefs": refs,
        "solutionStrategy": "Identify people and relationships first, then use possessives, pronouns, routines, and actions as evidence; answer only what the personal text supports.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-b-iv-1-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
