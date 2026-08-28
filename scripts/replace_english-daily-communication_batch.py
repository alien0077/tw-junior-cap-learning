"""獨立替換 B-Ⅳ-2 日常溝通字彙句型題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-b-iv-2.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-b-iv-2"
KNOWLEDGE = "kg-english-content-b-iv-2"
ITEMS = [
    ("A: Could you help me carry these books? B: ___.", ["Sure. They look heavy.", "I carried yesterday.", "It is a book.", "No, I am twelve."], "A", "Sure is a natural acceptance of a request for help."),
    ("A: What are you doing after school? B: ___.", ["I am going to the library.", "It was on Monday.", "I do it blue.", "Yes, after school."], "A", "The question asks about a plan, so a destination and activity answer fit."),
    ("The classroom is very dark. Which sentence is the best suggestion?", ["Why don't we turn on the lights?", "Why did lights turn?", "The lights turned yesterday.", "I am a light."], "A", "Why don't we ...? is used to make a suggestion."),
    ("A: I have a headache. B: ___.", ["You should get some rest.", "I have it yesterday.", "The headache is a pencil.", "Do you headache?"], "A", "You should ... gives appropriate advice for a headache."),
    ("Choose the sentence that politely asks for permission to use a phone.", ["May I use your phone for a minute?", "I may phone your minute.", "Use I your phone may.", "Your phone used me."], "A", "May I ...? is a polite way to ask for permission."),
    ("A: How often do you practice basketball? B: ___.", ["Twice a week.", "At the gym yesterday.", "With my blue shoes.", "Because it is round."], "A", "How often asks about frequency, and twice a week answers it."),
    ("Which response best completes: 'Thank you for showing me the way.'", ["You're welcome.", "I show yesterday.", "The way is long.", "Thank you me."], "A", "You're welcome is the conventional response to thanks."),
    ("A: Would you like some tea? B: ___.", ["Yes, please. That sounds nice.", "I like yesterday.", "Tea is on the chair.", "Would is a verb."], "A", "Yes, please accepts an offer politely."),
    ("Choose the best sentence for asking about the price of a notebook.", ["How much is this notebook?", "How many is this notebook?", "How much notebooks are?", "What price do notebook?"], "A", "How much is ...? asks for the price of one item."),
    ("A: I am sorry I broke your ruler. B: ___.", ["That's okay. Please be more careful next time.", "The ruler is sorry.", "I break tomorrow.", "Sorry is a ruler."], "A", "The response accepts the apology and gives a clear, polite reminder."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-b-iv-2-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究日常問答、請求、建議、邀請、頻率與購物溝通能力；課綱：" + CURRICULUM,
            "authoringNote": "自編日常溝通對話與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 daily-communication questions")

if __name__ == "__main__":
    main()
