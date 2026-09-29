import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "classroom language, instructions, and practical English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short classroom exchanges and context-based response"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional English, classroom directions, and application"),
]

DATA = [
    ("requesting permission", "A student asks, 'May I borrow a pencil?' Which response gives permission?", ["Sure. Here you are.", "No, the pencil is a color.", "Turn to page ten.", "Please close the window."], "Sure. Here you are.", "May I ...? asks for permission. Sure. Here you are grants permission and supplies the requested object."),
    ("page instruction", "The teacher says, 'Open your books to page 24.' What should students do?", ["Find page 24 and open the books there.", "Close every book and leave the room.", "Write the number 24 on the door.", "Ask the teacher to erase the board."], "Find page 24 and open the books there.", "Open your books to a page tells students to use their books and move to the specified page number."),
    ("pair work", "What should students do when the teacher says, 'Work with a partner'?", ["Complete the activity with one classmate.", "Work alone without speaking to anyone.", "Change classrooms immediately.", "Put every worksheet in the trash."], "Complete the activity with one classmate.", "A partner is one person who works with you. The instruction therefore asks for two-person cooperation, not individual work."),
    ("listening instruction", "Which action follows 'Listen and repeat'?", ["Hear the model and say the same words afterward.", "Read a new paragraph silently and skip the model.", "Write a question but do not hear the speaker.", "Leave the classroom before the sentence ends."], "Hear the model and say the same words afterward.", "Listen identifies the first action and repeat means say the model again. The order matters: hear first, then produce the words."),
    ("clarification request", "A student does not understand the task. Which classroom sentence is the most appropriate?", ["Could you explain it again, please?", "I am a window, please.", "Put your homework on my desk.", "The answer is under the chair."], "Could you explain it again, please?", "The sentence politely asks the teacher to clarify or repeat an explanation. Its meaning matches the student's difficulty."),
    ("turn-in instruction", "The teacher says, 'Hand in your worksheets before you leave.' What must students do?", ["Give the completed worksheets to the teacher or collection place first.", "Take the worksheets home without showing anyone.", "Draw a hand on the worksheet and keep it.", "Leave before completing the work."], "Give the completed worksheets to the teacher or collection place first.", "Hand in means submit or give work to the teacher or designated collection place. Before you leave sets the time condition."),
    ("participation phrase", "A student wants to answer during a discussion. Which action is most appropriate?", ["Raise a hand and wait to be called on.", "Shout over every classmate immediately.", "Turn off the classroom clock.", "Hide the answer under the desk."], "Raise a hand and wait to be called on.", "In a classroom discussion, raising a hand signals a wish to speak while waiting respects the turn-taking routine."),
    ("spelling request", "The teacher asks, 'How do you spell 'library'?' Which answer is a suitable response?", ["L-I-B-R-A-R-Y.", "It is next to the park.", "Please open the window.", "At three o'clock."], "L-I-B-R-A-R-Y.", "How do you spell ...? asks for the letters in a word. The letter-by-letter response answers that exact question."),
    ("quiet-work instruction", "What should a student do after hearing 'Please work quietly for five minutes'?", ["Work with little or no unnecessary talking during that time.", "Talk louder for five minutes.", "Finish by leaving the school.", "Refuse to look at the assignment."], "Work with little or no unnecessary talking during that time.", "Work quietly describes the expected manner, and for five minutes gives the duration. Please makes it polite but still communicates the classroom expectation."),
    ("integrated classroom exchange", "The teacher says, 'Compare your answers with your group, circle one difference, and be ready to share.' Which plan follows all three directions?", ["Discuss answers with the group, circle one difference, and prepare to report it.", "Work alone, erase every difference, and leave the room.", "Circle every answer without comparing and remain silent.", "Share a random story before looking at the answers."], "Discuss answers with the group, circle one difference, and prepare to report it.", "The instruction has three linked actions: compare with the group, mark one difference, and prepare to share. The correct plan preserves their order and purpose."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use short functional exchanges, instructions, and context-based response selection; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the classroom exchange and identify its function: {tag}.",
        f"Underline the action, object, time, or response requested, then apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by matching every part of the instruction, including the speaker's purpose and any order, time, or participation condition.",
        "Act out or reread the exchange, state what the student should say or do, and point to the words that prove the response is appropriate.",
    ]
    return {
        "id": f"question-english-content-ac-iv-2-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ac-iv-2"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; classroom contexts, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ac-iv-2", "examPatternRefs": refs,
        "solutionStrategy": "Identify who is speaking, what action or response is requested, and any timing or politeness cue; then choose the reply or behavior that satisfies every part of the classroom exchange.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ac-iv-2-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
