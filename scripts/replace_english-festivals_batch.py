"""獨立替換 C-Ⅳ-1 國內外節慶題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-c-iv-1.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-c-iv-1"
KNOWLEDGE = "kg-english-content-c-iv-1"
ITEMS = [
    ("A town holds a lantern festival every spring. What is one purpose of the event?", ["People gather to enjoy a shared tradition.", "The town is trying to stop all visitors.", "Lanterns are used only as school furniture.", "Spring means no one can meet."], "A", "A festival can bring people together through a shared tradition."),
    ("At a harvest festival, families bring food made from local crops. What does this show?", ["The celebration is connected with the season and local life.", "The families never eat together.", "The crops were grown in another century only.", "A festival cannot include food."], "A", "Harvest celebrations often connect seasonal crops with community life."),
    ("A student reads that people in another country decorate homes before a new-year celebration. What should the student do?", ["Learn what the decoration means in that culture.", "Assume it has exactly the same meaning everywhere.", "Say the custom is meaningless.", "Remove the decorations without asking."], "A", "Learning the meaning avoids assumptions and respects the custom."),
    ("Which sentence correctly compares two festivals?", ["Both festivals bring families together, but they use different foods.", "Both festivals are the same because both have names.", "Neither festival has any participants.", "One festival is better without evidence."], "A", "The sentence identifies a similarity and a difference without making an unsupported judgment."),
    ("A school celebrates a foreign festival by inviting a guest to explain its history. Why is this helpful?", ["Students can learn the festival's background from a source connected to it.", "Students can avoid listening to anyone.", "The history must be invented by the class.", "A celebration should have no information."], "A", "A knowledgeable guest can provide cultural and historical context."),
    ("During a festival, people wear special clothing. Which question is most respectful?", ["What does this clothing represent?", "Why do you dress strangely?", "Can I make fun of it?", "Is every person forced to wear it?"], "A", "The question asks about meaning without insulting or overgeneralizing."),
    ("A calendar says a festival begins on the first day of a lunar month. What information does this give?", ["It gives the festival's date according to a lunar calendar.", "It proves the festival lasts one year.", "It tells us the festival has no date.", "It says the moon is a building."], "A", "The statement identifies the calendar system used to set the date."),
    ("A family visits a festival but follows a sign asking visitors not to enter a sacred area. What does this show?", ["They respect the event's rules and meaning.", "They refuse to learn the rules.", "They believe every area is a playground.", "They are changing the festival."], "A", "Following posted guidance respects the community and its sacred space."),
    ("A report says a festival includes music, dancing, and a story about the community's past. What does the story add?", ["It connects the celebration with community history.", "It proves music is forbidden.", "It means nobody knows the festival.", "It changes every dancer into a historian."], "A", "A story about the past gives the festival historical meaning."),
    ("Which action is best when sharing information about an unfamiliar festival?", ["Name the source and separate facts from your own guesses.", "Present guesses as facts.", "Use one stereotype for everyone.", "Copy a random post without checking it."], "A", "Source attribution and separating facts from guesses make cultural information more reliable."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-c-iv-1-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究國內外節慶的時間、活動、意義、歷史脈絡與文化比較；課綱：" + CURRICULUM,
            "authoringNote": "自編節慶資訊與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 festival questions")

if __name__ == "__main__":
    main()
