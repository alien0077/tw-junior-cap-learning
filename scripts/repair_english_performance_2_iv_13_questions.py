import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = {
    "guochang_appointment": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87.pdf", "高雄市立國昌國民中學113學年度第2學期第2次段考七年級英文科試題", "113-2"),
    "yichang": ("https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2671&name=112-1-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%8C%A2%E5%AE%8F%E5%81%89.pdf&op=dlfile", "花蓮縣立宜昌國民中學112學年度第1學期第2次段考九年級英文科題目與答案", "112-1"),
    "keelung": ("https://oldcsjh.kl.edu.tw/books/file/360/110-1-%E4%B8%83%E5%B9%B4%E7%B4%9A3%E6%AE%B5%E8%80%830111.pdf", "基隆市立中山高級中學國中部110學年度第1學期第3次段考七年級英文科試題卷", "110-1"),
    "guochang_invite": ("https://school.tc.edu.tw/open-message/193521/get-file/61f258cb9b96df7136093939.pdf", "臺中市立至善國民中學110學年度第1學期七年級第3次定期評量英語科試題", "110-1"),
    "guochang_picnic": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C-2%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87-%E8%A9%A6%E9%A1%8C.pdf", "高雄市立國昌國民中學108學年度第2學期第1次段考八年級英文科試題", "108-2"),
    "guochang_apology": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91_5.pdf", "高雄市立國昌國民中學113學年度第1學期第1次段考八年級英文科試題", "113-1"),
    "zhishan": ("https://school.tc.edu.tw/open-message/193521/get-file/61f259ce3fa2fc1d7e423fab.pdf", "臺中市立至善國民中學110學年度第1學期八年級第3次定期評量英語科試題卷", "110-1"),
    "guochang_clothes": ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E4%BA%8C%E8%8B%B1%E6%96%87%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf", "高雄市立國昌國民中學110學年度第2學期第1次段考八年級英文科試題", "110-2"),
    "dawan": ("https://www.dwm.kh.edu.tw/upload/344/104_64184/106-2-3%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "高雄市立大灣國民中學106學年度第2學期第3次段考八年級英文科試題", "106-2"),
    "guangwu": ("https://web.gwjh.hc.edu.tw/uploads/1675745677488ZvKru5gb.pdf", "新竹市立光武國民中學111學年度第1學期第3次段考八年級英文科試題（含聽力）", "111-1"),
}

# answer, source, skill, prompt, options, explanation, steps, locator, observed pattern
ITEMS = [
    ("B", "guochang_appointment", "電話預約時確認可用時段", "You call a clinic after school. The receptionist says, 'We have an opening at 4:20 on Thursday. Would that work for you?' Which reply confirms the appointment clearly?", ["'I have a toothache.'", "'Yes, Thursday at 4:20 works for me. Thank you.'", "'The clinic is near the station.'", "'I usually finish school at three.'"], "接待人員已提供星期與時間並詢問是否方便；B明確重述兩項預約資訊並確認，其他句子沒有回答可否赴約。", ["辨認對方正在確認的是可預約時段。", "擷取兩個關鍵資訊：Thursday及4:20。", "選擇同時重述日期與時間並明確接受的句子。", "排除只說症狀、地點或平日作息而未確認的選項。", "選B；電話預約要複述關鍵時段，避免只用含糊的yes。"], "克漏字對話第21題：診所人員提出可用時段後，詢問該安排是否合適；本題改寫日期、時間及人物。", "依單一題目的問答功能，練習複述並確認預約時段。"),
    ("B", "yichang", "回應同學提出的學習協助請求", "A classmate points to a difficult science problem and asks, 'Could you please take a look at this question?' Which reply moves the conversation forward helpfully?", ["'The science room is on the second floor.'", "'Sure. Let's read the question together and find what it is asking.'", "'I finished my homework last week.'", "'You should have asked the teacher yesterday.'"], "B直接接受協助請求，並提出一起閱讀題目的下一步；其他選項提供無關資訊、離題敘述或責怪同學。", ["先聽出對方是在請求一起看題目。", "找出明確接受幫忙的回應。", "檢查回應是否提出可立即進行的共同步驟。", "排除只說地點、過去作業或責備對方的句子。", "選B；回應求助時先表明是否願意，再提出具體協助方式。"], "聽力基本問答第9題：對方請求協助查看科學題，選擇合宜的回應。", "把公開聽力中的學習求助／回應功能改寫成全新的科學題討論情境。"),
    ("A", "yichang", "以委婉問句問路", "You are near the train station but cannot find the public library. What is the clearest polite question to ask a passerby?", ["'Could you tell me how to get to the public library from here?'", "'You know the library, don't you?'", "'I went to the library yesterday.'", "'The station has many people.'"], "A以Could you tell me...提出請求，並清楚說出目的地及from here的出發點；其他選項未提出可回答的路線問題。", ["找出實際需求：從目前位置到公共圖書館的路線。", "辨認委婉請求句型Could you tell me...。", "確認句中有目的地library及出發位置from here。", "排除反問、過去敘述和與問路無關的觀察。", "選A；問路時同時交代目的地與出發點，對方才能提供可用方向。"], "手寫題第2題：把Could you tell me where I can park my car改成間接問句；本題改為詢問公共圖書館路線。", "參照禮貌間接問句詢問地點資訊的語用形式，路線、地點和句子另創。"),
    ("C", "guochang_clothes", "在商店回答尺寸問題", "A clerk asks which shirt size you wear. You need a medium. Which reply gives the needed information directly?", ["'I bought a shirt last winter.'", "'The blue one is near the door.'", "'I wear a medium. May I try it on?'", "'My sister likes this color.'"], "C先回答尺寸，再提出試穿請求；其他選項沒有提供店員詢問的尺寸。", ["確認店員問的是尺寸，不是顏色、位置或購買時間。", "從需求找出medium這個必要資訊。", "挑選先清楚回答再補充試穿請求的句子。", "排除未回答尺寸的其餘選項。", "選C；購物對話先回答對方問題，再補上下一個具體需求。"], "單題第6題：店員詢問顧客穿什麼尺寸；本題改寫成回答尺寸並接續試穿請求。", "沿用公開考題中尺寸問答的溝通功能，不重用原題人物或句子。"),
    ("D", "guochang_invite", "依時間衝突協調活動日期", "Your friend invites you to a concert on Friday, but you have an English class then. Which reply suggests a clear alternative date?", ["'I like concerts very much.'", "'Friday is the fifth day of the week.'", "'The concert hall is large.'", "'I have class on Friday. Could we go on Saturday instead?'"], "D說明原定時間的衝突，並提出可確認的新日期；其他選項沒有協調行程。", ["找出不能赴約的限制：Friday有英文課。", "判斷回應是否誠實說明衝突。", "確認是否提出具體替代日期並詢問對方。", "排除只談喜好、星期常識或場地的選項。", "選D；協調改期時說明衝突並提出可行替代方案。"], "聽力言談理解第7題：雙方討論演唱會日期，遇到時間衝突後提出並確認另一日。", "改寫公開試題中邀約、說明行程衝突及協調日期的對話功能。"),
    ("B", "guochang_apology", "承認失言並修復關係", "You interrupt a classmate and make a careless comment while they explain their experiment. Which reply takes responsibility and lets them continue?", ["'You should have talked faster.'", "'Sorry I interrupted you. Please finish your explanation; I’ll listen.'", "'The experiment is not important.'", "'I will answer for you from now on.'"], "B承認自己打斷對方、道歉並把發言權交還；其他選項責怪對方、貶低內容或奪走話語權。", ["先辨認溝通問題：自己打斷同學並說了不妥的話。", "選擇直接承認行為並道歉，而不是推卸責任。", "確認後半句有把發言機會交還原說話者。", "排除責怪、輕視對方或繼續替對方發言。", "選B；修復對話要承認影響、道歉，並用行動讓對方重新發言。"], "單題第3題：兒子回應提醒時道歉，並承諾不再重複傷人的話；本題改為打斷同學後道歉並交還發言權。", "參照公開試題中承認不當言語、道歉及提出修正的對話功能。"),
    ("C", "guochang_appointment", "用確認式追問消除指涉不清", "A teacher says, 'Please bring the blue folder to the lab.' There are two blue folders on your desk. Which follow-up prevents a mistake?", ["'The lab is downstairs.'", "'I already have a folder.'", "'Do you mean the blue folder labeled Chemistry or the one labeled Field Notes?'", "'Blue is my favorite color.'"], "C指出兩個可能對象並請老師確認指涉；其他選項沒有區分文件，仍可能拿錯。", ["辨認模糊處：桌上有兩份藍色資料夾。", "列出能區分兩者的可見標籤。", "使用問句請對方確認究竟是哪一份。", "排除只談地點、擁有文件或顏色偏好的句子。", "選C；澄清問題應呈現具體選項，讓對方容易確認。"], "克漏字對話第24題：根據語境詢問桌上書本屬於誰；本題改為辨認兩個藍色資料夾中的指定文件。", "參照公開試題以具體問句消除物品指涉不明的能力，物件和標籤另創。"),
    ("B", "zhishan", "在餐飲服務中追加清楚請求", "At a café, you order hot tea and the clerk says it will be ready soon. You also need a cup of water. What is the most suitable reply?", ["'I bought tea last year.'", "'Thank you. Could I also have a small cup of water?'", "'The café is next to the library.'", "'You should bring the menu tomorrow.'"], "B先禮貌回應原點餐，再提出具體附加需求；其他選項無關或不合服務情境。", ["確認店員已接下熱茶訂單。", "找出先致謝、再提出額外需求的選項。", "檢查新需求是否具體且店員能直接處理。", "排除過去敘述、地點資訊或不相關指令。", "選B；原需求確認後，追加要求要明確說出品項並維持禮貌。"], "單題第33題：顧客向店員點熱茶，店員回應會立即準備；本題改成確認訂單後追加飲水需求。", "參照公開考題中的餐飲點餐及服務回應功能，重新創作點單與附加需求。"),
    ("A", "guochang_picnic", "清楚回應邀請並接續安排", "A friend invites you to a Saturday community garden visit. You are free and would like to join. Which reply accepts and helps make the plan clear?", ["'That sounds great. Thanks for inviting me! What time should I meet you?'", "'Saturday is the day after Friday.'", "'I went to a garden last year.'", "'I don't know what a garden is.'"], "A禮貌接受邀請，並追問集合時間以便落實安排；其他選項未回應邀請或沒有推進計畫。", ["確認自己有空，而且想參加。", "找出明確接受邀請並表達感謝的句子。", "檢查是否詢問實際參加所需的集合資訊。", "排除星期常識、過去經驗或無關疑問。", "選A；接受邀約後可接著確認時間或地點，讓計畫更完整。"], "閱讀對話第26題：受邀者接受野餐邀請，並接續詢問集合時間與地點。", "改寫公開段考中接受邀請並追問活動安排的對話功能。"),
    ("C", "dawan", "在餐廳清楚說明餐點偏好", "A server asks how you would like your steak cooked. You prefer it medium-well. Which answer directly states your choice?", ["'That’s a point.'", "'I want them all.'", "'Medium-well, please.'", "'Lucky me.'"], "C直接回答服務人員的烹調熟度問題，並以please保持禮貌；其餘選項無法表達餐點偏好。", ["辨認服務人員詢問的是牛排熟度。", "對照自己的選擇：medium-well。", "選擇直接說出熟度並加上禮貌語的回答。", "排除文意不通或沒有回答問題的句子。", "選C；服務對話要聽清楚對方詢問的規格，再提供明確選擇。"], "對話選擇第39題：服務人員詢問牛排熟度，顧客直接回答medium-well；本題改寫選擇與答句。", "沿用餐廳服務對話中回答具體餐點偏好的功能，不複製原題對話。"),
]


def make(index, item):
    answer, source_key, skill, prompt, options, explanation, steps, locator, pattern = item
    url, title, year = SOURCES[source_key]
    return {
        "id": f"question-english-performance-2-iv-13-{index}",
        "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": [{"id": chr(65 + n), "text": value} for n, value in enumerate(options)],
        "knowledgeIds": ["kg-english-performance-2-iv-13"], "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" 正確答案：{answer}。"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": url, "sourceLocator": locator + "；人物、需求、台詞、選項與答案均重新創作。", "authoringNote": "僅參照公立學校英文段考的日常對話功能、合宜回應、預約／邀請／購物／求助題型作pattern-only改寫，未複製原題內容。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-24", "lessonId": "lesson-english-performance-2-iv-13",
        "examPatternRefs": [{"url": url, "title": title + "；只取日常溝通功能與回應方式，不複製原題。", "year": year, "subject": "english", "locator": locator, "observedPattern": pattern, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item"}],
        "solutionStrategy": f"{skill}：先確認情境中的目的與限制，再選用能清楚表達需求、尊重對方並推動下一步的句子。",
        "solutionSteps": steps,
    }


for index, item in enumerate(ITEMS, 1):
    (OUT / f"question-english-performance-2-iv-13-{index}.json").write_text(json.dumps(make(index, item), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(ITEMS)} original everyday-communication questions")
