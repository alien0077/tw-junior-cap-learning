"""Replace 3-IV-6 all-A grammar drills with contextual original items and exact exam locators."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-26"

SOURCES = {
    "kc108": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C-1%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87-%E8%A9%A6%E9%A1%8C%E5%8D%B7.pdf", "高雄市立國昌國中108學年度第2學期一年級第3次段考英文", "108-2", "高雄市立國昌國民中學", "一年級英文段考原卷；第1頁第16題測現在簡單式、第19題測 there is；第2頁第24題對照過去時間與 be 動詞。"),
    "kc110": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E8%8B%B1%E8%AA%9E%E5%8D%B7.pdf", "高雄市立國昌國中110學年度第2學期一年級第3次段考英文", "110-2", "高雄市立國昌國民中學", "一年級英文段考原卷；第2頁第18題以頻率副詞與時間表達重複習慣、第21題以 there is 表存在、第28至29題比較過去與現在狀態。"),
    "kc114g8": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/2-%E8%8B%B1%E6%96%87_3.pdf", "高雄市立國昌國中114學年度第1學期八年級第1次定期評量英文", "114-1", "高雄市立國昌國民中學", "八年級英文定期評量原卷；第1頁第7題以 last Friday 對照現在狀態，第9題區分 because 與 because of。"),
    "kc114g7first": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87_3.pdf", "高雄市立國昌國中114學年度第1學期一年級第1次段考英文", "114-1", "高雄市立國昌國民中學", "一年級英文段考原卷；第1頁第3題詢問 brushes 的所在位置並依問句選擇地點回答。"),
    "kc111g8": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中111學年度第1學期八年級第3次段考英文", "111-1", "高雄市立國昌國民中學", "八年級英文段考原卷；第3頁第28至30題以 Is there... 詢問圖書館位置並依路線資訊判讀地點。"),
    "nh110g8": ("https://www.nhjh.tp.edu.tw/uploads/1659511832873JPCBQBvo.pdf", "臺北市立內湖國中110學年度第2學期八年級第2次段考英文", "110-2", "臺北市立內湖國民中學", "八年級英文段考原卷；第2頁第17題比較跑步快慢、第21題判斷圖書館義務規則。"),
    "nh113g8": ("https://www.nhjh.tp.edu.tw/uploads/1753840039444z3K5m38Y.pdf", "臺北市立內湖國中113學年度第2學期八年級第1次段考英文", "113-2", "臺北市立內湖國民中學", "八年級英文段考原卷；第2頁第13題以 must 測試遵守規則的義務、第22題比較新舊錄音機、第24至26題比較級。"),
    "nh111g8": ("https://www.nhjh.tp.edu.tw/uploads/1675416243642o6V5uNiI.pdf", "臺北市立內湖國中111學年度第1學期八年級第2次段考英文", "111-1", "臺北市立內湖國民中學", "八年級英文段考原卷；第2頁第21題以 To make... 表達目的、第19題以 stop to look 判斷不定詞用途。"),
    "kc112g7": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91_6.pdf", "高雄市立國昌國中112學年度第2學期一年級第3次段考英文", "112-2", "高雄市立國昌國民中學", "一年級英文段考原卷；第1頁第1題依圖片判讀兩人正在進行的動作。"),
    "kc114g7": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87_4.pdf", "高雄市立國昌國中114學年度第1學期一年級第2次段考英文", "114-1", "高雄市立國昌國民中學", "一年級英文段考原卷；第1頁第8題以 Look 與 now 判斷現在進行中的烹調動作。"),
}

ITEMS = [
    {
        "prompt": "The school shuttle ___ at 7:20 every weekday, so students should be at the stop before then.",
        "options": ["arrived", "arrives", "is arriving", "arrive"], "answer": "B",
        "explanation": "正確答案 B。every weekday 表示固定班次，主詞 the school shuttle 是單數，現在簡單式動詞要加 -s。",
        "strategy": "先把固定時刻表辨認為規律，再讓單數主詞與現在式動詞一致。",
        "steps": ["圈出 every weekday，判定句子描述反覆發生的固定班次。", "確認主詞是單數的 the school shuttle，不是複數的學生。", "固定安排通常用現在簡單式；因此排除只表示一次過去的 arrived。", "現在簡單式遇到第三人稱單數 shuttle，動詞加 -s，得到 arrives。", "把句子放回公告情境朗讀，確認它是在說一般班表，不是此刻正在進站。"],
        "refs": [("kc108", "第16題：以 sometimes 表示反覆發生的天氣情形，判斷第三人稱單數現在式", "參照頻率線索搭配現在簡單式的命題模式；本題改寫為校車時刻表。"), ("kc110", "第18題：以 every two weeks 描述固定清潔頻率並判斷動詞形式", "參照週期性習慣與動詞形式的對應；題幹及情境均為原創。")],
    },
    {
        "prompt": "At yesterday’s exhibition, Mia ___ her design to the judges before lunch.",
        "options": ["presents", "is presenting", "presented", "present"], "answer": "C",
        "explanation": "正確答案 C。yesterday 和 before lunch 把事件放在已結束的過去，應使用 presented。",
        "strategy": "把事件放上時間線；已結束的昨天事件用過去式，不受現在的閱讀情境影響。",
        "steps": ["先定位時間詞 yesterday，確認展覽發表已經發生。", "before lunch 補充的是昨天事件的先後，不會把它變成現在進行。", "主詞 Mia 是單數，但過去式規則動詞不再另外加現在式的 -s。", "選擇 presented；presents 表習慣或現在，is presenting 表此刻正在發表。", "回讀完整句，確認事件時間、動詞形式與 before lunch 的順序一致。"],
        "refs": [("kc108", "第24題：以 this morning 詢問過去在家與否，使用 were／was 回答", "參照已結束時間與過去 be 動詞的配對。"), ("kc114g8", "第7題：last Friday 的受傷事件與 now 的狀態分置不同時間", "參照過去事件和目前結果不可混用時態；本題改為發表作品。")],
    },
    {
        "prompt": "A visitor asks what is on the library wall. Which sentence correctly reports one map?",
        "options": ["There are a map on the wall.", "There has a map on the wall.", "There is a map on the wall.", "There is maps on the wall."], "answer": "C",
        "explanation": "正確答案 C。there be 句型依後方名詞決定 be 動詞；a map 是單數，因此用 there is。",
        "strategy": "在 there be 句型中，先找 be 動詞後面的名詞，再決定 is 或 are。",
        "steps": ["辨認句子任務是報告牆上『有一張地圖』，不是表示某人擁有地圖。", "找到真正決定 be 動詞的名詞 a map。", "a map 為單數，be 動詞選 is，而不是 are。", "There has 不構成此處要表達存在的 there be 句型；maps 複數也不能搭配 is。", "讀出 There is a map on the wall，確認數量、存在關係和地點介系詞完整。"],
        "refs": [("kc108", "第19題：以 There is... 描述五月通常有大量雨水", "參照 there is 表示存在的句型；本題將不可數天氣改為單數可數地圖。"), ("kc110", "第21題組：There is a new supermarket in town", "參照 there is 與單數名詞的搭配，不沿用原句內容。")],
    },
    {
        "prompt": "You need to ask where the meeting room is. Which is the correct direct question?",
        "options": ["Where the meeting room is?", "Where does the meeting room?", "Where is the meeting room?", "Where is the room meeting?"], "answer": "C",
        "explanation": "正確答案 C。直接 wh 問句的順序是疑問詞＋be 動詞＋主詞；room 是位置所問的對象。",
        "strategy": "先找疑問詞，再檢查 be 動詞是否移到主詞前；不要把間接問句語序搬進直接問句。",
        "steps": ["確定問題要找 location，因此使用疑問詞 Where。", "句子的主詞是 the meeting room，be 動詞是 is。", "直接問句需把 is 放在主詞前，形成 Where is the meeting room...?。", "Where the meeting room is 是間接問句內部語序，不能單獨當直接問句；其他選項也缺少正確骨架。", "在句尾補問號並朗讀，確認問句自然詢問房間位置。"],
        "refs": [("kc114g7first", "第3題：詢問 brushes 的所在位置，並從選項辨認地點答句", "參照 Where＋be 動詞＋主詞的直接問句語序。"), ("kc111g8", "第28題組：Is there a library around here? 並接續詢問如何前往", "參照以問句取得地點資訊的對話任務；本題重新設計句型與地點。")],
    },
    {
        "prompt": "The east hallway is 40 meters long; the north hallway is 65 meters long. Which sentence states the same comparison?",
        "options": ["The east hallway is longer than the north hallway.", "The north hallway is longer than the east hallway.", "The two hallways are the same length.", "The east hallway is the longest of the two hallways."], "answer": "B",
        "explanation": "正確答案 B。65 大於 40，因此北側走廊比東側長；原句『東側較短』可反向表達為『北側較長』。",
        "strategy": "先把兩個數量放在同一尺度比較，再檢查比較級方向與 than 後的對象。",
        "steps": ["記下東側 40 公尺、北側 65 公尺，避免被 east／north 名稱干擾。", "比較 65 和 40，判斷北側較長、東側較短。", "比較級句型需用 longer than，並把較長者放在主詞位置。", "B 正確反向改述；A 倒置長短，C 抹去差異，D 的最高級不適用於兩者比較。", "用數字回查：65 > 40，與 B 所說的北側較長一致。"],
        "refs": [("nh113g8", "第22題：比較新錄音機與舊錄音機的 fashionable 程度", "參照比較級與 than 後比較對象的句型；本題改為校園距離。"), ("nh110g8", "第17題：以 slower than 比較姊姊與弟弟跑步速度", "參照形容詞比較級及比較方向的判讀。")],
    },
    {
        "prompt": "The laboratory rule requires eye protection during every experiment. Students ___ wear safety goggles before starting.",
        "options": ["could", "might", "must", "would"], "answer": "C",
        "explanation": "正確答案 C。題目明說這是每次實驗都必須遵守的規則，must 表達強制義務；could、might 是可能或能力，would 不表此處規定。",
        "strategy": "分辨規則、建議與可能性；只有規則要求時才選表義務的情態動詞。",
        "steps": ["抓住 requires 與 every experiment，判斷這是規定，不是個人偏好。", "把規定轉成英文義務語氣，而不是能力、可能性或假設。", "must 後接原形動詞 wear，不加 to，也不加 -s。", "選 must；could 和 might 力度不足以表達規定，would 也不合語境。", "檢查完整要求：Students must wear safety goggles before starting，義務與動作均清楚。"],
        "refs": [("nh113g8", "第13題：學生 must obey 規則以維持安全", "直接參照情態動詞 must 表示安全義務的考點。"), ("nh110g8", "第21題：以 has to／mustn’t 判斷圖書館行為規則", "參照規定、必要性與禁止語氣的區分。")],
    },
    {
        "prompt": "Mina opened the school library app ___ a dictionary for her science report.",
        "options": ["because she finds", "to find", "for find", "finding to"], "answer": "B",
        "explanation": "正確答案 B。Mina 開啟 App 的目的，是尋找字典；to find 可接在主要動作後表達目的。",
        "strategy": "問「她做前一個動作是為了什麼？」若後句回答目的，可用 to＋原形動詞。",
        "steps": ["辨認主要動作：Mina 開啟圖書館 App。", "追問她為什麼開啟 App；後方內容是尋找字典的目的。", "目的的不定詞用 to＋原形動詞，因此 find 保持原形。", "to find 能直接表目的；because 後需完整子句，for 後不能直接接原形 find。", "將句子譯回「她開啟 App 來找字典」，確認前後動作的目的關係。"],
        "refs": [("nh111g8", "第21題：To make a lot of money 放在句首說明公司搬遷工廠的目的", "直接參照 to＋原形動詞表目的的句型；本題改為查找字典。")],
    },
    {
        "prompt": "The basketball practice moved indoors ___ heavy rain made the outdoor court slippery.",
        "options": ["although", "because of", "because", "so"], "answer": "C",
        "explanation": "正確答案 C。空格後是有主詞 heavy rain 和動詞 made 的完整子句，應用 because 引出原因；because of 後面須接名詞片語。",
        "strategy": "看連接詞後面的結構：完整主詞＋動詞子句用 because，名詞片語才用 because of。",
        "steps": ["找出結果：練習移到室內；接下來要說明原因。", "檢查空格後的內容，heavy rain 是主詞，made 是動詞，構成完整子句。", "because 可以連接原因子句，因此語意和結構都符合。", "because of 後應接名詞片語；although 表讓步，so 會把結果方向接反。", "朗讀全句確認因果：大雨使室外球場濕滑，所以練習移到室內。"],
        "refs": [("kc114g8", "第9題：We didn’t go to the park ___ the rain was too heavy，區分 because 子句與 because of 名詞片語", "直接參照 because／because of 的結構差異。"), ("kc108", "第5題：以 because 連接地面濕滑與前一晚下雨的原因", "參照 because 後接完整原因句的使用模式。")],
    },
    {
        "prompt": "Look! Two volunteers ___ the event map right now; one is marking the exits and the other is checking the labels.",
        "options": ["marks", "marked", "are marking", "is marking"], "answer": "C",
        "explanation": "正確答案 C。Look 與 right now 指眼前正在發生的動作；主詞 two volunteers 是複數，使用 are marking。",
        "strategy": "同步核對「正在發生」的時間線與主詞單複數，再組 be＋V-ing。",
        "steps": ["Look 與 right now 都指向說話當下正在進行的工作。", "確認主詞 two volunteers 為複數，助動詞須用 are。", "現在進行式結構是 be＋動詞-ing，mark 變成 marking。", "marks 是習慣式、marked 是過去式；is marking 則與複數主詞不一致。", "用後面的 one...the other... 檢查：兩位志工都正做不同工作，複數主詞合理。"],
        "refs": [("kc114g7", "第8題：Look! Eric’s sister is cooking now", "直接參照 Look／now 與 be＋V-ing 的現在進行式線索。"), ("kc112g7", "第1題：依圖片辨認 Susan 與兄弟正在進行的動作", "參照以人物當下活動判讀現在進行式的題型。")],
    },
    {
        "prompt": "The chess club ___ in Room 12 every Friday, but this week it ___ in the library while Room 12 is repaired.",
        "options": ["meets; is meeting", "met; meets", "meet; is meeting", "meets; meet"], "answer": "A",
        "explanation": "正確答案 A。every Friday 是固定例行安排，用現在簡單式 meets；this week 表示暫時改到圖書館，現在進行式 is meeting 呈現本週安排。",
        "strategy": "同句出現兩條時間線時分開判斷：常態安排用現在簡單式，暫時例外用現在進行式。",
        "steps": ["將 but 前後分成兩個時間範圍：every Friday 的常態，以及 this week 的臨時變動。", "主詞 the chess club 為單數；常態動詞用現在簡單式 meets。", "本週暫時借用圖書館，需用現在進行式，單數 be 動詞為 is。", "第二空接 meeting，組成 is meeting；meet 不可直接接在 is 後作原形。", "回讀 while Room 12 is repaired，確認短期替代地點與暫時性安排相符。"],
        "refs": [("kc108", "第16題：頻率副詞描述固定天氣模式並使用現在簡單式", "參照常態／重複事件的現在簡單式。"), ("kc114g7", "第8題：以 Look 與 now 描寫此刻進行的烹調活動", "參照暫時進行中的活動使用 be＋V-ing；本題另以 this week 表暫時安排。")],
    },
]

def make_ref(key, locator, observed):
    url, title, year, _, _ = SOURCES[key]
    return {"url": url, "title": title, "year": year, "subject": "english", "locator": locator,
            "locatorLevel": "item", "observedPattern": observed, "reuseDecision": "pattern-only", "status": "recorded"}

def main():
    for index, item in enumerate(ITEMS, 1):
        path = ROOT / f"questions/english/question-english-performance-3-iv-6-{index}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["prompt"] = item["prompt"]
        data["options"] = [{"id": chr(65 + j), "text": text} for j, text in enumerate(item["options"])]
        data["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
        data["solutionStrategy"] = item["strategy"]
        data["solutionSteps"] = item["steps"]
        data["examPatternRefs"] = [make_ref(*ref) for ref in item["refs"]]
        data["provenance"]["sourceUrl"] = data["examPatternRefs"][0]["url"]
        data["provenance"]["sourceLocator"] = "依公立國中公開段考逐題研究句型、語境與推理模式；各題精確原卷題號見 examPatternRefs。只作 pattern-only 命題參照，不複製原題、選項或答案。"
        data["provenance"]["authoringNote"] = "依官方課綱與本單元 KG 獨立撰寫情境、選項、答案、繁中解析及步驟；公校原卷僅作可追溯能力模式參照。單元內容與版權 QA 未完成，維持 draft。"
        data["reviewStatus"] = "draft"
        data["updatedAt"] = TODAY
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    known = {entry["url"] for entry in catalog["sources"]}
    for url, title, year, institution, material in SOURCES.values():
        if url not in known:
            catalog["sources"].append({
                "institution": institution, "url": url, "subjects": ["english"],
                "availableMaterial": f"{title}；{material}",
                "researchUse": "校方公開段考原卷只作英文句型能力與題型模式研究；本專案不複製原題文字、選項、圖表或答案。",
                "licenseBoundary": "公開查閱不等於可重製；只保留可追溯的學校原卷 URL 與題號定位，題目及解析均獨立撰寫。",
                "sourceLocator": material,
            })
            known.add(url)
        if url not in catalog["questionSourceUrls"]:
            catalog["questionSourceUrls"].append(url)
    catalog["updatedAt"] = TODAY
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Re-authored 10 original 3-IV-6 questions with exact public-school item locators; all remain draft.")

if __name__ == "__main__":
    main()
