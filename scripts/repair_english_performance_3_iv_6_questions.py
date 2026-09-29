import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "sentence patterns, grammar in context, and functional meaning"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "basic structures, tense, and sentence completion"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "grammar choices, context clues, and application"),
]

DATA = [
    ("subject-verb agreement", "The notice says, 'The science club ___ every Thursday.' Which form completes it?", ["meets", "meet", "meeting", "to meet"], "A", "The singular subject club takes the present-tense form meets."),
    ("past event", "Yesterday, Mia ___ her project to the teacher before lunch.", ["submitted", "submit", "submits", "is submitting"], "A", "Yesterday signals a completed past action, so submitted fits."),
    ("there is", "Which sentence correctly tells a visitor that one map is on the wall?", ["There is a map on the wall.", "There are a map on the wall.", "There be a map on the wall.", "There is maps on the wall."], "A", "A singular map takes there is."),
    ("question order", "Which question correctly asks about the location of the meeting?", ["Where is the meeting?", "Where the meeting is?", "Is where the meeting?", "The meeting where is?"], "A", "A direct wh-question uses the question word, be verb, and subject in this order."),
    ("comparison", "The blue route is shorter than the red route. Which sentence has the same meaning?", ["The red route is longer than the blue route.", "The blue route is the longest of every route.", "The red route is as short as the blue route.", "The routes are short because they are blue."], "A", "If blue is shorter than red, red is longer than blue."),
    ("modal obligation", "The laboratory sign says students ___ wear safety glasses.", ["must", "would", "might have", "are wearing yesterday"], "A", "Must expresses the required safety action."),
    ("purpose infinitive", "Lena went to the library ___ a quiet place to study.", ["to find", "finding", "found", "finds"], "A", "To find introduces the purpose of going to the library."),
    ("because clause", "The game moved indoors ___ heavy rain covered the field.", ["because", "but", "or", "so that"], "A", "Because introduces the reason for moving the game."),
    ("present continuous", "Look! The students ___ a model of the bridge now.", ["are building", "build yesterday", "built every now", "to build"], "A", "Now and Look signal an action happening at this moment."),
    ("integrated sentence", "Which sentence correctly tells a friend that you finished the task, explains why, and offers the next step?", ["I finished the task because I checked the data, so I can present it now.", "I finish yesterday because data, so presenting was.", "I am finish the task but because checked and now.", "The task finished me, so data is a presentation."], "A", "The sentence uses a past result, a because reason, and so to connect the available next action."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取基本句型、文法語境與句意判讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以動詞形式、疑問句語序、比較、情態、連接詞與不定詞放入生活語境測量句型理解；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the sentence and identify the grammar function: {topic}.",
        "Mark the subject, time signal, auxiliary or connector, and the relationship the sentence must express.",
        f"Compare each option for form and meaning, then select the one that makes the complete sentence grammatical; the correct answer is {answer}.",
        f"Explain the form-and-context match: {explanation}",
        "Reread the complete sentence aloud and change the time, subject, or purpose condition once to confirm which part would need to change.",
    ]
    return {"id": f"question-english-performance-3-iv-6-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-6"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies basic sentence-pattern and grammar-in-context abilities only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; sentences, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-6", "examPatternRefs": refs, "solutionStrategy": "Read the whole sentence first, locate time and subject clues, identify the needed structure or connector, and reject choices that fail either grammar or meaning.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-6-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
