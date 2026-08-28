"""獨立替換 B-Ⅳ-7 角色扮演題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-b-iv-7.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-b-iv-7"
KNOWLEDGE = "kg-english-content-b-iv-7"
ITEMS = [
    ("In a role-play, you are a customer who wants a sandwich. What should you say?", ["I'd like a cheese sandwich, please.", "I am a sandwich yesterday.", "The customer is a door.", "Give me cheese because role-play."], "A", "I'd like ... please is a polite customer request."),
    ("You are a visitor asking for the science room. Which line fits the role?", ["Excuse me, could you tell me where the science room is?", "I am science room yesterday.", "Tell the room to walk.", "The visitor is a pencil."], "A", "The line politely asks for the location while staying in the visitor role."),
    ("You play a doctor. A patient says, 'I have a sore throat.' What is an appropriate reply?", ["You should drink warm water and rest.", "Your throat is a bicycle.", "I am sick yesterday.", "The patient should be a doctor."], "A", "The doctor role calls for a simple, relevant piece of advice."),
    ("You play a cashier. A customer gives you $100 for a $65 purchase. What should you say?", ["Here is your change: $35.", "The change is a classroom.", "You buy me $100.", "I am the customer yesterday."], "A", "The cashier should state the correct change: 100 minus 65 equals 35."),
    ("In a lost-and-found role-play, you found a blue water bottle. Which question should you ask?", ["Is this your water bottle?", "Are you a blue bottle?", "Did the bottle find you yesterday?", "Where is your found?"], "A", "Is this your ...? checks ownership naturally in the situation."),
    ("You are a tour guide. The group asks what they can see first. What is a suitable answer?", ["We can visit the museum first.", "The museum is visiting us.", "I saw first tomorrow.", "The group is a ticket."], "A", "The answer gives a clear first destination from the guide's role."),
    ("You play a student apologizing for being late. Which line is best?", ["I'm sorry I'm late. The bus was delayed.", "The bus apologizes to me.", "I am late tomorrow yesterday.", "Sorry is a classroom."], "A", "The line apologizes and gives a plausible reason in the student's role."),
    ("You are a librarian. A student asks where to return a book. What should you say?", ["Please put it in the return box by the desk.", "The book returns the student.", "I returned a desk tomorrow.", "You are a library box."], "A", "The librarian gives a clear instruction about the return location."),
    ("In a restaurant role-play, a guest says the soup is too salty. What is the best response from the server?", ["I'm sorry. I can bring you another bowl.", "The soup is serving the guest.", "You should be salt.", "I brought tomorrow's bowl yesterday."], "A", "The server acknowledges the problem and offers a helpful solution."),
    ("You play a teammate asking for a turn. Which line is appropriate?", ["Could I have a turn after you?", "The turn has no teammate.", "I turned you yesterday.", "You are a turn."], "A", "Could I ...? politely asks for a turn and fits the teammate role."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-b-iv-7-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究角色語氣、情境回應、請求、道歉、服務與任務對話；課綱：" + CURRICULUM,
            "authoringNote": "自編角色扮演情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 role-play questions")

if __name__ == "__main__":
    main()
