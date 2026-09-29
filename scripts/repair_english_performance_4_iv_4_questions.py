import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-4-iv-4"
KG = "kg-english-performance-4-iv-4"
SOURCES = [
    {
        "url": "https://www.chhs.tp.edu.tw/uploads/1657612547412Wif0qWRZ.pdf",
        "title": "臺北市立景興國中110學年度第2學期七年級第2次定期評量英文科試題",
        "year": "110-2",
        "locator": "PDF第2頁第31至33題：閱讀兩份原創回饋表，按欄位擷取偏好、同行者與營業資訊。",
        "observedPattern": "題目先指定表單欄位，再要求從對應列／欄或附註找出資料；本題採全新人物、數值與表格。",
    },
    {
        "url": "https://www.csjh.kh.edu.tw/teach/exam/107%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83/%E8%8B%B1%E6%96%87/%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立中山國中107學年度第2學期第3次段考一年級英文科試題",
        "year": "107-2",
        "locator": "PDF第6頁第45至48題：閱讀雜誌訂閱表與訂戶欄位，判讀期數、價格、年齡、職業、電話及選項。",
        "observedPattern": "將勾選項目、欄位資料與表格旁的說明合併核對；本題改用不同表單用途與數值。",
    },
    {
        "url": "https://www.chhs.tp.edu.tw/uploads/1612148562952u1jdsAwR.pdf",
        "title": "臺北市立景興國中109學年度第1學期八年級第2次定期評量英文科試題",
        "year": "109-1",
        "locator": "PDF第2頁第31至32題：依社團對話與報名表資訊判斷加入方式、截止日及活動安排。",
        "observedPattern": "表格閱讀需分清表內明列事實與對話指示，並依問題要求核對欄位或期限；本題採全新情境。",
    },
]


def refs():
    return [
        {
            **source,
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "subject": "english",
            "locatorLevel": "item",
        }
        for source in SOURCES
    ]


ITEMS = [
    {
        "prompt": "A science-day form reads: Student—Nora Lin; Grade—7; Session—Plant Lab; Arrival—8:40 a.m. Which value belongs in the Session box?",
        "options": {"A": "8:40 a.m.", "B": "Plant Lab", "C": "Nora Lin", "D": "7"},
        "answer": "B",
        "explanation": "Session asks which activity Nora registered for. Plant Lab is the activity; 8:40 is the arrival time, Nora Lin is the student, and 7 is the grade.",
        "strategy": "把欄位名稱先翻成它要的資料種類，再比對表單中的值；同一張表的時間、姓名與年級不能互換。",
        "steps": ["圈出題目指定的欄位 Session。", "判斷 Session 要填活動名稱，不是人名或時間。", "回到同一筆報名資料找活動：Plant Lab。", "排除 Nora Lin、7 與 8:40 a.m.，它們分別是姓名、年級和報到時間。", "選 B，並確認答案完整對應欄位。"],
    },
    {
        "prompt": "A library request lists: Book—Cloud Atlas for Kids; Member ID—L204; Pickup day—Thursday; Copies—2. How many copies should the library prepare?",
        "options": {"A": "Thursday", "B": "L204", "C": "2", "D": "Cloud Atlas for Kids"},
        "answer": "C",
        "explanation": "Copies records the requested quantity, which is 2. Thursday is the pickup day, L204 identifies the member, and Cloud Atlas for Kids is the title.",
        "strategy": "看到問數量時，找 Copies／Quantity 這類欄名；不要把日期或識別碼當成數量。",
        "steps": ["找出問題問的是 how many copies，也就是要找副本數量。", "在申請單中定位 Copies 欄，不要先看日期或會員代碼。", "沿著這個欄位讀出數值 2，並確認它對應這筆借閱申請。", "檢查 Thursday、L204 和書名各屬不同欄位，不能拿來回答數量。", "選 C；題目只問副本數，不要求加總或換算其他資料。"],
    },
    {
        "prompt": "A club form says: Applicant—Evan; Club—Chess; Meeting—Friday; Room—204. Where will Evan meet the club?",
        "options": {"A": "Chess", "B": "Evan", "C": "Friday", "D": "Room 204"},
        "answer": "D",
        "explanation": "The question asks for the meeting place. Room 204 is the location; Friday gives the day, Chess names the club, and Evan is the applicant.",
        "strategy": "把 where 對應到地點欄，再把 day、club 和 person 等近似線索排除。",
        "steps": ["辨認疑問詞 where：要找地點。", "查看表單的 Meeting 與 Room 欄，確認哪欄回答地點。", "Room 欄填的是 204。", "Friday 是日期／星期，Chess 是社團，Evan 是姓名。", "選 D，保留 Room 204 的完整地點資訊。"],
    },
    {
        "prompt": "A snack survey records: Pear—11 votes; Melon—6 votes; Guava—9 votes. Which fruit received the fewest votes?",
        "options": {"A": "Melon", "B": "Guava", "C": "Pear", "D": "All received the same number"},
        "answer": "A",
        "explanation": "Compare the vote counts attached to each fruit: Pear has 11, Melon has 6, and Guava has 9. Since 6 is smaller than both 9 and 11, Melon received the fewest votes.",
        "strategy": "題目問最少時逐一比較同一欄的計數；先確認每個數字都對應正確類別，再找最小值。",
        "steps": ["列出調查表的配對：Pear 11、Melon 6、Guava 9。", "確認比較的是 votes 數，而不是水果名稱。", "比較 11、6、9，最小值是 6。", "回查 6 所在的類別是 Melon。", "選 A；不能因 Melon 出現在第二列就誤讀為第二多。"],
    },
    {
        "prompt": "A weekend workshop registration shows: Name—Mia; Email—mia.chen@example.org; Fee—$350; Paid—Yes. Which field confirms that Mia has paid?",
        "options": {"A": "Email", "B": "Paid", "C": "Fee", "D": "Name"},
        "answer": "B",
        "explanation": "Paid is the status field and its value is Yes. The fee is an amount owed or charged; it does not by itself confirm payment.",
        "strategy": "問狀態是否完成，要讀狀態欄及其值，不能把金額或聯絡方式當作完成證明。",
        "steps": ["抓出題目關鍵：confirms that Mia has paid，問題在問付款是否完成。", "在表單找到表示付款狀態的欄位 Paid，而不是金額欄。", "讀取 Paid 欄的值 Yes，這是明確的已付款狀態。", "區分 Fee $350（金額）和 Email（聯絡資訊），它們都不能單獨證明款項已付。", "選 B，因為欄名 Paid 與值 Yes 合在一起才是付款完成的證據。"],
    },
    {
        "prompt": "Two feedback cards show: Rui—visit date 6/12—liked the soup; Ada—visit date 6/19—liked the music. Who visited later?",
        "options": {"A": "Rui", "B": "They visited on the same day", "C": "Ada", "D": "The cards do not show dates"},
        "answer": "C",
        "explanation": "Both feedback cards provide a visit date. Compare June 19 with June 12: the nineteenth is later than the twelfth, and the June 19 date appears on Ada's card.",
        "strategy": "比較日期前先將每個日期連回同一張表單的姓名，避免只找到日期卻配錯人。",
        "steps": ["在兩張卡中找 visit date 欄。", "建立姓名與日期配對：Rui—6/12；Ada—6/19。", "同為六月，比較日數 19 與 12。", "確認較晚的 6/19 屬於 Ada。", "選 C；不是根據喜歡的項目推測到訪時間。"],
    },
    {
        "prompt": "A delivery order has: 3 notebooks at $28 each; 1 folder at $36. What is the total price?",
        "options": {"A": "$64", "B": "$84", "C": "$92", "D": "$120"},
        "answer": "D",
        "explanation": "Three notebooks cost 3 × $28 = $84. The folder adds $36, so the full order costs $84 + $36 = $120. The quantity, unit price, and other item's price must be combined in that order.",
        "strategy": "逐項用數量乘單價，再加總；核算時把中間乘積和最後合計分開檢查。",
        "steps": ["找出每項的 quantity 與 unit price。", "計算筆記本：3 × $28 = $84。", "計算資料夾：1 × $36 = $36。", "合計 $84 + $36 = $120，回查選項。", "選 D；$92 是把單價與數量混加造成的錯誤。"],
    },
    {
        "prompt": "A volunteer form lists: Contact person—Leo; Phone—0912-345-678; Task—guide visitors; Shift—afternoon. Which value should be copied into the Phone field?",
        "options": {"A": "afternoon", "B": "guide visitors", "C": "Leo", "D": "0912-345-678"},
        "answer": "D",
        "explanation": "The Phone field contains 0912-345-678. The other values identify the shift, task, and contact person.",
        "strategy": "依欄名辨認資料型態，抄電話時保持完整數字與連字號，不要把姓名或工作內容填入。",
        "steps": ["定位題目指定的 Phone 欄。", "確認它要求電話號碼這種資料型態。", "從表單抄下 0912-345-678。", "排除 Leo、guide visitors 和 afternoon，它們分屬姓名、任務和班別。", "選 D，保留全部號碼與原格式。"],
    },
    {
        "prompt": "A timetable form gives: Check-in—9:10; Group talk—9:30; Break—10:15; Lab—10:30. Which activity starts immediately after the break?",
        "options": {"A": "Group talk", "B": "Lab", "C": "Check-in", "D": "The form gives no later activity"},
        "answer": "B",
        "explanation": "The schedule places Break at 10:15 and then lists Lab at 10:30. Since 10:30 is the next later entry, Lab is the activity that begins immediately after the break; the 9:30 talk occurs earlier.",
        "strategy": "先按時間順序定位指定事件，再讀下一筆活動；不要把前一個時段當作「之後」。",
        "steps": ["找出題目中的 break，定位 10:15。", "查看時間表中下一個較晚的時段。", "10:30 的活動是 Lab。", "排除 9:30 的 Group talk 和 9:10 的 Check-in，兩者都早於休息。", "選 B，因為它是休息後緊接著列出的活動。"],
    },
    {
        "prompt": "A meal-choice form says: Student—Jo; Main dish—bean rice; Side—cucumber salad; Drink—water; Note—no peanuts. What is Jo's main dish?",
        "options": {"A": "Water", "B": "Cucumber salad", "C": "Bean rice", "D": "Peanuts"},
        "answer": "C",
        "explanation": "Bean rice is entered specifically in the Main dish field. Cucumber salad and water are listed under Side and Drink, while the note no peanuts is a dietary restriction rather than the selected main dish.",
        "strategy": "多欄表單先鎖定 Main dish，再分辨 side、drink 與 dietary note，不能只挑看起來像食物的值。",
        "steps": ["圈出問題問 main dish。", "回到 Jo 的資料列讀 Main dish 欄。", "該欄值是 bean rice。", "Cucumber salad 是 side、water 是 drink、no peanuts 是限制備註。", "選 C，因為它是指定欄位的內容且沒有違反備註。"],
    },
]

for index, item in enumerate(ITEMS, start=1):
    item_id = f"question-english-performance-4-iv-4-{index}"
    source = SOURCES[(index - 1) % len(SOURCES)]
    question = {
        "id": item_id,
        "subject": "english",
        "type": "single-choice",
        "prompt": item["prompt"],
        "options": [{"id": key, "text": value} for key, value in item["options"].items()],
        "knowledgeIds": [KG],
        "difficulty": "medium" if index in {4, 6, 7, 9, 10} else "easy",
        "answer": {"value": item["answer"], "explanation": item["explanation"]},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": source["url"],
            "sourceLocator": source["locator"],
            "authoringNote": "依官方課綱知識節點及公立國中公開英文表格／表單題的資料定位能力方向自行創作；未複製原卷內容。仍待完整內容與授權界線複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-26",
        "lessonId": LESSON,
        "examPatternRefs": refs(),
        "solutionStrategy": item["strategy"],
        "solutionSteps": item["steps"],
    }
    (OUT / f"{item_id}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n")

print(json.dumps({"rewritten": len(ITEMS), "unit": LESSON, "draftPreserved": True}, ensure_ascii=False))
