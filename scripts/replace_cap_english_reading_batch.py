#!/usr/bin/env python3
"""Replace one English story-reading lesson with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-english-content-ae-iv-6"
KID = "kg-english-content-ae-iv-6"
SOURCE = "https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("Mia found a kitten under the stairs. It was wet and shaking, so she wrapped it in a towel and took it to a nearby animal clinic. What did Mia do first after finding the kitten?", ["She bought it a toy.", "She wrapped it in a towel.", "She took it to school.", "She left it under the stairs."], "B", "The passage says the kitten was first wrapped in a towel before Mia took it to the clinic.", "第20至21題故事理解題型改編"),
    ("Mia found a kitten under the stairs. It was wet and shaking, so she wrapped it in a towel and took it to a nearby animal clinic. Why did Mia take the kitten to the clinic?", ["Because it was wet and shaking.", "Because it could already run fast.", "Because it belonged to the clinic.", "Because she wanted to buy a bicycle."], "A", "The kitten was wet and shaking, which explains why Mia took it for help.", "第20至21題故事理解題型改編"),
    ("Tom practiced the violin every afternoon. At first, his neighbors complained about the noise. After Tom learned to play more smoothly, they began to enjoy the music. What changed in the story?", ["Tom stopped going home.", "The neighbors moved away.", "Tom's playing improved.", "The violin was lost."], "C", "The neighbors changed their opinion after Tom learned to play more smoothly.", "第26至28題人物事件理解題型改編"),
    ("Tom practiced the violin every afternoon. At first, his neighbors complained about the noise. After Tom learned to play more smoothly, they began to enjoy the music. How did the neighbors feel at first?", ["They were worried about a storm.", "They were unhappy about the noise.", "They were excited about a concert.", "They were proud of Tom's prize."], "B", "The first sentence says the neighbors complained about the noise.", "第26至28題人物事件理解題型改編"),
    ("A school garden had no flowers in March. The students planted seeds, watered them daily, and put signs beside each row. By May, the garden was colorful. What was the main reason the garden changed?", ["The students cared for the plants.", "The signs made flowers grow.", "The garden was moved indoors.", "The students stopped watering the seeds."], "A", "Planting and watering were the actions that led to the garden becoming colorful.", "第20至21題事件與結果題型改編"),
    ("A school garden had no flowers in March. The students planted seeds, watered them daily, and put signs beside each row. By May, the garden was colorful. When was the garden colorful?", ["In January.", "In March.", "In April.", "In May."], "D", "The passage states that the garden was colorful by May.", "第20至21題時間線理解題型改編"),
    ("Sara missed the bus because she could not find her keys. Her brother helped her look for them, and they found the keys inside a book. Sara then walked to the station. Why did Sara miss the bus?", ["She was reading at the station.", "She could not find her keys.", "Her brother took the bus.", "The station was closed."], "B", "The first sentence directly gives the reason: she could not find her keys.", "第20至21題原因理解題型改編"),
    ("Sara missed the bus because she could not find her keys. Her brother helped her look for them, and they found the keys inside a book. Sara then walked to the station. Where were the keys?", ["Inside a book.", "Under the bus.", "At the station.", "In her brother's bag."], "A", "The passage says that Sara and her brother found the keys inside a book.", "第20至21題細節理解題型改編"),
    ("The school announced a poster contest. Leo wanted to win, but he shared his best idea with Amy. Amy added a clear title, and Leo drew the picture. Their poster won first prize. Why did their poster win?", ["They worked together effectively.", "Leo refused to share his idea.", "Amy did all the work alone.", "The contest was canceled."], "A", "Leo and Amy combined their contributions, and their poster won first prize.", "第26至28題主旨與事件關係題型改編"),
    ("The school announced a poster contest. Leo wanted to win, but he shared his best idea with Amy. Amy added a clear title, and Leo drew the picture. Their poster won first prize. What did Leo do?", ["He added the title.", "He drew the picture.", "He canceled the contest.", "He hid the poster."], "B", "The final sentence about the picture identifies Leo's contribution.", "第26至28題人物行動理解題型改編"),
]

for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "english" / f"question-english-content-ae-iv-6-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考英語科閱讀；{locator}；官方答案表：{ANSWER}；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style English reading questions")
