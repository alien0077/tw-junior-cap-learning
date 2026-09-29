import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-6-iv-5"
KG = "kg-english-performance-6-iv-5"
SOURCES = [
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87_1.pdf", "title": "高雄市立國昌國中110學年度第一學期第二次段考一年級英語科試題", "year": "110-1"},
    {"url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/32%E4%B8%89%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/1%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/105-2-1%20%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf", "title": "高雄市立小港國民中學105學年度第2學期第1次段考三年級英文科", "year": "105-2"},
    {"url": "https://jweb.kl.edu.tw/userfiles/1389/document/39208_0524%E7%AC%AC%E4%BA%94%E7%AF%80--%E4%B9%9D%E4%B8%8B%E8%8B%B1%E6%96%87%E4%BA%8C%E6%AE%B5.pdf", "title": "基隆市立武崙國中110學年度第2學期九年級第2次段考英文科", "year": "110-2"},
]

def refs():
    locators = [
        ("PDF第4頁第24至26題：資訊文本事件排序、依文意推論及由上下文判斷詞義", "先回到短文找事件線索，再以鄰近語句判讀生字意思；本站只借用『以文本證據核對查詢結果』的推理型態。"),
        ("PDF第5頁第51至53題：依文章證據判斷敘述、主旨及片語在文中意思", "閱讀題要求將主張與文章細節對照，並用上下文理解片語；本題組只研究證據核對與語境判讀，不沿用原文。"),
        ("PDF第2頁第13至27題：句境詞義、片語搭配及詞性選用", "單題把目標字詞放進完整句境，需依語意和語法功能排除干擾項；本站只轉化成工具查詢後的語境核對步驟。"),
    ]
    return [{**s, "subject": "english", "locator": locators[i][0], "observedPattern": locators[i][1], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "page"} for i, s in enumerate(SOURCES)]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-english-performance-6-iv-5-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "參考三份公立學校英文段考之句境詞義、詞性、搭配與用法辨識型態；題目與答案均獨立撰寫。", "authoringNote": "依官方課綱與本單元工具書／網路查詢能力獨立創作情境、選項、答案與解法；公開試題僅作語境詞義及使用核對型態研究，維持 draft 待內容及版權 QA。"}, "reviewStatus": "draft", "updatedAt": "2026-09-27", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "You see 'conduct' in a sentence about leading an orchestra. Which dictionary information should you check first?", {"A": "The word's meaning and part of speech in that context.", "B": "Only the first translation you remember.", "C": "The dictionary cover color.", "D": "The number of pages in the dictionary."}, "A", "Conduct has different meanings and can have different parts of speech, so the sentence context must be matched with the entry.", "先用句子情境縮小詞義，再核對字典的詞性與解釋，不只看第一個翻譯。", ["圈出 conduct 與 leading an orchestra 的情境。", "判斷同一字可能有不同詞義或詞性。", "查字典時先對照 context、part of speech 與 meaning。", "排除 B、C、D，因為記憶、封面與頁數不能判斷此處詞義。", "選 A，確認查詢結果必須與原句功能相配。"], "medium"),
make(2, "Which search query is most precise for finding the English meaning of 'sustainable' in an environmental article?", {"A": "sustainable meaning environmental example", "B": "good word", "C": "English things", "D": "I do not know"}, "A", "A includes the target word and the needed meaning and context, making the search more focused.", "將查詢目的、目標詞與使用情境放入關鍵字，避免過度寬泛。", ["確認目標是 sustainable 的英文意義與環境文章脈絡。", "找同時包含 target word、meaning 與 environmental context 的查詢。", "檢查 A 的三個詞組是否限制搜尋方向。", "排除 B、C、D，因為它們沒有明確目標或查詢任務。", "選 A，回讀確認查詢能產生可用結果。"], "easy"),
make(3, "A dictionary entry labels 'record' as both a noun and a verb. Why should you read the example sentence before choosing a meaning?", {"A": "The sentence shows which word function and meaning fit.", "B": "Examples are only decoration and never matter.", "C": "The longest meaning is always correct.", "D": "A noun and a verb have exactly the same use."}, "A", "Record changes meaning and function depending on use, so an example sentence helps match the entry to the context.", "用詞性標籤與例句共同判斷，不把多義字固定成一個中文意思。", ["先注意 entry 有 noun 與 verb 兩種標籤。", "確認題目要求選符合 context 的 meaning。", "用 example sentence 觀察主詞、搭配與句中功能。", "排除 B、C、D，因為它們忽略例句、長度偏誤或詞性差異。", "選 A，確認例句是連結工具資料與原文的證據。"], "medium"),
make(4, "A search result says, 'This site claims that one method always improves memory.' What should you do before using the claim in a report?", {"A": "Check the source, evidence, date, and another reliable source.", "B": "Copy it because it appears first.", "C": "Use only the headline without opening the page.", "D": "Delete the claim without reading anything."}, "A", "A strong check examines who produced the claim, what evidence supports it, how current it is, and whether another reliable source agrees.", "把網路資訊分成來源、證據、日期與交叉核對四個查驗點。", ["辨認 result 使用 claim 而不是已證實的事實。", "列出 source、evidence、date 與 another reliable source。", "檢查 A 是否包含四個核對動作。", "排除 B、C、D，因為排序、標題或未閱讀都不足以驗證。", "選 A，確認使用前先建立可追溯證據。"], "hard"),
make(5, "You need the pronunciation of 'architecture.' Which tool result is most useful?", {"A": "A dictionary entry with an audio button and phonetic transcription.", "B": "A webpage showing only a large picture of a building.", "C": "A translation list with no sound or pronunciation guide.", "D": "A search result about architects' salaries."}, "A", "An audio button and phonetic transcription directly provide pronunciation evidence for the target word.", "先明確查詢目標是發音，再選含音檔或音標的工具資料。", ["圈出需要 pronunciation 的任務。", "列出最直接的證據形式：audio 與 phonetic transcription。", "檢查 A 兩者都有且對應 architecture。", "排除 B、C、D，因為圖片、翻譯或薪資資料不能提供讀音。", "選 A，確認查詢結果可立即聽讀並核對。"], "easy"),
make(6, "A learner finds two meanings for 'issue.' How can the learner choose the one needed in 'The magazine's latest issue is online'?", {"A": "Match the noun meaning 'edition' with the magazine context.", "B": "Choose the meaning with the shortest definition.", "C": "Use the verb meaning 'to argue' automatically.", "D": "Ignore the words around issue."}, "A", "Magazine and latest identify issue as a noun meaning an edition, not a verb about arguing.", "用上下文名詞搭配與詞性排除其他義項，再回查工具書例句。", ["找出 magazine's latest 與 issue 的搭配。", "判斷 issue 在句中是名詞。", "將 magazine 情境連到 edition 的詞義。", "排除 B、C、D，因為定義長短、動詞義與忽略上下文都不可靠。", "選 A，回讀整句確認 edition 能自然代入。"], "medium"),
make(7, "Which record makes a web search easier to repeat later?", {"A": "The exact keywords, useful URL, access date, and a short note about the result.", "B": "Only the color of the website.", "C": "A memory of seeing the page once.", "D": "The browser's starting screen."}, "A", "Recording search terms, URL, date, and result note makes the inquiry traceable and repeatable.", "把查詢歷程記錄成可追溯資料，而非只保存模糊印象。", ["確認題目問的是 repeat later 的查詢紀錄。", "列出可重現所需的 keywords、URL、date 與 note。", "檢查 A 四項都有且彼此互補。", "排除 B、C、D，因為外觀、記憶與起始畫面無法重建搜尋。", "選 A，確認另一個人也能依紀錄回到結果。"], "medium"),
make(8, "A learner wants a synonym for 'rapid' to use in a formal report. Which check is most important?", {"A": "Check the synonym's meaning, part of speech, tone, and example usage.", "B": "Choose any word that starts with r.", "C": "Use the most unusual word in the list.", "D": "Replace it without rereading the sentence."}, "A", "A synonym must fit meaning, grammatical function, register, and sentence context, not merely resemble the original word.", "查同義字後仍要做語意、詞性、語氣與例句四層核對。", ["確認目標是 formal report 中的替換字。", "列出 meaning、part of speech、tone 與 example usage。", "檢查 A 是否涵蓋正式語境所需的四項條件。", "排除 B、C、D，因為字首、罕見程度或不回讀都不能保證適用。", "選 A，確認替換後句子仍自然且語氣合適。"], "hard"),
make(9, "A search snippet and a dictionary disagree about the meaning of a word. What is the best next step?", {"A": "Open both sources, compare context and authority, and ask the teacher if needed.", "B": "Always trust the snippet because it is shorter.", "C": "Always trust the dictionary without reading its example.", "D": "Choose the meaning that sounds funniest."}, "A", "Opening and comparing the sources reveals context and authority; asking for help is appropriate if the conflict remains.", "遇到工具結果衝突時比較完整內容與來源品質，而不是用固定偏好決定。", ["確認目前有兩個互相衝突的結果。", "找出需開啟完整來源並比較 context 與 authority。", "保留 teacher support 作為仍不確定時的合理下一步。", "排除 B、C、D，因為它們以長短、盲信或玩笑取代查證。", "選 A，確認處理順序能解釋衝突來源。"], "hard"),
make(10, "Before citing an online article about a science fact in homework, which set of information should you save?", {"A": "Author or organization, title, URL, publication or update date, and access date.", "B": "Only the first sentence and a screenshot of the logo.", "C": "The page color and number of advertisements.", "D": "A different article's title from memory."}, "A", "These citation details identify the source and help readers locate and evaluate the information.", "把引用需求轉成來源識別與時間資訊，確保資料可追溯。", ["確認任務是引用 online article 的 science fact。", "列出 author／organization、title、URL、publication／update date、access date。", "檢查 A 是否完整保存來源識別與查閱時間。", "排除 B、C、D，因為它們不能定位或評估原文。", "選 A，確認未來讀者能依紀錄回查來源。"], "medium"),
]

KEYS = ["B", "D", "A", "C", "B", "D", "C", "A", "D", "B"]
CUSTOM_STEPS = [
    ["先讀原句，conduct 和 leading an orchestra 的搭配提示它描述指揮行為。", "在詞典條目中分辨 conduct 的詞性及多個義項。", "用例句檢查哪個解釋能代回原句且語意自然。", "只背第一個翻譯、看封面或頁數都不能消歧。", "答案 B：先核對符合上下文的詞義與詞性，再決定用哪個義項。"],
    ["搜尋前先寫清楚任務：找 sustainable 在環境文章中的英文意思。", "把詞本身、查詢目的和環境語境組成關鍵字。", "比較查詢字是否能排除 unrelated general results。", "good word、English things 和不知道都沒有可操作焦點。", "答案 D：使用 sustainable meaning environmental example，兼顧詞與語境。"],
    ["record 條目同時標 noun 和 verb，代表詞形不能單獨決定用法。", "回到句子確認它在主詞、受詞或動詞位置的功能。", "讀例句，觀察句型與搭配，再選同功能義項。", "最長解釋不必然正確，例句也不是裝飾。", "答案 A：例句能協助對上詞性與句中所需意思。"],
    ["看到 always improves 這種絕對主張，先暫停把搜尋摘要當事實。", "查明作者或機構、證據類型、發布時間及研究限制。", "再找另一個可信來源交叉比對是否支持相同結論。", "排名第一、只看標題或不讀就刪除都沒有完成查核。", "答案 C：確認來源、證據、日期並交叉查證後才引用。"],
    ["題目要的是 architecture 的發音，先辨認目標資訊類型。", "在工具結果中找音訊播放與音標兩種可核對線索。", "聽一次後可對照音標重播，確認重音與音節。", "詞義、圖片或相似字不能直接回答 pronunciation。", "答案 B：選同時提供音檔與音標的結果。"],
    ["把 issue 放回完整片語 The magazine's latest issue。", "由 magazine 和 latest 判斷語境指的是刊物中的一期。", "在字典中優先核對名詞義與期刊／出版物例句。", "爭論或提出問題的動詞義不符合所有格和 magazine 線索。", "答案 D：選用表示一期刊物的名詞義項。"],
    ["可重複的網路查詢必須讓日後能重跑並比較結果。", "留下搜尋詞、實際網址、查詢日期及結果摘要。", "檢查別人是否能依這些資訊找到同一資料並看懂選擇理由。", "只寫標題或『上網找到』會失去可追溯路徑。", "答案 C：完整記錄查詢式、URL、日期和簡短結果註記。"],
    ["找正式報告的 rapid 同義詞，不能只比中文意思近不近。", "先確認替代字仍表達相同速度概念且詞性可放入原句。", "再核對語域是否正式、搭配是否自然。", "只看拼字相似或字典列出的第一個近義詞不足以決定。", "答案 A：同時比對意思、詞性、語域與句子情境。"],
    ["搜尋摘要和字典不一致時，先辨認摘要可能截斷了語境。", "點開兩個原始來源，看完整句子、詞性標記及編者資訊。", "按來源權威性與上下文比較哪個義項適用。", "若核對後仍有歧義，再把原句帶去詢問老師。", "答案 D：打開來源並依語境比較，未解決再尋求協助。"],
    ["引用科學文章前，先保存可辨識且可回查的書目線索。", "記下作者或機構、文章標題、發布日期和網址。", "補上存取日期或段落定位，方便讀者檢查特定主張。", "只存搜尋結果排名、摘要或網站名稱會讓來源難以查證。", "答案 B：保留作者／機構、標題、日期、URL及相關定位資訊。"],
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
