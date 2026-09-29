import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "global information, maps, and inference"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "informational reading, data details, and context"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "comparison, cause, and practical application"),
]

DATA = [
    ("map direction", "On a map, Island A is west of Island B. A boat travels from B directly to A. In which direction does it travel?", ["West", "East", "North", "South"], "A", "If A is west of B, a direct trip from B to A travels west."),
    ("continent location", "A travel note says a country is south of the Mediterranean Sea and north of the Sahara Desert. Which information does this help identify?", ["Its broad geographic location", "Its exact population", "The name of every city there", "The country's future weather"], "A", "The two geographic features provide location clues, but they cannot establish population, every city, or future weather."),
    ("time zone", "City P is two hours ahead of City Q. If it is 9 a.m. in Q, what time is it in P?", ["7 a.m.", "9 a.m.", "11 a.m.", "2 p.m."], "C", "Being two hours ahead means adding two hours to 9 a.m., giving 11 a.m."),
    ("data table", "A table reports that Country X has 80 million people and Country Y has 20 million. What is directly supported?", ["Country X has four times as many people as Country Y in this table.", "Country X is always richer.", "Every city in X is larger than every city in Y.", "Y has no rural area."], "A", "Eighty million is four times twenty million; the other claims require evidence not shown in the table."),
    ("language distribution", "A map shows several languages near a national border. What is the most careful interpretation?", ["Languages can be used across borders, and political borders do not always match language areas.", "Each country must have exactly one language.", "People near borders cannot communicate.", "The map proves every speaker has the same culture."], "A", "The map supports language areas crossing a border, but it does not prove a single culture or communication problem."),
    ("environment and settlement", "A map shows most large cities near a river or coast. Which explanation is reasonable but still needs more evidence?", ["Water access may support transport, settlement, or trade.", "Every city must be built on a beach.", "Rivers create all jobs in every city.", "Coastal cities never face hazards."], "A", "Water access can support several human activities, but the map alone cannot prove one cause for every city."),
    ("migration route", "A student reads that many people moved from a rural area to a nearby city for school and jobs. What does this describe?", ["A population movement connected with education and employment.", "A change in the Earth's orbit.", "A language disappearing overnight.", "A weather forecast for the city."], "A", "The text directly links movement of people with school and work opportunities."),
    ("source reliability", "Two websites give different numbers for a country's population. What should a student check first?", ["The publication date, organization, definition, and original data source.", "Which page uses brighter colors.", "Which number is more surprising.", "The number that a friend prefers."], "A", "Population estimates can differ by date or definition, so source, date, and method must be checked before choosing."),
    ("global connection", "A phone is designed in one country, uses parts from several countries, and is assembled in another. What does this illustrate?", ["Products can be made through international supply and cooperation.", "A product has only one country connected to it.", "Countries cannot trade technology.", "Assembly location proves where every material came from."], "A", "The description names several countries and stages, illustrating a connected supply chain without claiming all materials have the same origin."),
    ("integrated world view", "A world-data card shows climate, population, transport, and language information for three regions. Which study habit is best?", ["Read the legend and units, compare like with like, and state only conclusions supported by the data.", "Choose the region with the largest number and call it best.", "Ignore the map legend because pictures are enough.", "Use one region's data to describe every region."], "A", "Accurate global reading requires checking the legend and units, comparing equivalent measures, and limiting conclusions to the evidence."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{
        "url": url, "title": f"{title}；僅取全球資訊與資料判讀能力方向，未複製原題、選項、圖表或答案。",
        "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "公開英文評量常以地圖、表格、時間、人口、地理位置、移動與全球情境測量細節、推論、比較與證據界線；本題為獨立改寫。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper",
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the global-information prompt and identify the skill: {topic}.",
        "Check the map direction, time relation, number, legend, source date, or stated connection before interpreting it.",
        f"Compare each choice with the available evidence; the correct answer is {answer}.",
        f"Explain the calculation or evidence boundary: {explanation}",
        "State the conclusion with the correct unit, direction, time, place, and scope, and avoid extending one data point to the whole world.",
    ]
    return {
        "id": f"question-english-content-c-iv-5-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-c-iv-5"], "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
            "sourceLocator": "Public-school English assessment materials; this item studies basic world-view, map, data, and global-context reading patterns only and does not reproduce an original question, option, image, or answer.",
            "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; global contexts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-c-iv-5", "examPatternRefs": refs,
        "solutionStrategy": "Read the map, table, clock, source note, or global scenario precisely, then apply the relevant relation and limit the answer to what the evidence can support.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-c-iv-5-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
