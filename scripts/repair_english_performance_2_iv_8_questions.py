import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "pronunciation, listening cues, and spoken sentence meaning"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "stress, intonation, and everyday oral communication"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "sound patterns, sentence purpose, and application"),
]

DATA = [
    ("word stress", "In the word 'record' used as a noun, which pronunciation pattern is most appropriate?", ["Stress the first syllable: RE-cord", "Stress only the final consonant", "Use equal stress and remove the vowel", "Stress a silent third syllable"], "A", "The noun record normally has first-syllable stress, unlike the common verb pattern."),
    ("final sounds", "Which pair ends with the same final sound?", ["map and cup", "rice and face", "bus and bag", "leaf and live"], "A", "Map and cup both end with the /p/ sound; spelling alone is not the deciding clue."),
    ("rising yes-no question", "Which intonation best fits the spoken question 'Are you ready?' when the speaker genuinely asks for confirmation?", ["A rising intonation at the end", "A flat whisper with no final movement", "A falling tone that sounds like a finished statement", "Stress only the word 'you' and omit the question"], "A", "A genuine yes-no question commonly uses rising intonation to invite confirmation."),
    ("falling wh-question", "Which intonation best fits 'Where is the bus stop?' in a neutral information request?", ["A falling intonation at the end", "A rising tone that makes it sound unfinished", "No final vowel sound", "Equal stress on every consonant"], "A", "A neutral wh-question commonly ends with falling intonation."),
    ("contrastive stress", "A student says, 'I wanted the GREEN folder, not the blue one.' Which word should receive the strongest contrastive stress?", ["GREEN", "wanted", "the", "one"], "A", "Green contrasts the requested folder with the rejected blue folder."),
    ("connected speech", "In a natural reading of 'Pick it up,' which choice describes a useful practice?", ["Link the words smoothly while keeping each word understandable.", "Pause after every sound and erase the final consonant.", "Say only the first word.", "Change the sentence into three unrelated words."], "A", "Smooth linking supports natural speech without removing the words or their meaning."),
    ("polite request", "Which spoken version sounds most polite when asking a classmate to repeat an answer?", ["Could you say that again, please?", "Say it again now!", "You repeat because I command you.", "Again is a classroom object."], "A", "Could you and please signal a respectful request."),
    ("meaning change", "In 'I didn't say she borrowed the book,' stressing 'she' most strongly suggests what contrast?", ["Someone else, not she, may have borrowed it.", "The speaker definitely borrowed the book.", "The book has no owner.", "The sentence is about the time of borrowing."], "A", "Stress on she contrasts that person with another possible borrower."),
    ("pause and phrasing", "Which reading makes 'After lunch, we will practice the dialogue' easiest to understand?", ["Pause briefly after 'lunch' and keep 'we will practice' together.", "Pause inside every word.", "Run all words together without any phrase boundary.", "Stress only the comma and skip the verb."], "A", "A phrase boundary after the opening time expression helps listeners process the subject and action."),
    ("integrated delivery", "A learner reads 'You finished the project?' after hearing an unexpected claim. Which delivery best shows surprise and checks the claim?", ["Use a clear rise at the end and stress 'finished'.", "Use a quiet falling tone and stress no word.", "Read it as a statement about yesterday's weather.", "Whisper only the word 'project'."], "A", "Rising intonation checks the claim, while stress on finished highlights the surprising information."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取發音、重音、語調與口語功能能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量與口語任務常以音節、尾音、重音、語調、連音及語意功能測量聽說辨識；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the sentence and identify the sound feature being tested: {topic}.",
        "Mark the syllable, final sound, contrast word, phrase boundary, or sentence purpose that controls the meaning.",
        f"Compare the choices with the stated pronunciation and communication context; the correct answer is {answer}.",
        f"Explain the sound-to-meaning connection: {explanation}",
        "Say the line once slowly and once naturally, then check that the stress or intonation still communicates the intended message.",
    ]
    return {"id": f"question-english-performance-2-iv-8-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-2-iv-8"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies pronunciation, stress, intonation, and spoken-purpose patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; speech situations, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-2-iv-8", "examPatternRefs": refs, "solutionStrategy": "Identify the sound feature and communicative purpose, locate the relevant syllable or phrase boundary, then choose the pronunciation pattern that preserves the intended meaning.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-2-iv-8-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
