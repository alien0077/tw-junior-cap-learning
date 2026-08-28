"""獨立替換 1-Ⅳ-3 基本重要句型題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/english/performance-1-iv-3.json").read_text())["source"]["url"]
LESSON = "lesson-english-performance-1-iv-3"
KNOWLEDGE = "kg-english-performance-1-iv-3"
ITEMS = [
    ("Choose the sentence that correctly describes one student in the library.", ["The student is reading quietly.", "The student are reading quietly.", "The student reading quietly is.", "The student quiet read."], "A", "A singular subject takes is and the present participle in this sentence."),
    ("Choose the correct question for asking about yesterday's activity.", ["What did you do yesterday?", "What do you did yesterday?", "What are you do yesterday?", "What did you doing yesterday?"], "A", "Did is followed by the base verb do in a past-time question."),
    ("Complete the sentence: 'There ___ two notebooks on the desk.'", ["are", "is", "am", "be"], "A", "Two notebooks is plural, so the correct form is there are."),
    ("Choose the sentence that expresses a future plan.", ["We are going to visit the museum tomorrow.", "We visited the museum yesterday tomorrow.", "We visiting the museum last week.", "We visit the museum before we were born."], "A", "Be going to plus a base verb expresses a planned future action."),
    ("Complete the sentence: 'My brother ___ a bicycle, but I do not.'", ["has", "have", "having", "to has"], "A", "A singular third-person subject takes has in the present tense."),
    ("Choose the sentence that gives advice about studying.", ["You should review the vocabulary tonight.", "You should to review the vocabulary.", "You reviewing should vocabulary.", "You should reviewed tomorrow."], "A", "Should is followed by the base verb review to give advice."),
    ("Choose the correct comparison: 'The blue bag is ___ than the red bag.'", ["heavier", "more heavy than", "heaviest than", "heavyest"], "A", "The comparative form of heavy is heavier, followed by than in the full sentence."),
    ("Complete the sentence: 'Sara and I ___ ready for the presentation.'", ["are", "is", "am", "be"], "A", "Sara and I is a plural subject, so it takes are."),
    ("Choose the sentence that asks for permission politely.", ["May I borrow your ruler, please?", "May I to borrow your ruler?", "I may borrowing your ruler?", "Borrow may your ruler me?"], "A", "May I plus the base verb is a polite permission question."),
    ("Choose the sentence that correctly states a reason.", ["I stayed home because I was sick.", "I stayed home because I sick was.", "Because I was sick, so I stayed home because.", "I because stayed home sick was."], "A", "Because introduces the reason, and the clause uses the correct word order."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-performance-1-iv-3-{i}.json"
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
            "sourceLocator": "鹽埕國中 114 學年度第 2 學期英文段考；研究 be、have、there be、過去式、未來計畫、情態動詞、比較級、請求與原因句型；課綱：" + CURRICULUM,
            "authoringNote": "自編基本重要句型情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 basic-sentence-pattern questions")

if __name__ == "__main__":
    main()
