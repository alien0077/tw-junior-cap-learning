"""獨立替換 C-Ⅳ-5 基本世界觀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-c-iv-5.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-c-iv-5"
KNOWLEDGE = "kg-english-content-c-iv-5"
ITEMS = [
    ("A map shows that Country A and Country B share a border. What does this tell us?", ["The two countries are next to each other.", "The two countries have the same government.", "Everyone in both countries speaks one language.", "The countries have no different history."], "A", "A shared border indicates a geographic relationship, not identical governments or cultures."),
    ("A class reads about people in several regions using different languages. What is a reasonable conclusion?", ["The world includes many language communities.", "Only one language can be meaningful.", "Different languages prevent all cooperation.", "A language tells us every person's opinion."], "A", "The information supports linguistic diversity without making claims about every individual."),
    ("Why do students use a map scale when planning a trip?", ["It helps estimate the real distance between places.", "It changes the names of countries.", "It proves all roads are straight.", "It tells us what every traveler likes."], "A", "A map scale relates map distance to real-world distance."),
    ("A news report says a product uses materials from several countries. What idea does this illustrate?", ["Countries and communities can be connected through trade.", "No country depends on any resource.", "Products are always made in one home.", "Trade means every culture is identical."], "A", "Materials from several countries show economic connections across places."),
    ("A student sees a photo of a crowded city and assumes every person in that country lives there. What should the student remember?", ["One photo shows only a limited part of a country.", "A photo always represents everyone.", "Cities and rural areas are exactly the same.", "Countries have only one type of landscape."], "A", "A single image cannot represent an entire country or all its people."),
    ("A coastal community prepares for a typhoon by checking warnings and moving supplies. What does this show?", ["People can respond to local environmental risks.", "Weather never affects communities.", "Warnings are only for tourists.", "Coastal places have no hazards."], "A", "The action connects local risk information with community preparation."),
    ("A class compares two countries' climates. Which evidence is most useful?", ["Weather and climate data collected over an identified period.", "A guess based on one person's clothing.", "A movie scene with no location.", "The color of a country's flag."], "A", "Identified weather or climate data are relevant evidence for comparison."),
    ("Why is it useful to learn where a source's information about a country came from?", ["It helps readers judge context and reliability.", "It guarantees every statement is true.", "It makes geography unnecessary.", "It lets readers replace facts with guesses."], "A", "Source context helps readers evaluate information, though no source should be accepted blindly."),
    ("A volunteer group from two countries works together to clean a river. What does this example suggest?", ["People across borders can cooperate on shared concerns.", "Countries cannot solve local problems.", "The river belongs to only one person.", "Cooperation removes cultural differences."], "A", "The example demonstrates cooperation while not claiming that differences disappear."),
    ("Which statement is a careful basic view of the world?", ["Places are connected, but each community also has its own history and experiences.", "All places are exactly alike.", "A country's size explains every person's life.", "One source can describe every community perfectly."], "A", "The statement balances global connections with local diversity and limits."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-c-iv-5-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究地理位置、語言多樣性、地圖尺度、跨國連結、環境風險、資料來源與世界觀範圍；課綱：" + CURRICULUM,
            "authoringNote": "自編基本世界觀情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 worldview questions")

if __name__ == "__main__":
    main()
