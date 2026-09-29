import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "short signs, notices, and practical reading"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "public signs, instructions, and contextual meaning"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "everyday notices, safety, and application"),
]

DATA = [
    ("prohibition", "A door sign says 'NO ENTRY.' What does it tell visitors?", ["They must not go inside.", "They should enter quickly.", "They may borrow a key there.", "They should wait for a meal."], "A", "No entry prohibits people from going through the door."),
    ("direction", "A sign with an arrow and the words 'EXIT' points left. Where should people go?", ["To the exit on the left", "To the kitchen on the right", "Back to the ticket office", "Up to a closed roof"], "A", "The arrow and exit label direct people left toward the way out."),
    ("time notice", "A library sign says 'CLOSED 12:00-1:00.' What should a visitor understand?", ["The library is not open during that hour.", "The library opens only at midnight.", "Books must be returned every twelve minutes.", "The visitor may enter without checking the time."], "A", "The time range marks the period when the library is closed."),
    ("safety warning", "A wet-floor sign stands beside a freshly mopped hallway. What should people do?", ["Walk carefully and avoid the wet area if possible.", "Run across the floor to dry it.", "Remove the sign before reading it.", "Sit in the wettest place."], "A", "The warning signals a slipping hazard and calls for careful movement."),
    ("facility label", "A room is labeled 'FIRST AID.' What service is likely available there?", ["Basic help for an injury", "A place to buy movie tickets", "A room for storing bicycles only", "A classroom for advanced algebra"], "A", "First aid refers to immediate basic care for someone who is hurt."),
    ("instruction", "A recycling bin says 'PAPER ONLY.' Which item belongs in it?", ["A clean sheet of paper", "A plastic bottle", "A metal spoon", "A banana peel"], "A", "The sign limits the bin to paper, so a clean paper sheet fits."),
    ("event notice", "A poster says 'Community Clean-up: Meet at Gate B, 8:30 Saturday.' Where and when should volunteers meet?", ["At Gate B at 8:30 on Saturday", "At Gate A at 8:30 on Sunday", "At Gate B at noon on Friday", "At the library after the event"], "A", "The poster supplies the exact meeting place and time."),
    ("service condition", "A café notice says 'Please order at the counter before taking a seat.' What is the required order?", ["Order first, then take a seat.", "Take a seat first and leave before ordering.", "Order only after the café closes.", "Ask another customer to order every meal."], "A", "Before establishes that ordering comes before sitting down."),
    ("symbol and words", "A sign shows a crossed-out phone and says 'SILENT ZONE.' What is the best interpretation?", ["Keep phones silent in this area.", "Use the phone speaker loudly.", "Charge every phone on the wall.", "The area is a shop selling phones."], "A", "The crossed-out phone and silent-zone words require quiet phone use."),
    ("integrated sign reading", "A station board says 'Platform 2: Train to Harbor Town, 10:15. Delayed 10 min.' What should a passenger conclude?", ["The Harbor Town train is at Platform 2 and will be about 10:25.", "The train leaves Platform 10 at 2:15.", "The train has been cancelled without a new time.", "The passenger should go to the airport for a bus."], "A", "The board gives the platform, destination, original time, and ten-minute delay."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取簡易英文標示、公告與生活資訊判讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以標示、公告、時間、地點、安全規則與服務條件測量直接理解及生活應用；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the sign and identify its practical function: {topic}.",
        "Circle the key word, symbol, arrow, number, time, place, restriction, or action that controls the message.",
        f"Match all sign details with the choices and select the action or conclusion supported by the sign; the correct answer is {answer}.",
        f"Explain how the sign supports the interpretation: {explanation}",
        "Put the answer into the real-life situation, then check whether any time, direction, safety rule, or condition has been lost.",
    ]
    return {"id": f"question-english-performance-3-iv-3-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-3"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies short English signs and practical-notice patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; signs, choices, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-3", "examPatternRefs": refs, "solutionStrategy": "Extract the sign's command, prohibition, location, time, or condition, combine words with symbols and numbers, and choose only the action directly supported by all details.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-3-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
