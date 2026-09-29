import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"

S = {
    "xiaogang": {"url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/21%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F/3%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/109-1-3%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "title": "高雄市立小港國民中學109學年度第一學期第三次段考二年級英文科試題", "year": "109-1"},
    "dawan": {"url": "https://www.dwm.kh.edu.tw/upload/344/104_64186/111%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C%28%E4%BD%B3%E9%9F%B3%29.pdf", "title": "高雄市立大灣國民中學111學年度第一學期第三次段考三年級英文科試題", "year": "111-1"},
    "guo110": {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E9%AB%98%E9%9B%84%E5%B8%82%E5%9C%8B%E6%98%8C%E5%9C%8B%E4%B8%AD%E4%BA%8C%E4%B8%8B%E8%8B%B1%E6%96%87%E8%81%BD%E5%8A%9B%E8%A7%A3%E6%9E%90%E5%8D%B7.pdf", "title": "高雄市立國昌國中110學年度第二學期二年級第一次段考英文聽力解析卷", "year": "110-2"},
    "guo113": {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%81%BD_10.pdf", "title": "高雄市立國昌國中113學年度第一學期第二次段考二年級英語科聽力試題", "year": "113-1"},
    "wuling": {"url": "https://www.whjhs.tyc.edu.tw/wp-content/uploads/doc/wh212/114%E5%AD%B8%E5%B9%B4%E8%8B%B1%E8%AA%9E9-3%E6%95%99%E8%82%B2%E6%9C%83%E8%80%83_%E8%81%BD%E5%8A%9B%E8%A7%A3%E6%9E%90.pdf", "title": "桃園市立武陵高中114學年國中教育會考模擬測驗英文聽力解析", "year": "114"},
}

ITEMS = {
    "x11": ("xiaogang", "第三部分言談理解第11題", "對話中第一個購物選擇因預算不合而改成另一件商品，測聽者追蹤替代方案。"),
    "x12": ("xiaogang", "第三部分言談理解第12題", "對話者接受改換購物地點的建議，測聽者辨認最後採用的地點。"),
    "x14": ("xiaogang", "第三部分言談理解第14題", "訂位對話明確提供人數、星期、時間與姓名，測聽者擷取多個約定細節。"),
    "x15": ("xiaogang", "第三部分言談理解第15題", "親子對話包含催促、原因與下一步行動，題目詢問說話者意圖。"),
    "d8": ("dawan", "第三部分言談理解第8題", "對話解釋沙發移出客廳的原因與所在位置，測聽者追蹤對話中的人物和地點資訊。"),
    "d10": ("dawan", "第三部分言談理解第10題", "選課對話包含先後年度的安排與最喜歡的科目，測聽者整合時間順序和偏好線索。"),
    "g11": ("guo110", "第三部分言談理解第11題", "遺失檔案的簡短問答以抽屜位置回應問題，支持問題—線索—處置資訊辨認。"),
    "g13": ("guo110", "第三部分言談理解第13題", "從成績比較的對話推論人物可能得到的結果，測聽者整合比較線索。"),
    "g17": ("guo110", "第三部分言談理解第17題", "廣告短講詢問說話者的目的，直接對應聽者辨認談話主旨／意圖。"),
    "g21": ("guo110", "第四部分聽力題組第21題", "對話比較外套與大衣的保暖及長度條件，測聽者從多項細節選出最後決定。"),
    "g22": ("guo110", "第四部分聽力題組第22題", "承接購衣對話詢問選擇理由，要求把前後條件連成因果。"),
    "n16": ("guo113", "第2頁第16題", "選項詢問對話人物為何感到自豪，直接測量語氣與態度線索。"),
    "n23": ("guo113", "第2頁第23題", "言談理解以三個相近時刻作選項，測聽者精確記錄時間資訊。"),
    "w12": ("wuling", "第1頁第12題", "模擬聽力問對話人物接下來先做什麼，測聽者依序整理建議和下一步行動。"),
    "w21": ("wuling", "第4頁第21題", "公告說明午餐延遲、品項售罄及需更換的選擇，適合研究多條件摘要筆記。"),
}

def refs(item_ids):
    result = []
    for item_id in item_ids:
        source_id, locator, pattern = ITEMS[item_id]
        source = S[source_id]
        result.append({"url": source["url"], "title": source["title"], "year": source["year"], "subject": "english", "locator": locator,
                       "observedPattern": pattern + " 僅借鑑可定位的題型能力；本題情境、對話、選項及作答內容均重新創作，未摘錄原卷。",
                       "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item"})
    return result

DATA = [
    {"prompt": "Mia: I have to give my science presentation on Friday, and I keep losing my place. Ben: We could rehearse together after school tomorrow. Mia: That would help a lot. What is the main purpose of their conversation?", "choices": ["Buy materials for a science project", "Arrange a rehearsal for Mia's presentation", "Move Friday's presentation to another day", "Choose a topic for Ben's report"], "key": "B", "explanation": "Mia提到週五要報告且練習時會忘詞；Ben提出隔天放學一起彩排，Mia接受。對話核心是安排報告練習，不是改日期或買材料。", "strategy": "聽主旨時，把困難、提議和對方回應連起來；不要只抓到話題名詞就作答。", "steps": ["先圈出 Mia 的問題：報告時會忘記講到哪裡，這說明她需要練習。", "找出 Ben 提出的具體行動：tomorrow after school 一起 rehearse。", "注意 Mia 回答 That would help a lot，表示接受彩排安排。", "檢查選項是否把『練習報告』誤成改期、選題或購物。", "記成「週五科學報告；週四放學一起彩排」，保留目的與時間。"], "refs": ["g17", "x15", "d10"]},
    {"prompt": "Nora: The library closes early today. Should we still meet there at 3:30? Leo: Let's use the music room instead, at 4:00. Nora: Perfect. Where and when is their final meeting plan?", "choices": ["Library at 3:30", "Music room at 3:30", "Music room at 4:00", "Library at 4:00"], "key": "C", "explanation": "Leo 用 instead 改了地點，也把時間從 3:30 改為 4:00；Nora 說 Perfect，代表採用新方案。筆記要記最後版本。", "strategy": "遇到行程修正，劃掉舊方案，只保留最後被接受的時間與地點。", "steps": ["把第一個提案 library、3:30 暫記為舊方案。", "聽到 instead 時，標記後面的 music room 是地點修正。", "把 Leo 新說的 4:00 記為更新後時間。", "用 Nora 的 Perfect 確認她接受新計畫，而非仍選圖書館。", "整理成一行：music room—4:00；不要把新舊時間混在一起。"], "refs": ["x14", "d8", "n23"]},
    {"prompt": "Teacher: For tomorrow's map task, bring a ruler and colored pencils. You may leave the glue at home; we will use tape in class. What should a student write under 'Bring'?", "choices": ["Glue and tape", "Ruler only", "Colored pencils and glue", "Ruler and colored pencils"], "key": "D", "explanation": "老師明確要求帶 ruler 和 colored pencils，並說 glue 不用帶；tape 由教室提供，不列入學生的攜帶物。", "strategy": "把『要帶』和『不用帶／現場提供』分成兩欄，避免否定句把物品誤記進去。", "steps": ["聽到 Bring 後，先記兩項明確要求：ruler、colored pencils。", "在 glue 旁記 not needed，因為老師說可留在家裡。", "分辨 tape 是課堂會用，但由教室提供，不是要學生攜帶。", "逐個核對選項有沒有混入被排除或由別人準備的物品。", "筆記寫成「帶：尺、彩色筆；免帶：膠水」，只留下可執行資訊。"], "refs": ["x14", "g21", "d10"]},
    {"prompt": "A: I planned to catch the 5:10 bus to the museum. B: The station just announced a delay. The next bus leaves at 5:30, and it still goes to the museum. What should be changed in the note?", "choices": ["Departure time: 5:10 → 5:30", "Destination: museum → library", "Transport: bus → train", "The trip is canceled"], "key": "A", "explanation": "公告只改了發車時間，目的地仍是博物館、交通方式仍是公車，也沒有取消行程。筆記只需更新 5:10 為 5:30。", "strategy": "逐項比較修正前後的欄位，僅改變被明確更新的那一格。", "steps": ["將原筆記拆成交通工具、時間、目的地三欄：bus／5:10／museum。", "找出新訊息指向哪一欄；句子說 next bus leaves at 5:30。", "確認仍去 museum，且仍搭 bus，排除其他欄位改變。", "聽 station announced a delay，判斷是延後而不是取消。", "只把時間改寫成 5:30，舊的 5:10 不再保留為目前計畫。"], "refs": ["n23", "x14", "d8"]},
    {"prompt": "Clerk: First, check that your name and class are correct. Then sign the form. Finally, put it in the blue tray. What is the second action?", "choices": ["Put the form in the blue tray", "Sign the form", "Check the name and class", "Take the form home"], "key": "B", "explanation": "First 對應核對姓名班級，Then 指第二步簽名，Finally 才是放入藍色托盤；不能把最後一步提前。", "strategy": "先把順序詞轉成 1、2、3，再對照題目問第幾步。", "steps": ["看到 First，先標 1：核對姓名和班級。", "看到 Then，標 2：在表格上簽名。", "看到 Finally，標 3：把表格放進藍色托盤。", "題目問 second action，因此取編號 2，不選最終提交動作。", "複述流程「檢查→簽名→投入托盤」，確認簽名位於中間。"], "refs": ["w12", "x15", "d10"]},
    {"prompt": "Evan: I can't find the folder for our art display. I last had it beside the classroom computer. June: Let's check that table before asking the teacher. Which note best captures the problem and next step?", "choices": ["Computer is broken → ask for a new one", "Art display is canceled → go home", "Teacher lost the folder → search the hallway", "Folder missing → check beside the classroom computer"], "key": "D", "explanation": "Evan 找不到資料夾，最後一次在教室電腦旁看見；June 建議先回那張桌子找，再決定是否問老師。", "strategy": "把問題、最後已知位置和下一個行動分開記，避免把猜測寫成已知事實。", "steps": ["先記確定的問題：art display folder 不見了。", "提取 last had it 的線索，位置是 classroom computer 旁。", "辨認 June 的下一步是先檢查那張桌子，而非立刻認定誰弄丟。", "排除把可能原因（電腦壞掉、老師弄丟）當作對話事實的選項。", "用箭號記錄「資料夾遺失→先查教室電腦旁桌面」。"], "refs": ["g11", "w12", "d8"]},
    {"prompt": "After the group finishes early, Kai says, 'Great—we have time to check the labels before we pack everything.' What attitude is best supported by his words?", "choices": ["Angry that the group finished", "Worried that the work is impossible", "Relieved and still careful", "Indifferent to the result"], "key": "C", "explanation": "Great 顯示 Kai 對提早完成感到正面；他接著主動檢查標籤，表示仍在意成果是否正確，因此是放心且仔細。", "strategy": "用語氣詞判斷情緒方向，再用後續行動確認態度，不單靠一個形容詞猜心情。", "steps": ["先看 Great 的正向語氣，排除生氣或漠不關心。", "把 have time 和提早完成連起來，推知他不再受時間壓迫。", "注意 check the labels 是仔細確認，不代表工作做不完。", "將情緒線索與行動線索合併：正面、放心，但仍謹慎。", "選擇同時符合兩組證據的態度，不把 relief 誤讀為粗心。"], "refs": ["n16", "g13", "x15"]},
    {"prompt": "Announcement: The science club will visit the aquarium on Saturday. Members meet at the east school gate at 8:15 a.m.; bring your student card. Which is the best compact note?", "choices": ["Science club—Aquarium, Sat.; east gate 8:15 a.m.; student card", "Aquarium—Sunday night; meet at west gate; bring cash", "Science club—school gate; time unknown; no card needed", "Saturday—meet at 8:15 p.m.; bring a library book"], "key": "A", "explanation": "完整筆記保留活動、日期、集合位置、時間和必帶證件；縮寫可以，但不能改成相反或未提供的資訊。", "strategy": "摘要筆記要用欄位檢查覆蓋率：活動、日期、地點、時間、物品逐一對照。", "steps": ["先列出五個欄位：誰的活動、做什麼、哪一天、在哪裡幾點、帶什麼。", "從公告填入 science club、aquarium、Saturday、east gate、8:15 a.m.、student card。", "把同一集合資訊合併成短語，保留 east 與 a.m. 這些會改變意思的詞。", "逐欄檢查選項，排除星期、方向、上午下午或物品被偷換者。", "確認 A 五項都齊全且沒有增加車資、集合後活動等未說內容。"], "refs": ["w21", "x14", "n23"]},
    {"prompt": "M: I wanted to join the cooking class, but it is full. The photography class still has seats and begins next week. W: Then I'll sign up for photography. What is the final plan?", "choices": ["Join cooking today", "Wait until both classes reopen", "Cancel every activity", "Join photography next week"], "key": "D", "explanation": "but 指出烹飪課額滿的轉折；女性明確接受仍有名額的攝影課，時間是下週。筆記應以最後決定為準。", "strategy": "辨認『原計畫受阻→替代方案→接受與否』三段，不把已放棄的第一方案記成決定。", "steps": ["把 cooking class 標為原本想參加的方案。", "聽到 full，記下原方案不可行的原因。", "第二位說 photography still has seats，指出可行替代方案。", "用 I'll sign up 確認她已選攝影課，next week 是開始時間。", "筆記保留「下週報名／參加攝影課」，不要誤記烹飪課或全部取消。"], "refs": ["x11", "x12", "w21"]},
    {"prompt": "M: Our project meeting is for the poster draft. The library room is unavailable, so we have moved to Room 302 at 4:00. Please bring the outline. W: Got it. Which note preserves all confirmed details?", "choices": ["Room 302; bring outline; meeting purpose and time omitted", "Poster draft meeting—Room 302, 4:00; bring outline", "Library room, 4:00; bring the finished poster", "Poster meeting canceled; outline not needed"], "key": "B", "explanation": "對話確認四項：會議目的是討論海報草稿、地點改成 302 室、時間四點、攜帶大綱。library room 已不可用，不應留作最後地點。", "strategy": "整合題逐欄核對『目的、最終地點、時間、攜帶物』，也要排除被修正的舊資訊。", "steps": ["從第一句抽出會議目的：poster draft，不要寫成完成品展示。", "聽到 library room unavailable，將圖書館標為失效地點。", "記下 moved to Room 302 與 4:00，這是最後確認的場所和時間。", "從 Please bring the outline 記錄需帶大綱，不能擴大成 finished poster。", "回頭核對四欄都有保留且沒有取消會議等對話未說的結論。"], "refs": ["x14", "d10", "w21"]},
]

positions = ["B", "C", "D", "A", "B", "D", "C", "A", "D", "B"]
for index, (row, key) in enumerate(zip(DATA, positions), 1):
    correct = row["choices"][["A", "B", "C", "D"].index(row["key"])]
    distractors = [v for v in row["choices"] if v != correct]
    ordered = [None] * 4
    ordered[ord(key) - 65] = correct
    it = iter(distractors)
    for slot in range(4):
        if ordered[slot] is None:
            ordered[slot] = next(it)
    options = [{"id": chr(65 + slot), "text": text} for slot, text in enumerate(ordered)]
    exam_refs = []
    for item_id in row["refs"]:
        source_id, locator, pattern = ITEMS[item_id]
        source = S[source_id]
        exam_refs.append({"url": source["url"], "title": source["title"], "year": source["year"], "subject": "english", "locator": locator,
                          "observedPattern": pattern + " 僅參考可定位的公校題型與聆聽能力，不採用原卷內容；本題對話、選項與答案均為原創。",
                          "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item"})
    item = {"id": f"question-english-performance-5-iv-7-{index}", "subject": "english", "type": "single-choice", "prompt": row["prompt"], "options": options,
            "knowledgeIds": ["kg-english-performance-5-iv-7"], "difficulty": "medium", "answer": {"value": key, "explanation": row["explanation"]},
            "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": exam_refs[0]["url"], "sourceLocator": "; ".join(f"{r['title']} {r['locator']}" for r in exam_refs) + "；僅 pattern-only 研究，未複製原卷文字或音檔。",
                            "authoringNote": "對話、選項、答案、筆記與詳解皆為原創；僅以公立學校公開試題定位聆聽題型，內容仍待全庫發布 gate，維持 draft。"},
            "reviewStatus": "draft", "updatedAt": "2026-09-26", "lessonId": "lesson-english-performance-5-iv-7", "examPatternRefs": exam_refs,
            "solutionStrategy": row["strategy"], "solutionSteps": row["steps"]}
    (OUT / f"{item['id']}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
