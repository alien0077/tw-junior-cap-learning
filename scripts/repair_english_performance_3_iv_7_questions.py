import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "dialogue main ideas, details, and speaker purpose"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "conversation sequence, intentions, and responses"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "spoken exchanges, detail reading, and inference"),
]

DATA = [
    ("main idea", "A student tells a friend, 'I missed the bus, so I called my mother. She will pick me up at the library.' What is the conversation mainly about?", ["How the student will get home after missing the bus", "How to buy a new library", "Why buses never run on weekends", "The mother's favorite book"], "A", "The lines focus on the problem and the arranged way home."),
    ("specific detail", "A: 'Are you joining the art workshop?' B: 'Yes, at two o'clock in Room 12.' When and where will B join?", ["At 2:00 in Room 12", "At 12:00 in Room 2", "At two o'clock in the library", "Tomorrow in the art shop"], "A", "B explicitly gives both the time and room number."),
    ("speaker purpose", "A: 'Could you send me the science file?' B: 'Sure. I will email it after dinner.' What does A want?", ["The science file", "A dinner invitation", "A new science teacher", "A place to email"], "A", "The request asks B to send the science file."),
    ("sequence", "First, the friends choose a recipe. Next, they buy vegetables. Finally, they cook together. What happens before cooking?", ["They choose a recipe and buy vegetables.", "They eat the finished meal twice.", "They close the market before choosing.", "They cook before buying anything."], "A", "The conversation gives recipe choice and shopping as the two earlier steps."),
    ("attitude", "A: 'I thought the test was difficult.' B: 'Really? I found the reading part quite easy.' How does B respond?", ["B gives a different opinion.", "B refuses to discuss the test.", "B asks for a new textbook.", "B apologizes for being late."], "A", "B contrasts a personal evaluation of the reading section with A's view."),
    ("problem and solution", "A: 'The classroom projector is not working.' B: 'Let's use the large monitor in Room 8.' What solution does B suggest?", ["Use the large monitor in Room 8.", "Repair every projector in the school.", "Cancel all classes for a week.", "Move the monitor to the cafeteria without asking."], "A", "B proposes the available monitor in Room 8 as an alternative."),
    ("referent", "A: 'I left my red notebook on the bus.' B: 'I hope you find it.' What does 'it' refer to?", ["The red notebook", "The bus driver", "The hope", "The bus stop"], "A", "The pronoun it refers to the lost notebook."),
    ("implied intention", "A: 'The room is very dark.' B: 'I will open the curtains.' What does B intend to do?", ["Make the room brighter", "Close the curtains more tightly", "Leave the room immediately", "Paint the room tomorrow"], "A", "Opening curtains responds to darkness by letting in more light."),
    ("best title", "A dialogue covers choosing a meeting day, checking everyone's schedule, and agreeing on Friday afternoon. Which title fits?", ["Choosing a Meeting Time", "A History of Friday", "How to Repair a Clock", "The Best Afternoon Weather"], "A", "The title summarizes the shared decision about when to meet."),
    ("integrated inference", "A: 'I printed the map and packed water.' B: 'Great. I checked the weather, and it should stay clear until noon.' What are they most likely preparing for?", ["A morning outdoor trip", "An indoor piano lesson at midnight", "A cooking contest with no travel", "A winter clothing sale next month"], "A", "A map, water, and a weather check together support an outdoor morning plan."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取對話主旨、細節與說話者意圖能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以雙人對話測量主旨、時間地點、目的、順序、態度、代名詞指涉與有限推論；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the dialogue and identify the comprehension task: {topic}.",
        "Mark who is speaking, the key action or problem, time/place details, pronoun references, and any cause or response.",
        f"Compare the choices with the complete exchange and select the one supported by the speakers' words; the correct answer is {answer}.",
        f"Explain the dialogue evidence: {explanation}",
        "Retell the exchange in one sentence and check that the selected answer does not add a fact the speakers never supplied.",
    ]
    return {"id": f"question-english-performance-3-iv-7-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-7"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies dialogue comprehension and spoken-inference patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; dialogues, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-7", "examPatternRefs": refs, "solutionStrategy": "Track each speaker's purpose and response, extract explicit details before inferring, connect events in order, and choose a conclusion limited to the dialogue evidence.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-7-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
