"""獨立替換 1-Ⅳ-8 簡易影片主要內容題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/performance-1-iv-8.json").read_text())["source"]["url"]
LESSON = "lesson-english-performance-1-iv-8"
KNOWLEDGE = "kg-english-performance-1-iv-8"
ITEMS = [
    ("A short video shows students planting herbs, labeling them, and watering them each morning. What is it mainly about?", ["A class caring for a small garden.", "A class repairing bicycles.", "A video about an empty room.", "Students refusing to plant anything."], "A", "The actions in the video all concern planting and caring for a garden."),
    ("A safety video shows a person stopping, looking both ways, and crossing at a marked crosswalk. What is its purpose?", ["To teach a safe way to cross a street.", "To advertise a new bicycle color.", "To explain how to bake bread.", "To show a person avoiding all roads."], "A", "The sequence demonstrates safe street-crossing behavior."),
    ("A video begins with a dirty beach and ends with volunteers collecting bags of trash. What change is shown?", ["The beach becomes cleaner through group effort.", "The beach becomes a classroom.", "The volunteers leave all trash behind.", "The video shows no change."], "A", "The beginning and ending contrast the dirty beach with the cleaned area."),
    ("A cooking video first lists ingredients, then demonstrates three steps, and finally shows the finished dish. What is the main structure?", ["A recipe explained in order.", "A weather report without instructions.", "A story about a missing plate.", "A list of ingredients with no action."], "A", "The video presents ingredients, ordered steps, and the finished dish."),
    ("A student video shows how to sort paper, cans, and bottles into different bins. What is the viewer learning?", ["How to sort recyclables.", "How to paint a classroom.", "Why bins should be hidden.", "How to mix every material together."], "A", "The demonstrations focus on placing recyclable materials in appropriate bins."),
    ("An interview video shows a baker describing an early mistake and how practice improved the bread. What is the main point?", ["Practice helped the baker improve.", "The baker stopped making bread forever.", "The interview is about a bus schedule.", "Mistakes cannot be corrected."], "A", "The speaker connects practice with improvement after an early mistake."),
    ("A travel video shows a map, a train ride, and a museum visit. Which detail is most likely central?", ["The route and visit to the museum.", "The color of the camera.", "A recipe made on the train.", "A school test unrelated to travel."], "A", "The map, train, and museum scenes together describe a trip to the museum."),
    ("A science video shows ice melting near a warm window and explains that heat changes its state. What is the video mainly explaining?", ["How heat can change ice into water.", "Why windows grow ice indoors.", "How to build a window frame.", "Why water cannot change state."], "A", "The observation and explanation concern melting caused by heat."),
    ("A public-service video shows a family preparing an emergency bag with water, food, and a flashlight. What is its purpose?", ["To explain basic emergency preparation.", "To sell a family vacation.", "To show how to decorate a bag.", "To encourage people to remove all supplies."], "A", "The items and actions demonstrate preparing an emergency bag."),
    ("A school video shows a student feeling nervous, practicing a presentation, and speaking confidently at the end. What is the main message?", ["Practice can build confidence.", "Presentations should never be practiced.", "The student cancels school.", "Confidence comes from avoiding every audience."], "A", "The sequence links practice with the student's later confidence."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-performance-1-iv-8-{i}.json"
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
            "sourceLocator": "114 年國中教育會考英語科閱讀公開試題；研究影片的主旨、目的、步驟、前後變化、細節與訊息判讀；課綱：" + CURRICULUM,
            "authoringNote": "自編簡易影片文字情境與選項，未重製公開試題文字、影片、圖片或音檔；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 video-main questions")

if __name__ == "__main__":
    main()
