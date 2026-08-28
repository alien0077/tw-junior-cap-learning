"""獨立替換 B-Ⅳ-8 引導式討論題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-b-iv-8.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-b-iv-8"
KNOWLEDGE = "kg-english-content-b-iv-8"
ITEMS = [
    ("In a discussion about a class trip, which question best invites an opinion?", ["What do you think about visiting the science museum?", "Who is a museum yesterday?", "The trip thinks at noon.", "Do opinion a bus?"], "A", "What do you think about ...? invites another person's opinion."),
    ("A classmate shares an idea. Which response shows that you are listening?", ["I see your point. Could you explain it a little more?", "Your point is a shoe.", "I will interrupt you now.", "No one may explain anything."], "A", "The response acknowledges the idea and asks a useful follow-up question."),
    ("Which sentence politely disagrees with a suggestion to cancel the club?", ["I understand your concern, but I think we should try one more week.", "You are wrong and foolish.", "The club disagrees yesterday.", "I am a concern."], "A", "The sentence recognizes the concern before presenting a different view."),
    ("During a discussion, the group has two possible plans. What should the leader do first?", ["Ask for reasons and compare the two plans.", "Choose randomly without listening.", "End the discussion immediately.", "Let one person decide everything."], "A", "Reasons and comparison help the group make an informed decision."),
    ("Which question asks a speaker to give evidence for an idea?", ["What makes you think that?", "Where is your idea sleeping?", "Who evidence tomorrow?", "Does evidence have a color?"], "A", "What makes you think that? asks for the speaker's supporting reason or evidence."),
    ("A: I think the school should add more recycling bins. B: ___.", ["That's an interesting idea. Where should they go?", "Bins are ideas yesterday.", "I recycle a question.", "No student can speak."], "A", "The reply acknowledges the proposal and asks for a practical detail."),
    ("Which phrase helps you take your turn in a group discussion?", ["May I add something?", "You must stop talking forever.", "I am a turn yesterday.", "No one can hear a phrase."], "A", "May I add something? politely signals a wish to speak."),
    ("The group cannot agree on a meeting time. Which solution is most cooperative?", ["Let's list everyone's available times and find one that works for most people.", "Only my time matters.", "We should choose a time no one can attend.", "Do not ask anyone."], "A", "Listing availability and seeking overlap respects the group and solves the problem."),
    ("Which closing statement best summarizes a discussion?", ["So, we agree to use the library on Friday and check the schedule tomorrow.", "The discussion is a banana.", "Nobody said anything, but we finished.", "We will forget every idea."], "A", "The sentence states the decision and a follow-up action."),
    ("A speaker is unclear about a proposal. What is the most helpful question?", ["Could you give us an example?", "Why is your proposal a wall?", "I will guess and move on.", "Examples are not allowed."], "A", "Requesting an example can make an unclear proposal easier to understand."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-b-iv-8-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究引導提問、聆聽回應、禮貌異議、證據、輪流與討論結論；課綱：" + CURRICULUM,
            "authoringNote": "自編引導式討論情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 guided-discussion questions")

if __name__ == "__main__":
    main()
