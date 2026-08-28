#!/usr/bin/env python3
"""Replace the basic-worldview template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-english-performance-8-iv-5"
KID = "kg-english-performance-8-iv-5"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"

rows = [
    ("An exchange student greets people in a way you do not know. What is the best response?", ["Ask politely about the greeting and respect the answer.", "Laugh and tell everyone it is wrong.", "Refuse to speak to the student.", "Assume every person from that country behaves the same way."], "A", "Asking politely and respecting the answer shows curiosity without judging another culture."),
    ("A class video call includes students in different time zones. What should the class do first?", ["Check everyone's local time before choosing a meeting time.", "Choose a time that is convenient for only one student.", "Tell students in other places to change their clocks.", "Ignore the time difference completely."], "A", "Checking local times helps the class make a fair and practical plan."),
    ("A school poster says, “Bring a reusable bottle to reduce plastic waste.” What is the main idea?", ["A daily action can help protect the environment.", "Plastic waste can never be reduced.", "Students should buy more single-use bottles.", "Only one country has an environment."], "A", "Using a reusable bottle can reduce the number of disposable bottles used."),
    ("A visitor asks why a local festival is held every spring. What is the best way to learn?", ["Read reliable information and ask local people respectfully.", "Make up an answer from the festival's color.", "Say that every festival has the same history.", "Copy an unverified comment without checking it."], "A", "Reliable sources and respectful conversations can explain a festival's history and meaning."),
    ("A menu marks some food as vegetarian. What should a visitor do if the meaning is unclear?", ["Ask the staff what ingredients the dish contains.", "Guess and blame the restaurant later.", "Order every dish without asking.", "Say that all food traditions are identical."], "A", "Asking about ingredients helps the visitor respect dietary choices and avoid misunderstanding."),
    ("Two websites give different numbers about the world's population. What is the best next step?", ["Check the dates, sources, and methods used by both websites.", "Choose the larger number because it looks more important.", "Trust the website with the brightest design.", "Average the numbers without reading the sources."], "A", "Dates, sources, and methods help readers judge why statistics may differ."),
    ("A class discusses a custom that is different from its own. Which sentence shows an open-minded attitude?", ["I would like to understand what this custom means to the people who practice it.", "Our custom is the only normal one.", "Different customs should never be discussed.", "One example proves that everyone in the group agrees."], "A", "The first sentence seeks context and avoids judging a culture by one group's standards."),
    ("A school plans a global-project poster. Which topic best connects local action with a world issue?", ["Saving water at school and explaining why water matters in many regions.", "Listing students' favorite colors only.", "Copying a foreign flag without any explanation.", "Describing a single lunch without a question."], "A", "The first topic connects a local action with a broader environmental concern."),
    ("During an international online meeting, a classmate speaks slowly because English is not their first language. What should you do?", ["Listen patiently and ask for clarification when needed.", "Interrupt and finish every sentence.", "Ignore the classmate's ideas.", "Use difficult words to make the conversation faster."], "A", "Patient listening and respectful clarification support communication across language backgrounds."),
    ("Which action best shows a basic world view when reading news about another country?", ["Compare reliable sources and consider the country's own context.", "Share the headline immediately without reading it.", "Assume one person's experience represents everyone.", "Judge the whole country from one photograph."], "A", "Reliable comparison and attention to local context help avoid stereotypes and overgeneralization."),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "english" / f"question-english-performance-8-iv-5-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": "高雄市立鹽埕國中九年級英文段考公開題本；基本世界觀、跨文化理解與全球議題判讀能力方向之獨立改編；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} public-school English worldview questions")
