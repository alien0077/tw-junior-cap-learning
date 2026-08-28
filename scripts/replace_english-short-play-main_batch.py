"""獨立替換 1-Ⅳ-6 故事短劇主要內容題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/performance-1-iv-6.json").read_text())["source"]["url"]
LESSON = "lesson-english-performance-1-iv-6"
KNOWLEDGE = "kg-english-performance-1-iv-6"
ITEMS = [
    ("Short play: Mia drops her map. Leo helps her find it, and they arrive at the park together. What is the play mainly about?", ["Friends helping one another.", "A map that wants to travel alone.", "A park that closes forever.", "Leo losing his bicycle."], "A", "The events focus on Leo helping Mia and their shared arrival."),
    ("Short play: A seed does not grow. The children move it to a sunny place and water it regularly. What happens in the end?", ["The seed begins to grow.", "The children throw away the garden.", "The sun disappears.", "The seed becomes a book."], "A", "After the children change the conditions and care for it, the seed begins to grow."),
    ("Short play: Nora wants the last seat, but she notices an elderly guest standing. She gives up the seat. What does Nora's action show?", ["Consideration for another person.", "A plan to leave the theater.", "Fear of sitting down.", "A wish to hide the seat."], "A", "Giving the seat to someone standing shows consideration."),
    ("Short play: Two teams argue about a ball. The coach asks them to describe what happened, and they agree on a fair solution. What is the main idea?", ["Listening can help solve a disagreement.", "Arguments can never end.", "The ball belongs to the coach.", "Teams should avoid all rules."], "A", "The teams listen, discuss the facts, and reach a fair solution."),
    ("Short play: Kai practices a difficult line many times. On the show night, he says it clearly. What is the story mainly about?", ["Practice preparing someone for a performance.", "A show with no actors.", "A line that cannot be spoken.", "Kai refusing to rehearse."], "A", "Repeated practice helps Kai perform the difficult line clearly."),
    ("Short play: A fox sees food behind a fence. It first pulls the fence, then notices an open gate and walks through it. What changes?", ["The fox finds a better solution.", "The food disappears because of the gate.", "The fence begins to walk.", "The fox stops looking for food forever."], "A", "The open gate gives the fox a simpler way to reach the food."),
    ("Short play: Ella is nervous about speaking. Her partner smiles and says, 'Take your time.' Ella speaks more calmly. What is the partner doing?", ["Giving encouragement.", "Ending the presentation.", "Making Ella forget the topic.", "Asking Ella to run away."], "A", "The partner's supportive words help Ella feel calmer."),
    ("Short play: A group plans a picnic, but dark clouds appear. They move the picnic indoors and still enjoy lunch. What is the main point?", ["Changing a plan can solve a problem.", "Picnics must always be outdoors.", "Clouds are food.", "The group cancels every activity."], "A", "Moving indoors allows the group to continue despite the weather."),
    ("Short play: Sam finds a wallet and asks a teacher to help locate its owner. The owner returns and thanks him. What value is emphasized?", ["Honesty.", "Speed in a race.", "Keeping lost things.", "Avoiding all teachers."], "A", "Sam returns the wallet instead of keeping it, demonstrating honesty."),
    ("Short play: The final scene shows the class planting a tree together after cleaning the school yard. What does the ending suggest?", ["Cooperation can improve a shared place.", "The class dislikes all trees.", "Cleaning makes a place worse.", "Only one student did every task."], "A", "The class works together and improves the school environment."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-performance-1-iv-6-{i}.json"
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
            "sourceLocator": "114 年國中教育會考英語科閱讀公開試題；研究短劇的角色、事件、轉折、問題解決、價值與結局判讀；課綱：" + CURRICULUM,
            "authoringNote": "自編故事短劇與選項，未重製公開試題文字、劇本、歌曲或音檔；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 short-play-main questions")

if __name__ == "__main__":
    main()
