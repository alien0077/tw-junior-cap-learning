import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "story elements, narrative structure, and evidence"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "characters, setting, conflict, and point of view"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "narrative clues, symbolism, and outcome"),
]

DATA = [
    ("character", "In a story, Jun secretly repairs the old community clock because he wants younger children to enjoy the town square. Who is the main character?", ["Jun", "The younger children", "The town square", "The clock"], "A", "Jun performs the central actions and has the stated goal."),
    ("setting", "The story begins on a foggy morning at a small harbor where fishing boats are leaving. Which detail is part of the setting?", ["A foggy morning at a small harbor", "The hero's final decision", "A promise made next year", "The solution to a school puzzle"], "A", "Setting includes the time and place in which the events occur."),
    ("conflict", "A girl wants to enter a singing contest, but she is afraid of forgetting the lyrics on stage. What is her main conflict?", ["Her goal conflicts with her fear of making a mistake.", "She has already won and has no decision to make.", "The contest is about repairing a bridge.", "The audience wants to leave before the song begins."], "A", "The internal fear creates the obstacle to the girl's goal."),
    ("point of view", "The narrator says, 'I hid the letter under my pillow and hoped no one would find it.' Which point of view is used?", ["First person", "Second person instructions", "A newspaper headline only", "A map's point of view"], "A", "The narrator uses I to tell the events from a participant's perspective."),
    ("exposition", "At the beginning, the reader learns that the two brothers live beside a river and have not spoken since an argument. What story element is this?", ["Background information that introduces characters and situation", "The final resolution", "A random setting unrelated to the plot", "The climax after all problems are solved"], "A", "The opening gives character and relationship information needed to understand the later events."),
    ("climax", "After searching all night, the team opens the locked box and discovers the missing evidence. Why can this be the climax?", ["It is the key moment when the central mystery is revealed.", "It occurs before any character or problem is introduced.", "It is only a description of the weather.", "It prevents the story from having any turning point."], "A", "The discovery is the high-tension moment that changes the mystery's direction."),
    ("symbol", "A character carries a cracked compass throughout a story about making difficult choices. What might the compass symbolize?", ["Uncertainty about which direction or decision to take", "A guarantee that every journey is easy", "The character's favorite food", "A rule that no one may travel"], "A", "A compass connected to difficult choices can represent direction and uncertainty."),
    ("character change", "At first, Kai refuses to share his invention. After another student explains how it could help the whole class, Kai opens the design to everyone. What change occurs?", ["Kai becomes more willing to cooperate.", "Kai loses interest in all inventions.", "The class disappears from the story.", "Kai changes the invention into a compass."], "A", "His action changes from keeping the design private to sharing it for a group benefit."),
    ("foreshadowing", "Before the storm arrives, the story mentions dark clouds and birds flying low. What do these details do?", ["They hint that a change in weather may come later.", "They prove the storm happened last year.", "They introduce a new narrator who is a bird.", "They solve the character's conflict immediately."], "A", "The early clues prepare readers for the later storm."),
    ("integrated elements", "A story has a bicycle-race setting, a rival who becomes a teammate, a broken wheel as the obstacle, and a shared finish at the end. Which statement best connects the elements?", ["The obstacle and changed relationship support a theme of cooperation.", "The setting proves the race has no characters.", "The broken wheel is unrelated because the story has no conflict.", "The ending shows the rival remained unchanged and alone."], "A", "The elements work together to move the relationship from rivalry toward cooperation."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取故事要素、敘事結構與證據判讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以故事角色、場景、衝突、觀點、轉折、象徵、伏筆與主題測量敘事要素辨識；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the narrative clue and identify the story element being tested: {topic}.",
        "Locate the exact character, time/place, goal, obstacle, narrator wording, repeated object, early hint, or relationship change in the text.",
        f"Compare the choices with that evidence and select the element or interpretation that fits the story structure; the correct answer is {answer}.",
        f"Explain the narrative evidence: {explanation}",
        "Place the answer back into the story map—beginning, rising problem, turning point, and ending—and check that it does not invent an unsupported event.",
    ]
    return {"id": f"question-english-performance-3-iv-10-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-10"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies narrative-element recognition patterns only and does not reproduce an original question, option, image, or story.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; narrative clues, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-10", "examPatternRefs": refs, "solutionStrategy": "Name the narrative element, point to its exact textual clue, connect it to the plot structure or character change, and reject interpretations that exceed the story evidence.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-10-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
