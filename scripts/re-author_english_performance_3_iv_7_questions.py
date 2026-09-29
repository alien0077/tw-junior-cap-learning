"""Re-author English 3-IV-7 dialogue comprehension items with verified public-exam patterns."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-26"
SOURCES = {
    "kc108g7": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C-1%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87-%E8%A9%A6%E9%A1%8C%2B%E7%AD%94%E6%A1%88%E5%8D%B7_1.pdf", "高雄市立國昌國中108學年度第2學期一年級第2次定期評量英文", "108-2", "高雄市立國昌國民中學", "一年級英文定期評量原卷；第4頁第34題判斷廣告溝通目的，第4頁第36題依上下文判斷 it 的指涉。"),
    "kc108g9": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E.pdf", "高雄市立國昌國中108學年度英文科段考", "108", "高雄市立國昌國民中學", "九年級英文試題原卷；第29題讀完包含角色對話及事件結果的寓言後，推論故事寓意。"),
    "kc114g7": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87_3.pdf", "高雄市立國昌國中114學年度第1學期一年級第1次段考英文", "114-1", "高雄市立國昌國民中學", "一年級英文段考原卷；第3題以 Where are the brushes? 詢問物品位置；第19題依初次見面前文補出回應。"),
    "kc114g8": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/2-%E8%8B%B1%E6%96%87_3.pdf", "高雄市立國昌國中114學年度第1學期八年級第1次定期評量英文", "114-1", "高雄市立國昌國民中學", "八年級英文評量原卷；第11題依飢餓情境提出用餐行動，第14題由回答反推原因問句，第15題處理電話中對方不在的請求。"),
    "nh109g7": ("https://www.nhjh.tp.edu.tw/30/2133/news/19/2021-7/2021-7-30-9-57-24-nf1.pdf", "臺北市立內湖國中109學年度第2學期七年級第1次段考英文", "109-2", "臺北市立內湖國民中學", "七年級英文段考原卷；第1頁第7題聽取對話並判斷頻率時間細節，第2頁第20題依顧客回應辨認點餐問題，第2頁第30題以 How come 追問原因。"),
    "nh109g8": ("https://www.nhjh.tp.edu.tw/30/2133/news/19/2021-7/2021-7-30-10-16-24-nf1.pdf", "臺北市立內湖國中109學年度第2學期八年級第1次段考英文", "109-2", "臺北市立內湖國民中學", "八年級英文段考原卷；第1頁第20題根據颱風警告選擇較安全的替代行動，第2頁第34至35題從活動時刻表整合日期、活動與人數條件。"),
    "nh111g8": ("https://www.nhjh.tp.edu.tw/uploads/1675416243642o6V5uNiI.pdf", "臺北市立內湖國中111學年度第1學期八年級第2次段考英文", "111-1", "臺北市立內湖國民中學", "八年級英文段考原卷；第2頁第39題依步驟排列土耳其咖啡製作程序的正確先後。"),
    "nh113g8": ("https://www.nhjh.tp.edu.tw/uploads/1753840039444z3K5m38Y.pdf", "臺北市立內湖國中113學年度第2學期八年級第1次段考英文", "113-2", "臺北市立內湖國民中學", "八年級英文段考原卷；第2頁第21題依前後發言辨認同意立場，並以理由句支持判斷。"),
    "kc112g9": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91_5.pdf", "高雄市立國昌國中112學年度第2學期三年級第2次段考英文", "112-2", "高雄市立國昌國民中學", "九年級英文段考原卷；第4頁第35題詢問代名詞 It 所指對象，需回看前段資訊。"),
    "kc111g8": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf", "高雄市立國昌國中111學年度第1學期八年級第3次段考英文", "111-1", "高雄市立國昌國民中學", "八年級英文段考原卷；第3頁第31題整合即時路況與路線資訊，選擇合適行程。"),
}

ITEMS = [
    {
        "prompt": "Leo: The 6:10 bus left before I reached the stop. I texted Mom, and she can meet me at the museum entrance in twenty minutes.\nNina: At least you have a plan.\nWhat is the main point of the exchange?",
        "options": ["Leo plans to study at the museum after taking the bus.", "Leo missed his bus and arranged for his mother to pick him up.", "Nina will take the next bus with Leo.", "Leo's mother has been waiting at the bus stop since 6:10."], "answer": "B",
        "explanation": "正確答案 B。先發生的是錯過公車，接著 Leo 聯絡媽媽並約好接送地點與時間；主旨要涵蓋問題及後續安排。",
        "strategy": "用「事件—反應—結果」串起對話，不讓單一地點或時間詞取代整段重點。",
        "steps": ["把 Leo 的話拆成先後兩件事：公車已離站；他傳訊息聯絡媽媽。", "辨認後一句的結果：媽媽二十分鐘後到博物館入口接他。", "用一句話同時保留遇到的問題和採取的安排，才算概括整段。", "B 同時包含 missed the bus 與 arranged pickup；A、C、D 各自添加原文沒有的計畫或人物行動。", "回讀 Nina 的 At least you have a plan，確認她回應的是接送安排，而非博物館活動。"],
        "refs": [("kc108g9", "第29題：依角色對話與事件結果推論寓言要傳達的重點", "參照整合對話行動及結果歸納文本核心訊息的題型；本題改為日常接送情境。")],
    },
    {
        "prompt": "Mia: The printmaking workshop starts later than we first thought.\nRay: The new note says 3:40 p.m. in Art Room 204. Let’s meet by the stairs at 3:30.\nWhen and where will they attend the workshop?",
        "options": ["At 3:30 p.m. by the stairs.", "At 4:30 p.m. in Art Room 204.", "At 3:40 p.m. by the stairs.", "At 3:40 p.m. in Art Room 204."], "answer": "D",
        "explanation": "正確答案 D。3:30 是兩人約好碰面的時間與地點；工作坊本身則在 3:40、Art Room 204 舉行，題目問的是參加活動的資訊。",
        "strategy": "分清「碰面安排」和「活動安排」，再各自擷取題目要求的時間、地點欄位。",
        "steps": ["圈出問句中的 When and where，確認需要活動時間和活動地點。", "Ray 先報告工作坊的新資訊：3:40 p.m.、Art Room 204。", "下一句 Let’s meet 指的是參加者彼此碰面的安排，不是工作坊舉辦地點。", "把兩個資訊來源分開後，選 D；A 和 C 把碰面地點當成活動地點。", "逐欄核對 3:40 與 Art Room 204 都取自新公告，而非兩人提早碰面的句子。"],
        "refs": [("nh109g7", "第1頁第7題：聽取對話後從選項辨認頻率／時間細節", "參照根據口語線索擷取時間資訊的聽力題型。"), ("kc114g7", "第3題：由 Where 問句與對話選項辨認物品位置", "參照把位置問句對應到地點資訊的細節定位方式。")],
    },
    {
        "prompt": "A: Could you share the recording from our science experiment? I want to compare the two sound readings.\nB: Sure. I’ll upload the audio file to our class folder after dinner.\nWhat is A asking B to provide?",
        "options": ["A copy of the experiment recording.", "A printed chart of the dinner menu.", "A new science classroom.", "A second experiment with louder sounds."], "answer": "A",
        "explanation": "正確答案 A。Could you share... 明確提出分享科學實驗錄音的請求；後句的 audio file 也確認了所指物品。",
        "strategy": "抓住請求動詞及其受詞，再用對方承諾的回應核實請求內容。",
        "steps": ["先找出 A 的請求句型 Could you share...，判斷 A 要求 B 提供某項資料。", "沿著 share 往後讀，受詞是 the recording from our science experiment。", "B 回答會上傳 audio file，與錄音檔相互印證。", "A 正確概括請求；其他選項把錄音、圖表、地點或另做實驗混為一談。", "用 compare the two sound readings 檢查目的：需要的是錄音，不是餐點或教室。"],
        "refs": [("kc114g8", "第15題：電話交談中處理找不到受話者並判斷可留下訊息的請求", "參照從對話辨認請求內容及後續處理方式。"), ("nh109g7", "第2頁第20題：依顧客點餐句回推服務人員提出的問題", "參照利用相鄰話輪核實對話所談的具體事項。")],
    },
    {
        "prompt": "A: We have permission to use the school garden, but we still need a room for the seed workshop.\nB: First, let’s compare the two rooms the office offered.\nA: Once we choose one, what should we do next?\nB: Ask the secretary to reserve it; after she confirms, we can message the group.\nWhat comes immediately after choosing a room?",
        "options": ["Message the group before asking anyone.", "Start planting seeds in the garden.", "Ask the secretary to reserve the room.", "Compare the rooms again after the workshop."], "answer": "C",
        "explanation": "正確答案 C。對話用 once 表示選好房間後，下一步是請秘書預約；只有收到確認後才通知群組。",
        "strategy": "把先後詞轉成時間線，題目問 immediately after 時只取緊接的一步。",
        "steps": ["先找時間線標記 First，確認目前在比較兩間教室。", "Once we choose one 表示選定房間是下一個前置事件。", "追蹤 B 的 after she confirms：預約確認之前，需先請秘書保留房間。", "因此選 C；通知群組在確認之後，種植和重新比較都不在緊接步驟。", "按原順序復述：比較→選定→請秘書預約→收到確認→通知群組。"],
        "refs": [("nh111g8", "第39題：依操作說明排列咖啡製作步驟的先後", "直接參照程序順序與連接語所測的排序能力；本題改為校園活動籌備。")],
    },
    {
        "prompt": "A: I was nervous about the robotics demo, but the team explained each step clearly.\nB: Same here. Once they showed how the sensor changed the robot’s direction, the whole project made sense.\nWhat does B think about the explanation?",
        "options": ["It helped B understand how the project works.", "It made B decide to leave the team.", "It proved the sensor never changes direction.", "It was too difficult for B to follow."], "answer": "A",
        "explanation": "正確答案 A。B 說 the whole project made sense，表示看過感測器如何改變方向後，自己理解了專題運作。",
        "strategy": "辨認說話者的評價線索，再把評價連回它所描述的對象。",
        "steps": ["注意 B 先說 Same here，表示回應並承接 A 對展示說明的感受。", "定位評價語 made sense，判斷 B 認為內容變得清楚、可理解。", "前文 once they showed 指出理解發生的原因，是團隊展示感測器如何改變方向。", "A 對應這個理解結果；B、C、D 都和 made sense 的正向評價相反或無關。", "把 made sense 換回白話「理解專題怎麼運作」，確認答案沒有誇大成完全掌握所有細節。"],
        "refs": [("nh113g8", "第21題：由第二位說話者的附加理由判斷其對前一主張的同意立場", "參照讀取回應語與理由來推論說話者態度。")],
    },
    {
        "prompt": "A: The classroom projector stopped working, and the presentation begins in three minutes.\nB: Use Ms. Chen’s laptop with the large monitor in Room 8. I’ll carry the slides there while you tell the class to meet us.\nWhat solution does B propose?",
        "options": ["Cancel the presentation and wait for a new projector.", "Move the class to the library and buy a monitor.", "Use the laptop and Room 8 monitor, while B brings the slides.", "Ask the class to repair the broken projector."], "answer": "C",
        "explanation": "正確答案 C。B 提出以筆電接 Room 8 的大螢幕替代故障投影機，並主動搬運簡報；不是取消或修理設備。",
        "strategy": "把問題和提案分開記錄，再核對提案包含的設備、地點與分工。",
        "steps": ["先辨認問題是教室投影機故障，而且簡報很快開始。", "找出 B 的祈使句 Use...，這是提出的替代做法。", "記錄方案兩個核心條件：Ms. Chen 的筆電、Room 8 的大螢幕。", "再補上分工：B 搬投影片，A 通知全班集合；選項 C 完整涵蓋方案。", "排除等待新設備、購買螢幕或要求全班修理，因為對話沒有提出這些行動。"],
        "refs": [("nh109g8", "第1頁第20題：依安全警告選擇合適的替代行動", "參照面對問題後從回應中辨認可行解決行動。"), ("kc114g8", "第11題：從飢餓問題的對話回應辨認立即提議的處理方式", "參照由 Let's... 建議句讀取解決方案。")],
    },
    {
        "prompt": "A: I found a voice recorder inside a cracked plastic case.\nB: The case is damaged, so please place it on the repair desk. Don’t leave it in the equipment cabinet.\nWhat does the first ‘it’ in B’s reply refer to?",
        "options": ["The voice recorder.", "The repair desk.", "The equipment cabinet.", "The plastic case."], "answer": "D",
        "explanation": "正確答案 D。緊接在第一個 it 前的主題是 cracked plastic case，且 damaged 正是要送修的理由，所以請放到維修桌的是外殼。",
        "strategy": "追蹤代名詞時同時檢查最近的名詞、語意特徵與後續動作，不只靠距離猜。",
        "steps": ["標記第一個 it 的位置：B 說 The case is damaged, so please place it...。", "向前找候選名詞：voice recorder 與 plastic case 都是單數。", "利用 damaged 判斷哪個物件需要修理，線索指向外殼。", "後續 place it on the repair desk 也符合送修外殼；錄音機本身沒有被說明損壞。", "回代成 please place the plastic case on the repair desk，確認句意連貫且沒有和第二個 it 混淆。"],
        "refs": [("kc108g7", "第36題：依前文人物與物件內容判斷 it 的指涉", "直接參照以先行詞及上下文線索解析代名詞指涉。"), ("kc112g9", "第35題：回看前段交通系統說明，判斷代名詞 It 指稱何者", "參照先行詞與語意一致性並用的指代判讀。")],
    },
    {
        "prompt": "A: The notice is hard to read from the back row, and the projector remote is missing.\nB: I’ll enlarge the slide on my laptop and send it to the room screen before the talk begins.\nWhat is B trying to accomplish?",
        "options": ["Make the notice easier for the audience to see.", "Turn off the room screen before the talk.", "Find the missing remote without changing anything.", "Move the audience to the back row."], "answer": "A",
        "explanation": "正確答案 A。問題是後排看不清楚，B 要放大投影片並傳到大螢幕，目的就是讓觀眾看得清楚。",
        "strategy": "從前一句的困難推回後一句行動要改善什麼，辨認行動目的而非只重複動作。",
        "steps": ["先指出 A 描述的障礙：後排不容易看清公告。", "把 B 的動作串起來：在筆電放大投影片，再送到教室螢幕。", "問這兩個動作能解決哪個障礙，推論目標是改善可視性。", "選 A；B、C、D 不是所提動作的合理目的。", "檢查目的推論沒有超出線索：對話支持「看得更清楚」，沒有說 B 要修好遙控器。"],
        "refs": [("kc108g7", "第34題：依廣告內容判斷訊息的溝通目的", "參照從訊息內容推論說話者／作者目的的題型；本題改寫為簡短對話。"), ("kc114g8", "第11題：以 Let's stop to eat 回應飢餓情境並提出行動目的", "參照由對話建議推論要解決的需求。")],
    },
    {
        "prompt": "A: Wednesday is impossible because I have team practice. Thursday I work until six.\nB: I’m free Friday after club.\nA: Friday at 4:30 works. I’ll reserve the study room for then.\nWhat time did they finally agree to meet?",
        "options": ["Wednesday at 4:30.", "Thursday after six.", "Friday at 4:30.", "Friday before club."], "answer": "C",
        "explanation": "正確答案 C。前兩天都有衝突；雙方最後接受 Friday at 4:30，預約自習室的 then 回指這個時間。",
        "strategy": "先排除被拒絕的時段，再追蹤最後被接受並由行動確認的安排。",
        "steps": ["按對話順序列出選項：Wednesday 被 practice 排除，Thursday 要工作到六點。", "B 提出 Friday after club 作為可行時段。", "A 明確確認 Friday at 4:30 works，這是最後取得共識的具體時間。", "I’ll reserve...for then 的 then 回指剛確認的週五四點半。", "選 C，並排除只提過但被拒絕或未確認的其他時段。"],
        "refs": [("nh109g8", "第34至35題：整合活動日期、項目時間及團體人數條件作答", "參照將時程表細節合併成具體活動安排的資訊定位模式。")],
    },
    {
        "prompt": "A: The riverside path is open tomorrow, and the forecast says the morning will be clear.\nB: I packed water, sunscreen, and the folded trail map. We should leave before the afternoon heat.\nWhat are they most likely preparing to do?",
        "options": ["Take an outdoor walk or hike along the riverside.", "Stay inside all afternoon to study for a test.", "Go swimming tonight during heavy rain.", "Return a library book before school today."], "answer": "A",
        "explanation": "正確答案 A。開放的河岸步道、晴朗早晨、飲水、防曬、步道地圖及避開午後高溫，共同指向戶外步行活動。",
        "strategy": "把分散在兩個話輪的地點、天氣、裝備與時間限制合併，推論最符合全部線索的情境。",
        "steps": ["先收集地點線索：明天開放的是 riverside path，而不是室內場館。", "再整理天氣和時間：早上晴朗，午後會熱，因此打算提早出發。", "核對裝備用途：飲水、防曬用品和摺疊步道圖都適合戶外步行。", "A 最能同時解釋地點、裝備和時間；其他選項與晴天、步道或裝備不符。", "確認推論只到「沿河戶外步行／健行」，不額外猜測對話未提供的同行人數或確切目的地。"],
        "refs": [("kc111g8", "第31題：整合路況報告與地圖線索，選出適合的行進路線", "參照從路線、交通與情境資訊推論行動安排；本題改為河岸步行準備。"), ("nh109g8", "第34至35題：從活動日期、內容與附註推論參與安排", "參照綜合多個行程線索作情境判斷。")],
    },
]

def ref(key, locator, observed):
    url, title, year, _, _ = SOURCES[key]
    return {"url": url, "title": title, "year": year, "subject": "english", "locator": locator,
            "locatorLevel": "item", "observedPattern": observed, "reuseDecision": "pattern-only", "status": "recorded"}

def main():
    for i, item in enumerate(ITEMS, 1):
        path = ROOT / f"questions/english/question-english-performance-3-iv-7-{i}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["prompt"] = item["prompt"]
        data["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(item["options"])]
        data["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
        data["solutionStrategy"] = item["strategy"]
        data["solutionSteps"] = item["steps"]
        data["examPatternRefs"] = [ref(*x) for x in item["refs"]]
        data["provenance"]["sourceUrl"] = data["examPatternRefs"][0]["url"]
        data["provenance"]["sourceLocator"] = "依公立國中英文段考中對話主旨、時間地點、請求、順序、態度、建議、指代與行動推論的公開命題模式獨立改寫；逐題原卷題號列於 examPatternRefs。"
        data["provenance"]["authoringNote"] = "本題情境、對話、選項、答案與繁中解析均依 3-Ⅳ-7 能力獨立重寫；公開試題僅作可追溯 pattern-only 參照，不複製原文或選項。完整內容與版權 QA 未完成，維持 draft。"
        data["reviewStatus"] = "draft"
        data["updatedAt"] = TODAY
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(path.read_text(encoding="utf-8"))
    known = {x["url"] for x in catalog["sources"]}
    for url, title, year, institution, material in SOURCES.values():
        if url not in known:
            catalog["sources"].append({
                "institution": institution, "url": url, "subjects": ["english"],
                "availableMaterial": f"{title}；{material}",
                "researchUse": "校方公開英文段考僅作短對話理解、資訊整合、推論或語篇任務模式研究；本專案不複製原題、選項、圖表或答案。",
                "licenseBoundary": "公開可查閱不代表取得重製授權；保留校方原卷 URL 與逐題 locator，題幹、選項及解說由本專案獨立撰寫。",
                "sourceLocator": material,
            })
            known.add(url)
        if url not in catalog["questionSourceUrls"]:
            catalog["questionSourceUrls"].append(url)
    catalog["updatedAt"] = TODAY
    path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Re-authored ten original 3-IV-7 questions with item-level public-school patterns; all remain draft.")

if __name__ == "__main__":
    main()
