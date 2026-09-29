import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-4-iv-6"
KG = "kg-english-performance-4-iv-6"
SOURCES = [
    {
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/106-2-2%E8%8B%B1%E6%96%87%E4%B8%80%E5%B9%B4%E7%B4%9A%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf",
        "title": "高雄市立大灣國中106學年度第2學期第2次評量一年級英文科試題",
        "year": "106-2",
        "locator": "PDF第3頁第七大題第1至4題：用中文提示完成整句翻譯，包含習慣、頻率、時間和 because from 等語意；本題不沿用原句。",
        "observedPattern": "中文整句轉寫須保留人物、時間、頻率和句間關係，並依英文語序重組；本題使用全新人物與事件。",
    },
    {
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/108-1-2%E8%8B%B1%E6%96%87%E4%B8%80%E5%B9%B4%E7%B4%9A%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf",
        "title": "高雄市立大灣國中108學年度第1學期第2次評量一年級英文科試題",
        "year": "108-1",
        "locator": "PDF第3頁第七大題第1至4題：以中文完成整句翻譯並處理疑問、there be、地點和關係子句；本題採新的語境。",
        "observedPattern": "完整翻譯要同時判斷句型功能、核心動詞與地點／關係訊息，而非逐字直譯；本題不複製試卷題文。",
    },
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91.pdf",
        "title": "高雄市立國昌國中112學年度第1學期三年級第1次段考英文科試題",
        "year": "112-1",
        "locator": "PDF第6頁第四大題第51至53題：整句翻譯，需處理時態、事件順序和完整問句；只取翻譯能力模式。",
        "observedPattern": "長句需先拆解主句、時間／原因關係與問句功能，再用完整英文語序組合；本題改用全新句意。",
    },
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立國昌國中113學年度第2學期第2次段考一年級英文科試題",
        "year": "113-2",
        "locator": "PDF第7頁第八大題第1至2題：整句式中文翻英，包含禮貌請求與日常活動；本題另造情境。",
        "observedPattern": "日常整句翻譯檢查功能語氣、主詞動詞搭配與時間片語是否完整；本題採原創語料。",
    },
]


def refs():
    return [
        {
            **source,
            "subject": "english",
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "item",
        }
        for source in SOURCES
    ]


ITEMS = [
    {
        "prompt": "中翻英：我哥哥每星期三放學後參加音樂社。",
        "options": {"A": "My brother join the music club after school every Wednesday.", "B": "My brother is joining the music club yesterday after school.", "C": "My brother joins the music club after school every Wednesday.", "D": "Every Wednesday the music club join my brother after school."},
        "answer": "C",
        "explanation": "Every Wednesday marks a repeated habit. My brother is third-person singular, so join becomes joins; after school and every Wednesday preserve when he attends.",
        "strategy": "先鎖定主詞與習慣時間，再補第三人稱單數字尾，最後依「參加什麼／何時」排列訊息。",
        "steps": ["找出主詞「我哥哥」，英文是 My brother，屬第三人稱單數。", "「每星期三」表示習慣，選現在簡單式。", "將 join 改為 joins，並保留受詞 the music club。", "把 after school 和 every Wednesday 放在句尾交代時間。", "選 C；A 少了 -s，B 時間不合，D 把社團誤當動作者。"],
    },
    {
        "prompt": "中翻英：現在 Mina 正在圖書館找她的水壺。",
        "options": {"A": "Mina is looking for her water bottle in the library now.", "B": "Mina looks for her water bottle in the library last night.", "C": "Mina are looking her water bottle at library now.", "D": "Now Mina looking for the library her water bottle."},
        "answer": "A",
        "explanation": "現在 and now describe an action in progress, so Mina takes is looking. The phrasal verb look for means search for, and in the library gives the location.",
        "strategy": "用「現在／正在」判斷進行式，接著把 look for 當成完整動詞片語，再安放受詞與地點。",
        "steps": ["圈出「現在／正在」，確認動作此刻仍在進行。", "主詞 Mina 是單數，選 is 加 V-ing：is looking。", "找東西要用 look for，受詞是 her water bottle。", "用 in the library 表示所在位置，now 可置句尾。", "選 A；B 時間衝突，C 主詞與 are 不合且少 for，D 語序錯。"],
    },
    {
        "prompt": "中翻英：上星期五，他們沒有搭公車去美術館。",
        "options": {"A": "They do not take a bus to the art museum last Friday.", "B": "They did not take a bus to the art museum last Friday.", "C": "They did not took a bus to the art museum last Friday.", "D": "Last Friday they were not take bus to the art museum."},
        "answer": "B",
        "explanation": "Last Friday sets the sentence in the past. Past negation uses did not plus the base verb take; to the art museum expresses the destination.",
        "strategy": "過去否定由 did not 承擔時態，主要動詞回到原形；不要在 did 後重複加過去式。",
        "steps": ["找出時間「上星期五」，判定為過去。", "「沒有」需要否定，過去式使用 did not。", "did 已標示過去，take 必須維持原形。", "把 a bus 和 to the art museum 接在動詞後。", "選 B；A 用現在否定，C 重複過去標記，D 動詞結構不成立。"],
    },
    {
        "prompt": "中翻英：可以請你把這張地圖遞給我嗎？",
        "options": {"A": "Are you can pass me this map, please?", "B": "Can you passes this map to me, please?", "C": "Can you to pass me the map, please?", "D": "Can you pass me this map, please?"},
        "answer": "D",
        "explanation": "A polite request can use Can you plus the base verb pass. The indirect-object pattern pass me this map is grammatical and preserves this map and the request tone.",
        "strategy": "把禮貌疑問句拆成 Can＋主詞＋原形動詞；確認「給誰」與「給什麼」都保留。",
        "steps": ["辨認「可以請你……嗎」是禮貌請求，不是詢問能力以外的陳述。", "用 Can you 開頭，you 後接原形 pass。", "按 pass＋人＋物排列：pass me this map。", "用 please 保留客氣語氣，句末加問號。", "選 D；A 重複 be 動詞，B 動詞加 -s，C 原形動詞前多了 to。"],
    },
    {
        "prompt": "中翻英：因為公車晚到了，我們錯過了電影開演。",
        "options": {"A": "Because the bus arrives late, we miss the movie last night.", "B": "We missed the movie started because late the bus.", "C": "Because the bus arrived late, we missed the start of the movie.", "D": "Because arrived late the bus, we missed start movie."},
        "answer": "C",
        "explanation": "Because introduces the cause, the bus arrived late; the result is that we missed the start of the movie. Both events are past, and both clauses keep their own subject and verb.",
        "strategy": "先分辨原因與結果，再讓 because 緊接完整原因子句；同一段過去事件的兩個動詞都用過去式。",
        "steps": ["拆出原因「公車晚到」與結果「我們錯過電影開演」。", "在原因子句放入主詞 the bus 和過去式 arrived。", "在結果子句放入主詞 we 和過去式 missed。", "用 the start of the movie 表達錯過電影開始，兩個子句以 because 連接。", "選 C；其他選項時態不合或破壞子句詞序／完整性。"],
    },
    {
        "prompt": "中翻英：桌上有兩個乾淨的杯子。",
        "options": {"A": "There is two clean cups in the table.", "B": "Two clean cups there are on the table.", "C": "There are two clean cups on the table.", "D": "There are a clean cup on table."},
        "answer": "C",
        "explanation": "The sentence introduces the existence of two cups, so use There are with the plural noun. On the table describes the surface where they are located.",
        "strategy": "存在句先看 be 後名詞的單複數，再選 there is／are；「桌上」表示表面位置，用 on。",
        "steps": ["找出存在句要介紹的事物：兩個杯子，名詞為複數。", "複數名詞搭配 There are。", "在 cups 前放數量 two 與形容詞 clean。", "「桌上」是 on the table，不是 in the table。", "選 C，並核對數量、動詞和介系詞三處。"],
    },
    {
        "prompt": "中翻英：你上週末有打羽球嗎？",
        "options": {"A": "Did you play badminton last weekend?", "B": "Do you played badminton last weekend?", "C": "Were you play badminton last weekend?", "D": "Did you played badminton last weekend?"},
        "answer": "A",
        "explanation": "Last weekend requires a past yes/no question. Use Did before the subject and the base verb play; badminton does not need an article here.",
        "strategy": "過去一般疑問句依 Did＋主詞＋原形動詞組成；時間片語確認為過去，句末用問號。",
        "steps": ["由「上週末」確定問句使用過去時態。", "一般動詞疑問句以 Did 開頭，接主詞 you。", "did 已標記過去，因此 play 用原形。", "加上 badminton 與 last weekend，保留運動名稱及時間。", "選 A；B 混用現在助動詞，C be 動詞搭配錯，D did 後不接 played。"],
    },
    {
        "prompt": "中翻英：這條街比那條街安靜。",
        "options": {"A": "This street is more quiet that street.", "B": "This street is the quietest than that street.", "C": "This street is quieter than that street.", "D": "This street quieter than that street."},
        "answer": "C",
        "explanation": "The sentence compares two streets, so use the comparative quieter followed by than. The subject needs is before the adjective phrase.",
        "strategy": "看到「比」先判斷是兩者比較，採用比較級＋than；句子仍須有主詞與 be 動詞。",
        "steps": ["比較對象是 this street 和 that street，屬兩者比較。", "quiet 的比較級是 quieter。", "在主詞後放 be 動詞 is。", "用 than 引出第二個比較對象 that street。", "選 C；B 誤用最高級，A 比較結構缺 than，D 缺 be 動詞。"],
    },
    {
        "prompt": "中翻英：請把訪客名牌放在門旁邊。",
        "options": {"A": "Please puts the visitor badges beside the door.", "B": "Please put the visitor badge beside the door.", "C": "Please to put a visitor badge beside the door.", "D": "Please are put the visitor badge beside the door."},
        "answer": "B",
        "explanation": "This is a polite instruction, so Please is followed by the base verb put. The singular badge and beside the door express the requested object and its location.",
        "strategy": "禮貌祈使句用 Please＋原形動詞；再核對名詞數量及「在旁邊」的介系詞 beside。",
        "steps": ["辨認「請」表示禮貌指示，用 Please 開頭。", "祈使句省略 you，動詞 put 用原形。", "「名牌」在此是一張，選單數 a visitor badge。", "把位置補成 beside the door，表示門的旁邊。", "選 B；A 動詞錯加 -s，C 多 to，D 混入不必要的 are。"],
    },
    {
        "prompt": "中翻英：如果明天放晴，班上就會到河岸散步。",
        "options": {"A": "If it will be sunny tomorrow, the class walks by the river.", "B": "If sunny tomorrow, the class will walks by the river.", "C": "The class if it is sunny tomorrow will taking a walk by the river.", "D": "If it is sunny tomorrow, the class will take a walk by the river.",},
        "answer": "D",
        "explanation": "A likely future condition uses present tense after if and will plus the base verb in the result clause. Take a walk naturally expresses 散步, and by the river gives the route location.",
        "strategy": "把句子拆成 if 條件和將來結果；if 子句用現在式，主句用 will＋原形動詞。",
        "steps": ["找出條件「如果明天放晴」及結果「班上會散步」。", "if 子句使用 it is sunny tomorrow，不在 if 後放 will。", "結果句以 the class will 開頭，will 後接原形 take。", "用 take a walk 表達散步，by the river 表示河岸路線。", "選 D；其餘選項把 will 放錯子句、動詞加錯形式或漏掉必要主詞。"],
    },
]

for index, item in enumerate(ITEMS, start=1):
    item_id = f"question-english-performance-4-iv-6-{index}"
    source = SOURCES[(index - 1) % len(SOURCES)]
    question = {
        "id": item_id,
        "subject": "english",
        "type": "single-choice",
        "prompt": item["prompt"],
        "options": [{"id": key, "text": value} for key, value in item["options"].items()],
        "knowledgeIds": [KG],
        "difficulty": "medium" if index in {2, 3, 5, 7, 8, 10} else "easy",
        "answer": {"value": item["answer"], "explanation": item["explanation"]},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": source["url"],
            "sourceLocator": source["locator"],
            "authoringNote": "依官方課綱知識節點與四份公立國中英文整句翻譯試題所呈現的句意轉寫能力方向獨立創作；人物、事件與句子均重新設計，未複製原卷內容。完整內容與授權界線仍待審查。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-26",
        "lessonId": LESSON,
        "examPatternRefs": refs(),
        "solutionStrategy": item["strategy"],
        "solutionSteps": item["steps"],
    }
    (OUT / f"{item_id}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n")

print(json.dumps({"rewritten": len(ITEMS), "unit": LESSON, "sourceCountPerQuestion": len(SOURCES), "draftPreserved": True}, ensure_ascii=False))
