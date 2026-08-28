"""獨立替換 C-Ⅳ-2 風土民情題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-c-iv-2.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-c-iv-2"
KNOWLEDGE = "kg-english-content-c-iv-2"
ITEMS = [
    ("A visitor sees people remove their shoes before entering a home. What should the visitor do?", ["Ask or observe the host and follow the home's practice.", "Walk in without asking.", "Say the practice is silly.", "Move all the shoes outside."], "A", "Observing and following the host's practice is respectful."),
    ("A travel note says a mountain village has houses adapted to heavy rain. What can a reader infer?", ["The local environment influences the way people live.", "Rain has no effect on homes.", "Every village has identical houses.", "The houses were built under the sea."], "A", "The statement connects local climate with housing and daily life."),
    ("A community market sells foods made from ingredients grown nearby. What does this show?", ["Local resources can influence food culture.", "The market has no connection to the area.", "All foods must come from overseas.", "Ingredients cannot be part of culture."], "A", "Nearby ingredients can shape what a community cooks and sells."),
    ("A student reads that a coastal town has a long history of fishing. Which source would add useful context?", ["An interview with local fishers or a community museum record.", "A random joke with no location.", "A weather guess from an unrelated city.", "A picture with no caption or date."], "A", "Local voices and community records can explain the town's way of life."),
    ("A guest is unsure whether to take a photograph during a community ceremony. What is best?", ["Ask permission and follow the event's guidance.", "Photograph everyone secretly.", "Interrupt the ceremony for a better picture.", "Post the picture before asking anyone."], "A", "Permission and event guidance protect participants and show respect."),
    ("Two regions use different ways to welcome visitors. What is a fair description?", ["Their customs are different, and each should be understood in its own context.", "One way must be the only polite way.", "Neither region welcomes visitors.", "A custom proves that all people there are identical."], "A", "Customs should be understood in context rather than ranked without evidence."),
    ("A village changes its festival schedule because the harvest season changed. What does this suggest?", ["Community activities may respond to local conditions.", "Festivals never relate to work or seasons.", "The village has no traditions.", "A schedule can change only by accident."], "A", "Seasonal work and local conditions can influence community activities."),
    ("A visitor learns that a greeting has a special meaning in a community. What is a good response?", ["Use the greeting carefully after learning when it is appropriate.", "Repeat it loudly as a joke.", "Tell everyone the meaning is unimportant.", "Use it in every situation without context."], "A", "Learning when and how to use a greeting avoids disrespect."),
    ("A description of a town mentions a river, a bridge, and a weekly market. What are these details mainly used to explain?", ["Features of the town and its community life.", "A recipe with no location.", "The writer's shoe size.", "A rule that markets cannot exist."], "A", "The details describe the place and how people use it."),
    ("Which question best helps someone learn about local customs without making assumptions?", ["What does this practice mean to people in your community?", "Does everyone there do exactly this?", "Why is your custom strange?", "Can I decide what it means for you?"], "A", "The question invites local explanation and does not assume everyone has the same experience."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-c-iv-2-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究地方環境、生活方式、社區市場、迎賓與風俗脈絡判讀；課綱：" + CURRICULUM,
            "authoringNote": "自編風土民情情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 local-customs questions")

if __name__ == "__main__":
    main()
