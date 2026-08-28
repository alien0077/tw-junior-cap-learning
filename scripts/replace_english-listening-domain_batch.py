"""獨立替換英文語言能力（聽）導覽題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/performance-1.json").read_text())["source"]["url"]
LESSON = "lesson-english-performance-1"
KNOWLEDGE = "kg-english-performance-1"
ITEMS = [
    ("Listen: 'The art club meets in Room 204 after school.' Where does it meet?", ["In Room 204.", "At the art store.", "On the school bus.", "At home before school."], "A", "The announcement gives Room 204 as the location."),
    ("Listen: 'Please bring a raincoat tomorrow because rain is expected.' What should students bring?", ["A raincoat.", "A swimsuit.", "A camera only.", "A lunch ticket."], "A", "The speaker directly asks students to bring a raincoat."),
    ("Listen: 'I finished my homework, but I forgot to print it.' What did the speaker forget?", ["To print the homework.", "To finish the homework.", "To write the question.", "To attend a concert."], "A", "The speaker says the homework is finished but not printed."),
    ("Listen: 'The bus leaves at 7:15, so please arrive before seven.' When does the bus leave?", ["At 7:15.", "At 7:00.", "At 8:15.", "Before six."], "A", "The departure time is 7:15; arriving before seven is a separate instruction."),
    ("Listen: 'Would you like tea or orange juice?' Which answer shows a choice?", ["Orange juice, please.", "Yes, I am thirsty yesterday.", "The cup is on the table.", "I would like a question."], "A", "Orange juice is one of the two choices offered."),
    ("Listen: 'Mia sounds excited about the school trip.' How does Mia probably feel?", ["She feels excited.", "She feels asleep.", "She feels like a map.", "She feels absent tomorrow."], "A", "The description explicitly identifies excitement."),
    ("Listen: 'First wash the vegetables, then cut them, and finally put them in the bowl.' What happens second?", ["Cut the vegetables.", "Wash the bowl.", "Eat the vegetables first.", "Put the bowl in the vegetables."], "A", "The sequence names cutting after washing and before putting the vegetables in the bowl."),
    ("Listen: 'I cannot join the game tonight because I have to care for my little brother.' Why cannot the speaker join?", ["The speaker must care for a younger brother.", "The game was canceled by rain.", "The speaker lost a ball.", "The speaker is already at the game."], "A", "The speaker gives caring for a younger brother as the reason."),
    ("Listen: 'You left your notebook on the library table.' What is the message mainly doing?", ["Pointing out where the notebook was left.", "Inviting someone to a birthday party.", "Describing a new library book.", "Explaining how to cook dinner."], "A", "The sentence identifies the notebook's location."),
    ("Listen: 'Oh, I thought the meeting was on Friday, not Thursday.' What does the speaker realize?", ["The meeting is on Thursday.", "The meeting has no date.", "Friday comes before Thursday.", "The speaker canceled every meeting."], "A", "The correction from Friday to Thursday shows the realized meeting date."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-performance-1-{i}.json"
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
            "sourceLocator": "114 年國中教育會考英語科閱讀公開試題；研究聽力中的地點、細節、時間、選擇、情緒、順序、原因與主旨判讀；課綱：" + CURRICULUM,
            "authoringNote": "自編聽力文字稿情境與選項，未重製公開試題文字、選項或音檔；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 English listening-domain questions")

if __name__ == "__main__":
    main()
