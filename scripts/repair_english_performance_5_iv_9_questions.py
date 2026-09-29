import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = {
    "cap111": {
        "url": "https://school.tc.edu.tw/open-message/064526/get-file/628aea9f04ad8678f4674dca",
        "title": "111年國中教育會考英語科試題說明（臺中市教育局校務系統公開PDF）",
        "year": "111",
        "locator": "PDF第10頁聽力示例第12題；百貨廣播主旨、地點與結束時間",
        "pattern": "辨識單人公共廣播的目的及其中時間／地點線索；只取測量方式，不沿用特賣主題、句子或選項。",
    },
    "cap113": {
        "url": "https://cgjh.hcc.edu.tw/p/405-1032-440270,c5348.php",
        "title": "新竹縣立成功國中公告之113年國中教育會考英語科聽力試題本",
        "year": "113",
        "locator": "校方公告附件英語聽力試題本PDF第5頁第19題；捷運廣播中的乘客行動指示",
        "pattern": "從公共交通廣播抓出面向聽眾的具體安全行動；不沿用捷運情節、英文原句或選項。",
    },
    "cap114": {
        "url": "https://sljh.hcc.edu.tw/p/406-1034-491334,r1565.php?Lang=zh-tw",
        "title": "新竹縣立勝利國中公告之114年國中教育會考英語科聽力試題本",
        "year": "114",
        "locator": "校方公告附件英語聽力試題本PDF第5頁第21題；戶外比賽遇雨後的安排與條件",
        "pattern": "整合公共活動公告中的天候條件與後續安排；不沿用競賽情境、答案文字或選項。",
    },
    "yichang": {
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=358&cfsn=2105&name=109-1-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%838%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E5%BE%90%E7%BE%8E%E9%9B%B2.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中109學年度第1學期第2次段考八年級英語科試題與聽力錄音稿",
        "year": "109-1",
        "locator": "PDF第2頁Part III言談理解第9-12題及PDF第10頁錄音稿第9-12題；聽取簡短言談細節並判斷場景／結果",
        "pattern": "依短篇口語訊息中的明示細節推斷地點、行動與結果；僅取聽力理解能力模式，不挪用原對話或情節。",
    },
}

DATA = [
    {
        "focus": "broadcast purpose",
        "prompt": "The school speaker says, ‘Our student art show opens in the main hall at noon. Families are welcome to visit.’ What is the announcement mainly doing?",
        "options": ["Teaching a drawing technique", "Announcing the show and inviting families", "Reporting a train problem", "Explaining where lunch is served"],
        "answer": "B",
        "correct": "Announcing the show and inviting families",
        "explanation": "It gives the event, venue, and opening time, then directly welcomes families; the message informs listeners and invites them to attend.",
        "strategy": "先用開頭判斷公告談什麼，再看結尾是否要求、邀請或提醒聽眾採取行動；主旨要涵蓋整段而非只抓一個時間。",
        "steps": ["題目問的是整段公告的主要功能，不是單獨問場地或時間。", "抓住主題 art show，以及 main hall、noon 兩項活動資訊。", "注意 Families are welcome to visit 是對聽眾發出的邀請。", "選B，因它同時概括活動通知與邀請；其他選項把公告主題換成無關事項。", "最後核對答案涵蓋前面的事件資訊和結尾的聽眾行動。"],
        "refs": ["cap111", "cap113", "cap114"],
    },
    {
        "focus": "time and place",
        "prompt": "An announcer says, ‘The safety talk starts at 9:15 in the auditorium. Please enter through the west doors.’ Where and when should students go?",
        "options": ["Library, 9:50", "Auditorium, after school", "Auditorium, 9:15", "West gate, at noon"],
        "answer": "C",
        "correct": "Auditorium, 9:15",
        "explanation": "The announcement states the venue and start time directly. The west doors are an entrance, not the location of the talk.",
        "strategy": "聽到活動資訊時，把「活動地點、開始時間、進場入口」分欄記；不要把相鄰但用途不同的入口當成活動場地。",
        "steps": ["先分辨題目要回答的是 where 和 when，而不是從哪個門進入。", "記下地點 auditorium、時間 9:15、入口 west doors 三項。", "將前兩項配成活動地點與開始時間，入口另作行動備註。", "選C；A、B、D至少有地點或時間與播音不符。", "回讀三欄筆記，確認沒有把 west doors 誤填成會場。"],
        "refs": ["cap111", "cap113", "yichang"],
    },
    {
        "focus": "warning and required action",
        "prompt": "At the station, the announcement says, ‘Keep behind the marked line. Let passengers leave the train before you get on, and hold your bags close.’ What should waiting passengers do?",
        "options": ["Board before anyone gets off", "Put bags in the doorway", "Stand on the marked line", "Wait behind the line and let riders exit first"],
        "answer": "D",
        "correct": "Wait behind the line and let riders exit first",
        "explanation": "The message gives two safety instructions: stay behind the line and allow exiting riders to pass before boarding.",
        "strategy": "公告警示常有多個動作；將 each instruction 拆開記錄，再選能同時符合安全界線與先後順序的選項。",
        "steps": ["確認題目問等待中的乘客應怎麼做，需找指令而非公告目的。", "拆出三條規則：站在線後、先讓乘客下車、行李靠近自己。", "比較選項是否顛倒上下車順序或違反安全界線。", "選D，因為它同時遵守站位和讓乘客先下車兩個關鍵要求。", "再把答案和第三條行李提醒核對，確認沒有選到相反動作。"],
        "refs": ["cap113", "cap114", "yichang"],
    },
    {
        "focus": "schedule order",
        "prompt": "A museum notice lists: doors open at 9:00, the guided tour begins at 9:30, and the craft table opens at 10:15. Which activity happens second?",
        "options": ["The guided tour", "The craft table", "The museum closes", "A lunch break"],
        "answer": "A",
        "correct": "The guided tour",
        "explanation": "The sequence is doors open at 9:00, guided tour at 9:30, then craft activity at 10:15; the tour is second.",
        "strategy": "把公告中每個時間和事件配成一列，再依時間排序；題目問第幾項時，不要把場地開門誤當成活動。",
        "steps": ["分辨 doors open 是入場時間，不是導覽或手作活動。", "建立時間序：9:00開門、9:30導覽、10:15手作桌開放。", "按先後數出事件，導覽排在開門之後、手作之前。", "選A；B是第三個安排，C和D都沒有在公告出現。", "用時間由早到晚重新檢查次序，確認沒有將兩項活動對調。"],
        "refs": ["cap111", "cap114", "yichang"],
    },
    {
        "focus": "weather change",
        "prompt": "The morning report says, ‘Skies will stay clear until 3 p.m.; showers are expected after that.’ What should listeners be ready for later in the day?",
        "options": ["Snow before breakfast", "Rain after 3 p.m.", "Sunshine all night", "A storm exactly at noon"],
        "answer": "B",
        "correct": "Rain after 3 p.m.",
        "explanation": "The forecast marks a change point: clear weather lasts until 3 p.m., and showers are expected afterward.",
        "strategy": "天氣播報要記「現在狀況＋轉變時間＋之後狀況」；別只聽到 clear 就忽略後面的時間轉折。",
        "steps": ["把 until 和 after 視為關鍵時間界線。", "整理成前後兩段：三點前晴朗，三點後有陣雨。", "題目問 later，故答案應取後半段而非目前天氣。", "選B；A、C、D把天氣種類或發生時間改掉了。", "再次核對 showers 的時間在 3 p.m. 之後，而非正好中午。"],
        "refs": ["cap114", "cap111", "cap113"],
    },
    {
        "focus": "traffic alternative",
        "prompt": "A traffic update says, ‘Oak Street is closed for repairs today. Drivers heading downtown should use Pine Road instead.’ Which route should those drivers take?",
        "options": ["Oak Street through the repair zone", "Wait on Oak Street until midnight", "Pine Road", "Turn Oak Street into a parking lot"],
        "answer": "C",
        "correct": "Pine Road",
        "explanation": "Instead signals the replacement route. Since Oak Street is closed, downtown drivers should use Pine Road.",
        "strategy": "交通消息先辨認封閉路段，再抓 instead、detour 等替代路線訊號；不要因熟悉路名而忽略路況更新。",
        "steps": ["找到受影響路段及時間：Oak Street 今天因施工封閉。", "再找公告給的替代路線，注意 instead 導出 Pine Road。", "把目標 downtown 和新路線連起來，形成實際行動筆記。", "選C；A和B仍留在封閉路段，D不是可行路線。", "確認 Pine Road 是給前往市中心的駕駛人，而非所有方向的車流。"],
        "refs": ["cap113", "cap114", "yichang"],
    },
    {
        "focus": "cancellation and continuation",
        "prompt": "A community announcement says, ‘Lightning has canceled the outdoor movie. The indoor talk will still begin in Room 2 at 7:00.’ Which event is still happening?",
        "options": ["The outdoor movie during the lightning", "Both events are canceled", "A sports game tomorrow morning", "The indoor talk in Room 2 at 7:00"],
        "answer": "D",
        "correct": "The indoor talk in Room 2 at 7:00",
        "explanation": "Canceled applies only to the outdoor movie. Still begin marks the indoor talk as continuing, with its room and time unchanged.",
        "strategy": "公告若同時報取消與照常舉行，逐項標上狀態；辨認 still、instead、but 等詞，避免把一個活動的變更套到全部活動。",
        "steps": ["把兩個活動分開：戶外電影與室內講座。", "分別標記狀態：電影因閃電取消；講座仍在 Room 2、7:00 開始。", "題目問仍然舉行者，所以只取狀態為 continuing 的那一項。", "選D；B把取消活動當成照常，C則錯把取消擴大到講座。", "最後核對房間與時間都屬於講座，不是戶外電影的安排。"],
        "refs": ["cap114", "cap113", "cap111"],
    },
    {
        "focus": "speaker purpose",
        "prompt": "A librarian announces, ‘Please return borrowed tablets to the desk before you leave today. Another class needs them this afternoon.’ Why is she making this announcement?",
        "options": ["To ask visitors to return the tablets before leaving", "To explain how tablets are made", "To invite students to borrow more tomorrow", "To announce that the library is closed next month"],
        "answer": "A",
        "correct": "To ask visitors to return the tablets before leaving",
        "explanation": "The direct request and the reason about another class state the immediate purpose: return borrowed tablets today.",
        "strategy": "聽目的題時看「請求／提醒的動詞＋對象＋期限」；背景理由用來確認目的，不要誤當成新的主題。",
        "steps": ["先圈出公告的行動動詞 return，確認聽眾要歸還物品。", "記錄歸還對象 tablets、地點 desk、期限 before leaving today。", "把 another class needs them 當作要求的理由，而不是另一項指令。", "選A；其餘選項談製造、借用或下月閉館，都未被要求。", "檢查答案包含動作、物品與期限，確實回答 why。"],
        "refs": ["cap111", "cap114", "yichang"],
    },
    {
        "focus": "combined factual notes",
        "prompt": "A bus announcement says, ‘Route 6 leaves from Stop B at 4:20 today. Student passes only; cash is not accepted.’ Which note is accurate?",
        "options": ["Route 6, Stop A, 4:02; cash only", "Route 6, Stop B, 4:20; student passes only", "Route 5, Stop B, 4:20; free for everyone", "Route 6, Stop C, 2:40; no passengers"],
        "answer": "B",
        "correct": "Route 6, Stop B, 4:20; student passes only",
        "explanation": "The correct note keeps all four stated fields: route, stop, departure time, and fare condition. The other notes alter at least one field.",
        "strategy": "多欄公告用小表格記路線、站點、時間、限制；逐欄比對，不能因三欄正確就放過一個錯誤條件。",
        "steps": ["依序抽取 route 6、Stop B、4:20、student passes only 四個欄位。", "特別記下 cash is not accepted，避免只記可用票種而漏掉排除條件。", "逐個選項檢查四欄，要求每一欄都和播音吻合。", "選B，因為路線、站點、時間與付款規則全一致。", "回聽式核對一次欄位清單，確認沒有把Stop B、4:20或票種抄錯。"],
        "refs": ["cap111", "cap113", "yichang"],
    },
    {
        "focus": "integrated final instructions",
        "prompt": "A festival update says, ‘Because rain is expected, use the east entrance. The program still starts at 6:00, but move the dance show to the gym. Please bring a reusable cup.’ Which note keeps the final instructions?",
        "options": ["West entrance; noon start; dance show outdoors; bring glass bottles", "Gym entrance; time canceled; no cup needed", "East entrance; 6:00 start; dance show in gym; bring a reusable cup", "East entrance; 6:00 start; dance show canceled; bring a paper plate"],
        "answer": "C",
        "correct": "East entrance; 6:00 start; dance show in gym; bring a reusable cup",
        "explanation": "The note preserves the changed entrance and venue, the unchanged start time, and the requested cup without inventing a cancellation.",
        "strategy": "綜合公告先標示「改了什麼／保持不變／聽眾要做什麼」，再把最後版本合併成筆記；時間沒改不能自行刪除。",
        "steps": ["把更新分成入口、開始時間、表演場地及攜帶物四個欄位。", "辨認因雨而改的是入口與舞蹈表演場地；6:00仍照常。", "記錄聽眾行動 bring a reusable cup，注意沒有取消活動。", "選C；A、B、D分別篡改時地、刪除條件或憑空取消表演。", "按播報次序核對每欄，確認筆記採用更新後安排且保留未變時間。"],
        "refs": ["cap114", "cap113", "cap111"],
    },
]


def make(index, row):
    refs = []
    for key in row["refs"]:
        source = SOURCES[key]
        refs.append({
            "url": source["url"], "title": source["title"], "year": source["year"],
            "subject": "english", "locator": source["locator"],
            "observedPattern": source["pattern"], "reuseDecision": "pattern-only",
            "status": "recorded", "locatorLevel": "item",
        })
    options = [{"id": chr(65 + n), "text": value} for n, value in enumerate(row["options"])]
    return {
        "id": f"question-english-performance-5-iv-9-{index}",
        "subject": "english", "type": "single-choice", "prompt": row["prompt"],
        "options": options, "knowledgeIds": ["kg-english-performance-5-iv-9"],
        "difficulty": "medium",
        "answer": {"value": row["answer"], "explanation": f"正確答案：{row['answer']}。{row['explanation']}"},
        "provenance": {
            "origin": "original", "license": "All rights reserved",
            "sourceUrl": refs[0]["url"], "sourceLocator": "; ".join(ref["locator"] for ref in refs),
            "authoringNote": "原創英文公共公告／廣播筆記題；參考三份由公立國中校方公開之國中教育會考聽力考題／試題說明，以及宜昌國中公開段考英聽題。只改寫能力型態，不複製原題內容、選項、答案或音檔。題組維持draft，完整課程、內容及版權審查尚未完成。",
        },
        "reviewStatus": "draft", "updatedAt": "2026-09-26",
        "lessonId": "lesson-english-performance-5-iv-9", "examPatternRefs": refs,
        "solutionStrategy": row["strategy"], "solutionSteps": row["steps"],
    }


for number, row in enumerate(DATA, 1):
    file = OUT / f"question-english-performance-5-iv-9-{number}.json"
    file.write_text(json.dumps(make(number, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} original questions with exact public-exam locators")
