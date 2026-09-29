import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-4-iv-7"
KG = "kg-english-performance-4-iv-7"
SOURCES = [
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf",
        "title": "高雄市立國昌國中112學年度第1學期第1次段考一年級英文科試題",
        "year": "112-1",
        "locator": "PDF第3頁題組C第28至29題：閱讀未來寫給自己的生日信，判讀收件人、時間與信件細節；本題完全另寫語料。",
        "observedPattern": "短書信題以稱呼、寄件者與時間線索判斷讀者及內容細節；本題僅取書信理解能力方向。",
    },
    {
        "url": "https://www.csjh.kh.edu.tw/teach/exam/108%E4%B8%8B%E5%AD%B8%E6%9C%9F/%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83/%E8%8B%B1%E6%96%87%E7%A7%91/%E4%B8%80%E5%B9%B4%E7%B4%9A/108%E4%B8%8B%E4%BA%8C%E6%AE%B5%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf",
        "title": "高雄市立中山國中108學年度第2學期第2次段考一年級英文科試題",
        "year": "108-2",
        "locator": "PDF第2頁題組A第19至21題：閱讀女兒寫給父親的信，判讀寫信原因、內容與主旨；本題另創人物與情境。",
        "observedPattern": "書信閱讀題須整合稱呼、家庭關係、正文事件與結尾，區分明示細節與整體目的；本題不沿用原文。",
    },
    {
        "url": "https://www.csjh.kh.edu.tw/teach/exam/113%E4%B8%8A%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83/%E8%8B%B1%E8%AA%9E%E7%A7%91/%E4%B8%89%E5%B9%B4%E7%B4%9A/113%E4%B8%8A%E4%B8%89%E6%AE%B5%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf",
        "title": "高雄市立中山國中113學年度第1學期第3次段考三年級英文科試題",
        "year": "113-1",
        "locator": "PDF第3頁閱讀題組第31至34題：閱讀寄給 May 的旅行邀請 email，辨認收件人、出發計畫、請求與回信期待；本題原創。",
        "observedPattern": "電子郵件題組結合收件人、旅行資訊、詢問與回覆期待，要求沿上下文選出合宜訊息；本題只取閱讀推理形式。",
    },
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C-3%E5%B9%B4%E7%B4%9A%E6%9C%9F%E6%9C%AB-%E8%8B%B1%E6%96%87%E7%A7%91-%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立國昌國中公開英文段考試題（PDF，正式學年度與年級標題以原卷首頁為準）",
        "year": "public-school-exam",
        "locator": "PDF第6頁閱讀題組第32至35題：正式客訴信與商家回覆，判斷寫信目的、回應立場及細節；本題僅改寫公務書信理解能力。",
        "observedPattern": "成對書信閱讀須比對寄件者目的、收件者回應與事件處理結果；本題採全新公共服務情境。",
    },
]


def refs():
    return [
        {
            **source,
            "subject": "english",
            "locator": source["locator"],
            "observedPattern": source["observedPattern"],
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "item",
        }
        for source in SOURCES
    ]


def make(index, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {
        "id": f"question-english-performance-4-iv-7-{index}",
        "subject": "english",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": key, "text": value} for key, value in options.items()],
        "knowledgeIds": [KG],
        "difficulty": difficulty,
        "answer": {"value": answer, "explanation": explanation},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCES[0]["url"],
            "sourceLocator": "三份公立學校公開英文評量僅供卡片、訊息、書信與電郵的能力方向研究；未複製原題、選項、文章或答案。",
            "authoringNote": "依官方課綱 KG 與四份公立學校英文試題精確題組定位所呈現的短訊息理解能力獨立改寫；題幹、選項、答案與解析均為原創，保持 draft，未執行 Terra 審查。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-09",
        "lessonId": LESSON,
        "examPatternRefs": refs(),
        "solutionStrategy": strategy,
        "solutionSteps": steps,
    }


QUESTIONS = [
    make(
        1,
        "Read the note: 'Hi Leo, I left your science notebook on the kitchen table. Please bring it to school tomorrow. —Mia' What should Leo do?",
        {"A": "Bring the notebook to school tomorrow.", "B": "Buy a new kitchen table.", "C": "Leave school before lunch.", "D": "Write a science report tonight."},
        "A",
        "Mia says where the notebook is and directly asks Leo to bring it to school tomorrow, so A states the required action.",
        "先找訊息的收件人與明確要求，再把動作和時間與選項逐一比對。",
        [
            "確認訊息是寫給 Leo，題目問的是他要採取的行動。",
            "圈出動作 bring 以及物品 science notebook。",
            "保留時間 tomorrow 與地點 school，避免只抓到 notebook。",
            "將完整要求與四個選項比對，A 同時包含動作、物品與時間。",
            "回讀原文，確認其他選項沒有獲得文字證據支持。",
        ],
        "easy",
    ),
    make(
        2,
        "Read the email subject and opening: 'Subject: Thank you for the concert tickets / Dear Aunt May, The music was wonderful last night.' Why did the writer send the email?",
        {"A": "To thank the aunt for the tickets.", "B": "To invite the aunt to a new concert.", "C": "To complain about the music.", "D": "To ask the aunt to sell tickets."},
        "A",
        "Thank you and the positive comment about last night's music show appreciation for the tickets, so A best describes the purpose.",
        "先讀主旨與開頭判斷寫信目的，再用語氣和事件確認不是邀請或抱怨。",
        [
            "定位收件人 Aunt May，判斷這是寫給阿姨的個人電郵。",
            "讀主旨中的 Thank you，先提出感謝的目的假設。",
            "用 wonderful 和 last night 檢查語氣與已發生的音樂會事件。",
            "排除 invite、complain、sell 等原文沒有支持的目的。",
            "選 A，並以主旨與正面評語作為兩項證據。",
        ],
        "easy",
    ),
    make(
        3,
        "A card says: 'Happy birthday, Nina! Your gift is waiting at the front desk. See you after practice.' Where should Nina look for the gift?",
        {"A": "At the front desk.", "B": "In the practice room.", "C": "At the birthday party tomorrow.", "D": "Inside the writer's school bag."},
        "A",
        "The card explicitly says that the gift is waiting at the front desk; the other locations are not stated.",
        "卡片細節題要鎖定明確地點，不用生日或練習等背景字詞自行推測。",
        [
            "先辨認題目問的是禮物地點，而非生日祝福的目的。",
            "找出關鍵句 Your gift is waiting at the front desk。",
            "把 at the front desk 與選項的地點逐字對照。",
            "注意 practice 只說見面時間脈絡，沒有說禮物在練習室。",
            "選 A，回到原句確認地點片語完全一致。",
        ],
        "easy",
    ),
    make(
        4,
        "Read the letter: 'Dear Ben, I will arrive on the 6:20 train, not the 5:50 one. Please wait by Exit 2. —Dad' What changed?",
        {"A": "The arrival train is later.", "B": "The meeting place moved to Exit 5.", "C": "The writer will arrive by bus.", "D": "The meeting was cancelled."},
        "A",
        "The letter contrasts the 6:20 train with the earlier 5:50 train, so only the arrival time has changed.",
        "比較訊息中的新舊數字與否定詞，分清楚改變的條件和仍然不變的地點。",
        [
            "找出原先的 5:50 與新的 6:20，這是一組時間比較。",
            "確認 6:20 晚於 5:50，因此 train arrival 變晚。",
            "另讀 Please wait by Exit 2，確認地點沒有改成 Exit 5。",
            "檢查 arrive 與 train，排除 bus 和 cancelled 等不符資訊。",
            "選 A，說明改變的是抵達班次時間，不是會面地點。",
        ],
        "medium",
    ),
    make(
        5,
        "Read this message: 'Could you send me the address of the art museum? I want to plan our route before Saturday.' What does the writer want the reader to do?",
        {"A": "Send the museum's address.", "B": "Meet at the museum on Friday.", "C": "Draw a picture for Saturday.", "D": "Cancel the route plan."},
        "A",
        "Could you send me the address is a polite request for the museum's address; planning the route explains why it is needed.",
        "先辨認問句中的禮貌請求，再把 want to do 與補充原因分開判讀。",
        [
            "找出 Could you，判斷後面是請求而非敘述事實。",
            "找出主要動詞 send 與受詞 the address。",
            "確認 art museum 限定地址的對象，不能只回答 send something。",
            "把 before Saturday 視為使用地址的時間背景，不改變請求內容。",
            "選 A，回讀確認其他選項都不是訊息直接要求的動作。",
        ],
        "medium",
    ),
    make(
        6,
        "A student writes: 'Dear Ms. Chen, I was absent on Monday because I was sick. Could you tell me which worksheet I should complete? Sincerely, Eva.' Why did Eva write the letter?",
        {"A": "To ask about missed schoolwork.", "B": "To report a new illness at school.", "C": "To invite Ms. Chen to dinner.", "D": "To explain how to make a worksheet."},
        "A",
        "Eva explains her absence and asks which worksheet to complete, so the letter's purpose is to ask about missed schoolwork.",
        "整合原因與請求兩句，找出最後的實際任務，而不是把 because 子句當成主旨。",
        [
            "確認收件人是 Ms. Chen，這是學生寫給老師的正式信件。",
            "把 was absent 與 sick 標成背景原因，而非主要請求。",
            "找出 Could you tell me which worksheet I should complete 的問句。",
            "將 worksheet 與 absent on Monday 連結，推得是補做缺席作業。",
            "選 A，並用請求句作為目的的直接證據。",
        ],
        "medium",
    ),
    make(
        7,
        "Read the announcement message: 'The library closes at 4:30 today for cleaning. Please return your books before then.' What should students do?",
        {"A": "Return books before 4:30.", "B": "Clean the library at 5:00.", "C": "Borrow books after closing.", "D": "Keep the library open today."},
        "A",
        "The announcement gives a closing time and asks students to return books before that time, making A the supported action.",
        "把公告的時間限制與祈使句連在一起，判斷讀者現在該做的事。",
        [
            "先圈出 closes at 4:30，建立不可晚於此時間的限制。",
            "再找 Please return your books，這是對學生的直接指示。",
            "將 before then 代回 4:30，而不是另設 5:00。",
            "檢查選項是否同時符合 return books 與時間限制。",
            "選 A，並指出 cleaning 是關閉原因，不是學生要完成的任務。",
        ],
        "easy",
    ),
    make(
        8,
        "A postcard says: 'Greetings from Green Island! We saw sea turtles this morning. Wish you were here.' Which statement is true?",
        {"A": "The writer saw sea turtles this morning.", "B": "The reader is already on Green Island.", "C": "The writer will see turtles next year.", "D": "The postcard is about a school exam."},
        "A",
        "The postcard directly reports seeing sea turtles this morning; wish you were here shows the reader is elsewhere.",
        "用時間副詞和已完成事件判讀明示細節，再避免把 wish 句誤讀成讀者已在同地。",
        [
            "找出地點 Green Island，確認明信片的旅行情境。",
            "圈出 saw sea turtles，辨認這是已發生的觀察。",
            "保留 this morning，確認事件時間而非 next year。",
            "讀 wish you were here，推知收件人目前不在該地。",
            "選 A，因為它完整重述了原文的主詞、事件與時間。",
        ],
        "medium",
    ),
    make(
        9,
        "Read the email: 'To: Club members / The meeting has moved from Room 201 to Room 305. It will still begin at 3:00 p.m.' Which detail stayed the same?",
        {"A": "The starting time.", "B": "The room number.", "C": "The club members' names.", "D": "The date of the next holiday."},
        "A",
        "The email says the room changed but explicitly keeps the 3:00 p.m. starting time, so A stayed the same.",
        "抓住 from...to... 判斷改變項，再找 still 所標示的未變條件。",
        [
            "先把 Room 201 和 Room 305 標成同一項目的舊值與新值。",
            "找到 still begin at 3:00 p.m.，注意 still 表示維持不變。",
            "比較四個選項，只有 starting time 對應 3:00 p.m.。",
            "排除 room number，因為它正是由 201 改成 305 的項目。",
            "選 A，回讀確認題目問 stayed the same 而不是 changed。",
        ],
        "medium",
    ),
    make(
        10,
        "Choose the best closing for a polite email to a community center: 'Dear Staff, I would like to ask whether the swimming pool is open on Sunday. ...'",
        {"A": "Thank you for your help. Best regards, Kai", "B": "Open the pool now. Bye, Kai", "C": "You must answer me today!!! Kai", "D": "See you in class. Your student, Kai"},
        "A",
        "The email is a polite inquiry to staff, so a courteous thanks and Best regards is the appropriate closing.",
        "依收件人、目的與語氣選結尾；正式詢問需要禮貌收束，不是命令或不相干稱謂。",
        [
            "辨認收件人是 community center staff，屬於正式聯絡對象。",
            "確認主旨是詢問營業時間，不是命令對方開門。",
            "檢查選項的語氣，Thank you 與 Best regards 都符合禮貌書信。",
            "排除命令、過度標點和 class／student 等不合情境的結尾。",
            "選 A，確認稱謂、目的與收束語氣前後一致。",
        ],
        "hard",
    ),
]

ANSWER_ORDER = ["C", "A", "D", "B", "C", "B", "A", "D", "B", "C"]
for question, correct_key in zip(QUESTIONS, ANSWER_ORDER, strict=True):
    original_options = [option["text"] for option in question["options"]]
    # Each order is intentionally distinct; move the authored correct option A
    # to the selected key while preserving each distractor's wording and rationale.
    orders = {
        "A": [0, 1, 2, 3],
        "B": [3, 0, 1, 2],
        "C": [1, 3, 0, 2],
        "D": [1, 2, 3, 0],
    }
    question["options"] = [
        {"id": key, "text": original_options[index]}
        for key, index in zip(("A", "B", "C", "D"), orders[correct_key], strict=True)
    ]
    question["answer"]["value"] = correct_key
    question["answer"]["explanation"] = question["answer"]["explanation"].replace("A ", f"{correct_key} ").replace("A states", f"{correct_key} states").replace("making A ", f"making {correct_key} ").replace("so A ", f"so {correct_key} ").replace("so A", f"so {correct_key}")
    question["solutionSteps"][-1] = question["solutionSteps"][-1].replace("選 A", f"選 {correct_key}")
    (OUT / f"{question['id']}.json").write_text(
        json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
print(f"rewrote {len(QUESTIONS)} questions")
