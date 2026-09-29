#!/usr/bin/env python3
"""Independent English Ae-IV-5 genre and topic text rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ae-iv-5"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "短文、生活文本與閱讀理解"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "不同文本、主旨與細節"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "文章體裁、訊息與推論"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求辨認日記、通知、說明、人物介紹、經驗敘述等簡易文章的體裁目的、主旨、細節、因果與字詞線索；本題採全新文本。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("Text type: **Bring a hat and water. The walk begins at 8 a.m. Meet outside the school gate.** What kind of text is this?", ["A trip reminder.", "A personal diary.", "A restaurant review.", "A science definition."], "A", "The text lists things to bring, a start time and a meeting place, so it functions as a trip reminder.", "從功能資訊判斷體裁：物品、時間、集合地點通常服務通知或提醒。", ["Find the action readers need to take.", "List the items to bring.", "Locate the time and meeting place.", "Choose trip reminder.", "Reject genres without an instruction or schedule."]),
    ("A short article explains that planting trees gives shade and helps birds find homes. What is its main topic?", ["Ways trees help people and animals.", "How to cook a meal.", "A train's ticket price.", "A family's holiday schedule."], "A", "The two details both describe benefits of trees, so the topic is their helpful effects.", "找出多個細節的共同對象與共同功能，再概括主題。", ["Identify the repeated subject trees.", "Compare the shade and bird-home details.", "Find their shared idea: benefits.", "Choose the main topic.", "Avoid choosing a detail that appears nowhere in the article."]),
    ("Diary entry: **I felt nervous before the speech, but my friends smiled and I spoke clearly. I was proud afterward.** How did the writer feel at the end?", ["Proud.", "Angry.", "Sleepy.", "Lost."], "A", "The final sentence directly says the writer was proud afterward.", "依時間順序找結尾感受，注意 afterward 的位置。", ["Read the feeling before the speech.", "Notice the change after friends' support.", "Locate the final feeling word.", "Choose proud.", "Do not let the earlier nervous feeling replace the ending."]),
    ("Notice: **The swimming pool is closed on Monday for cleaning. It opens again Tuesday morning.** Why is it closed?", ["For cleaning.", "For a birthday party.", "Because the water is frozen.", "Because the staff are traveling."], "A", "The notice directly gives cleaning as the reason for the closure.", "看 for 後的原因片語，再區分原因與重新開放時間。", ["Identify the place swimming pool.", "Find the closure day.", "Locate the phrase for cleaning.", "Choose cleaning as the reason.", "Use Tuesday morning only for the reopening detail."]),
    ("A short biography says Mei moved to a new city, learned to cook local food, and opened a small restaurant. What does the article mainly show?", ["How Mei built a new life through learning and work.", "Why trains are faster than buses.", "How to draw a map.", "What animals live in the forest."], "A", "The three events form a life-change story centered on learning, work and starting a restaurant.", "整合人物的連續事件，不把單一事件當成全文主旨。", ["Track Mei's move, learning and restaurant.", "Find what connects the three events.", "Describe the change in her life.", "Choose the main idea.", "Reject unrelated topics absent from the biography."]),
    ("A recipe text lists **wash the fruit, cut it, and mix it with yogurt**. What is the writer's purpose?", ["To explain how to make a simple snack.", "To tell a mystery story.", "To announce a school election.", "To describe a mountain view."], "A", "The ordered action verbs explain a procedure for making a snack.", "看到連續動作與食材，判斷文章是在說明步驟。", ["Identify the ingredients and actions.", "Notice the order of wash, cut and mix.", "Infer a procedure.", "Choose explaining a snack recipe.", "Reject narrative and announcement purposes."]),
    ("A short report says the town library added evening hours because many students finish activities late. What can readers infer?", ["The new hours may help students visit after their activities.", "Students can no longer use the library.", "The library moved to another town.", "The town canceled all activities."], "A", "The reason for evening hours and the students' late schedules support the likely benefit of later visits.", "由 because 的原因與政策改變推論合理結果，避免過度延伸。", ["Find why evening hours were added.", "Identify who finishes activities late.", "Connect later hours with possible access.", "Choose the supported inference.", "Keep the claim as may help, not a guaranteed result for everyone."]),
    ("A travel blog describes a quiet beach, gives two bus options, and recommends going early. Which detail shows the writer's personal opinion?", ["The beach is quiet.", "There are two bus options.", "The writer recommends going early.", "The beach is near the town."], "A", "A recommendation expresses the writer's judgment, while the other details can be presented as factual information.", "區分可查證資訊與作者建議或評價。", ["List the transport and location details.", "Find the verb recommending an action.", "Identify it as the writer's judgment.", "Choose the recommendation.", "Do not confuse a descriptive fact with an opinion."]),
    ("An email from a club says **We will meet in Room 12 at noon to plan the school fair.** What information is not given?", ["The meeting place.", "The meeting time.", "The purpose.", "The exact number of members attending."], "A", "The email gives Room 12, noon and planning the fair, but it does not state how many members will attend.", "逐項核對問題選項是否能在文本中找到，保留未提供的資訊。", ["Mark Room 12 as the place.", "Mark noon as the time.", "Mark planning the fair as the purpose.", "Search for a number of members.", "Choose the information absent from the email."]),
    ("A compare-and-contrast paragraph says city parks are busy but offer many facilities, while mountain trails are quiet but require more preparation. What is the paragraph's structure?", ["It compares two places by their advantages and needs.", "It gives only one place's history.", "It lists steps for baking bread.", "It tells a joke with no comparison."], "A", "The paragraph presents both city parks and mountain trails and contrasts their features and preparation needs.", "先找兩個比較對象，再找 but 連接的相反特徵。", ["Identify the two places.", "List the feature of each place.", "Notice the contrast marker but.", "Choose the comparison structure.", "Reject genres that do not contain the two-place relationship."]),
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
    item = {"id": f"question-english-content-ae-iv-5-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ae-iv-5"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究通知、日記、人物介紹、食譜、報告、遊記與比較文章的題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫不同體裁主題文章題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ae-iv-5-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
