import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "short plays, dialogue purpose, and stage information"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "dramatic scenes, characters, and sequence"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "dialogue meaning, conflict, and outcome"),
]

DATA = [
    ("main idea", "A short play shows two students finding a lost wallet, deciding to ask the office for help, and reuniting it with its owner. What is the play mainly about?", ["Returning a lost wallet through honest cooperation", "Winning a race against the school office", "Hiding a wallet so no one can find it", "Planning a new school uniform"], "A", "The actions and resolution focus on honesty and cooperation to return the wallet."),
    ("character role", "In a scene, Alex holds a clipboard and asks each team member for a report before the presentation. What is Alex's role?", ["The team leader organizing the reports", "A customer ordering lunch", "A visitor lost at a train station", "A musician tuning a guitar"], "A", "The clipboard and requests for reports show an organizing leadership role."),
    ("stage direction", "The script says '[Mia points to the dark window and steps back.]' What does this direction tell the actor?", ["Where Mia looks and how she moves", "What Mia should eat during the scene", "Which character wrote the script", "When the audience should leave the theater"], "A", "The bracketed direction gives a visual action and movement for Mia."),
    ("dialogue purpose", "Sam says, 'If we leave now, we can still catch the last train.' What is Sam trying to do?", ["Persuade the others to leave promptly", "Explain how to repair a train", "Apologize for losing a ticket yesterday", "Announce that the station is closed forever"], "A", "The conditional suggestion is intended to persuade the group to act in time."),
    ("conflict", "In a play, one friend wants to use the money for a class gift, while another wants to save it for an emergency. What is their conflict?", ["They disagree about how the money should be used.", "They cannot remember the name of the school.", "They both want to cancel the play immediately.", "They are arguing about the weather forecast only."], "A", "The opposing plans create a clear decision conflict about the money."),
    ("sequence", "The scene shows: the lights go out, the characters use a phone light, and they discover the fuse switch. What happens second?", ["They use a phone light.", "They discover the fuse switch.", "The lights go out for the first time.", "They leave before noticing the darkness."], "A", "Using the phone light comes after the outage and before discovering the switch."),
    ("emotion", "At the start, Lily speaks softly after making a mistake. At the end, she volunteers to explain the solution to the class. What change does the scene show?", ["Lily becomes more confident.", "Lily becomes less willing to communicate.", "Lily changes into the teacher.", "Lily forgets what the mistake was and leaves the story."], "A", "Her movement from quietness to volunteering indicates growing confidence."),
    ("prop function", "A red scarf is passed from one character to another whenever someone agrees to help. What does the scarf mainly do in the play?", ["It marks the shared promise to help.", "It proves the scene takes place underwater.", "It replaces every character's dialogue.", "It tells the audience the play is about cooking."], "A", "The repeated prop action gives the scarf a shared-help meaning."),
    ("ending", "The final line is, 'We solved it because we listened to one another.' What does the ending emphasize?", ["Listening helped the characters solve the problem.", "The problem was never real.", "Only one character acted without help.", "The characters decided never to speak again."], "A", "The final line directly states the role of listening in the solution."),
    ("integrated drama", "A short play begins with a missing class banner, follows students checking clues, includes a disagreement about blaming someone, and ends when they find it in the art room and apologize. Which summary is best?", ["Students investigate a missing banner, avoid an unfair accusation, find it, and repair trust.", "Students lose the banner, blame a classmate, and refuse to solve the problem.", "The play is mainly a lesson about painting colors with no conflict.", "The banner is found before the students begin looking for it."], "A", "The summary preserves the mystery, ethical conflict, discovery, apology, and repaired relationship."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取簡易短劇、角色、舞台指示與情節判讀能力方向，未複製原題、選項、圖表或劇本。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以短劇對話、角色目標、舞台動作、衝突、順序、道具與結局測量戲劇文本理解；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the dramatic scene and identify the performance-reading target: {topic}.",
        "Mark the character roles, spoken purpose, stage directions, props, conflict, event order, emotional change, and ending line.",
        f"Compare the choices with the whole scene and select the interpretation supported by dialogue and action; the correct answer is {answer}.",
        f"Explain the stage or dialogue evidence: {explanation}",
        "Retell the scene from opening problem to ending and check that the answer does not add a character, action, or motive absent from the script.",
    ]
    return {"id": f"question-english-performance-3-iv-13-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-13"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies short-play comprehension patterns only and does not reproduce an original question, option, image, or script.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; scenes, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-13", "examPatternRefs": refs, "solutionStrategy": "Read dialogue and stage directions together, track each role's goal and action, connect the conflict to the ending, and choose only the interpretation supported by the scene.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-13-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
