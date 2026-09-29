#!/usr/bin/env python3
"""Independent English Ae-IV-1 short text and story rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ae-iv-1"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "短文、對話與基礎理解"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "故事、短文與訊息判讀"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "短文主旨、細節與順序"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求從簡短歌謠、對話、故事及短文找出人物、地點、事件順序、原因和主旨；本題採全新文本。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("Read: **Nina plants a seed. She waters it every morning. After two weeks, a small leaf appears.** What happens first?", ["A leaf appears.", "Nina waters the seed.", "Nina plants a seed.", "Two weeks pass."], "A", "The first sentence says Nina plants a seed, so that is the first event.", "先找時間順序訊號，再依文本句子排列事件。", ["Read the three sentences in order.", "Mark the action in the first sentence.", "Compare it with watering and the leaf.", "Choose plants a seed.", "Check that every later event follows it."]),
    ("In the short story, Leo brings an umbrella because the weather report says rain is coming. Why does Leo bring it?", ["Because he wants to stay dry.", "Because he wants to swim.", "Because he lost his shoes.", "Because the sun is very hot."], "A", "The rain forecast gives the reason, and an umbrella helps Leo stay dry.", "先找 because 或原因線索，再連結物品的功能。", ["Locate the weather clue.", "Identify the object Leo brings.", "Ask what problem it solves.", "Choose staying dry.", "Reject choices that conflict with rain protection."]),
    ("A chant repeats **Step, step, turn!** What is the chant mainly helping children remember?", ["A movement sequence.", "A restaurant menu.", "A family address.", "A weather forecast."], "A", "The repeated action words step and turn describe a simple movement sequence.", "從重複動詞判斷歌謠的任務與訊息，而非只看押韻。", ["Underline the action words.", "Notice the repeated rhythm.", "Combine step and turn as movements.", "Choose movement sequence.", "Check that the other topics have no support in the chant."]),
    ("In a short play, Maya says, **I cannot find my key.** Ben answers, **Look under the chair.** What does Ben do?", ["He gives a possible solution.", "He changes the subject to food.", "He says he lost a book.", "He ends the play."], "A", "Ben responds to Maya's problem with a suggestion for where to look.", "把角色的問題和下一句回應配對，判斷對話功能。", ["Identify Maya's problem.", "Read Ben's suggestion.", "Connect under the chair to finding the key.", "Choose possible solution.", "Reject interpretations not supported by the dialogue."]),
    ("Read: **The little dog is afraid of the thunder. It hides beside its owner until the storm ends.** What is the main idea?", ["The dog seeks safety during a storm.", "The dog enjoys loud music.", "The owner leaves the house.", "The storm lasts forever."], "A", "The two sentences focus on the dog's fear and its choice to stay near the owner during the storm.", "用多句共同線索歸納主旨，不被單一細節帶走。", ["Identify the repeated situation: thunder and storm.", "Notice the dog's feeling afraid.", "Notice its action hiding near the owner.", "Combine them into a main idea.", "Choose the safety-during-storm statement."]),
    ("A poem says **The moon is a lamp above the town.** What comparison does the line make?", ["The moon is compared to a lamp.", "The town is compared to a river.", "A lamp is compared to a cloud.", "The moon is compared to a bicycle."], "A", "The phrase says the moon is like a lamp because both give light in the image.", "找出 is a 的比喻對象，再確認兩者共享的特徵。", ["Locate the two nouns in the line.", "Compare moon and lamp.", "Identify their shared light image.", "Choose moon compared to lamp.", "Ignore objects not present in the poem."]),
    ("In a story, Sara forgets her lunch, and her friend shares a sandwich with her. How does Sara probably feel?", ["Thankful.", "Angry at the sandwich.", "Sleepy because of music.", "Proud of a broken chair."], "A", "A friend sharing food is helpful, so Sara would probably feel thankful; this is an inference from the event.", "由事件推測人物感受，並標記 probably 表示合理推論。", ["Identify Sara's problem.", "Notice the friend's helpful action.", "Ask what feeling usually follows help.", "Choose thankful.", "Keep it as a likely inference, not a directly stated fact."]),
    ("A short dialogue ends with **Everyone laughs and starts cleaning the room.** What does the ending suggest?", ["The problem has been resolved and the group cooperates.", "The group is beginning a race outside.", "Nobody understands the situation.", "The room is becoming darker because of rain."], "A", "Laughter followed by shared cleaning suggests the earlier problem is settled and the group is working together.", "用結尾的共同動作判斷故事結果與人物關係。", ["Read the final actions.", "Identify everyone as a group subject.", "Connect laughter with a resolved mood.", "Connect cleaning with cooperation.", "Choose the resolution-and-cooperation interpretation."]),
    ("In a song, each verse names a different animal and ends with **What can it do?** What structure helps listeners?", ["A repeated question pattern.", "A different story setting in every word.", "A list of prices.", "A formal letter ending."], "A", "Repeating the same question after each animal creates a predictable pattern that helps listeners follow the song.", "觀察每段反覆出現的句型，再判斷它對理解的作用。", ["Compare the endings of the verses.", "Notice the repeated question.", "Identify what changes: the animal.", "Identify what stays: the question pattern.", "Choose repeated question pattern."]),
    ("Read: **Tom wanted to join the game, but he had to finish his chores first. After he finished, he went outside.** Why did Tom wait?", ["He needed to finish his chores.", "He did not like the game.", "The game was inside the house.", "He had already gone outside."], "A", "The text directly states that Tom had to finish his chores before joining the game.", "先找 but 前後的轉折，再確認原因與後續行動。", ["Locate the contrast marker but.", "Identify Tom's wish to join.", "Read the obligation that follows.", "Choose finishing chores as the reason for waiting.", "Check the final sentence confirms the later action."]),
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
    item = {"id": f"question-english-content-ae-iv-1-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ae-iv-1"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究短文、歌謠、短劇故事的順序、主旨、角色、原因與推論題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫簡易篇章文本題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ae-iv-1-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
