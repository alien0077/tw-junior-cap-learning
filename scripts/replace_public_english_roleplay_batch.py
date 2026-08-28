#!/usr/bin/env python3
"""Replace the role-play template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-english-performance-2-iv-9"
KID = "kg-english-performance-2-iv-9"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"

rows = [
    ("In a role-play at a café, the customer wants to order soup. Which line is most appropriate?", ["Could I have a bowl of soup, please?", "Where did you go yesterday?", "Please close the library at five.", "I am looking for the train station."], "A", "The first line politely orders soup and fits the café role-play."),
    ("In a role-play, a visitor is lost and wants directions. Which question should the visitor ask?", ["Could you tell me how to get to the museum?", "Would you like some cake?", "What time does the movie end?", "How much is this jacket?"], "A", "The first question asks for directions to a specific place."),
    ("A customer wants to return a shirt because it is too small. Which sentence is the most polite?", ["Excuse me, could I exchange this shirt for a larger one?", "Give me a larger shirt now.", "This shirt is your fault.", "I do not want to speak to anyone."], "A", "Could I exchange... is a polite and useful request for a role-play in a store."),
    ("In a doctor-patient role-play, the patient has had a headache since yesterday. What should the patient say?", ["I have had a headache since yesterday.", "I bought this at the supermarket.", "The bus stops over there.", "Please turn off the museum lights."], "A", "The first sentence clearly gives the doctor the patient's symptom and its duration."),
    ("In a hotel role-play, a guest wants to ask whether breakfast is included. Which question is correct?", ["Is breakfast included in the room price?", "Did breakfast include the room?", "Where did you include the hotel?", "Can breakfast room the price?"], "A", "The first question naturally asks whether breakfast is part of the room price."),
    ("Two students are acting out a disagreement. Which line best keeps the conversation polite?", ["I understand your idea, but I have a different suggestion.", "You are always wrong, so stop talking.", "I will not listen to anyone.", "Your idea is too silly to discuss."], "A", "The first line acknowledges the other idea and introduces a different suggestion respectfully."),
    ("In a role-play at a train station, a passenger missed the train. What should the passenger ask?", ["When is the next train to Tainan?", "How do I cook this rice?", "Which color is your notebook?", "Did you finish the school project last month?"], "A", "The first question fits a passenger asking about the next train and destination."),
    ("A student is role-playing an apology after arriving late. Which sentence is best?", ["I am sorry I am late. The bus was delayed.", "You should wait for me forever.", "I was late, and that is your problem.", "No one needs to explain anything."], "A", "The first sentence contains a polite apology and a brief reason."),
    ("In a job-interview role-play, the interviewer asks about a student's strength. Which answer is most suitable?", ["I am good at organizing tasks and working with others.", "The cafeteria is next to the gym.", "I would like two tickets, please.", "Turn left at the traffic light."], "A", "The first answer describes a personal strength and directly responds to the interview question."),
    ("Before performing a role-play, which preparation is most helpful?", ["Understand the character's goal and practice suitable expressions.", "Memorize random sentences without knowing the situation.", "Speak as quickly as possible so no one can interrupt.", "Ignore the partner's lines and read only one word."], "A", "Knowing the role's goal and practicing expressions helps the performance sound natural and meaningful."),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "english" / f"question-english-performance-2-iv-9-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": "高雄市立鹽埕國中九年級英文段考公開題本；角色扮演、情境語用與對話回應能力方向之獨立改編；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} public-school English role-play questions")
