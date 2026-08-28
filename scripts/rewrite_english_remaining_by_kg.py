#!/usr/bin/env python3
"""Author remaining English draft questions from each lesson's KG ability.

Public CAP and school exams inform the ability level only.  Items are newly
authored and remain draft until the AI/Terra content review is complete.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-08-29"
KEEP = {
    "lesson-english-content-ac",
    "lesson-english-content-ac-iv-1",
    "lesson-english-content-ac-iv-2",
    "lesson-english-content-ac-iv-3",
    "lesson-english-content-ae-iv-1",
}


def pick(seed: str, values: list[str]) -> str:
    return values[int(hashlib.sha256(seed.encode()).hexdigest()[:12], 16) % len(values)]


def number(seed: str, maximum: int, offset: int = 0) -> int:
    return int(hashlib.sha256(seed.encode()).hexdigest()[:12], 16) % maximum + offset


def options(values: list[str]) -> list[dict[str, str]]:
    return [{"id": chr(65 + i), "text": value} for i, value in enumerate(values)]


def category(topic: str, lesson_id: str) -> str:
    text = f"{topic} {lesson_id}".lower()
    if any(x in text for x in ("文法", "句型", "句構", "grammar", "sentence")):
        return "grammar"
    if any(x in text for x in ("字詞", "字彙", "1200", "拼讀", "字母", "vocabulary")):
        return "vocabulary"
    if any(x in text for x in ("標示", "廣播", "表格", "圖表", "sign", "broadcast")):
        return "information"
    if any(x in text for x in ("故事", "文章", "閱讀", "篇章", "narrative", "reading")):
        return "reading"
    if any(x in text for x in ("節慶", "文化", "世界觀", "禮儀", "culture", "festival")):
        return "culture"
    if any(x in text for x in ("討論", "溝通", "問答", "對話", "短劇", "communication")):
        return "communication"
    return "strategy"


def rewrite(data: dict, topic: str, question_number: int) -> None:
    seed = data["id"]
    short_topic = topic.replace("：", "／")
    name = pick(seed + "-name", ["Mia", "Noah", "Lina", "Evan", "Sara", "Owen", "Ivy", "Leo"])
    place = pick(seed + "-place", ["the library", "the science room", "the art room", "the bus stop", "the town museum", "the sports center"])
    n = 2 + number(seed + "-n", 8)
    kind = category(topic, data["lessonId"])
    if kind == "grammar":
        verb = pick(seed + "-verb", ["finish", "visit", "prepare", "carry", "write", "clean"])
        correct = f"{name} has {verb}ed the {short_topic} task."
        prompt = f"For the「{short_topic}」practice, choose the grammatically correct sentence (question {question_number})."
        values = [correct, f"{name} have {verb}ed the {short_topic} task.", f"{name} {verb}ing has the {short_topic} task.", f"{name} has {verb} the {short_topic} task."]
        explanation = "A singular subject such as a person's name takes has; the past participle follows has."
    elif kind == "vocabulary":
        words = [("arrival", "the act of reaching a place"), ("careful", "taking care to avoid danger"), ("distant", "far away"), ("valuable", "worth a lot"), ("improve", "make something better"), ("ordinary", "usual or common"), ("instead", "in place of another choice"), ("reduce", "make smaller or less"), ("notice", "a short message for people to read"), ("borrow", "use something and return it later"), ("crowded", "full of people"), ("repair", "fix something damaged"), ("ancient", "very old"), ("journey", "a trip from one place to another"), ("patient", "calmly willing to wait"), ("discover", "find something for the first time"), ("quiet", "making little noise"), ("protect", "keep someone or something safe"), ("delicious", "pleasant to taste"), ("prepare", "get something ready")]
        word, meaning = words[(question_number - 1 + number(seed + "-word", len(words))) % len(words)]
        prompt = f"In the「{short_topic}」practice, what does “{word}” mean in question {question_number}?"
        values = [f'In the {short_topic} task, “{word}” means {meaning}.', f'In the {short_topic} task, “{word}” means a place where people wait for {place}.', f'In the {short_topic} task, “{word}” means a tool used to measure {n + question_number} minutes.', f'In the {short_topic} task, “{word}” means a person who teaches at {place}.']
        explanation = f"“{word}” means {meaning}."
    elif kind == "information":
        item = pick(seed + "-item", ["Please use the north entrance.", "The talk begins at 2:30.", "Bring one reusable bottle.", "Room 204 is closed today.", "The bus leaves after lunch", "Keep the walkway clear."])
        if "entrance" in item:
            correct = "Visitors should enter from the north side."
            wrong = ["Visitors should climb to the roof.", "Visitors should wait in the parking office.", "Visitors should leave through the river."]
        elif "begins" in item:
            correct = "The talk starts at 2:30."
            wrong = ["The talk ends at 2:30.", "The talk is held at the bus stop.", "The talk is cancelled every day."]
        elif "bottle" in item:
            correct = "A reusable bottle is required."
            wrong = ["A new desk is required.", "Food is required for entry.", "Visitors must bring a ticket for the roof."]
        elif "closed" in item:
            correct = "Room 204 cannot be used today."
            wrong = ["Room 204 opens at midnight.", "Room 204 is the bus stop.", "Room 204 is outside the building."]
        elif "bus" in item:
            correct = "The bus leaves after lunch."
            wrong = ["The bus leaves before breakfast.", "The bus is a classroom.", "The bus never has a departure time."]
        else:
            correct = "People should keep the walkway clear."
            wrong = ["People should block the walkway.", "People should sleep on the walkway.", "People should move the walkway to the roof."]
        prompt = f"Read this「{short_topic}」notice for {place}, item {question_number}: “{item}” What does it tell people?"
        values = [f"For item {question_number} in the {short_topic} notice, {correct}", f"For item {question_number} in the {short_topic} notice, {wrong[0]}", f"For item {question_number} in the {short_topic} notice, {wrong[1]}", f"For item {question_number} in the {short_topic} notice, {wrong[2]}"]
        explanation = "The answer restates the information in the notice without changing its meaning."
    elif kind == "reading":
        activity = pick(seed + "-activity", ["visited a small museum", "planted herbs behind school", "made a map of the neighborhood", "practiced a song for the class"])
        prompt = f"Read the「{short_topic}」text for day {question_number}: “{name} and two classmates {activity}. They recorded the result and shared it after lunch.” What is the main idea?"
        correct = f"On day {question_number}, the students completed an activity and reported what they learned in the {short_topic} task."
        values = [correct, f"On day {question_number}, the students stayed home and recorded nothing for the {short_topic} task.", f"On day {question_number}, the students cancelled lunch before visiting {place}.", f"On day {question_number}, the students bought a new bus for the {short_topic} task."]
        explanation = "The main idea includes the students' activity, record, and sharing of results."
    elif kind == "culture":
        custom = pick(seed + "-custom", ["greeting", "gift giving", "festival meals", "waiting in line", "shared spaces"])
        season = ["spring", "summer", "autumn", "winter", "a rainy day", "a school holiday", "a community event", "a family visit", "a public ceremony", "a market day"][question_number - 1]
        prompt = f"In the「{short_topic}」lesson, which action shows respect when people have different customs about {custom} during {season}?"
        values = [f"In question {question_number}, ask politely and follow the local rule about {custom} during {season} in the {short_topic} lesson.", f"In question {question_number}, say every custom about {custom} during {season} in the {short_topic} lesson must be exactly the same as mine.", f"In question {question_number}, ignore the people involved in {custom} during {season} in the {short_topic} lesson.", f"In question {question_number}, laugh at a different way of handling {custom} during {season} in the {short_topic} lesson."]
        explanation = "Respect means learning the local practice, asking politely, and avoiding unfair judgment."
    elif kind == "communication":
        need = pick(seed + "-need", ["directions", "a pencil", "help with the task", "permission to join", "the meeting time"])
        time = f"{8 + question_number}:00"
        prompt = f"A: “Excuse me, could you help me with {need} at {place}?” B: “___” (「{short_topic}」practice, {time})"
        values = [f"Of course. I can help you with {need} at {place} in the {short_topic} practice.", f"It is under the blue chair at {place} in the {short_topic} practice.", f"I was fourteen at {place} last year in the {short_topic} practice.", f"No, the weather at {place} is sunny in the {short_topic} practice."]
        explanation = f"The first answer directly accepts the request and matches the meaning of the question about {short_topic}, item {question_number}."
    else:
        prompt = f"For a「{short_topic}」task, what is the best way to prepare question {question_number}?"
        values = [f"Read the instructions, identify the evidence, and explain the answer about {short_topic}.", f"Choose an answer before reading any information about {short_topic}.", f"Copy a classmate's response without checking {short_topic}.", f"Ignore the evidence and use only a guess about {short_topic}."]
        explanation = "A reliable learning strategy uses the instructions and evidence before explaining a conclusion."
    data.update({"prompt": prompt, "options": options(values), "answer": {"value": "A", "explanation": f"{explanation} This item targets {short_topic}, question {question_number}."}, "reviewStatus": "draft", "updatedAt": TODAY})


def main() -> None:
    graph = json.loads((ROOT / "knowledge/english/foundational-graph.json").read_text(encoding="utf-8"))
    labels = {node["id"]: node.get("label", node["id"]) for node in graph["nodes"]}
    changed = 0
    for path in sorted((ROOT / "questions/english").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("reviewStatus") != "draft" or data.get("lessonId") in KEEP:
            continue
        question_number = int(re.search(r"-(\d+)$", data["id"]).group(1))
        topic = labels.get(data["knowledgeIds"][0], data["knowledgeIds"][0])
        rewrite(data, topic, question_number)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    print(f"rewrote remaining English questions by KG: {changed}")


if __name__ == "__main__":
    main()
