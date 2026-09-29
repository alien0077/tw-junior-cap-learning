#!/usr/bin/env python3
"""Independently rewrite English B-IV-5 people/time/place/object descriptions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-b-iv-5"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "who、what、when、where、why、how 情境題型"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "人物、事件描述、疑問詞與細節判讀"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "英文資訊問句、描述與情境應用"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "113-114", "subject": "english", "locator": l, "observedPattern": "公立學校英語評量以 who、what、when、where、why、how 擷取人物、物件、時間、地點、原因與方式，並要求將多項線索整合成完整描述；本題採全新情境。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("At the science fair, **Mina displayed a model volcano beside the blue poster.** Who displayed the model volcano?", ["Mina", "The science fair", "The blue poster", "The model volcano"], "A", "The question asks who, so the answer must be the person doing the displaying: Mina.", "先圈出動作者，再把 who 限定為人物，不被物件或地點干擾。", ["Read the action displayed.", "Ask who performed that action.", "Locate Mina as the subject.", "Choose Mina from the options.", "Check that the answer is a person, not the poster or volcano."]),
    ("The art club made **eight paper lanterns** for the school hallway. What did the club make?", ["Eight paper lanterns", "The hallway", "The art club", "A school bus"], "A", "What asks for the thing made; the passage says the club made eight paper lanterns.", "把 what 對準動作的受詞，並排除做事的人與發生地點。", ["Find the verb made.", "Look immediately for what was made.", "Separate the quantity eight from the object paper lanterns.", "Select eight paper lanterns.", "Verify that hallway is only the destination, not the product."]),
    ("The student council meeting starts **at 4:15 on Thursday**. When does it start?", ["At 4:15 on Thursday", "In the council room", "With the class president", "To plan a festival"], "A", "When asks for time or date, and the sentence provides both 4:15 and Thursday.", "看到 when 就找時刻與日期，不把地點、人物或目的當作時間。", ["Identify the event meeting starts.", "Search for clock and calendar information.", "Combine 4:15 with Thursday.", "Choose the complete time expression.", "Reject room, person, and purpose details."]),
    ("A sign says, **Please leave returned books on the cart near the entrance.** Where should readers leave them?", ["On the cart near the entrance", "In the cafeteria after lunch", "With the librarian at home", "Under the playground slide"], "A", "Where asks for a place; the sign specifies the cart near the entrance.", "先找動作 leave 的地點片語，再保留 near the entrance 這個限定。", ["Locate the action leave returned books.", "Find the phrase answering where.", "Notice both cart and entrance.", "Select the complete place phrase.", "Reject locations that are not written on the sign."]),
    ("Kai brought an umbrella **because the weather report predicted heavy rain**. Why did Kai bring it?", ["Because heavy rain was predicted", "Because the umbrella was a musical instrument", "Because Kai was buying a sandwich", "Because the classroom was empty"], "A", "Because introduces the reason, and the forecast of heavy rain explains the umbrella.", "看到 why 要找 because 後的原因，不能只選同句出現的其他名詞。", ["Identify the action brought an umbrella.", "Read the clause after because.", "Turn the forecast into a concise reason.", "Choose the heavy-rain option.", "Reject unrelated objects, food, and classroom information."]),
    ("The guide showed visitors the old bridge **by pointing to it on a map**. How did the guide show it?", ["By pointing to it on a map", "At the river yesterday", "Because the bridge was old", "With three visitors"], "A", "How asks about manner or method; pointing to the bridge on a map is the stated method.", "將 how 解讀為方式，找 by 或動作方法，而不是時間、原因或人物數量。", ["Find the verb showed.", "Ask what method the guide used.", "Match by pointing to it on a map.", "Choose the method option.", "Reject place, reason, and group-size answers."]),
    ("In the sentence **The narrow wooden bench stood beside the fountain**, which object is described as wooden?", ["The bench", "The fountain", "The sentence", "The sidewalk"], "A", "Wooden modifies bench; narrow also describes the bench, while beside the fountain gives location.", "先找形容詞修飾的名詞，再區分材質、形狀與位置資訊。", ["Locate the adjective wooden.", "Read the noun it directly describes.", "Separate narrow from wooden as two descriptions of one object.", "Choose the bench.", "Do not attach the material adjective to the nearby fountain."]),
    ("Which question best matches the answer **Under the nurse's desk**?", ["Where is the first-aid box?", "Who found the first-aid box?", "Why is the box useful?", "When will the nurse arrive?"], "A", "Under the nurse's desk names a place, so it answers a where question.", "由答案型態反推疑問詞：介系詞地點片語通常回答 where。", ["Classify Under the nurse's desk as a place.", "Match a place answer with where.", "Read each question's requested information.", "Choose Where is the first-aid box?.", "Reject who, why, and when because they ask for different information."]),
    ("Read: **On Monday, Rosa interviewed the coach in the gym about teamwork.** What was the interview about?", ["Teamwork", "Monday", "The gym", "Rosa"], "A", "The phrase about teamwork names the topic, while Monday, the gym, and Rosa answer other questions.", "題目問 about 的主題時，要找 about 後面的內容，不選時間、地點或訪問者。", ["Identify interviewed as the main action.", "Notice the phrase about teamwork.", "Classify Monday as time and gym as place.", "Choose teamwork as the topic.", "Confirm Rosa is the interviewer, not the subject of about."]),
    ("At 6:30, **Ben and his aunt repaired the bicycle in the garage to prepare for a weekend ride**. Which sentence describes the event accurately?", ["Ben and his aunt repaired a bicycle in the garage for a weekend ride.", "Ben repaired a boat alone at noon in the library.", "His aunt bought a bicycle because the garage was closed.", "The weekend ride repaired two people."], "A", "The first option preserves who, what, where, and purpose without changing the time or inventing an event.", "整合描述題要逐項核對人物、動作物件、地點與目的，再排除改動線索的選項。", ["List the people Ben and his aunt.", "List the action and object repaired bicycle.", "Check the place garage.", "Retain the purpose for a weekend ride.", "Choose the only option that preserves all four details."]),
]

assert len(DATA) == 10
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]
for i, (prompt, options, answer, explanation, strategy, steps) in enumerate(DATA, 1):
    target = TARGETS[i - 1]
    if target != answer:
        oi, ti = ord(answer) - 65, ord(target) - 65
        correct = options[oi]
        rest = [v for j, v in enumerate(options) if j != oi]
        options = rest[:ti] + [correct] + rest[ti:]
        answer = target
    item = {"id": f"question-english-content-b-iv-5-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-b-iv-5"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校國中英語段考；只研究人物、物件、時間、地點、原因、方式與整合描述題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫人事時地物描述問答題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-b-iv-5-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
