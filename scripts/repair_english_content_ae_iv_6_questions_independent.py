#!/usr/bin/env python3
"""Independent English Ae-IV-6 story setting, character, event and ending rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ae-iv-6"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "故事人物、時間與事件"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中公開英語段考", "敘事理解、因果與結局"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "短篇故事主旨與細節"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求從故事的時間地點、人物特徵、事件順序、問題、反應與結局建立敘事理解；本題採全新故事片段。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("Story: **At dawn, Omar waited at the quiet harbor with a red map.** What is the setting?", ["A quiet harbor at dawn.", "A noisy classroom at noon.", "A hospital at midnight.", "A mountain school in winter."], "A", "The sentence names both the place harbor and the time dawn.", "分開找地點與時間，再合併成故事背景。", ["Locate the place noun harbor.", "Locate the time expression at dawn.", "Combine them as the setting.", "Choose the quiet harbor at dawn.", "Reject settings not stated in the sentence."]),
    ("Story: **Nora always checks the old bridge before crossing. She carries a small repair kit.** What can readers infer about Nora?", ["She is careful and prepared.", "She dislikes walking.", "She is afraid of every book.", "She never notices problems."], "A", "Checking the bridge and carrying a repair kit show caution and preparation.", "用人物反覆行動與物件推論性格，避免只靠名字猜測。", ["Identify Nora's repeated action.", "Notice the repair kit.", "Connect both clues to a character quality.", "Choose careful and prepared.", "Keep the inference supported by the two details."]),
    ("Story: **The wind blew away Jin's notes before the contest. He asked Mei to help him remember the key points.** What problem does Jin face?", ["He lost his notes.", "He won the contest.", "He found a new bicycle.", "He forgot where the school is."], "A", "The wind blew away the notes, creating the immediate problem Jin needs to solve.", "找出事件造成的損失，再區分問題與後續求助。", ["Read what the wind did.", "Identify the missing object notes.", "Separate the problem from Jin's request.", "Choose lost notes.", "Reject outcomes not described in the passage."]),
    ("Story: **Because the path was icy, the hikers took a longer road. They arrived safely before sunset.** Why did they take a longer road?", ["The original path was icy.", "They wanted to miss sunset.", "The road had no signs.", "They lost their shoes."], "A", "Because introduces the reason: the original path was icy and unsafe.", "看到 because 先找直接原因，再確認結果。", ["Locate the connector Because.", "Read the condition of the path.", "Connect it to the decision to change roads.", "Choose the icy path reason.", "Use arriving safely as the result, not the cause."]),
    ("Story: **Lena found a bird with an injured wing. She called a rescue center and waited nearby.** Which action happens after finding the bird?", ["She called a rescue center.", "She flew to another country.", "She closed the center.", "She forgot the bird immediately."], "A", "The story states that calling the rescue center follows finding the injured bird.", "依事件順序找 next action，不把後續等待和前面行動混淆。", ["Identify the first event finding the bird.", "Read the next sentence.", "Locate the rescue-center action.", "Choose called a rescue center.", "Check that waited nearby happens later."]),
    ("Story: **The robot's battery died during the race. Kai replaced it, and the robot finished the course.** What is the result of Kai's action?", ["The robot finished the course.", "The battery disappeared before the race.", "Kai left the course.", "The race was canceled before starting."], "A", "Replacing the battery allowed the robot to finish the course.", "用 and 連接的前後事件判斷行動造成的結果。", ["Identify the problem battery died.", "Find Kai's response replaced it.", "Read the event after and.", "Choose finished the course.", "Do not replace the stated ending with an invented one."]),
    ("Story: **Mia wanted to win, but she stopped to help a younger runner. At the end, both runners crossed the line together.** What does the ending show?", ["Mia chose to help and shared the success.", "Mia refused to run.", "The race never began.", "The younger runner went home alone."], "A", "Stopping to help and crossing together show that Mia valued helping and they finished together.", "結合人物選擇與結尾畫面，推論故事呈現的結果。", ["Find Mia's original goal.", "Notice the contrast marker but.", "Read the final shared action.", "Choose the helping-and-shared-success interpretation.", "Reject endings that conflict with crossed the line together."]),
    ("Story: **Every evening, the fox watched the empty garden. One night, it found a gate left open and entered.** What changed?", ["The gate became open, giving the fox a way into the garden.", "The garden disappeared.", "The fox stopped watching forever.", "The gate became a river."], "A", "The open gate is the new condition that changes the fox's opportunity to enter.", "比較前後情況，找出促成新事件的關鍵變化。", ["Describe the earlier situation empty garden.", "Locate the new event one night.", "Identify the open gate.", "Connect it to entering.", "Choose the changed condition."]),
    ("Story: **After the storm, the village repaired the bridge together. Children painted a sign that said Welcome Back.** What is the likely ending mood?", ["Hopeful and cooperative.", "Lonely and completely silent.", "Angry at the children.", "Unrelated to the storm."], "A", "Repairing the bridge together and painting a welcoming sign create a hopeful, cooperative ending.", "由群體共同動作與最後象徵判斷故事氣氛。", ["Identify the storm as the earlier difficulty.", "Notice villagers working together.", "Read the children's welcoming sign.", "Infer the ending mood.", "Choose hopeful and cooperative."]),
    ("Story: **At first, Sam could not find the old recipe. He asked his grandmother, who remembered it and wrote it down. Sam then cooked the soup for the family.** What is the best summary?", ["Sam solves a recipe problem with his grandmother's help and cooks soup.", "Sam loses his family after cooking.", "His grandmother refuses to remember anything.", "The soup is never prepared."], "A", "The summary includes the problem, the grandmother's help and the final cooking event.", "摘要要保留問題、關鍵協助與結局，不加入文本沒有的結果。", ["Identify Sam's initial problem.", "Find the grandmother's help.", "Locate the final action cooked soup.", "Combine the three into a short summary.", "Choose the option covering the whole event chain."]),
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
    item = {"id": f"question-english-content-ae-iv-6-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ae-iv-6"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究故事背景、人物、問題、事件順序、因果與結局題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫故事結構題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ae-iv-6-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
