import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "tables, charts, and extracting practical information"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "data comparison, labels, and contextual inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "simple charts, schedules, and evidence-based reading"),
]

DATA = [
    ("title and unit", "A chart is titled 'Books Borrowed in April' and its vertical axis is labeled 'Number of books.' What does the chart measure?", ["The number of books borrowed in April", "The price of every book in May", "The height of the library building", "The number of students absent in April"], "A", "The title and axis together identify both the item and the time period being measured."),
    ("highest value", "A table lists Monday 12, Tuesday 18, and Wednesday 15 visitors. Which day has the highest number?", ["Tuesday", "Monday", "Wednesday", "All days have the same number"], "A", "Eighteen is larger than twelve and fifteen, so Tuesday is highest."),
    ("lowest value", "A weather chart shows 24°C, 21°C, 27°C, and 23°C from Monday to Thursday. Which day is coolest?", ["Tuesday", "Monday", "Wednesday", "Thursday"], "A", "Twenty-one degrees is the smallest value, so Tuesday is coolest."),
    ("change", "A recycling chart shows 8 kg in Week 1 and 13 kg in Week 2. What happened?", ["The amount increased by 5 kg.", "The amount decreased by 5 kg.", "The amount stayed exactly the same.", "The chart gives no two-week comparison."], "A", "Subtracting 8 from 13 shows an increase of 5 kilograms."),
    ("category comparison", "A snack survey records apples 10, bananas 6, and oranges 10. Which statement is supported?", ["Apples and oranges received the same number of votes.", "Bananas received the most votes.", "Oranges received no votes.", "Apples received twice as many as oranges."], "A", "Both apples and oranges have a value of ten."),
    ("schedule", "A bus table shows Route A at 8:10 and Route B at 8:25. If you need the earlier bus, which should you choose?", ["Route A", "Route B", "Either route because they leave together", "Neither route because no time is shown"], "A", "8:10 is earlier than 8:25, so Route A is the earlier choice."),
    ("average-free inference", "A chart shows three students read 2, 4, and 6 books. Which conclusion can be made without calculating an average?", ["The student who read 6 read more than the other two.", "Every student read exactly 4 books.", "The class read no books before this chart.", "The chart proves why each student chose the books."], "A", "The individual values directly support the comparison, but not the unsupported claims."),
    ("scale reading", "On a bar chart, each grid line represents 10 visitors. A bar reaches the third grid line. How many visitors does it represent?", ["30", "3", "13", "100"], "A", "Three grid intervals at ten visitors each give 30 visitors."),
    ("trend limitation", "A line chart rises from January to March and then falls in April. Which statement is careful?", ["The value rose through March and then decreased in April.", "The value will certainly rise again in May.", "The chart proves the reason for every change.", "The value stayed constant for four months."], "A", "The statement reports only the visible trend and avoids predicting or inventing a cause."),
    ("integrated chart reading", "A school table shows a concert at 2:00 in Hall A, a workshop at 3:00 in Hall B, and a talk at 4:00 in Hall A. Which plan follows the table?", ["Attend the concert at 2:00 in Hall A, then the workshop at 3:00 in Hall B.", "Attend the workshop at 2:00 in Hall A, then the concert at 3:00 in Hall B.", "Attend every event at 4:00 in Hall B.", "The table gives times but no locations."], "A", "The plan preserves the time, event, and location for the first two entries."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取簡易圖表、表格與資料判讀能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以表格、圖表、時間、單位、數量、排序與趨勢測量資料擷取及有限推論；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the chart or table and identify the data task: {topic}.",
        "Check the title, labels, units, categories, times, and scale before comparing any numbers.",
        f"Read the relevant values and select the statement supported by the displayed data; the correct answer is {answer}.",
        f"Show the numerical or label evidence: {explanation}",
        "Reread the conclusion against the chart and mark any claim that goes beyond what the displayed data can prove.",
    ]
    return {"id": f"question-english-performance-3-iv-4-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-3-iv-4"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies simple chart and table reading patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; data, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-3-iv-4", "examPatternRefs": refs, "solutionStrategy": "Read labels and units first, locate the requested category or value, calculate only the needed comparison, and state a conclusion no broader than the chart supports.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-3-iv-4-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
