import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "titles, pictures, and prediction before reading"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "book titles, visual clues, and limited inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "headings, images, and predicting content"),
]

DATA = [
    ("title clue", "A book is titled 'The Last Seed' and its cover shows a child protecting one small plant in dry soil. What is the book likely about?", ["Protecting a plant in a difficult environment", "Training a large team of swimmers", "A guide to repairing clocks", "A menu for a winter restaurant"], "A", "The title and image jointly point to a seed, a plant, and a challenging dry setting."),
    ("image setting", "A poster is titled 'Night at the Museum' and shows a dark exhibition hall with a flashlight. Where will the event most likely happen?", ["In a museum after dark", "At a beach in the morning", "In a supermarket kitchen", "On a school bus at noon"], "A", "The title names the museum and the image supports a nighttime setting."),
    ("character prediction", "The cover 'Maya Builds a Robot' shows a girl holding wires beside a workbench. What can readers predict?", ["Maya will probably create or repair a robot.", "Maya will train for a swimming race.", "Maya will run a bakery without tools.", "Maya will travel to a forest to find a horse."], "A", "The title, character, wires, and workbench all support a robot-building activity."),
    ("heading purpose", "A webpage heading says 'Three Ways to Save Water' above pictures of a short shower, a closed tap, and a rain barrel. What will the text likely do?", ["Explain three water-saving actions", "Describe three kinds of musical instruments", "Tell a story about a lost passport", "List the names of every river in the world"], "A", "The heading gives the topic and number, while the pictures preview water-saving actions."),
    ("book genre clue", "A cover titled 'Mystery at Platform 4' shows a train station, a magnifying glass, and a shadowy suitcase. What kind of reading is likely?", ["A mystery involving a station and a missing or puzzling object", "A recipe collection for train meals", "A science report about engine fuel only", "A biography of a famous chef"], "A", "Mystery, the station, and the magnifying glass signal a puzzling narrative."),
    ("event prediction", "A school poster titled 'From Seed to Salad' shows students planting, watering, and holding a bowl of vegetables. What might the activity include?", ["Growing vegetables and using them in food", "Building a model airplane from metal", "Studying only the history of sports", "Painting a winter mountain without plants"], "A", "The sequence of images predicts growing plants and using the harvest as food."),
    ("warning title", "A sign titled 'Before You Hike' shows a water bottle, a map, and a cloudy mountain trail. What information will likely follow?", ["Preparation and safety advice for a hike", "Instructions for buying a train ticket", "A list of indoor dance costumes", "A recipe using only sugar"], "A", "The title and objects suggest preparation and safety before hiking."),
    ("compare clues", "Two article titles are 'City Birds' and 'Deep-Sea Travelers.' Which topic best matches both titles?", ["Animals living or moving in two different environments", "A single recipe for city and sea food", "How to build two kinds of roads", "The history of one classroom window"], "A", "The titles point to birds in cities and travelers in the deep sea, both environmental topics."),
    ("avoid overclaim", "A cover titled 'A Rainy Saturday' shows one child looking through a window. Which prediction is reasonable but limited?", ["The story may describe what the child does during a rainy Saturday.", "Every person in the town will definitely stay indoors all day.", "The book proves that rain is always dangerous.", "The child must be traveling to another country."], "A", "The prediction uses the title and image without claiming facts beyond the available clues."),
    ("integrated preview", "A chapter preview has the title 'The New Neighbor,' a picture of moving boxes, and a caption 'A note under the door.' What is most likely to happen first?", ["A new person arrives, and a note begins a neighborhood interaction.", "The neighbors finish a year-long war before anyone moves.", "The boxes are revealed to be a weather chart.", "The chapter begins with a sports final unrelated to the home."], "A", "The title, boxes, and note together preview a new arrival and an initial interaction."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取圖片、標題、書名與閱讀前推測能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以標題、圖片、書名、圖說與預讀線索要求學生提出有限且可驗證的內容預測；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the title, caption, and visual clue, then identify the prediction task: {topic}.",
        "List the concrete people, objects, place, action, number, and genre signals before making a prediction.",
        f"Choose the prediction that fits all visible and written clues without adding unsupported details; the correct answer is {answer}.",
        f"Explain the clue connection: {explanation}",
        "State the prediction as a tentative idea, then note what text evidence would confirm or revise it after reading.",
    ]
    return {"id": f"question-english-performance-3-iv-11-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-11"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies title, image, and pre-reading prediction patterns only and does not reproduce an original question, option, image, or book cover.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; previews, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-11", "examPatternRefs": refs, "solutionStrategy": "Combine the title or heading with concrete visual clues, make a narrow prediction, and keep it tentative until later text evidence confirms or changes it.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-11-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
