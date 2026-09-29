import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "international festivals, cultural descriptions, dates, and activities"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "global celebrations, audience, practices, and respectful comparison"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "reading international cultural information and introducing a festival"),
]

DATA = [
    ("festival identification", "A passage describes families lighting lamps, sharing sweets, and celebrating the victory of light over darkness in India. Which festival is it most likely describing?", ["Diwali", "Canada Day", "Oktoberfest", "The Cherry Blossom Festival"], "A", "Lamps, sweets, and the theme of light are strong clues for Diwali."),
    ("activity detail", "A notice about a Mexican celebration includes music, colorful decorations, and a community parade. Which detail is directly stated?", ["A community parade is part of the event", "The event is held only in a laboratory", "Visitors must stay silent all day", "The notice describes a winter examination"], "A", "The parade is the explicit activity in the notice."),
    ("date caution", "A comparison says Thanksgiving is observed on different dates in the United States and Canada. What should a careful reader do?", ["Check the country before stating the date", "Assume every country uses the same date", "Ignore the country and invent a date", "Conclude that neither country observes it"], "A", "The comparison warns that country context matters when reporting a date."),
    ("cultural purpose", "A passage says a harvest festival gives a community time to express thanks and share food. What purpose is emphasized?", ["Gratitude and community sharing", "Private competition with no visitors", "Replacing all meals with games", "Avoiding communication between families"], "A", "Giving thanks and sharing food describe the festival's social purpose."),
    ("audience", "A student introduces a Korean cultural celebration to classmates who have never heard of it. What should the student do first?", ["Give the name, place, and a simple explanation of its main practice", "Assume the classmates already know every detail", "Copy a description of an unrelated holiday", "List difficult words without explaining the event"], "A", "Basic identity and context make an unfamiliar festival accessible to the audience."),
    ("respectful behavior", "You are invited to observe a religious festival in another country. Which action is most respectful?", ["Learn the local expectations and follow the host's guidance", "Touch every ceremonial object without asking", "Laugh at practices that seem unfamiliar", "Insist that the event follow your own customs"], "A", "Respect begins with learning context and following appropriate guidance."),
    ("contrast", "A text says one festival welcomes the spring season, while another marks the end of a fasting period. What is the useful contrast?", ["Their cultural purposes are different", "Both festivals must have identical practices", "Neither festival has a connection to time", "The text proves one culture is better"], "A", "The sentences identify different purposes without judging either tradition."),
    ("interpretation", "A visitor sees people wearing special clothing during a festival. Which conclusion is safest?", ["The clothing may express cultural or ceremonial meaning; read the explanation before judging it", "The clothing proves everyone has the same personal reason", "Special clothing is always a costume for a competition", "The festival has no meaning because clothing is visible"], "A", "The cautious interpretation uses context instead of assuming one universal motive."),
    ("invitation response", "A host invites you to an international festival but explains that one activity is private. Which reply is appropriate?", ["Thank you; I will enjoy observing the public activities and respect the private part.", "I will enter the private activity because every visitor has that right.", "Private customs are meaningless, so I will criticize them.", "I will change the festival schedule for everyone."], "A", "The response accepts the invitation while recognizing the host's boundary."),
    ("integrated introduction", "A student must introduce an overseas festival to a school audience. Which outline is strongest?", ["Name and country → time and purpose → key activity → respectful participation → comparison or question", "Food list only → unrelated sports result → no country or purpose", "Copy a foreign webpage → remove all cultural explanations → present stereotypes", "Give a date without identifying the festival or its people"], "A", "The outline supplies identity, context, practice, respectful behavior, and a way to connect learning."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取國外節慶的來源、日期、活動、文化脈絡、受眾、禮儀與介紹能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以國際節慶短文與公告測量日期、活動、文化目的、受眾、尊重差異、比較與口筆語介紹；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the international-festival situation and identify the cultural target: {topic}.",
        "Mark the country or community, date, activity, purpose, audience, public or private practice, and any comparison clue.",
        f"Choose the interpretation or response supported by the text and respectful cross-cultural reasoning; the correct answer is {answer}.",
        f"Explain how the festival evidence supports the answer without treating one practice as universal: {explanation}",
        "Reread the passage and check that the response distinguishes stated facts from guesses or stereotypes about another culture.",
    ]
    return {"id": f"question-english-performance-8-iv-2-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-8-iv-2"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies international-festival information, cultural context, audience, respectful comparison, and introduction only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; festival contexts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-8-iv-2", "examPatternRefs": refs, "solutionStrategy": "Locate country, purpose, date, and practice, then explain the festival for its audience while checking evidence and avoiding cultural assumptions.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-8-iv-2-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
