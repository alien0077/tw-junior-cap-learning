import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "cultural descriptions, details, and contextual inference"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short informational texts and daily-life context"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional reading, cause, comparison, and inference"),
]

DATA = [
    ("environment and lifestyle", "A village lies on a steep mountain slope, so many homes have narrow paths instead of wide roads. What best explains this feature?", ["The landform affects how people build and travel.", "The villagers never need to move anywhere.", "Mountain villages must all have the same language.", "Narrow paths are used only for festivals."], "A", "The steep slope makes wide roads difficult, so the environment can influence building and transportation."),
    ("food and climate", "A coastal town often serves grilled fish, seaweed soup, and fresh shellfish. Which statement is most supported?", ["Local food may reflect access to nearby marine resources.", "Everyone in the town eats only shellfish every day.", "The town cannot grow any plants.", "The food proves that the town has no winter."], "A", "The description supports a connection between coastal resources and local food, but it does not support the absolute claims."),
    ("clothing and weather", "In a cold region, a travel note describes thick wool coats, gloves, and indoor markets. What can readers infer?", ["People choose clothing and activities partly to cope with cold weather.", "The region is always hotter than a desert.", "Gloves are worn only for sports competitions.", "Indoor markets mean there are no shops outdoors anywhere."], "A", "Warm clothing and indoor activities are reasonable responses to cold conditions; the other choices go beyond the evidence."),
    ("housing adaptation", "Homes in a rainy area have steep roofs and raised doorways. Why might these features be useful?", ["They can help water run off and reduce water entering the home.", "They make rain fall upward.", "They show that residents never leave home.", "They are used to measure the number of clouds."], "A", "Steep roofs help rain drain, and raised doorways can reduce water entering, so both features fit a wet environment."),
    ("transportation", "A city has many canals and small bridges, and residents often use boats to carry goods. What is the best conclusion?", ["The water network is part of the city's transportation system.", "Boats are used because roads do not exist in any city.", "The residents cannot walk.", "Bridges are built only for decoration."], "A", "The text directly connects canals, boats, bridges, and carrying goods, showing that water is part of transportation."),
    ("seasonal work", "Farmers in a dry region collect and store rainwater before the hot season. What problem are they responding to?", ["They are preparing for a period with less available water.", "They are trying to make the hot season colder.", "They are replacing all crops with fish.", "They are collecting rainwater because rain never falls anywhere."], "A", "Storing rainwater before a hot season is a reasonable adaptation to expected water shortage, not proof that rain never falls."),
    ("local material", "A reading passage says houses near a bamboo forest use bamboo screens because the material is light and available nearby. Which idea does this illustrate?", ["People may use local materials that fit their needs and environment.", "Every house in the world must use bamboo.", "Bamboo screens can replace every building material.", "The forest makes all houses identical."], "A", "The passage gives a local-material choice based on availability and practical use; it does not make a universal claim."),
    ("cause and effect", "After a new bridge connects two neighborhoods, the text says farmers can send vegetables to market earlier. What changed?", ["Transportation became more efficient for moving goods.", "Vegetables began growing without water.", "The market moved into the river.", "Farmers stopped using roads and bridges."], "A", "The bridge shortens or improves the route, so farmers can transport produce earlier."),
    ("compare regions", "Region X has cool summers and many hiking trails. Region Y has hot summers and shaded street markets. Which comparison is supported?", ["Their environments may shape different outdoor activities and daily routines.", "Region X and Region Y must have identical clothing.", "Only Region Y has people.", "Hiking trails and markets are the same thing."], "A", "The information supports comparing how climate and place relate to activities, but not the absolute or unrelated claims."),
    ("integrated cultural geography", "A profile describes a river town: houses stand on higher ground, residents use boats during the rainy season, and meals often include river fish. Which summary is best?", ["The river and rainy environment influence housing, transportation, and food.", "The town has no connection with its environment.", "Residents use boats only because roads are illegal.", "River fish prove that every meal is the same."], "A", "The summary links three stated details to the river and rainy setting without adding unsupported rules or exaggerations."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{
        "url": url, "title": f"{title}；僅取風土民情閱讀能力方向，未複製原題、選項、圖表或答案。",
        "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "公開英文評量常以地理、生活方式、食物、居住、交通與文化情境測量主旨、因果、比較、細節與推論；本題為獨立改寫。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper",
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the description and identify the culture-and-place focus: {topic}.",
        "Underline the environmental condition, local practice, object, activity, or stated cause-and-effect relationship.",
        f"Check every choice against the passage; the correct answer is {answer}.",
        f"Explain the evidence without adding an absolute claim: {explanation}",
        "Separate a supported local pattern from an unsupported statement about all people, all places, or every occasion.",
    ]
    return {
        "id": f"question-english-content-c-iv-2-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-c-iv-2"], "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
            "sourceLocator": "Public-school English assessment materials; this item studies local environment and cultural-life reading patterns only and does not reproduce an original question, option, image, or answer.",
            "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; local-life contexts, options, explanations, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-c-iv-2", "examPatternRefs": refs,
        "solutionStrategy": "Connect explicit place and environment clues to daily practices, then verify whether each option stays within the passage's evidence instead of turning a local pattern into a universal rule.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-c-iv-2-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
