import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "charts, tables, reading comprehension, and practical English use"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "English data reading, notices, and contextual inference"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "short texts, data comparison, and application tasks"),
]

DATA = [
    ("chart title", "A chart is titled 'How Class 8A Travels to School.' What information is the chart most likely about?", ["Students' ways of traveling to school.", "The colors of the classroom walls.", "Teachers' favorite books.", "The weather in another country."], "Students' ways of traveling to school.", "The title identifies both the group, Class 8A, and the topic, ways of traveling to school. A chart title sets the scope before any numbers are read."),
    ("highest value", "A table lists library visits: Monday 12, Tuesday 18, Wednesday 9, Thursday 15. On which day were there the most visits?", ["Tuesday", "Monday", "Wednesday", "Thursday"], "Tuesday", "The largest value is 18, and it appears next to Tuesday. Finding the maximum requires comparing all four entries."),
    ("lowest value", "A bar chart shows reusable bottles collected: Team A 7, Team B 11, Team C 5, Team D 9. Which team collected the fewest?", ["Team C", "Team A", "Team B", "Team D"], "Team C", "The smallest number is 5, which belongs to Team C. Fewest means the lowest quantity, not the team listed first."),
    ("difference", "A chart records 24 students choosing fruit and 16 choosing bread for breakfast. How many more students chose fruit?", ["8", "10", "40", "6"], "8", "Subtract the smaller count from the larger count: 24 - 16 = 8. The question asks for the difference, not the total."),
    ("total", "A table shows three days of water use: Monday 30 liters, Tuesday 25 liters, Wednesday 35 liters. What was the total?", ["90 liters", "60 liters", "65 liters", "95 liters"], "90 liters", "Add the three daily amounts: 30 + 25 + 35 = 90 liters. Total means combine every listed value."),
    ("trend", "A line graph shows the number of seedlings as 4 in April, 7 in May, and 10 in June. What trend does it show?", ["The number increased each month.", "The number decreased each month.", "The number stayed exactly the same.", "The graph gives no month information."], "The number increased each month.", "The values rise from 4 to 7 to 10, so the graph shows an upward trend over the three months."),
    ("legend", "In a weather chart, a blue key means 'rainy' and a yellow key means 'sunny.' Tuesday's bar is yellow. What was Tuesday's weather?", ["Sunny", "Rainy", "Windy", "Snowy"], "Sunny", "The legend explains the colors. Because yellow is defined as sunny, Tuesday's yellow bar represents sunny weather."),
    ("unit and label", "A snack chart labels its vertical axis 'Number of students' and shows 14 beside apples. What does 14 represent?", ["Fourteen students chose apples.", "The apples weigh fourteen kilograms.", "The survey lasted fourteen months.", "There are fourteen kinds of fruit."], "Fourteen students chose apples.", "The vertical-axis label supplies the unit: number of students. Therefore 14 is the count of students in the apple category."),
    ("evidence limit", "A survey shows that 20 of 30 students prefer reading after school. Which conclusion is directly supported?", ["Reading is the most popular choice in this survey.", "Every student in the city prefers reading.", "Reading always improves grades.", "No student prefers another activity."], "Reading is the most popular choice in this survey.", "The data support a statement about this survey and its respondents. They do not justify claims about every student, grades, or the absence of other preferences."),
    ("integrated chart action", "A class chart shows recycling rose from 10 kg in March to 18 kg in April. The goal for May is 20 kg. Which statement is best?", ["The class needs 2 more kilograms than April's amount to reach the May goal.", "The class already collected 20 kg in April.", "Recycling fell by 8 kg from March to April.", "The chart proves no one recycled in May."], "The class needs 2 more kilograms than April's amount to reach the May goal.", "April has 18 kg and the goal is 20 kg, so 20 - 18 = 2 kg more is needed. The other statements contradict or go beyond the chart."),
]


def make(index, row):
    tag, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    answer_id = next(option["id"] for option in options if option["text"] == answer)
    refs = [{
        "url": url, "title": f"{title}; pattern-only study, no original item or option copied.", "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "Public-school English assessments use tables, graphs, labels, comparison, arithmetic from data, and evidence-limited inference; this is an independent rewrite without copying wording, options, figures, or answers.",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"Read the chart prompt and identify the data skill: {tag}.",
        f"Locate the title, labels, legend, values, units, or time points before calculating or inferring; apply this rule: {explanation}",
        f"Check option {answer_id}: {answer}",
        "Reject the other options by checking every number against the correct category and unit, and by refusing conclusions that the displayed data cannot support.",
        "State the evidence from the table or graph in a complete sentence, then explain whether the task required locating, comparing, calculating, or cautiously inferring.",
    ]
    return {
        "id": f"question-english-content-ae-iv-2-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-ae-iv-2"], "difficulty": "medium",
        "answer": {"value": answer_id, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "Public-school English assessment materials; this item studies assessment patterns only and does not reproduce an original question, option, image, or answer.", "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; data contexts, values, options, explanation, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-ae-iv-2", "examPatternRefs": refs,
        "solutionStrategy": "Read the chart's title, labels, legend, units, and values in that order; then perform only the comparison or calculation asked for and keep the conclusion within the displayed evidence.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-ae-iv-2-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
