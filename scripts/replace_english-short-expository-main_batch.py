"""獨立替換 1-Ⅳ-7 簡短說明敘述情境主旨題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/performance-1-iv-7.json").read_text())["source"]["url"]
LESSON = "lesson-english-performance-1-iv-7"
KNOWLEDGE = "kg-english-performance-1-iv-7"
ITEMS = [
    ("Read: 'The school placed water stations near the sports field. Students now refill bottles instead of buying new ones.' What is the main idea?", ["Water stations can reduce disposable bottle use.", "Sports fields cannot have water.", "Students stopped drinking water.", "New bottles are required at school."], "A", "The passage connects refill stations with using fewer disposable bottles."),
    ("Read: 'Bees visit many flowers and carry pollen between them. This helps some plants produce seeds.' What is the passage mainly explaining?", ["How bees can help plants reproduce.", "Why flowers cannot make seeds.", "How to build a beehive from paper.", "Why all insects avoid flowers."], "A", "The passage explains the relationship between bee visits, pollen, and plant seeds."),
    ("Read: 'Lina keeps a small notebook of new words. Each evening she writes one sentence with three of them.' What is the main point?", ["Using new words in sentences supports learning.", "Notebooks make words disappear.", "Lina never studies English.", "Three sentences are always too many."], "A", "The routine connects recording vocabulary with meaningful practice."),
    ("Read: 'The town added trees along a busy street. Their shade makes the sidewalk cooler on sunny afternoons.' What does the text mainly tell us?", ["Trees can make a sidewalk more comfortable in the sun.", "Sidewalks grow like trees.", "Sunny afternoons are always cold.", "The town removed every tree."], "A", "The text states that tree shade cools the sidewalk."),
    ("Read: 'Before the trip, the class checked the weather and packed rain gear. A shower arrived in the afternoon, but the activity continued.' What is the main idea?", ["Preparation helped the class continue despite rain.", "The class canceled the trip before leaving.", "Rain gear caused the shower.", "The weather was never checked."], "A", "Checking conditions and packing suitable gear allowed the activity to continue."),
    ("Read: 'A museum uses labels with large print and clear colors. Visitors can read the information more easily.' What is the purpose of the design?", ["To make museum information easier to read.", "To hide every museum object.", "To make visitors leave quickly.", "To replace all exhibits with labels."], "A", "Large print and clear colors improve access to the information."),
    ("Read: 'The farmer covers the soil with dry leaves. The leaves help keep moisture in the ground.' What is the passage mainly about?", ["Using leaves to help soil retain moisture.", "Leaves always make soil dry.", "Farmers should remove all soil.", "Moisture cannot stay in the ground."], "A", "The passage explains the effect of dry leaves on soil moisture."),
    ("Read: 'When the library sends a reminder two days before a book is due, more students return books on time.' What relationship is described?", ["A reminder is associated with more on-time returns.", "Books are returned before they are borrowed.", "Reminders prevent students from reading.", "The library has no due dates."], "A", "The reported change links reminders with timely returns."),
    ("Read: 'The cooking group divides tasks: one person washes vegetables, another cuts them, and a third prepares the pan.' What is the main point?", ["Dividing tasks helps the group prepare food.", "Only one person can cook.", "Vegetables should never be washed.", "The pan prepares itself."], "A", "The text shows how assigned tasks support group cooking."),
    ("Read: 'A short guide explains how to save a file: choose a folder, type a name, and click Save.' What is the guide mainly for?", ["Teaching the steps for saving a file.", "Describing a folder's color.", "Explaining why files cannot be named.", "Asking readers to close the computer first."], "A", "The guide presents a sequence for saving a file."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-performance-1-iv-7-{i}.json"
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
            "sourceLocator": "114 年國中教育會考英語科閱讀公開試題；研究簡短說明與敘述情境的主旨、因果、目的、步驟與資訊關係判讀；課綱：" + CURRICULUM,
            "authoringNote": "自編短篇說明／敘述文字與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 short-expository-main questions")

if __name__ == "__main__":
    main()
