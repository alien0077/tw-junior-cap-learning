"""獨立替換 B-Ⅳ-1 自己、家人、朋友題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-b-iv-1.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-b-iv-1"
KNOWLEDGE = "kg-english-content-b-iv-1"
ITEMS = [
    ("Mia is my mother's daughter. Who is Mia to me?", ["My sister", "My aunt", "My cousin", "My grandmother"], "A", "My mother's daughter is my sister."),
    ("Ben and Leo have the same parents. Ben is older than Leo. Who is Leo?", ["Ben's younger brother", "Ben's uncle", "Ben's father", "Ben's cousin"], "A", "Leo has the same parents as Ben and is younger, so he is Ben's younger brother."),
    ("Amy says, 'I live with my parents and my younger brother.' How many children are in Amy's family?", ["Three", "One", "Two", "Four"], "C", "Amy and her younger brother are the two children in the family."),
    ("David helps his grandfather carry a box. What is David showing?", ["Care for a family member", "Anger at a friend", "Fear of school", "A plan to travel alone"], "A", "Helping his grandfather shows care for a family member."),
    ("Kate and May study together every Friday. Kate says, 'May always listens when I have a problem.' What is May like?", ["A good friend", "A noisy neighbor", "A new teacher", "A distant relative"], "A", "Listening when a friend has a problem is a quality of a good friend."),
    ("Sam's uncle is his mother's brother. What is Sam's uncle to Sam's mother?", ["Her brother", "Her son", "Her father", "Her husband"], "A", "A woman's brother is her brother."),
    ("Ivy is younger than her sister but older than her brother. Who is the youngest?", ["Her brother", "Ivy", "Her sister", "Their mother"], "A", "Ivy is older than her brother, so her brother is the youngest."),
    ("Tom forgot his friend's birthday, so he apologized and made a card. What did Tom do?", ["He took responsibility and repaired the friendship.", "He blamed his friend.", "He refused to talk.", "He invited a stranger."], "A", "Tom apologizes and makes a card to repair the relationship."),
    ("Nina and her cousin live in different cities. They call each other every Sunday. Why do they call?", ["To keep in touch", "To avoid their families", "To cancel school", "To buy a house"], "A", "A regular call helps relatives in different cities keep in touch."),
    ("A student says, 'My best friend is honest and returns things that do not belong to him.' What quality does the student value?", ["Honesty", "Speed", "Silence", "Height"], "A", "Returning another person's belongings shows honesty."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-b-iv-1-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        rotated = options[shift:] + options[:shift]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + j), "text": text} for j, text in enumerate(rotated)]
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["knowledgeIds"] = [KNOWLEDGE]
        data["lessonId"] = LESSON
        data["difficulty"] = "medium"
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": "114 年國中教育會考英語科公開閱讀／生活情境能力方向；課綱：" + CURRICULUM,
            "authoringNote": "自編人物關係與家人朋友情境，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 self-family-friends questions")

if __name__ == "__main__":
    main()
