import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "genres, topics, structure, and evidence"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "notices, narratives, explanations, and letters"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "text type, purpose, and main-idea reading"),
]

DATA = [
    ("narrative", "A text tells how a child found a lost dog, asked neighbors for help, and reunited it with its owner. What type of text is it mainly?", ["A narrative describing connected events", "A timetable listing train departures", "A recipe with numbered cooking steps", "A dictionary entry defining one word"], "A", "Characters and connected events form a narrative."),
    ("explanation", "An article describes how rain becomes groundwater using causes, processes, and labeled stages. What is its main purpose?", ["To explain a natural process", "To invite readers to a birthday party", "To tell a fictional mystery about a dog", "To sell a pair of shoes"], "A", "Processes and causes show that the article explains how something works."),
    ("notice", "A school notice gives a date, room, required materials, and a contact person for a workshop. What should readers mainly learn?", ["How and when to attend the workshop", "The complete history of the school building", "A character's feelings in a story", "The ingredients for a family dinner"], "A", "A notice organizes practical attendance information."),
    ("letter", "A letter begins with 'Dear Uncle,' describes a trip, and ends with 'Write back soon.' What is the writer's purpose?", ["To share news and invite a reply", "To report a laboratory result to a machine", "To define a word in a dictionary", "To list bus fares without a reader"], "A", "The greeting, personal news, and request for a reply identify a personal letter."),
    ("opinion", "A short article says school gardens are valuable because they teach science and cooperation, then asks schools to create one. What is the writer doing?", ["Presenting an opinion with reasons and a suggestion", "Listing neutral weather measurements only", "Retelling a mystery with no claim", "Giving directions to a train station"], "A", "The claim, reasons, and recommendation form an opinion argument."),
    ("structure", "A text has headings 'Problem,' 'Evidence,' and 'Possible Solution.' What structure does it use?", ["It moves from an issue to support and a response.", "It lists unrelated vocabulary in alphabetical order.", "It tells events backward with no explanation.", "It gives only a greeting and a signature."], "A", "The headings signal a problem-evidence-solution organization."),
    ("genre clue", "A text includes a title, author name, dialogue lines, and stage directions in brackets. What genre is most likely?", ["A play or script", "A weather table", "A personal shopping receipt", "A dictionary definition"], "A", "Dialogue and bracketed stage directions are distinctive script features."),
    ("compare genres", "A recipe and a science explanation both use the word 'first.' How should a reader decide its function?", ["Use the surrounding steps and purpose of each text.", "Assume it always introduces the same kind of action.", "Ignore the sentences after it.", "Choose the text with the larger font."], "A", "The same transition word can organize different genres, so local structure and purpose matter."),
    ("source limitation", "An advertisement says a drink is 'the best choice for everyone.' Which response reads it critically?", ["Identify it as a persuasive claim and look for supporting evidence.", "Treat the word everyone as verified scientific data.", "Assume an advertisement cannot contain opinions.", "Ignore the product and analyze only the font."], "A", "Advertising language may persuade, so the broad claim needs evidence rather than automatic acceptance."),
    ("integrated genre", "A webpage contains a short explanation of recycling, a chart of local collection days, and a notice about where to put boxes. What is the best reading approach?", ["Use the explanation for why, the chart for when, and the notice for what action to take.", "Read every part as a fictional story with one character.", "Use only the chart to understand the recycling process.", "Ignore the notice because different genres cannot work together."], "A", "Each genre contributes a different kind of information to the reader's task."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取不同體裁、主題、結構與目的判讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常結合故事、說明、公告、書信、腳本、廣告與資料圖表測量體裁辨識、主旨、目的與證據整合；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the passage and identify the genre-reading target: {topic}.",
        "Mark the format signals, audience, purpose, headings, sequence, claims, evidence, dialogue, or practical details.",
        f"Compare the choices with the text type and its structure, then select the interpretation supported by the text; the correct answer is {answer}.",
        f"Explain the genre and evidence connection: {explanation}",
        "Reread the relevant feature and state how the answer would change if the text's audience, purpose, or genre changed.",
    ]
    return {"id": f"question-english-performance-3-iv-16-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-16"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies genre, topic, structure, and purpose patterns only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; texts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-16", "examPatternRefs": refs, "solutionStrategy": "Identify the text form and audience, connect format to purpose and structure, then select a main idea or action that fits the genre-specific evidence.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-16-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
