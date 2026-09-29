import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"

# Every entry below is independently authored. Sources support only the stated
# public-exam skill pattern; no prompt, passage, option, or answer is copied.
SOURCES = {
    "nantou_2025": {
        "url": "https://web.tdvs.ntct.edu.tw/mediafile/1040/news/294/2025-11/2025112610306_0.pdf",
        "title": "南投縣第四屆縣長盃國中英文閱讀測驗暨引導式寫作比賽測驗（官方公開試卷）",
        "year": "114",
        "locator": "PDF印刷頁第3頁，第三部分引導式寫作第1題；評分含內容與組織，任務要求交代事件、行動、感受及學習所得。",
        "pattern": "引導寫作以多個明確內容要求與組織評分檢驗讀者能否扣題、安排支持內容並形成完整段落。",
    },
    "nantou_2024": {
        "url": "https://www.tdvs.ntct.edu.tw/mediafile/1040/news/294/2024-12/2024128103749_1.pdf",
        "title": "南投縣第三屆縣長盃國中學生英文閱讀測驗暨引導式寫作比賽測驗試題",
        "year": "113",
        "locator": "PDF印刷頁第7頁，第二部分引導式寫作第1題；100字以上短文，評分明列內容、組織、文法、用字及標點。",
        "pattern": "引導寫作要求圍繞單一生活主題發展經驗與反思，評分明列內容完整度及組織。",
    },
    "nantou_2023": {
        "url": "https://www.tdvs.ntct.edu.tw/mediafile/1040/news/294/2023-12/2023121175637_1.pdf",
        "title": "南投縣第二屆縣長盃國中學生英文閱讀測驗暨引導式寫作比賽測驗試題",
        "year": "112",
        "locator": "PDF印刷頁第7頁，第二部分引導式寫作第1題；100字以上說明型短文，評分明列內容與組織。",
        "pattern": "說明型提示要求學生先表達可發展的中心主張，再用相關理由組織成段落。",
    },
    "guochang_110": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87_1.pdf",
        "title": "高雄市立國昌國中110學年度第一學期第二次段考一年級英語科試題",
        "year": "110-1",
        "locator": "PDF印刷頁第5頁，非選擇題第七大題第3小題：將重排詞組整理成語意完整且符合英文語序的句子。",
        "pattern": "重組作答需先確立句子主幹，再依語意關係排列修飾語並檢查完整性。",
    },
    "gushan_108": {
        "url": "https://www.kusjh.kh.edu.tw/upload/files/f340d81b4a7600f0db410e25671b18a3.pdf",
        "title": "高雄市立鼓山高中附設國中部108學年度第二學期第一次段考國一英語科閱讀試題卷",
        "year": "108-2",
        "locator": "PDF印刷頁第2頁，第五大題第4、5小題；依提示詞組重組成文法與語意完整的句子。",
        "pattern": "句子重組要辨認主幹及詞組搭配，並用語法和完整語意檢查排序結果。",
    },
    "xiaogang_110": {
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/11%E4%B8%80%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F/2%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/110-1-2%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立小港國民中學110學年度第一學期第二次段考一年級英文科試題",
        "year": "110-1",
        "locator": "PDF印刷頁第5頁，第二部分第二大題第3小題；提示詞組句子重組，解答在第6頁。",
        "pattern": "提示詞組需依疑問句語序、否定詞位置及地點片語關係組成完整句。",
    },
    "ziqiang_107": {
        "url": "https://www.tcjh.tyc.edu.tw/uploads/1548635646492gsGMmT1l.pdf",
        "title": "桃園市立自強國中107學年度第一學期第一次段考八年級英語科試題",
        "year": "107-1",
        "locator": "PDF印刷頁第1頁，第三大題第5題（because）；第2頁，第三大題第12題（so），辨識子句因果關係。",
        "pattern": "校內英文試題以相鄰子句的原因與結果關係辨識連接詞功能。",
    },
    "hcvs_112": {
        "url": "https://www.hcvs.kh.edu.tw/uploads/1709192173637fEtZziD7.pdf",
        "title": "112學年度共同科目英文試題（高雄市立中正高工校網公開）",
        "year": "112-2",
        "locator": "PDF印刷頁第5頁，第34題：讀取產品組裝說明後判斷程序先後順序。",
        "pattern": "程序型文本以明示步驟測量動作順序及前後依賴，不可只按字面相似度排列。",
    },
}

DATA = [
    {
        "skill": "topic sentence and scope",
        "prompt": "A student is planning a paragraph about making the school library easier to use during lunch. Which sentence would be the strongest topic sentence?",
        "options": [
            "My lunch box has a green lid and two small clips.",
            "Some libraries in other cities open on weekends.",
            "A few simple changes can make our lunch-time library calmer and easier to use.",
            "The school library contains books about many subjects.",
        ],
        "answer": "C",
        "explanation": "C names the paragraph's specific focus—improving the library at lunch—and leaves room for several supporting changes. A is unrelated; B shifts to other cities; D is true but only describes the library and does not state the proposed focus.",
        "strategy": "先把題目限制圈出（school library、during lunch、make easier to use），再選能同時涵蓋主題與可發展方向的句子；太窄或只是背景事實都不適合當主題句。",
        "steps": [
            "圈出寫作對象與時段：地點是校內圖書館，情境是午餐時間，任務是提出改善方向。",
            "比較四句涵蓋範圍：A談午餐盒、B談外地週末開館，都離開本段場景。",
            "D只告訴讀者館藏很多，沒有指出午餐時要改善什麼，因此不足以統領後文。",
            "C同時點出午餐時段、圖書館使用感受及可採取的改變，後續可接座位或動線細節。",
            "把C放在段首後，逐句追問支持句是否說明『如何更安靜、更好使用』；答不出就刪除或改寫。",
        ],
        "refs": ["nantou_2025", "nantou_2024", "nantou_2023"],
    },
    {
        "skill": "relevant supporting detail",
        "prompt": "The topic sentence is: 'Bringing a reusable bottle can reduce waste at school.' Which detail gives the clearest support?",
        "options": [
            "Many students decorate their bottles with stickers.",
            "A student who refills one bottle avoids taking a new disposable cup at each water break.",
            "The school basketball team practices after class on Tuesdays.",
            "Some bottles keep drinks cold for several hours.",
        ],
        "answer": "B",
        "explanation": "B shows the direct mechanism connecting reuse to less disposable waste. A and D describe bottle features or preferences but do not show waste reduction; C is off topic.",
        "strategy": "把主題句改寫成待證明的因果關係，再找能補上『為什麼會減少垃圾』的具體例子，而不是只找同一主題名詞。",
        "steps": [
            "將主題句拆成主張與待補原因：主張是垃圾變少，原因必須涉及少用一次性容器。",
            "A雖提到水瓶，貼紙裝飾與垃圾量沒有清楚因果連結，不能當主要證據。",
            "C談球隊練習，完全沒有回應瓶子或廢棄物；D談保冷功能，也沒有證明少丟容器。",
            "B描寫每次補水都沿用同一瓶，直接減少拿取新紙杯或塑膠杯的次數，所以能支持主張。",
            "檢查段落時，用『因此少了哪一件廢棄物？』追問支持句，答案能指出一次性杯，論證才閉合。",
        ],
        "refs": ["nantou_2025", "nantou_2023"],
    },
    {
        "skill": "chronological paragraph order",
        "prompt": "A student is writing a short how-to paragraph about turning a clean jar into a seed starter. Which order makes the process clear?\n(1) Place the jar near a bright window and check the soil each day.\n(2) Rinse the jar and make sure it is dry.\n(3) Add damp soil and press one seed just below the surface.\n(4) Cover the seed lightly and label the jar with the planting date.",
        "options": [
            "3 → 2 → 4 → 1",
            "2 → 4 → 1 → 3",
            "4 → 3 → 2 → 1",
            "2 → 3 → 4 → 1",
        ],
        "answer": "D",
        "explanation": "The container must be clean and dry before it is filled. The seed is placed in the soil, then covered and labeled; daily care follows only after planting.",
        "strategy": "這是有物理前置條件的程序段。先找不可顛倒的依賴（容器先乾淨、種下後才覆土、完成後才照護），再排其他細節。",
        "steps": [
            "先判斷操作對象：種子不能先放進尚未清潔的罐子，因此(2)必須起頭。",
            "罐子乾燥後才加入濕土並放入種子，故(3)接在(2)之後。",
            "(4)提到 cover the seed，必須先有已放入土中的種子，所以(4)不能排在(3)前。",
            "靠窗與每日檢查是播種完成後的照護，只有(1)可作最後一步。",
            "按D的順序逐一復述：洗乾罐子→放土與種子→覆土標日期→移至窗邊照顧；前後依賴皆成立。",
        ],
        "refs": ["hcvs_112", "guochang_110", "gushan_108"],
    },
    {
        "skill": "audience and purpose",
        "prompt": "A paragraph for younger students explains how to choose a first after-school club. Which opening best fits both the audience and purpose?",
        "options": [
            "If you are unsure, visit one meeting and ask a member what beginners usually do.",
            "Every student must join the club with the most trophies.",
            "Our school was built many years ago beside a busy road.",
            "The committee hereby requests immediate registration by all eligible persons.",
        ],
        "answer": "A",
        "explanation": "A speaks directly and reassuringly to a younger reader and offers a practical first action. B pressures rather than advises, C is unrelated background, and D is formal administrative language unsuitable for peer guidance.",
        "strategy": "先辨認讀者的經驗與段落目的，再檢查稱呼、語氣和建議是否讓讀者做得到；讀者不同，合適的開場也不同。",
        "steps": [
            "從for younger students確定讀者是可能尚未參加社團的新手，而不是校務行政人員。",
            "從choose a first club確定目的在提供可執行的入門建議，不是宣傳獎盃或介紹校史。",
            "A直接稱呼讀者並提供旁聽、詢問兩個低門檻行動，符合新手需要。",
            "排除B的強迫語氣與D的公文腔；兩者都沒有照顧讀者猶豫或知識不足的情況。",
            "續寫時讓後文回答『參觀時看什麼、要問什麼』，維持友善建議的同一目的。",
        ],
        "refs": ["nantou_2024", "nantou_2025"],
    },
    {
        "skill": "logical connector",
        "prompt": "Choose the connector that shows the correct relation: 'The class checked the weather forecast before planning the outdoor reading day. ___, it moved the event to Friday, when no rain was expected.'",
        "options": ["For example", "In contrast", "As a result", "Meanwhile"],
        "answer": "C",
        "explanation": "The forecast check leads to the decision to move the event, so 'As a result' expresses consequence. The other choices signal an example, contrast, or simultaneous event, none of which matches the cause-and-decision relation.",
        "strategy": "不要先憑語感選轉折詞；先用中文說明前後句的關係，再挑選表達該邏輯功能的英文連接語。",
        "steps": [
            "讀第一句，找出已發生的資訊：班級先查天氣預報，這是後續安排的依據。",
            "讀第二句，辨認新行動：活動改到不會下雨的星期五，這是查詢後作出的決定。",
            "用『因為查過預報，所以改期』描述兩句關係，判定為原因導致結果。",
            "For example、In contrast、Meanwhile分別表示舉例、對比、同時，與因果決策不符。",
            "選As a result後重讀整段，確認連接詞沒有把結果錯說成例子或對比。",
        ],
        "refs": ["nantou_2023", "nantou_2024", "ziqiang_107"],
    },
    {
        "skill": "evidence detail relevance",
        "prompt": "A paragraph argues that the new student garden helps classmates learn to care for living things. Which detail most directly supports that idea?",
        "options": [
            "The garden fence was painted green during the holiday.",
            "Teams record how changing the amount of sunlight affects the seedlings and adjust their watering notes.",
            "The science classroom has twenty-four chairs.",
            "Some students prefer drawing flowers to planting them.",
        ],
        "answer": "B",
        "explanation": "B gives observable actions—tracking sunlight effects and adapting care—that demonstrate learning and responsibility toward living plants. A is decoration, C is unrelated room information, and D is a preference rather than evidence of care.",
        "strategy": "支持細節要能讓讀者看見主張如何發生。檢查句子是否含有可觀察的行動或結果，而非只和主題共享一個名詞。",
        "steps": [
            "把主張分成兩部分：學生有學習，而且學會照顧植物；細節必須同時連到其中至少一項。",
            "A描述圍欄顏色，只有外觀資訊，沒有學習或照顧行為。",
            "C的椅子數量與花園經驗無關；D只比較興趣，沒有說明學生實際如何照料植物。",
            "B呈現持續觀察幼苗、記錄光照變化並調整澆水，能直接顯示照護及依證據學習。",
            "若要把B擴成段落，可再寫一個觀察結果，但不得把尚未量測的效果說成已證實。",
        ],
        "refs": ["nantou_2025", "nantou_2023"],
    },
    {
        "skill": "concluding sentence",
        "prompt": "A paragraph describes how students planned a book swap, labeled the books by age group, and made a quiet corner for browsing. Which concluding sentence best brings the paragraph to a close?",
        "options": [
            "The moon appears to change shape during the month.",
            "Next week, our class may learn how to bake bread.",
            "With these small choices, the swap became welcoming and helped more books find new readers.",
            "A dictionary lists words in alphabetical order.",
        ],
        "answer": "C",
        "explanation": "C gathers the described actions into their shared outcome without adding a new topic. A, B, and D introduce unrelated facts instead of closing the book-swap paragraph.",
        "strategy": "好的結尾不是再塞一個新話題，而是把前述做法收束到共同成果，讓讀者知道這些細節為何放在同一段。",
        "steps": [
            "回看三個已出現的細節：規劃交換、分類標示、安排瀏覽角落，全部服務於讓活動容易參與。",
            "先找能概括它們共同效果的句子，而不是只重複其中一項例如分類。",
            "C把三項安排收束成友善參與與書本找到新讀者的成果，能結束而不偏題。",
            "A、B、D分別切到月相、烘焙及字典，沒有承接任何已述證據，因此不能作結尾。",
            "將C接在段尾再讀一次，確認段落從準備措施走到活動成果，沒有突然開啟新的說明。",
        ],
        "refs": ["nantou_2024", "nantou_2025"],
    },
    {
        "skill": "paragraph coherence and reference",
        "prompt": "Four sentences from a paragraph about keeping a reading group after school have been mixed up. Which order makes the cause and response easiest to follow?\n(1) The art club began using the library table at that time.\n(2) Our reading group still wanted to meet after school twice a week.\n(3) We therefore moved our meetings to Tuesday lunch.\n(4) This new time worked because members could bring lunch and stay in the library.",
        "options": [
            "1 → 3 → 2 → 4",
            "3 → 4 → 1 → 2",
            "1 → 2 → 4 → 3",
            "2 → 1 → 3 → 4",
        ],
        "answer": "D",
        "explanation": "Start with the group's goal (2), explain the conflict that prevents the old meeting place/time (1), give the resulting change (3), then explain why that change works (4). 'Therefore' and 'This new time' point back to the preceding ideas.",
        "strategy": "同時追蹤時間、因果和指涉詞：therefore前面要有原因，this new time前面必須先出現一個新時段。",
        "steps": [
            "(4)的This new time需要先有某個新時段作為先行詞；因此(4)不可能排在(3)之前。",
            "(3)的therefore表示結果，前面要交代原因：讀書小組想繼續聚會，但原地點被占用。",
            "把(2)作為段落入口先交代小組需求，接著以(1)說明圖書館桌子被美術社使用的障礙。",
            "原因成立後才用(3)說明改到週二午餐時間，最後(4)解釋為何新安排可行。",
            "依D順讀，代名詞和因果連接都有明確前文，段落形成『需求→衝突→調整→結果』。",
        ],
        "refs": ["guochang_110", "gushan_108", "xiaogang_110", "nantou_2024"],
    },
    {
        "skill": "outline and paragraph development",
        "prompt": "A prompt asks for a short recommendation for a class picnic spot. The paragraph should give one clear choice and reasons that classmates can check. Which outline is best?",
        "options": [
            "State the suggested spot → compare shade and restroom access at two places → explain which class needs each feature → restate the recommendation",
            "List favorite snacks → describe a movie → mention a bus color → end with a weather fact",
            "Name a park → give an unsupported claim that it is perfect → change to a story about a pet",
            "Describe the class photo → list every student's hobby → introduce a new topic about exams",
        ],
        "answer": "A",
        "explanation": "A begins with a clear recommendation, develops it with comparable and relevant criteria, considers the audience's needs, and returns to the choice. The other outlines drift between topics or rely on unsupported claims.",
        "strategy": "先把提示改成一個要回答的問題，再依『立場、可核對理由、讀者需求、收束』安排材料；每個大綱節點都要能回到推薦目的。",
        "steps": [
            "確認任務不是自由寫野餐故事，而是要替全班推薦一處地點，因此需要提出明確選擇。",
            "有效理由應能比較或查證；遮蔭與廁所位置都會影響同學是否適合參加。",
            "A先表明建議，再提供兩項可比較條件，之後連回不同班級需求，結尾回扣選擇。",
            "B和D把零散興趣塞入同段，C則只有perfect的主觀斷言，沒有資料或理由支撐。",
            "動筆前逐項檢查大綱：若某句不能幫讀者判斷野餐地點，就移除或另開新段。",
        ],
        "refs": ["nantou_2023", "nantou_2024", "nantou_2025"],
    },
    {
        "skill": "integrating constraints and evidence",
        "prompt": "A student must recommend a route for classmates walking to an evening event. The map marks a well-lit main street that enters campus through the east gate; the notice says the east gate closes at 6:00 p.m.; the timetable shows the last school shuttle leaves at 5:50. Which plan uses all three pieces of information responsibly?",
        "options": [
            "Recommend the east gate at 6:10 because the shuttle runs later than usual.",
            "Recommend the lit main street, tell classmates to arrive before the east gate closes, and note that anyone needing the shuttle must leave before 5:50.",
            "Say every route is equally safe and omit the gate and shuttle times.",
            "Copy the three facts as a list but do not explain what classmates should do.",
        ],
        "answer": "B",
        "explanation": "B connects the route's lighting to safety and preserves both time constraints without inventing a later shuttle. A contradicts the timetable and gate notice; C makes an unsupported safety claim; D includes facts but never turns them into a useful recommendation.",
        "strategy": "多來源段落先分清每份資料能支持什麼，再核對限制是否互相衝突；結論只能強於資料允許的範圍，不能自行補造班次或安全保證。",
        "steps": [
            "把三項資料分開記錄：地圖支持照明較好的街道；公告限制東門須在六點前通過；時刻表限制搭車者五點五十前離校。",
            "用讀者需求檢查推薦內容：步行安全要選亮路，校門與接駁車時間則是不同的行程條件。",
            "B保留三項證據並分別提出對應行動，沒有把門禁時間誤當成接駁車發車時間。",
            "A把已知時刻改成『更晚』且安排在關門後，與資料矛盾；C聲稱所有路線同樣安全，資料並未比較所有路線。",
            "D雖沒有篡改數字，卻缺少如何行動的主旨句；寫作要把事實組織成讀者能採取的建議。",
        ],
        "refs": ["nantou_2025", "nantou_2023"],
    },
]


def reference(source_key, skill):
    source = SOURCES[source_key]
    return {
        "url": source["url"],
        "title": source["title"],
        "year": source["year"],
        "subject": "english",
        "locator": source["locator"],
        "observedPattern": f"{source['pattern']}本題只改寫其命題型態以練習「{skill}」，題幹、選項、情境與答案均為原創。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


for index, item in enumerate(DATA, 1):
    refs = [reference(source_key, item["skill"]) for source_key in item["refs"]]
    question = {
        "id": f"question-english-performance-4-iv-8-{index}",
        "subject": "english",
        "type": "single-choice",
        "prompt": item["prompt"],
        "options": [{"id": chr(65 + n), "text": value} for n, value in enumerate(item["options"])],
        "knowledgeIds": ["kg-english-performance-4-iv-8"],
        "difficulty": "medium",
        "answer": {"value": item["answer"], "explanation": item["explanation"]},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": refs[0]["url"],
            "sourceLocator": refs[0]["title"] + "；" + refs[0]["locator"],
            "authoringNote": "依官方課綱能力及公開試題的段落組織／引導寫作型態獨立命題；只借鑑 pattern，不重製任何原卷文字、選項、圖表或答案。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-26",
        "lessonId": "lesson-english-performance-4-iv-8",
        "examPatternRefs": refs,
        "solutionStrategy": item["strategy"],
        "solutionSteps": item["steps"],
    }
    (OUT / f"question-english-performance-4-iv-8-{index}.json").write_text(
        json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

print(f"authored {len(DATA)} independent English 4-IV-8 questions")
