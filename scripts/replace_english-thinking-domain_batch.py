"""獨立替換英文思考能力領域導覽題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-d.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-d"
KNOWLEDGE = "kg-english-content-d"
ITEMS = [
    ("A notice says the library closes at 5:00 p.m., but a student arrives at 5:30 p.m. What can the student infer?", ["The library is probably closed.", "The library must be open all night.", "The notice says the student is a librarian.", "The time has no connection to the notice."], "A", "The arrival is after the stated closing time, so the library is probably closed."),
    ("A chart lists apples, bananas, and oranges by price from low to high. What can a reader do with it?", ["Compare and order the prices.", "Know which fruit tastes best to everyone.", "Prove that all shops use these prices.", "Decide the weather tomorrow."], "A", "The chart supports price comparison and ordering, not taste or universal claims."),
    ("A plant grew faster after it received more light, but no other conditions were recorded. What is a careful conclusion?", ["More light may be related to faster growth, but other factors are unknown.", "Light is the only possible cause.", "All plants always grow faster in any light.", "The plant did not grow."], "A", "The observation suggests a relationship while acknowledging missing factors."),
    ("Which sentence is a fact that could be checked?", ["The school bus arrived at 7:20 this morning.", "The bus is the nicest thing in town.", "Everyone loves riding this bus.", "The bus looks happier than a car."], "A", "An arrival time is an observable claim that can be checked against a record."),
    ("A student has three tasks due on different dates. Which strategy shows classification and ordering?", ["Group tasks by subject and arrange each group by due date.", "Choose the task with the longest title.", "Ignore all dates.", "Put every task in a random order."], "A", "Grouping by subject and ordering by date uses two clear criteria."),
    ("A message says, 'Bring a hat because the outdoor activity will be under strong sun.' What is the implied reason for the hat?", ["It can help protect the person from the sun.", "It will make the activity move indoors.", "It proves that rain is falling.", "It is required for every indoor class."], "A", "The message connects the hat with protection from strong sun."),
    ("Two sources give different numbers for the same event. What should a careful reader do first?", ["Check each source's date, method, and definition of the number.", "Choose the larger number because it sounds impressive.", "Delete both sources.", "Assume numbers never need context."], "A", "Differences may result from timing, method, or definitions, so context should be checked."),
    ("A survey of 20 students finds that 15 prefer reading. Which conclusion is justified?", ["In this survey, 15 of the 20 students preferred reading.", "Every student in the city prefers reading.", "Reading is objectively the best activity.", "No student prefers another activity."], "A", "The conclusion stays within the surveyed group and reported result."),
    ("A recipe says to mix the ingredients before baking. What should happen first?", ["Mix the ingredients.", "Bake the empty bowl.", "Serve the finished cake before mixing.", "Skip every step."], "A", "The instruction gives mixing as the step before baking."),
    ("A claim says a new club improved attendance, but it gives no attendance records. What evidence would best test the claim?", ["Attendance records from before and after the club began.", "A colorful club poster.", "One person's guess.", "The club's name."], "A", "Comparable before-and-after records directly test the attendance claim."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-d-{i}.json"
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
            "sourceLocator": "114 年國中教育會考英語科閱讀公開試題；研究資訊推論、分類排序、因果、事實與意見的閱讀思考能力；課綱：" + CURRICULUM,
            "authoringNote": "自編思考能力情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 thinking-domain questions")

if __name__ == "__main__":
    main()
