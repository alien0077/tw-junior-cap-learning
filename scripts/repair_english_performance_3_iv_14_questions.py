import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "rapid reading, key information, and text structure"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "skimming, headings, and focused retrieval"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "reading speed, summaries, and evidence selection"),
]

DATA = [
    ("title and first scan", "You have 30 seconds to understand a text titled 'Why Cities Need Trees.' What should you inspect first?", ["The title, headings, and repeated words about trees and cities", "Every unfamiliar word in the final paragraph", "The writer's address only", "The punctuation count without reading words"], "A", "A first scan uses visible structure and repeated topic words to establish the subject quickly."),
    ("key word", "A notice repeats 'bring a reusable cup' three times. Which detail is probably important?", ["The reusable cup is a key required item.", "The notice is mainly about buying a new phone.", "The repeated phrase can be ignored because it is long.", "The cup is a place rather than an object."], "A", "Repetition is a strong signal that the item matters to the notice's purpose."),
    ("first-last sentence", "A paragraph begins with 'Our class wanted less food waste' and ends with 'We now plan portions more carefully.' What can a quick reader infer?", ["The paragraph describes a class effort to reduce food waste.", "The paragraph is about a sports competition only.", "The class increased waste without making a plan.", "The paragraph has no problem or response."], "A", "The opening problem and closing response frame the paragraph's central idea."),
    ("scan for date", "A long event page contains history and descriptions, but you need the registration deadline. Which reading move is efficient?", ["Scan for 'register,' 'deadline,' dates, and time expressions.", "Read the history section three times first.", "Choose the largest number without checking its label.", "Read only the page footer and guess."], "A", "Scanning target words and date expressions directly addresses the needed detail."),
    ("summary", "A short article says students walk, use buses, and share rides to reduce traffic near school. Which summary is best?", ["Students use several transportation choices to reduce school-area traffic.", "Every student walks to school every day.", "The article explains how to repair a bus engine.", "Traffic is unrelated to transportation choices."], "A", "The summary covers the multiple actions without turning them into an unsupported universal claim."),
    ("discard detail", "To answer 'What is the article mainly about?' which detail should receive less attention first?", ["A single example that appears once", "The title and repeated central idea", "The opening claim", "The conclusion that restates the topic"], "A", "A one-time example is less useful for identifying the whole article's main focus."),
    ("heading map", "Headings read 'Problem,' 'Community Ideas,' and 'Next Steps.' What structure can a reader predict?", ["The text will move from an issue to possible responses and future action.", "The text will list unrelated animal names only.", "The text will repeat one sentence without development.", "The text will give a recipe before naming any problem."], "A", "The headings provide a clear problem-response-action organization."),
    ("time limit", "When reading quickly for a train departure time, why should you avoid translating every sentence?", ["It uses time on information that is not needed for the immediate question.", "Translation always makes every answer incorrect.", "The departure time can never be written in a sentence.", "A train table contains no numbers."], "A", "A focused task calls for locating the relevant time efficiently, not processing every detail equally."),
    ("key information", "A poster lists a location, two activities, a fee, and a contact email. If you plan to attend, which information set is essential?", ["The location, activity, fee, and contact email", "Only the poster's background color", "Only the designer's favorite activity", "A sentence from an unrelated advertisement"], "A", "Those four details support deciding whether and how to attend."),
    ("integrated rapid reading", "A reader first skims a title and headings, scans for a date and place, then rereads one paragraph to confirm the purpose. Why is this effective?", ["It combines speed with a focused evidence check.", "It avoids reading any meaningful words.", "It treats the first guess as proof even if details disagree.", "It spends equal time on every mark on the page."], "A", "The sequence is fast for orientation but returns to local evidence before answering."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取快速閱讀、重點擷取與資訊篩選能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以標題、重複字詞、首尾句、段落標題、日期地點與摘要測量快速抓取重點及證據回查；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the task and identify the rapid-reading target: {topic}.",
        "Set the purpose and mark the title, headings, repeated words, first/last sentences, numbers, dates, places, or required items.",
        f"Select the choice that answers the target using the smallest sufficient set of evidence; the correct answer is {answer}.",
        f"Explain why the selected information is central: {explanation}",
        "Return to the relevant phrase or label to verify it, then state which extra details can be left aside for this particular question.",
    ]
    return {"id": f"question-english-performance-3-iv-14-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-14"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies rapid-reading and key-information patterns only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; texts, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-14", "examPatternRefs": refs, "solutionStrategy": "Define the question target, use titles and structural signals to orient quickly, scan for the requested evidence, and reread only enough context to verify the answer.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-14-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
