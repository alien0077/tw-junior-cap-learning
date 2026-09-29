import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "inference from notices, data, context, and multiple clues"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "implicit meaning, evidence, cause, and reasonable conclusions"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "reading information and drawing supported inferences"),
]

DATA = [
    ("implicit cause", "A notice says the playground is closed after heavy rain and asks students to use the indoor gym. What can be inferred?", ["The rain may have made the playground unsafe", "The gym has been demolished", "Students are forbidden from all exercise", "The notice is about a summer concert"], "A", "The closure and alternative indoor location support a safety-related inference."),
    ("data trend", "A chart shows library visits rising from 20 in April to 35 in May and 50 in June. What trend is supported?", ["Visits increased each month", "Visits decreased each month", "Visits stayed exactly the same", "The chart gives no monthly information"], "A", "The values rise in each successive month."),
    ("context inference", "A student carries an umbrella, checks a weather app, and wears a raincoat before leaving. What is most reasonable to infer?", ["The student expects wet weather", "The student is preparing for a swimming race indoors", "The student has forgotten the weather", "The student plans to avoid all clothing"], "A", "The three clues together point to expected rain."),
    ("speaker intention", "A message says, 'The report is due tomorrow. Could you send me your section tonight so I can combine the pages?' What does the writer want?", ["The writer wants the section tonight to assemble the report", "The writer wants to cancel the report", "The writer wants a new school subject", "The writer wants the recipient to delete every page"], "A", "The deadline and combining request reveal the intended action."),
    ("cause inference", "A bus arrives late, and several passengers look at their watches before hurrying toward the school gate. What likely happened?", ["The delay made them worry about arriving on time", "The passengers are preparing for a picnic next month", "The bus arrived much earlier than planned", "The school gate has permanently closed"], "A", "The late bus, watches, and hurried movement form a supported explanation."),
    ("unstated comparison", "A table shows reusable bottles used 40 times in one class and 12 times in another. What can be concluded?", ["The first class recorded more reusable-bottle use", "The second class used more bottles", "Both classes recorded exactly 40 uses", "The table compares test scores instead"], "A", "The numbers directly support the comparison of recorded use."),
    ("emotion inference", "After reading a message, Kai smiles, replies 'That is wonderful news!', and immediately calls his family. What feeling is most likely?", ["Happiness or excitement", "Anger at the good news", "Confusion about every word", "Boredom with the message"], "A", "The positive reply and immediate call indicate strong happiness or excitement."),
    ("negative evidence", "A museum page lists no public entry on Monday but gives tour times Tuesday through Sunday. What should a visitor infer?", ["The visitor should plan a tour from Tuesday through Sunday", "Monday has the most tours", "The museum is open for public tours every Monday", "The page gives no information about any day"], "A", "The listed schedule excludes Monday and provides tour information for the other days."),
    ("multiple clues", "A recipe says to chill the dough, the baker places it in a refrigerator, and the next step begins after thirty minutes. Why?", ["The dough needs time to become chilled before the next step", "The baker is trying to cook the dough immediately", "The refrigerator is being used as an oven", "The recipe has no connection to temperature"], "A", "The instruction, action, and time together explain the purpose of chilling."),
    ("integrated inference", "A school report shows less litter after more recycling bins were added, while a student survey says signs helped students find the bins. What is a supported inference?", ["More accessible bins and clear signs may have contributed to less litter", "The report proves signs alone caused every change", "Recycling bins increased litter everywhere", "The survey and report describe unrelated sports events"], "A", "Both sources support a cautious combined explanation, without claiming one factor is certain."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取資訊推論的因果、趨勢、隱含意圖、情緒、比較、負面證據與多來源整合能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常要求從公告、表格、對話與多個線索推論未明說原因、目的、情緒、趨勢或合理結論，並區分證據與過度推論；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read every stated detail and identify the inference target: {topic}.",
        "Mark the clues, numbers, time order, contrast, action, emotion, and source limits before forming a conclusion.",
        f"Choose the conclusion that follows from all relevant clues without adding an unsupported certainty; the correct answer is {answer}.",
        f"Explain the evidence chain from the information to the inference: {explanation}",
        "Reread the source and remove any option that is unrelated, reverses a fact, or claims more than the evidence can prove.",
    ]
    return {"id": f"question-english-performance-9-iv-1-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-9-iv-1"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies inference from notices, charts, messages, context, and multiple evidence only and does not reproduce an original question, option, image, or text.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; information sets, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-9-iv-1", "examPatternRefs": refs, "solutionStrategy": "Collect the explicit clues, connect them through cause, comparison, purpose, or pattern, and choose only the conclusion that the evidence reasonably supports.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-9-iv-1-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
