import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SANDUO = "https://www.sdjh.ntpc.edu.tw/p/405-1000-6042%2Cc837.php?Lang=zh-tw"
YICHANG = "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=432&cfsn=2875&fn=113-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile"
JINGXING = "https://www.chhs.tp.edu.tw/uploads/1642655973756S6WiICcM.pdf"
ZHONGSHAN = "https://csjh.kl.edu.tw/books/file/528/111-1%E7%AC%AC%E4%B8%89%E6%AC%A1%E5%9C%8B%E4%B8%89%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf"

SOURCES = {
    "sanduo_routine": (SANDUO, "新北市立三多國中113學年度第1學期八年級第一次段考英文科", "113-1", "PDF第4頁第45題：綜合星期、地點與社團活動線索判斷人物正在做什麼", "把地點、固定活動時間與人物行程交叉比對；本題改為從影片場景和字幕確認拍攝地。"),
    "sanduo_sequence": (SANDUO, "新北市立三多國中113學年度第1學期八年級第一次段考英文科", "113-1", "PDF第5頁手寫題第3題：以After／Before改寫先後順序", "辨認兩個動作的先後關係再轉述；本題另創影片步驟，不沿用來源句子。"),
    "sanduo_time": (SANDUO, "新北市立三多國中113學年度第1學期八年級第一次段考英文科", "113-1", "PDF第4頁第44題：依人物活動與時段表判斷當下時間", "將活動和時間線索對應；本題以全新影片字幕提供時間地點。"),
    "sanduo_infer": (SANDUO, "新北市立三多國中113學年度第1學期八年級第一次段考英文科", "113-1", "PDF第3頁第41題：由對話推知人物對季節的看法", "根據語句線索推知人物態度；本題改以表情變化、旁白和行動結果共同判讀情緒。"),
    "yichang_main": (YICHANG, "花蓮縣立宜昌國中113學年度第1學期九年級第一次段考英文科", "113-1", "PDF第3頁第30題：閱讀主旨", "整合多個訊息判斷整體主旨；本題另寫原創多鏡頭影片訊息。"),
    "yichang_purpose": (YICHANG, "花蓮縣立宜昌國中113學年度第1學期九年級第一次段考英文科", "113-1", "PDF第3頁第27題：判斷短篇資訊的用途", "依說明內容判斷其用途；本題以全新教學影片的設計特徵推斷目標觀眾。"),
    "yichang_cause": (YICHANG, "花蓮縣立宜昌國中113學年度第1學期九年級第一次段考英文科", "113-1", "PDF第4頁第36題：閱讀中的原因判讀", "從明示資訊找出結果成因；本題以畫面變化和旁白重新設計因果情境。"),
    "yichang_fact": (YICHANG, "花蓮縣立宜昌國中113學年度第1學期九年級第一次段考英文科", "113-1", "PDF第3頁第31題：根據文章判斷正確敘述", "逐項核對文本細節；本題以畫面字幕交叉提供新事實。"),
    "jingxing_cause": (JINGXING, "臺北市立景興國中110學年度第1學期八年級第三次定期評量英文科", "110-1", "PDF第2頁第32題：由規則和情境判斷事件原因", "把當下行動連結到明確規則；本題另寫交通安全影片。"),
    "zhongshan_main": (ZHONGSHAN, "基隆市立中山高中國中部111學年度第1學期九年級第三次段考英文科", "111-1", "PDF第4頁第33題：閱讀主旨", "把跨段訊息統整為文章主旨；本題重寫為全新影片標題判讀。"),
}

ITEMS = [
    ("D", "yichang_main", "影片主旨", "Three clips show a student repairing a torn backpack, filling a bottle at a water station, and sharing a bike. The final caption reads, 'Small choices add up.' What is the video mainly encouraging viewers to do?", ["Buy new equipment for every activity.", "Avoid using public places.", "Repair only objects made of cloth.", "Choose reusable or repairable options in daily life."], "修補背包、重複裝水與共用單車是三種不同例子，結尾字幕把它們統整為日常可持續選擇。", ["先判斷題目問整支影片主旨，不是單一鏡頭。", "逐鏡頭記下行動：修理、重複使用、共用。", "讀結尾字幕，確認它把多種小行動歸納在一起。", "排除只談布包的C和鼓勵購買新品的A。", "選D；主旨要同時涵蓋例子與影片結語。"]),
    ("C", "sanduo_routine", "場景線索整合", "The camera passes a lighthouse and fishing boats. A wall map labels the building 'Harbor History Center,' while the guide points to an old ship model. Where is the video being filmed?", ["At a mountain weather station.", "Inside a city swimming pool.", "At a harbor history center.", "In a school science laboratory."], "燈塔、漁船只是環境線索；牆上標示的 Harbor History Center 直接確認拍攝地點。", ["先列出畫面可見的場所線索，再把背景與文字分開。", "辨認燈塔和漁船指向港邊，但不要只靠背景猜機構。", "再讀牆上名稱 Harbor History Center。", "檢查選項C同時符合地點標示與船舶展品。", "選C；場景題用明確標示驗證背景推測。"]),
    ("A", "sanduo_sequence", "鏡頭順序", "A repair video shows four shots: unplug the lamp, remove the shade, replace the bulb, and test the switch. Which action happens immediately before replacing the bulb?", ["Remove the shade.", "Test the switch.", "Plug the lamp in.", "Clean the table."], "影片次序是拔插頭、拆燈罩、換燈泡、測試開關；換燈泡前一個動作是拆下燈罩。", ["把題目問的動作定位為 replace the bulb。", "從影片描述抄出四個動作，不自行補步驟。", "按順序排成1拔插頭、2拆燈罩、3換燈泡、4測試。", "尋找第3步緊鄰的前一格，並排除之後才做的測試。", "選A；immediately before 問的是緊接前一動作。"]),
    ("B", "sanduo_time", "字幕時間地點", "A title card reads 'Club open house — Friday, 4:15 p.m., Art Room 2.' The next shot shows students setting up paintbrushes. When and where should a visitor go?", ["Thursday at 4:50 in the music room.", "Friday at 4:15 p.m. in Art Room 2.", "Friday at 2:15 p.m. in the gym.", "Saturday at 4:15 p.m. in the art office."], "字幕同時提供星期、時間和教室；後續畫面是美術材料，與 Art Room 2 相符。", ["先從字幕提取星期 Friday。", "再記時間 4:15 p.m.，保留下午而非上午。", "讀地點 Art Room 2，不用由畫面自行猜樓層。", "逐項比對三個欄位，B 全部一致。", "選B；遇到時間地點題，逐欄核對避免選項偷換一項。"]),
    ("C", "jingxing_cause", "行動原因", "At a crosswalk, the video shows a red signal and cars moving across the street. A student waits behind the line, then crosses when the signal turns green. Why did the student wait?", ["To let a friend take a photograph.", "Because the sidewalk was closed.", "The signal and traffic made crossing unsafe at that moment.", "To stop the cars from reaching the next street."], "紅燈且車輛仍在通行，說明當下不適合穿越；等待綠燈才通行是安全原因。", ["找出等待發生時的兩個線索：紅燈、車流。", "確認影片接著顯示綠燈才通過，建立前後對照。", "將規則和行動連起來：車輛通行時停等可避免危險。", "排除拍照、封路和控制車輛等畫面未提供的原因。", "選C；推原因必須由同時出現的線索支持。"]),
    ("D", "sanduo_infer", "表情與情緒推論", "Mina looks tense as wind pushes rain toward her poster. Her classmates move the display under a covered walkway. She exhales, smiles, and says, 'Now everyone can read it.' How does Mina most likely feel at the end?", ["Confused because the poster disappeared.", "Angry that nobody came to school.", "Bored with the project from the beginning.", "Relieved that the poster is protected and visible."], "移到有遮蔽處後她吐氣、微笑，並說大家看得到，支持她放下擔心、感到安心。", ["先比較前後表情：起初緊張，最後微笑並吐氣。", "注意行動改變：海報移到有遮蔽的走廊。", "聽她說 everyone can read it，確認問題已解決。", "排除困惑、憤怒和無聊，這些情緒與解決後的反應不符。", "選D；判斷情緒要合看表情、台詞及事件結果。"]),
    ("A", "yichang_cause", "畫面因果", "A dark classroom becomes brighter in the next shot. The curtains are now open, and sunlight reaches the desks. The narrator says, 'Let the daylight do the work.' What caused the room to brighten?", ["Opening the curtains allowed daylight to enter.", "Students turned off every window.", "The desks were moved into a different building.", "The narrator changed the time on the clock."], "前後鏡頭顯示拉開窗簾後陽光照進教室，旁白也指出利用日光。", ["比較前後兩個鏡頭的變化：暗室變亮。", "找出兩鏡頭之間改變的動作：窗簾打開。", "用窗邊陽光照到桌面的畫面驗證光線來源。", "旁白 daylight 與畫面相互支持，其他選項未出現。", "選A；因果題需確認變化前後及可見的觸發動作。"]),
    ("B", "zhongshan_main", "影片標題／核心主題", "A short film follows volunteers sorting donated books, checking each book's condition, and placing usable copies in a free shelf. A final card says, 'A good story can travel again.' Which title best fits the whole film?", ["The Fastest Way to Build a Bookshelf", "Giving Used Books Another Reader", "Why Libraries Must Close Early", "How to Write a Mystery Novel"], "整理、檢查並放上免費書架都服務於讓可用書籍找到下一位讀者；B涵蓋整段影片。", ["先列出影片重複的核心物件與行動：二手書、整理、分享。", "留意結尾 travel again 是書再次流通的比喻。", "選能概括整理、檢查和分享目的的標題。", "排除只談書架、閉館時間或寫作技巧的選項。", "選B；好標題需包含影片核心行動與目的，而非只抓一個物件。"]),
    ("C", "yichang_purpose", "受眾與教學方式", "A video demonstrates how to fold a paper map. It pauses after each fold, places a close-up beside the full map, and labels each step with simple words. Who is the video most likely designed to help?", ["People who already teach mapmaking professionally.", "Viewers looking for a fast travel advertisement.", "Beginners learning the folding method for the first time.", "People who want to repair a camera."], "逐步停格、近景和簡單標籤是為初學者降低操作難度的教學設計。", ["先辨認影片類型：它示範一個可照做的摺法。", "找教學支持：逐步停格、近景、簡單字詞。", "推論這些安排服務首次學習者，而非熟練專業者。", "排除旅遊廣告和相機維修，兩者與畫面任務無關。", "選C；受眾題從語言難度、示範速度及說明細度推回目標觀眾。"]),
    ("D", "yichang_main", "多模態摘要", "A safety clip shows a wet entrance, a worker placing a bright sign, and visitors using another doorway. The narrator adds, 'Please keep this path clear until the floor is dry.' Which summary includes the most important message?", ["The worker is selling a new floor sign.", "Visitors should clean the entire building before entering.", "The entrance is closed permanently for construction.", "Use the alternate doorway and keep clear of the wet floor until it dries."], "畫面提供濕地、警示牌和替代入口，旁白補上保持通道暢通直到地面乾燥；D整合了安全行動和期限。", ["先把畫面證據分成危險、警示、替代路線三項。", "再聽旁白的行動要求及時間條件：地面乾前保持通道暢通。", "選擇同時保留避開濕地與暫時性的摘要。", "排除永久封閉、全棟清潔或販售告示牌等無據內容。", "選D；摘要需整合影像和旁白，且不能刪掉關鍵安全限制。"]),
]


def make(index, row):
    answer, src_key, skill, prompt, choices, explanation, steps = row
    url, title, year, locator, pattern = SOURCES[src_key]
    ref = {"url": url, "title": title + "；僅吸收題型／推理方向，不複製原題、選項、答案或素材。", "year": year, "subject": "english", "locator": locator, "observedPattern": pattern, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item"}
    return {"id": f"question-english-performance-1-iv-8-{index}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": chr(65+i), "text": text} for i, text in enumerate(choices)], "knowledgeIds": ["kg-english-performance-1-iv-8"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" 正確答案：{answer}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": url, "sourceLocator": locator + "；依能力模式獨立創作新影音情境，未重製原題。", "authoringNote": "短片描述、鏡頭、字幕、旁白、選項、解析、策略及解題步驟皆為原創；僅取公立學校公開英文試題的資訊整合能力模式。維持draft；Terra審查依使用者指示取消。"}, "reviewStatus": "draft", "updatedAt": "2026-09-24", "lessonId": "lesson-english-performance-1-iv-8", "examPatternRefs": [ref], "solutionStrategy": f"{skill}：分辨畫面、字幕／旁白與鏡頭順序各自提供的證據，再選擇能被完整影片線索支持、且沒有額外杜撰的解讀。", "solutionSteps": steps}


for i, row in enumerate(ITEMS, 1):
    (OUT / f"question-english-performance-1-iv-8-{i}.json").write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(ITEMS)} original multimodal-video comprehension questions")
