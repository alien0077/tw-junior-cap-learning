import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "fact, opinion, evidence, claims, and text clues"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "verifiable statements, subjective language, and supported opinions"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "distinguishing information from interpretation and evaluation"),
]

DATA = [
    ("verifiable fact", "Which sentence is a fact that could be checked with a school calendar?", ["The science fair is on May 18.", "The science fair is the most exciting event.", "Everyone should love the science fair.", "The science fair feels magical."], "A", "A date can be checked against a calendar, while the other sentences express evaluation or feeling."),
    ("opinion marker", "Which word most clearly signals an opinion in 'In my view, the new park is the best place to exercise'?", ["In my view and best", "new and park", "place and exercise", "the and is"], "A", "In my view marks a personal position, and best evaluates the park."),
    ("evidence", "A writer claims the new bus route is useful and cites that it connects three neighborhoods. What is the cited information?", ["It connects three neighborhoods", "It is useful", "The writer's personal preference", "The word new"], "A", "The connection among neighborhoods is the concrete support for the claim."),
    ("fact versus evaluation", "Which statement contains an evaluation rather than only information?", ["The museum opens at 9:00.", "The museum has four galleries.", "The museum's entrance is beautiful.", "The museum is on River Street."], "C", "Beautiful expresses a judgment that different readers may not share."),
    ("checkability", "A post says, 'The meal costs $8' and 'It is the tastiest meal in town.' Which statement is more directly verifiable?", ["The meal costs $8", "It is the tastiest", "Both are personal feelings", "Neither can be checked"], "A", "A listed price can be checked, while tastiest depends on personal judgment and comparison."),
    ("mixed sentence", "'The trail is 2 kilometers long, so it is perfect for a relaxing walk.' Which part is an opinion?", ["It is perfect for a relaxing walk", "The trail is 2 kilometers long", "The word trail", "The number 2 alone"], "A", "Perfect and relaxing express an evaluation based on the writer's judgment."),
    ("source clue", "A report says, 'According to the survey, 68 students chose bicycles.' What kind of support is this?", ["Quantitative evidence from a survey", "A personal feeling with no source", "A fictional character's dialogue", "A prediction about an unknown result"], "A", "The survey and number identify sourced quantitative evidence."),
    ("balanced reading", "A writer says, 'The library should stay open later because many students study after school.' What should a reader ask?", ["What evidence shows that many students study after school?", "Why are libraries made of books?", "Which opinion is always correct?", "Can the claim be accepted without any support?"], "A", "The reader should examine the evidence supporting the recommendation."),
    ("fact and opinion set", "A paragraph states that a river is 120 kilometers long and calls it the country's most beautiful river. Which classification is correct?", ["The length is a fact; the beauty claim is an opinion", "Both are opinions because rivers are natural", "Both are facts because the paragraph says them", "The beauty claim is a measurement"], "A", "Length is measurable, while beauty is an evaluative judgment."),
    ("integrated evaluation", "A review lists a movie's release date, length, ticket price, and the reviewer's claim that it is unforgettable. How should a reader use the information?", ["Treat date, length, and price as checkable details, and treat unforgettable as the reviewer's opinion.", "Treat every sentence as an objective measurement.", "Reject all details because one sentence is an opinion.", "Treat unforgettable as a ticket price."], "A", "The reader can separate verifiable details from subjective evaluation rather than accepting or rejecting everything together."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取事實、意見、證據、主觀詞、可驗證性與混合文本判讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以公告、評論、圖表與短文要求分辨可查證資訊、主觀評價、作者主張、證據來源及混合句；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the text and identify the fact-opinion target: {topic}.",
        "Underline dates, numbers, places, sources, modal words, evaluative adjectives, feelings, and claims that could be checked.",
        f"Classify the statement or clause using its wording and evidence status; the correct answer is {answer}.",
        f"Explain which text clue makes it factual, evaluative, or evidence-based: {explanation}",
        "Reread the sentence and separate checkable information from the writer's judgment instead of treating the whole paragraph as one type.",
    ]
    return {"id": f"question-english-performance-9-iv-4-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-9-iv-4"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies distinguishing fact, opinion, evidence, subjective wording, checkability, and mixed claims only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; statements, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-9-iv-4", "examPatternRefs": refs, "solutionStrategy": "Locate checkable details and sources, notice evaluative language, separate claims from evidence, and classify each clause rather than the paragraph by impression.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-9-iv-4-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
