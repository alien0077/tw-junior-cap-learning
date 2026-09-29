import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-6-iv-4"
KG = "kg-english-performance-6-iv-4"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "title": "高雄市立鹽埕國民中學114學年度第2學期第1次段考三年級英文科", "year": "114-2"},
    {"url": "https://jweb.kl.edu.tw/userfiles/1389/document/40425_%E5%85%AB%E5%B9%B4%E7%B4%9A1%E6%AE%B5%E8%8B%B1%E6%96%87.pdf", "title": "基隆市立武崙國中111學年度第2學期八年級第1次段考英文科", "year": "111-2"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E8%AA%9E.pdf", "title": "高雄市立國昌國民中學110學年度第1學期七年級英文科第1次段考", "year": "110-1"},
]

def refs():
    patterns = [
        ("PDF第1頁聽力第6至15題；依圖像題及短對話題型定位", "英文評量以圖像線索與短對話搭配，要求比對視覺訊息、語句細節與情境推論；此處只研究多模態作答形式。"),
        ("聽力測驗第一部分辨識句意第1至5題及圖像情境題", "圖像與簡短口語訊息需交叉比對，不能只依單一線索猜測；站內另製作圖表、地圖與標籤素材。"),
        ("PDF第1頁圖片判讀第1題；第2頁表格資料題第30至31題", "評量結合圖片、表格與短文資料要求抽取明確資訊；本站情境、數值與答案均重新創作。"),
    ]
    return [{**s, "subject": "english", "locator": patterns[i][0], "observedPattern": patterns[i][1], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "page" if i != 1 else "paper"} for i, s in enumerate(SOURCES)]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-english-performance-6-iv-4-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "參考鹽埕、武崙、國昌公校英文試卷中的圖像理解、資料表閱讀及情境推論題型；未複製原題或選項。", "authoringNote": "依官方課綱與多元素材閱讀能力獨立創作素材描述、選項、答案與詳解；公校試題只作題型研究，維持 draft 待後續內容及版權 QA。"}, "reviewStatus": "draft", "updatedAt": "2026-09-27", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "A school infographic shows three icons: a bus, a clock, and a rain cloud, with the note 'Leave 15 minutes earlier on rainy days.' What is its main purpose?", {"A": "To give travel advice for rainy days.", "B": "To describe three kinds of clouds.", "C": "To sell a new bus.", "D": "To report yesterday's temperature."}, "A", "The icons and note connect rain, travel, and an earlier departure, so the infographic gives practical travel advice.", "整合圖示與文字的共同訊息，再判斷素材的功能而非只看單一圖示。", ["找出三個圖示與 note 的關聯。", "將 rainy days、leave earlier 與交通行動連起來。", "檢查 A 是否涵蓋圖示支持的實用建議。", "排除 B、C、D，因為素材沒有雲種類、商品或昨日溫度資料。", "選 A，確認目的由圖文共同證明。"], "easy"),
make(2, "A map legend says: '★ = drinking water; dotted line = 500-meter walking path.' What does the star show?", {"A": "A place to get drinking water.", "B": "The longest walking path.", "C": "A closed road.", "D": "The map's publication date."}, "A", "The legend explicitly defines the star as drinking water, so A is a direct map-reading answer.", "先讀圖例再看地圖符號，不用符號外形自行猜測。", ["定位 map legend，確認它是符號意義的主要證據。", "圈出 ★ = drinking water。", "將星號與 A 的地點功能對應。", "排除 B、C、D，因為 dotted line 或日期才可能涉及其他資訊。", "選 A，回讀圖例確認符號含義。"], "easy"),
make(3, "A menu lists: 'Vegetable soup $40, Chicken rice $75, Fruit cup $35.' Which item is the cheapest?", {"A": "Fruit cup", "B": "Vegetable soup", "C": "Chicken rice", "D": "All three cost the same."}, "A", "Fruit cup costs $35, less than $40 and $75, so it is the cheapest item.", "把菜單文字轉成價格比較，先讀單位再找最小值。", ["列出三個品項與價格。", "比較 40、75、35 的數值大小。", "確認最小價格 35 對應 Fruit cup。", "排除 soup、chicken rice 與相同價格的說法。", "選 A，回查品項與價格沒有對調。"], "easy"),
make(4, "A short podcast transcript says, 'First, put the seeds in wet cotton. After three days, move them to soil.' What should happen after three days?", {"A": "Move the seeds to soil.", "B": "Put the seeds in wet cotton for the first time.", "C": "Throw away the soil.", "D": "Record a weather forecast."}, "A", "After three days introduces the second step: moving the seeds from wet cotton to soil.", "用轉折時間詞與流程動詞重建音訊文字稿的事件順序。", ["圈出 First 與 After three days。", "建立第一步 wet cotton、第二步 soil 的時間線。", "檢查 A 是否完整重述第二步。", "排除 B、C、D，因為它們顛倒流程或無關。", "選 A，確認順序與原文字稿一致。"], "easy"),
make(5, "A comic shows a student looking at a full trash bin and saying, 'Let's use the recycling boxes next time.' What problem is the comic highlighting?", {"A": "Trash is being placed without enough recycling.", "B": "The school has too many science books.", "C": "Students cannot find the bus stop.", "D": "The recycling boxes are selling food."}, "A", "The full trash bin and suggestion to use recycling boxes point to a waste-sorting problem.", "整合漫畫畫面與對白，找出它們共同指向的問題。", ["先觀察畫面 full trash bin。", "再讀對白 use the recycling boxes。", "將兩項線索連成垃圾分類不足的問題。", "排除 B、C、D，因為漫畫沒有教材、交通或販售證據。", "選 A，確認圖像與語句互相支持。"], "medium"),
make(6, "A product label says: 'Keep refrigerated. Best before June 12.' What information is most important before eating it?", {"A": "Check that it has been kept cold and is before June 12.", "B": "Count the letters on the label.", "C": "Place it in direct sunlight.", "D": "Ignore the date if the package is colorful."}, "A", "The label gives storage and date limits, so both refrigeration and the best-before date should be checked.", "把標籤上的兩項安全條件轉成食用前的檢查行動。", ["圈出 Keep refrigerated 與 Best before June 12。", "將兩句分別轉成保存與日期檢查。", "確認 A 同時保留冷藏與期限。", "排除 B、C、D，因為它們忽略或違反標籤資訊。", "選 A，回讀確認兩個安全條件都被處理。"], "medium"),
make(7, "A bar chart shows library visits: Monday 12, Tuesday 18, Wednesday 15. Which statement is supported?", {"A": "Tuesday had the most visits.", "B": "Monday had the fewest visits and Wednesday had none.", "C": "All three days had 15 visits.", "D": "Wednesday had more visits than Tuesday."}, "A", "The chart's highest value is Tuesday's 18 visits, so A is supported by the data.", "讀取圖表數值並比較大小，不用趨勢印象取代精確數據。", ["列出 Monday 12、Tuesday 18、Wednesday 15。", "比較三個數值找最大值。", "確認最大 18 對應 Tuesday。", "排除 B、C、D，逐一對照錯誤數量或比較方向。", "選 A，回查結論與圖表數據一致。"], "easy"),
make(8, "A museum caption says: 'This bridge was built in 1890 and is still used by pedestrians today.' What can readers infer?", {"A": "The bridge has served people for a long time.", "B": "The bridge was built last year.", "C": "Only cars may use the bridge.", "D": "The museum caption is about a train ticket."}, "A", "Built in 1890 and still used today support the inference that the bridge has served people for a long time.", "把明示年份與現在狀態連成時間跨度，再做有限度推論。", ["圈出 1890 與 still used today。", "判斷兩個時間點相距很久。", "將 pedestrians 對應 people 使用橋梁。", "排除 B、C、D，因為它們與年份、使用者或素材類型不符。", "選 A，確認推論沒有超出兩項文字證據。"], "medium"),
make(9, "A website post has the heading 'Three Easy Ways to Save Water' and sections about shorter showers, fixing leaks, and reusing rainwater. What is the post mainly doing?", {"A": "Giving practical water-saving suggestions.", "B": "Comparing three kinds of websites.", "C": "Explaining why showers are expensive to build.", "D": "Announcing a sports competition."}, "A", "The heading and three sections all present actions for saving water, so A states the main purpose.", "結合標題與段落內容判斷主旨，避免只抓其中一個例子。", ["先讀 heading，找出 save water 的主題。", "整理三段都是可執行的節水方法。", "檢查 A 是否涵蓋標題與三個例子的共同功能。", "排除 B、C、D，因為它們不是貼文內容的核心。", "選 A，確認主旨能統攝所有段落。"], "medium"),
make(10, "A photo with a short caption shows students planting trees beside a river. The caption says, 'Our class will check the young trees every month.' What is the best conclusion?", {"A": "The class plans continued care after planting.", "B": "The students planted trees only for one minute.", "C": "The river has no water.", "D": "The class will never return to the site."}, "A", "Planting and checking the trees every month show an ongoing care plan, not a one-time event only.", "整合照片、caption 的未來行動與時間頻率，做有證據界線的結論。", ["觀察照片的 planting action。", "圈出 check every month，找出持續性與頻率證據。", "將兩項資料整合成 continued care。", "排除 B、C、D，因為它們沒有照片或文字支持。", "選 A，確認結論只延伸到每月照顧，不過度推測。"], "hard"),
]

KEYS = ["C", "A", "D", "B", "C", "D", "A", "B", "D", "C"]
CUSTOM_STEPS = [
    ["不要只數圖示；先讀旁邊的句子，確認它補充了什麼行動。", "將 bus、clock、rain cloud 與 rainy days 的文字線索連成情境。", "比較 leave earlier 是否提供可執行的交通建議。", "雲的種類、巴士販售或昨日氣溫都沒有被圖文支持。", "答案 C：素材提醒下雨天提早出門，目的在提供通勤建議。"],
    ["先讀 map legend，因為它直接規定符號代表的意思。", "把星號和 drinking water 對照，不要和虛線資訊混淆。", "選擇能指出取水地點功能的敘述。", "500-meter path 對應 dotted line，封路和出版日期沒有圖例依據。", "答案 A：星號標示可取得飲用水的位置。"],
    ["逐行把菜名與金額配對，避免跨列讀錯。", "把三個價格排序：35、40、75。", "最低數值35對應 Fruit cup。", "Soup和Chicken rice較貴，三項也並非同價。", "答案 D：Fruit cup的35元最低。"],
    ["把短稿中的 First 與 After three days 畫成前後兩個時間節點。", "第一節點是種子放在濕棉花，先不要把它當成三天後行動。", "讀取第二個時間點後面的 move 動詞及目的地 soil。", "重新放棉花、丟土或錄天氣都沒有文字依據。", "答案 B：三天後把種子移到土壤中。"],
    ["漫畫先呈現滿溢垃圾桶，再讓人物提出下次使用回收箱。", "比較問題情境與建議行動，找出兩者共同指向的原因。", "垃圾分類或回收不足最能解釋前後畫面。", "滿桶不是交通、噪音或水源問題的證據。", "答案 C：漫畫在提醒垃圾未妥善分類回收。"],
    ["標籤提供兩種不同資訊：保存方式與期限，先分開讀。", "確認 keep refrigerated 是食用前的保存條件。", "再核對 June 12 是否已過，兩項都會影響是否食用。", "只看包裝顏色或品名不能替代標籤安全資訊。", "答案 D：食用前同時確認冷藏狀態與最佳食用日期。"],
    ["先讀圖表標題與日期類別，確認數值代表圖書館到訪次數。", "比較12、18、15，找最大值而不是把星期順序當高低。", "18對應Tuesday，因此相關陳述有數據支持。", "Monday與Wednesday數值較低，也不能推論整週趨勢。", "答案 A：Tuesday有18次，是三天中最多的一天。"],
    ["把caption拆成時間資訊built in 1890與現況still used today。", "兩個事實合看，橋梁存在很久而且仍供行人使用。", "推論須比原文多一步，但不能超出原文證據。", "不能據此斷定橋永不維修、只給遊客用或完全沒有變化。", "答案 B：可推知這座橋長期服務行人且至今仍在使用。"],
    ["先用標題判斷文章主題，再快速掃描三個小節。", "把 shorter showers、fixing leaks、reusing rainwater歸成共同目標。", "三項行動都在說明如何節約用水。", "文章不是談水質、游泳安全或城市建築。", "答案 D：貼文主要提供節水方法。"],
    ["照片顯示植樹，文字補充每月檢查幼樹，兩種媒體需合讀。", "把一次性的 planting 與重複性的 monthly checks 放在時間軸上。", "定期照料表示活動安排有後續，而非拍照即結束。", "不能推論幼樹已長成、河岸已完成復育或只種一天。", "答案 C：班級計畫持續照顧並追蹤新植樹木。"],
]
for index, question in enumerate(Q):
    correct_text = question["options"][0]["text"]
    distractors = [option["text"] for option in question["options"][1:]]
    distractors.insert(ord(KEYS[index]) - ord("A"), correct_text)
    question["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(distractors)]
    question["answer"]["value"] = KEYS[index]
    question["solutionSteps"] = CUSTOM_STEPS[index]
    question["answer"]["explanation"] = CUSTOM_STEPS[index][-1]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")
