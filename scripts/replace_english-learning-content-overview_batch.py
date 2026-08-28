"""獨立替換英文學習內容導覽題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://cap.rcpet.edu.tw/index.html"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/812/(%E7%99%BC%E5%B8%83%E7%89%88)%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F-%E8%8B%B1%E8%AA%9E%E6%96%87%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81.pdf"
LESSON = "lesson-english-learning-content"
KNOWLEDGE = "kg-english-learning-content"
ITEMS = [
    ("A lesson asks students to read a short message and identify who will do what. What content is being practiced?", ["Understanding people, actions, and information in English.", "Only drawing a map.", "Memorizing an unrelated number.", "Avoiding all context."], "A", "The task uses English text to identify people, actions, and information."),
    ("Which example is language content rather than a study shortcut?", ["Using a question form to ask about a schedule.", "Choosing every answer marked B.", "Skipping the sentence with a new word.", "Copying a classmate's answer without reading."], "A", "A question form used for a schedule is actual language content; the others are unreliable shortcuts."),
    ("A learner practices words for places and then uses them in directions. Why is this useful?", ["It connects vocabulary with a meaningful communication task.", "It proves every place has the same name.", "It makes grammar unnecessary.", "It prevents the learner from speaking."], "A", "Using place words in directions connects form with communicative meaning."),
    ("Which activity focuses on understanding the main idea of a short English passage?", ["Read the passage, identify its topic, and choose supporting details.", "Count the letters in every word only.", "Select the shortest option without reading.", "Translate a title from an unrelated book."], "A", "Topic and supporting details are evidence for a passage's main idea."),
    ("A student changes 'She goes to school' to 'They go to school.' What is the student practicing?", ["Subject-verb agreement and pronoun changes.", "The history of a festival.", "Map distance only.", "Punctuation in a Chinese poem."], "A", "The change requires adjusting both the pronoun and the verb form."),
    ("Which task practices language used for making a polite request?", ["Write 'Could you open the window, please?' for a classroom situation.", "List colors without using a sentence.", "Draw a window with no words.", "Guess a speaker's age from a photo."], "A", "The sentence uses a polite request in a clear situation."),
    ("A listening exercise asks students to hear a time and write it down. What is being checked?", ["Listening for a specific piece of information.", "The speaker's shoe size.", "The color of the classroom wall.", "Whether all conversations are identical."], "A", "Writing a time checks the ability to locate specific information while listening."),
    ("Which pair shows a useful connection between form and meaning?", ["'Because' introduces a reason in a sentence.", "A comma always names a person.", "A question mark means every answer is true.", "A capital letter replaces every verb."], "A", "Because links a clause to its reason, showing both form and meaning."),
    ("A learner reads a menu, chooses a meal, and explains the choice in English. What does the task combine?", ["Reading information with purposeful spoken or written communication.", "Only copying menu decorations.", "Only reciting an alphabet.", "No language use because food is involved."], "A", "The learner reads information and communicates a choice for a real purpose."),
    ("Which reflection best checks whether a learner understood new English content?", ["Can I use the new form or words in a new situation and explain my choice?", "Did I finish without reading?", "Was the answer position familiar?", "Did I avoid asking questions?"], "A", "Applying and explaining new language in a new situation provides meaningful evidence of understanding."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-learning-content-{i}.json"
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
            "sourceLocator": "國中教育會考官方入口與國教院英語文課綱；研究英語學習內容中的字彙、句型、閱讀、聽力與語用任務；課綱：" + CURRICULUM,
            "authoringNote": "自編英語學習內容情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 English learning-content questions")

if __name__ == "__main__":
    main()
