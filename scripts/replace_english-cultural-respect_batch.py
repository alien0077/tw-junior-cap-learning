"""獨立替換 C-Ⅳ-4 尊重欣賞文化題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/content-c-iv-4.json").read_text())["source"]["url"]
LESSON = "lesson-english-content-c-iv-4"
KNOWLEDGE = "kg-english-content-c-iv-4"
ITEMS = [
    ("A classmate introduces a family tradition that is new to you. What is the best response?", ["That sounds interesting. What does it mean to your family?", "That tradition is wrong.", "Everyone must practice it exactly as I do.", "I will copy it without learning about it."], "A", "The response shows interest and invites the classmate to explain personal meaning."),
    ("You do not understand a ceremony at a cultural event. What should you do?", ["Ask a respectful question or read the event information.", "Make jokes during the ceremony.", "Tell others that it has no meaning.", "Interrupt the participants to correct them."], "A", "A respectful question or reliable information supports understanding."),
    ("Which statement avoids a stereotype?", ["People in a community may have different experiences of the same tradition.", "Every person in a country likes exactly the same food.", "One visitor can speak for everyone.", "A single example proves what all people believe."], "A", "The first statement recognizes individual differences and avoids overgeneralizing."),
    ("A friend says a greeting in your culture incorrectly but is trying to learn. What is a helpful response?", ["Gently explain the appropriate use and thank the friend for asking.", "Laugh and refuse to explain.", "Tell the friend never to speak again.", "Post the mistake online without permission."], "A", "Gentle explanation and appreciation encourage respectful learning."),
    ("A museum asks visitors not to touch a traditional object. Why should you follow the rule?", ["It protects the object and respects its cultural significance.", "Rules are never useful in museums.", "Touching always improves understanding.", "The object belongs to every visitor personally."], "A", "Following the rule protects both the artifact and its meaning."),
    ("Which action shows appreciation rather than appropriation or mockery?", ["Learn the context and credit the community when sharing information.", "Use a sacred symbol as a costume joke.", "Remove a cultural symbol from its context.", "Claim another community's tradition as your invention."], "A", "Context and credit show appreciation and avoid treating cultural elements as props."),
    ("A student hears two different opinions about a custom. What is the best conclusion?", ["The custom may be experienced differently by different people.", "One opinion must represent everyone.", "The custom has no value.", "The student should invent a third opinion."], "A", "Different perspectives can coexist; one speaker should not be treated as everyone."),
    ("Before presenting a culture in a school report, which step is most responsible?", ["Check reliable sources and ask whether the description is respectful and accurate.", "Use the first stereotype found online.", "Leave out the community's own explanations.", "Change facts to make the report funny."], "A", "Source checking and respectful accuracy are essential for a responsible report."),
    ("A visitor is invited to join a dance at a public celebration. What should the visitor do?", ["Join only after learning that visitors are welcome and following the instructions.", "Enter a restricted ritual without asking.", "Change the dance to make fun of it.", "Demand that everyone stop."], "A", "Confirming permission and following instructions respects the event."),
    ("Which sentence best expresses cultural appreciation?", ["I learned something new, and I respect that this practice has meaning for its community.", "My way is the only civilized way.", "Unfamiliar practices are all silly.", "I know what everyone in that community thinks."], "A", "The sentence values learning while recognizing the community's own meaning."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-content-c-iv-4-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究尊重提問、避免刻板印象、文化脈絡、來源查核與參與界線；課綱：" + CURRICULUM,
            "authoringNote": "自編文化尊重情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 cultural-respect questions")

if __name__ == "__main__":
    main()
