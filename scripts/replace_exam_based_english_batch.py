#!/usr/bin/env python3
"""Replace one English grammar lesson with independently adapted public-exam-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-english-content-ad-iv-1"
KID = "kg-english-content-ad-iv-1"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"

rows = [
    ("There are many books on the desk, ________?", ["aren't there", "are they", "isn't it", "don't they"], "A", "The subject is plural books, and the statement is affirmative, so the tag is aren't there.", "第22題題型改編"),
    ("Kevin forgot to bring his umbrella, ________?", ["did he", "didn't he", "does he", "will he"], "B", "The main verb is past-tense forgot; an affirmative statement takes the negative tag didn't he.", "第23題題型改編"),
    ("Mia enjoys both drawing and singing, and ________ her brother.", ["does", "is", "has", "do"], "A", "The main verb is enjoys in the present simple, so the agreeing expression is so does her brother.", "第29題題型改編"),
    ("Leo doesn't like spicy food, and his sister doesn't, ________.", ["too", "either", "also", "neither"], "B", "Either follows a negative statement to mean that the sister also does not like it.", "第30題題型改編"),
    ("The children ________ in the park when it started to rain.", ["play", "are playing", "were playing", "played"], "C", "The ongoing action in the past uses were playing, while started marks the interrupting event.", "第31題題型改編"),
    ("You can spend the afternoon either ________ a bike or reading a novel.", ["ride", "riding", "to ride", "rides"], "B", "Either...or... joins parallel forms; reading is a gerund, so riding is required.", "第32題題型改編"),
    ("The box is too heavy for Nina ________ alone.", ["carry", "carrying", "to carry", "carried"], "C", "The pattern too...for + person + to V is used, so to carry is correct.", "第34題題型改編"),
    ("The new library is not only bright ________ also quiet.", ["and", "but", "or", "so"], "B", "The fixed correlative conjunction is not only...but also....", "第28題題型改編"),
    ("The lights were off, so we could ________ see the path.", ["hardly", "already", "usually", "nearly"], "A", "Hardly means almost not and fits the meaning that the path was difficult to see.", "第24題題型改編"),
    ("The science show was interesting, ________?", ["was it", "wasn't it", "did it", "doesn't it"], "B", "The be verb was is repeated in the tag, and an affirmative statement takes wasn't it.", "第27題題型改編"),
]

for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "english" / f"question-english-content-ad-iv-1-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"高雄市立鹽埕國中 114 學年度第 2 學期三年級第 1 次段考英文科；{locator}；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} English questions")
