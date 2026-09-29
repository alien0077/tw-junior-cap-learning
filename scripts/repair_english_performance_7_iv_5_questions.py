"""Write original, source-traceable 7-IV-5 study-plan questions.

Public-school exam references are used as question-pattern evidence only. No
exam prompt, option, passage, answer, or graphic is copied.
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
REGISTRY = ROOT / "data/public-exam-sources.json"
TODAY = date.today().isoformat()

SOURCES = [
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91_6.pdf",
        "title": "高雄市立國昌國民中學112學年度第2學期第3次段考七年級英文科試題",
        "year": "112-2",
        "locator": "PDF第4頁第31題：比較四份讀書時段與休息安排，辨認符合指定學習方法的計畫。",
        "observedPattern": "以多份時間表的活動與時段比對條件；本題只借用讀取排程、核對限制的設問形式。",
        "school": "高雄市立國昌國民中學",
        "grade": "7",
        "exam": "112學年度第2學期第3次段考",
        "questionUrl": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91_6.pdf",
        "answerLocator": "PDF第4頁第31題；僅參照時間表條件判讀形式。",
    },
    {
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=356&cfsn=2061&name=107-1%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%838%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E7%A7%91%E8%80%83%E9%A1%8C-%E9%84%A7%E7%88%B0%E7%91%80.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國民中學107學年度第1學期第2次段考八年級英文科試題",
        "year": "107-1",
        "locator": "PDF第5頁閱讀題組第39至41題；第41題判讀建議製作讀書計畫及善用時間的理由。",
        "observedPattern": "從建議信的情境線索判斷讀書計畫與時間運用的功能；本題重新設計人物、目標及決策。",
        "school": "花蓮縣立宜昌國民中學",
        "grade": "8",
        "exam": "107學年度第1學期第2次段考",
        "questionUrl": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=356&cfsn=2061&name=107-1%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%838%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E7%A7%91%E8%80%83%E9%A1%8C-%E9%84%A7%E7%88%B0%E7%91%80.pdf&op=dlfile",
        "answerLocator": "PDF第5頁閱讀題組第39至41題；只參照建議與理由理解。",
    },
    {
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/109-1-3%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立大灣國民中學109學年度第1學期第3次段考九年級英文科試題",
        "year": "109-1",
        "locator": "PDF第3頁（試卷印刷第4頁）第31至33題；判讀平日讀書安排與週末休閒選擇的對話資訊。",
        "observedPattern": "依對話明示的週間安排及週末活動判讀時間配置與選擇；本題以不同任務及時間資料改寫。",
        "school": "高雄市立大灣國民中學",
        "grade": "9",
        "exam": "109學年度第1學期第3次段考",
        "questionUrl": "https://www.dwm.kh.edu.tw/upload/344/104_64184/109-1-3%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
        "answerLocator": "PDF第3頁（試卷印刷第4頁）第31至33題；只參照安排與休閒平衡的資訊判讀。",
    },
]

# Each row is independently authored for one self-monitoring decision. The
# answer letter distribution is deliberately balanced: A/B/C/D = 2/3/2/3.
ITEMS = [
    {
        "prompt": "小芸想在兩週內改善英文單字運用。哪個目標最容易在期限後檢查是否達成？",
        "options": ["把英文變得更好", "學會 12 個校園單字，並各寫一句新句子", "有空就翻英文課本", "背完整本字典"], "answer": "B",
        "explanation": "B 同時說明學習內容、可計數的成果與可觀察的運用方式；其他選項不是沒有界定標準，就是不切實際。",
        "strategy": "目標可檢核性：把「想進步」拆成指定內容、數量與可展示成果。",
        "steps": ["先找出小芸要改善的是單字運用，而非泛稱英文成績。", "比較各選項是否說明學什麼、做到多少，以及如何呈現成果。", "B 指定 12 個校園單字，並要求各自造新句，兩部分都能核對。", "A 沒有標準，C 沒期限也沒成果，D 的範圍不合理，因此排除。", "回到兩週期限檢查：十二句可逐句計數，故選 B。"],
    },
    {
        "prompt": "阿哲週三只有 45 分鐘，想練聽力並整理錯題。哪個安排最符合時間限制，也留下檢查結果的時間？",
        "options": ["聽一小段 10 分鐘、重聽並記下 3 個漏聽處 20 分鐘、核對修正 15 分鐘", "連續播放影片 45 分鐘，不做記錄", "列出要買的耳機與文具 45 分鐘", "排入兩小時聽力練習，再省略核對"], "answer": "A",
        "explanation": "A 的三段合計正好 45 分鐘，且安排聆聽、診斷漏聽與核對；其餘安排缺少自我檢查或超出可用時間。",
        "strategy": "有限時段配置：先守住可用分鐘數，再確保練習、診斷、核對都有位置。",
        "steps": ["題目給的總時長是 45 分鐘，不能把超時計畫當成可執行方案。", "把任務拆成聽素材、找出漏聽點、核對修正三個必要環節。", "A 的 10、20、15 分鐘相加為 45，且三個環節都有安排。", "B 沒有紀錄或核對；C 未進行英文練習；D 超過時限且捨棄核對。", "逐項檢查總時數與任務是否齊全，唯一符合者是 A。"],
    },
    {
        "prompt": "小安能看懂單字，卻常把重音念錯。開始練習前，哪種資源最直接對準這個困難？",
        "options": ["只抄中文意思的筆記", "沒有聲音功能的單字清單", "附英語發音音檔、可重播並顯示音節的字典", "與單字無關的英文電影海報"], "answer": "C",
        "explanation": "C 能讓小安聽到發音、反覆比對並觀察音節；其他選項沒有提供判斷重音所需的聲音或相關資訊。",
        "strategy": "資源與弱點配對：先描述錯誤類型，再選能提供對應回饋的工具。",
        "steps": ["小安的問題不是不懂詞義，而是發音中的重音位置。", "因此需要可聽見的範例，最好還能分辨音節或重播比對。", "C 同時提供音檔、重播及音節資訊，直接支援這項練習。", "A、B 都只有文字而無聲音；D 與目標單字及發音無關。", "用「能否讓我聽見並核對重音」作最後檢查，答案是 C。"],
    },
    {
        "prompt": "小琳複習 8 個片語後，想知道自己能否在新情境中使用它們。哪個檢查最能提供證據？",
        "options": ["重看片語表並覺得眼熟", "把片語抄三遍但不遮答案", "確認自己記得課本頁碼", "遮住中文提示，抽出兩個片語各寫一個不同的新句子"], "answer": "D",
        "explanation": "D 要求不看提示回想並把片語遷移到新句子，能檢查提取與運用；眼熟、抄寫或記頁碼都不足以證明會用。",
        "strategy": "提取加遷移：暫時移除提示，再以不同語境產出可檢查的答案。",
        "steps": ["先分清楚「看過」和「能自己提取並使用」不是同一種證據。", "有效檢查應遮住提示，避免答案直接留在眼前。", "D 還要求把片語放進兩個不同新句，檢查能否遷移。", "A 只測熟悉感；B 仍看著答案抄；C 只測位置記憶。", "確認作答時沒有看中文提示且句子語意合適，選 D。"],
    },
    {
        "prompt": "怡君做英文短文題時，主旨題常答對，但時間與日期題常漏看。下週她應先怎麼調整？",
        "options": ["整份短文只重抄一次，不再看錯題", "保留主旨練習，另用短文圈出時間詞與日期並逐題核對漏看的原因", "把所有錯題都歸因於單字太難", "停止閱讀，改背與錯題無關的單字"], "answer": "B",
        "explanation": "B 保留已有效的主旨練習，同時針對可觀察的日期漏讀進行標記與原因檢查；其他選項沒有根據錯誤模式調整。",
        "strategy": "錯誤模式回饋：依錯題類型調整下一輪任務，而不是整體推倒重來。",
        "steps": ["先讀表現紀錄：主旨題已較穩，時間與日期題是明確弱點。", "調整時要把練習焦點放在時間詞、日期定位及漏看原因。", "B 同時保留有效的主旨練習，又加入針對弱點的圈記與核對。", "A 沒有診斷；C 把不同錯誤混成單一原因；D 練習內容不對應。", "比對下一週的任務是否能產生新的日期題表現證據，故選 B。"],
    },
    {
        "prompt": "美玲每天放學後有 30 分鐘可讀英文，並希望每週知道自己是否更能理解短文。哪個週計畫較可執行？",
        "options": ["每天讀同一篇直到背熟，週末不做檢查", "每天安排 90 分鐘，未完成就取消休息", "週一到週四各讀一篇短文並記下主旨與兩項線索，週五重做一篇新短文比較紀錄", "先花整週整理書桌，月底才開始讀"], "answer": "C",
        "explanation": "C 符合每日 30 分鐘限制，安排穩定練習並在週五用新短文比較理解證據；其餘不是缺少檢核，就是不符合時間條件。",
        "strategy": "週期安排與回測：把每日可用時間轉成短任務，預留新材料檢查進步。",
        "steps": ["每天上限是 30 分鐘，因此先排除每天 90 分鐘的方案。", "計畫需要在一週中分散練習，不能只重讀同一篇來製造熟悉感。", "C 將四天練習分開，並記錄主旨與兩項線索作為基準。", "週五用新短文回測，能比較理解表現而非背誦原文。", "檢查時間、持續性與週末前的證據三項條件，C 全部符合。"],
    },
    {
        "prompt": "冠宇讀完新短文後，想判斷自己是否真的學會抓主旨，而不是只記住文章內容。哪項成果最有力？",
        "options": ["不看原文，用一句話說出另一篇短文主旨，並圈出支持句", "指出新短文的頁碼", "把文章標題抄在筆記本上", "說自己讀得很快，但沒有留下答案"], "answer": "A",
        "explanation": "A 在新文本上展示主旨概括並連結支持句，能同時檢查遷移與證據；頁碼、標題抄寫或自我感覺都不能證明理解。",
        "strategy": "成果證據判讀：選能讓他人重看、核對且對準學習目標的表現。",
        "steps": ["學習目標是抓主旨，所以證據也要直接呈現主旨判斷。", "為了排除背熟原文的可能，應使用另一篇短文並不看原文。", "A 要求用一句話概括，還要指出支持句，答案可以被核對。", "B、C 只留下位置或抄寫痕跡；D 是感受，不是可檢查成果。", "確認證據同時包含新文本概括與文本依據，故選 A。"],
    },
    {
        "prompt": "子晴的週記寫著：「這週聽懂了人物和地點，但三次都漏掉集合時間；下週聽完先記下數字，再回放核對。」這段紀錄最完整地做到什麼？",
        "options": ["只寫了聽力分數，沒有指出問題", "證明她已不需要再練習", "把具體漏聽模式連到下一次可執行的策略", "把所有聽力錯誤都歸因於設備故障"], "answer": "C",
        "explanation": "C 準確連結本週具體錯誤「漏掉集合時間」與下週「先記數字、再回放核對」的調整；不是籠統分數或沒有證據的歸因。",
        "strategy": "反思轉成行動：用「已做到—卡住處—下次改法」檢查反思是否可執行。",
        "steps": ["從週記分出已理解內容、反覆出現的困難，以及下週打算。", "困難被具體描述為三次漏掉集合時間，不是泛稱聽力不好。", "下一步提出先記數字並回放核對，能直接處理時間資訊漏聽。", "A 忽略了調整；B 過度推論不用練習；D 把原因推給沒有證據的設備問題。", "核對困難與方法是否一一對應，這正是 C 所述的反思行動鏈。"],
    },
    {
        "prompt": "家豪想在兩週後回顧自己的閱讀練習。哪種紀錄最能幫他決定下一步？",
        "options": ["每天寫心情顏色，不記做了什麼", "記日期、文本類型、主旨題與細節題結果、常漏的線索和下次要試的方法", "只寫「今天有努力」", "把同學的分數抄下來當自己的進度"], "answer": "B",
        "explanation": "B 留下時間、任務、表現、錯誤模式與後續策略，兩週後可以比較並據此修正；其他紀錄缺少自己的學習證據。",
        "strategy": "歷程資料可用性：紀錄需能回答何時做了什麼、結果如何、下一步為何。",
        "steps": ["兩週後要回顧，因此紀錄必須保留可比較的日期與任務。", "只寫努力或心情，無法知道閱讀表現是否改變。", "B 也留下題型結果及常漏線索，能找出反覆出現的模式。", "同學分數不是家豪自己的學習證據，不能代替個人紀錄。", "確認紀錄包含日期、任務、結果、錯誤與下一步，答案是 B。"],
    },
    {
        "prompt": "小彤三週後要參加英文閱讀測驗；她每週可練習四次，每次 25 分鐘。哪個方案形成「計畫—檢查—調整」循環？",
        "options": ["第一週讀很多篇，之後不再查看答題狀況", "每天臨時挑最短的文章，測驗前一天才看錯題", "三週都反覆讀同一篇，最後用背出的答案當進步證明", "每週兩次限時讀新短文、一次整理錯因、一次重做相近新題；週末比較紀錄並調整下週題型比例"], "answer": "D",
        "explanation": "D 使用可行的週頻率，分配練習、診斷及新題回測，並根據週末紀錄調整下一週；其他選項沒有持續監控或把檢查結果用來修正。",
        "strategy": "循環式自我監控：預先安排練習，固定收集結果，再讓結果改變下一輪配置。",
        "steps": ["先將題目的條件列出：三週期限、每週四次、每次 25 分鐘。", "完整循環至少要有練習、錯因檢查、新題驗證和依結果修正。", "D 把四次分別配置給新短文、錯因整理與相近新題，且安排週末比較。", "A、B 沒有定期查看並調整；C 用重複熟悉取代新題表現證據。", "逐項確認時間沒有超限，而且每週結果會影響下週安排，故選 D。"],
    },
]


def reference(source):
    return {
        "url": source["url"],
        "title": source["title"] + "；只參照指定題目中的排程／建議理解型態，本題內容全新創作。",
        "year": source["year"],
        "subject": "english",
        "locator": source["locator"],
        "observedPattern": source["observedPattern"],
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


for number, item in enumerate(ITEMS, 1):
    refs = [reference(source) for source in SOURCES]
    payload = {
        "id": f"question-english-performance-7-iv-5-{number}",
        "subject": "english",
        "type": "single-choice",
        "prompt": item["prompt"],
        "options": [{"id": chr(65 + i), "text": value} for i, value in enumerate(item["options"])],
        "knowledgeIds": ["kg-english-performance-7-iv-5"],
        "difficulty": "medium",
        "answer": {"value": item["answer"], "explanation": item["explanation"]},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCES[0]["url"],
            "sourceLocator": "以三所公立國中公開英文試題之讀表、時間安排與建議理由判讀模式作 pattern-only 參照；題幹、人物、時間、選項、答案與解說均另行創作。",
            "authoringNote": "依官方課綱能力及三所公立學校公開原卷的可追溯題型重新撰寫；未複製原題、選項、答案、文章或圖像。內容維持 draft，完整課程融合與發布審查尚未完成。",
        },
        "reviewStatus": "draft",
        "updatedAt": TODAY,
        "lessonId": "lesson-english-performance-7-iv-5",
        "examPatternRefs": refs,
        "solutionStrategy": item["strategy"],
        "solutionSteps": item["steps"],
    }
    (OUT / f"question-english-performance-7-iv-5-{number}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

# Register the three verified public-school exam records in the canonical
# provenance registry; retain existing source entries unchanged.
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
known = {row.get("questionUrl") for row in registry["sources"]}
for source in SOURCES:
    if source["url"] in known:
        continue
    registry["sources"].append({
        "id": f"english-7-iv-5-{source['year'].replace('-', '-')}-{source['school'].replace(' ', '').replace('市立', '').replace('國民中學', '').replace('國民', '')}",
        "school": source["school"],
        "grade": source["grade"],
        "subject": "english",
        "exam": source["exam"],
        "questionUrl": source["url"],
        "answerLocator": source["answerLocator"],
        "usePolicy": "只參照此公開原卷指定題目的時間表／建議理解方式，所有題幹、選項、答案、文章及圖像均獨立創作，不重製原卷。",
        "verifiedAt": TODAY,
    })
registry["updatedAt"] = TODAY
REGISTRY.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unit": "7-Ⅳ-5", "rewritten": len(ITEMS), "answerKey": [item["answer"] for item in ITEMS], "schools": [source["school"] for source in SOURCES]}, ensure_ascii=False))
