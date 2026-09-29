#!/usr/bin/env python3
"""Replace generic English role-play questions with original, sourced items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DASHE = "https://www.dam.kh.edu.tw/upload/68/101_28414/%E4%BA%8C%E5%B9%B4%E7%B4%9A%28%E8%87%AA%E7%84%B6.%E6%AD%B7%E5%8F%B2.%E5%9C%B0%E7%90%86.%E5%85%AC%E6%B0%91.%E8%8B%B1%E8%81%BD.%E6%95%B8%E5%AD%B8%29.pdf"
DAGANG = "https://web.dgjh.tyc.edu.tw/asp/exam/upload/100%E5%AD%B8%E5%B9%B4%E5%BA%A6%E5%85%AB%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%9C%88%E8%80%83%E5%AD%B8%E7%94%9F%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf"
DAWAN = "https://www.dwm.kh.edu.tw/upload/344/104_64184/113%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf"
SOURCES = {
    DASHE: ("高雄市立大社國中", "103學年度第二學期第一次段考八年級英語科聽力試卷", "只參考基本問答第6至10題依對話脈絡選擇合宜回應的任務形式；未複製原對話、選項或答案。"),
    DAGANG: ("桃園市立大崗國中", "100學年度上學期八年級第二次月考英文科考題", "只參考聽力第6至10題依說話目的選擇合宜回應的任務形式；未複製字詞、對話、選項或答案。"),
    DAWAN: ("高雄市立大灣國中", "113學年度第一學期八年級英語科第一次段考", "只參考聽力第5、6、10題的對話理解與合宜回應任務形式；未複製原卷對話、選項或答案。"),
}

ITEMS = [
    {"answer":"C","source":(DASHE,8,"basic-response question 8"),"prompt":"At a café, your drink arrives with dairy milk, but you ordered oat milk. What should you say first to the server?","options":[("A","This café is always crowded."),("B","I will order a cake next time."),("C","I asked for oat milk, but this contains dairy. Could you remake it, please?"),("D","My friend likes this table.")],"explanation":"C 先指出飲品與原訂內容的差異，再提出可執行的更換請求並保持禮貌；其他選項沒有處理送錯飲料。店員可據此核對訂單並立即採取更換，而不必猜測顧客期待。","strategy":"角色扮演遇到服務問題時，先描述可核對的事實，再提出明確、可行且不責怪對方的修正要求。","steps":["你扮演顧客，眼前的任務不是評論咖啡店，而是修正牛奶種類錯誤。","把已知事實說清楚：原本點燕麥奶，現在拿到的飲品含乳製品；店員才能核對訂單。","接著提出 remake 請求，讓服務人員知道具體要採取什麼行動，而非只表達不滿。","C 同時包含差異、處理要求與 please；A、B、D 都偏離送錯飲品這個問題。","選 C；若店員確認訂單，再簡短回答即可，避免重複抱怨而沒有推進解決。"]},
    {"answer":"A","source":(DAWAN,10,"basic-response question 10"),"prompt":"You are the librarian on duty. A student needs a book for a report but knows only the topic, not the title. Which response moves the search forward?","options":[("A","Tell me the topic, and I can help you search the catalogue."),("B","You should already know the title."),("C","The library closes yesterday."),("D","I borrowed that book last month.")],"explanation":"A 先詢問目前已知的主題，再提供可立即進行的館藏查詢協助，符合圖書館員的角色與學生需求。它運用學生已掌握的線索，並給出可以立刻執行的下一步。","strategy":"扮演協助者時，回應要接住對方已提供的線索，並提出下一個能實際縮小搜尋範圍的問題或行動。","steps":["說話者是值班館員，對方需要為報告找書，但尚未知道書名；搜尋仍可從主題開始。","因此不應要求學生提供他目前沒有的資訊，而要利用已知的主題開始查找。","A 請學生說出主題，並提出搜尋 catalogue 的下一步，角色職責與任務一致。","B 責備學生；C 的時間資訊不合理且無關；D 談館員自己的借閱經驗，沒有協助搜尋。","選 A；學生接著提供主題後，館員便能示範關鍵字搜尋或分類查詢。"]},
    {"answer":"D","source":(DAGANG,6,"listening appropriate-response question 6"),"prompt":"In a clinic role-play, the doctor asks when your sore throat began and whether you have had a fever. Which answer gives the most useful information?","options":[("A","I usually take the bus to school."),("B","My cousin likes warm soup."),("C","The clinic is near the station."),("D","It started yesterday, and I had a fever last night.")],"explanation":"D 回答症狀開始時間及是否發燒，直接提供醫師詢問的兩項健康資訊；其餘選項均未回答問題。這些可觀察線索能幫助醫師了解症狀經過，並不是患者自行診斷。","strategy":"醫療情境依對方問的症狀線索回答，按時間或變化提供可觀察資訊，不自行替自己下診斷。","steps":["醫師問了兩件事：喉嚨痛何時開始，以及最近是否發燒；兩部分都要回應。","先按時間交代症狀起點，再補充是否出現發燒，讓回答與問題一一對應。","D 的 yesterday 和 last night 提供清楚時間線，也沒有把症狀推論成疾病名稱。","A、B、C 分別談交通、親友偏好及地點，沒有提供患者狀況或回答醫師問題。","所以選 D；若醫師再詢問程度或其他症狀，再依實際感受補充，不猜測病因。"]},
    {"answer":"B","source":(DASHE,9,"basic-response question 9"),"prompt":"You are a visitor at a station and cannot find the museum train. Which opening best helps the information-desk worker guide you?","options":[("A","Museums are interesting places."),("B","Could you tell me which platform the museum train leaves from?"),("C","I bought a ticket last week."),("D","The weather may be sunny tomorrow.")],"explanation":"B 清楚指出需要的資訊是月台，並以禮貌問句向服務人員求助；其他選項沒有提出可回答的問路需求。旅客同時給出目的地與明確問題，站務人員便能提供可行動的方向。","strategy":"問路時先說明要找的交通工具或目的地，再把需要對方提供的資訊問得具體，避免只說迷路卻沒有可回答的焦點。","steps":["你扮演旅客，已知道要搭往博物館的列車，缺少的是發車月台；問題焦點要鎖定在此。","問句應把列車目的地與所需資訊 platform 一起說出，讓站務人員能直接回答。","B 用 Could you tell me…? 緩和請求，也明確詢問月台。","A 是一般評論，C 是過去購票經驗，D 談天氣；它們都沒有推進找車任務。","選 B；聽到月台後可再確認方向或班次，確保下一步資訊足以行動。"]},
    {"answer":"A","source":(DAWAN,5,"listening basic-response question 5"),"prompt":"As class representative, you must tell classmates that the science meeting has moved from Room 204 to Room 310 at 3:30. Which announcement is complete?","options":[("A","The science meeting is now in Room 310 at 3:30, not Room 204."),("B","The science meeting is interesting."),("C","Meet me somewhere after school."),("D","Room 204 was painted last year.")],"explanation":"A 保留活動名稱、新地點、時間與舊地點更正，讓同學可以據此前往正確教室。明確標出舊安排已被取代，能避免同學仍依記憶走到 Room 204。","strategy":"轉述活動異動時逐項核對事件、最新地點與時間；若舊資訊已流傳，明說替代關係以免聽者沿用舊地點。","steps":["班代的責任是讓同學收到能採取行動的最新安排，不是只傳達會議存在。","必要資訊包含 science meeting、Room 310 及 3:30；缺任一項都可能讓同學走錯或遲到。","由於有人可能記得原教室 Room 204，還要清楚說明新地點取代舊地點。","A 包含全部欄位和 not 的更正關係；B、C、D 缺少關鍵安排或只談無關內容。","因此選 A；公告後可以請同學複述教室與時間，檢查訊息是否傳達成功。"]},
    {"answer":"C","source":(DAGANG,7,"listening appropriate-response question 7"),"prompt":"You work at a shop. A customer likes a jacket but says the price is over their budget. What is the most helpful reply?","options":[("A","Then you should not shop here."),("B","That jacket is blue."),("C","What price range works for you? I can show you a similar option."),("D","The store opened ten years ago.")],"explanation":"C 先尊重顧客的預算限制，再詢問可接受範圍並提出替代選項，對話因此能繼續解決需求。這種回應不預設顧客可以加價，也保留由顧客決定的空間。","strategy":"角色回應須回應對方剛提出的限制；先澄清條件，再提出匹配方案，不要否定需求或只重複商品資訊。","steps":["顧客的核心訊息是喜歡外套但價格超出預算，價格限制是目前要處理的條件。","店員先詢問可接受的區間，就能縮小候選商品，而非擅自假設顧客願意加價。","C 也提出展示相似款，讓對話從問題走向可選方案，並由顧客比較後決定。","A 帶有排斥語氣，B 只重複顏色，D 提供店史，都沒有回應預算。","選 C；接著店員應依顧客提供的範圍介紹商品，並讓顧客自行比較。"]},
    {"answer":"D","source":(DAWAN,6,"listening basic-response question 6"),"prompt":"Your partner thinks the picnic invitation is for Saturday, but you meant Sunday afternoon at the riverside park. How should you repair the misunderstanding?","options":[("A","You never listen to me."),("B","Picnics are fun in every season."),("C","I already bought a blue backpack."),("D","Sorry, I meant Sunday afternoon at Riverside Park. Does that work for you?")],"explanation":"D 不責怪對方，而是重述正確日期和地點，再確認對方是否能配合，完整修復了邀請資訊。確認問題能檢查雙方是否已對新安排取得共識，避免誤解延續。","strategy":"發現誤解時先用中性語氣標示修正，再重述缺漏的時間／地點，最後用確認問題檢查雙方是否同步。","steps":["誤會涉及兩個可核對欄位：日期從 Saturday 改為 Sunday，地點是 Riverside Park。","用 Sorry, I meant… 標示自己要澄清，而不是直接指責對方沒聽清楚，讓修補保持合作。","D 補齊 Sunday afternoon 和 Riverside Park，避免只改正其中一項。","句末 Does that work for you? 邀請對方確認行程是否可行，讓雙方達成共識。","因此選 D；若對方時間不合，再協商新時段，而不假設邀請已被接受。"]},
    {"answer":"B","source":(DASHE,7,"basic-response question 7"),"prompt":"You notice water spreading across a classroom walkway. As a student in the role-play, what should you say and do first?","options":[("A","Let us race across it."),("B","Please stay back—the floor is wet. I’ll tell the teacher now."),("C","The floor looks shiny."),("D","I will clean it with my bare hands.")],"explanation":"B 先提醒同學避開濕滑區域，再通知教師處理，兼顧即時安全與合適的求助對象。先降低碰撞或滑倒風險，再交由能安排清理的人員處理，較符合學生角色。","strategy":"遇到可能造成受傷的校園狀況，先降低眼前風險，再交由負責成人處理；不要逞強或只描述現象。","steps":["場景裡水正在擴散到走道，最迫切的目標是避免有人滑倒，因此安全優先於清理。","第一句要讓附近同學立刻停下並避開濕地，而不是邀請他們靠近或跨過去。","接著通知教師，由適當負責人安排清理或設置警示，學生不必徒手處理。","B 有清楚警告和求助行動；A 增加危險，C 只有觀察，D 讓學生徒手處理並不妥當。","選 B；通報時再補充位置與水量，讓老師能快速找到並處理危險。"]},
    {"answer":"A","source":(DAGANG,8,"listening appropriate-response question 8"),"prompt":"You are interviewing a visiting student about a school club. After asking what activity they enjoy most, what should the interviewer do?","options":[("A","Listen to the answer, then ask one relevant follow-up."),("B","Answer the question for the guest."),("C","Immediately ask an unrelated question."),("D","Repeat the same question louder before the guest can speak.")],"explanation":"訪談者提問後要留出回答空間，聽取內容，再沿著受訪者提供的資訊追問，才能形成真正的互動。追問須承接來訪學生實際提供的線索，而非照稿繼續提出無關問題。","strategy":"角色扮演對話不能只輪流念預寫句子；聽對方答案後選擇相關追問，才能讓後續內容接得上。","steps":["訪談者已提出 club activity 的開放問題，現在輪到來訪學生回答，發言權暫時交給對方。","先停下來聽完整答案，不要替對方回答或用新問題蓋過發言；這樣才有可追問的資訊。","從回答中選一個具體線索，例如活動方式或原因，再提出相關追問。","A 保留對方的發言輪次，也讓訪談沿著受訪者真正說出的資訊發展。","所以選 A；演練時可用對方答案中的一個詞組成 follow-up，檢查自己是否確實有聽。"]},
    {"answer":"C","source":(DASHE,10,"basic-response question 10"),"prompt":"At a hotel desk, your key card no longer opens the room and you also need to know when breakfast starts. Which request handles both needs clearly?","options":[("A","Breakfast is my favorite meal."),("B","My room has a large window."),("C","My key card won’t open the door. Could you replace it? Also, what time does breakfast begin?"),("D","I stayed here with my family years ago.")],"explanation":"C 先報告房卡故障並提出更換需求，再另問早餐時間；兩個目的分開表達，櫃台可逐一處理。Also 清楚引出第二項詢問，避免接待人員以為房卡問題是唯一需求。","strategy":"一個情境包含兩項任務時，先分成問題處理與資訊詢問，再用清楚連接語逐一提出，避免漏掉其中一件。","steps":["旅客同時需要立即恢復進房，以及安排隔日早餐時間，兩項需求性質不同，不能只處理其一。","第一句說明房卡無法開門，接著提出 replacement 的可執行請求。","用 Also 開啟第二個問題，明確詢問早餐開始時間，並把兩項需求分開。","C 依序涵蓋故障、處置和時刻資訊；A、B、D 都只提供背景或偏好，沒有提出櫃台可處理的請求。","選 C；櫃台回覆後分別確認新卡是否可用，以及早餐時間，避免只完成一半。"]},
]


def make_ref(url: str, number: int, locator: str) -> dict:
    school, exam, boundary = SOURCES[url]
    year = {DASHE:"103-2", DAGANG:"100-1", DAWAN:"113-1"}[url]
    return {"url":url,"title":f"{school}{exam}","year":year,"subject":"english","locator":locator,"observedPattern":f"只參考第{number}題依對話內容選擇合宜回應的任務形式；{boundary}","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"item"}


def main() -> None:
    paths=[ROOT/f"questions/english/question-english-performance-2-iv-9-{n}.json" for n in range(1,11)]
    if len(ITEMS)!=10 or any(not p.is_file() for p in paths):
        raise FileNotFoundError("Expected ten stable question IDs; no writes performed")
    for path,item in zip(paths,ITEMS,strict=True):
        data=json.loads(path.read_text(encoding="utf-8")); url,n,locator=item["source"]
        data["prompt"]=item["prompt"]
        data["options"]=[{"id":k,"text":v} for k,v in item["options"]]
        data["answer"]={"value":item["answer"],"explanation":item["explanation"]}
        data["examPatternRefs"]=[make_ref(url,n,locator)]
        data["solutionStrategy"]=item["strategy"]; data["solutionSteps"]=item["steps"]
        data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":url,"sourceLocator":f"{SOURCES[url][0]}公開試卷 {locator}；僅參照對話回應任務型態，不重製原卷。","authoringNote":"依官方英語課綱、Knowledge Graph 與公立學校公開英語試題 item-level pattern-only 任務證據獨立創作，未複製原題、選項或答案；題目維持 draft，尚待版本研究與完整內容發布審查。"}
        data["reviewStatus"]="draft"; data["updatedAt"]="2026-09-24"
        path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    catalog_path=ROOT/"implementation/reports/public-exam-source-catalog.json"
    catalog=json.loads(catalog_path.read_text(encoding="utf-8"))
    for url,(school,title,boundary) in SOURCES.items():
        entry={"institution":school,"url":url,"subjects":["english"],"availableMaterial":title,"researchUse":"英語2-Ⅳ-9角色目的辨識、合宜回應、澄清誤解、安全通報與訪談輪流；逐題 pattern-only，不複製考題。","licenseBoundary":boundary}
        row=next((r for r in catalog["sources"] if r.get("url")==url),None)
        if row: row.update(entry)
        else: catalog["sources"].append(entry)
    catalog["questionSourceUrls"]=sorted({r["url"] for r in catalog["sources"] if r.get("url")})
    catalog_path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"rewritten":len(ITEMS),"allRemainDraft":True,"sourceSchools":len(SOURCES)},ensure_ascii=False))


if __name__=="__main__": main()
