"""獨立替換英文文化與習俗領域導覽題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-c.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-c"
KNOWLEDGE = "kg-english-content-c"
ITEMS = [
    ("A class is learning about a local festival. Which action shows respect?", ["Ask questions and listen before judging.", "Say every other custom is wrong.", "Copy a ceremony as a joke.", "Refuse to learn anything."], "A", "Listening and asking respectfully helps students learn without judging another culture."),
    ("Two countries celebrate the new year at different times. What is a fair conclusion?", ["Their calendars and traditions may be different.", "One country has no culture.", "Only one celebration can be real.", "The people must dislike new years."], "A", "Different dates can result from different calendars and traditions; they do not prove cultural superiority."),
    ("A visitor is unsure how to greet people at a community event. What should the visitor do?", ["Observe or politely ask what greeting is appropriate.", "Use the loudest greeting possible.", "Laugh at everyone nearby.", "Assume every place has the same rule."], "A", "Observing and asking politely avoids assumptions and shows respect."),
    ("Which statement distinguishes a custom from a personal habit?", ["A custom is shared by a community, while a habit may belong to one person.", "A custom is always private.", "A habit must be a national holiday.", "They can never be described."], "A", "Shared community practice and individual behavior are different scopes."),
    ("A student compares food traditions in two regions. Which method is best?", ["Use reliable information and describe both traditions accurately.", "Choose one region and invent details about the other.", "Judge a tradition by one person's opinion.", "Ignore the people who practice it."], "A", "Accurate sources and balanced description support a fair cultural comparison."),
    ("A guest is offered food that is unfamiliar. Which response is most respectful?", ["Thank the host and ask what the food contains.", "Make fun of its appearance.", "Tell the host the food is disgusting.", "Take it without listening to any explanation."], "A", "Thanking the host and asking about ingredients communicates curiosity and respect."),
    ("Why should we avoid saying that every person in a country behaves the same way?", ["People within a culture can have different experiences and choices.", "Countries have no traditions.", "People never learn from one another.", "A stereotype is always precise."], "A", "Individuals are not identical, so broad stereotypes can be inaccurate and unfair."),
    ("A school invites an exchange student to share a tradition. What is a good follow-up question?", ["What does this tradition mean to your family?", "Why is your tradition strange?", "Do all people do exactly this?", "Can I change it without asking?"], "A", "The question invites personal meaning without assuming the student represents everyone."),
    ("A museum label explains that an object was used in a ceremony. What should a reader do?", ["Read the context before deciding what the object means.", "Guess from its shape only.", "Treat it as a modern toy.", "Ignore the label and make up a story."], "A", "Cultural objects should be interpreted with historical and social context."),
    ("Which behavior best supports cultural exchange?", ["Share your own experience and remain open to another person's experience.", "Demand that others adopt your custom.", "Collect stereotypes instead of information.", "Speak for people you have never met."], "A", "Exchange involves sharing and listening, not forcing or stereotyping."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-c-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究節慶、習俗、文化比較、脈絡與尊重欣賞；課綱：" + CURRICULUM,
            "authoringNote": "自編文化與習俗情境及選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 culture-customs domain questions")

if __name__ == "__main__":
    main()
