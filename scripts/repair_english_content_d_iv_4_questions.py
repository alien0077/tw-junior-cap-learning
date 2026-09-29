import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "fact, opinion, evidence, and reading purpose"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "notices, claims, and supported detail"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "short texts, audience, and evidence evaluation"),
]

DATA = [
    ("verifiable fact", "Which sentence can be checked directly using the school calendar?", ["The science fair begins on May 12.", "The science fair is the most exciting event.", "Everyone will love the fair.", "The fair should win an award."], "A", "A date is a verifiable detail in a calendar; the other sentences express evaluation or prediction."),
    ("opinion signal", "Which word most clearly signals an opinion in the sentence: 'This is the best way to save energy.'?", ["best", "way", "save", "energy"], "A", "Best expresses a personal judgment or ranking, so it signals an opinion rather than a neutral measurement."),
    ("evidence for claim", "A review says, 'This backpack is durable.' Which evidence would best support that claim?", ["It stayed intact after a controlled load-and-use test.", "It comes in a bright color.", "The reviewer likes its logo.", "The bag is on a shelf."], "A", "A controlled use test directly examines durability; color, logo preference, and location do not establish strength."),
    ("fact versus prediction", "A weather report states, 'Rain is expected tomorrow.' Which sentence is a prediction rather than a present fact?", ["It will probably rain tomorrow.", "The report was published today.", "The thermometer reads 24°C now.", "The forecast names a 70% chance."], "A", "Will probably describes a future expectation; the other choices report present or stated details that can be checked now."),
    ("mixed sentence", "A poster says, 'The pool is 25 meters long, so it is the perfect place for serious training.' Which part is an opinion?", ["the perfect place for serious training", "25 meters long", "the pool", "is"], "A", "The length is measurable, while perfect place for serious training evaluates the pool."),
    ("source and opinion", "A student reads: 'In my view, the new lunch menu is healthier.' What should the student ask before treating healthier as a fact?", ["What nutrition data or comparison supports the claim?", "Which font was used?", "Whether the writer likes lunch.", "How many chairs are in the cafeteria?"], "A", "A nutrition claim needs relevant data or a comparison, not design details or the writer's general preference."),
    ("advertising language", "Which phrase in an advertisement is mainly persuasive opinion?", ["the tastiest snack in town", "contains 3 grams of fiber", "sold in a 40-gram package", "available at the school store"], "A", "Tastiest is a promotional judgment; the other phrases present quantities or availability that can be checked."),
    ("fact supported by table", "A table records 32 students choosing apples and 18 choosing bananas. Which statement is a fact supported by the table?", ["More students chose apples than bananas.", "Apples are the most delicious fruit.", "Bananas are a poor choice.", "Everyone should choose apples tomorrow."], "A", "The counts support the comparison; the other statements add taste judgments or recommendations."),
    ("separate recommendation", "A report says the park received 120 visitors on Saturday. Which sentence is a recommendation?", ["The park should add another water station.", "The park received 120 visitors.", "Saturday was the busiest recorded day.", "The report lists the visitor number."], "A", "Should add proposes an action; the other sentences describe information from the report."),
    ("integrated evaluation", "A product page lists a lamp's price, brightness, and battery life. A reviewer writes, 'It is worth buying.' What is the best way to evaluate the review?", ["Use the listed specifications and your own needs to judge whether the recommendation fits.", "Treat the recommendation as a proven fact for every buyer.", "Ignore all specifications because opinions never matter.", "Assume a higher price always means better quality."], "A", "The specifications are evidence, while worth buying is a judgment that depends on the buyer's needs and criteria."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取事實意見與證據判讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以公告、評論、廣告、統計表與短文要求辨認可驗證事實、意見詞、證據與建議；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the statement and identify the evidence skill: {topic}.",
        "Ask whether the sentence can be checked with a calendar, measurement, record, or source, or whether it expresses judgment, preference, prediction, or advice.",
        f"Check the wording and choose the best answer: {answer}.",
        f"Explain the evidence boundary: {explanation}",
        "If a claim is evaluative, identify the criteria and evidence needed before accepting it as a general fact.",
    ]
    return {"id": f"question-english-content-d-iv-4-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-content-d-iv-4"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies fact, opinion, evidence, and recommendation patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; statements, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-d-iv-4", "examPatternRefs": refs, "solutionStrategy": "Classify each statement by its checkability and language, then connect judgments or recommendations to explicit criteria and evidence instead of treating them as universal facts.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-d-iv-4-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
