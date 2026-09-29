import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "narrator perspective, attitude, purpose, and evidence"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "tone, viewpoint, claims, and reader inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "author purpose, attitude language, and textual support"),
]

DATA = [
    ("perspective", "A passage says, 'I checked the garden every morning and recorded each new leaf.' Which point of view is used?", ["First person, from the observer's perspective", "Second person, giving commands to the reader", "Third person, with no narrator involved", "A weather report with no human viewpoint"], "A", "The repeated I shows that the narrator participates and reports personal observations."),
    ("attitude", "A writer describes a community garden as 'a cheerful place where neighbors share tools and stories.' What is the writer's attitude?", ["Positive and appreciative", "Angry and rejecting", "Uncertain that the garden exists", "Indifferent to every neighbor"], "A", "Cheerful and share carry favorable emotional meanings."),
    ("purpose", "An article gives three reasons to turn off lights when leaving a room and ends with 'Small actions save energy.' What is its purpose?", ["To encourage energy-saving behavior", "To tell readers how to design a lamp", "To criticize every form of electricity", "To describe a fictional night journey"], "A", "Reasons and the final call about small actions aim to persuade readers to save energy."),
    ("fact versus attitude", "A report says, 'The bus arrived at 7:10, but unfortunately the crowded ride made the trip uncomfortable.' Which phrase shows attitude?", ["unfortunately ... uncomfortable", "arrived", "at 7:10", "the bus"], "A", "The evaluative words express the writer's negative judgment, while the other details are factual."),
    ("narrator knowledge", "A narrator says, 'I saw Mei enter the room, but I do not know what she planned.' What limitation does this show?", ["The narrator reports an observation but cannot know Mei's private plan.", "The narrator knows every character's thoughts.", "The narrator was not present in the room.", "The narrator is giving directions to Mei."], "A", "The sentence separates visible action from information the narrator does not possess."),
    ("purpose and audience", "A school newsletter explains how to join a recycling team, lists a contact email, and names a deadline. Who is the likely audience?", ["Students who may want to join the team", "People repairing a distant bridge", "Readers looking for a poem about winter", "Only the newsletter printer"], "A", "The instructions, contact, and deadline address potential participants."),
    ("tone shift", "At first a writer says, 'I worried that the new student would feel alone.' Later the writer says, 'By lunch, we were laughing together.' What shift occurs?", ["From concern to warmth and relief", "From excitement to anger", "From certainty to complete confusion", "From criticism to fear of a storm"], "A", "The emotional language moves from worry to a friendly successful connection."),
    ("claim evidence", "A writer claims that walking meetings help teams think. Which evidence would best support the claim?", ["The writer describes two meetings where walking produced several workable ideas.", "The writer likes comfortable shoes.", "The office has a blue door.", "The claim appears in a very large font."], "A", "Observed examples connecting walking meetings with ideas directly support the claim."),
    ("loaded word", "A review calls a new schedule 'a wonderfully flexible plan.' What does wonderfully suggest?", ["Strong approval", "Fear of the plan", "A neutral measurement only", "Proof that the plan is impossible"], "A", "Wonderfully is an intensifier that expresses favorable evaluation."),
    ("integrated analysis", "A first-person article describes a failed beach clean-up, admits the writer underestimated the trash, thanks volunteers, and asks readers to join next month. Which analysis is best?", ["The writer is reflective, appreciative, and encouraging readers to participate.", "The writer is mocking volunteers and wants the clean-up cancelled.", "The article has no purpose because it reports an event.", "The writer claims the beach had no trash at all."], "A", "The admission shows reflection, thanks show appreciation, and the invitation shows an encouraging purpose."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取敘事者觀點、態度、目的與證據判讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以第一人稱、情緒詞、目的、受眾、主張與支持證據測量文本立場及語氣分析；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the passage and identify the analysis focus: {topic}.",
        "Mark pronouns, evaluative words, action verbs, audience clues, stated reasons, claims, and evidence before judging attitude or purpose.",
        f"Compare the choices with the narrator's exact language and select the interpretation supported by the text; the correct answer is {answer}.",
        f"Explain the viewpoint, tone, purpose, or evidence: {explanation}",
        "Reread one supporting phrase and state how a different word, audience, or narrator position would change the analysis.",
    ]
    return {"id": f"question-english-performance-3-iv-15-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-15"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies narrator-viewpoint, attitude, purpose, and evidence patterns only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; passages, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-15", "examPatternRefs": refs, "solutionStrategy": "Separate who is speaking from how the wording evaluates a subject, identify the intended audience and purpose, and connect any interpretation to a precise textual phrase.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-15-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
