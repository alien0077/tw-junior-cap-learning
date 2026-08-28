#!/usr/bin/env python3
"""Replace the song/rhyme/rhythm template set with independently authored items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-english-performance-1-iv-10"
KID = "kg-english-performance-1-iv-10"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"

rows = [
    ("Which pair of words rhymes?", ["light / night", "cat / cut", "rain / run", "seat / set"], "A", "Light and night end with the same sound, so they rhyme."),
    ("Which word has two syllables?", ["table", "book", "school", "green"], "A", "Table is pronounced ta-ble, with two syllables; the other choices have one syllable."),
    ("In the word “TAble,” which syllable is stressed?", ["The first syllable: TA.", "The second syllable: ble.", "Both syllables are always equally stressed.", "The word has no syllable."], "A", "In the common pronunciation of table, the first syllable receives the main stress."),
    ("Which word best completes the original rhyme? “We play outside every ____.”", ["day", "book", "fish", "chair"], "A", "Day rhymes with play, so it completes the short original rhyme."),
    ("How many syllables are in “banana”?", ["Three", "One", "Two", "Four"], "A", "Banana is commonly pronounced ba-na-na, so it has three syllables."),
    ("Which line has the clearest repeated beginning sound?", ["Bright birds bring blue berries.", "The dog runs home.", "A child opens a door.", "We read after lunch."], "A", "Bright, birds, bring, and blue begin with the /b/ sound, creating alliteration."),
    ("A class reads “Walk to the park, walk to the park” with the same beat twice. What does this repetition mainly create?", ["A regular rhythm that is easy to follow", "A change in the story's setting", "A list of unrelated characters", "A completely silent reading"], "A", "Repeating the same phrase and beat creates a regular rhythm that helps listeners follow along."),
    ("When performing an original English rhyme aloud, which action best helps listeners hear the rhythm?", ["Keep a steady beat and stress the important words", "Read every word at a random speed", "Whisper only the final word", "Stop after every letter"], "A", "A steady beat and clear stress make the rhythm and meaning easier for listeners to hear."),
    ("Which pair has the same ending sound in ordinary pronunciation?", ["cake / lake", "head / hide", "moon / man", "play / please"], "A", "Cake and lake share the ending sound /eɪk/, so they form a rhyming pair."),
    ("A poem is difficult to chant because each line has very different timing. What is the best revision?", ["Adjust the wording so the lines have a more regular beat", "Add unrelated facts to every line", "Remove all verbs from the poem", "Change every word into a proper name"], "A", "More regular timing makes a chant easier to perform and helps the audience follow its rhythm."),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "english" / f"question-english-performance-1-iv-10-{index}.json"
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
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": "高雄市立鹽埕國中九年級英文段考公開題本；歌謠韻文節奏、音節、押韻與口語表現能力方向之獨立改編；非原題或歌詞重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} public-school English rhythm/rhyme questions")
