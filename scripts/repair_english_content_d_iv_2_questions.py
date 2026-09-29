import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "comparison, categorization, and ordered information"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "tables, schedules, quantities, and detail selection"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional reading, comparison, and practical decisions"),
]

DATA = [
    ("ascending numbers", "A list gives four plants' heights: fern 12 cm, rose 25 cm, mint 8 cm, and lily 18 cm. Which order is shortest to tallest?", ["mint, fern, lily, rose", "rose, lily, fern, mint", "fern, mint, rose, lily", "lily, rose, mint, fern"], "A", "Ordering 8, 12, 18, and 25 from smallest to largest gives mint, fern, lily, rose."),
    ("time order", "The school events are: club fair at 9:00, lunch at 12:10, rehearsal at 10:30, and bus departure at 4:00. Which schedule is chronological?", ["club fair, rehearsal, lunch, bus departure", "lunch, club fair, rehearsal, bus departure", "rehearsal, club fair, bus departure, lunch", "bus departure, lunch, rehearsal, club fair"], "A", "The times increase from 9:00 to 10:30 to 12:10 to 4:00, matching the first option."),
    ("price and size", "Which drink is the best value if the choices are 300 mL for $30, 500 mL for $45, and 700 mL for $70?", ["300 mL for $30", "500 mL for $45", "700 mL for $70", "They all have the same price per mL"], "B", "The approximate prices per 100 mL are 10, 9, and 10, so the 500 mL drink has the lowest unit price."),
    ("functional category", "A table lists a raincoat, umbrella, sandals, and wool scarf. Which pair belongs in the 'rain protection' category?", ["raincoat and umbrella", "sandals and wool scarf", "umbrella and wool scarf", "raincoat and sandals"], "A", "A raincoat and umbrella directly protect a person from rain; the other items serve different purposes."),
    ("shared condition", "The library rules say: books A and B may be borrowed for 14 days, book C for 7 days, and reference book D cannot leave the library. Which books share the 14-day rule?", ["A and B", "B and C", "C and D", "A and D"], "A", "Only A and B have the stated 14-day borrowing period."),
    ("filtering a table", "A club requires members to be at least 13 years old and available on Saturday. The list shows Ana, 13 and Saturday; Ben, 14 and Sunday; Cara, 12 and Saturday; Dan, 15 and Saturday. Who qualifies?", ["Ana and Dan", "Ben and Cara", "Ana and Cara", "Ben and Dan"], "A", "Ana and Dan meet both conditions: age 13 or older and Saturday availability."),
    ("descending order", "A chart records weekly recycling totals: Week 1 = 16 kg, Week 2 = 24 kg, Week 3 = 11 kg, Week 4 = 20 kg. Which is greatest to least?", ["Week 2, Week 4, Week 1, Week 3", "Week 3, Week 1, Week 4, Week 2", "Week 4, Week 2, Week 3, Week 1", "Week 1, Week 3, Week 2, Week 4"], "A", "The values in descending order are 24, 20, 16, and 11 kg."),
    ("two-category classification", "A trip checklist has passport, water bottle, camera, and rain jacket. Which classification puts items needed for entry documents together?", ["passport only", "water bottle and rain jacket", "camera and passport", "all four items"], "A", "Among the listed items, only the passport is an entry document; the others are equipment or personal supplies."),
    ("compare conditions", "Three buses take 20, 35, and 25 minutes. A student must arrive within 30 minutes. Which buses meet the time condition?", ["The 20-minute and 25-minute buses", "The 35-minute bus only", "All three buses", "None of the buses"], "A", "Both 20 and 25 minutes are within 30 minutes; 35 minutes is not."),
    ("integrated choice", "A workshop table lists: A, Monday, $40, 20 seats; B, Tuesday, $30, 12 seats; C, Monday, $35, 18 seats. You need Monday, a price below $40, and at least 18 seats. Which workshop fits?", ["Workshop A", "Workshop B", "Workshop C", "Both B and C"], "C", "Workshop C satisfies all three filters: Monday, $35, and 18 seats; A is not below $40 and B is on Tuesday."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；僅取比較分類排序能力方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "english", "locator": locator, "observedPattern": "公開英文評量常以表格、時間表、數量、價格、功能與條件資料要求比較、分類、排序及篩選；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"Read the list or table and identify the comparison operation: {topic}.",
        "Write down the exact standard: shortest, earliest, cheapest per unit, same category, all conditions, greatest, or another stated rule.",
        f"Apply that standard to every item and choose the option that satisfies it; the correct answer is {answer}.",
        f"Show the comparison or calculation: {explanation}",
        "Check that no item was skipped and that the order direction or all required filters match the wording of the question.",
    ]
    return {"id": f"question-english-content-d-iv-2-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-english-content-d-iv-2"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies comparison, categorization, ordering, and filtering patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; lists, conditions, options, explanations, and transfer tasks are original; pending second-round AI/Terra content review."}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-d-iv-2", "examPatternRefs": refs, "solutionStrategy": "Identify the requested standard and direction first, then normalize the relevant numbers, times, categories, or conditions before comparing every candidate.", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-d-iv-2-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
