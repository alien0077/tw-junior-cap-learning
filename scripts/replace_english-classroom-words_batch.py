"""獨立替換 1-Ⅳ-1 課堂字詞題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/performance-1-iv-1.json").read_text())["source"]["url"]
LESSON = "lesson-english-performance-1-iv-1"
KNOWLEDGE = "kg-english-performance-1-iv-1"
ITEMS = [
    ("The teacher says, 'Please open your books to page 12.' What should students do?", ["Open their books to page 12.", "Close the classroom door forever.", "Write page 20 without a book.", "Leave the lesson."], "A", "The instruction directly tells students to open the books to page 12."),
    ("A teacher says, 'Work in pairs.' What does 'pairs' mean?", ["Groups of two.", "Groups of ten.", "One student alone.", "The teacher's desk."], "A", "A pair consists of two people or things."),
    ("The instruction is 'Circle the correct answer.' What should a learner do?", ["Draw a circle around the correct answer.", "Erase every answer.", "Read the answer aloud only.", "Draw a square on the desk."], "A", "Circle means to mark the selected answer with a circle."),
    ("A classmate asks, 'What does underline mean?' Which explanation is correct?", ["Draw a line under the word.", "Color the ceiling.", "Put the word in a bag.", "Skip the word completely."], "A", "To underline is to draw a line beneath text."),
    ("The teacher says, 'Listen and repeat.' What is the second action?", ["Say the words again.", "Close your ears.", "Write a new story first.", "Leave before listening."], "A", "Repeat means say or do something again after listening."),
    ("A worksheet says, 'Match each word with its picture.' What does 'match' mean here?", ["Connect each word to the picture that belongs with it.", "Hide every picture.", "Read only the title.", "Change every picture into a number."], "A", "Match means connect items that belong together."),
    ("The teacher says, 'Take out a pencil.' Which item should a student prepare?", ["A pencil.", "A lunch tray.", "A soccer ball.", "A winter coat only."], "A", "Take out means remove something from a bag or place so it is ready to use."),
    ("A class rule says, 'Raise your hand before speaking.' What should a student do?", ["Lift a hand and wait for permission to speak.", "Speak louder without waiting.", "Put both hands in a bag.", "Write on another student's paper."], "A", "The rule asks the student to lift a hand before speaking."),
    ("The teacher says, 'Hand in your homework.' What does the student need to do?", ["Give the homework to the teacher or submission place.", "Take the homework home again.", "Draw a hand on the homework.", "Hide the homework under the desk."], "A", "Hand in means submit or give work to the teacher."),
    ("A student hears, 'Any questions?' Which response is appropriate when the student is confused?", ["Yes. Could you explain this word again?", "No, I am a question.", "The word is under the floor.", "I will never listen."], "A", "The response clearly signals confusion and asks for an explanation."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-performance-1-iv-1-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究課堂指令、學習單詞彙、作答動作與澄清用語；課綱：" + CURRICULUM,
            "authoringNote": "自編課堂字詞情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 classroom-word questions")

if __name__ == "__main__":
    main()
