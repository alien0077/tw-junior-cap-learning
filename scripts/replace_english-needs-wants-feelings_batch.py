"""獨立替換 B-Ⅳ-4 需求、意願、感受題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-b-iv-4.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-b-iv-4"
KNOWLEDGE = "kg-english-content-b-iv-4"
ITEMS = [
    ("A: What do you need for the art class? B: ___.", ["I need some colored paper.", "I feel blue paper.", "I wanted yesterday.", "Need is a class."], "A", "The question asks about a needed item, so colored paper fits."),
    ("A: Would you like to join our study group? B: ___.", ["Yes, I'd love to.", "I joined at three yesterday.", "The group is a table.", "Would is not a feeling."], "A", "Yes, I'd love to politely expresses willingness to join."),
    ("The long bus ride made Kevin tired. How does Kevin feel?", ["He feels tired.", "He feels hungry for a bus.", "He wants a ticket yesterday.", "He needs to be a road."], "A", "The sentence directly states that Kevin is tired."),
    ("A: I want to borrow your umbrella. B: ___.", ["Sure, but please return it tomorrow.", "I am an umbrella yesterday.", "The rain borrowed me.", "Want means Wednesday."], "A", "The reply grants the request and states a return condition."),
    ("Which sentence expresses a strong desire to visit Japan?", ["I would really like to visit Japan.", "I visited Japan never.", "Japan is a suitcase.", "I need visited tomorrow."], "A", "Would really like to ... expresses a strong but polite desire."),
    ("A: Why are you carrying a flashlight? B: ___.", ["I need it because the room may be dark.", "I feel it because it is Tuesday.", "I want yesterday's room.", "The flashlight carries me."], "A", "The answer explains a practical need and its reason."),
    ("Lily received a kind note from her friend and smiled. How did she probably feel?", ["She felt happy.", "She felt like a notebook.", "She wanted to be a note.", "She needed to smile yesterday."], "A", "Smiling after receiving a kind note supports the feeling happy."),
    ("Which request is polite and clearly states a need?", ["Could I have a glass of water, please?", "Give water now, you!", "Water me yesterday.", "I am a glass need."], "A", "Could I ... please? is a polite request for something needed."),
    ("A: Do you want to watch the movie tonight? B: ___.", ["I'd rather stay home because I have a test tomorrow.", "The movie wants a test.", "I watched tonight tomorrow.", "Rather is a theater."], "A", "I'd rather ... clearly expresses a preference and gives a reason."),
    ("Mason lost his wallet, so he looked worried and asked for help. What does he probably need?", ["He needs help finding it.", "He wants to lose another wallet.", "He feels like a question.", "He is a wallet's brother."], "A", "The situation shows that Mason needs help finding the lost wallet."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-b-iv-4-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究需求、意願、偏好與感受的生活情境問答；課綱：" + CURRICULUM,
            "authoringNote": "自編需求意願感受情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 needs-wants-feelings questions")

if __name__ == "__main__":
    main()
