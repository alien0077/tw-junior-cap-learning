import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-6-iv-2"
KG = "kg-english-performance-6-iv-2"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "title": "高雄市立鹽埕國民中學114學年度第2學期第1次段考三年級英文科", "year": "114-2"},
    {"url": "https://jweb.kl.edu.tw/userfiles/1389/document/40425_%E5%85%AB%E5%B9%B4%E7%B4%9A1%E6%AE%B5%E8%8B%B1%E6%96%87.pdf", "title": "基隆市立武崙國中111學年度第2學期八年級第1次段考英文科", "year": "111-2"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E8%AA%9E.pdf", "title": "高雄市立國昌國民中學110學年度第1學期七年級英文科第1次段考", "year": "110-1"},
]

def refs():
    locators = [
        ("PDF第1頁聽力第6至15題：基本問答與言談理解", "試卷題型提供提問理解、擷取對話訊息及選擇回應的練習形式；題目內容另行原創。"),
        ("聽力測驗（二）基本問答第6至8題及言談理解部分", "題型要求聽取問題、辨認關鍵訊息並選擇支持答案的對話資訊；只供練習策略設計參考。"),
        ("PDF第2頁第21至25題對話回應；第3頁第32至33題對話理解", "以對話脈絡整理訊息並作答；本站另外設計預習、整理、錯誤檢核及遷移任務。"),
    ]
    return [{**s, "subject": "english", "locator": locators[i][0], "observedPattern": locators[i][1], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper" if i == 1 else "page"} for i, s in enumerate(SOURCES)]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-english-performance-6-iv-2-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "參考三份公立學校英文評量的對話理解、問答與證據擷取題型；不取用原題文字、選項或答案。", "authoringNote": "依官方課綱與本單元預習、複習及整理能力獨立創作情境、選項、答案與詳解；公開試題僅供題型研究，題目保持 draft 待後續內容與版權 QA。"}, "reviewStatus": "draft", "updatedAt": "2026-09-27", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "Before reading a new English article about recycling, which preparation is most useful?", {"A": "Preview the title, predict the topic, and note two questions.", "B": "Copy every word before seeing the article.", "C": "Memorize an unrelated poem.", "D": "Skip the title and guess the answer key."}, "A", "Previewing the title and making questions activates relevant knowledge and gives the reader a purpose.", "把預習拆成啟動先備知識與設定閱讀目的，而非盲目抄寫。", ["確認任務是 article 的預習。", "找能在閱讀前啟動主題知識的行動。", "檢查 A 同時有 title、prediction 與 questions。", "排除 B、C、D，因為它們抄寫、離題或跳過文本證據。", "選 A，確認預習能引導後續閱讀。"], "easy"),
make(2, "Which review plan is most likely to help remember ten new words for a test next week?", {"A": "Use the words in short sentences on several different days.", "B": "Read the list once for two hours the night before.", "C": "Look only at the Chinese meanings and never recall English.", "D": "Rewrite the same title without using the words."}, "A", "Using words in context across several days combines retrieval and spacing, which supports longer-term memory.", "比較分散多日提取與單次長時間重讀，找出有間隔且能產出英文的方案。", ["圈出 test next week，判斷需要保留一段時間的記憶。", "尋找 several different days 的間隔安排。", "確認 short sentences 要求主動使用與提取單字。", "排除 B、C、D，因為它們集中重讀、只看提示或沒有使用詞彙。", "選 A，確認計畫同時具備間隔與語境。"], "medium"),
make(3, "After getting three grammar questions wrong, what should a learner record first?", {"A": "The exact error, the rule involved, and a corrected example.", "B": "Only the score, without looking at the sentences.", "C": "A classmate's unrelated favorite song.", "D": "The page number and nothing else."}, "A", "An error log is useful when it preserves the error, the underlying rule, and a corrected example for later review.", "從錯誤建立可回看的證據，不能只保存分數或頁碼。", ["確認目標是從三題文法錯誤學習。", "列出需要保存的三項資訊：錯在哪、規則是什麼、如何改正。", "檢查 A 三者都有。", "排除 B、C、D，因為它們無法說明錯誤原因或修正方式。", "選 A，確認紀錄能支持下次重做與遷移。"], "easy"),
make(4, "A student must review a paragraph. Which note is the best summary?", {"A": "It explains why a school garden helps students and gives two examples.", "B": "School garden, students, examples, and many copied sentences.", "C": "The paragraph is on page five.", "D": "I like gardens."}, "A", "A summary states the central idea and key supporting information without copying every sentence or adding a personal opinion.", "摘要要保留主旨與重要支持細節，並刪除頁碼與個人偏好。", ["先找題目要求 review a paragraph 的整理成果。", "比較選項是否包含主旨與支持資訊。", "檢查 A 有 why school garden 與 two examples。", "排除 B 的零散關鍵字、C 的頁碼與 D 的個人意見。", "選 A，確認內容精簡但足以重建段落重點。"], "medium"),
make(5, "When reviewing a dialogue, which method checks whether you can remember it without looking?", {"A": "Cover the script and retell the speakers' main points.", "B": "Highlight every line and keep the script open.", "C": "Count the punctuation marks only.", "D": "Read the title and stop."}, "A", "Covering the script and retelling the main points requires retrieval rather than simple rereading.", "判斷複習是否包含主動回想，而不是只增加標記或重看文本。", ["確認問題問的是不看稿能否記得。", "找需要 cover the script 的提取行動。", "檢查 retell main points 是否保留對話核心。", "排除 B、C、D，因為它們仍依賴開啟文本或只處理形式。", "選 A，確認方法能直接測量回想結果。"], "easy"),
make(6, "A learner has one hour before an English quiz and is weak at question words. Which plan is most focused?", {"A": "Review who, what, when, and why with examples, then answer five new items.", "B": "Read every chapter equally, including familiar topics.", "C": "Decorate the notes with colors but do not solve questions.", "D": "Study only the easiest vocabulary."}, "A", "A targets the known weakness, provides examples, and checks transfer with new items within the available hour.", "依診斷出的弱點分配有限時間，再用新題驗證是否能遷移。", ["圈出 one hour 與 weak at question words，找限制與優先目標。", "確認 A 先整理 who、what、when、why 的例子。", "檢查 five new items 是否能驗證理解。", "排除 B、C、D，因為它們平均分配、只美化或避開弱點。", "選 A，確認計畫集中且有檢核步驟。"], "medium"),
make(7, "Two notes about the same lesson conflict. What should the learner do?", {"A": "Return to the lesson evidence and compare which note matches it.", "B": "Choose the longer note automatically.", "C": "Keep both without checking the text.", "D": "Delete both and change the topic."}, "A", "Comparing both notes with the original lesson evidence resolves the conflict using a verifiable source.", "遇到整理衝突時回到原文證據，不用長短或直覺決定。", ["確認衝突發生在兩份 notes，而不是已知答案。", "找出共同的核對基準 original lesson evidence。", "逐項比較哪份筆記忠實呈現文本。", "排除 B、C、D，因為它們沒有進行證據核對。", "選 A，確認決定過程可追溯且能修正筆記。"], "medium"),
make(8, "Which weekly routine best combines preview and review?", {"A": "Preview key words before class, review mistakes after class, and revisit them on Friday.", "B": "Study only when a test is announced.", "C": "Preview once but never return to the lesson.", "D": "Review answers without recording why they were wrong."}, "A", "A includes before-class preparation, after-class error review, and a later revisit, covering the full cycle.", "看時間線是否包含課前、課後與延後回顧三個階段。", ["圈出 preview 與 review，確認題目要完整學習循環。", "檢查 A 的 before class、after class 與 Friday。", "確認 mistakes 是可供回顧的具體材料。", "排除 B、C、D，因為它們臨時、單次或沒有錯誤原因。", "選 A，回讀一週時間線確認三階段俱全。"], "medium"),
make(9, "A student remembers a grammar rule but cannot use it in a new sentence. What is the best next step?", {"A": "Study one worked example, explain the rule, and write a new sentence.", "B": "Repeat the rule silently without changing the example.", "C": "Skip grammar and memorize the answer letter.", "D": "Copy the entire textbook page."}, "A", "A moves from an example to an explanation and then to a new sentence, testing transfer instead of recall alone.", "辨認記得規則與能使用規則的差距，再選包含示例、解釋與新情境的步驟。", ["確認困難是 transfer，而非完全不知道規則。", "找出先看 worked example、再 explain、最後 write new sentence 的順序。", "檢查新句子是否改變情境但保留規則。", "排除 B、C、D，因為它們只重複、猜答案或大量抄寫。", "選 A，確認方法能檢查真正的應用能力。"], "hard"),
make(10, "After reviewing, which evidence best shows that a learner is ready for the quiz?", {"A": "The learner can answer new questions, explain mistakes, and correct them without the notes.", "B": "The learner has highlighted every page.", "C": "The learner feels familiar with the chapter title.", "D": "The learner has spent exactly two hours looking at the book."}, "A", "New-question performance, explanation of errors, and independent correction provide direct evidence of understanding.", "用可觀察的成果判斷準備度，不用時間長短或熟悉感取代表現證據。", ["找出題目問 readiness 的證據，而不是投入時間的紀錄。", "確認 A 包含新題、錯誤解釋與不看筆記修正。", "判斷三項都能觀察理解與遷移。", "排除 B、C、D，因為標記、熟悉感與時間不保證能作答。", "選 A，回讀確認證據直接對應測驗要求。"], "hard"),
]

KEYS = ["C", "A", "D", "B", "C", "A", "D", "B", "A", "C"]
CUSTOM_STEPS = [
    ["讀前策略的目的，是帶著問題進入文本，不是先抄完整篇。", "回到標題 recycling，先喚起與回收相關的已知概念。", "在未讀內文前寫下兩個想查證的問題，形成閱讀任務。", "其餘做法不是延後到閱讀前的準備，就是與文章無關。", "答案 C：先看標題、預測主題並提出問題，讀後再用文章修正預測。"],
    ["測驗在下週，複習安排要跨日而非考前一次塞完。", "選擇會讓單字從記憶中被提取並放進句子的做法。", "把 several different days 畫成日程點，確認有間隔。", "單次長讀或只看中文提示不能證明能回想英文詞形與用法。", "答案 A：分幾天用單字造句，兼顧間隔與主動提取。"],
    ["錯了三題文法，先留下能解釋錯因的原始證據。", "紀錄應同時包含錯誤句、對應規則和修正例句。", "對照選項，確認不是只有分數、頁碼或別人的資訊。", "沒有錯誤內容就無法比較原判斷與正確規則。", "答案 D：把錯誤、規則和改正例子放在同一筆紀錄中。"],
    ["段落摘要要壓縮資訊，但不能只列關鍵字或加入偏好。", "先找作者要說明的中心，再看哪些例子支持它。", "核對選項能否讓沒讀段落的人重建主要意思。", "逐句抄寫太細，頁碼與個人喜好又不是段落主旨。", "答案 B：用一句中心意思加上兩項支持資訊概括段落。"],
    ["要檢查『不看稿還記不記得』，就得先移除視覺提示。", "遮住腳本後，從記憶重述對話的主要資訊。", "重述時若卡住，可標記缺漏處，稍後再回原稿核對。", "開著稿高亮仍在重看；數標點或讀標題不測記憶。", "答案 C：遮稿重述，才直接測到能否主動提取內容。"],
    ["時間只有一小時，優先處理已知弱點 question words。", "分配短段：辨認 who/what/when/why 的提問功能並看例句。", "保留最後時間做新題，檢查是否能辨別未見句子中的疑問焦點。", "平均讀所有章節或只做熟悉詞彙，無法針對診斷弱點。", "答案 A：集中練疑問詞，再以五題新題驗證成效。"],
    ["兩份筆記互相矛盾，先不要用篇幅或直覺決定哪份對。", "找到共同依據：原課文、板書或教師提供的資料。", "把爭議句逐項對照原始證據，標記支持與不支持處。", "未核對就兩份並留或全部刪除，都沒有解決資訊衝突。", "答案 D：回到可查證的課程材料，修訂與證據不合的筆記。"],
    ["一週的預習複習不應只在宣布考試時才啟動。", "沿時間軸檢查課前準備、課後回顧和延後再提取是否都出現。", "確認錯題有記下原因，週五回看時能重新作答。", "只預習一次、只看答案或臨考才讀，缺少循環中的一段。", "答案 B：課前預習、課後檢討、週末再訪形成完整週期。"],
    ["已記得規則卻造不出新句，缺的是活用，不是再背一遍。", "先分析一個解題示例，說明規則如何限制句子形式。", "遮住示例後另造句，檢查能否換內容仍用對規則。", "照抄整頁或背答案字母都不會顯示遷移能力。", "答案 A：從示例抽出規則，再用新句測試能否遷移。"],
    ["準備度要看能否獨立處理新問題，不只看投入時數。", "選擇能同時檢查作答、錯因說明與自我修正的證據。", "特別確認作答時沒有依賴筆記提示，避免把熟悉感當會了。", "畫滿螢光筆、認得章名和讀很久都不能直接代表理解。", "答案 C：能答新題、說明錯因並獨立修正，才有較直接的準備證據。"],
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
