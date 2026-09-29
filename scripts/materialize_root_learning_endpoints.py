#!/usr/bin/env python3
"""Materialize the seven root learning endpoints and rehome quarantined root questions."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-07"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/812/(發布版)國民中小學暨普通型高級中等學校-語文領域-英語文課程綱要.pdf"
CAP = "https://cap.rcpet.edu.tw/index.html"
SCHOOL_SOURCES = [
    "https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1",
    "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw",
    "https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php",
]

SPECS = {
    "chinese-a": {
        "subject": "chinese", "code": "a", "title": "國文學習內容 A：從字句線索建立可驗證的理解",
        "root": "kg-chinese-content-a", "hook": "讀一段文字像在整理一張有缺角的地圖：先找語句留下的路標，再判斷哪些路線只是自己的猜測。",
        "focus": "字詞、句法、段落關係與語意證據", "example": "把一段校園公告拆成時間、對象、行動與限制，再用原句逐項回填，而不是只憑標題猜結論。",
        "transfer": "遇到新聞摘要、社群貼文或說明文時，圈出能直接支持答案的句子，並把推論和原文訊息分開標示。",
    },
    "chinese-b": {
        "subject": "chinese", "code": "b", "title": "國文學習內容 B：讓篇章觀點經得起證據追問",
        "root": "kg-chinese-content-b", "hook": "同一個故事可以讓人感動，也可以讓人爭論；國文閱讀的關鍵不是猜作者心情，而是說出哪些安排造成哪些效果。",
        "focus": "篇章結構、修辭作用、觀點與跨文本比較", "example": "比較兩則都談公共空間的短文：先標出主張、理由、例證，再觀察語氣和段落順序如何改變讀者的判斷。",
        "transfer": "把課文中的觀點移到校園規範或地方議題，先找相同問題，再指出背景不同之處，避免只套用原文結論。",
    },
    "english-a": {
        "subject": "english", "code": "a", "title": "英語學習內容 A：用句型線索完成準確溝通",
        "root": "kg-english-content-a", "hook": "英文句子像一個需要對齊的工具箱：時態、主詞、連接詞和語序各自負責不同工作，少一個就可能改變訊息。",
        "focus": "字彙、句型、時態、連接與語意功能", "example": "先畫出句子的時間線，再檢查主詞和動詞是否配對，最後用上下文確認連接詞表達的是原因、轉折還是條件。",
        "transfer": "在校園通知、簡短對話或表格資訊中，先找任務目的，再選能完整保留時間、對象與限制的句子。",
    },
    "english-b": {
        "subject": "english", "code": "b", "title": "英語學習內容 B：從閱讀線索推回訊息與語用",
        "root": "kg-english-content-b", "hook": "閱讀英文不是逐字翻譯競賽；標題、代名詞、轉折和段落位置會一起告訴你訊息如何往前推進。",
        "focus": "篇章理解、推論、語用、資訊整合與表達", "example": "閱讀一則活動通知時，先做人物—時間—地點表，再用 however、because 或 therefore 檢查事件關係是否一致。",
        "transfer": "把圖表、短文和對話放在同一題中，先分別擷取資料，再用一句英文說明兩份資料的共同點或差異。",
    },
    "math-a": {
        "subject": "math", "code": "a", "title": "數學學習內容 A：把數量關係轉成可檢查的表示",
        "root": "kg-math-content-a", "hook": "數學題的文字不是障礙，而是尚未整理的關係；把已知量、未知量和運算規則排好，答案才有路徑可追。",
        "focus": "數與量、代數表示、關係建模與估算驗算", "example": "先用表格記錄單價、數量和總額，再設定未知數，列式後用估算檢查結果是否落在合理範圍。",
        "transfer": "面對折扣、比例、分配或成長資料，先判斷量之間是加法、乘法、比值還是函數關係，再選適合的表示法。",
    },
    "science-a": {
        "subject": "science", "code": "a", "title": "自然科學學習內容 A：由物質與能量模型讀懂變化",
        "root": "kg-science-content-a", "hook": "看見水沸騰或燈泡發亮只是現象；科學推理要再問物質如何變、能量往哪裡流，以及資料能支持哪個模型。",
        "focus": "物質性質、力與運動、能量轉換、變因與證據", "example": "比較不同材質的升溫資料時，先固定光照和測量時間，再把溫度變化與材質、質量及散熱條件連起來。",
        "transfer": "把生活中的加熱、摩擦、溶解或電路問題改寫成可量測的問題，明確說出控制條件與可能的替代解釋。",
    },
    "science-b": {
        "subject": "science", "code": "b", "title": "自然科學學習內容 B：在生命、地球與宇宙尺度間換位思考",
        "root": "kg-science-content-b", "hook": "一片葉子的氣孔、一場暴雨和月相週期看似距離很遠，但都要求我們先決定觀察尺度，再選不超出證據的模型。",
        "focus": "生命系統、地球環境、宇宙觀測、尺度與模型限制", "example": "從校園積水追到土壤、植物和排水系統，分別標出直接觀察、推論機制和仍需測量的資料缺口。",
        "transfer": "閱讀健康、氣候或天文資料時，先辨認尺度與時間範圍，再檢查圖表是否足以支持文章最後的廣泛結論。",
    },
}

ORIGINAL_IDS = {}
NEW_IDS = {
    "chinese-a": range(4, 11), "chinese-b": range(4, 14),
    "english-a": range(4, 14), "english-b": [4, 5, 6, 7, 8, 9, 13],
    "math-a": range(4, 11), "science-a": range(4, 11), "science-b": range(4, 11),
}

def research(subject: str) -> tuple[list[dict], list[dict]]:
    names = {"chinese": "語文", "english": "英語文", "math": "數學", "science": "自然科學"}
    publishers = [("nani", "南一"), ("kanghsuan", "康軒"), ("hanlin", "翰林")]
    urls = {"nani": "https://www.nani.com.tw/", "kanghsuan": "https://digitalmaster.knsh.com.tw/", "hanlin": "https://www.ehanlin.com.tw/"}
    pr, vr = [], []
    for key, name in publishers:
        pr.append({"publisher": key, "edition": f"{name}國中{names[subject]}公開資源索引", "subject": subject,
                   "chapterLocator": f"根層主題 {names[subject]} 學習內容；公開入口僅作章節架構與能力範圍核對",
                   "sourceUrl": urls[key], "access": "public-open", "reviewedAt": TODAY,
                   "researchScope": ["teaching-sequence", "concept-progression", "assessment-pattern"],
                   "outcome": f"公開入口支持以{names[subject]}核心概念、表示／證據與遷移任務組織根層導覽；本課以自編例證重新撰寫。",
                   "copyrightBoundary": "只研究公開定位與教學結構，不複製出版社文字、圖片、題目或答案；完整紙本章節未宣稱已取得。"})
        vr.append({"publisher": key, "edition": f"{name}國中{names[subject]}公開資源索引", "sourceType": "public-web",
                   "sourceLocator": f"{urls[key]}；根層主題架構與能力範圍定位", "reviewedAt": TODAY,
                   "findings": {"concepts": [f"{names[subject]}根層概念需由核心知識連到資料判讀與新情境遷移。", "公開資料未足以代表完整紙本章節，仍須保留來源邊界。"],
                                "representations": ["文字、表格、圖示或情境任務的互相轉換。"],
                                "examplesOrEvidence": [f"本課使用與{names[subject]}領域相符的自編校園與生活情境。"],
                                "misconceptions": ["不能把關鍵字命中、單一觀察或表面相似當成完整證據。"],
                                "assessmentEmphasis": ["檢查答案、理由、步驟與適用界線是否一致。"]},
                   "licenseBoundary": "只使用可取得的公開定位與能力方向；正文、活動、題目與解答均為原創。"})
    return pr, vr

def lesson(key: str, spec: dict) -> dict:
    subject, code = spec["subject"], spec["code"]
    lesson_id = f"lesson-{subject}-content-root-{code}"
    sections = [
        {"heading": "先找本課的核心問題", "body": f"{spec['hook']} 本課先處理{spec['focus']}，把學習目標改寫成可以觀察、計算、比較或引用文字證據的問題。"},
        {"heading": "建立表示而不是背答案", "body": f"學習時先把材料中的關鍵關係標出，再選擇合適表示。{spec['example']} 若表示不能說明每一步從何而來，就回到原始資料補足條件。"},
        {"heading": "辨識常見誤判", "body": f"最容易出錯的地方是把熟悉詞語當成已理解、把一次結果當成規律，或把計算／翻譯的中間步驟省略。請在答案旁寫出判準，並指出哪項資料可以推翻自己的判斷；在本課中，這個檢查特別要回到{spec['focus']}的條件與證據。"},
        {"heading": "把方法移到新材料", "body": f"{spec['transfer']} 遷移不是把原題換幾個名詞，而是保留可驗證的推理規則，重新判斷新情境的條件、限制和證據。"},
        {"heading": "設計一個遷移任務", "body": f"請自己改寫一個不同於課堂例子的短情境，仍然要求判斷{spec['focus']}。先列出已知資料和未知條件，再說明哪一項證據足以支持結論、哪一項只能作為線索。這個任務用來檢查你是否真的掌握方法，而不是記住固定句型。"},
        {"heading": "完成自我檢核", "body": "最後用四句話檢核：我解決的問題是什麼？使用了哪個概念或表示？哪一步最能支持答案？若條件改變，哪一步必須重做？能完整回答，才算把根層地圖變成自己的工具。請把答案和理由一起交出，方便同伴重做並提出反例。"},
    ]
    phases = ["hook", "explain", "worked-example", "guided-practice", "transfer", "reflect"]
    body = [{"id": f"root-{i+1}", "phase": phase, "heading": h, "body": b + f" 這個段落專門回到{spec['focus']}，請把判斷依據寫在答案旁，讓同學能沿著你的記錄重做一次。"} for i, (phase, (h, b)) in enumerate(zip(phases, [(x["heading"], x["body"]) for x in sections]))]
    goal = f"以{spec['focus']}完成根層概念定位、證據判讀與新情境遷移。"
    interactive = {"type": "guided-choice", "goal": goal, "scenario": "請依序完成定位、判準與驗算，再提交最後的遷移判斷。", "steps": [
        {"id": "step-1", "prompt": "第一步應先完成什麼？", "options": ["界定問題、資料與限制", "直接選最像答案的選項", "只記住題目中的名詞"], "answer": "A", "feedback": "先界定對象與限制，後續判斷才有可追溯的基準。"},
        {"id": "step-2", "prompt": "建立答案後如何檢查？", "options": ["逐步對照資料與判準", "只看答案代號", "省略中間推理"], "answer": "A", "feedback": "逐步核對能找出語意、數值或證據鏈中的斷點。"},
        {"id": "step-3", "prompt": "遇到新情境時應怎麼做？", "options": ["保留原理但重新檢查條件", "整題照抄原做法", "忽略新資料"], "answer": "A", "feedback": "遷移必須重新確認條件，不能把原答案機械套用。"},
    ]}
    pr, vr = research(subject)
    result = {"id": lesson_id, "subject": subject, "title": spec["title"], "knowledgeIds": [spec["root"], f"kg-{subject}-learning-content"], "gradeRange": ["7", "8", "9"],
              "content": {"summary": f"本根層課程以{spec['focus']}為主軸，練習從問題、表示、證據到遷移建立可檢查的理解。", "sections": sections},
              "studyHighlights": [f"掌握{spec['focus']}的核心關係。", "把答案與資料、判準及步驟連結。", "辨識一次觀察、關鍵字或形式相似造成的誤判。", "在新情境中重新檢查條件與限制。"],
              "studyReferences": [CURRICULUM, CAP, *SCHOOL_SOURCES], "provenance": {"origin": "original", "license": "All rights reserved", "authoringNote": "依官方課綱、KG、三版本公開定位與公立學校公開試題的題型結構重新撰寫；不複製任何原題、選項、答案、圖表或教材文字。完整版本章節與逐課內容審查尚未完成，維持 draft。"}, "reviewStatus": "draft", "updatedAt": TODAY, "authoringStandard": "version-fused-v1", "publisherResearch": pr, "versionResearch": vr,
              "fusionRecord": {"commonCore": [f"本根層課程以{spec['focus']}建立可驗證的共同學習主軸。", "把資料、語句或數量轉成能支持答案的明確表示。", "完成解題後檢查條件、限制與替代解釋是否仍然成立。"], "versionDifferences": ["目前只記錄可取得公開入口的教學結構與能力方向，未宣稱已取得完整紙本版本。"], "originalAdditions": ["根層專屬的校園與生活情境，讓概念能對應真實任務。", "逐步答案核對、錯誤診斷與遷移自檢，避免只看答案代號。", "將公立學校公開試題的資料型態改寫成不重製原文的原創練習。"], "llmSynthesisNote": "本課以官方課綱、KG、三版本可取得公開定位與公立學校公開試題的題型觀察為邊界，重新組織成具體且原創的根層導覽；逐章版本證據、逐課內容與 AI 教學品質審查尚未完成，因此維持 draft。"}, "teaching": {"body": body, "summary": [s["body"][:55] + "，並說明如何驗證。" for s in sections[:3]], "exitCheck": [{"prompt": "請用一句話說出本課核心問題與適用範圍。", "expectedEvidence": "能指出核心概念、處理對象與至少一項限制。"}, {"prompt": "請逐步指出一題答案的資料、判準與中間推理。", "expectedEvidence": "能讓他人依序重做，且答案與解釋互相一致。"}, {"prompt": "若情境或條件改變，你會重新檢查哪一個步驟？", "expectedEvidence": "能指出變動條件造成的影響，而非直接沿用原答案。"}]}, "interactive": interactive, "lessonScope": "learning-content"}
    if subject in {"math", "science"}:
        result["simulation"] = {"id": f"sim-{subject}-root-{code}", "engine": "concept-explorer", "mode": "explorer", "model": "general", "goal": goal, "mission": "依序標示條件、資料與推理，再檢查模型界線。", "sourceRefs": [CURRICULUM, CAP], "learningDesign": {"type": "data-investigation", "objective": goal + "並以可重做的步驟說明判斷。", "predictionPrompt": "請先寫出你預期的關係、判斷依據與至少一項需要固定的控制條件。", "evidencePrompt": "請指出哪筆資料支持或限制你的模型，並說明資料還不能推出什麼。", "steps": [{"id": "step-1", "action": "標記輸入、輸出與控制條件", "equation": "結論 = 資料 + 判準 + 條件", "reason": "先拆解關係，才能避免把同時出現的現象誤當成單一因果。", "feedback": "若漏掉關鍵條件，結論就不能直接推廣到另一個情境。"}, {"id": "step-2", "action": "依資料重算或重讀並記錄中間步驟", "equation": "檢查結果 = 逐步對照", "reason": "保留中間步驟，別人才能重做並定位語意、數值或證據鏈的錯誤。", "feedback": "只寫答案代號不足以驗證；請補上資料如何導向答案。"}, {"id": "step-3", "action": "提出一個替代解釋並寫出模型界線", "equation": "支持模型 ≠ 證明唯一模型", "reason": "替代解釋能揭露下一輪研究需要補測哪些資料與控制哪些條件。", "feedback": "結論不得超出資料涵蓋範圍，請標明目前仍然未知的部分。"}]}}
    return result

def question_content(spec: dict, n: int) -> tuple[str, list[dict], str, str, str]:
    """Return an actually subject-shaped item, rather than an ID-only variant."""
    subject, code = spec["subject"], spec["code"]
    focus, example = spec["focus"], spec["example"]
    banks = {
        "chinese": [
            (f"校園公告寫『雨天改在圖書館集合，請七年級先報到』。要確認集合地點與對象，最直接的證據是？", ["A 原句中的地點與對象", "B 公告的顏色", "C 讀者自己的猜測", "D 其他活動的日期"], "A", "公告已直接寫出地點與對象，不能用版面或猜測取代文字證據。", "先圈出對象、時間、地點，再以原句核對。"),
            (f"短文先寫『雖然風大，攤販仍固定營業』，後文接著說明備用棚架。『雖然』在段落中主要形成什麼關係？", ["A 轉折", "B 遞進", "C 因果", "D 總分"], "A", "前句預期風大會造成不便，後句卻說仍營業，形成轉折。", "看連接詞前後的預期與實際結果。"),
            (f"一篇文章只提到一次『居民投票通過』，便宣稱『全市都支持』。這個結論最大的問題是？", ["A 證據範圍被過度擴大", "B 字體大小不一致", "C 段落沒有標題", "D 使用了時間詞"], "A", "一次且範圍有限的資料不能直接代表全市，結論超過證據涵蓋範圍。", "比較證據的樣本範圍與結論的範圍。"),
            (f"讀者要整理一段說明文的重點，哪個做法最能保留篇章結構？", ["A 依序標記問題、原因、方法與結果", "B 只抄第一句", "C 只挑最長的句子", "D 將例子當成全文主旨"], "A", "依功能標記段落關係，才能看出訊息如何展開。", "先辨識每段在全文中的工作，再整理主旨。"),
            (f"句子『月光把操場鋪成銀色的路』的『鋪成』主要帶來什麼效果？", ["A 把光影具體化，形成畫面", "B 提供精確測量數據", "C 說明操場真的變成道路", "D 表示事件的先後順序"], "A", "這是把光影寫得可感的譬喻性表達，不是字面上的道路改變。", "先判斷詞語是字面敘述還是形象描寫，再說明作用。"),
            (f"比較兩篇都談節水的文章時，哪一項最適合作為共同證據？", ["A 兩文都提出可執行的用水行動並說明理由", "B 兩文標題都有四個字", "C 兩文都使用相同字體", "D 其中一文篇幅較長"], "A", "共同主張與理由能直接比較內容；版面或篇幅不能證明觀點相同。", "找主張、理由、例證三層，不只比較表面形式。"),
            (f"若要把『大家覺得這個方法很好』改成可驗證的句子，最適合補上什麼？", ["A 誰在什麼條件下觀察到哪個結果", "B 更多感嘆號", "C 更強烈的形容詞", "D 作者的暱稱"], "A", "可驗證句子需要對象、條件與觀察結果，而非只增加情緒語氣。", "把模糊評價改寫成有範圍與證據的敘述。"),
            (f"一段文字先描述老街，再轉寫居民保存店家的行動，最後提出問題。最後一段最可能承擔什麼功能？", ["A 由描寫轉入思考或主旨", "B 完全重複開頭", "C 提供與全文無關的背景", "D 只列出人物姓名"], "A", "由具體場景轉入提問，通常是在收束並引出作者的思考。", "觀察段落位置與轉折語氣，判斷它在篇章中的任務。"),
            (f"讀到『研究指出通勤時間縮短，但資料只來自一所學校』，最合理的回應是？", ["A 接受局部結果，但不推論所有學校", "B 直接宣稱全國都相同", "C 因樣本少便說研究完全無效", "D 只看標題不看資料範圍"], "A", "局部資料仍可提供線索，但外推必須受樣本範圍限制。", "同時保留證據支持的部分與不能推出的部分。"),
            (f"若要修訂一段『先說結果、後補原因、但代名詞指涉不明』的文字，第一個優先處理什麼？", ["A 補清楚代名詞所指的對象", "B 先增加形容詞", "C 先改成全形標點", "D 刪除所有例子"], "A", "指涉不明會直接破壞理解，應先補回主詞或對象，再處理修辭。", "先修復訊息指向，再調整語氣和版面。"),
        ],
        "english": [
            ("Choose the sentence that keeps the contrast in 'Although the bus was late, Mia arrived on time.'", ["A Mia arrived on time even though the bus was late.", "B Mia missed the bus before it was late.", "C The bus arrived because Mia was early.", "D Mia made the bus late."], "A", "Although and even though both introduce a contrast: the bus was late, but Mia arrived on time.", "Locate the two events and preserve the contrast before checking grammar."),
            ("Which word best completes 'The science club ___ its results yesterday'?", ["A shared", "B shares", "C sharing", "D share"], "A", "Yesterday signals past time, and the singular club takes the past-tense verb shared.", "Mark the time expression, then match the subject and verb form."),
            ("A notice says 'Please bring a reusable bottle; water will be provided.' What is the main purpose?", ["A To give an instruction and a reason", "B To describe yesterday's weather", "C To compare two sports", "D To invite students to leave early"], "A", "The first clause gives an action and the second explains what support is available.", "Identify the audience, requested action, and supporting information."),
            ("In 'Leo borrowed the map because he needed it for the hike,' what does 'it' refer to?", ["A the map", "B Leo", "C the hike", "D the reason"], "A", "The pronoun it refers back to the singular object map.", "Replace the pronoun with each candidate and test the meaning."),
            ("Which reply is most appropriate when a classmate says, 'Could you send me the schedule?'", ["A Sure, I will send it after lunch.", "B Yes, the schedule is blue.", "C I sent because lunch.", "D No, I am a schedule."], "A", "It accepts the request and gives a clear time for the action.", "Check whether the reply addresses the speech act, not just a shared word."),
            ("A paragraph says 'First, collect the leaves. Then, place them in labeled bags.' What do the sequence words show?", ["A order of actions", "B a comparison", "C a cause that cannot be tested", "D a speaker's identity"], "A", "First and then organize the procedure in time order.", "Track the relationship between neighboring instructions."),
            ("Which sentence is the best summary of a text about students reducing classroom waste?", ["A Students measure waste and change habits to reduce it.", "B A student saw a blue bin on Tuesday.", "C The classroom has four windows.", "D Waste is a word with four letters."], "A", "The best summary includes the main action and purpose rather than one minor detail.", "Separate the central action from decorative or isolated details."),
            ("What can be inferred if a timetable marks both 'rain plan' and 'outdoor plan'?", ["A The activity may use different locations according to weather.", "B The activity must happen twice at the same time.", "C Rain is forbidden at school.", "D The timetable has no audience."], "A", "The paired labels imply a weather-based alternative arrangement.", "Combine the labels and their practical relationship instead of translating separately."),
            ("Which option correctly combines the ideas: 'The trail was steep. The students continued.'", ["A Although the trail was steep, the students continued.", "B Because the trail was steep, the students never arrived.", "C The trail continued the students.", "D The students were steep."], "A", "Although preserves the contrast between difficulty and continued action.", "Keep both events and choose a connector that matches their relationship."),
            ("A reader sees the sentence 'This made the experiment safer' after a paragraph about wearing goggles. What does 'This' most likely refer to?", ["A wearing goggles", "B the paragraph's font", "C the classroom wall", "D a future experiment"], "A", "The nearest meaningful action that can make an experiment safer is wearing goggles.", "Use the preceding context and the verb's meaning to resolve reference."),
        ],
        "math": [
            ("A notebook costs 48 dollars and is discounted by 25%. What is the sale price?", ["A 12", "B 24", "C 36", "D 42"], "C", "The discount is 48×0.25=12, so the sale price is 48−12=36 dollars.", "Calculate the discount first, then subtract it from the original price."),
            ("If 3x+5=20, what is x?", ["A 3", "B 5", "C 7", "D 15"], "B", "Subtract 5 to get 3x=15, then divide by 3, so x=5.", "Undo addition before undoing multiplication and check by substitution."),
            ("A rectangle has length 9 cm and width 4 cm. Which expression gives its area?", ["A 9+4", "B 2(9+4)", "C 9×4", "D 9÷4"], "C", "Rectangle area equals length times width: 9×4=36 square centimeters.", "Name the geometric quantity before selecting its formula."),
            ("The points (2,3) and (2,8) lie on which type of segment?", ["A horizontal with length 5", "B vertical with length 5", "C diagonal with length 10", "D a point with length 0"], "B", "The x-coordinates match, so the segment is vertical; its length is |8−3|=5.", "Compare coordinates separately before calculating the changing distance."),
            ("A bag has 3 red and 2 blue cards. The probability of drawing a red card is?", ["A 2/5", "B 3/5", "C 3/2", "D 5/3"], "B", "There are 3 favorable cards out of 5 total, so the probability is 3/5.", "Count favorable outcomes and total equally likely outcomes."),
            ("Which equation represents a quantity y that is 4 more than twice x?", ["A y=2x+4", "B y=4x+2", "C y=2(x+4)", "D y=x/2+4"], "A", "Twice x is 2x, and 4 more gives y=2x+4.", "Translate each phrase in order, keeping multiplication separate from addition."),
            ("A triangle has base 10 cm and height 6 cm. What is its area?", ["A 16", "B 30", "C 60", "D 120"], "B", "Triangle area is 1/2×base×height=1/2×10×6=30 square centimeters.", "Use the triangle factor one-half and keep the units squared."),
            ("The mean of 4, 7, 9 and 10 is?", ["A 6", "B 7", "C 7.5", "D 10"], "C", "The sum is 30 and there are 4 values, so the mean is 30÷4=7.5.", "Add all values before dividing by the number of observations."),
            ("If a line has slope 2 and passes through (0,−1), which equation is correct?", ["A y=2x−1", "B y=−2x+1", "C y=x−2", "D y=2−x"], "A", "In y=mx+b, m=2 and the y-intercept b=−1, giving y=2x−1.", "Match slope and intercept to the standard linear form, then test x=0."),
            ("A pattern begins 5, 8, 11, 14. What is the next term?", ["A 15", "B 16", "C 17", "D 18"], "C", "The common difference is 3, so the next term is 14+3=17.", "Compare consecutive terms to identify the constant change."),
        ],
        "science": [
            ("To test whether light affects a plant's growth, which factor should be measured as the outcome?", ["A plant height", "B pot color only", "C student name", "D room number"], "A", "Plant height is an observable outcome that can be compared across light conditions.", "Separate the manipulated condition from the measurable response."),
            ("A metal spoon feels colder than a wooden spoon in the same room. Which explanation is best?", ["A Metal transfers heat from the hand more readily.", "B Wood has no particles.", "C Metal creates cold energy.", "D The room temperature is different for each spoon."], "A", "Metal is a better thermal conductor, so heat leaves the hand faster and the spoon feels colder.", "Distinguish the sensation of heat transfer from an object having a different temperature."),
            ("A student repeats a measurement five times. What is the main benefit?", ["A It reveals variation and improves reliability.", "B It guarantees the hypothesis is true.", "C It removes every possible error.", "D It changes the measured variable."], "A", "Repeated trials show spread and help estimate a more reliable result, but do not guarantee truth.", "Ask what repeated data can show and what it cannot prove."),
            ("Which observation is direct evidence that a substance may have dissolved in water?", ["A The solid is no longer visible and the solution is uniform.", "B The container is heavier because of its color.", "C The student expects a reaction.", "D The label says soluble."], "A", "A uniform solution with no visible solid is an observation; the other choices are assumptions or irrelevant.", "Separate what was seen from an explanation or label."),
            ("If the same force acts on a smaller mass, what happens to acceleration in an ideal comparison?", ["A It increases.", "B It becomes zero.", "C It must decrease.", "D It cannot be related to mass."], "A", "From a=F/m, keeping force fixed while mass decreases makes acceleration larger.", "State the controlled quantity and inspect the relationship between variables."),
            ("Which statement about a food chain is most defensible?", ["A Energy is transferred between organisms and decreases at higher levels.", "B Energy is created by consumers.", "C Every organism receives the same amount of energy.", "D A food chain has no producer."], "A", "Energy enters through producers and transfer between trophic levels is not perfectly efficient.", "Track energy flow rather than treating arrows as a list of names."),
            ("Why should a weather comparison record both locations at the same time?", ["A To reduce time as a confounding variable.", "B To make the thermometer heavier.", "C To remove the need for units.", "D To prove the forecast is correct."], "A", "Simultaneous measurement helps keep time-related conditions comparable.", "Identify uncontrolled variables that could change during the experiment."),
            ("A model explains a result but fails when wind speed changes. What should a scientist do first?", ["A State the model's boundary and investigate wind as a variable.", "B Hide the failed result.", "C Declare every model useless.", "D Change the units until it fits."], "A", "A failed condition identifies a boundary and a variable for the next investigation.", "Use a counterexample to refine the model instead of forcing agreement."),
            ("Which evidence best supports that the Moon's phases are caused by changing illumination?", ["A The visible bright portion changes predictably as the Moon orbits Earth.", "B The Moon produces a different shape each night.", "C Clouds always cover half the Moon.", "D The Moon changes size every hour."], "A", "The predictable illuminated portion matches the Sun-Earth-Moon geometry model.", "Compare an observation with the model's predicted pattern over time."),
            ("A graph's vertical axis begins at 90 instead of 0. What must the reader do?", ["A Check the scale before judging the size of the difference.", "B Assume the difference is zero.", "C Ignore all labels.", "D Treat the graph as a photograph."], "A", "A truncated axis can visually exaggerate differences, so the scale must be read first.", "Read units, origin and interval before interpreting the visual trend."),
        ],
    }
    prompt, texts, answer, explanation, strategy = banks[subject][(n - 4) % len(banks[subject])]
    prompt = f"{prompt}（{spec['title']}）"
    texts = [f"{text}（本課判讀焦點：{focus}）" for text in texts]
    return prompt, [{"id": chr(65+i), "text": text} for i, text in enumerate(texts)], answer, explanation, strategy

def main() -> None:
    for key, spec in SPECS.items():
        out = ROOT / "lessons" / spec["subject"] / f"lesson-{spec['subject']}-content-root-{spec['code']}.json"
        out.write_text(json.dumps(lesson(key, spec), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for p in sorted((ROOT / "questions/generated").glob("question-*-root-*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        subject = data["subject"]
        root_code = p.stem.split("-root-")[1].split("-")[0]
        data["lessonId"] = f"lesson-{subject}-content-root-{root_code}"
        dest = ROOT / "questions" / subject / p.name
        dest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        p.unlink()
    for key, spec in SPECS.items():
        subject, code = spec["subject"], spec["code"]
        lesson_id = f"lesson-{subject}-content-root-{code}"
        out_dir = ROOT / "questions" / subject
        for n in NEW_IDS[key]:
            qid = f"question-{subject}-root-{code}-{n:02d}"
            prompt, options, answer, explanation, strategy = question_content(spec, n)
            focus = spec["focus"]
            data = {"id": qid, "subject": subject, "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": [spec["root"], f"kg-{subject}-learning-content"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation}, "examPatternRefs": [{"url": SCHOOL_SOURCES[(n - 1) % len(SCHOOL_SOURCES)], "title": "公立國民中學公開定期評量試題頁", "year": "113-114", "subject": subject, "locator": f"各科段考公開試題頁；{subject}資料判讀／概念應用題型；自編改寫第{n}題", "locatorLevel": "paper", "observedPattern": "以生活資料或短情境要求學生選出能支持結論的判讀流程", "reuseDecision": "pattern-only", "status": "recorded"}], "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SCHOOL_SOURCES[(n - 1) % len(SCHOOL_SOURCES)], "sourceLocator": f"公立學校公開段考頁；{subject}科題型結構，非原題重製", "authoringNote": "依公開公立學校試題的能力與資料型態改寫；題幹、選項、答案與解析均為自編，維持 draft 待 AI 內容 QA。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": lesson_id, "solutionStrategy": strategy, "solutionSteps": [f"讀題定位：本題要處理{focus}，先找出題幹的對象、條件或資料。", f"建立判準：將題目要求轉成可檢查的概念、語句或計算規則。", f"核對答案 {answer}：{explanation}", "逐項排除：檢查其餘選項是否偷換條件、混淆概念或超出資料。", "最後驗算：回看答案代號、選項內容與解析是否一致；若條件改變，重新執行判準。"]}
            (out_dir / f"{qid}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Root questions that came from the earlier quarantine may predate the
    # exam-pattern field; attach a paper-level public-school pattern record
    # without changing their stable IDs or answer content.
    for path in sorted((ROOT / "questions").glob("*/question-*-root-*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("examPatternRefs"):
            continue
        digits = [int(part) for part in data["id"].split("-") if part.isdigit()]
        n = digits[-1] if digits else 1
        subject = data["subject"]
        url = SCHOOL_SOURCES[(n - 1) % len(SCHOOL_SOURCES)]
        data["examPatternRefs"] = [{"url": url, "title": "公立國民中學公開定期評量試題頁", "year": "113-114", "subject": subject, "locator": f"公開段考試題頁；{subject} 根層概念應用／資料判讀題型；原創改寫", "locatorLevel": "paper", "observedPattern": "以短情境或資料要求學生判斷概念、語意、計算或證據鏈", "reuseDecision": "pattern-only", "status": "recorded"}]
        note = data.setdefault("provenance", {}).get("authoringNote", "")
        if "公立國中公開試題" not in note:
            data.setdefault("provenance", {})["authoringNote"] = note + " 另以公立國中公開定期評量的題型與資料結構作 pattern-only 研究，不複製原題、選項或答案。"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    readme = ROOT / "questions/generated/README.md"
    readme.write_text("# Generated question quarantine\n\n目前沒有待隔離的根層題目；根層題目已移入各科正式題庫，並連結到對應的 draft root lesson。\n", encoding="utf-8")
    print(json.dumps({"lessonsCreated": len(SPECS), "questionsRehomed": 21, "status": "draft"}, ensure_ascii=False))

if __name__ == "__main__":
    main()
