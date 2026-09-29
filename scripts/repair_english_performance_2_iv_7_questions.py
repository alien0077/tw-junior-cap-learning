import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "question words, dialogues, and information requests"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "who, what, when, where questions in context"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional questions, details, and appropriate replies"),
]

DATA = [
    ("who", "The note says, 'Ms. Lin will lead the museum tour.' Which question asks about the person?", ["Who will lead the museum tour?", "When will the museum tour lead?", "Where will lead the museum tour?", "Why will the person be a museum?"], "A", "Who asks for the person, and the note identifies Ms. Lin."),
    ("what", "The announcement says, 'Please bring a raincoat for the river walk.' Which question asks about the needed item?", ["What should participants bring?", "Who should participants bring?", "Where should participants bring?", "When should participants be a raincoat?"], "A", "What asks for the item, which is a raincoat."),
    ("when", "The club starts at 3:40 after the last class. Which is the clearest question?", ["When does the club start?", "Who does the club start?", "What does the club start?", "Where does the club start a clock?"], "A", "When asks for the starting time."),
    ("where", "The rehearsal will be in Room 204 beside the music room. Which question asks for the place?", ["Where will the rehearsal be?", "What will the rehearsal be beside?", "Who will the rehearsal be?", "When will Room 204 rehearse?"], "A", "Where asks for the location, and the answer is Room 204."),
    ("why", "The bus leaves earlier because the mountain road may close. Which question asks for the reason?", ["Why does the bus leave earlier?", "Who leaves the mountain road?", "Where does the reason leave?", "What time is a reason?"], "A", "Why asks for the cause of the earlier departure."),
    ("how", "A classmate wants to know the method for submitting a video. Which question is suitable?", ["How should I submit the video?", "Who should I submit the video?", "When is the video method?", "Where does a method submit?"], "A", "How asks about the method or procedure."),
    ("which", "There are two buses, and only the green one goes to the sports center. Which question helps choose one?", ["Which bus goes to the sports center?", "Who bus goes to the sports center?", "Why bus is a sports center?", "When bus is a green?"], "A", "Which is used to select one bus from the two choices."),
    ("polite request", "You did not hear the meeting time. Which question politely asks for repetition?", ["Could you tell me the meeting time again, please?", "Say time now because I command you.", "The meeting time is a question mark.", "You tell me yesterday's time tomorrow."], "A", "The modal could and please make the request clear and polite."),
    ("match question and answer", "The answer is 'Because the field is wet.' Which question matches it?", ["Why was the soccer game moved indoors?", "Where is the field moved?", "Who is the wet?", "What time because indoors?"], "A", "An answer beginning with because matches a why-question about the cause."),
    ("integrated inquiry", "You need the person, time, and place for a volunteer meeting. Which set of questions is complete?", ["Who is attending, when is it, and where will it be?", "What color is it, why is a person, and who is the place?", "Where is attending, what time is a person, and why is the room?", "When is a volunteer, who is a clock, and what is the place?"], "A", "The set correctly maps who to people, when to time, and where to place."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取人事時地物提問與功能語言能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以公告、對話與生活資訊要求學生選擇適切疑問詞、配對答案並提出禮貌問題；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the context and identify the inquiry target: {topic}.",
        "List the information type needed—person, thing, time, place, reason, method, choice, or a polite repetition request.",
        f"Check the question word and sentence meaning against the context; the correct answer is {answer}.",
        f"Explain the grammar and information match: {explanation}",
        "Read the question with its expected answer, then replace one detail and confirm which question word must change.",
    ]
    return {"id": f"question-english-performance-2-iv-7-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-2-iv-7"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies question-word selection and functional information requests only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; contexts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-2-iv-7", "examPatternRefs": refs, "solutionStrategy": "Identify the information requested, map it to the correct question word or polite form, verify the answer type, and reread the exchange for grammatical and contextual fit.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-2-iv-7-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
