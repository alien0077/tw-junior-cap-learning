"""獨立替換 B-Ⅳ-3 語言與非語言溝通策略題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-b-iv-3.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-b-iv-3"
KNOWLEDGE = "kg-english-content-b-iv-3"
ITEMS = [
    ("Your classmate looks confused during your explanation. What should you do?", ["Ask, 'Would you like me to explain it again?'", "Speak much faster.", "Turn away without speaking.", "Change the topic to lunch."], "A", "A polite check and offer to clarify responds to the listener's nonverbal signal."),
    ("Which action shows that you are listening carefully?", ["Make eye contact and nod when appropriate.", "Look at your phone the whole time.", "Interrupt every sentence.", "Walk away while the person speaks."], "A", "Eye contact and suitable nodding are nonverbal signs of attention."),
    ("A: Could you repeat the last instruction, please? B: ___.", ["Of course. First, open the file.", "No, the instruction is a chair.", "I repeated tomorrow.", "Please is a color."], "A", "The response repeats the instruction clearly and politely."),
    ("The room is noisy. Which strategy will help your partner hear you?", ["Move closer and speak clearly.", "Whisper from far away.", "Cover your mouth.", "Talk while facing the wall."], "A", "Moving closer and speaking clearly adapts to the communication environment."),
    ("Someone says, 'I am fine,' but speaks very quietly and avoids eye contact. What is the best response?", ["You seem worried. Would you like to talk?", "You must be happy, so leave.", "Your eyes are wrong.", "I will tell everyone your secret."], "A", "The response notices possible feelings without claiming certainty and invites communication."),
    ("Which sentence politely checks whether a message was understood?", ["Does that make sense?", "You understand nothing.", "Understand it now!", "Why are you a message?"], "A", "Does that make sense? checks understanding politely."),
    ("During a group discussion, two students speak at once. What should you say?", ["Let's let Alex finish, and then I will respond.", "Everyone must stop forever.", "I will shout louder.", "No one may have an idea."], "A", "Taking turns lets each speaker be heard and keeps the discussion cooperative."),
    ("A visitor does not understand your directions. Which action is most helpful?", ["Point to the map and use shorter sentences.", "Repeat the same long sentence louder.", "Laugh at the visitor.", "Give directions with no landmarks."], "A", "A map, shorter sentences, and useful gestures can clarify meaning."),
    ("Which message is most appropriate for a formal email to a teacher?", ["Could you please confirm the meeting time? Thank you.", "Hey, tell me now!!!", "Meeting? Whatever.", "You answer me because I say so."], "A", "Could you please ...? and Thank you create a respectful formal request."),
    ("When you do not know a word in English, which strategy is best?", ["Describe it with words you know or ask for help.", "Stop communicating immediately.", "Use a random word and refuse correction.", "Speak only by pointing forever."], "A", "Paraphrasing or asking for help keeps communication going despite a vocabulary gap."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-b-iv-3-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究語言、表情、眼神、手勢、輪流與澄清策略；課綱：" + CURRICULUM,
            "authoringNote": "自編溝通策略情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 verbal-nonverbal strategy questions")

if __name__ == "__main__":
    main()
