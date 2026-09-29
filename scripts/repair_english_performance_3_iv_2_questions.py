import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "classroom vocabulary, instructions, and contextual meaning"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "school words, sentence clues, and functional reading"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "classroom actions, vocabulary use, and application"),
]

DATA = [
    ("instruction verb", "The teacher says, 'Please underline the sentence that gives the reason.' What should students do?", ["Draw a line under the relevant sentence.", "Erase the entire page.", "Read only the title aloud.", "Close the book without marking it."], "A", "Underline means draw a line beneath the selected words or sentence."),
    ("classroom object", "Which object would a student most likely use to erase a pencil answer?", ["An eraser", "A ruler", "A stapler", "A projector"], "A", "An eraser removes pencil marks."),
    ("group action", "A worksheet says, 'Work in pairs and compare your answers.' What does 'in pairs' mean?", ["Work with one other classmate.", "Work alone with two books.", "Work with the entire school.", "Work only after the class ends."], "A", "A pair consists of two people, so each student works with one partner."),
    ("context clue", "The sentence says, 'Please hand in your report before Friday.' What does 'hand in' mean here?", ["Submit the report to the teacher or required place.", "Hold the report above your head forever.", "Draw a hand on the report.", "Take the report home and hide it."], "A", "In a classroom, hand in means submit work."),
    ("location word", "The pencil case is beside the notebook. Where is it?", ["Next to the notebook", "Inside the notebook", "Far below the desk", "Behind the classroom door"], "A", "Beside means next to or at the side of something."),
    ("schedule word", "The bell rings at the end of the period. When should students usually prepare to leave?", ["When the class period finishes", "Before the teacher begins every lesson", "Only during lunch next week", "Whenever the first student arrives"], "A", "End of the period signals that the scheduled class time has finished."),
    ("question word", "A teacher asks, 'What is the main idea of the paragraph?' What kind of answer is needed?", ["The paragraph's central point", "The writer's shoe size", "The classroom's exact temperature", "A list of every punctuation mark"], "A", "Main idea asks for the central point, not an unrelated detail."),
    ("material word", "The experiment instruction says, 'Pour the water into the beaker.' Which item receives the water?", ["The beaker", "The calendar", "The whiteboard", "The backpack zipper"], "A", "Into identifies the container that receives the water."),
    ("polite classroom request", "You cannot hear the last instruction. Which sentence should you use?", ["Could you repeat the last instruction, please?", "Your instruction disappeared, so stop teaching.", "Repeat is a classroom object.", "I heard nothing and will guess every step."], "A", "The question politely asks the teacher to say the instruction again."),
    ("integrated vocabulary", "A student reads 'Open your textbook, circle two key words, and discuss them with a partner.' Which sequence is correct?", ["Open the book, circle two important words, then discuss them with a partner.", "Discuss first, close the book, and erase every word.", "Circle the partner, then open the classroom door.", "Read the instruction only after the work is finished."], "A", "The sequence preserves the three classroom actions and their order."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取課堂字詞、指令與語境辨識能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以課堂指令、物品、位置、時間、動作與功能請求測量基礎字詞在語境中的理解；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the classroom situation and identify the vocabulary target: {topic}.",
        "Underline the surrounding action, object, location, time, or purpose that gives the word its meaning.",
        f"Compare every choice with the sentence and select the meaning that fits the classroom context; the correct answer is {answer}.",
        f"Explain the contextual evidence: {explanation}",
        "Replace the word with the selected meaning and reread the whole instruction to check that the task remains possible and logical.",
    ]
    return {"id": f"question-english-performance-3-iv-2-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-2"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies classroom vocabulary and contextual-meaning patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; classroom contexts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-2", "examPatternRefs": refs, "solutionStrategy": "Use the surrounding classroom action and object as evidence, identify the word's function in the sentence, and select the meaning that makes the entire instruction coherent.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-2-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
