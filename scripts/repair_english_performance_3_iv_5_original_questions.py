"""Re-author unit 3-IV-5 response questions and attach verified public-exam patterns."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-26"
SOURCES = {
    "guochang": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87_3.pdf",
        "title": "高雄市立國昌國中114學年度第1學期七年級第1次段考英文",
        "year": "114-1",
        "institution": "高雄市立國昌國民中學",
        "availableMaterial": "七年級英文段考原卷；第2頁第19題為初次見面對話回應，第24題為對人物介紹後的合宜回應。",
    },
    "neihu7": {
        "url": "https://www.nhjh.tp.edu.tw/30/2133/news/19/2021-7/2021-7-30-9-57-24-nf1.pdf",
        "title": "臺北市立內湖國中109學年度第2學期七年級第1次段考英文",
        "year": "109-2",
        "institution": "臺北市立內湖國民中學",
        "availableMaterial": "七年級英文段考原卷；第1頁第6題為基本問答回應，第2頁第20題為服務對話，第2頁第30題為追問原因。",
    },
    "neihu8": {
        "url": "https://www.nhjh.tp.edu.tw/30/2133/news/19/2021-7/2021-7-30-10-16-24-nf1.pdf",
        "title": "臺北市立內湖國中109學年度第2學期八年級第1次段考英文",
        "year": "109-2",
        "institution": "臺北市立內湖國民中學",
        "availableMaterial": "八年級英文段考原卷；第1頁第5題為邀約情境回應，第2頁第20題為天候警示的安全回應、第23題為道謝後的回應、第29題為延後點餐的請求。",
    },
    "dashe": {
        "url": "https://www.dam.kh.edu.tw/upload/68/101_28414/114-1%E4%B9%9D%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf",
        "title": "高雄市立大社國中114學年度第1學期九年級第1次段考英文",
        "year": "114-1",
        "institution": "高雄市立大社國民中學",
        "availableMaterial": "九年級英文段考題目與解答；第4頁第17題為受邀後以個人理由婉拒的對話。",
    },
    "yancheng": {
        "url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立鹽埕國中114學年度第2學期九年級第1次段考英文",
        "year": "114-2",
        "institution": "高雄市立鹽埕國民中學",
        "availableMaterial": "九年級英文段考公開題卷；第2頁第11題服務對話含道歉與補救回應，第2頁第13題以對話辨認共同偏好。",
    },
}

ITEMS = [
    {
        "prompt": "A new classmate says, ‘Good morning. I’m Mia.’ Which reply both greets Mia and responds to her introduction?",
        "options": ["Good morning, Mia. I’m Alex.", "Good night, Mia. See you yesterday.", "I’m fine, thank you.", "The morning bus is late."], "answer": "A",
        "explanation": "正確答案 A。對方先問候並自我介紹，A 同時回應早安並介紹自己；C 是回答 How are you?，沒有回應名字。",
        "strategy": "把對方話語拆成兩個功能：問候與自我介紹；回覆也要接住兩件事。",
        "steps": ["先標出 Mia 說了兩件事：Good morning 是問候，I’m Mia 是自我介紹。", "回應第一部分時，使用相同時段的問候語。", "再檢查是否自然提供自己的名字，讓初次見面的交換完整。", "A 兩個功能都符合；C 雖像日常回答，卻是在回答健康狀況。", "連讀對話確認稱呼、時段與交談目的都一致。"],
        "refs": [("guochang", "第2頁第19題：初次見面對話中，依前句完成自然的自我介紹回應", "對話回應需承接問候與初次見面的社交功能。"), ("neihu7", "第1頁第6題：聽取生活陳述後選擇最合宜的基本問答回應", "由語境功能而非孤立字詞選擇回應；本題另加入姓名介紹。")],
    },
    {
        "prompt": "Your classmate lends you an umbrella during a sudden shower and says, ‘Here you are.’ What is the most natural reply?",
        "options": ["You should take it back now.", "I’m sorry you are wet.", "Thanks—that’s very kind of you.", "Would you like me to borrow it?"], "answer": "C",
        "explanation": "正確答案 C。對方正在幫忙把傘借給你，先表達感謝最切合情境；D 把借出與借入的角色弄反。",
        "strategy": "先辨認對方做了什麼，再選擇能回應這項善意的話。",
        "steps": ["確認 Here you are 是把物品交給對方，不是提出新邀請。", "從前後情境判斷：同學主動借傘，目的是幫你避雨。", "回應應承認幫助並表達謝意，不必要求對方立刻收回。", "C 感謝同學的好意；D 則把借傘方向說反。", "把 C 接在同學的話後朗讀，確認人際角色及語氣合理。"],
        "refs": [("neihu8", "第2頁第23題：對方表達感謝後，選出符合社交情境的回應", "參照道謝／回應的語用配對，不沿用原題措辭。"), ("guochang", "第2頁第24題：聽完人物介紹後選擇自然的對話收束回應", "參照生活對話中依前文選擇回應的題型。"), ("yancheng", "第2頁第11題：服務對話中顧客提出問題後，服務人員道歉並提出補救", "參照承接他人行動、維持禮貌互動的對話功能。")],
    },
    {
        "prompt": "You accidentally spill water on a classmate’s worksheet. They say, ‘My notes are all wet.’ What should you say first?",
        "options": ["It was only a little water.", "I’m sorry. Let me help dry it and replace the page.", "You should have moved your notes.", "Congratulations on your new worksheet."], "answer": "B",
        "explanation": "正確答案 B。先承認自己造成的不便並道歉，再提出具體補救；A 淡化對方損失，C 則推卸責任。",
        "strategy": "遇到自己造成的困擾，依序處理責任、道歉與補救，不急著辯解。",
        "steps": ["辨認事件原因：水是自己不小心打翻的。", "理解同學指出的是實際損失——筆記被弄濕。", "合宜的第一反應應承認影響並道歉，而非爭辯嚴重程度。", "B 再提出擦乾及補印的可行補救，完整回應問題。", "檢查語氣是否尊重對方，並確認提出的補救確實針對濕掉的講義。"],
        "refs": [("yancheng", "第2頁第11題：服務人員對顧客的不滿先致歉，再提供更換餐點的補救", "參照承認造成不便並提出補救的對話功能；本題改為校園情境。"), ("neihu7", "第2頁第30題：聽到對方取消活動後，以追問理解原因", "參照先回應他人處境、再取得資訊的互動順序。")],
    },
    {
        "prompt": "A friend invites you to a movie tonight, but you already promised to help your younger brother study. Which reply is polite and clear?",
        "options": ["Thanks for inviting me, but I can’t tonight—I promised to help my brother.", "No. Movies are a waste of time.", "Maybe I will go, but don’t wait for me.", "I’d love to go, so I’ll cancel my promise."], "answer": "A",
        "explanation": "正確答案 A。先感謝邀請，再明確婉拒並說明既有承諾；這既不貶低對方的邀請，也不留下含糊期待。",
        "strategy": "婉拒時兼顧關係與資訊：感謝邀請、清楚答覆、提供簡短真實理由。",
        "steps": ["確認對方提出的是今晚的邀約，答案需要明確說能否參加。", "注意自己已有承諾，不能用不確定的 Maybe 讓朋友空等。", "選擇先表示感謝、再說明今晚無法赴約的回覆。", "A 說明了無法參加的理由，而且沒有批評電影或邀請者。", "檢查回答是否同時傳達拒絕、理由與尊重。"],
        "refs": [("dashe", "第17題：受邀參加聚會者以個人偏好婉拒", "參照邀請—婉拒的語用關係；題幹、理由及句子均另行創作。"), ("neihu8", "第1頁第5題：依邀約前文選擇適切的接受回應", "參照邀約對話需與說話者立場相符的能力模式。")],
    },
    {
        "prompt": "Your roommate says, ‘Could you turn the music down? I’m trying to read.’ You think it is not very loud. What is the most considerate reply?",
        "options": ["You’re too sensitive; the music is fine.", "I’ll turn it up after you leave.", "The book should listen to the music.", "Sure—I’ll lower it. Tell me if you still need it quieter."], "answer": "D",
        "explanation": "正確答案 D。室友已說明音量影響閱讀；先配合降低音量，再讓對方回報是否改善，比爭論自己覺得多大聲更尊重需求。",
        "strategy": "對方提出可執行的請求時，先回應需求；自己的感受不能取代對方正在受影響的事實。",
        "steps": ["找出請求：把音樂調小；理由是室友正在閱讀。", "分清自己的主觀感受與對方明確提出的干擾。", "挑選能立即降低干擾且保持合作的回覆。", "D 先承諾調低，再用簡短追問確認是否足夠。", "排除指責或故意反向操作的選項，檢查回應是否解決閱讀受干擾。"],
        "refs": [("neihu8", "第2頁第29題：顧客尚未準備好時，禮貌請服務人員稍後再來", "參照生活請求中承接對方需求、調整下一步的回應模式。"), ("neihu7", "第1頁第6題：依聽到的情境選擇適切基本回應", "參照從情境判斷回應，而非只看表面同意或否定。")],
    },
    {
        "prompt": "A station announcement is unclear, and you are not sure whether your train leaves from platform 3 or 13. What should you ask a staff member?",
        "options": ["Could you please repeat the platform number? I heard either 3 or 13.", "I’ll choose a platform at random.", "Why are trains always announcements?", "The station is probably platform 3."], "answer": "A",
        "explanation": "正確答案 A。兩個月台號只差一個音節，猜錯可能搭錯車；指出聽到的兩種可能並請對方重複，才能取得關鍵資訊。",
        "strategy": "資訊不足且猜錯有代價時，具體指出不確定處並禮貌請對方重述。",
        "steps": ["圈出目前唯一關鍵的不確定資訊：月台號是 3 還是 13。", "評估猜測後果：選錯月台可能錯過列車。", "設計澄清句，明確點出聽不清的欄位，而不是籠統說不懂。", "A 說明兩個候選數字並請工作人員重複，能直接排除歧義。", "確認取得答案前不先採取不可逆行動，例如隨意上車。"],
        "refs": [("neihu7", "第2頁第30題：聽到無法參加的消息後追問 How come 以釐清原因", "參照以追問消除資訊缺口的對話功能；本題改為交通安全資訊。"), ("guochang", "第2頁第19題：依對話前句理解社交資訊並完成回應", "參照必須根據對話線索回應的命題方式。")],
    },
    {
        "prompt": "A teammate asks, ‘Would you rather present the map or explain the schedule?’ You are comfortable doing either, but you prefer the map. What should you say?",
        "options": ["I don’t know what a schedule is.", "Either is fine, but I’d prefer to present the map.", "The map presented me yesterday.", "No, I don’t like questions."], "answer": "B",
        "explanation": "正確答案 B。問題詢問兩項工作的偏好；B 先表示兩者都可，再清楚指出較想負責地圖，沒有把偏好說成拒絕。",
        "strategy": "辨認選擇題問的是偏好而非能力，再用讓步加偏好說清楚立場。",
        "steps": ["確認對方提供兩項任務：介紹地圖或說明時程。", "分辨自己的狀態：兩件都能做，但其中一件較喜歡。", "選出既保留彈性、又清楚呈現首選的句子。", "B 的 Either is fine 表示可接受兩者，後半句指出地圖是偏好。", "回看選項，排除把偏好誤答成不懂、過去事件或拒絕對話的句子。"],
        "refs": [("yancheng", "第2頁第13題：由對話判斷兩人是否共享對某事物的偏好", "參照從對話內容辨認偏好立場的能力模式；本題改為任務選擇。"), ("neihu7", "第1頁第19題：依人物喜好選出最合適的活動描述", "參照以情境線索判讀偏好，而非字面重複。")],
    },
    {
        "prompt": "A sign says the main library entrance is closed because the floor is wet. A visitor asks how to get inside. What should you tell them?",
        "options": ["The floor is wet, so please use the side entrance and walk carefully.", "Run through the main entrance before it gets wetter.", "The sign means the library is closed all day.", "You can’t enter any library when it rains."], "answer": "A",
        "explanation": "正確答案 A。公告只說主要入口因地面濕滑而關閉，並沒有說整間圖書館停止服務；A 依限制提供安全替代入口。",
        "strategy": "把警示中的限制與服務是否全面停止分開，再給出有根據的安全替代方案。",
        "steps": ["讀出標示的範圍：關閉的是主要入口，原因是地面濕滑。", "不要把局部入口管制擴大解讀為整棟圖書館停業。", "訪客問如何進入，因此回答需提供可行替代路線。", "A 同時指出側門與小心行走，符合資訊及安全需求。", "確認建議沒有叫人穿越濕地，也沒有推測標示未提供的閉館時間。"],
        "refs": [("neihu8", "第1頁第20題：遇到颱風警示時選出遠離海邊較安全的回應", "參照先理解警示風險、再選安全行動的生活對話模式。"), ("neihu7", "第1頁第6題：依情境選擇能回應實際需求的基本答句", "參照情境與回應功能配對，不據此推定原卷涉及圖書館。")],
    },
    {
        "prompt": "A librarian says, ‘This book is due tomorrow. Please return it by 5 p.m.’ You can return it then. Which reply confirms the important detail?",
        "options": ["Tomorrow is a very busy day.", "I returned the book last week.", "Okay, I’ll bring it back by 5 p.m. tomorrow.", "Could you lend me another book instead?"], "answer": "C",
        "explanation": "正確答案 C。期限包含日期和時間；重述 tomorrow 與 by 5 p.m. 能確認自己掌握完整要求。",
        "strategy": "遇到有期限的請求，把日期和截止時間一併回述，避免只記住其中一項。",
        "steps": ["從圖書館員的句子擷取兩個限制：明天歸還、下午五點前。", "判斷自己能配合，所以不需要拒絕或改談另一件事。", "選擇重述日期與時間的確認句。", "C 保留了完整期限；只說明天可能漏掉截止時刻。", "最後核對時間介系詞 by 表示最晚不得超過該時刻。"],
        "refs": [("neihu8", "第2頁第29題：對服務人員提出稍後再來的時間請求", "參照日常服務情境中清楚處理時間要求的對話模式。"), ("neihu7", "第1頁第20題：服務對話中回應點餐流程與資訊", "參照服務場合依對話目的提供具體回覆的題型。")],
    },
    {
        "prompt": "The clinic receptionist says, ‘Your appointment is at 3 p.m. The doctor will see you in Room 208 instead of Room 205.’ What should you confirm?",
        "options": ["So my appointment moved to 5 p.m. in Room 205?", "So it’s still at 3 p.m., but I should go to Room 208—is that right?", "Room 208 is probably closed, so I’ll wait in 205.", "I don’t need to know the room if I know the doctor."], "answer": "B",
        "explanation": "正確答案 B。接待人員只更改診間，時間仍是三點；B 將不變資訊與更新資訊分開複述，並請對方確認。",
        "strategy": "通知有多個欄位時，逐一標記哪些改變、哪些維持，再做封閉式確認。",
        "steps": ["把通知拆成時間與地點兩個欄位。", "比較新舊資訊：時間仍為三點，診間從205改為208。", "排除自行推測的變動，例如把時間改成五點。", "B 同時保留原時間、更新房號，最後用問句請櫃台確認。", "完成確認後只按已核實的新資訊前往，不自行沿用舊診間。"],
        "refs": [("neihu7", "第1頁第20題：服務情境中由前句判斷顧客需要回答的具體資訊", "參照服務對話的訊息承接與資訊確認形式。"), ("neihu8", "第2頁第29題：在服務對話中清楚提出時間安排", "參照把時間資訊明確放入回應的能力模式。"), ("guochang", "第2頁第19題：依對話前文補全必要的人物資訊", "參照根據已知資訊完成確認，而非自行增添未提供內容。")],
    },
]

def source_ref(key, locator, observed):
    source = SOURCES[key]
    return {
        "url": source["url"], "title": source["title"], "year": source["year"], "subject": "english",
        "locator": locator, "locatorLevel": "item", "observedPattern": observed,
        "reuseDecision": "pattern-only", "status": "recorded",
    }

def main():
    for i, item in enumerate(ITEMS, 1):
        path = ROOT / f"questions/english/question-english-performance-3-iv-5-{i}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["prompt"] = item["prompt"]
        data["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(item["options"])]
        data["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
        data["solutionStrategy"] = item["strategy"]
        data["solutionSteps"] = item["steps"]
        data["examPatternRefs"] = [source_ref(*ref) for ref in item["refs"]]
        data["provenance"]["sourceUrl"] = data["examPatternRefs"][0]["url"]
        data["provenance"]["sourceLocator"] = "本題參照公立國中英文段考中依對話目的選擇生活回應的命題模式；逐題原卷定位見 examPatternRefs。公開查閱不代表授權重製；本題情境、文字、選項、答案與解析均重新撰寫。"
        data["provenance"]["authoringNote"] = "依本單元生活互動能力原創改寫；公開試題僅作 pattern-only 題型參考，未複製原題、選項或答案；仍待單元內容與答案 QA，維持 draft。"
        data["reviewStatus"] = "draft"
        data["updatedAt"] = TODAY
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    existing = {item["url"] for item in catalog["sources"]}
    for source in SOURCES.values():
        if source["url"] not in existing:
            catalog["sources"].append({
                "institution": source["institution"], "url": source["url"], "subjects": ["english"],
                "availableMaterial": source["availableMaterial"],
                "researchUse": "公開英文段考只作可追溯的對話回應能力／題型模式參考；不複製題幹、選項、圖片或答案。",
                "licenseBoundary": "公開查閱不等於可重製；保留校方原卷URL與逐題定位，教材與題目由本專案重新撰寫。",
                "sourceLocator": source["availableMaterial"],
            })
        if source["url"] not in catalog["questionSourceUrls"]:
            catalog["questionSourceUrls"].append(source["url"])
    catalog["updatedAt"] = TODAY
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Re-authored 10 original items; attached verified public-school item locators; all remain draft.")

if __name__ == "__main__":
    main()
