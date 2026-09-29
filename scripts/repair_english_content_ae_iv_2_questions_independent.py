#!/usr/bin/env python3
"""Independent English Ae-IV-2 chart and table reading rewrite."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-content-ae-iv-2"
SOURCES = [
    ("https://www.kusjh.kh.edu.tw/upload/files/110%E4%B8%8A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E5%9C%8B%E4%B8%AD%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立鼓山高中國中部七年級公開英語段考", "短文資訊、數字與表格理解"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中七年級公開英語段考", "生活資料、比較與閱讀推論"),
    ("https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "高雄市立大社國中七年級公開英語段考", "數據、時間與簡易圖表題型"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "110-114", "subject": "english", "locator": l, "observedPattern": "公立學校國中英語評量要求閱讀表格或簡易圖表的標題、單位、數值、排序、比較、時間趨勢與資料限制；本題採全新資料。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l in SOURCES]

DATA = [
    ("A table shows **Monday 12 books, Tuesday 18 books, Wednesday 15 books** borrowed. Which day has the highest number?", ["Monday", "Tuesday", "Wednesday", "All days are equal"], "A", "Tuesday has 18 books, which is greater than 12 and 15.", "先確認比較的是數值，再找最大值而非只看日期順序。", ["Read the three day labels.", "Record the values 12, 18 and 15.", "Compare the numbers.", "Identify 18 as the maximum.", "Match 18 with Tuesday."]),
    ("A chart shows bus riders: Route A 20, Route B 35, Route C 25. How many more riders use B than A?", ["5", "10", "15", "55"], "A", "Subtract 20 from 35: 35 - 20 = 15.", "先找兩個指定資料，再用大數減小數。", ["Locate Route B and its value 35.", "Locate Route A and its value 20.", "Set up 35 - 20.", "Calculate 15.", "Check that 55 is a sum, not a difference."]),
    ("A weekly chart lists temperatures: Mon 20°C, Tue 22°C, Wed 22°C, Thu 19°C. What is true?", ["Tuesday and Wednesday have the same temperature.", "Thursday is the hottest.", "Monday is warmer than Tuesday.", "All four days are equal."], "A", "Both Tuesday and Wednesday are listed as 22°C, so they share the highest temperature.", "逐項對照數值，注意相同值與最高值可以同時成立。", ["Read the temperature for each day.", "Compare Tuesday and Wednesday.", "Confirm both are 22°C.", "Compare 22 with the other values.", "Choose the statement supported by the table."]),
    ("A bar chart shows reading minutes: Ana 30, Ben 20, Cara 40. Who reads the longest?", ["Ana", "Ben", "Cara", "They read the same amount"], "A", "Cara has 40 minutes, the largest value in the chart.", "找最大柱值並回到對應的人名。", ["List each person's minutes.", "Identify the largest number.", "Match 40 with Cara.", "Ignore the order of the names.", "Choose Cara."]),
    ("A table shows an event starts at 9:00 and ends at 11:30. How long does it last?", ["1 hour", "2 hours", "2 hours 30 minutes", "3 hours 30 minutes"], "A", "From 9:00 to 11:30 is two hours and thirty minutes.", "把時間切成整小時和剩餘分鐘計算。", ["Move from 9:00 to 11:00.", "Count the remaining 30 minutes.", "Combine the two parts.", "Choose 2 hours 30 minutes.", "Check that the answer is shorter than a full four-hour period."]),
    ("A chart says **Favorite fruit: apples 8, bananas 5, oranges 8**. Which statement is supported?", ["Apples and oranges are equally popular.", "Bananas are the most popular.", "Only one student likes oranges.", "The total is 8 students."], "A", "Apples and oranges both have a count of 8, so the chart shows a tie.", "先找相等數值，再區分並列第一與總人數。", ["Read the three counts.", "Compare apples and oranges.", "Notice both are 8.", "Choose the equal-popularity statement.", "Do not confuse one category's count with the total."]),
    ("A line chart rises from 10 visitors in April to 16 in May, then falls to 12 in June. What happened from May to June?", ["Visitors increased by 4.", "Visitors decreased by 4.", "Visitors stayed at 16.", "There were no visitors."], "A", "The value drops from 16 to 12, a decrease of 4 visitors.", "先判斷線段方向，再計算前後數值差。", ["Read May's value 16.", "Read June's value 12.", "Notice the line falls.", "Calculate 16 - 12 = 4.", "Choose decreased by 4."]),
    ("A table records water use in liters: Class 1 40, Class 2 35, Class 3 50. Which class used the least?", ["Class 1", "Class 2", "Class 3", "The table does not show it"], "A", "35 liters is the smallest value, so Class 2 used the least.", "題目問 least，要找最小值而不是最大值。", ["List 40, 35 and 50.", "Identify that least means smallest.", "Find 35.", "Match it with Class 2.", "Check that the unit is liters for every class."]),
    ("A chart title says **Students' transport to school**, but the categories have no numbers. What can a reader conclude?", ["The chart's topic is clear, but the most common transport cannot be identified.", "Buses are definitely the most common.", "Every student walks.", "The chart proves the school is far away."], "A", "The title tells the topic, but without category values the chart cannot support a ranking or cause about transportation.", "先分辨圖表已提供的資訊與缺少的數值，不用猜測結果。", ["Read the chart title.", "Identify the subject being measured.", "Check whether categories have values.", "State what the missing numbers prevent us from knowing.", "Choose the limited conclusion."]),
    ("A recycling chart records 6 kg in Week 1, 6 kg in Week 2 and 9 kg in Week 3. What is the total?", ["15 kg", "18 kg", "21 kg", "27 kg"], "A", "Add the three weekly values: 6 + 6 + 9 = 21 kg.", "確認單位相同後，逐項相加而非只取最高值。", ["Read all three weekly quantities.", "Confirm every value is in kilograms.", "Add 6 + 6.", "Add 9 to get 21.", "Choose the total with the correct unit."]),
]

assert len(DATA) == 10
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]
for i, (prompt, options, answer, explanation, strategy, steps) in enumerate(DATA, 1):
    target = TARGETS[i - 1]
    if target != answer:
        oi, ti = ord(answer) - 65, ord(target) - 65
        correct = options[oi]
        rest = [v for j, v in enumerate(options) if j != oi]
        options = rest[:ti] + [correct] + rest[ti:]
        answer = target
    item = {"id": f"question-english-content-ae-iv-2-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(options)], "knowledgeIds": ["kg-english-content-ae-iv-2"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公立學校七年級英語段考；只研究簡易表格、圖表、數值比較、時間、趨勢與資料限制題型。", "authoringNote": "依官方英語文領域課綱、單元 KG 與三個公立學校公開來源，獨立改寫常見圖表題；未複製原文、選項、篇章、圖片或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}
    (OUT / f"question-english-content-ae-iv-2-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
