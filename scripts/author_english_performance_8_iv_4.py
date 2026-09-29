#!/usr/bin/env python3
"""Write the missing, unit-specific English 8-IV-4 fusion manuscript and items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-english-performance-8-iv-4"
LESSON_PATH = ROOT / "lessons/english/lesson-english-performance-8-iv-4.json"
CURRICULUM_URL = "https://www.naer.edu.tw/upload/1/16/doc/812/(%E7%99%BC%E5%B8%83%E7%89%88)%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F-%E8%8B%B1%E8%AA%9E%E6%96%87%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81.pdf"
NANI_URL = "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMxTDNCMFlWOHlNalF4WHpNMU1qUTNPRGxmT0RRME1qWXVjR1Jt&fname=LOGGYSOKWW10A1IH50LKKPHGPK30WT3414JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP3435GCQP3504B0UWYWWXUW50OOA0A0YWPOXX21JCLKSWIGQOB4SWHCUS30A110"
KANGHSUAN_URL = "https://www.msjh.tp.edu.tw/uploads/1722920307628qqQMRB3p.pdf"
HANLIN_URL = "https://www.dyjhs.tyc.edu.tw/modules/tad_uploader/index.php?cat_sn=124&cfsn=2165&name=5-1-1-2%E8%8B%B1%E8%AA%9E%E6%96%87.pdf&op=dlfile"
NEIHU_URL = "https://www.nhjh.tp.edu.tw/uploads/1675417163713PBpnsLYp.pdf"
GUOCHANG_URL = "https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87.pdf"

SECTIONS = [
    ("先把「我看到的」和「我猜的」分開", "班級交流牆上有一則自編訊息：「有位同學帶了自己的午餐，沒有拿分享桌上的食物。」這句話只交代一位同學做了什麼；它沒有說明原因，也沒有說明任何群體的規範。若立刻補上「他一定不喜歡我們」或「他們都不能吃這種食物」，就是把觀察偷換成推測。讀文化情境時，先用兩欄寫下可直接找到的文字與尚待查證的解釋；尊重不是停止思考，而是不把猜測冒充知識。"),
    ("文化不是一張貼紙", "習俗可能和家庭記憶、信念、地方環境、世代經驗或個人選擇有關；同一地區的人也可能做法不同。課綱的8-Ⅳ-4連結C-Ⅳ-3，要求了解並尊重文化習俗，不是要學生替整個族群背一套固定答案。看見某個例子，只能先說「這份資料中的某位受訪者……」；要擴大到社群或地區，必須有相稱且可追溯的資料，並保留差異。"),
    ("比較要有共同問題，也要有範圍", "如果兩份資料談不同習俗，別急著排誰比較特別。先問同一個問題，例如「參與者如何表示歡迎？」再記來源、地點、對象和時間；接著分清楚資料明說的做法與作者的解釋。可寫「在這份校方介紹中，受訪者提到……」，不寫「所有人都……」。若兩人對同一做法有不同經驗，差異本身就是資料，不應逼其中一人替整群人定論。"),
    ("開口前，先給對方選擇權", "想了解一項自己不熟悉的習俗，可以問：「Would you feel comfortable telling us what this means to you?」對方可以分享，也可以婉拒；不需要當眾交代家庭、信仰或身分。若活動涉及飲食、照片、服飾或稱謂，先提供選項與資訊，再讓當事人決定是否參與。善意不會自動變成許可；好奇也不能取代同意。"),
    ("示範：替交流展板修一段說明", "社團收到兩則自編訪談摘要：A同學說家中某次聚餐會先向長輩問候；B同學說親友聚會通常直接開始用餐。兩份回答不能用來判定誰「更尊敬家人」，因為受訪者談的是不同家庭經驗。較準確的展板可以寫：「The two students described different ways their families begin a meal.」接著註明這是兩位受訪者的描述，不代表所有家庭。讀者因此同時看見共同情境、個人差異和證據邊界。"),
    ("練習：四格檢查，不替證據加戲", "面對文化短文或題組，依序標記四件事：誰提供資訊、文字確實說了什麼、哪些結論仍是推論、是否需要再查資料或詢問同意。再檢查選項：它有沒有把一個人說成所有人？有沒有把差異排成高低？有沒有把「沒提到」說成「不存在」？先排除越過證據範圍的句子，再選能同時保留事實、脈絡與人的選項。"),
    ("遷移：設計一場不要求誰當代表的文化分享", "規劃班級展覽時，先讓每位分享者自行挑選願意公開的內容，標清資料來自本人、家庭或可查證的公共來源；不邀請某位同學「代表某國／族群」，也不把未經同意的照片貼上牆。英文標籤可用「In this interview…」「One family described…」「Practices may vary…」限定範圍。最後請同伴逐句核對：來源在哪裡？文字有沒有擴大？當事人能否修改或撤回？這比背誦一串國家習俗更能把尊重落實在行動裡。"),
]

RESEARCH = [
    {
        "publisher": "nani", "edition": "南一標示公校七年級計畫，Lesson 3節慶閱讀；跨年級主題參照，非8-Ⅳ-4指定課本原文",
        "sourceType": "public-web", "sourceLocator": "新北市丹鳳高中國中部公校計畫PDF p.17，Lesson 3 *How Do You Celebrate the New Year?* pp.53–60；列出圖像／pre-reading引導及scanning。此為校方教學計畫，非出版社正文。",
        "reviewedAt": "2026-09-28",
        "findings": {
            "concepts": ["先由圖片與預讀問題喚起對節慶文本的背景假設，再以文章線索確認內容。", "校方計畫把掃讀用於定位特定資訊；它沒有提供足以重建出版社課文或完整活動的內容。"],
            "representations": ["可查核表徵是課次名稱、頁碼、圖像預測及掃讀策略，不是可閱讀的完整教材頁面。"],
            "examplesOrEvidence": ["課程計畫列出New Year節慶閱讀、預讀問題與圖片猜測；本課只取先提出問題再回文定位的高層次方法。"],
            "misconceptions": ["節慶名稱與單一圖片不能代表一個國家所有家庭的做法，也不能代替逐句證據。"],
            "assessmentEmphasis": ["公校計畫以提問討論、課堂參與和口說等方式檢視理解；未呈現該出版社原題或標準答案。"],
        },
        "licenseBoundary": "只記錄公校版本標示、課次、頁碼及教學策略；不複製課本或習作文字、圖片、題目、答案，也不將七年級計畫說成目標單元原書。",
    },
    {
        "publisher": "kanghsuan", "edition": "康軒標示公校九年級資源班計畫；跨年級能力參照，非目標單元出版社章節",
        "sourceType": "public-web", "sourceLocator": "臺北市立民生國中113學年度資源班英語計畫PDF pp.1–2；明列8-Ⅳ-4及C-Ⅳ-2，並有飲食、節慶與emoji等不同單元目標。課程未提供出版社完整學生頁。",
        "reviewedAt": "2026-09-28",
        "findings": {
            "concepts": ["計畫把文化理解列入英語年度目標，並和生活情境語言及簡易溝通並行。", "不同週次分開處理食物、節慶、符號與其他議題，不能把它們合併成某一個課本章節。"],
            "representations": ["可見的是週次、單元標題、學習目標和評量方式；沒有提供教材段落或原始題目供逐頁比對。"],
            "examplesOrEvidence": ["計畫中的食物與節慶目標提示可從具體日常經驗進入文化議題；本課另設全新校園交流案例。"],
            "misconceptions": ["版本標示和課綱代碼不等於該版課本已呈現同一個例子或固定文化答案。"],
            "assessmentEmphasis": ["校方課程計畫描述基本英語溝通及課堂活動，未提供足以認定出版社評量設計的完整證據。"],
        },
        "licenseBoundary": "僅使用公開校方計畫確認版本標示與能力範圍；不複製資源班教材、題目或答案，也不把跨年級計畫當成康軒目標課次原書。",
    },
    {
        "publisher": "hanlin", "edition": "翰林標示公校九年級計畫，Unit 6文化差異與關懷行善；跨年級相關單元參照",
        "sourceType": "public-web", "sourceLocator": "桃園市立大有國中英語領域計畫PDF pp.13–14：標示翰林版九上，Unit 6 *The Sign Which You Used Is Not OK*，並列C-Ⅳ-3、多元文化、來源查核及跨文本閱讀議題。校方計畫不是出版社課文。",
        "reviewedAt": "2026-09-28",
        "findings": {
            "concepts": ["校方將文化差異與關懷議題並置，並同列習俗理解、尊重與綜合資訊推論。", "計畫特別提到來源查證和跨文本比較，可將尊重延伸到核實說法而非只猜他人意圖。"],
            "representations": ["可定位的表示包括單元名稱、學習表現代碼、議題內涵及課程計畫的週次安排。"],
            "examplesOrEvidence": ["公校計畫列出8-Ⅳ-4相關的文化差異議題與簡易英語溝通；本課不沿用其 sign 情境或教材文字。"],
            "misconceptions": ["看見一個符號或個人反應，不足以推斷整個群體的習俗、意圖或價值排序。"],
            "assessmentEmphasis": ["計畫列口說、討論、紙筆和檔案等校本評量類型，未公開該課本實際題目與逐題配分。"],
        },
        "licenseBoundary": "只記錄公校計畫公開的版本標示、課次定位與學習代碼；不轉錄課本或習作內容、插圖、題目或答案。",
    },
]

FUSION = {
    "commonCore": [
        "以英語理解生活中的文化相關訊息，分清明載事實、個人觀點與尚待查證的推論。",
        "從具體文本或交流情境辨認文化差異，使用可定位的證據和適切語言回應。",
        "尊重與欣賞差異時保留地區、家庭、個人及資料來源的範圍，不把單一案例擴大成普遍規則。",
    ],
    "versionDifferences": [
        "目前能讀到的是三種出版社標示的公校課程計畫而非三版完整課本：南一相關計畫偏節慶閱讀的圖像預測與掃讀；康軒計畫把文化目標分散在食物、節慶及符號等生活主題；翰林計畫將文化差異與關懷議題、來源查核並列。這是校方公開計畫呈現的差異，不等於出版社原書逐頁比較。",
    ],
    "originalAdditions": [
        "新增觀察／推論／查證三分法，避免以一個人的行為推定整個群體。",
        "新增同一問題、多份來源、地點與對象範圍並列的比較表述方法。",
        "新增同意、拒答權、代表負擔與撤回權等交流倫理，並以獨立校園展覽任務遷移。",
    ],
    "llmSynthesisNote": "我依官方英語文8-Ⅳ-4及C-Ⅳ-3、該課Knowledge Graph，實際閱讀南一、康軒、翰林三種版本標示的公校課程計畫，抽取節慶文本預讀／掃讀、生活議題情境、文化差異與來源核實等互補取徑，再以全新班級交流情境重新組織成七段教學。可用資料是校方課程計畫，不是出版社課本全文；因此不假稱完成三版指定章節逐頁融合，也不複製其課文、題目或圖片。 lesson維持draft，使用者另交ChatGPT審查。",
}

INTERACTIVE_STEPS = [
    {"id": "step-1", "prompt": "A student brings lunch from home and skips the shared dish. What does the note itself support?", "text": "先鎖定可觀察的行為，別替當事人補上原因。", "options": ["The student chose lunch from home in this instance.", "The student dislikes every local food.", "The student's whole family follows one rule."], "answer": "A", "retryHint": "哪個選項只重述訊息明說的事，沒有猜動機？", "feedback": "選A。訊息只記錄這一次的選擇；原因和群體規範都沒有提供。"},
    {"id": "step-2", "prompt": "You want to ask about a classmate's family practice. Which opening protects their choice?", "text": "問題要有禮貌，也要讓對方能不分享。", "options": ["Tell everyone why your family does that.", "Would you feel comfortable telling us what it means to you?", "People from your background all do this, right?"], "answer": "B", "retryHint": "找出同時詢問意願、又沒有要求對方替整個群體發言的句子。", "feedback": "選B。它先確認對方是否願意分享，並把說明範圍留在本人經驗。"},
    {"id": "step-3", "prompt": "Two students describe different ways their families begin a meal. Which caption is supported?", "text": "兩筆個人資料可以呈現差異，不能替所有家庭下結論。", "options": ["One family is more respectful than the other.", "All families in the two communities eat differently.", "The two students described different ways their families begin a meal."], "answer": "C", "retryHint": "選一個能準確保留受訪者數量與資料範圍的句子。", "feedback": "選C。它忠實呈現兩位學生的敘述，沒有排名或擴大代表性。"},
    {"id": "step-4", "prompt": "A student exhibit uses an online photo and a broad claim about a community. What should the team do first?", "text": "文化分享同時要核實資料、標示來源並取得影像使用同意。", "options": ["Keep it because the picture is online.", "Ask the student from that community to approve everything.", "Check the source and scope, seek image permission, and narrow the claim."], "answer": "C", "retryHint": "公開可見不等於可任意使用；也不要把查核責任丟給一位同學。", "feedback": "選C。它同時處理來源、範圍與同意，且不要求任何人代表整個群體。"},
]

QUESTIONS = [
    {"prompt": "A draft caption says, ‘Everyone in the neighborhood follows this greeting.’ The only source is one student's interview. What is the best revision?", "options": ["Keep the sentence; one interview is enough.", "Remove the source so the sentence sounds certain.", "Write, ‘One student described this greeting in their family.’", "Say the greeting is better than other greetings."], "answer": "C", "strategy": "先比對主張範圍與來源數量，再把句子縮回受訪者實際說明的範圍。", "why": "一位學生的訪談只能支持該受訪者描述的家庭經驗，不能證明社區每個人都如此。"},
    {"prompt": "At a class potluck, a guest declines a dish. Which response is most respectful and useful?", "options": ["You must try it to understand our culture.", "Would ingredient information or another option be helpful?", "People like you never eat this dish.", "I will tell the class why you refused."], "answer": "B", "strategy": "先提供資訊和替代選項，不追問私事，也不替對方指定身分原因。", "why": "B讓對方自行決定是否需要成分資訊或替代選項；其餘選項強迫、概括或公開隱私。"},
    {"prompt": "Two interviewees from the same town describe a holiday differently. What should a student writer do?", "options": ["Choose the answer that sounds more traditional.", "Ask one interviewee to correct the other.", "Combine both answers into one rule for the town.", "Report both accounts with each speaker's context."], "answer": "D", "strategy": "把不同敘述各自連回說話者與情境，保留變異，不替資料製造共識。", "why": "兩筆不同經驗可以並存；沒有額外證據時，不應排名、合併或推成全鎮規則。"},
    {"prompt": "A student says, ‘My family does not follow that custom.’ Which reply invites learning without making the student a spokesperson?", "options": ["Thanks for sharing. Would you like to say more, or shall we use another source?", "Then your family must have forgotten its culture.", "Please explain how everyone in your community feels.", "That proves the custom is not real."], "answer": "A", "strategy": "承認個人經驗，詢問是否願意續談，並提供不由同學承擔代表工作的查證路徑。", "why": "A尊重對方分享的界線，也承認一個家庭的經驗不會證實或推翻整體習俗。"},
    {"prompt": "The class wants to display a visitor's clothing photo. What is the first ethical step?", "options": ["Post it because the visitor joined the event.", "Ask permission for this specific photo and explain where it will appear.", "Guess the clothing's meaning from its color.", "Ask a classmate with a similar background to decide."], "answer": "B", "strategy": "先確認影像本人對特定用途的知情同意，再處理標示與脈絡。", "why": "參加活動不等於同意公開照片；顏色也不足以推斷意義，旁人不能代替當事人授權。"},
    {"prompt": "A visitor corrects how you pronounce their name. What is the best response?", "options": ["Thank you. Could you say it once more so I can practice?", "Your name is too difficult, so I will use a nickname.", "I know the correct pronunciation already.", "Names are not important at school."], "answer": "A", "strategy": "接住更正、請求示範並實際練習；不把方便自己當成改名理由。", "why": "A以具體行動採納當事人的資訊；其他選項否定、忽略或擅自改動對方稱謂。"},
    {"prompt": "A website says a custom is ‘common in some families’ but gives no date or location. Which note is most accurate?", "options": ["The custom is practiced everywhere.", "The custom has never changed.", "The page describes it as common in some families; place and date still need checking.", "The page proves every family follows it."], "answer": "C", "strategy": "保留來源原有的限定詞，再標出缺少的定位資訊，不擴寫成全稱判斷。", "why": "C如實保留some families並指出資料缺口；其他選項把有限說法擴張為無例外事實。"},
    {"prompt": "A poster says one greeting is ‘the traditional way’ for a whole country, but two local sources show regional variation. What should the team write?", "options": ["Use the broad claim because posters need short text.", "Name the two sources' locations and say practices vary.", "Delete both sources and choose one custom.", "Ask a student to decide which region is typical."], "answer": "B", "strategy": "讓地點和來源跟著主張一起出現，必要時縮小結論而不是替來源投票。", "why": "B保留可查核的區域差異；沒有代表性研究時，不能挑一區代替全國。"},
    {"prompt": "A classmate is the only student whose family has a particular background. The class is planning a culture display. Which plan avoids putting them on the spot?", "options": ["Require the student to explain the group's customs.", "Ask the student to approve every label written by others.", "Invite the student to contribute only if they choose, and research public sources independently.", "Use the student's family photo without asking."], "answer": "C", "strategy": "讓參與由本人選擇，同時由小組自行查找可追溯資料，不把文化勞動外包給單一同學。", "why": "C兼顧自願與獨立查證；同學的背景不代表同意、專業或替全體發言的義務。"},
    {"prompt": "Which final reflection best shows understanding of respectful cultural comparison?", "options": ["Different means one practice must be better.", "I can infer a group's beliefs from one photo.", "Once I learn a custom, I no longer need to check the source.", "I can compare a named example, cite its source, and note what it cannot show."], "answer": "D", "strategy": "檢查是否同時具備具體對象、來源依據和結論限制，三者缺一不可。", "why": "D把比較建立在可定位例子上，也說明證據不能支持什麼；其他句子把差異變排名、猜動機或免除查證。"},
]

def exam_refs() -> list[dict[str, str]]:
    return [
        {"url": NEIHU_URL, "title": "臺北市立內湖國中111學年度第1學期九年級第2次段考英語科試卷", "year": "111-1", "subject": "english", "locator": "PDF第3頁第44至46題：節慶報告中的多欄資訊擷取、未提及資訊辨識與有據推論", "observedPattern": "先定位篇章資料，再分辨文本明載、未提及與可推論的結論；本題改用自編校園情境，不沿用原節慶或題目。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item"},
        {"url": GUOCHANG_URL, "title": "高雄市立國昌國中113學年度第2學期七年級第2次段考英語科試題", "year": "113-2", "subject": "english", "locator": "PDF第5頁第30至32題：農曆新年文化短文的節期範圍、詞義及習俗敘述核對", "observedPattern": "以閱讀脈絡核對文化相關文字的具體主張；本題更換全部人物、內容、選項與答案，只參考逐項對照方式。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item"},
    ]

def main() -> None:
    # Protect already registered authored work: no authoring script may rewrite a listed manuscript.
    inventory_path = ROOT / "implementation/reports/authored-fusion-writing-inventory.json"
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    if LESSON_ID in inventory.get("authoredFusionDraftIds", []):
        raise SystemExit(f"Refusing to rewrite registered fusion manuscript: {LESSON_ID}")
    lesson = json.loads(LESSON_PATH.read_text(encoding="utf-8"))
    lesson["reviewStatus"] = "draft"
    lesson["updatedAt"] = "2026-09-28"
    lesson["authoringStandard"] = "version-fused-v1"
    lesson["studyReferences"] = [CURRICULUM_URL, NANI_URL, KANGHSUAN_URL, HANLIN_URL]
    lesson["provenance"]["authoringNote"] = "Original unit-specific fusion manuscript based on the official English curriculum/KG and three publisher-labeled public-school course plans; these plans are not complete publisher textbook chapters. No protected text, exam stem, options, answer, image, or worksheet is reproduced. Final content review remains with the user's ChatGPT workflow; draft status retained."
    lesson["publisherResearch"] = [
        {"publisher": "nani", "edition": "公校課程計畫標示南一七年級教材；跨年級節慶閱讀方法參照", "subject": "english", "chapterLocator": "丹鳳高中國中部公校計畫PDF p.17列Lesson 3及pp.53–60；不是8-Ⅳ-4目標課本原文。", "sourceUrl": NANI_URL, "access": "public-open", "reviewedAt": "2026-09-28", "researchScope": ["teaching-sequence", "concept-progression", "activity-pattern", "assessment-pattern"], "outcome": "能核對的是校方列出的節慶閱讀課次、圖片預測與掃讀；出版社章節全文及與目標單元逐頁對應未取得。", "copyrightBoundary": "只記校方計畫的章次、頁碼和教學策略，不複製教材正文、圖片、題目或答案。"},
        {"publisher": "kanghsuan", "edition": "民生國中公校九年級資源班計畫標示康軒；跨年級文化主題參照", "subject": "english", "chapterLocator": "PDF pp.1–2明列8-Ⅳ-4、C-Ⅳ-2及食物／節慶等分週主題；非本課出版社章節。", "sourceUrl": KANGHSUAN_URL, "access": "public-open", "reviewedAt": "2026-09-28", "researchScope": ["teaching-sequence", "concept-progression", "activity-pattern", "assessment-pattern"], "outcome": "校方計畫呈現文化能力和日常英語情境並行，沒有提供可確認的目標課次正文或完整評量。", "copyrightBoundary": "僅用公開校方課程定位作方法研究，不複製資源班教材、題目或答案。"},
        {"publisher": "hanlin", "edition": "大有國中公校九年級計畫標示翰林九上Unit 6；跨年級文化議題參照", "subject": "english", "chapterLocator": "PDF pp.13–14：Unit 6 *The Sign Which You Used Is Not OK*，C-Ⅳ-3與多元文化、來源核實議題；校方計畫非課本正文。", "sourceUrl": HANLIN_URL, "access": "public-open", "reviewedAt": "2026-09-28", "researchScope": ["teaching-sequence", "concept-progression", "activity-pattern", "assessment-pattern"], "outcome": "課程定位把文化差異、關懷和資訊查核並列；未取得出版社學生頁，不能推定出版社完整教學順序。", "copyrightBoundary": "只保留公校計畫公開的版本標示與課程定位，不轉錄課本、習作、題目、圖片或答案。"},
    ]
    lesson["versionResearch"] = RESEARCH
    lesson["fusionRecord"] = FUSION
    lesson["content"] = {"summary": "以文化情境閱讀、範圍判斷與尊重溝通，練習依證據理解差異並避免替他人或群體下定論。", "sections": [{"heading": h, "body": b} for h, b in SECTIONS]}
    lesson["studyHighlights"] = ["把直接觀察、個人解釋和待查證資訊分開。", "比較時註明來源、地點、對象與時間，不由單一經驗概括群體。", "提問先徵求分享意願，讓對方保有拒答、修改和撤回的選擇。"]
    lesson["teaching"] = {"body": [{"id": f"section-{i+1}", "phase": phase, "heading": h, "body": b} for i, (phase, h, b) in enumerate([(p, h, b) for p, (h, b) in zip(["hook", "explain", "explain", "guided-practice", "worked-example", "guided-practice", "transfer"], SECTIONS)])], "summary": ["先辨識來源明說的內容，不把猜測當成文化事實。", "再比較相同問題下的具體例子，保留家庭、個人和地區差異。", "交流前確認同意與範圍，讓英語表達既精確又尊重。"], "exitCheck": [{"prompt": "一則訪談能支持哪個範圍的說法？", "expectedEvidence": "說明說話者身分／情境及文本實際提供的內容，指出不能推廣到所有人的限制。"}, {"prompt": "如何用英語詢問一項不熟悉的習俗？", "expectedEvidence": "用禮貌、非預設的開放式問句，並保留對方不回答或改用其他來源的選擇。"}, {"prompt": "展板使用照片和文化描述前要檢查什麼？", "expectedEvidence": "查來源及地點範圍、確認照片使用同意、避免要求同學代表整個群體。"}]}
    lesson["interactive"] = {"type": "guided-choice", "goal": "練習依文本和來源判斷文化敘述的證據範圍，並以尊重同意及拒答權的方式交流。", "steps": INTERACTIVE_STEPS}
    LESSON_PATH.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i, data in enumerate(QUESTIONS, start=1):
        path = ROOT / f"questions/english/question-english-performance-8-iv-4-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"prompt": data["prompt"], "options": [{"id": chr(65+j), "text": t} for j, t in enumerate(data["options"])], "answer": {"value": data["answer"], "explanation": f"正確答案是{data['answer']}。{data['why']}"}, "reviewStatus": "draft", "updatedAt": "2026-09-28", "lessonId": LESSON_ID, "studyReferences": lesson["studyReferences"], "examPatternRefs": exam_refs(), "solutionStrategy": data["strategy"], "solutionSteps": [f"步驟一｜讀題：{data['prompt']}", f"步驟二｜找證據：{data['why']}", f"步驟三｜比選項：逐項排除把個人說成全體、把差異排高低或忽略同意界線的說法。", f"步驟四｜作判斷：選擇{data['answer']}，因為它符合題目證據並保留當事人與來源的實際範圍。", f"步驟五｜回查：{data['why']} 檢查答案沒有加入題目未提供的文化規則。"], "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": CURRICULUM_URL, "sourceLocator": "課綱8-Ⅳ-4/C-Ⅳ-3及KG kg-english-performance-8-iv-4；題型僅參照所列公校英語試卷的指定頁／題，題幹、選項、情境及解答均重新撰寫。", "authoringNote": "Original item with correct answer, Chinese explanation, unit-specific strategy and five detailed steps. Public-school exam references are pattern-only; no original question, options, image, passage or answer is copied. User's ChatGPT retains final content review; draft retained."}})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Authored {LESSON_ID}: {len(SECTIONS)} sections, {len(INTERACTIVE_STEPS)} interactive steps, {len(QUESTIONS)} solved items.")

if __name__ == "__main__":
    main()
