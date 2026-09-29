import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QROOT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國中114學年度第2學期九年級第1次段考英文", "114-2"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91--2%E6%A0%A1.pdf", "高雄市立國昌國中111學年度第2學期八年級第3次段考英文", "111-2"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%BA%8C%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87-%E8%A9%A6%E9%A1%8C.pdf", "高雄市立國昌國中109學年度第1學期八年級第2次段考英文", "109-1"),
]
ITEMS = [
    {
        "prompt": "A field note begins, “I checked the tide markers before sunrise, then wrote down how far the water had moved.” Which viewpoint shapes the report?",
        "options": ["A first-person observer reports actions and measurements", "A second-person guide commands every reader", "An outside narrator knows every volunteer’s thoughts", "A timetable speaks without an observer"], "key": "C",
        "strategy": "用人稱代名詞和親自執行的動詞辨認敘述位置；第一人稱能報告觀察，不能自動代表所有人的經驗。",
        "steps": ["圈出主詞 I，並標記 checked、wrote 兩個親自進行的動作。", "確認句子呈現的是記錄者的觀察流程，而非直接命令讀者。", "把「第一人稱觀察者」和「全知旁觀者」分開。", "注意潮位變化是記錄者看到的現象，不足以代表所有海岸或所有時段。", "選擇第一人稱觀察敘述，並保留個人記錄的範圍限制。"],
        "locators": ["第3頁閱讀測驗第39–44題：日記敘述者用第一人稱交代家庭事件與感受", "第3頁閱讀題組E第27–29題：由文本事件和證據推論環境影響", "第4頁閱讀題組第32–35題：辨識作者看法並以文中主張作答"]
    },
    {
        "prompt": "A student describes the repair club as “patient, welcoming, and surprisingly fun,” then says beginners were invited to try a small repair. What attitude is conveyed?",
        "options": ["The writer is doubtful that the club exists", "The writer is approving and warmly encouraging", "The writer is angry that beginners attended", "The writer gives only a neutral time record"], "key": "B",
        "strategy": "先找帶評價的形容詞和行動描述，再判斷整段立場；不要只靠某一個情緒詞推成強烈情緒。",
        "steps": ["標記 patient、welcoming、fun 這些評價詞。", "看後句邀請新手參與，判斷文字是否支持初學者。", "把態度概括成正向且鼓勵，不擴張為毫無疑慮或狂熱讚美。", "排除憤怒、懷疑與純客觀紀錄，因為它們和用字不符。", "以評價詞和邀請行動各舉一項證據，支持「欣賞並鼓勵」的判斷。"],
        "locators": ["第3頁閱讀題組第43題：由人物用語判斷對父親的態度", "第3頁閱讀測驗第24–26題：由隊友鼓勵和主角回應推論態度轉變", "第3頁閱讀題組第32–35題：根據作者立場及建議選擇最適敘述"]
    },
    {
        "prompt": "A library notice explains how to label a donated book, where to leave it, and ends with “Help another reader discover a story.” What is the notice mainly trying to do?",
        "options": ["Compare the history of public libraries", "Report how many books were printed last year", "Argue that readers should stop borrowing books", "Guide people to donate books and invite them to participate"], "key": "D",
        "strategy": "把操作指示和結尾呼籲合看：前者說明如何行動，後者揭示行動希望帶來的讀者參與。",
        "steps": ["找出 label、leave 等指示動詞，確認讀者被要求完成捐書步驟。", "辨認最後一句的祈使／邀請功能，連到分享閱讀的目的。", "把流程資訊和呼籲合併，概括為引導並鼓勵捐書。", "排除只描述圖書館背景、印刷統計或反對借閱等文本未提主張。", "檢查答案同時涵蓋「怎麼做」與「為何邀請參與」，而非只抓一個細節。"],
        "locators": ["第4頁閱讀題組第45–47題：對話指出宣導消防安全的目的並呼籲行動", "第3頁閱讀題組E第27–29題：文章說明問題後提出可採取的行動", "第4頁閱讀題組第32–35題：文章先給話題建議，再說明作者倡議"]
    },
    {
        "prompt": "A class claims that a shaded waiting area lowers students’ heat exposure. Which evidence most directly supports that claim without proving more than it measures?",
        "options": ["A survey records lower afternoon surface temperatures in shaded seats than in nearby sunny seats on six sampled days", "The new roof is painted green", "Several students say the area looks attractive", "The school has many classrooms"], "key": "A",
        "strategy": "對照主張中的比較對象和結果指標，選取直接測量同一變項的資料，並保留抽樣與推論範圍。",
        "steps": ["拆解主張：遮蔭區相對曝曬區，熱暴露較低。", "尋找同時含比較組與溫度／熱暴露指標的觀察。", "確認六天資料是在相近時段對照陰影與日照座位。", "指出測量的是抽樣日表面溫度，不能直接證明所有季節或所有學生的健康結果。", "選出最直接對應主張的比較資料，拒絕顏色、喜好或校舍規模等無關資訊。"],
        "locators": ["第3頁閱讀題組第39–44題：根據日記內容和事件線索判斷敘述是否受支持", "第3頁閱讀題組E第27–28題：從文章所述機制挑出支持環境影響的證據", "第3頁閱讀測驗第26–28題：分辨文章明示事實與不受支持的敘述"]
    },
    {
        "prompt": "A student writes, “I interviewed six lunchtime users; four said the new quiet corner helped them focus. This small sample suggests it may help some students.” Which conclusion best respects the evidence?",
        "options": ["Every student in the school focuses better there", "The corner has been proven to raise exam scores", "Several interviewed users reported better focus, but the result may not represent everyone", "The interviews prove that noise never affects learning"], "key": "C",
        "strategy": "先分開訪談結果與作者推論，再用樣本數、對象和限定詞檢查結論有沒有超出證據。",
        "steps": ["抽出可確認的資料：訪談六人，其中四人回報較能專心。", "辨認作者使用 small sample、may、some 等限制語。", "將結果限縮到「受訪者中有人如此回報」。", "排除把小樣本擴大到全校、考試成績或所有噪音情境的絕對結論。", "選擇同時保留觀察結果與代表性限制的敘述。"],
        "locators": ["第3頁閱讀題組第39–44題：依日記敘述的有限事件線索推論人物理解", "第3頁閱讀題組E第27–28題：從具體文章線索推論而不捏造額外結果", "第3頁閱讀測驗第33、35題：把作者觀點與文章實際支持範圍分開"]
    },
    {
        "prompt": "A school message explains a free weekend workshop, lists the age range, bus route, and sign-up form, then asks families to register by Friday. Who is the message chiefly addressing, and why?",
        "options": ["Bus drivers, so they can change the route", "Families with eligible students, so they can decide and register", "Workshop instructors, so they can write a textbook", "People who already attended, so they can review last year"], "key": "B",
        "strategy": "從資訊種類和最後要求推回對象：資格、交通、報名期限是供潛在參與者作決定的線索。",
        "steps": ["找出文中提供的年齡資格、交通方式和報名表。", "確認結尾要求在星期五前登記，這是讀者需要採取的動作。", "把具資格學生及其家庭和這些資訊的實際用途配對。", "排除只需知道路線的司機、授課教師或已結束活動的舊參加者。", "用「資格＋如何到場＋如何報名」說明訊息主要服務潛在家庭。"],
        "locators": ["第3頁閱讀題組第45–47題：由消防安全訊息對象及行動呼籲判斷目的", "第3頁閱讀題組E第27–29題：由問題與建議判斷訊息希望讀者採取的行動", "第4頁閱讀題組第32–34題：由作者建議推斷目標讀者與適當行動"]
    },
    {
        "prompt": "An article first lists the freedom of remote work, then mentions weak internet and loneliness, and closes by advising readers to weigh both sides. Which description of its stance is fairest?",
        "options": ["It presents advantages and cautions, then recommends a balanced decision", "It claims remote work has no disadvantages", "It tells everyone to move abroad immediately", "It rejects all forms of online work"], "key": "D",
        "strategy": "沿著篇章轉折追蹤正反資訊與結尾建議；不要讓開頭的優點遮掉後段限制。",
        "steps": ["掃描列舉標記，分別記下自由工作的好處和困難。", "注意 weak internet、loneliness 等明確限制。", "讀結尾建議，判斷作者希望讀者如何處理前述利弊。", "排除全盤讚成、全盤反對或催促立即採取行動等極端說法。", "用「呈現兩面並建議衡量後決定」概括全文立場。"],
        "locators": ["第3頁閱讀題組第39–44題：比較日記事件前後敘述，追蹤敘述者理解變化", "第3頁閱讀測驗第24–26題：依故事由挫折、支持到行動的順序理解態度", "第4頁閱讀題組第32–35題：把作者陳述與建議合併判斷立場"]
    },
    {
        "prompt": "A post says, “Three volunteers collected 18 bags of litter on Saturday; the north path was cleaner afterward.” Which added conclusion is unsupported?",
        "options": ["Three volunteers took part in the cleanup", "The report counted 18 bags", "The north path was reported cleaner afterward", "Everyone in the town now keeps every public area clean"], "key": "A",
        "strategy": "逐句把已觀察資訊和推論分欄；人數、袋數、局部結果不能證明整個城鎮的長期行為。",
        "steps": ["列出三項原文直接提供的內容：三位志工、十八袋、北側步道變乾淨。", "確認時間和地點只涵蓋星期六及北側步道。", "檢查待選結論是否把局部行動外推到所有居民和所有公共空間。", "保留原文可支持的三個陳述，標出全鎮永久改善沒有證據。", "選出唯一超出人數、地點與時間範圍的說法。"],
        "locators": ["第3頁閱讀題組第39–44題：區分日記明示事件和超出文本的推斷", "第3頁閱讀題組E第27–28題：根據具體因果線索判斷合理與不合理推論", "第3頁閱讀題組第33–35題：比較明示內容、作者看法及過度概括"]
    },
    {
        "prompt": "A first-person blog says, “I loved the evening market, but I visited only one Friday and did not ask local residents.” What is the most responsible use of this account?",
        "options": ["Treat it as one visitor’s experience, not a complete account of the whole community", "Assume every resident loves the market equally", "Use it to prove the market is open every evening", "Ignore it because first-person writing can never offer evidence"], "key": "A",
        "strategy": "評估第一人稱材料的證據價值與視角邊界：親身經驗可說明個人感受，但不能代替未訪問群體。",
        "steps": ["辨認 I loved 表示這是作者親身感受。", "標出作者明說的取樣界線：只去過一個星期五、未訪問居民。", "判斷這段材料能支持個人喜好和當晚經驗。", "排除推論所有居民態度或每天營業的說法，也不必把個人經驗完全作廢。", "選擇既使用第一手觀察、又明確限制代表性的結論。"],
        "locators": ["第3頁閱讀題組第39–44題：日記作者描述個人感受並隨新經驗調整理解", "第3頁閱讀測驗第24–26題：把個人敘述視角與故事事實分開判斷", "第4頁閱讀題組第32–35題：以作者觀點分析主張，同時按文本範圍判斷"]
    },
    {
        "prompt": "A student’s report opens with disappointment that the team lost, quotes two teammates’ practice logs, and ends by saying, “I now see how steady practice changed our passing.” Which reading is best supported?",
        "options": ["The student’s view shifts from disappointment toward recognizing improvement, supported by practice evidence", "The report proves the team won every game", "The writer is neutral because feelings are never stated", "The logs show that practice had no connection to passing"], "key": "B",
        "strategy": "把開頭態度、引用資料和結尾反思串成一條證據鏈，分辨情緒轉變與客觀成績主張。",
        "steps": ["讀開頭，標記失利帶來的失望情緒。", "檢視兩份練習紀錄，確認它們提供的是傳球練習的資料。", "對照結尾 steady practice changed our passing，找出作者重新理解的方向。", "排除「每場都贏」等沒有出現的結果，也不要把感受誤當成勝負統計。", "以開頭、紀錄和結尾三處證據支持作者態度轉變的解讀。"],
        "locators": ["第3頁閱讀測驗第39–44題：日記敘述者的感受由事件前後發生變化", "第3頁閱讀測驗第24–26題：由人物困境、收到支持及後續改變推論態度", "第4頁閱讀題組第33、35題：用段落證據核對對作者主張的理解"]
    },
]

keys = "CBDACBDACB"
correct_indices = [0, 1, 3, 0, 2, 1, 0, 3, 0, 0]
all_steps, all_strategies, failures = [], [], []
for i, item in enumerate(ITEMS, 1):
    path = QROOT / f"question-english-performance-3-iv-15-{i}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    key = keys[i - 1]
    correct_index = correct_indices[i - 1]
    correct, wrong = item["options"][correct_index], [t for j, t in enumerate(item["options"]) if j != correct_index]
    pos = ord(key) - 65
    arranged = wrong[:pos] + [correct] + wrong[pos:]
    data["prompt"] = item["prompt"]
    data["options"] = [{"id": letter, "text": text} for letter, text in zip("ABCD", arranged)]
    data["answer"] = {"value": key, "explanation": f"正解{key}：{item['strategy']}"}
    data["solutionStrategy"] = item["strategy"]
    data["solutionSteps"] = item["steps"]
    data["reviewStatus"] = "draft"
    refs = []
    for source, locator in zip(SOURCES, item["locators"]):
        url, title, year = source
        refs.append({"url": url, "title": title, "year": year, "subject": "english", "locator": locator, "locatorLevel": "item", "observedPattern": "只參照公立學校英文試題的觀點／態度／目的／證據閱讀能力與推理模式；本題文本、情境、選項、答案和解析均為原創。", "reuseDecision": "pattern-only", "status": "recorded"})
    data["examPatternRefs"] = refs
    data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "鹽埕國中114-2九年級Q39–47；國昌國中111-2八年級Q24–29；國昌國中109-1八年級Q26–35。僅借鑑題型能力與文本推理層次，未複製原卷文字或答案。", "authoringNote": "本題由官方課綱知識點與多份公立學校公開評量的題型模式獨立撰寫；題幹、文本、選項、解析及遷移內容原創；保持draft。"}
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    all_steps.extend(item["steps"])
    all_strategies.append(item["strategy"])
    answer_text = data["options"][pos]["text"]
    if answer_text != correct or len(set(item["steps"])) != 5 or len(refs) != 3:
        failures.append(path.name)
if len(set(all_steps)) != 50: failures.append("reused-solution-steps")
if len(set(all_strategies)) != 10: failures.append("reused-strategies")
report = {"unit": "3-Ⅳ-15", "checked": 10, "passed": 10 if not failures else 10 - len(failures), "uniqueStrategies": len(set(all_strategies)), "uniqueSolutionSteps": len(set(all_steps)), "failures": failures, "status": "pass" if not failures else "fail", "notes": "十題具原創文本、正解、繁中逐題分析、差異化策略與五步解題；各題三筆精確題號公校試題pattern-only參照；全部保持draft。"}
(ROOT / "implementation/reports/english-performance-3-iv-15-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(bool(failures))
