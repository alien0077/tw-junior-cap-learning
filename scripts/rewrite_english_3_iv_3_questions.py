#!/usr/bin/env python3
"""Rewrite 3-Ⅳ-3 questions from verified public-school exam patterns."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "questions/english/question-english-performance-3-iv-3-{}.json"

SOURCES = {
    "xiaogang": {
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/11%E4%B8%80%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F/3%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/110-1-3%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立小港國中110學年度第一學期七年級第三次段考英文試題",
        "year": "110-1",
        "locator": "PDF第2頁第16題：依圖像標記判斷場所規則",
        "pattern": "考生需將圖像標記與一項場所限制配對；本題改寫為畫廊拍攝規定，未沿用原標誌或選項。",
    },
    "neihu114": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1753839175199ERtbxbag.pdf",
        "title": "臺北市立內湖國中113學年度第二學期七年級第三次段考英文試題",
        "year": "113-2",
        "locator": "PDF第3頁第46–48題：活動時間及方向路線判讀",
        "pattern": "試題要求依時間資訊判斷活動是否已開始，及按方向詞和地標重組移動路線；本題採全新地點、時刻與路線。",
    },
    "neihu111": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1675415417654MTSxFV3o.pdf",
        "title": "臺北市立內湖國中111學年度第一學期七年級第二次段考英文試題卷",
        "year": "111-1",
        "locator": "PDF第3頁第34、35題及第4頁第52–54題：規則適用與泳池時刻表判讀",
        "pattern": "題目需從規則文字辨認違規行為，或把表格營業時段與當下星期、時間交叉核對；本題使用新場館和新數值。",
    },
    "yichang": {
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=359&cfsn=2135&name=110-2%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%838%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E6%AE%B5%E8%80%83%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E6%9E%97%E9%9D%9C%E6%85%88.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中110學年度第二學期八年級第一次段考英文科試題與聽力稿",
        "year": "110-2",
        "locator": "聽力稿PDF第11頁第3題：依警告標示語句辨認須採取的安全行動",
        "pattern": "從簡短警告標示擷取危險來源並選擇安全反應；本題改寫成校園器材區警示與避讓行動。",
    },
    "neihu113": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1753839175199ERtbxbag.pdf",
        "title": "臺北市立內湖國中113學年度第二學期七年級第三次段考英文試題",
        "year": "113-2",
        "locator": "PDF第2頁第32題：依受傷情境判斷應前往的服務場所",
        "pattern": "從情境中的受傷線索選擇相應的照護設施；本題改成活動現場的急救標示與求助行動。",
    },
    "guochang": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%BA%8C%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87-%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立國昌國中109學年度第二學期二年級第二次定期評量英文科試題卷",
        "year": "109-2",
        "locator": "PDF第3頁第21題：從對話解讀攤位標示所載優惠條件",
        "pattern": "讀者需把告示中的購買條件轉成可採取的消費決定；本題改成借用器材的時限條件。",
    },
    "lab": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1675415417654MTSxFV3o.pdf",
        "title": "臺北市立內湖國中111學年度第一學期七年級第二次段考英文試題卷與聽力稿",
        "year": "111-1",
        "locator": "聽力稿PDF第6頁第11題：判讀實驗室規定中可做與不可做的事",
        "pattern": "須同時分辨允許事項與禁止事項；本題換成圖書館的手機靜音規則。",
    },
}

ITEMS = [
    {
        "source": "xiaogang", "answer": "A",
        "prompt": "Beside a large aquarium tank, a crossed-out hand symbol appears above 'PLEASE DO NOT TAP THE GLASS.' Which visitor follows the sign?",
        "options": ["A visitor watches the fish without touching the tank.", "A visitor taps the glass softly to get a fish's attention.", "A visitor puts a hand inside the tank.", "A visitor knocks harder so everyone can hear."],
        "explanation": "Both the crossed-out hand and the sentence forbid contact with the glass. A follows the rule; the other actions touch or strike the tank.",
        "strategy": "把圖示代表的動作和文字指令交叉比對，再選同時遵守兩者的行為。",
        "steps": ["先看位置：標示貼在大型水族箱旁，規則對象是觀眾與魚缸。", "辨認被劃掉的手勢，表示不要用手接觸。", "再讀 DO NOT TAP THE GLASS，確認不能敲擊玻璃。", "A只觀看而不碰觸；B、D敲玻璃，C把手伸進缸內，全部違反規則。", "答案選A；公共展示物旁的禁止符號要轉成具體可做／不可做行為。"],
    },
    {
        "source": "neihu114", "answer": "C", "locator": "PDF第3頁第47–48題：把方向詞與地標組成可執行路線",
        "prompt": "A museum map says: 'Leave the lobby, pass the café, then turn right at the blue stairs.' Where is the next turn?",
        "options": ["At the café entrance.", "At the lobby.", "At the blue stairs.", "After reaching the second floor."],
        "explanation": "Pass the café means continue beyond it; 'turn right at the blue stairs' identifies the turning point. The directions do not say to go upstairs.",
        "strategy": "拆解路線的先後動作，分清楚『經過某處』與『在某處轉彎』；轉向詞後的地標才是轉彎位置。",
        "steps": ["先標出起點與移動方向：離開大廳，往地圖指示路徑前進。", "把 pass the café 解作經過咖啡店，不在那裡轉向。", "再讀 turn right at the blue stairs；藍色樓梯才是右轉地標。", "A把經過點當轉彎點，B是起點，D額外推測上樓，均無文字支持。", "選C；移動時每完成一個動作，再確認下一個地標。"],
    },
    {
        "source": "neihu111", "answer": "B", "locator": "PDF第4頁第53題：依泳池開放時間表判斷星期與時段",
        "prompt": "A recreation center's weekend schedule says it opens at 10:30 a.m. and closes at 7:00 p.m. A family arrives at 9:50 a.m. on Sunday. What should they do?",
        "options": ["Enter now because Sunday is a weekend.", "Wait until 10:30 a.m. before entering.", "Return at 7:00 a.m. because that is the opening time.", "Come back after 7:00 p.m. to enter."],
        "explanation": "Sunday uses the weekend row, whose opening time is 10:30 a.m. Since 9:50 is earlier, the family must wait; 7:00 p.m. is the closing time.",
        "strategy": "先選對星期對應的時段，再比較抵達時間與開門端點；同時看清 a.m. 和 p.m.。",
        "steps": ["確認今天是 Sunday，因此使用週末時刻表。", "讀出開門為10:30 a.m.，關門為7:00 p.m.。", "把9:50 a.m.與10:30 a.m.比較，抵達早了40分鐘。", "所以應等待開門；C、D把晚間閉館時間誤讀成可入場時刻。", "答案選B；遇到時刻表要同時核對星期、上午／下午與營業端點。"],
    },
    {
        "source": "yichang", "answer": "D", "locator": "聽力稿PDF第11頁第3題：由警告標示選擇安全行動",
        "prompt": "A notice beside a school garden reads 'WASPS NEAR THE FLOWERS — KEEP BACK.' What is the safest choice?",
        "options": ["Touch the flowers to see whether wasps are nearby.", "Shake the plants so the insects will leave.", "Stand closer and take a flash photo.", "Stay away from the marked area and tell an adult if someone is at risk."],
        "explanation": "The warning identifies wasps and explicitly asks people to keep back. D follows both the hazard information and the requested distance; the other actions approach or disturb the insects.",
        "strategy": "把警告中的危險來源與要求動作連起來；安全題不能只翻譯名詞，還要落實距離或避讓指令。",
        "steps": ["先找警告對象：flowers 附近有 wasps。", "再讀命令 keep back，意思是保持距離，不要進入標示區。", "把危險和命令合併，選擇不靠近並在有人遇險時通知大人。", "A、B會碰觸或驚擾蜂群，C更靠近危險源，都違反警告。", "答案選D；不要自行驅趕蜂群，讓成人或校方處理。"],
    },
    {
        "source": "neihu113", "answer": "C", "locator": "PDF第2頁第32題：依受傷情境判斷照護場所",
        "prompt": "At a school sports day, a sign with a green cross says 'FIRST AID — REPORT INJURIES HERE.' A runner has a bleeding knee. What should the teammate do?",
        "options": ["Send the runner to the ticket booth.", "Tell the runner to keep racing without help.", "Take the runner to the first-aid station and alert the staff.", "Look for a place to buy a new uniform."],
        "explanation": "The green cross and FIRST AID label identify the care point, while REPORT INJURIES HERE tells visitors what to do. C uses both the location and action cues.",
        "strategy": "設施名稱回答『去哪裡』，命令句回答『怎麼做』；兩種線索都吻合時才完成判讀。",
        "steps": ["從情境抓出關鍵事件：跑者膝蓋流血，需要處理受傷。", "讀標示上的 FIRST AID，辨認為急救／基本傷口協助處。", "再讀 REPORT INJURIES HERE，知道應向該處工作人員通報。", "C同時符合地點和行動；其他選項的票亭、繼續比賽或買衣服都不處理傷勢。", "答案選C；若傷勢嚴重，交由現場成人和急救人員處理。"],
    },
    {
        "source": "neihu111", "answer": "A", "locator": "PDF第3頁第35題：依活動規則辨認違規行為",
        "prompt": "A school notice says: 'For the class art display, use the labeled paper-recycling bin; plastic wrappers go in the general-waste bin.' Which student follows the notice?",
        "options": ["Mina puts a clean paper worksheet in the labeled bin.", "Leo puts a plastic wrapper in the paper bin.", "Annie mixes a paper cup with food scraps in the labeled bin.", "Ben ignores the labels because all bins are the same."],
        "explanation": "The notice classifies clean paper separately from plastic wrappers and other waste. A places a paper worksheet in the matching bin; the other choices mix materials or ignore the sorting rule.",
        "strategy": "先找分類標籤，再逐項比對物品材質與限制條件；注意題目是否限定乾淨、可回收或特定容器。",
        "steps": ["讀出兩條分類規則：紙類進標示的紙回收桶，塑膠包裝進一般垃圾桶。", "逐一確認物品材質；worksheet 是紙，且題幹沒有說它沾污。", "Mina把紙張投入紙類桶，符合標示。", "Leo放錯材質，Annie把混合廢棄物放進去，Ben則完全不看分類標籤。", "答案選A；實際分類時若物品沾有食物或材質複合，先查詢校方規則。"],
    },
    {
        "source": "neihu114", "answer": "D", "locator": "PDF第3頁第46題：以活動起始時間和當下時刻判斷行動",
        "prompt": "A field-trip notice says the shuttle leaves at 8:40 a.m. Students must check in ten minutes earlier. At what time should a student arrive?",
        "options": ["8:50 a.m.", "9:40 a.m.", "8:40 p.m.", "8:30 a.m."],
        "explanation": "Ten minutes earlier than 8:40 a.m. is 8:30 a.m. The notice gives a check-in time, not a later arrival time.",
        "strategy": "先分清公告中的基準事件與提前／延後量，再在同一上午時間軸上加減分鐘。",
        "steps": ["圈出接駁車發車時間8:40 a.m.。", "理解 check in ten minutes earlier 是報到要比發車早10分鐘。", "從8:40往前倒數10分鐘，得到8:30。", "A反而晚10分鐘，B晚一小時，C把上午誤成晚上。", "答案選D；到場後仍需依現場公告確認集合地點。"],
    },
    {
        "source": "guochang", "answer": "B", "locator": "PDF第3頁第21題：從對話解讀告示中的消費條件",
        "prompt": "A school equipment desk displays: 'Borrow a tablet for up to 90 minutes. Return it no later than 4:30 p.m., when the library closes.' A student borrows one at 3:20 p.m. What is the latest return time?",
        "options": ["5:00 p.m., because 90 minutes is always allowed.", "4:30 p.m., because the closing rule comes first.", "6:20 p.m., after adding three hours.", "There is no need to return the tablet."],
        "explanation": "Ninety minutes after 3:20 would be 4:50, but the notice also requires return no later than 4:30. The earlier limit controls, so B is the latest permitted time.",
        "strategy": "遇到同時存在的條件，要全部遵守；分別算出各自期限後，採用較早、較嚴格的限制。",
        "steps": ["讀出借用上限：自3:20起最多90分鐘，算到4:50 p.m.。", "另讀出第二個條件：必須在4:30 p.m.閉館前歸還。", "比較兩個期限，4:30比4:50早，因此它才是實際最後期限。", "A只採用90分鐘而忽略閉館條件；C計算錯誤，D違反歸還規定。", "答案選B；多條件公告要逐條列出，再以最先到期者安排行動。"],
    },
    {
        "source": "lab", "answer": "C", "locator": "聽力稿PDF第6頁第11題：判讀實驗室允許與禁止的行動",
        "prompt": "A library sign shows a crossed-out speaker and says 'SILENT STUDY AREA.' Which action is allowed?",
        "options": ["Play a video aloud for a friend.", "Make a phone call beside the reading desks.", "Switch the phone to silent mode and read quietly.", "Turn up the speaker so everyone can hear the lesson."],
        "explanation": "The crossed-out speaker and silent-study wording prohibit noise. C is compatible with the rule; A, B, and D create sound in the marked area.",
        "strategy": "標示圖示和文字要互相核對；題目問『允許』時，找不違反任何一條限制的選項。",
        "steps": ["辨認區域用途：silent study area，表示安靜自習區。", "讀 crossed-out speaker，確認外放聲音被禁止。", "檢查選項是否產生聲音；切換靜音並安靜閱讀符合兩項線索。", "A、D會外放，B在座位旁通話，也會破壞安靜規則。", "答案選C；若需要通話，離開標示區再進行。"],
    },
    {
        "source": "neihu111", "answer": "C", "locator": "PDF第4頁第53題：依泳池營業表格判斷星期與開放時段",
        "prompt": "A pool board lists Tuesday–Friday hours as 7:00–11:30 a.m. and 5:00–9:00 p.m. It is Tuesday at 12:15 p.m. When does swimming open again?",
        "options": ["At 12:30 p.m.", "At 4:15 p.m.", "At 5:00 p.m.", "At 7:00 p.m."],
        "explanation": "The morning session ends at 11:30 a.m., and the evening session begins at 5:00 p.m. At 12:15 the pool is between sessions, so the next one starts at 5:00 p.m.",
        "strategy": "將一天分成表格列出的營業區段；若現在落在兩段之間，答案是下一段的開始時刻。",
        "steps": ["確認 Tuesday 使用 Tuesday–Friday 時段。", "讀出兩段開放時間：上午7:00至11:30，以及下午5:00至晚上9:00。", "12:15 p.m. 已晚於上午場結束，且早於晚間場開始。", "下一個游泳時段因此在下午5:00開始；其他選項都不是下一個開放端點。", "答案選C；分段營業時刻表要找當下之後最近的開放區間。"],
    },
]


for number, item in enumerate(ITEMS, 1):
    path = Path(str(BASE).format(number))
    data = json.loads(path.read_text(encoding="utf-8"))
    source = SOURCES[item["source"]]
    data["prompt"] = item["prompt"]
    data["options"] = [{"id": chr(65 + index), "text": text} for index, text in enumerate(item["options"])]
    data["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
    data["solutionStrategy"] = item["strategy"]
    data["solutionSteps"] = item["steps"]
    data["provenance"]["sourceUrl"] = source["url"]
    locator = item.get("locator", source["locator"])
    data["provenance"]["sourceLocator"] = f"{source['title']}；{locator}。本題依題型與推理能力重新創作，不複製原題、選項、圖像或答案。"
    data["provenance"]["authoringNote"] = "原創題幹與選項；僅將公立學校公開試題作為題型與推理能力參照。答案、策略及逐步解說為本題獨立撰寫；保持draft，未執行Terra複核。"
    data["examPatternRefs"] = [{
        "url": source["url"], "title": source["title"], "year": source["year"],
        "subject": "english", "locator": locator,
        "observedPattern": source["pattern"], "reuseDecision": "pattern-only",
        "status": "recorded", "locatorLevel": "item",
    }]
    data["reviewStatus"] = "draft"
    data["updatedAt"] = "2026-09-24"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
