"""獨立替換 B-Ⅳ-6 圖片描述題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-b-iv-6.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-b-iv-6"
KNOWLEDGE = "kg-english-content-b-iv-6"
ITEMS = [
    ("A picture shows a boy reading under a tree. Which sentence best describes it?", ["The boy is reading under a tree.", "The boy reads under a tree yesterday.", "The boy is a tree.", "The tree is reading a boy."], "A", "The sentence matches the person, action, and place shown in the scene."),
    ("A picture shows three cups on a table and one cup on the floor. Which statement is correct?", ["There are four cups in all.", "There is only one cup.", "All four cups are under the table.", "The table is drinking the cups."], "A", "Three cups plus one cup makes four cups in all."),
    ("A picture shows a woman holding an umbrella while it rains. What is she probably doing?", ["She is protecting herself from the rain.", "She is making the sun rain.", "She is swimming in an umbrella.", "She is holding a cloud."], "A", "An umbrella during rain supports the first description."),
    ("A picture shows a dog in front of a closed gate. Which sentence describes the dog's position?", ["The dog is in front of the gate.", "The dog is inside the gate yesterday.", "The gate is behind the dog never.", "The dog is a gate."], "A", "In front of identifies the dog's position relative to the gate."),
    ("A picture shows two children riding bicycles beside a river. Which sentence is best?", ["Two children are riding bicycles beside a river.", "Two rivers are riding children.", "The children rode no bicycles beside a river.", "The bicycles are children."], "A", "The sentence correctly identifies people, action, number, and location."),
    ("A picture shows a plate with an apple and two bananas. How many pieces of fruit are shown?", ["Three pieces of fruit.", "Two plates of fruit.", "One banana and no apple.", "Four apples."], "A", "One apple plus two bananas equals three pieces of fruit."),
    ("A picture shows a girl who is giving a book to a boy. What is happening?", ["The girl is giving a book to the boy.", "The boy is giving a girl to the book.", "The book is giving the boy.", "The girl gave no book to anyone."], "A", "The sentence correctly states the giver, action, object, and receiver."),
    ("A picture shows a family eating dinner in a bright kitchen. Which detail is supported?", ["They are eating in a kitchen.", "They are sleeping in a dark park.", "The kitchen is eating the family.", "No one is at the table."], "A", "The scene supports eating in a kitchen; the other choices contradict it."),
    ("A picture shows a small cat beside a large box. Which comparison is correct?", ["The cat is smaller than the box.", "The box is smaller than the cat.", "The cat is inside a cloud.", "The box is beside no cat."], "A", "The stated sizes and position support the first comparison."),
    ("A picture shows a man walking toward a bus stop with a backpack. Which sentence best describes his movement?", ["He is walking toward the bus stop.", "He is driving away from the bus stop.", "The bus stop is carrying his backpack.", "He is sitting under the road."], "A", "Walking toward the bus stop matches the action and direction in the scene."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-b-iv-6-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究圖片中的人物、動作、數量、位置、比較與方向描述；課綱：" + CURRICULUM,
            "authoringNote": "自編圖片描述文字情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 picture-description questions")

if __name__ == "__main__":
    main()
