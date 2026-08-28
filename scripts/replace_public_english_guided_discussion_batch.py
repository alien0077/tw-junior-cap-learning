#!/usr/bin/env python3
"""Replace one guided-discussion lesson with independently adapted public-exam-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-english-performance-2-iv-12"
KID = "kg-english-performance-2-iv-12"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"

rows = [
    ("Mia: I think our class should start a recycling plan. Ken: ________", ["I agree. It can reduce waste at school.", "No, I am a student.", "Please close the window.", "I went there yesterday."], "A", "The first speaker gives an opinion, so the suitable response agrees and gives a relevant reason.", "第6至10題基本問答與對話題型改編"),
    ("A: Which activity should we choose for the class trip? B: ________", ["I think visiting the science museum is a good idea.", "Because I was late this morning.", "Yes, I am reading it.", "It is under the desk."], "A", "The question asks which activity to choose, so an opinion about an activity is relevant.", "第6至10題基本問答與對話題型改編"),
    ("Lily: The library should stay open later. What do you think? Amy: ________", ["I agree, because many students study after sports practice.", "Turn left at the corner.", "It was sunny last Sunday.", "I have two notebooks."], "A", "A guided discussion response should state a position and connect it to a reason.", "第6至10題基本問答與對話題型改編"),
    ("Tom: I believe school uniforms are useful. Which response disagrees politely?", ["I see your point, but I think students should have more choices.", "You are stupid.", "I do not understand the question.", "The uniforms are in the closet."], "A", "The response acknowledges the other view and then gives a different opinion politely.", "第13至15題對話理解題型改編"),
    ("A: Why do you support the plan to plant trees? B: ________", ["Because trees can provide shade and help the environment.", "At three o'clock.", "No, it is not a tree.", "I bought a new bag."], "A", "Why asks for a reason; the first option gives a reason related to planting trees.", "第6至10題基本問答與對話題型改編"),
    ("During a group discussion, a student says, 'The survey shows that 18 of 25 students prefer more reading time.' Which reply uses the evidence appropriately?", ["That result suggests many students may support more reading time.", "The number proves every student wants it.", "The survey is useless because I dislike reading.", "We should ignore the numbers and choose randomly."], "A", "The response makes a limited inference from the survey instead of claiming that all students agree.", "第24至25題資料情境理解題型改編"),
    ("A: Could you explain why you chose that answer? B: ________", ["Sure. I chose it because the chart shows a steady increase.", "Yes, I am going to the gym.", "It is my brother's bicycle.", "No, the meeting was yesterday."], "A", "The question asks for an explanation, and the first response refers to evidence in a chart.", "第22至23題對話與理由題型改編"),
    ("Which question is most useful for continuing a discussion about reducing plastic use?", ["What evidence shows that reusable bottles reduce waste?", "What color is your pencil?", "Did you sleep well last night?", "Where did you put my shoes?"], "A", "A useful follow-up question asks for relevant evidence about the discussion topic.", "第22至23題對話與主題延伸題型改編"),
    ("At the end of a discussion, which sentence best summarizes two different opinions?", ["Some students prefer a longer lunch, while others want an earlier dismissal.", "Everyone has exactly the same opinion.", "I forgot what we were discussing.", "The classroom has four windows."], "A", "The sentence accurately presents two contrasting positions without claiming a false consensus.", "第26至28題閱讀理解與觀點整理題型改編"),
    ("Which is the best order for a short class discussion?", ["State the question, share reasons, listen to different views, and summarize.", "Choose an answer first, then ignore all reasons.", "Interrupt everyone and leave before listening.", "Copy a classmate's answer without checking it."], "A", "A guided discussion needs a clear question, reasons, listening, and a final summary.", "第26至28題閱讀理解與事件順序題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "english" / f"question-english-performance-2-iv-12-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    target = ord(answer_positions[index - 1]) - ord("A")
    options = options[1:target + 1] + options[:1] + options[target + 1:]
    answer = answer_positions[index - 1]
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"高雄市立鹽埕國中 114 學年度第 2 學期第 1 次段考英文科；{locator}；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} public-exam-style English discussion questions")
