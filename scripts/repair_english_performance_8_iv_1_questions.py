import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "festival notices, cultural descriptions, dates, activities, and audience"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "domestic festivals, event details, invitations, and cultural practices"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "reading festival information and explaining local culture"),
]

DATA = [
    ("festival purpose", "A notice says families gather during the Mid-Autumn Festival to share mooncakes and look at the moon. What is the notice mainly introducing?", ["A local festival activity and its family tradition", "A winter sports competition", "A school examination schedule", "A recipe for making train tickets"], "A", "The notice connects a festival with family gathering, food, and moon viewing."),
    ("date and activity", "A Lantern Festival program lists a lantern display on Saturday evening and a daytime cooking class on Sunday. When is the lantern display?", ["Saturday evening", "Sunday morning", "Friday afternoon", "Every weekday at noon"], "A", "The program places the lantern display on Saturday evening."),
    ("Dragon Boat clue", "A passage describes teams paddling long boats and watching races on a river during a traditional local festival. Which activity is central?", ["A dragon boat race", "A snowboarding lesson", "A harvest movie screening", "A school spelling test"], "A", "Long boats, paddling teams, and river races identify dragon boat racing."),
    ("cultural meaning", "A student explains that a festival lets neighbors visit one another and share traditional food. What value is emphasized?", ["Community connection and sharing", "Avoiding every neighbor", "Winning a private competition", "Replacing all traditions with advertisements"], "A", "Visiting and sharing food highlight community relationships."),
    ("audience", "A school poster invites students to introduce one domestic festival to exchange students. Who is the intended audience for the presentation?", ["Exchange students and the school audience", "Only professional athletes", "A group of museum guards", "People who cannot attend any school activity"], "A", "The poster names exchange students as the audience and places the task at school."),
    ("appropriate behavior", "At a crowded festival, which action shows respect for the event and other visitors?", ["Follow the signs, wait your turn, and avoid blocking the performance.", "Push through the crowd and step onto the stage.", "Take every shared item before others arrive.", "Shout through the performance so no one can hear."], "A", "Following instructions and considering others supports respectful participation."),
    ("information contrast", "A festival page says the parade is free, but food stalls require payment. Which statement is correct?", ["Visitors can watch the parade without paying, but food may cost money.", "Visitors must pay to see the parade and food is always free.", "Neither the parade nor the stalls are part of the event.", "The page says every activity has the same price."], "A", "The contrast separates the free parade from paid food stalls."),
    ("invitation response", "A friend invites you to a local festival on Sunday, but you have a family appointment. Which reply is appropriate?", ["Thanks for inviting me, but I cannot join on Sunday. I hope you have fun.", "Your festival is meaningless, so I will never answer.", "I will attend every festival without checking the date.", "Please cancel your family appointment for me."], "A", "The reply politely thanks the friend, declines, and gives a clear limitation."),
    ("festival comparison", "One domestic festival centers on lantern displays at night, while another centers on boat races by day. What is a useful comparison?", ["Their main activities and typical times are different.", "Both festivals must be the same event because they are local.", "Neither festival includes a public activity.", "The comparison should ignore all dates and activities."], "A", "Comparing activity and time identifies a meaningful difference without judging either tradition."),
    ("integrated introduction", "A student introduces a local festival to visitors. Which plan is most complete?", ["Give its name and time, explain one activity and its meaning, describe respectful behavior, and invite questions.", "List only a food name and say nothing about the festival.", "Copy a foreign festival description and change the title.", "Give an exact schedule but no cultural explanation or audience support."], "A", "A good introduction combines factual details, cultural meaning, respectful participation, and communication with visitors."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取國內節慶介紹的日期、活動、文化意義、受眾、禮儀與資料整合能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以節慶公告與文化短文測量日期活動、主旨、文化實踐、受眾、合宜行為與口筆語介紹；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the festival situation and identify the cultural-reading target: {topic}.",
        "Mark the festival name, date, activity, purpose, people, value, behavior expectation, contrast, and audience.",
        f"Choose the interpretation or response supported by the festival information and respectful cultural context; the correct answer is {answer}.",
        f"Explain how the details support the selected answer: {explanation}",
        "Reread the description and check that the answer distinguishes stated tradition from an invented stereotype or unrelated activity.",
    ]
    return {"id": f"question-english-performance-8-iv-1-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-8-iv-1"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies domestic-festival information, cultural meaning, dates, activities, audience, and respectful participation only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; festival contexts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-8-iv-1", "examPatternRefs": refs, "solutionStrategy": "Locate the festival facts first, connect each activity with its cultural purpose and audience, then answer using respectful, evidence-based interpretation.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-8-iv-1-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
