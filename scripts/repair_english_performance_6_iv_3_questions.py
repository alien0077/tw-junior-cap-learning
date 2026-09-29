import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-6-iv-3"
KG = "kg-english-performance-6-iv-3"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "title": "高雄市立鹽埕國民中學114學年度第2學期第1次段考三年級英文科", "year": "114-2"},
    {"url": "https://jweb.kl.edu.tw/userfiles/1389/document/40425_%E5%85%AB%E5%B9%B4%E7%B4%9A1%E6%AE%B5%E8%8B%B1%E6%96%87.pdf", "title": "基隆市立武崙國中111學年度第2學期八年級第1次段考英文科", "year": "111-2"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E8%AA%9E.pdf", "title": "高雄市立國昌國民中學110學年度第1學期七年級英文科第1次段考", "year": "110-1"},
]

def refs():
    patterns = [
        ("PDF第1頁聽力第6至15題：基本問答與言談理解", "聽辨活動對話、抓取目的及依聽到的條件作答；只參考英語活動理解型態，題幹與情境獨立創作。"),
        ("聽力測驗（二）基本問答第6至8題及言談理解部分", "公開試題使用情境對話檢查訊息理解與適切反應；本題另寫活動規則、完成證據與回饋情境。"),
        ("PDF第2頁第21至25題對話回應；第3頁第32至33題校園對話理解", "對話回應／校園交談題型可研究角色互動與訊息銜接；不使用原題文、角色或答案。"),
    ]
    return [{**s, "subject": "english", "locator": patterns[i][0], "observedPattern": patterns[i][1], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper" if i == 1 else "page"} for i, s in enumerate(SOURCES)]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-english-performance-6-iv-3-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "參考三份公立學校英文評量中的活動對話理解及情境回應題型；不取用原題文字、角色或答案。", "authoringNote": "依官方課綱與本單元參與英語活動的能力獨立創作題幹、選項、答案與詳解；公校試題僅作題型研究，題目保持 draft 待後續內容與版權 QA。"}, "reviewStatus": "draft", "updatedAt": "2026-09-27", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "The English club is holding a lunchtime story circle. What is the main purpose of the activity?", {"A": "To share and discuss short English stories.", "B": "To sell all the school's lunch boxes.", "C": "To repair the library computers.", "D": "To test students' running speed."}, "A", "A story circle uses short stories and discussion, so A states the activity's purpose.", "先從活動名稱與時間找核心任務，再排除沒有文本或討論證據的選項。", ["圈出 story circle，確認活動核心與故事有關。", "用 English club 判斷需要英語閱讀或分享。", "檢查 A 是否同時包含 stories 與 discuss。", "排除 B、C、D，因為它們不是故事交流任務。", "選 A，回讀活動名稱與目的確認一致。"], "easy"),
make(2, "An English movie night notice says: 'Bring a notebook. After the film, write one sentence about your favorite scene.' What should participants do after watching?", {"A": "Write one sentence about a favorite scene.", "B": "Leave before the film ends.", "C": "Translate every line aloud during the film.", "D": "Return the notebook to the cafeteria."}, "A", "The notice gives a post-film writing task about a favorite scene, so A follows the stated instruction.", "依活動流程詞 after the film 定位後續任務，不把 bring a notebook 誤當成最後成果。", ["找出活動素材 film 與流程詞 after the film。", "圈出 write one sentence 與 favorite scene。", "將兩項合併成 A 的完整行動。", "排除 B、C、D，因為它們違反時間或沒有被公告要求。", "選 A，確認回答重述的是觀影後任務。"], "easy"),
make(3, "At an English conversation booth, students can practice ordering food with a partner. Which action best uses the booth?", {"A": "Take turns as customer and server using English.", "B": "Stand outside and read the booth title only.", "C": "Use the booth to solve a math worksheet silently.", "D": "Let the partner speak every line."}, "A", "Taking both roles and using English directly practices the target restaurant conversation.", "把活動目的轉成角色輪替與英語產出兩項可觀察證據。", ["確認 booth 的任務是 ordering food with a partner。", "列出需要的兩個角色 customer 與 server。", "檢查 A 有 take turns 與 using English。", "排除 B、C、D，因為它們不完成對話練習。", "選 A，確認行動與活動設計完全對應。"], "medium"),
make(4, "The school invites an exchange student to speak about her hometown. Which question would best support the English activity?", {"A": "What food is popular in your hometown?", "B": "How many chairs are in this classroom?", "C": "Can I leave before the talk?", "D": "What is the answer to tomorrow's math test?"}, "A", "A asks about the guest's hometown and invites a meaningful English response related to the talk.", "先找講座主題與來賓背景，再選能延伸內容的開放問題。", ["圈出 exchange student 與 hometown，確認談話主題。", "尋找能請來賓分享家鄉資訊的英文問題。", "檢查 A 的 food is popular 是否與 hometown 直接相連。", "排除 B、C、D，因為它們談教室、離席或無關考試。", "選 A，確認問題能促成有意義的英語交流。"], "easy"),
make(5, "A poster for an English reading challenge says: 'Read three books in April and record the titles on the class sheet.' What evidence shows completion?", {"A": "Three book titles recorded on the class sheet.", "B": "A colorful poster on the wall.", "C": "A student says reading is important.", "D": "One book borrowed in March."}, "A", "The poster defines completion as three April books with their titles recorded, so A is direct evidence.", "把活動規則轉成可核對的數量、時間與紀錄欄位。", ["圈出 three books、in April 與 record the titles。", "判斷完成證據必須同時對應數量、月份與紀錄。", "檢查 A 三項條件是否都有。", "排除 B、C、D，因為它們沒有證明三本四月閱讀。", "選 A，回到公告逐項核對完成標準。"], "medium"),
make(6, "During an English song workshop, the teacher asks groups to change one verse into a new verse with the same rhythm. Which result meets the task?", {"A": "A new verse with different words but the same rhythm.", "B": "A copied verse with no changes.", "C": "A drawing with no English words.", "D": "A list of songs from another class."}, "A", "The task requires new words while preserving the rhythm, exactly as A describes.", "拆解 same rhythm 與 new verse 兩個限制，再檢查作品是否同時滿足。", ["找出要求中的 change one verse 與 new verse。", "圈出 same rhythm，確認形式需保留。", "檢查 A 同時有 different words 與 same rhythm。", "排除 B、C、D，因為它們沒有原創英文新歌詞或偏離任務。", "選 A，確認內容改變但節奏條件保留。"], "medium"),
make(7, "An English game station gives points for asking and answering five questions politely. Which plan follows the rules?", {"A": "Ask five questions, answer each one, and use polite phrases.", "B": "Ask one question five times without listening.", "C": "Take points without speaking English.", "D": "Answer before reading the questions."}, "A", "A includes the number, both sides of the interaction, and the polite-language rule.", "用公告中的數量、雙向互動與語用限制逐項核對計畫。", ["圈出 five questions、asking and answering、politely。", "列出三個必備條件。", "檢查 A 是否完整包含提問、回答與禮貌表達。", "排除 B、C、D，因為它們重複、逃避英語或未完成理解。", "選 A，確認計畫能取得活動要求的 points。"], "medium"),
make(8, "After an English camp role-play, which reflection is most useful?", {"A": "I asked for directions clearly, but I need to listen more carefully.", "B": "The camp was three days long.", "C": "My costume was blue.", "D": "I participated because there was no other choice."}, "A", "A identifies a communication success and a specific next improvement related to the role-play.", "反思要回到英語活動的溝通表現，包含證據與下一步，而非外在細節。", ["確認活動是 role-play，重點是溝通能力。", "尋找一項完成的語言行動與一項可修正能力。", "檢查 A 的 asked clearly 與 listen more carefully。", "排除 B、C、D，因為它們只談天數、服裝或動機。", "選 A，確認反思可轉成下一次活動目標。"], "medium"),
make(9, "A school English fair has a booth where visitors match words with pictures. How can a student improve the booth?", {"A": "Add clear labels and ask visitors to explain one match.", "B": "Remove all pictures and leave only a blank table.", "C": "Give visitors answers before they try.", "D": "Use instructions in a different subject only."}, "A", "Clear labels improve access and asking for an explanation adds meaningful English participation and evidence.", "評估改進方案是否兼顧可理解性、操作與英語表達，而非直接代答。", ["確認 booth 的核心是 words 與 pictures 的配對。", "找同時改善提示與學習證據的方案。", "檢查 A 有 clear labels 與 explain one match。", "排除 B、C、D，因為它們移除材料、揭露答案或離題。", "選 A，確認訪客仍需思考並用英語說明。"], "hard"),
make(10, "The English club wants more students to join next month. Which evidence should it collect after this month's activity?", {"A": "Attendance, completed tasks, and one participant suggestion.", "B": "Only the color of the event banner.", "C": "The organizer's favorite song.", "D": "A random number unrelated to the activity."}, "A", "Attendance measures reach, completed tasks show engagement, and a participant suggestion supports improvement planning.", "把活動成效分成參與人數、任務完成與學習者回饋三種證據。", ["確認問題問的是下月改進需要的 evidence。", "列出能反映 reach、engagement 與 feedback 的資料。", "檢查 A 三項分別對應三種成效。", "排除 B、C、D，因為它們不能反映活動參與或品質。", "選 A，確認資料能支持下一次活動決策。"], "hard"),
]

KEYS = ["D", "B", "C", "A", "D", "B", "C", "A", "B", "D"]
CUSTOM_STEPS = [
    ["先拆解 story circle 這個活動名稱，再判定題目問的是目的而非時間。", "將 story 對應到短篇故事，circle 對應到輪流分享或討論。", "檢查是否有選項同時保留英文故事與交流這兩個核心。", "販售午餐、修電腦、測跑速都沒有文本或談話活動。", "答案 D：活動要讓成員分享並討論簡短英文故事。"],
    ["讀公告時先畫出時間順序：bring notebook 是入場準備。", "定位 after the film，這才是題目要求的觀影後行動。", "擷取 write one sentence 與 favorite scene 兩個必要細節。", "離場、觀影中逐句翻譯、還筆記本都不是公告指令。", "答案 B：看完後寫一句最喜歡場景的感想。"],
    ["先確認 conversation booth 練的是餐廳點餐對話。", "把角色分成顧客與服務人員，安排輪流說話。", "檢查方案是否使用英語且兩人都實際開口。", "只看招牌、安靜做數學或讓搭檔包辦都沒有完成練習。", "答案 C：輪流扮演顧客和店員，以英語完成點餐對話。"],
    ["活動主題由來賓談家鄉；問題需能引出相關內容。", "找可以讓對方說明家鄉生活的開放式提問。", "判斷 food is popular 是否能延伸到 hometown 的文化與生活。", "教室椅子、提前離席、數學考題都偏離講座。", "答案 A：詢問家鄉常見食物，延續演講主題並促進英語交流。"],
    ["將完成規則拆成閱讀量、期限、登記方式三欄。", "核對題目給的三本、四月和班級紀錄表。", "逐一比對證據選項是否涵蓋所有條件。", "海報外觀、口頭稱讚或三月只借一本都不足以證明完成。", "答案 D：班級表上登記三本四月讀物的書名。"],
    ["先讀懂改編任務有兩個約束：歌詞要新，節奏要保留。", "分別檢查作品的文字是否不同於原段，以及節拍是否相同。", "只有同時符合兩項才算達成，而不是只改其中一項。", "照抄沒有新內容，畫圖或列別班歌單則不是新歌詞。", "答案 B：寫出新詞句並保持原有節奏。"],
    ["把得分規則轉成可勾選的三項：五個問題、逐一回答、禮貌用語。", "判斷計畫是否讓兩位參與者都有提問與回答回合。", "對照 polite phrases，確認用語符合活動社交規範。", "只問一題、拿分不說英語或沒讀題都漏掉規則。", "答案 C：問五題並回答每題，互動時使用禮貌語句。"],
    ["角色扮演的回顧應描述交流表現，而不只是營隊外在資訊。", "找一項成功的溝通行為，再找下一次可改進的技能。", "檢查 asked for directions 與 listen more carefully 是否可觀察。", "天數、服裝顏色和被迫參加都不能指引下一次練習。", "答案 A：說明自己能清楚問路，也設定更專心聆聽的下一步。"],
    ["展攤原本是詞圖配對，改善時要讓訪客仍能完成配對。", "增加清楚標示可降低操作門檻，請訪客說明配對則增加英語輸出。", "檢查改進有沒有保留思考，而不是直接公布答案。", "空桌、先給答案或只用其他科指示會破壞活動目標。", "答案 B：加上易懂標籤，再請訪客解釋一組配對。"],
    ["活動後要規劃下次招募，先界定需要哪些可行動的資料。", "出席數顯示觸及，完成任務顯示參與，建議回饋指出改善方向。", "確認三種資料分別回答『來了多少、做了什麼、怎麼改』。", "布條顏色、主辦者歌曲或無關數字無法說明活動成效。", "答案 D：記錄出席、任務完成情況及一則參加者建議。"],
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
