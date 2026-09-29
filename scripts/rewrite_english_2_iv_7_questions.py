#!/usr/bin/env python3
"""Independently rewrite English 2-IV-7 question-formation items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GCH = "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91.pdf"
ZIQIANG = "https://www.tcjh.tyc.edu.tw/uploads/1548635646492gsGMmT1l.pdf"
DAWAN = "https://www.dwm.kh.edu.tw/upload/344/104_64184/113%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf"

SOURCES = {
    GCH: ("高雄市立國昌國中", "111學年度第一學期八年級第一次定期評量英文科試題", "只參考原卷人事問答、疑問句重建、方法提問與多選項判讀模式；不複製原題、選項或答案。"),
    ZIQIANG: ("桃園市立自強國中", "107學年度第一學期八年級第一次段考英語科試題", "只參考原卷疑問詞辨識與閱讀問答模式；不複製原題、選項、語料或答案。"),
    DAWAN: ("高雄市立大灣國中", "113學年度第一學期八年級英語科第一次段考", "只參考原卷問句與回答配對、行程表及日期資訊擷取模式；不複製原題、選項、表格或答案。"),
}

ITEMS = [
    {
        "answer": "B", "source": (GCH, 36, "printed page 4, matching question 36"),
        "prompt": "A: Someone packed the clay models after the art fair.\nB: Mr. Hsu did.\nWhich question should A ask to learn the person's identity?",
        "options": [("A", "What did Mr. Hsu pack after the art fair?"), ("B", "Who packed the clay models after the art fair?"), ("C", "When did Mr. Hsu pack the clay models?"), ("D", "Where did Mr. Hsu pack the clay models?")],
        "explanation": "回應只用 did 代替前句的動作，沒有重複主詞；因此要問「誰」做了打包動作。B 的 who 對應人，clay models 則保留已知受詞。",
        "strategy": "先確認答句省略了哪個已知動作，再判斷空缺是人、物、時間還是地點；主詞位置的未知人物用 who。",
        "steps": ["先把對話中的已知部分標出：黏土模型被打包，時間是藝術市集結束後。", "回應 Mr. Hsu did 以 did 代替 packed the clay models，真正新增資訊是執行動作的人。", "要詢問動作主詞的人物，疑問詞應放在句首用 Who，而不是詢問物品的 What。", "B 的問句保留 packed 與 clay models，只把未知的人物改成 Who，與回答一一對應。", "核對其餘選項：A 問物品、C 問時間、D 問地點，都不是回答提供的新資訊，因此選 B。"],
    },
    {
        "answer": "C", "source": (GCH, 37, "printed page 4, matching question 37"),
        "prompt": "A: ______?\nB: I placed the seed packets in the labeled drawer before lunch.\nChoose the question that asks about the action and its object.",
        "options": [("A", "Who placed the seed packets in the drawer?"), ("B", "Where did you place the seed packets?"), ("C", "What did you place in the labeled drawer?"), ("D", "When did you place the seed packets in the drawer?")],
        "explanation": "答句同時說出動作 placed 與受詞 seed packets；題目指定要問動作及其物件，C 的 What did you place 正好索取該受詞。",
        "strategy": "不要只看到答句有很多資訊就全選；依題目限定的焦點，區分動作受詞 what、人物 who、地點 where 與時間 when。",
        "steps": ["把答句切成動作 placed、物品 seed packets、地點 labeled drawer、時間 before lunch 四塊。", "題目要求的是 action and its object，焦點落在「放了什麼」，不是誰放、放在哪裡或何時放。", "選項 C 用 What did you place…? 詢問受詞，答句可以直接用 seed packets 回答。", "B、D 雖然也能對應答句裡的真實線索，卻分別只詢問地點和時間，沒有命中指定焦點。", "因此選 C；解 wh-question 時先找資訊缺口，再看該缺口在句中扮演的角色。"],
    },
    {
        "answer": "C", "source": (DAWAN, 4, "PDF page 3, schedule-reading question 4"),
        "prompt": "The rehearsal card lists the robotics team on Thursday at 4:15 p.m.\nWhich question asks specifically for the weekday?",
        "options": [("A", "What time does the robotics team rehearse?"), ("B", "How often does the robotics team rehearse?"), ("C", "What day does the robotics team rehearse?"), ("D", "Where does the robotics team rehearse?")],
        "explanation": "卡片同時列出星期、鐘點與活動。題目特別指定 weekday，應使用 What day；A 問鐘點，B 問頻率，D 問地點。",
        "strategy": "讀行程資料時先把日期粒度分清楚：What day 問星期、What time 問鐘點、How often 問頻率；不可把同屬時間的資訊混為一談。",
        "steps": ["在卡片中圈出 Thursday 與 4:15 p.m.，它們分別是星期與鐘點，並非同一欄。", "題目限定 weekday，表示只要星期幾，不需要回答幾點或每週幾次。", "What day 是詢問星期的自然問法，回答 Thursday 即可完整回應。", "A 的 What time 對應 4:15 p.m.；B 問重複頻率；D 則轉向活動地點。", "故選 C；查看表格時應先確認問題要求的時間尺度，再查對應欄位。"],
    },
    {
        "answer": "A", "source": (DAWAN, 4, "PDF page 2, grammar-choice question 4"),
        "prompt": "A: ______?\nB: At the covered court beside the library.\nChoose the question that asks for the place where the group plays badminton every Saturday.",
        "options": [("A", "Where does the group play badminton every Saturday?"), ("B", "When does the group play badminton every Saturday?"), ("C", "Who plays badminton every Saturday?"), ("D", "How often does the group play badminton at the court?")],
        "explanation": "答句 At the covered court… 是地點片語；問句應以 Where 索取場所。題幹已交代每週六，故不需再問時間或頻率。",
        "strategy": "看回答的句首或核心片語判斷資訊類型；At／in／near 引出的場所通常回應 where，而頻率副詞已給定時不要重問 how often。",
        "steps": ["答句以 At 開頭，後面是 covered court，這是場所而非人物、日期或活動次數。", "問句要索取地點，先選 Where，再保留完整的主詞與活動內容。", "主詞 the group 是第三人稱單數，因此一般現在式問句用 does，後接原形 play。", "B 問時間、C 問參與者；D 問頻率，但 every Saturday 已經給出頻率。", "A 同時符合地點焦點與 does + 主詞 + 原形動詞的句型，故選 A。"],
    },
    {
        "answer": "D", "source": (ZIQIANG, 2, "printed page 1, grammar-choice question 2"),
        "prompt": "A: ______?\nB: Because the lift stopped between floors, we used the stairs.\nChoose the question that asks for the cause of our choice.",
        "options": [("A", "Where did you use the stairs?"), ("B", "When did the lift stop?"), ("C", "How did you reach the lobby?"), ("D", "Why did you use the stairs?")],
        "explanation": "答句的 Because 子句提供改走樓梯的原因；因此問句應以 Why 詢問因果。C 雖問到抵達方式，但不是要求解釋選擇的原因。",
        "strategy": "先辨認 because 引出的因果，再看題目問的是「為何如此決定」還是「實際怎麼做」；why 與 how 不可只憑同一段答案混選。",
        "steps": ["句中 because the lift stopped between floors 是理由，後半句 used the stairs 是採取的行動。", "題目明確問 cause of our choice，資訊缺口是做出選擇的原因，因此要用 Why。", "Why did you use…? 是過去式疑問句：did 已標示過去，主要動詞 use 回到原形。", "C 的 How did you reach…? 會詢問到達方法；答句雖提到樓梯，但不直接回答方法細節。", "D 直接追問改走樓梯的原因，且可由 Because 子句作答，所以選 D。"],
    },
    {
        "answer": "C", "source": (GCH, 49, "printed page 5, sentence-response question 49"),
        "prompt": "A: ______?\nB: By scanning the blue code in the school app twice a day.\nChoose the question that asks about the procedure.",
        "options": [("A", "Why do you check in twice a day?"), ("B", "When do you scan the code?"), ("C", "How do you check in?"), ("D", "Which app do you use to check in?")],
        "explanation": "By scanning… 說明完成簽到的方法與步驟，故應問 How。B 只問時間，D 問應用程式是哪一個；它們都沒有詢問程序。",
        "strategy": "當回答以 by + V-ing 或步驟描述開頭，先判斷是在講方法而非原因、時刻或工具名稱，再選 how。",
        "steps": ["注意答句開頭 By scanning，這個結構通常用來描述採取的方式或手段。", "題目問 procedure，對應「怎麼做」，因此目標疑問詞是 How。", "把問句還原為 How do you check in?，主詞 you 搭配 do，check 使用原形。", "A 的 Why 需要原因；B 的 When 需要時間；D 的 Which 需要在選項中辨認特定應用程式。", "答句補充每天兩次是頻率，但主要回應仍是掃描代碼的方法，所以選 C。"],
    },
    {
        "answer": "A", "source": (GCH, 35, "printed page 4, reading-comprehension question 35"),
        "prompt": "Two shuttle routes serve the campus: the orange route stops at the west gate, and the teal route stops at the sports hall. You need to identify one route from these choices.\nWhich question asks you to select the route?",
        "options": [("A", "Which route stops at the sports hall?"), ("B", "How many routes stop at the sports hall?"), ("C", "Why does the shuttle stop at the sports hall?"), ("D", "Where is the sports hall?")],
        "explanation": "題目要在已知的兩條路線中辨認其中一條，應用 Which + 名詞。A 要求選出路線；B 問數量，C 問原因，D 問場所。",
        "strategy": "看到有限集合（兩條路線、數個時段或候選人）而要選出其中一項，用 Which；若問數量才用 How many。",
        "steps": ["先列出可選集合：orange route 與 teal route，題目不是開放式詢問任意資訊。", "任務是 identify one route，必須從有限候選項中挑出符合條件的一條。", "Which 後接名詞 route，構成 Which route…?，可直接要求辨認候選路線。", "B 會問符合條件的路線有幾條；C 追問停靠原因；D 只問 sports hall 的位置。", "只有 A 同時保留選擇功能與sports hall條件，因此答案為 A。"],
    },
    {
        "answer": "D", "source": (DAWAN, 10, "PDF page 1, listening basic-response question 10"),
        "prompt": "You could not hear the platform number at the station. Which reply politely asks the staff member to say it again?",
        "options": [("A", "Tell me the number now."), ("B", "Why is the number a platform?"), ("C", "I said the number again."), ("D", "Could you repeat the platform number, please?")],
        "explanation": "Could you…please? 以情態助動詞與 please 緩和請求，repeat 明確表示再說一次。D 既禮貌又直接補足聽漏的資訊。",
        "strategy": "需要對方重說時，使用 Could you repeat…? 或 Could you say that again, please?；語氣是否禮貌與請求內容是否明確要一起判斷。",
        "steps": ["情境指出平台號碼沒有聽清楚，溝通目標是請對方重複已說過的內容。", "repeat 是「重複、再說一次」；只用 tell me 並加 now 會顯得命令，也沒有禮貌緩和。", "Could you…? 以 could 提出較客氣的請求，句末 please 再標示禮貌語氣。", "D 的受詞 platform number 清楚指出需要重說的資訊，不會讓對方猜測要重複哪一部分。", "B 不合語意，C 描述自己說過什麼；故 D 同時符合請求功能與情境禮貌。"],
    },
    {
        "answer": "C", "source": (GCH, 44, "printed page 4, matching question 44"),
        "prompt": "A campus guide says, ‘The first-aid station has moved from the gym to the greenhouse.’ Which follow-up asks for its new location?",
        "options": [("A", "Who moved the first-aid station?"), ("B", "Why did the first-aid station move?"), ("C", "Where has the first-aid station moved?"), ("D", "When did the first-aid station move?")],
        "explanation": "已知訊息指出服務站搬遷，題目只想追問新位置；Where 索取地點。A 問搬運者、B 問原因、D 問時間，都不是場所。",
        "strategy": "從新情境抽出待查資料：若事件已知、只缺新地址或位置，就用 where；再檢查助動詞是否與句中的時態相容。",
        "steps": ["導覽員已說明服務站從 gym 搬到 greenhouse，移動這件事本身不是未知資訊。", "追問目標是 new location，因此疑問詞應索取地點，而不是人物、原因或搬遷時間。", "句子使用 has moved，現在完成式疑問句把 has 移到主詞前：Where has the station moved?", "A 問誰搬動，B 用 did 追問過去原因，D 問發生時刻；它們都避開了新位置。", "C 使用 Where 並保留 has moved 的句構，能以 greenhouse 回答，因此選 C。"],
    },
    {
        "answer": "B", "source": (DAWAN, 7, "PDF page 3, reading-comprehension question 7"),
        "prompt": "The festival notice lists a children's puppet show on Saturday at 2:30 p.m. in Hall B. A visitor wants to find out the start time. Which question is best?",
        "options": [("A", "Where will the puppet show begin?"), ("B", "What time does the puppet show start?"), ("C", "Who will watch the puppet show?"), ("D", "Why is the puppet show in Hall B?")],
        "explanation": "通知列出星期、鐘點與場地，訪客明確要查 start time，因此問 What time。B 的資訊焦點是 2:30 p.m.；其他問句分別索取地點、人物或原因。",
        "strategy": "多欄公告題先把需求詞圈出來（start time），再對照資料欄位；when 可問較廣的時間，what time 精確索取鐘點。",
        "steps": ["從公告抽出 Saturday、2:30 p.m.、Hall B 三項資訊，分別代表日期、開始鐘點與地點。", "訪客想知道 start time，所需答案是精確時刻，不是活動在哪裡或由誰參加。", "What time 專門詢問鐘點，start 作為動詞時可搭配助動詞 does 與原形 start。", "A 索取地點、C 索取人物、D 索取原因；即使它們對應公告其他欄位也不回答問題。", "B 能以 2:30 p.m. 作答並精準符合需求，所以選 B。"],
    },
]


def make_ref(url: str, number: int, locator: str) -> dict:
    school, exam, boundary = SOURCES[url]
    year = {GCH: "111-1", ZIQIANG: "107-1", DAWAN: "113-1"}[url]
    return {
        "url": url,
        "title": f"{school}{exam}",
        "year": year,
        "subject": "english",
        "locator": locator,
        "observedPattern": f"只參考第{number}題的人事時地物疑問、回答配對或資訊定位能力；{boundary}",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


def main() -> None:
    if len(ITEMS) != 10:
        raise ValueError("2-IV-7 必須恰有十題，停止以免穩定 ID 越界")
    for n, item in enumerate(ITEMS, 1):
        path = ROOT / f"questions/english/question-english-performance-2-iv-7-{n}.json"
        if not path.is_file():
            raise FileNotFoundError(path)
    for n, item in enumerate(ITEMS, 1):
        path = ROOT / f"questions/english/question-english-performance-2-iv-7-{n}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        url, source_number, locator = item["source"]
        data["prompt"] = item["prompt"]
        data["options"] = [{"id": key, "text": text} for key, text in item["options"]]
        data["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
        data["examPatternRefs"] = [make_ref(url, source_number, locator)]
        data["solutionStrategy"] = item["strategy"]
        data["solutionSteps"] = item["steps"]
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": url,
            "sourceLocator": f"{SOURCES[url][0]}公開原卷：{locator}。只取命題能力／資料閱讀模式，不重製原題。",
            "authoringNote": "依官方課綱、Knowledge Graph 與公立學校公開英語試題之精確 item-level pattern-only 證據獨立重寫；未複製原題、選項、圖表或答案。題目維持 draft，尚待完整版本研究與發布審查。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-09-24"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    for url, (institution, exam, boundary) in SOURCES.items():
        entry = {
            "institution": institution,
            "url": url,
            "subjects": ["english"],
            "availableMaterial": exam,
            "researchUse": "英語 2-Ⅳ-7 人事時地物疑問句、回答配對、問句重建與行程資料定位；只作逐題 pattern-only 依據。",
            "licenseBoundary": boundary,
        }
        existing = next((row for row in catalog["sources"] if row.get("url") == url), None)
        if existing:
            existing.update(entry)
        else:
            catalog["sources"].append(entry)
    catalog["questionSourceUrls"] = sorted({row["url"] for row in catalog["sources"] if row.get("url")})
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rewritten": len(ITEMS), "allRemainDraft": True, "publicSchools": len(SOURCES)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
