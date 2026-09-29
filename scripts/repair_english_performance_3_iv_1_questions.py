import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "letter recognition, spelling, and reading information"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "alphabet forms, word identification, and context clues"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "spelling details, visual discrimination, and application"),
]

DATA = [
    ("lowercase identification", "A handwritten note shows a tall loop followed by a short round stroke: 'l'. Which printed letter should it be read as?", ["l", "t", "e", "i"], "A", "The note's tall loop and single straight stem are intended as lowercase l."),
    ("uppercase identification", "The first letter of a handwritten sentence has two slanting strokes joined by a middle bar. Which capital letter is it?", ["A", "H", "M", "N"], "A", "Two slanting strokes and a middle bar form capital A."),
    ("confusable pair", "A learner reads a handwritten word as 'cat,' but the final letter has a tall rising stroke and a loop. Which correction is most likely?", ["It may be 'can' if the final letter is n, so check the last stroke.", "It must be 'cap' because every loop is p.", "The word cannot contain a final letter.", "The rising stroke proves it is the number 7."], "A", "The final handwritten form must be checked against the letter's characteristic strokes; n is a plausible correction, not an automatic guess."),
    ("word context", "The card shows a handwritten form that could be 'ship' or 'shop.' The sentence is 'Please ___ the box to Room 2.' Which reading fits?", ["ship", "shop", "sharp", "sheep"], "A", "The verb ship means send an item, which fits the instruction about the box."),
    ("letter order", "Which option correctly spells 'green' when the handwritten letters are g-r-e-e-n?", ["green", "geren", "grean", "gerren"], "A", "The letters appear in the order g, r, e, e, n."),
    ("case and meaning", "A label begins with a large handwritten 'P' and then 'ark.' What word is most likely intended?", ["Park", "parked", "Pork", "Bark"], "A", "A capital P followed by ark forms Park, a likely place name on a label."),
    ("readability repair", "A classmate's handwritten 'u' looks like 'v.' What is the best way to check before copying it?", ["Compare the surrounding word and the writer's other examples of u and v.", "Choose the letter with the longer name.", "Copy both letters into every word.", "Ignore the word's meaning completely."], "A", "Context plus the writer's repeated letter forms provides evidence for a difficult handwritten character."),
    ("alphabetical order", "A worksheet lists handwritten words 'blue,' 'apple,' and 'chair.' Which alphabetical order is correct?", ["apple, blue, chair", "blue, chair, apple", "chair, apple, blue", "apple, chair, blue"], "A", "Compare the first letters a, b, and c to place the words alphabetically."),
    ("address detail", "A handwritten envelope appears to say '15 Lake Rd.' Which detail must be checked most carefully before delivery?", ["Whether the first number is 15 and the street name is Lake", "Whether the envelope is the favorite color of the sender", "Whether every road in town has the same number", "Whether the word Rd. is a person's name"], "A", "An address depends on exact number and street-name recognition, so ambiguous strokes must be verified."),
    ("integrated recognition", "A student reads a handwritten message, checks a repeated capital G in the signature, and uses the sentence meaning to confirm one unclear word. Why is this reliable?", ["It combines letter-shape evidence, a repeated sample, and context.", "It chooses the longest word without reading the sentence.", "It treats every unclear stroke as a different alphabet.", "It copies the first guess without checking."], "A", "Several independent clues reduce the chance of misreading a handwritten letter or word."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取字母辨識、拼字與閱讀細節能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以字母、拼字、語境與細節辨識測量學生從文字形式建立正確讀寫判斷；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the handwriting task and identify the recognition focus: {topic}.",
        "Mark the visible stroke, letter position, capitalization, nearby letters, or sentence context that supplies evidence.",
        f"Compare each option with all available clues and select the form that can be read and used accurately; the correct answer is {answer}.",
        f"Explain the visual and language evidence: {explanation}",
        "Check the word or message again as a whole, and state what additional sample would resolve the ambiguity if the strokes remained unclear.",
    ]
    return {"id": f"question-english-performance-3-iv-1-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-1"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies letter-form recognition and spelling-pattern abilities only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; letter descriptions, contexts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-1", "examPatternRefs": refs, "solutionStrategy": "Separate the visual stroke evidence from guesses, compare a doubtful letter with nearby forms and context, then verify the complete word before accepting the reading.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-1-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
