import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = {
    "dawan": {
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/106-2-3%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立大灣國民中學106學年度第2學期第3次段考八年級英文科試題",
        "year": "106-2",
    },
    "guochang": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/3-%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立國昌國民中學113學年度第2學期第1次段考九年級英文科試題",
        "year": "113-2",
    },
    "dashe": {
        "url": "https://www.dam.kh.edu.tw/upload/68/101_28414/104-1-1%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A9%A6%E5%8D%B7.pdf",
        "title": "高雄市立大社國民中學104學年度第1學期第1次段考九年級英文科試卷",
        "year": "104-1",
    },
}

ITEMS = [
    ("D", "guochang", "提出可討論的開放問題", "At the student council meeting, the chair says, 'Our topic is whether the library should open before school. What benefits and concerns should we consider?' What is the chair doing?", ["Announcing that the decision is already final.", "Asking one member to defend the library staff.", "Ending discussion before anyone speaks.", "Opening the discussion and inviting different viewpoints."], "主席先界定要討論的政策，再邀請提出利弊與疑慮，尚未宣布結論；因此是在開啟討論並邀請多方觀點。", ["先找出會議主題：圖書館是否提早開放。", "辨認問句要求列出benefits and concerns，而非只答yes/no。", "確認主席是在收集不同考量，尚未定案。", "排除指派辯護、宣布結果或提前結束等不符語句的選項。", "選D；好的討論開場要界定問題，同時讓不同意見有發言空間。"], "閱讀題組第38題：主持人提出手機校園規範議題並詢問同學看法；本題改為圖書館開放政策。", "以公共議題開啟立場交換；本題的新議題與表述均另行創作。"),
    ("B", "guochang", "主張加上可檢驗理由", "Mina proposes a shaded waiting area near the bus stop. She adds, 'The noon sun is strong, and the nurse recorded several heat complaints last month.' What does her second sentence contribute?", ["It changes the topic to bus schedules.", "It gives reasons and evidence for her proposal.", "It proves that every student supports the idea.", "It asks the chair to end the meeting."], "她先提出遮蔭區，再用正午曝曬與校護紀錄的抱怨作理由和資料；這不等於證明人人同意。", ["分辨第一句的提案和第二句的功能。", "找出第二句的兩項支持：日照強及校護記錄。", "判斷資料是在支持設置遮蔭處，而不是轉換主題。", "小心證據只反映記錄到的狀況，不能推成全體學生都支持。", "選B；討論主張要以理由或資料支撐，但結論範圍不可超過證據。"], "閱讀題組第39至41題：就校園手機政策提出主張、理由並回應疑問；本題改寫為候車遮蔭方案。", "辨識主張與支持理由，並守住資料能支持的範圍。"),
    ("A", "dawan", "追問證據而非否定發言者", "A classmate says, 'Most students want the art room open at lunch.' Which follow-up would best help the group check that claim?", ["'How many students did you ask, and which grades were included?'", "'You are wrong, so we should stop discussing this.'", "'Can we choose the room color now?'", "'Everyone knows what students think already.'"], "詢問受訪人數和年級能檢查「most students」的樣本範圍；其他選項不是人身否定、偏離主題，就是把未查證的概括當事實。", ["找出需要核實的詞：most students。", "思考什麼資訊能檢查這個比例主張是否有代表性。", "比較各選項是否詢問樣本數和涵蓋年級。", "排除攻擊發言者、離題及未經調查就說everyone knows的說法。", "選A；以中性追問檢查證據，比直接否定或附和更能推進討論。"], "第40題：對他人關於選角的意見作適切回應；本題把互動焦點改為追問主張的資料基礎。", "參照對話題的回應選擇形式，練習用有目的的問題延伸交流。"),
    ("C", "dashe", "先肯定再補充顧慮", "A teammate says, 'Let's replace the paper permission slips with an online form.' You agree that it could save paper, but some families have limited internet access. Which response is most constructive?", ["'That idea is perfect; there can be no problem.'", "'No. Online forms are always a bad choice.'", "'I like the paper-saving goal. Could we also keep a paper option for families who need it?'", "'Let's ignore families and vote now.'"], "C先承接節省紙張的共同目標，再提出可能受影響的家庭並給出並行紙本方案；既不盲目附和，也不一概否決。", ["先確認你同意的部分：減少紙張。", "清楚說明實際顧慮：有些家庭網路使用受限。", "找出兼顧目標與需求的方案，而不是只評價提案好壞。", "排除假定毫無缺點、絕對否定或跳過受影響者的回應。", "選C；建設性回應可先承認共同點，再把顧慮轉成可討論的調整。"], "第14題：對同伴陳述的觀點作適切同意與回應；本題另創數位表單的可近用性情境。", "辨認意見交流中同意、理由與延伸提案的語用功能。"),
    ("B", "dawan", "公平分配發言輪次", "During a group discussion, two members begin speaking at once while a quieter student is still holding up a note. What should the facilitator say?", ["'The loudest person gets to decide.'", "'Let's hear Alex finish first, then Sam; I also want to return to Priya's note.'", "'Only people who speak quickly may join.'", "'We have heard enough, so nobody else can contribute.'"], "B為兩位同時發言者安排順序，也明確保留安靜同學的書面意見；能維持輪流並兼顧不同表達方式。", ["觀察討論中的三個訊號：兩人重疊發言、有人等待、有人用紙條參與。", "找能建立清楚輪序而不羞辱任何人的回應。", "確認安靜同學的意見不會因為沒有搶話而被漏掉。", "排除以音量、速度或直接封口決定參與資格的選項。", "選B；主持人要管理輪替，也要讓口說以外的參與方式被看見。"], "第40題：從對話中選出貼合前一句的回應；本題另創小組輪流發言與書面參與。", "取對話回應判讀能力，並拓展到促進公平輪替的討論功能。"),
    ("D", "guochang", "準確歸納不同立場", "After discussing a later school start, one member says students may sleep more, while another worries buses and family schedules would be disrupted. Which summary is fairest?", ["Everyone agrees the school must start later.", "The only concern is that students dislike taking buses.", "The group has decided to change the schedule tomorrow.", "Supporters see a rest benefit; others raise transport and family-schedule concerns."], "D保留兩方各自提出的理由，沒有虛構共識或立即決策，也沒有把交通疑慮縮成對公車的不喜歡。", ["把對話分成支持與疑慮兩側。", "各自記下原本提出的理由，不改成自己的評價。", "檢查摘要是否保留transport及family schedules兩項顧慮。", "排除把分歧寫成全體同意或已經作出決策的選項。", "選D；公平摘要要代表不同發言者，不能把討論中尚未決定的事寫成定案。"], "第38至41題：整合校園手機議題的主張、理由及反方疑問；本題改為上課時間政策的觀點摘要。", "用多輪對話比對各方立場，再整理共同討論但尚未解決的分歧。"),
    ("A", "dashe", "把共識轉成分工", "The group agrees to test a quieter lunch area for one week. Which sentence best moves the discussion into a workable plan?", ["'I'll ask the office about a room; can you track noise levels, and can Jo collect student feedback?'", "'Great, someone should probably do something someday.'", "'Let's announce that the trial worked before we begin.'", "'We agree, so there is no need to assign tasks.'"], "A把共識拆成場地、噪音記錄和使用者回饋三項具體工作，並清楚詢問成員分工；其餘不是空泛、預先下結論，就是沒有執行安排。", ["先確認討論已形成試辦一週的共識。", "找出方案落地需要哪些工作：詢問場地、記錄噪音、蒐集回饋。", "檢查句子是否指派負責人並維持工作與目標一致。", "排除沒有期限的空話及開始前宣告成功等錯誤做法。", "選A；討論的結尾應把共識轉為可執行、可回報的分工。"], "第7題型態：從對話選出符合共同活動目的的句子；本題另創會議結論到任務分派。", "由短對話功能題型轉化為辨認執行計畫是否明確可行。"),
    ("C", "dawan", "管理時間並保留最後意見", "The meeting has three minutes left, and two proposals remain. What should the chair do?", ["Cancel the meeting without recording either idea.", "Let one speaker continue until the bell, even if others cannot reply.", "Give each proposal a brief final turn, summarize the trade-offs, then explain how the group will decide.", "Choose the first proposal without telling anyone."], "C讓兩個方案都有最後簡短陳述，主席再整理取捨並交代決策方式；既守住時間，也沒有暗中偏袒。", ["確認剩餘時間及尚未處理的兩個方案。", "找能讓兩方都獲得發言機會的安排。", "加入整理取捨與公開決策方式，讓後續流程透明。", "排除放任一人占用全部時間、突然散會或私下決定。", "選C；時間管理不是只求結束，而要公平收尾並說清楚下一步。"], "第40題：依既有對話選擇自然且合宜的回應；本題延伸至主席安排最後發言和決策流程。", "以語境合宜性題型練習討論主持者如何公平結束議程。"),
    ("D", "guochang", "尊重異議並尋找可比較方案", "One student wants a large festival concert; another worries about cost and noise. Which reply disagrees respectfully and helps the group compare options?", ["'Your idea is ridiculous, so stop talking.'", "'Cost does not matter if the event is fun.'", "'Let's pick my plan because I said it first.'", "'Could we compare a smaller concert with a daytime acoustic event using cost and noise limits?'"], "D沒有否定同學，而是把成本與噪音轉成共同比較標準，並提出兩個規模不同的可選方案。", ["辨認兩項已提出的限制：預算與噪音。", "選擇承認限制而非貶低提案者的語句。", "查看是否提出可按相同標準比較的替代方案。", "排除只重複自己的偏好或忽視另一方顧慮的答案。", "選D；尊重異議包含承認不同需求，並把爭論轉為可檢驗的比較。"], "第38至41題：在手機政策討論中呈現主張、理由及對方疑問；本題改寫為校慶活動的條件比較。", "從公開英語討論題型取立場交換能力，不沿用題目政策或原對話。"),
    ("B", "guochang", "避免以小樣本過度概括", "A team asks six students who use the east gate about adding a crossing guard. Five support the idea. What is the most accurate conclusion for the meeting notes?", ["Almost every student in the school supports the idea.", "Five of the six students surveyed support it; the group should ask more students before claiming school-wide support.", "The survey proves the crossing guard will prevent all accidents.", "No conclusion can be written because only six students answered."], "資料只涵蓋六位東門使用者，能準確記錄其中五人支持，也需說明尚不能代表全校；不能推成全校多數或保證零事故。", ["先寫出樣本範圍：六位東門使用者。", "計算並核對比例：其中五位支持。", "區分樣本結果和全校意見，判斷要不要再蒐集資料。", "排除把有限樣本推廣到全校或把意見調查當成事故因果證明。", "選B；會議結論要忠於數據並標示代表性限制，而非誇大或完全噤聲。"], "第39至41題：從校園政策對話整合多項理由與疑問；本題改為討論紀錄如何界定調查資料的支持範圍。", "依討論中的主張—理由—疑問結構整理結論，明確保留證據限制。"),
]


def make(index, item):
    answer, source_key, skill, prompt, options, explanation, steps, locator, pattern = item
    source = SOURCES[source_key]
    return {
        "id": f"question-english-performance-2-iv-12-{index}",
        "subject": "english",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": chr(65 + n), "text": value} for n, value in enumerate(options)],
        "knowledgeIds": ["kg-english-performance-2-iv-12"],
        "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" 正確答案：{answer}。"},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": source["url"],
            "sourceLocator": locator + "；本題會議、立場、理由、選項與答案皆重新創作。",
            "authoringNote": "原創引導式討論情境；僅參照公立學校英文段考中辨認意見、理由、合宜回應及整合對話的能力型態，不複製原題或選項。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-24",
        "lessonId": "lesson-english-performance-2-iv-12",
        "examPatternRefs": [{
            "url": source["url"],
            "title": source["title"] + "；僅參照對話／意見交流推理能力，不複製原題。",
            "year": source["year"],
            "subject": "english",
            "locator": locator,
            "observedPattern": pattern,
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "item",
        }],
        "solutionStrategy": f"{skill}：先分清討論者的主張、理由與回應功能，再以對話證據判斷最能促進理解或共同決策的說法。",
        "solutionSteps": steps,
    }


for index, item in enumerate(ITEMS, 1):
    (OUT / f"question-english-performance-2-iv-12-{index}.json").write_text(json.dumps(make(index, item), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(ITEMS)} original guided-discussion questions")
