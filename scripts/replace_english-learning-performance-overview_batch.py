"""獨立替換英文學習表現導覽題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/02-1_114P_English.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/812/(%E7%99%BC%E5%B8%83%E7%89%88)%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F-%E8%8B%B1%E8%AA%9E%E6%96%87%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81.pdf"
LESSON = "lesson-english-learning-performance"
KNOWLEDGE = "kg-english-learning-performance"
ITEMS = [
    ("A student listens to a short announcement and identifies the time and place. Which performance is shown?", ["Locating specific information while listening.", "Writing a fictional novel.", "Drawing the speaker's house.", "Avoiding all spoken information."], "A", "Identifying time and place demonstrates listening for specific information."),
    ("After reading a message, a learner explains its main point in English. What is being demonstrated?", ["Understanding and communicating the message.", "Memorizing the message without meaning.", "Measuring the paper's length.", "Changing every word into a picture."], "A", "Explaining the main point shows comprehension followed by communication."),
    ("Which action demonstrates effective spoken interaction?", ["Ask a follow-up question and respond to the partner's answer.", "Speak without allowing a reply.", "Repeat unrelated words.", "Leave before hearing the question."], "A", "Interaction requires listening, responding, and keeping the exchange meaningful."),
    ("A learner writes a short invitation with a date, place, and purpose. What makes the performance successful?", ["The writing includes information needed by its intended reader.", "The writing has no audience.", "The date is replaced by a random symbol.", "The purpose is hidden from everyone."], "A", "Purposeful writing supplies relevant details for its reader."),
    ("A student hears a speaker's rising tone at the end of a sentence and recognizes it as a question. What is the student using?", ["Clues from intonation to understand meaning.", "The speaker's handwriting.", "A map scale.", "The number of chairs in the room."], "A", "Intonation can provide information about a speaker's intended meaning."),
    ("Which behavior shows that a learner can use English in a familiar situation?", ["Order a drink politely and check that the order is correct.", "Recite unrelated words in silence.", "Ignore the server's question.", "Use a sentence with no communicative purpose."], "A", "The exchange uses English for a familiar real-world purpose."),
    ("A reader uses a title, repeated words, and nearby sentences to infer an unfamiliar word. What skill is shown?", ["Using context to understand language.", "Guessing from the word's length only.", "Avoiding all reading.", "Counting punctuation without meaning."], "A", "Title and surrounding context provide evidence for interpreting an unfamiliar word."),
    ("A learner revises an email after noticing that its tone is too casual for a teacher. What performance is shown?", ["Adjusting language to audience and purpose.", "Changing the recipient's identity.", "Removing all information.", "Writing without considering communication."], "A", "Revision for a teacher shows awareness of audience, purpose, and tone."),
    ("A student summarizes a short audio report and includes only details that support its topic. What is demonstrated?", ["Selecting and organizing relevant information.", "Copying every sound without understanding.", "Changing the report into a drawing only.", "Adding unrelated personal rumors."], "A", "A useful summary selects details relevant to the report's topic."),
    ("Which self-check best evaluates an English learning performance?", ["Can I understand the message, use suitable language, and explain my evidence?", "Did I choose the same answer position each time?", "Did I avoid all communication?", "Was the worksheet the brightest color?"], "A", "Understanding, appropriate use, and evidence provide meaningful performance checks."),
]

def main() -> None:
    for i, (prompt, options, _correct, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/english" / f"question-english-learning-performance-{i}.json"
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
            "sourceLocator": "114 年國中教育會考英語科閱讀公開試題；研究聽讀理解、口語互動、寫作目的、語調、語境推論與學習表現自我檢核；課綱：" + CURRICULUM,
            "authoringNote": "自編英語學習表現情境與選項，未重製公開試題文字、選項或圖片；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 English learning-performance questions")

if __name__ == "__main__":
    main()
