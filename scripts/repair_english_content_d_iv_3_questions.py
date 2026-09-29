import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "cause, effect, sequence, and evidence"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "narrative details, reasons, and supported inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional text, sequence, and causal reasoning"),
]

DATA = [
    ("event sequence", "The notice says the freezer door was left open overnight. In the morning, the food was warm and had to be discarded. What happened first?", ["The freezer door was left open.", "The food was discarded.", "The food became warm after the inspection.", "The notice was written next year."], "A", "The open door occurred overnight before the food was found warm and discarded, so it is the first event in the sequence."),
    ("direct cause", "A heavy rain blocked the road to the farm, so the delivery truck arrived late. What caused the delay?", ["The heavy rain and blocked road", "The truck arriving late", "The farm receiving the vegetables", "The driver reading the notice"], "A", "The text directly links heavy rain and the blocked road to the late arrival."),
    ("necessary condition", "The experiment guide says the plant must receive water to stay alive. A student stops watering it and the plant wilts. Which statement is careful?", ["Lack of water can contribute to the wilting in this situation.", "Water is the only possible factor in every plant problem.", "The student proved all plants need the same amount of water.", "Wilting caused the student to stop watering earlier."], "A", "The guide and observation support water shortage as a contributing factor, but not the absolute claim that no other factor matters."),
    ("correlation versus cause", "A town records more ice-cream sales and more sunburn cases in July. What is the best explanation?", ["Hot, sunny weather may contribute to both, so the two records alone do not prove that ice cream causes sunburn.", "Ice cream always causes sunburn.", "Sunburn makes people buy every kind of food.", "The records show no relationship at all."], "A", "A third factor, hot sunny weather, can affect both measures; simultaneous change alone does not prove direct causation."),
    ("multiple causes", "A bus was late because of road construction, a traffic accident, and a long passenger stop. What caused the delay?", ["Several factors together contributed to the delay.", "Only the passenger stop mattered.", "The bus was early because of construction.", "The accident happened after the bus arrived on time."], "A", "The passage names three contributing factors, so reducing the delay to one cause would ignore evidence."),
    ("effect prediction", "If the school fixes a leaking pipe, which result is most directly expected?", ["Less water will be wasted at that pipe.", "Every pipe in town will become new.", "The school will never need water again.", "The weather will change immediately."], "A", "Repairing the named leak directly addresses water loss at that location, but does not support claims about every pipe or the weather."),
    ("counterexample", "A student says, 'The new study app always raises scores because our class score rose once.' Which evidence would challenge the claim?", ["Another class used the app but showed no score increase under similar testing conditions.", "The app has a bright icon.", "The student likes studying on a phone.", "The class used pencils during the test."], "A", "A comparable case without an increase is a counterexample to the word 'always' and calls for more careful analysis."),
    ("before and after", "A school installed shade cloth in May. June playground temperatures were lower than May temperatures, but June was also cloudy. What should the report say?", ["Temperatures were lower after installation, but cloudier weather may also have contributed.", "The shade cloth alone definitely caused every degree of change.", "The installation had no possible connection.", "Clouds prove shade cloth never works."], "A", "The before-and-after pattern is relevant, but the changed weather is another possible explanation."),
    ("reason versus purpose", "A student wears a raincoat because it is raining. Which phrase states the reason, not the purpose?", ["because it is raining", "to stay dry", "in order to walk outside", "so that the clothes remain clean"], "A", "Because it is raining explains why the student wears the coat; the other phrases describe intended purposes or results."),
    ("integrated causal claim", "A report says a garden produced more vegetables after compost was added, but the gardeners also increased sunlight and watering. Which conclusion is strongest?", ["The harvest increased after several changes; the report cannot isolate compost as the only cause.", "Compost alone definitely caused the entire increase.", "Sunlight and water cannot affect plants.", "The harvest decreased before the changes."], "A", "Because several conditions changed together, the report supports an after-change increase but not a single-cause conclusion."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取因果與證據判讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以事件順序、原因結果、前後資料、多因素情境與推論界線測量因果判讀；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the passage and identify the causal task: {topic}.",
        "Mark which event happened first, which condition changed, which result was observed, and whether another factor is present.",
        f"Choose the option that matches the evidence without adding a stronger claim; the correct answer is {answer}.",
        f"Explain the causal boundary: {explanation}",
        "Replace words such as 'always,' 'only,' or 'definitely' with a narrower statement when the passage does not justify certainty.",
    ]
    return {"id": f"question-english-content-d-iv-3-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-content-d-iv-3"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies causal reasoning and evidence limits only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; causal scenarios, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-d-iv-3", "examPatternRefs": refs, "solutionStrategy": "Put events in time order, distinguish direct evidence from a possible explanation, check for alternative factors or counterexamples, and keep the conclusion no stronger than the data.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-d-iv-3-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
