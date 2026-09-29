import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "comparison, classification, ranking, tables, and practical information"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "sorting data, grouping features, comparing values, and criteria"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "reading charts and organizing information by evidence"),
]

DATA = [
    ("ascending order", "A table lists walking times of 12, 8, 15, and 10 minutes. Which order is shortest to longest?", ["8, 10, 12, 15", "15, 12, 10, 8", "10, 8, 15, 12", "12, 15, 8, 10"], "A", "Ascending order begins with the smallest value and ends with the largest."),
    ("descending order", "Scores are 76, 91, 84, and 68. Which score should appear first when ranking from highest to lowest?", ["91", "68", "76", "84"], "A", "91 is the largest score, so it comes first in descending order."),
    ("classification", "A list includes apples, carrots, rice, and bananas. Which group contains only fruits?", ["Apples and bananas", "Carrots and rice", "Apples and rice", "Carrots and bananas"], "A", "Apples and bananas are fruits, while carrots and rice belong to other food categories."),
    ("shared feature", "A chart groups buses and trains under 'public transportation' and bicycles under 'personal transportation.' What feature is used?", ["How people use the vehicle to travel", "The color of each vehicle", "The length of every road", "The price of one ticket only"], "A", "The category is based on whether transportation is shared or personal."),
    ("comparison", "A table shows Book A has 120 pages and Book B has 95 pages. Which statement is correct?", ["Book A is 25 pages longer than Book B", "Book B is 25 pages longer than Book A", "Both books have the same number of pages", "The table does not show page numbers"], "A", "Subtracting 95 from 120 gives a 25-page difference."),
    ("criteria", "A student must choose the cheapest bus that arrives before 8:00. Which information must be compared?", ["Price and arrival time", "Bus color and driver name", "Seat fabric and route length only", "The day of the student's birthday"], "A", "Both conditions are required, so price and arrival time must be checked together."),
    ("category exception", "A list groups activities by indoor and outdoor location. Swimming is held in an indoor pool. Where should it be classified?", ["Indoor activities", "Outdoor activities", "Both categories automatically", "Neither category because water is involved"], "A", "The location is indoors even though the activity involves water."),
    ("rank with tie", "A race table shows Mia and Lee both finish in 14 minutes, while Sam finishes in 16. What is true?", ["Mia and Lee share the faster time", "Sam is faster than both", "Only Lee has a recorded time", "All three have different times"], "A", "The equal values create a tie, and 14 is faster than 16."),
    ("multi-step sort", "A chart lists four parks with distance and entrance fee. To find the nearest park that costs less than $5, what should you do?", ["Filter fees below $5, then compare the remaining distances", "Choose the farthest park before checking its fee", "Compare names alphabetically and ignore both numbers", "Add all fees and choose the largest total"], "A", "The condition must be applied first, followed by the requested distance comparison."),
    ("integrated organization", "A report has animal names, habitats, body lengths, and endangered status. Which organization best supports a reader who wants endangered animals from shortest to longest?", ["Filter by endangered status, then sort the matching animals by body length", "Sort all animals by name and ignore status and length", "Group by habitat only and remove body lengths", "Choose the largest animal before checking whether it is endangered"], "A", "The plan applies the requested category first and the requested numeric order second."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取比較、分類、排序、條件篩選、表格數值與資料組織能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以時刻表、數字、圖表與生活資料要求依條件比較、分類、由高低排序、處理同值並整合多欄證據；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the data task and identify the organization target: {topic}.",
        "Write down the comparison direction, category rule, numeric unit, tie condition, and every filter or criterion.",
        f"Apply the criteria in order and compare only the matching values; the correct answer is {answer}.",
        f"Explain how the data structure supports the classification, ranking, or comparison: {explanation}",
        "Reread the table and verify that no row, unit, tie, or condition was skipped or reversed.",
    ]
    return {"id": f"question-english-performance-9-iv-2-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-performance-9-iv-2"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies comparison, classification, sorting, ranking, filtering, ties, and table organization only and does not reproduce an original question, option, image, or table.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; data sets, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-performance-9-iv-2", "examPatternRefs": refs, "solutionStrategy": "Identify the requested category or order, apply filters before ranking when required, compare the correct values, and verify units and ties.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-performance-9-iv-2-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
