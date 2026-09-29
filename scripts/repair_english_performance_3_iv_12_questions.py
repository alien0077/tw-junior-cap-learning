import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "reading strategies, evidence, and comprehension"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "context clues, skimming, scanning, and main ideas"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "reading purpose, inference, and text evidence"),
]

DATA = [
    ("preview", "Before reading an article titled 'How Bees Help Gardens,' what is a useful first step?", ["Predict the topic from the title and identify what you already know.", "Read the last word only and choose an answer.", "Ignore the title and memorize every punctuation mark.", "Decide the author's personal address before seeing the text."], "A", "The title supports a focused prediction about bees and gardens before detailed reading."),
    ("skimming", "You need the general topic of a long article quickly. Which strategy is most suitable?", ["Skim the title, headings, first sentences, and repeated key words.", "Translate every word before noticing the topic.", "Read only the page number.", "Choose the longest paragraph as the topic automatically."], "A", "Skimming uses prominent structure and repeated ideas to form a quick overall understanding."),
    ("scanning", "A notice contains many details, but you only need the event time. What should you do?", ["Scan for numbers, time expressions, and the event label.", "Read every sentence with equal attention for an hour.", "Guess from the notice's color.", "Look only at the writer's name."], "A", "Scanning targets a specific detail rather than the entire text."),
    ("context clue", "The sentence says, 'The path was slippery, so hikers moved slowly.' What does slippery most likely mean?", ["Easy to slide on", "Full of bright flowers", "Very far from the mountain", "Closed because it is sunny"], "A", "The consequence of moving slowly on the path supports the meaning easy to slide on."),
    ("main idea", "A paragraph explains that reusable bottles reduce plastic waste, save money, and are easy to carry. What is its main idea?", ["Reusable bottles offer several practical and environmental benefits.", "Plastic bottles are always expensive to carry.", "The paragraph is mainly about buying a new backpack.", "Only one person in the world uses a reusable bottle."], "A", "The sentence covers the three benefits that organize the paragraph."),
    ("evidence", "A reader claims, 'The writer supports school gardens.' Which sentence would be strongest evidence?", ["The writer says gardens provide vegetables and a place for students to learn.", "The article has a green title.", "The reader likes plants.", "The writer mentions a school bell once."], "A", "The sentence gives explicit reasons showing support for school gardens."),
    ("inference", "A text says a child packed an umbrella, checked dark clouds, and changed the picnic location. What can readers infer?", ["The child expected rain and planned around it.", "The child was preparing for a swimming contest indoors.", "The picnic had already ended before the clouds appeared.", "The umbrella was packed to make the bag heavier."], "A", "The three actions together support a weather-related planning inference."),
    ("reference word", "In 'The museum opened a new room. It contains local maps,' what does It refer to?", ["The new room", "The museum visitors", "The local maps before they exist", "The opening time"], "A", "The singular pronoun It refers to the newly mentioned room."),
    ("purpose", "A text lists steps for washing hands and explains why each step prevents germs. What is the author's main purpose?", ["To teach a procedure and explain its health value", "To tell a fictional story about a lost hand", "To advertise a music concert", "To compare two kinds of school uniforms"], "A", "Steps plus reasons indicate instruction with an explanation of health benefits."),
    ("integrated strategy", "You must answer whether a text's claim is supported. Which reading process is strongest?", ["Predict the topic, skim for structure, scan for key details, then reread the evidence.", "Choose an option before reading and refuse to revise it.", "Use only the title and ignore all examples.", "Translate one sentence and treat it as the whole text."], "A", "The sequence combines efficient navigation with a final evidence check."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取閱讀策略、證據與理解監控能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以預測、略讀、掃讀、上下文線索、主旨、證據、推論、指涉與目的測量閱讀策略運用；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the situation and identify the reading skill: {topic}.",
        "State the reading purpose and mark the title, structure, target word, repeated idea, reference word, or evidence needed.",
        f"Apply the strategy to the text clue and select the choice supported by the reading process; the correct answer is {answer}.",
        f"Explain why the strategy fits: {explanation}",
        "Reread the relevant sentence or section, verify the answer against direct evidence, and revise the prediction if the text disagrees.",
    ]
    return {"id": f"question-english-performance-3-iv-12-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-12"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies reading-strategy and evidence-monitoring patterns only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; reading tasks, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-12", "examPatternRefs": refs, "solutionStrategy": "Set a reading purpose, use the matching navigation strategy, connect local clues to a claim, and return to the text to verify rather than treating a first guess as proof.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-12-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
