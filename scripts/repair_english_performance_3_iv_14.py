import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "questions/english"
SOURCES = [
    ("https://www.nhjh.tp.edu.tw/uploads/1706770089045DwNPg1SE.pdf", "臺北市立內湖國中112學年度第1學期七年級第3次段考英文", "112-1"),
    ("https://www.nhjh.tp.edu.tw/uploads/1753840039444z3K5m38Y.pdf", "臺北市立內湖國中113學年度第2學期八年級第1次段考英文", "113-2"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國中114學年度第2學期九年級第1次段考英文", "114-2"),
]
ITEMS = [
    {
        "prompt": "A school page has the heading ‘Repair Café’, then subheadings ‘Bring’, ‘When’, and ‘Where’. You have half a minute to decide whether to go. What should you do first?",
        "options": ["Read the headings to predict the page’s sections, then scan the time and place", "Translate every sentence in the history section", "Count how often the word ‘café’ appears without checking details", "Read only the last line and assume it gives the address"],
        "key": "A", "skill": "標題與版面預覽後鎖定任務資訊", "strategy": "先用標題預測資訊分類，再依出席決策掃描時間、地點，最後回看相應欄位。",
        "steps": ["把任務改寫成「是否能到場」，列出必需資訊是時間與地點。", "先讀主標和小標，預測頁面把物品、時間、地點分開說明。", "直接掃描 When、Where 及其後的日期、時刻、地址。", "不要把活動介紹或單獨出現的數字誤當成答案。", "回讀時間與地點所在欄位，確認資訊屬於同一場活動。"], "locators": ["第4頁閱讀題組（一）第48–50題：公告主旨、代名詞及情境行動", "第3頁閱讀題組A第27–34題：段落資訊與問題定位", "第3頁閱讀題組第39–44題：依敘事段落尋找事件細節"]
    },
    {
        "prompt": "A short recycling notice says ‘Wash bottles before placing them in the blue bin’ in both the opening and the final reminder. Which idea deserves attention when skimming?",
        "options": ["The repeated instruction is central to using the bin correctly", "The notice is mainly about the history of blue paint", "The same instruction appears twice, so it must be ignored", "The bin is a person who needs to be washed"],
        "key": "A", "skill": "辨認重複細節所凸顯的核心指示", "strategy": "重複不是直接等於主旨；先辨認它是否反覆服務同一個行動目的。",
        "steps": ["確認閱讀任務是抓重要指示，而非統計出現次數。", "圈出重複的動作與對象：洗淨瓶子後放入藍桶。", "檢查開頭與結尾是否都把這個動作連到正確回收。", "排除只抓顏色、把桶當人物或因重複而略讀的選項。", "用一句話重述規則，並確認沒有擴大成公告未說的要求。"], "locators": ["第4頁閱讀題組（一）第49題：辨別公告中的真實細節", "第3頁閱讀題組B第35–37題：由短文證據判斷主張", "第3頁閱讀題組第39–44題：回到敘事細節辨認重點"]
    },
    {
        "prompt": "A paragraph opens with ‘The garden beds dried out during the school break’ and ends with ‘Now each class takes a watering turn’. What is the best quick summary?",
        "options": ["The school organized shared watering after the garden dried", "The classes stopped growing plants because they dislike gardens", "The paragraph explains how to build a classroom", "The school proved that gardens never need water"],
        "key": "A", "skill": "以段首問題與段末回應概括段意", "strategy": "比較段首提出的狀況和段末採取的回應，摘要保留兩者關係而不添油加醋。",
        "steps": ["快速讀段首，記下問題是放假期間菜床乾掉。", "跳到段末，抓出後續作法是各班輪流澆水。", "把問題和回應接成一個因果／解決摘要。", "排除忽略問題、只說活動，或把結論誇張成永不缺水的選項。", "回頭檢查摘要每個資訊是否都能在段首或段末找到依據。"], "locators": ["第4頁閱讀題組（一）第49題：以短文明示資訊核對敘述", "第3頁閱讀題組B第37題：由文章內容選出可成立的理解", "第3頁閱讀題組第39–44題：綜合段落事件作答"]
    },
    {
        "prompt": "You need the closing time of a community pool. Its page includes a history, safety rules, prices, and a weekly timetable. Which move is most efficient?",
        "options": ["Scan for ‘hours’, weekdays, and time expressions, then verify the correct day", "Read the history from the first sentence and memorize it", "Choose the latest time printed anywhere on the page", "Use the price list to guess the closing time"],
        "key": "A", "skill": "帶著明確目標掃讀時間表", "strategy": "先鎖定要查的日別，再以時間格式掃描；不可把頁面上任一時刻當成營業時間。",
        "steps": ["把問題拆成兩欄：指定日期類型和結束時刻。", "在頁面找 timetable、hours 或開放時間等標示。", "沿著目標日別那一列掃描時間範圍的右端。", "辨認票價、救生員值班或入場時間等其他數字，避免混用。", "回讀表頭和該列，確認讀到的是泳池關閉時刻。"], "locators": ["第4頁閱讀題組（二）票價與開放時間表：依表頭比對日期及時間", "第3頁閱讀題組A第27–34題：依問題回查段落／資料細節", "第3頁閱讀題組第39–44題：定位文本中支援特定問題的資訊"]
    },
    {
        "prompt": "A report lists three ways students reduce lunch waste: choose a smaller serving first, share unopened fruit, and return for more if still hungry. Which is the fairest summary?",
        "options": ["Students use several choices to avoid taking more food than they need", "Every student must eat the smallest serving and cannot ask for more", "The report is mainly about growing fruit trees", "Sharing unopened fruit causes all lunch waste to disappear"],
        "key": "A", "skill": "跨列舉細節整合而不過度概括", "strategy": "把多個例子抽成共同目的，同時保留彈性條件，避免把建議改寫成絕對規定。",
        "steps": ["略讀列舉標記，辨認文中有三種做法。", "找三項共同方向：先少取、分享未拆封食物、需要時再添。", "將它們歸納為依食量取餐以減少剩食。", "排除把其中一項說成全體強制規則或保證零浪費的選項。", "對照每個做法，確定摘要涵蓋共同目的但沒有添加文章未承諾的結果。"], "locators": ["第3頁閱讀題組A第27–34題：統整多個篇章資訊再選答案", "第3頁閱讀題組B第35–37題：判斷概括是否受文章支持", "第3頁閱讀題組第39–44題：跨段整理事件／資訊"]
    },
    {
        "prompt": "The question asks for an article’s main idea. One paragraph briefly mentions a student’s green backpack, while the title and three other paragraphs discuss saving electricity. Which should receive less weight first?",
        "options": ["The one-time backpack example", "The title and repeated electricity-saving focus", "The opening statement about energy use", "The conclusion that returns to saving electricity"],
        "key": "A", "skill": "主旨判斷時區分例子與反覆主線", "strategy": "主旨要覆蓋全文；單一例子通常只支援局部，需和標題、開頭及結尾比較。",
        "steps": ["確認題目問的是全篇主旨，不是背包那一段的細節。", "先記錄標題、三段重複出現的節能焦點及結論。", "把綠色背包標記為只出現一次的局部例子。", "比較哪項資訊能解釋最多段落，而非只和一個例子相連。", "用標題和結論交叉核對主線，確保不是把例子放大成全文主旨。"], "locators": ["第3頁閱讀題組A第27–34題：由段落主線與細節作答", "第3頁閱讀題組B第35–37題：比較文章主張與局部證據", "第3頁閱讀題組第39–44題：辨認敘事主線而非單一細節"]
    },
    {
        "prompt": "A page uses the headings ‘Problem’, ‘What Residents Tried’, and ‘What Changed’. Before reading every line, what organization is most reasonable to expect?",
        "options": ["A local issue, attempted responses, and their results", "A list of unrelated recipes with no shared topic", "A set of character descriptions followed by a poem", "A timetable that contains only departure platforms"],
        "key": "A", "skill": "利用標題層級預測篇章組織", "strategy": "小標能預告段落功能，但只是閱讀假設；讀正文時仍要驗證各段實際內容。",
        "steps": ["依序讀三個小標，不急著逐字閱讀正文。", "把標題轉成可能的功能：提出問題、介紹嘗試、呈現變化。", "預測文章可能採問題—行動—結果的組織。", "提醒自己標題是線索，不是已證明的正文結論。", "閱讀各段首句，逐一驗證它們是否符合預測，必要時修正。"], "locators": ["第3頁閱讀題組C第38–40題：辨認資訊展開與事件順序", "第3頁閱讀題組B第35–37題：標題／主題與段落訊息配合判讀", "第3頁閱讀題組第39–44題：按事件脈絡理解段落發展"]
    },
    {
        "prompt": "A transit website has a long explanation of the city’s rail history. You only need the next train’s platform and departure time. Why should you scan instead of translating each paragraph?",
        "options": ["The question calls for two labeled details, so unrelated history would slow the search", "Translation makes every timetable inaccurate", "Platforms and times are never written with words or numbers", "Reading quickly means you must ignore the platform label"],
        "key": "A", "skill": "依問題需求選擇掃讀而非逐句翻譯", "strategy": "掃讀適合找指定欄位；先讀標籤與目標，再回看局部語句以免把相鄰班次看錯。",
        "steps": ["從題目抽出兩個目標：月台和下一班發車時間。", "先找 departures、platform 等欄名或相應圖示。", "沿著下一班那一列掃描，不逐句處理歷史介紹。", "注意相鄰列的時間可能屬於另一班車，不能只取最近的數字。", "回讀列標、目的地及時間，確認兩個答案指向同一班列車。"], "locators": ["第4頁閱讀題組（二）營業時間與票價表：辨讀標籤後擷取指定欄位", "第3頁閱讀題組A第27–34題：帶著題目返回局部文本取證", "第3頁閱讀題組第39–44題：用問題導向定位關鍵資訊"]
    },
    {
        "prompt": "A festival poster gives a date, venue, two activities, a fee, and an email for registration. Your family is deciding whether to join. Which set is most useful to check together?",
        "options": ["Date, venue, activity, fee, and registration contact", "Only the poster’s color and the illustrator’s name", "Only the activity title, without date or cost", "A sentence from an unrelated school announcement"],
        "key": "A", "skill": "依讀者目的整合公告多項必要資訊", "strategy": "先說清楚決策目的，再選取足以判斷能否參加及如何報名的資訊組合。",
        "steps": ["把讀者目的定為評估是否參加並完成報名。", "逐項檢查時間與地點，判斷家庭是否能到場。", "確認活動內容和費用，判斷是否符合需求與預算。", "找報名聯絡方式，確認採取下一步所需管道。", "把資訊組合回決策情境，排除裝飾資訊或缺少關鍵條件的選項。"], "locators": ["第4頁閱讀題組（一）第50題：依公告情境推斷可採取的行動", "第4頁閱讀題組（二）：由開放時間、票價與附註完成到訪決策", "第3頁閱讀題組第39–44題：結合多處資訊回答具體問題"]
    },
    {
        "prompt": "A reader previews a page’s headings, scans the table for a date, then rereads the matching note before answering. Why is this sequence stronger than relying on the first guess?",
        "options": ["Preview sets direction, scanning locates evidence, and rereading checks the match", "Headings prove every detail, so the table can be skipped", "Scanning means choosing the first number seen", "Rereading is useful only when it changes the topic"],
        "key": "A", "skill": "整合預覽、掃讀與局部回讀的證據流程", "strategy": "把三種閱讀動作分工：預覽建構搜尋地圖、掃讀定位、回讀驗證語境與欄位。",
        "steps": ["說明預覽的功能是建立頁面結構假設。", "說明掃讀如何依日期線索縮小到特定表格列。", "回讀該列旁的註記，檢查日期是否有例外或限制。", "比較這項證據與最初猜測，若不一致就修正答案。", "用題目要求的資訊作最後檢查，不把快速閱讀誤當成略過驗證。"], "locators": ["第3頁閱讀題組C第38–40題：資訊定位、順序整理及全篇核對", "第4頁閱讀題組（一）第48–50題：先理解公告再依細節作答", "第3頁閱讀題組第39–44題：回到段落證據檢核初步理解"]
    },
]

failures = []
all_steps = []
all_strategies = []
for i, item in enumerate(ITEMS, 1):
    path = BASE / f"question-english-performance-3-iv-14-{i}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    key = "CB DACBDACB".replace(" ", "")[i - 1]
    data["prompt"] = item["prompt"]
    choices = item["options"]
    correct = choices[0]
    wrong = choices[1:]
    answer_index = ord(key) - ord("A")
    arranged = wrong[:answer_index] + [correct] + wrong[answer_index:]
    data["options"] = [{"id": letter, "text": text} for letter, text in zip("ABCD", arranged)]
    data["answer"] = {"value": key, "explanation": f"正解{key}：{item['skill']}。" + item["steps"][-1]}
    data["solutionStrategy"] = item["strategy"]
    data["solutionSteps"] = item["steps"]
    all_steps.extend(item["steps"])
    all_strategies.append(item["strategy"])
    data["reviewStatus"] = "draft"
    refs = []
    for (url, title, year), locator in zip(SOURCES, item["locators"]):
        refs.append({"url": url, "title": title, "year": year, "subject": "english", "locator": locator, "locatorLevel": "item", "observedPattern": f"參照公開原卷的閱讀理解能力模式：{item['skill']}；只取考查方式，不複製題幹、選項、文本、圖像或答案。", "reuseDecision": "pattern-only", "status": "recorded"})
    data["examPatternRefs"] = refs
    data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "內湖國中112-1七年級英文第4頁閱讀題組Q48–50；內湖國中113-2八年級英文第3–4頁閱讀Q34、Q37–40；鹽埕國中114-2九年級英文第3頁閱讀Q39–44、Q45–47。僅抽取可追溯的閱讀任務與推理模式，所有情境、題幹、選項、答案及解析均獨立撰寫。", "authoringNote": "原創快速閱讀題；依三所公立學校公開原卷的具體題號與能力模式獨立撰寫，未複製原文、題幹、選項或答案；維持 draft。"}
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if len(set(item["steps"])) != 5 or len(set(item["options"])) != 4 or data["options"][answer_index]["text"] != correct or len(refs) != 3 or not all(ref["status"] == "recorded" and ref["locatorLevel"] == "item" for ref in refs):
        failures.append(path.name)
if len(set(all_steps)) != 50:
    failures.append("cross-question-solution-step-reuse")
if len(set(all_strategies)) != 10:
    failures.append("cross-question-strategy-reuse")

report = {"unit": "3-Ⅳ-14", "checked": len(ITEMS), "passed": len(ITEMS) if not failures else len(ITEMS) - len(set(failures)), "uniqueStrategies": len(set(all_strategies)), "uniqueSolutionSteps": len(set(all_steps)), "failures": failures, "status": "pass" if not failures else "fail", "notes": "十題均為原創快速閱讀情境，具唯一答案、逐題繁中解析、單元專屬策略、五步推理及三所公立學校公開原卷的精確題號 pattern-only 來源；全部維持 draft。"}
(ROOT / "implementation/reports/english-performance-3-iv-14-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(bool(failures))
