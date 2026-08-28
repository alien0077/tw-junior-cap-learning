"""獨立替換英文領域導覽題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://cap.rcpet.edu.tw/index.html"
CURRICULUM = "https://www.k12ea.gov.tw/Tw/Common/SinglePage?filter=11C2C6C1-D64E-475E-916B-D20C83896343"
LESSON = "lesson-english-language-domain"
KNOWLEDGE = "kg-english-learning-focus"
ITEMS = [
    ("A student reads an English notice, discusses it with a partner, and writes a short response. Which abilities are being combined?", ["Reading, speaking, and writing.", "Only drawing.", "Only memorizing a date.", "No language ability."], "A", "The student reads, discusses, and writes, so three language abilities are combined."),
    ("Which habit best helps a learner understand a new English article?", ["Use context, check key words, and confirm the main idea.", "Choose an answer only because it is longest.", "Skip every unknown word and the title.", "Copy the first sentence as the whole meaning."], "A", "Context, key words, and main-idea checking support reliable reading."),
    ("A learner hears an unfamiliar word during a conversation. What is a useful strategy?", ["Ask the speaker to repeat or explain it.", "End the conversation immediately.", "Pretend to understand every detail.", "Change every word to a number."], "A", "Clarification keeps communication going and checks understanding."),
    ("Which task most clearly requires writing for a real purpose?", ["Write an email asking a teacher about a meeting time.", "Point at a blank wall.", "Count chairs silently.", "Memorize a color without using it."], "A", "The email has a clear audience, purpose, and message."),
    ("A student compares two English webpages before using information in a report. Why is this useful?", ["It helps check whether the information is consistent and trustworthy.", "It guarantees that the longer page is true.", "It makes sources unnecessary.", "It replaces reading with guessing."], "A", "Comparing sources can reveal context and improve information checking."),
    ("Which activity best supports speaking fluency?", ["Practice a short conversation and respond to a partner.", "Look at a vocabulary list without saying anything.", "Copy punctuation marks only.", "Listen to silence."], "A", "Conversation practice requires producing and responding to spoken English."),
    ("A learner notices that a sentence sounds unclear. What should the learner do?", ["Reread it, check the surrounding context, and revise if needed.", "Assume unclear sentences are always correct.", "Delete the entire page without checking.", "Ask an unrelated question."], "A", "Rereading, context checking, and revision are useful language-learning strategies."),
    ("Why should an English learner consider the audience before writing?", ["Word choice and tone can be adjusted for the reader and purpose.", "Every reader expects exactly the same message.", "Audience makes grammar irrelevant.", "Writing never has a purpose."], "A", "Audience and purpose guide suitable vocabulary, tone, and detail."),
    ("A group uses a picture, a short caption, and spoken explanation to present a topic. What does this show?", ["Different forms can work together to communicate meaning.", "Pictures always replace language.", "Spoken explanations cannot add information.", "Captions have no audience."], "A", "Visual, written, and spoken forms can support one another."),
    ("Which reflection question best helps a learner improve English?", ["What did I understand, where was I unsure, and what will I try next?", "Was the page the correct color?", "Can I avoid all practice?", "Did I guess every answer?"], "A", "The question identifies understanding, difficulty, and a next learning action."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-language-domain-{i}.json"
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
            "sourceLocator": "國中教育會考官方入口與官方課綱索引；研究閱讀、聽說互動、寫作目的、資訊查核與學習反思；課綱：" + CURRICULUM,
            "authoringNote": "自編英語領域整合情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 English domain overview questions")

if __name__ == "__main__":
    main()
