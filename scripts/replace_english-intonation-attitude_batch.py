"""獨立替換 1-Ⅳ-9 語調所表達的情緒態度題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/performance-1-iv-9.json").read_text())["source"]["url"]
LESSON = "lesson-english-performance-1-iv-9"
KNOWLEDGE = "kg-english-performance-1-iv-9"
ITEMS = [
    ("The speaker says, 'We won!' with a bright, rising voice. What feeling is most likely expressed?", ["Happiness or excitement.", "Boredom.", "Fear of reading.", "Anger at the team."], "A", "The words and bright rising voice signal happiness or excitement."),
    ("A student says, 'You finished the project already?' with a surprised rising tone. What is the attitude?", ["The student is surprised.", "The student is giving a cooking order.", "The student is certain the project is unfinished.", "The student is saying goodbye."], "A", "A rising tone on already? can show surprise in this context."),
    ("A teacher says, 'Please sit down.' in a calm, gentle voice. What attitude is shown?", ["Polite calmness.", "Strong anger.", "Confusion about the classroom.", "Excitement about a race."], "A", "A calm gentle voice makes the instruction sound polite and calm."),
    ("A speaker says, 'That was your idea?' with a flat, doubtful tone. What does the tone suggest?", ["The speaker is doubtful.", "The speaker is celebrating.", "The speaker is asking for a bus ticket.", "The speaker is whispering a welcome."], "A", "The flat doubtful tone signals uncertainty about the idea."),
    ("A child says, 'I lost my favorite book,' in a slow, quiet voice. How does the child probably feel?", ["Sad.", "Proud of winning.", "Amused by a joke.", "Certain the book is nearby."], "A", "The words and slow quiet delivery support sadness."),
    ("A friend says, 'Sure, take the last cookie,' with a warm, friendly voice. What attitude is expressed?", ["Generosity and friendliness.", "A warning not to eat.", "Anger about the cookie.", "Fear of the kitchen."], "A", "The wording and warm voice communicate a friendly offer."),
    ("A coach says, 'Keep going!' loudly with energetic emphasis. What is the coach trying to do?", ["Encourage the players.", "Ask them to sleep.", "End the practice immediately.", "Apologize for a missing book."], "A", "Loud energetic emphasis makes the phrase an encouragement."),
    ("A speaker says, 'Oh, great,' with a long sigh after missing the bus. What attitude is most likely?", ["Frustration or disappointment.", "Real excitement about the bus.", "A neutral weather report.", "A request for directions to school."], "A", "The sigh and situation make the words sound disappointed rather than genuinely pleased."),
    ("A listener hears, 'Could you help me?' with a rising tone at the end. What is the speaker doing?", ["Asking for help.", "Announcing that help is finished.", "Describing yesterday's weather.", "Giving a final answer with no request."], "A", "The rising tone and question form signal a request."),
    ("A student says, 'I understand now,' in a relaxed voice after an explanation. What does the student express?", ["Understanding and relief.", "Anger at the explanation.", "A plan to hide the homework.", "Confusion about the speaker's name."], "A", "The words and relaxed delivery indicate understanding, likely with relief."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-performance-1-iv-9-{i}.json"
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
            "sourceLocator": "114 年國中教育會考英語科閱讀公開試題；研究語調、重音、速度、音量、語境與情緒態度判讀；課綱：" + CURRICULUM,
            "authoringNote": "自編對話與語調文字描述，未重製公開試題文字、音檔或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 intonation-attitude questions")

if __name__ == "__main__":
    main()
