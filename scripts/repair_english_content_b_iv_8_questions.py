import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "dialogue, opinion, and contextual response"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short exchanges, functional language, and inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "conversation, information integration, and situation-based application"),
]

DATA = [
    ("state an opinion", "Guided discussion: The class is choosing a way to reduce paper waste. Which opening clearly states an opinion?", ["I think we should use both sides of each worksheet.", "Paper waste is a blue yesterday.", "I am an opinion at three o'clock.", "Nobody may discuss the question."], "I think we should use both sides of each worksheet.", "I think signals an opinion, and the rest gives a concrete proposal related to paper waste."),
    ("support with evidence", "Guided discussion: A student says, 'The recycling box helps.' Which reply adds useful evidence?", ["Our class filled it twice this week, so it kept many bottles out of the trash.", "Evidence is a sandwich with no door.", "You are wrong because I feel sleepy.", "The box should sing a song."], "Our class filled it twice this week, so it kept many bottles out of the trash.", "The reply gives an observable classroom fact and connects it to the claim instead of merely repeating an opinion."),
    ("ask for clarification", "Guided discussion: A partner says, 'We should improve the school garden.' Which question asks for clarification?", ["What change would you like us to make first?", "Why is the garden a pencil?", "I improve the garden yesterday.", "Do not explain your idea."], "What change would you like us to make first?", "The question asks the speaker to specify the first action, making the broad idea easier to discuss."),
    ("agree with a reason", "Guided discussion: A classmate suggests adding a quiet reading corner. Which response agrees and gives a reason?", ["I agree because some students need a calm place to read.", "I agree because the corner ate lunch.", "No one can give a reason.", "Reading corners are tomorrow."], "I agree because some students need a calm place to read.", "I agree states agreement and because introduces a relevant reason connected to students' needs."),
    ("qualified disagreement", "Guided discussion: Someone wants a class trip on Friday, but you know several students have exams. Which response is constructive?", ["I understand the idea, but could we choose a day after the exams?", "Your idea is foolish, so stop talking.", "Friday is a door and exams are clouds.", "I disagree and will not suggest anything."], "I understand the idea, but could we choose a day after the exams?", "The response acknowledges the proposal, gives a practical concern, and offers an alternative instead of attacking the speaker."),
    ("negotiate a task", "Guided discussion: Four students must prepare a presentation. Which line moves the group toward fair work?", ["Let's list the jobs and choose one each before we begin.", "One person should do everything without asking.", "The presentation can finish itself.", "I will hide the task list."], "Let's list the jobs and choose one each before we begin.", "Listing jobs before choosing them makes responsibilities visible and supports a fair division of work."),
    ("summarize consensus", "Guided discussion: Three classmates agree to plant herbs, use a small budget, and check them weekly. Which sentence summarizes their agreement?", ["So we will plant herbs, stay within the budget, and check them every week.", "You all discussed a purple bicycle.", "Nobody reached any idea at all.", "The herbs will check the students."], "So we will plant herbs, stay within the budget, and check them every week.", "So introduces a summary that preserves all three agreed actions without adding a new claim."),
    ("manage discussion time", "Guided discussion: The group has two minutes left and still needs a decision. What should the chair say?", ["We have two minutes left; let's hear one final suggestion and then vote.", "We have time forever, so no one needs to listen.", "The clock should make the decision alone.", "Stop speaking and leave the room."], "We have two minutes left; let's hear one final suggestion and then vote.", "The chair states the time limit, allows a final contribution, and names a fair decision procedure."),
    ("invite a quiet speaker", "Guided discussion: One student has not spoken. Which chairperson response encourages participation respectfully?", ["Mia, would you like to add an idea, or would you prefer to pass?", "Mia must speak now or lose her seat.", "Only loud voices matter.", "I will answer for Mia without asking."], "Mia, would you like to add an idea, or would you prefer to pass?", "The invitation gives the student a choice and respects the possibility that she may pass."),
    ("integrate discussion", "Guided discussion: The team wants a safer bike area. Members mention a map, a student survey, and a meeting with the principal. Which conclusion connects the evidence and next step?", ["The map and survey show where the risk is, so we will bring both to the principal and request a safer route.", "Maps and surveys are unrelated, so we should forget the issue.", "The principal is a bike, and the route can answer itself.", "We collected information but will not use it."], "The map and survey show where the risk is, so we will bring both to the principal and request a safer route.", "The conclusion uses the two information sources to support a specific next step and keeps the group's safety goal visible."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url,
        "title": f"{title}; pattern-only study, no original item or option copied.",
        "year": "113-114",
        "subject": "english",
        "locator": locator,
        "observedPattern": "Public-school English assessments use short exchanges, opinions, reasons, information integration, and contextual response selection; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "paper",
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the discussion prompt and identify the conversational goal: {tag}.",
        f"Separate the speaker's claim, reason, evidence, question, or next action, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by checking relevance, grammar, respect for other speakers, evidence, and whether the line helps the group move forward.",
        "Say the selected line aloud, explain how it responds to the previous speaker, and propose one follow-up question or action for the discussion.",
    ]
    return {
        "id": f"question-english-content-b-iv-8-{index}",
        "subject": "english",
        "type": "single-choice",
        "prompt": prompt,
        "options": options,
        "knowledgeIds": ["kg-english-content-b-iv-8"],
        "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCES[0][0],
            "sourceLocator": "Public-school English assessment materials; this item studies guided discussion and functional communication patterns only and does not reproduce an original question, option, image, or answer.",
            "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; discussion situations, roles, options, explanation, and transfer task are original; pending second-round AI/Terra content review.",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-09",
        "lessonId": "lesson-english-content-b-iv-8",
        "examPatternRefs": refs,
        "solutionStrategy": "Identify the discussion move required, then choose a relevant and respectful sentence that states an idea, supports it, clarifies it, negotiates it, summarizes it, or turns it into a fair next action.",
        "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-b-iv-8-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
