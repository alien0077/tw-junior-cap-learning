#!/usr/bin/env python3
"""Repair public sources, answer keys, and response strategies for English 5-IV-12."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/english"
CATALOG = ROOT / "data/public-exam-sources.json"
TODAY = "2026-09-26"

SOURCES = [
    {
        "id": "kcjh-105-2-term3-grade7-english",
        "school": "高雄市立國昌國民中學", "grade": "7", "subject": "english",
        "exam": "105學年度第2學期第3次段考", "year": "105-2",
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/1%E8%8B%B1%E6%96%87%E4%BF%AE%E6%AD%A30623.pdf",
        "title": "高雄市國昌國中105學年度第2學期第3次段考一年級英語科題目卷",
        "examLocator": "PDF第3頁筆友信閱讀題第34至35題；辨認書信資訊與依文作答",
    },
    {
        "id": "ycjh-110-1-term1-grade7-english",
        "school": "花蓮縣立宜昌國民中學", "grade": "7", "subject": "english",
        "exam": "110學年度第1學期第1次段考", "year": "110-1",
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=359&cfsn=2121&fn=110-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE-%E6%9E%97%E7%8E%89%E8%93%AE.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中110學年度第1學期第一次段考七年級英語科試題",
        "examLocator": "PDF第5頁第31至33題；未來的自己收到信件後的細節與推論",
    },
    {
        "id": "nhjh-110-1-term3-grade8-english",
        "school": "臺北市立內湖國民中學", "grade": "8", "subject": "english",
        "exam": "110學年度第1學期第3次段考", "year": "110-1",
        "url": "https://www.nhjh.tp.edu.tw/30/2133/news/19/2022-1/42022-1-27-13-49-5-nf1.pdf",
        "title": "臺北市立內湖國中110學年度第1學期八年級英語科第三次段考",
        "examLocator": "PDF第4頁第43至47題；兩封往返信件的對象、目的、推論及指涉",
    },
]

# Key, options A-D, locators from the three sources, strategy, worked steps.
ITEMS = {
    1: ("A", ["Coach Lee", "Sam's bus driver", "The team photographer", "A bookstore clerk"], ["PDF第3頁筆友信閱讀題第34至35題", "PDF第5頁第31至33題", "PDF第4頁第43至47題"], "辨認收件者時看稱呼而非署名：Dear 後面是收件人，結尾 Your... 後面才是寄件人。", ["先找到信件開頭的稱呼 Dear Coach Lee。", "Dear 後方的名字標示收件者；感謝教練的內容也與稱呼一致。", "結尾 Your player, Sam 是寄件人的署名，不能把 Sam 誤認成讀信者。", "其餘三個人既未出現在稱呼，也不符合信件對象。", "答案 A：收件者是 Coach Lee。"]),
    2: ("B", ["To order a meal at a restaurant", "To share news about a move", "To report a broken school computer", "To give directions to a hospital only"], ["PDF第3頁筆友信閱讀題第34至35題", "PDF第5頁第31至33題", "PDF第4頁第43至47題"], "判斷寫信目的要看訊息中心，而不是把每個附帶細節都當主旨；搬家是主訊息，安靜街區與公園是補充。", ["先抽出最先交代的事件：上個月搬進新公寓。", "安靜的鄰里和附近公園都是搬家後的生活近況。", "將資訊合併成目的：寫信分享搬家及新住處消息。", "餐點、電腦故障與醫院路線都沒有在信中出現。", "答案 B：這封信是在分享搬家的近況。"]),
    3: ("C", ["Cold and threatening", "Formal and angry", "Warm and cheerful", "Confused and apologetic"], ["PDF第3頁筆友信閱讀題第34至35題", "PDF第5頁第31至33題", "PDF第4頁第43至47題"], "語氣從祝福用語判斷：wonderful、fun、good surprises 都帶正向情感，因此應選溫暖愉快，而非只看卡片形式。", ["標出 Have a wonderful day 及 good surprises 兩個正向詞語。", "寫信者祝對方生日愉快，也盼對方新的一年有好事。", "這些措辭傳達親切祝福，並非正式、憤怒或道歉。", "對照選項，warm and cheerful 同時涵蓋親切與正面情緒。", "答案 C：生日卡片語氣溫暖、愉快。"]),
    4: ("D", ["A tent for Friday night", "A book for the library", "A winter coat for the mountain", "Fruit"], ["PDF第3頁筆友信閱讀題第34至35題", "PDF第5頁第31至33題", "PDF第4頁第43至47題"], "回覆邀請的物品題以明確請求為準，把 bring 後的受詞直接記下，不從活動地點猜測額外裝備。", ["確認邀請的活動是 Sunday 11:00 在 Riverside Park 的 picnic。", "讀出邀請者的明確請求：asks her to bring fruit。", "只選被明講要帶的物品，不自行推測帳篷、書或登山衣物。", "時間、地點與其他干擾物品都不能取代 fruit 這項要求。", "答案 D：Priya 應帶 fruit。"]),
    5: ("A", ["Say whether the writer can join and respond by Tuesday", "Describe an unrelated holiday from last year", "Ask the friend to move to another country", "Copy the question without giving an answer"], ["PDF第3頁筆友信閱讀題第34至35題", "PDF第5頁第31至33題", "PDF第4頁第43至47題"], "回覆邀約需完成兩件事：回答能否參加，並遵守對方要求的回覆期限；日期和 yes/no 意圖都不可漏。", ["把邀請拆成事件與需要回覆的資訊：週四讀書會、能否加入。", "再圈出 Please tell me by Tuesday，這是回覆期限。", "一封合宜回信要交代是否參加，且在週二前讓朋友知道。", "談去年假期、要求搬國或照抄問題，都沒有回答邀請。", "答案 A：說明能否參加，並在 Tuesday 前回覆。"]),
    6: ("B", ["Your invitation is meaningless, and stop writing.", "Thank you for asking, but I cannot attend because I have a family appointment.", "I will attend every event forever without a date.", "Please send the appointment to my classroom."], ["PDF第3頁筆友信閱讀題第34至35題", "PDF第5頁第31至33題", "PDF第4頁第43至47題"], "婉拒訊息保留關係的順序是先感謝，再清楚拒絕，最後給簡短且不過度暴露的原因。", ["情境的核心限制是有家庭約會，無法出席。", "先用 Thank you for asking 表達感謝，讓對方知道邀請被重視。", "再明確說 cannot attend，避免讓對方誤以為仍會到場。", "because I have a family appointment 提供合宜理由；其餘選項失禮或不合邏輯。", "答案 B：感謝邀請、清楚婉拒並簡述家庭行程。"]),
    7: ("C", ["Mail the empty envelope", "Choose a different recipient before reading", "Write a short message", "Throw away the card"], ["PDF第3頁筆友信閱讀題第34至35題", "PDF第5頁第31至33題", "PDF第4頁第43至47題"], "依序詞 first、then、finally 建立步驟鏈；問 after choosing a photo 就找緊接在 then 的動作。", ["將指令轉成三步：choose a photo → write a short message → put the card in an envelope。", "題目指定第一步之後，因此不需要猜最後的寄送安排。", "then 引出的第二步是 write a short message。", "空信封、換收件人和丟掉卡片都不是指示列出的下一步。", "答案 C：選好照片後，接著寫一段短訊息。"]),
    8: ("D", ["The writer never received a gift", "The writer lost the jacket before the trip", "The mountain is always hot at night", "The writer finds the jacket useful in cool weather"], ["PDF第3頁筆友信閱讀題第34至35題", "PDF第5頁第31至33題", "PDF第4頁第46至47題"], "推論要由原文線索跨一步但不能超出證據：天冷、每天穿那件外套，支持它在涼冷天氣實用。", ["找出原因線索：mountain air is cool。", "再讀行動：作者每個早晨都穿上對方送的 jacket。", "將兩句連起來，可推知外套適合山區涼冷氣候，且作者常用它。", "原文沒有說外套遺失、沒收到禮物或夜間總是炎熱。", "答案 D：作者認為那件外套在涼冷天氣很實用。"]),
    9: ("B", ["No one is presenting, so bring a birthday cake.", "Of course. We can practice after lunch, and I can listen to your opening.", "I practiced last year, and the weather was sunny.", "Do not speak to me about school or presentations."], ["PDF第3頁筆友信閱讀題第34至35題", "PDF第5頁第31至33題", "PDF第4頁第43至47題"], "支持性回覆需回應對方的情緒和明確請求；把對方提出的時間、活動與需要的幫助逐一對上。", ["同學說 nervous，表示需要鼓勵，但回信仍要回應實際請求。", "請求是 after lunch 練習簡報，並非詢問去年經驗或生日活動。", "合適回覆接受練習邀請，還提出可聽開場作為具體協助。", "其餘選項否定簡報情境、偏離主題或拒絕支持。", "答案 B：答應午餐後練習，並提供與開場相關的幫助。"]),
    10: ("C", ["Answer only the hobby and discuss an unrelated movie for the rest of the letter.", "Ignore every question and send only a greeting.", "Answer the date, meal, and hobby questions in order, then ask one related question.", "Change the arrival date without explaining the reason."], ["PDF第3頁筆友信閱讀題第34至35題", "PDF第5頁第31至33題", "PDF第4頁第43至47題"], "多問句回信先逐項做核對清單，再依原信順序回答；結尾可加一個相關問題，避免漏答或跳題。", ["把原信三個問項列成清單：抵達日期、寄宿家庭餐點、可分享的嗜好。", "草擬回覆時按原順序逐項填入答案，方便讀者逐題找到資訊。", "回答完三項後，可以補一個與交換生活相關的問題延續對話。", "只答嗜好、只打招呼或無故更改日期，都沒有完整回應原信。", "答案 C：依序回答日期、餐點、嗜好，再附上一個相關問題。"]),
}

OBSERVED = "只參照公立學校英文評量中書信／卡片的稱呼、署名、目的、明示資訊、推論與回應方式；站內人物、情境、措辭、選項與答案均獨立撰寫，未複製原卷。"


def refs(locators: list[str]) -> list[dict]:
    return [{"url": source["url"], "title": source["title"], "year": source["year"], "subject": "english", "locator": locator, "locatorLevel": "page", "observedPattern": OBSERVED, "reuseDecision": "pattern-only", "status": "recorded"} for source, locator in zip(SOURCES, locators, strict=True)]


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    known = {source["id"] for source in catalog["sources"]}
    for source in SOURCES:
        if source["id"] not in known:
            catalog["sources"].append({"id": source["id"], "school": source["school"], "grade": source["grade"], "subject": source["subject"], "exam": source["exam"], "questionUrl": source["url"], "answerLocator": source["examLocator"], "usePolicy": "僅研究公立學校公開英語書信閱讀與回應的能力方向；不保存或重製原卷題文、選項或答案。", "verifiedAt": TODAY})
    catalog["updatedAt"] = TODAY
    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for number, (key, options, locations, strategy, steps) in ITEMS.items():
        path = QDIR / f"question-english-performance-5-iv-12-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)]
        data["answer"]["value"] = key
        data["answer"]["explanation"] = steps[-1]
        data["solutionStrategy"] = strategy
        data["solutionSteps"] = steps
        data["examPatternRefs"] = refs(locations)
        data["provenance"]["sourceUrl"] = SOURCES[0]["url"]
        data["provenance"]["sourceLocator"] = "國昌、宜昌、內湖三所公立國中公開英語段考；逐題書信閱讀頁碼／題號及 pattern-only 界線見 examPatternRefs。"
        data["provenance"]["authoringNote"] = "依官方課綱與 KG-english-performance-5-iv-12，參照三所公立學校英語書信理解／回應題的能力方向獨立撰寫；情境、用語、選項、答案及詳解均為原創，仍待完整內容與版權 gate。"
        data["updatedAt"] = TODAY
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("updated ten original letter/card questions with three public-school references each")


if __name__ == "__main__":
    main()
