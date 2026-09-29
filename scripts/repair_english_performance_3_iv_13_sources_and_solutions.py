import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"

GUOCHANG = "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E.pdf"
YANCHENG = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf"
NEIHU = "https://www.nhjh.tp.edu.tw/uploads/1706770089045DwNPg1SE.pdf"

SCHOOL = {
    GUOCHANG: ("高雄市立國昌國中110學年度第二學期二年級第二次段考英文科", "110-2"),
    YANCHENG: ("高雄市立鹽埕國中114學年度第二學期三年級第一次段考英文科", "114-2"),
    NEIHU: ("臺北市立內湖國中112學年度第一學期七年級第三次段考英文科（康軒版）", "112-1"),
}

# Every locator was matched to the public school's original exam and selected for
# the reading operation being rewritten; no original question text is reused.
REFS = {
    1: [(GUOCHANG, "試卷第5頁第30題：依人物行動與故事情節配對評論"), (YANCHENG, "試卷第3頁第39–44題：整合日記敘事與事件理解"), (NEIHU, "試卷第4頁第49題：核對閱讀敘述是否符合原文")],
    2: [(GUOCHANG, "試卷第5頁第30題：辨認評論所描述的故事角色與行動"), (YANCHENG, "試卷第3頁第45–47題：從對話輪替判斷人物回應"), (NEIHU, "試卷第4頁第50題：依人物情境線索選擇合宜行動")],
    3: [(YANCHENG, "試卷第3頁第45–47題：辨識對話發話者及其言談脈絡"), (GUOCHANG, "試卷第5頁第30題：由故事動作線索判斷角色行為"), (NEIHU, "試卷第4頁第50題：依敘事中的角色行動選擇後續處置")],
    4: [(YANCHENG, "試卷第3頁第45–47題：依對話內容理解人物意圖與回應"), (GUOCHANG, "試卷第5頁第30題：比對故事行動與人物評論"), (NEIHU, "試卷第4頁第50題：由公告情境推得人物可採取的行動")],
    5: [(YANCHENG, "試卷第3頁第39–44題：辨認日記敘事中的家庭關係與情緒張力"), (GUOCHANG, "試卷第5頁第30題：依故事角色行動辨別評論內容"), (NEIHU, "試卷第4頁第50題：從情境問題辨認待解決行動")],
    6: [(YANCHENG, "試卷第3頁第39–44題：按日記內容追蹤事件與時間線索"), (GUOCHANG, "試卷第5頁第30題：依故事事件判斷評論指涉情節"), (NEIHU, "試卷第4頁第50題：依故事情境判斷下一個可行動作")],
    7: [(YANCHENG, "試卷第3頁第39–44題：綜合敘事前後訊息推斷人物感受"), (GUOCHANG, "試卷第5頁第31題：根據多項敘事線索推測人物特質"), (NEIHU, "試卷第4頁第50題：由故事條件推論角色後續行動")],
    8: [(GUOCHANG, "試卷第6頁第34–35題：由詩歌意象與整體語氣判斷傳達訊息"), (YANCHENG, "試卷第3頁第39–44題：從重複敘事線索理解人物重視的事物"), (NEIHU, "試卷第4頁第49題：以文本明示內容檢驗解讀")],
    9: [(GUOCHANG, "試卷第6頁第35題：判斷短詩希望傳達的核心訊息"), (YANCHENG, "試卷第3頁第43–44題：由敘事末段核對人物態度與期待"), (NEIHU, "試卷第4頁第49題：依全文證據辨認正確理解")],
    10: [(GUOCHANG, "試卷第5頁第30–33題：整合故事、評論與後續敘事細節"), (YANCHENG, "試卷第3頁第39–47題：連結敘事事件、人物態度與對話"), (NEIHU, "試卷第4頁第48–50題：整合人物指涉、明示細節與情境行動")],
}

ITEMS = {
    1: {
        "key": "C",
        "explanation": "正確答案：C。短劇從發現錢包開始，角色沒有把它占為己有，而是找辦公室協助，最後讓失主取回。推動情節的是誠實與合作；選項 C 抓到這條行動與結果的主線。",
        "strategy": "主旨題要把角色採取的關鍵行動和結局連起來，再用能涵蓋兩者的概念概括；不要被單一場景或道具帶偏。",
        "steps": ["先找短劇起點：兩位學生發現遺失的錢包。", "追蹤他們遇到問題後採取的做法：向辦公室求助，而非藏起來。", "確認結尾如何收束：錢包回到失主手中。", "把行動與結果連成主旨：誠實地合作處理失物。", "選 C；賽跑、制服和藏匿都沒有出現在劇情因果線上。"],
    },
    2: {
        "key": "B",
        "explanation": "正確答案：B。Alex 手持剪貼板，並逐一要求組員在報告前交出進度；這些任務分配與追蹤行為支持「統整團隊報告的組長」身分，不是顧客、旅客或演奏者。",
        "strategy": "判讀角色身分時，把道具當輔助線索、把角色正在做的事當主要證據；再檢查候選身分能否解釋整個行動。",
        "steps": ["圈出與角色直接相連的兩項線索：clipboard 和 asks each team member for a report。", "注意事情發生在 presentation 之前，顯示他正在整合小組工作。", "把『統整進度、要求回報』與組長職責配對。", "排除餐廳點餐、車站迷路及調音，因為劇本沒有相應對象或行動。", "選 B：角色功能由組織組員與收集報告的行為判定。"],
    },
    3: {
        "key": "D",
        "explanation": "正確答案：D。方括號中的文字不是 Mia 說出口的台詞，而是演員可執行的舞台指示：她望向暗窗並往後退。這提供視線方向和身體動作，不會告訴演員吃什麼或觀眾何時離場。",
        "strategy": "劇本中的括號或方括號動作要和角色台詞分開讀；把動詞轉成舞台上可看見的動作，避免把未寫出的原因自行補進去。",
        "steps": ["辨認方括號格式，判斷這句是舞台指示而非角色對白。", "找兩個可演出的動作：points to the dark window 與 steps back。", "分別轉成演員的視線方向和移動方式。", "檢查選項是否只說明文字明示的動作，不延伸到飲食或觀眾安排。", "選 D：指示告訴演員 Mia 看向哪裡、如何移動。"],
    },
    4: {
        "key": "A",
        "explanation": "正確答案：A。Sam 用 If 引出「現在離開就趕得上末班車」的理由，目的在說服同伴及時出發。句子提出可採取的選擇與後果，不是在教修火車，也沒有宣布車站永久關閉。",
        "strategy": "對話目的題先看說話者提出了什麼行動，再看 if／so／because 等連接詞如何把行動和後果連起來；用語用功能判斷，不只翻譯字面。",
        "steps": ["標出 Sam 的提議：leave now。", "讀完條件句的結果：仍能 catch the last train。", "判斷這個理由想讓聽者做什麼：現在動身。", "比較選項的溝通目的，只有勸大家及時離開符合提議與後果。", "選 A；修理、道歉與永久封站都沒有語句證據。"],
    },
    5: {
        "key": "C",
        "explanation": "正確答案：C。兩位朋友都在談班級的錢，但一人想買禮物、一人想留作緊急用途；衝突不是不認識學校或天氣，而是對同一筆錢的用途有不同主張。",
        "strategy": "找衝突時，把角色各自想要的結果並排，再找兩者無法同時滿足的決策點；共同背景不是衝突本身。",
        "steps": ["分別寫下第一位朋友的目標：把錢用於班級禮物。", "再寫第二位朋友的目標：保留緊急備用金。", "比較兩個目標是否能同時使用同一筆有限的錢。", "將爭議聚焦在決策內容，而非無關的校名、劇本或天氣。", "選 C：他們對錢應如何使用意見不同，這就是場景的核心衝突。"],
    },
    6: {
        "key": "B",
        "explanation": "正確答案：B。題目明確給出順序：lights go out、characters use a phone light、then discover the fuse switch。第二個事件就是使用手機照明；找到保險絲開關是第三步，停電是第一步。",
        "strategy": "事件順序題把每個動作寫成時間線節點，再依 then／after／before 等順序標記定位；不要把重要結果誤當成第二件事。",
        "steps": ["把場景中三個動作分開：停電、打開手機照明、找到保險絲開關。", "依照敘述連接詞先排列第一個動作。", "接著讀 the characters use a phone light，將它放在第二格。", "確認 discover the fuse switch 發生在 then 之後，是下一個動作。", "選 B：手機照明位於停電之後、找到開關之前。"],
    },
    7: {
        "key": "D",
        "explanation": "正確答案：D。開頭的 Lily 因犯錯而小聲說話；結尾她主動志願向全班解釋解法。由退縮轉為主動公開表達，顯示她更有信心。文本沒有說她變成老師或忘記事件。",
        "strategy": "分析人物改變要比較同一角色在前後場景的可觀察言行；用差異支持性格或信心變化，不以單一形容詞代替證據。",
        "steps": ["抓開頭狀態：犯錯後 Lily 說話很小聲。", "抓結尾行動：她主動舉手志願說明解法。", "比較兩個時點的參與程度，而不是只看其中一幕。", "由退縮到主動承擔公開說明，推得信心提升。", "選 D；角色仍是 Lily，且故事沒有說她放棄溝通。"],
    },
    8: {
        "key": "A",
        "explanation": "正確答案：A。圍巾每次在有人答應幫忙時交到下一位角色手上，反覆出現的動作把它和互助承諾連在一起。這個象徵解讀能解釋道具為何被傳遞；其他選項與場景無關。",
        "strategy": "道具象徵要從它重複出現的時機和角色如何使用推論；結論必須能解釋這個重複模式，不能只憑顏色聯想。",
        "steps": ["找出圍巾反覆出現的時刻：有人同意提供幫助時。", "注意它被交給下一位角色，表示意義跨越單一人物。", "把道具行動和角色承諾互相比對，找能解釋重複規律的意思。", "排除水下場景、取代台詞或烹飪等沒有劇本線索的選項。", "選 A：圍巾標記大家共同接力幫忙的承諾。"],
    },
    9: {
        "key": "C",
        "explanation": "正確答案：C。結尾直接說 We solved it because we listened to one another，把問題解決與彼此傾聽連在一起。最穩妥的主題是傾聽促成合作解決問題，不是問題不存在或大家停止說話。",
        "strategy": "結局主題題先找最後一句的因果或評語，再回看它能否概括整段衝突與解決方式；不要把角色的話擴大成文本沒有支持的絕對結論。",
        "steps": ["鎖定最後一句中的因果詞 because。", "找出結果 solved it 與原因 listened to one another。", "回想前文存在待解決的問題，確認結尾是在總結解決方式。", "排除『問題不是真的』和『再也不交談』等與結尾相反的說法。", "選 C：故事強調互相聆聽有助於解決問題。"],
    },
    10: {
        "key": "B",
        "explanation": "正確答案：B。完整摘要須保留失蹤布條引發調查、角色面臨是否指責同學的倫理分歧、最後在美術教室找到布條並道歉修復關係。B 涵蓋問題、選擇與結果，沒有把情節順序顛倒。",
        "strategy": "整合劇情摘要可用「問題—角色選擇—結果」三段核對；只提道具或場景太窄，漏掉衝突與結局就會失真。",
        "steps": ["先界定起始問題：班級布條不見了，學生開始查線索。", "保留中段關鍵抉擇：是否在證據不足時責怪某位同學。", "讀結局確認布條在美術教室找到，並有人道歉。", "檢查摘要是否同時包含調查、公平選擇、發現與信任修復。", "選 B：它忠實串起主要事件與關係結果，其他選項漏情節或顛倒順序。"],
    },
}


def make_ref(url: str, locator: str) -> dict:
    title, year = SCHOOL[url]
    return {
        "url": url,
        "title": title,
        "year": year,
        "subject": "english",
        "locator": locator,
        "observedPattern": f"公開原卷{locator}；只參照人物／敘事／對話判讀能力，不沿用原題情境、文字、選項或答案。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


for number, item in ITEMS.items():
    path = OUT / f"question-english-performance-3-iv-13-{number}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    options = data["options"]
    correct = next(option for option in options if option["id"] == data["answer"]["value"])
    distractors = [option for option in options if option is not correct]
    target = ord(item["key"]) - ord("A")
    ordered = distractors[:target] + [correct] + distractors[target:]
    data["options"] = [{"id": chr(ord("A") + index), "text": option["text"]} for index, option in enumerate(ordered)]
    data["answer"] = {"value": item["key"], "explanation": item["explanation"]}
    data["solutionStrategy"] = item["strategy"]
    data["solutionSteps"] = item["steps"]
    refs = REFS[number]
    data["examPatternRefs"] = [make_ref(url, locator) for url, locator in refs]
    data["provenance"]["sourceUrl"] = refs[0][0]
    data["provenance"]["sourceLocator"] = "；".join(locator for _, locator in refs)
    data["provenance"]["authoringNote"] = "本題短劇情境、角色行動、選項與繁中詳解均為原創；公立學校公開試題只作人物／敘事／對話理解的 pattern-only 參照，未複製原題或答案。維持 draft；依使用者指示不安排 Terra 審查。"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote answers, explanations, strategies, steps, and exact exam locators for {len(ITEMS)} items")
