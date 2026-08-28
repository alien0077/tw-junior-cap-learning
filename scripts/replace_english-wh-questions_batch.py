"""獨立替換 B-Ⅳ-5 人事時地物描述問答題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-b-iv-5.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-b-iv-5"
KNOWLEDGE = "kg-english-content-b-iv-5"
ITEMS = [
    ("A: Who is the girl in the red jacket? B: ___.", ["She is my cousin.", "She is at three o'clock.", "She is in the kitchen.", "She is carrying a jacket."], "A", "Who asks about a person, so a relationship answer fits."),
    ("A: Where did you put the keys? B: ___.", ["They are on the desk.", "They are my brother's.", "They were expensive.", "They open at noon."], "A", "Where asks for a place, and on the desk identifies the location."),
    ("A: When does the movie start? B: ___.", ["At 7:30 p.m.", "At the theater.", "With my sister.", "It is an exciting movie."], "A", "When asks about time, so 7:30 p.m. is the appropriate answer."),
    ("A: What is your father doing? B: ___.", ["He is fixing his bicycle.", "He is in the garage yesterday.", "He is my father.", "He does at six feet."], "A", "What is ... doing? asks for an action in progress."),
    ("A: How can I get to the post office? B: ___.", ["Walk two blocks and turn left.", "It is open on Tuesday.", "My uncle works there.", "I mailed a letter."], "A", "How can I get to ...? asks for directions, and the answer gives steps."),
    ("A: Which bag is yours? B: ___.", ["The small blue one.", "I bought it yesterday.", "It is under the bus.", "My bag is heavy."], "A", "Which asks the listener to identify one item; the color and size distinguish it."),
    ("A: Why is Anna absent today? B: ___.", ["Because she is sick.", "She is in Class 8.", "At the school gate.", "She arrived tomorrow."], "A", "Why asks for a reason, and because she is sick supplies one."),
    ("A: How many students joined the club? B: ___.", ["Twenty-four students.", "For two hours.", "In the music room.", "They joined last year."], "A", "How many asks for a number, so twenty-four students is correct."),
    ("A: What does the new library look like? B: ___.", ["It has large windows and bright tables.", "It opens at eight tomorrow.", "It is next to the gym.", "I borrowed a novel there."], "A", "What does it look like? asks for appearance or features."),
    ("A: Whose notebook is this? B: ___.", ["It is Kevin's.", "It is on the chair.", "It is about science.", "It was written yesterday."], "A", "Whose asks about ownership, and Kevin's identifies the owner."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-b-iv-5-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究 who、where、when、what、how、why 與 whose 問答；課綱：" + CURRICULUM,
            "authoringNote": "自編人事時地物問答情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 wh-question questions")

if __name__ == "__main__":
    main()
