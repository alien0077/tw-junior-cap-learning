#!/usr/bin/env python3
"""Replace the public-announcement template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-english-performance-1-iv-11"
KID = "kg-english-performance-1-iv-11"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"

rows = [
    ("Announcement: The library will close at 5:30 today for cleaning. What should students do?", ["Leave the library before 5:30.", "Borrow books at 6:00.", "Bring cleaning tools tomorrow.", "Wait outside until midnight."], "A", "The announcement says the library will close at 5:30, so students should leave before then."),
    ("Announcement: Flight 208 to Osaka will leave from Gate 6 instead of Gate 2. What is the main purpose?", ["To tell passengers about a gate change.", "To sell tickets to Osaka.", "To cancel every flight.", "To describe the weather in Osaka."], "A", "The key information is that Flight 208 has moved from Gate 2 to Gate 6."),
    ("Announcement: Please keep your receipt. You can exchange the jacket within seven days. What should the customer keep?", ["The receipt.", "The weather report.", "The train map.", "The store's uniform."], "A", "The announcement directly asks the customer to keep the receipt for an exchange."),
    ("Announcement: The school bus will arrive at the west gate in ten minutes. Where should students wait?", ["At the west gate.", "In the science lab.", "At the east parking lot.", "Inside the cafeteria kitchen."], "A", "The location given in the announcement is the west gate."),
    ("Announcement: Due to heavy rain, the baseball game is postponed until Saturday. When will the game take place?", ["On Saturday.", "Today at noon.", "Tomorrow morning for sure.", "It has already finished."], "A", "Postponed until Saturday means the game is moved to Saturday."),
    ("Announcement: The museum tour starts at 2:00. Visitors who want audio guides should meet at the information desk at 1:50. What time should they meet there?", ["At 1:50.", "At 1:05.", "At 2:50.", "At 3:00."], "A", "The announcement gives the meeting time as 1:50, ten minutes before the tour."),
    ("Announcement: The elevator is out of order. Please use the stairs to reach the third floor. What should visitors use?", ["The stairs.", "The elevator.", "The swimming pool.", "The parking meter."], "A", "Because the elevator is not working, visitors should use the stairs."),
    ("Announcement: A blue wallet was found near the information desk. Please show an ID before claiming it. What must the owner show?", ["An ID.", "A bus ticket.", "A menu.", "A library card from another person."], "A", "The owner must show an ID before claiming the wallet."),
    ("Announcement: Please stand behind the yellow line while the train is entering the station. Why is this rule given?", ["For passengers' safety.", "To make the train arrive earlier.", "To change the train's destination.", "To sell yellow paint."], "A", "Standing behind the line keeps passengers at a safe distance from the arriving train."),
    ("Announcement: The lost-and-found office is on the first floor, beside the main entrance. Where is the office?", ["On the first floor beside the main entrance.", "On the second floor beside the cafeteria.", "Outside the building behind the bus.", "In the basement under the parking lot."], "A", "The announcement gives both the floor and the location beside the main entrance."),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "english" / f"question-english-performance-1-iv-11-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    target = ord(answer_positions[index - 1]) - ord("A")
    rotated = options[1:target + 1] + options[:1] + options[target + 1:]
    answer = answer_positions[index - 1]
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(rotated)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": "高雄市立鹽埕國中九年級英文段考公開題本；公共場所廣播理解與資訊擷取能力方向之獨立改編；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} public-school English announcement questions")
