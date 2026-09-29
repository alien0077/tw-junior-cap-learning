import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "context, cause, effect, sequence, condition, and connectors"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "reading causal relationships and selecting context-appropriate meaning"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "inferring cause and effect from connected sentences and events"),
]

DATA = [
    ("because", "The field trip was moved indoors because the forecast predicted heavy rain. What does because introduce?", ["The reason for moving the trip", "The place where rain was invented", "A result that happened before the forecast", "An unrelated activity"], "A", "The clause after because explains why the trip was moved."),
    ("therefore", "The path was covered with fallen leaves; therefore, the workers closed it for cleaning. What is the effect?", ["The workers closed the path", "Leaves grew on the path after it closed", "The path caused the weather", "No action followed the leaves"], "A", "Therefore signals that closing the path follows from the leaves."),
    ("sequence", "First, Sara saved her file. Then, the computer restarted. After that, she opened the file again. What happened before she reopened it?", ["She saved the file and the computer restarted", "She printed the file twice", "She deleted the file permanently", "She opened it before saving anything"], "A", "The time markers place saving and restarting before reopening."),
    ("condition", "If the library has a free study room, the group will meet there; otherwise, they will use the classroom. What determines the location?", ["Whether the library room is available", "The color of the group's notebooks", "The weather from last week", "The number of books in a different city"], "A", "The if condition and otherwise alternative make availability the deciding factor."),
    ("contrast cause", "The sign says the elevator is out of order, so visitors should use the stairs. Why should visitors use the stairs?", ["The elevator cannot be used", "The stairs are always faster than elevators", "Visitors are not allowed inside the building", "The sign is about a restaurant menu"], "A", "The elevator's condition causes the suggested alternative."),
    ("before and after", "Mina charged her phone before leaving, so she could use the map during the hike. What was the purpose of charging it?", ["To have power for using the map", "To make the hike shorter", "To replace the map with a paper ticket", "To stop the phone from displaying directions"], "A", "Charging before leaving provides power for the later map use."),
    ("unless", "The team will practice outside unless the air quality is poor. When will they not practice outside?", ["When the air quality is poor", "Whenever the sky is blue", "When the team has enough time", "Only after the practice ends"], "A", "Unless introduces the exception that prevents the usual plan."),
    ("counterfactual", "The notice says, 'Without the backup battery, the alarm would not have worked during the outage.' What does this imply?", ["The backup battery allowed the alarm to work during the outage", "The outage made the alarm louder before the battery", "The alarm was never connected to power", "The battery caused the outage"], "A", "The without construction identifies the battery as a necessary support in the imagined situation."),
    ("paragraph coherence", "A paragraph says the river became polluted, fish numbers fell, and the town installed a filtering system. Which order best shows the relationship?", ["Pollution → fewer fish → filtering response", "Filtering response → pollution → fewer fish only", "Fewer fish → unrelated holiday → pollution", "All events happened without any connection"], "A", "The sequence follows the problem, consequence, and response."),
    ("integrated causality", "A school planted shade trees, measured lower playground temperatures, and reported that students stayed outside longer. Which explanation best fits the context?", ["The trees may have made the playground cooler, which may have encouraged longer outdoor activity.", "The students stayed longer, so the trees must have been planted afterward.", "The measurements prove trees cause every change in student behavior.", "Temperature and outdoor activity cannot be related."], "A", "The explanation respects the observed sequence and uses cautious causal language."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取上下文因果、結果、順序、條件、連接詞與多句脈絡能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以公告、故事、說明與生活情境測量 because、therefore、if、unless、before、after 等關係，要求由上下文釐清原因、結果與條件；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the connected sentences and identify the causal target: {topic}.",
        "Underline connectors, time markers, conditions, exceptions, actions, and results, then place events on a timeline if needed.",
        f"Match the cause, effect, condition, or sequence to the wording and choose the supported interpretation; the correct answer is {answer}.",
        f"Explain the relationship between the sentences: {explanation}",
        "Reread both clauses and check that the answer does not reverse time order or claim stronger causation than the context provides.",
    ]
    return {"id": f"question-english-performance-9-iv-3-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-9-iv-3"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies contextual cause, effect, sequence, condition, connectors, and cautious causal reasoning only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; contexts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-9-iv-3", "examPatternRefs": refs, "solutionStrategy": "Track connectors and event order, identify which clause supplies the reason or result, and distinguish a supported relation from an overstrong causal claim.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-9-iv-3-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
