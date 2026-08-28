"""獨立替換 1-Ⅳ-2 常用教室與生活用語題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/performance-1-iv-2.json").read_text())["source"]["url"]
LESSON = "lesson-english-performance-1-iv-2"
KNOWLEDGE = "kg-english-performance-1-iv-2"
ITEMS = [
    ("A student arrives late. Which sentence is appropriate to say to the teacher?", ["I'm sorry I'm late.", "I am late the classroom.", "Late is a pencil.", "You late me yesterday."], "A", "I'm sorry I'm late is a common polite classroom expression."),
    ("Your friend asks to borrow an eraser. Which response gives permission?", ["Sure. Here you are.", "The eraser is yesterday.", "Borrow is a color.", "No, I am an eraser."], "A", "Sure. Here you are accepts the request and offers the eraser."),
    ("The teacher says, 'Please be quiet.' What should students do?", ["Stop talking and lower their voices.", "Open every window loudly.", "Ask the desk to speak.", "Leave the school without permission."], "A", "Be quiet means stop talking or make very little noise."),
    ("A student does not hear the instruction. Which sentence should the student use?", ["Could you say that again, please?", "Say the classroom again.", "I hear yesterday.", "The instruction is a shoe."], "A", "The sentence politely requests repetition."),
    ("You want to know the location of the restroom in a public building. What should you ask?", ["Excuse me, where is the restroom?", "What restroom are you?", "The restroom is where yesterday.", "I am a location."], "A", "Where is the restroom? asks for the location clearly and politely."),
    ("A friend offers you a snack, but you do not want it. Which response is polite?", ["No, thank you.", "No snack you.", "I thank yesterday no.", "The snack is refusing me."], "A", "No, thank you politely declines an offer."),
    ("The sign says, 'Please wait here.' What does it ask people to do?", ["Stay in this place until it is their turn.", "Run to another building.", "Take the sign home.", "Speak before arriving."], "A", "Wait here means remain at this location for a time."),
    ("A classmate asks, 'Can I use your calculator?' Which answer politely refuses?", ["Sorry, I need it right now.", "Calculator is a window.", "I can yesterday your calculator.", "Use means Tuesday."], "A", "The response gives a polite refusal and a reason."),
    ("You need help finding the school office. Which request is best?", ["Could you show me how to get to the office?", "Show office me yesterday.", "The office is asking me.", "I am a way to school."], "A", "Could you ...? is a polite request for directions."),
    ("A class ends and the teacher says, 'See you tomorrow.' What is a natural reply?", ["See you tomorrow.", "Tomorrow sees me yesterday.", "The class is a reply.", "No, I see a chair."], "A", "See you tomorrow is the natural farewell response."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-performance-1-iv-2-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究課堂與生活中的道歉、請求、允許、拒絕、問路、等待與道別用語；課綱：" + CURRICULUM,
            "authoringNote": "自編常用教室與生活用語情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 classroom-life language questions")

if __name__ == "__main__":
    main()
