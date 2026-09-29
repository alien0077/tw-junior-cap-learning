import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "global awareness, places, people, environment, and shared needs"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "world geography, global connections, evidence, and perspectives"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "understanding the world through maps, data, culture, and responsible action"),
]

DATA = [
    ("map and location", "A map shows two cities on opposite sides of the same river. What can the map support?", ["The cities share a geographic feature and may have connections across the river", "The cities must have identical cultures and histories", "The map proves no one travels between them", "The river has no relationship to either city"], "A", "The map supports a geographic relationship, but not unsupported claims about culture or travel."),
    ("time zones", "A message says a video meeting begins at 8:00 p.m. in Taipei and 8:00 a.m. in another city. What should participants check?", ["The time-zone difference before joining", "Whether both cities use the same school uniforms", "The weather in every country on Earth", "Whether time zones affect the meeting topic"], "A", "Different local times require checking time zones so participants join at the intended moment."),
    ("global connection", "A passage explains that a phone may be designed in one country, use materials from another, and be assembled in a third. What idea does it show?", ["Products can involve cooperation and supply chains across countries", "Every product is made entirely in the buyer's city", "Countries never depend on one another", "A phone has no connection to people or resources"], "A", "The stages describe a global production network."),
    ("shared need", "A city project plants trees to reduce heat and create shade. Which broader issue does it connect to?", ["Communities in many places may seek healthier environments", "Only one street in the world needs shade", "Trees can solve every social problem alone", "Environmental conditions never affect people"], "A", "Reducing heat and creating shade reflect a need shared by many communities."),
    ("evidence and scale", "A chart shows one country's population increasing, while a paragraph says population trends vary by region. What is the careful conclusion?", ["The chart describes that country; more regional evidence is needed for a global claim", "The one-country chart proves every region is growing", "No population data can ever be useful", "The paragraph must be wrong because the chart has numbers"], "A", "The conclusion respects the scale of the evidence."),
    ("multiple perspective", "A new dam provides electricity but changes a village's river access. Which world-view response considers both sides?", ["Examine energy benefits and listen to affected residents before deciding", "Celebrate the dam and ignore residents", "Reject all electricity projects without reading evidence", "Assume the village has no valid perspective"], "A", "A balanced response includes environmental or social impact and development needs."),
    ("resource responsibility", "A school learns that water use in one place can affect shared watersheds. Which action shows global responsibility?", ["Reduce waste and consider how local choices affect other people and ecosystems", "Use as much water as possible because only local users matter", "Avoid learning where water comes from", "Blame a distant community without checking facts"], "A", "Responsible action links local behavior with broader environmental systems."),
    ("migration context", "A story says a family moved to a new country for work and keeps both old and new traditions. What is a fair interpretation?", ["People can belong to more than one cultural context and adapt over time", "Moving requires abandoning every earlier identity", "All families move for exactly the same reason", "The family cannot contribute to the new community"], "A", "The story supports a complex identity rather than a single fixed label."),
    ("source perspective", "A news article describes an international project from one country's viewpoint. What should a reader do for a fuller understanding?", ["Compare reliable accounts and notice whose experiences are included or missing", "Treat one viewpoint as the complete truth automatically", "Reject the article without reading any evidence", "Choose the viewpoint with the most dramatic title"], "A", "Comparing perspectives reveals scope and possible omissions."),
    ("integrated world view", "A class studies a map, a climate chart, interviews with residents, and a report about trade. Which conclusion shows basic world awareness?", ["Places, environments, people, and economies are connected, so claims should use evidence from more than one source.", "One map can explain every human experience without other evidence.", "Global issues belong only to governments and never affect students.", "Different sources cannot be combined because they use different formats."], "A", "A world view connects systems and uses multiple forms of evidence without oversimplifying."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取基本世界觀的地理、時間、全球連結、共同需求、證據尺度、觀點與責任能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量與全球議題情境常以地圖、時間、文化、環境、資料與生活案例測量跨地區理解、證據尺度、多元觀點與負責任行動；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the world-related situation and identify the global-awareness target: {topic}.",
        "Mark the place, scale, time, people, environment, economic connection, perspective, and evidence source.",
        f"Choose the conclusion that fits the stated evidence without overgeneralizing or ranking people; the correct answer is {answer}.",
        f"Explain how the information supports a connected and responsible view of the world: {explanation}",
        "Reread the source and check that the conclusion distinguishes local evidence from a broader claim and includes affected perspectives.",
    ]
    return {"id": f"question-english-performance-8-iv-5-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-8-iv-5"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies basic global awareness, geography, time, interdependence, scale, perspectives, environment, and responsible action only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; global contexts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-8-iv-5", "examPatternRefs": refs, "solutionStrategy": "Locate the place and scale, connect people and systems, compare perspectives, and limit conclusions to what the evidence can support.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-8-iv-5-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
