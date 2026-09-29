import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "english"
SOURCE_FILE = ROOT / "data" / "public-exam-sources.json"

references = [
    {
        "url": "https://www2.csjh.kh.edu.tw/teach/exam/106%E4%B8%8A%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83/%E9%81%B8%E4%BF%AE%E8%8B%B1%E6%96%87/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E9%81%B8%E4%BF%AE%E8%8B%B1%E6%96%87/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E9%81%B8%E8%8B%B1%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立中山國民中學106學年度第1學期第3次段考二年級選修英文試題",
        "year": "106-1",
        "subject": "english",
        "locator": "第46至47題：依網路天氣預報內容理解資訊並作行程判斷",
        "locatorLevel": "item",
        "observedPattern": "先辨識線上資訊的用途，再把可查核的內容傳達給受眾；本題僅取資訊理解與分享的能力模式。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
    },
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87_1.pdf",
        "title": "高雄市立國昌國中110學年度第1學期第1次段考三年級英語科試題",
        "year": "110-1",
        "subject": "english",
        "locator": "PDF第4頁第27至29題：整合學生分享內容，辨認分享目的與文本證據",
        "locatorLevel": "page",
        "observedPattern": "閱讀多位分享者的內容，依其主題、證據與意圖判讀訊息；本站情境與文字均另行創作。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
    },
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf",
        "title": "高雄市立國昌國中111學年度第1學期第3次定期評量三年級英文科試題",
        "year": "111-1",
        "subject": "english",
        "locator": "PDF第8頁第42至45題：判讀網路購物評論的資訊用途、可信度與限制",
        "locatorLevel": "page",
        "observedPattern": "網路資訊分享須辨別證據與可信度，並保留不確定性；本站不複製其文章或題目。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
    },
]

answer_keys = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]
correct_option_fragments = [
    "Today I will explain two safe cycling habits",
    "Article title, author or organization, URL, and access date",
    "Choose the main claim, two supporting details, and one conclusion",
    "Use a permitted image, credit its creator, and include the source",
    "Ask the classmate for permission and agree on what may be shared",
    "Favorite after-school activities: number of students (n=40)",
    "It came from the survey table on slide 3; I can show the source note",
    "Both claims, the evidence each uses, and a cautious conclusion",
    "Which feature was clearest, and what would you improve",
    "Check facts and links, credit images, remove private data, and test the page with a reader",
]
solution_steps = [
    ["確認分享任務是介紹 bicycle safety 的短報告。", "從聽眾角度檢查開場是否交代主題、範圍和目的。", "A 同時說明兩項安全習慣及其重要性，三個要素齊全。", "B 只提找到網站；C 是零散描述；D 只要求看標題，皆未交代報告目的。", "選 A：聽眾一開始便知道要聽什麼，以及分享者為何選這個主題。"],
    ["確認任務是分享線上文章的一項事實，而非轉貼文章全文。", "想像讀者想自行查證時，需要辨認文章及其發布來源。", "B 提供標題、作者或機構、網址和查閱日期，足以回到原始材料。", "A 沒有來源；C 的網頁底色無關查證；D 只是朋友猜測，皆不能追溯事實。", "選 B：附上可辨識且可回查的來源資訊，再用自己的話分享事實。"],
    ["抓出簡報限制：文章很長，但口頭分享只有三分鐘。", "先決定主張，再挑選最能支撐主張的少量證據。", "C 保留主要主張、兩項支持細節與結論，份量適合時限。", "A 要求逐字快念；B 只有網址沒有說明；D 複製整篇文章，均不利理解或涉及不當重製。", "選 C：濃縮而保留論證脈絡，讓受眾能在時間內掌握重點。"],
    ["辨認材料是網路照片，使用前須同時考慮授權與署名。", "逐項核對選項是否確認可使用、標示創作者並列出來源。", "D 三項都有：先選可使用的圖片，再署名與記錄來源。", "A 移除作者資訊；B 把公開誤當免費授權；C 冒稱自己拍攝，皆不尊重創作權。", "選 D：確認許可並清楚標示作者和來源後，才放進課堂簡報。"],
    ["判斷訪談內容涉及同學本人，公開前可能揭露個人資訊。", "先把「是否同意」與「同意分享哪些內容」分開確認。", "A 在發布之前徵求同意，並約定公開範圍，尊重當事人的選擇。", "B 未經同意便發布；C 公開電話；D 即使改名仍保留私人細節，皆不能保障隱私。", "選 A：先取得明確同意並確認可分享範圍，才整理或發布訪談。"],
    ["確認圖表呈現40位學生的課後活動調查結果。", "讀者需要知道調查主題、數值代表什麼，以及樣本數。", "B 清楚標出活動偏好、人數單位與 n=40，能正確解讀資料。", "A 是空泛標題；C 沒有主題或單位；D 叫讀者不要提問，均未提供圖表標籤。", "選 B：補齊主題、測量單位和樣本數，避免把圖表數值看錯。"],
    ["聽眾追問數字來源，表示需要能回查的證據位置。", "回答應指出資料所在處，而非只重複主張或猜測。", "C 指向第3張投影片的調查表，並提出來源註記供核對。", "A 承認不記得；B 要求停止提問；D 說數字是想像的，都沒有提供可查證依據。", "選 C：把數字連回表格及來源註記，讓聽眾可以自行核實。"],
    ["兩個網站對睡眠提出不同主張，不能只挑較吸睛的一方。", "公平比較時，分別呈現各自的主張與支持證據。", "D 保留雙方主張、各自證據，並以審慎結論表達證據限制。", "A 只挑驚人的說法；B 不交代來源；C 依圖片數量投票，皆不能支持可靠判斷。", "選 D：並列主張和證據，再依證據強弱保留必要的不確定性。"],
    ["分享結束後要收集能改善下一版的回饋。", "有效問題應聚焦內容是否清楚，也邀請具體建議。", "A 同時詢問最清楚的功能及可改進之處，能得到可採取的意見。", "B 預設完美而拒絕評論；C 只叫人離開；D 限縮成顏色評分，皆無法檢查理解。", "選 A：用開放問題蒐集清晰度與改進方向，作為修訂依據。"],
    ["網頁將公開給讀者使用，發布前須兼顧正確性、可用性與安全。", "把事實、連結、圖片權利、隱私和實際讀者測試列為檢查點。", "B 的清單涵蓋五個面向，能在公開前找出內容與使用風險。", "A 尚未核實便發布；C 沒有來源；D 蓄意隱藏錯誤，都會降低可信度或傷害讀者。", "選 B：逐項測試內容、連結、授權與隱私，再請讀者試用後才發布。"],
]
source_records = [
    {
        "id": "csjh-106-1-grade8-elective-english",
        "school": "高雄市立中山國民中學",
        "grade": "8",
        "subject": "english",
        "exam": "106學年度第1學期第3次段考二年級選修英文試題",
        "questionUrl": references[0]["url"],
        "answerLocator": "第46至47題，線上天氣資訊理解與行程判斷",
        "usePolicy": "僅作線上資訊理解與分享的能力模式研究；本站重新設計情境、題幹、選項、答案與解析，不複製原卷。",
        "verifiedAt": "2026-09-27",
    },
    {
        "id": "kcjh-110-1-term1-grade9-english",
        "school": "高雄市立國昌國民中學",
        "grade": "9",
        "subject": "english",
        "exam": "110學年度第1學期第1次段考三年級英語科試題",
        "questionUrl": references[1]["url"],
        "answerLocator": "PDF第4頁第27至29題，閱讀分享內容並判讀意圖與證據",
        "usePolicy": "僅作多位分享者訊息理解的能力模式研究；本站素材、選項、答案及解析皆原創，不複製原卷。",
        "verifiedAt": "2026-09-27",
    },
    {
        "id": "kcjh-111-1-term3-grade9-english",
        "school": "高雄市立國昌國民中學",
        "grade": "9",
        "subject": "english",
        "exam": "111學年度第1學期第3次定期評量三年級英文科試題",
        "questionUrl": references[2]["url"],
        "answerLocator": "PDF第8頁第42至45題，網路評論資訊用途、可信度及限制",
        "usePolicy": "僅作網路資訊查核與證據判讀模式研究；本站另創資料與題目，不複製原卷。",
        "verifiedAt": "2026-09-27",
    },
]

catalog = json.loads(SOURCE_FILE.read_text(encoding="utf-8"))
known_urls = {row.get("questionUrl") for row in catalog["sources"]}
for record in source_records:
    if record["questionUrl"] not in known_urls:
        catalog["sources"].append(record)
catalog["updatedAt"] = "2026-09-27"
SOURCE_FILE.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

for number, expected_key in enumerate(answer_keys, start=1):
    path = QUESTION_DIR / f"question-english-performance-6-iv-6-{number}.json"
    question = json.loads(path.read_text(encoding="utf-8"))
    options = question["options"]
    correct = next(option for option in options if correct_option_fragments[number - 1].casefold() in option.get("text", "").casefold())
    distractors = [option for option in options if option is not correct]
    reordered = [correct if letter == expected_key else distractors.pop(0) for letter in "ABCD"]
    for letter, option in zip("ABCD", reordered):
        option["id"] = letter
    question["options"] = reordered
    question["answer"]["value"] = expected_key
    question["solutionSteps"] = solution_steps[number - 1]
    question["answer"]["explanation"] = question["solutionSteps"][-1]
    question["provenance"] = {
        "origin": "original",
        "license": "All rights reserved",
        "sourceUrl": references[(number - 1) % len(references)]["url"],
        "sourceLocator": references[(number - 1) % len(references)]["locator"],
        "authoringNote": "題幹、情境、選項、答案與解析均為原創；公立學校試題只提供可追溯的能力模式參照，不重製原文。內容狀態維持draft，Terra審查已取消。",
    }
    question["examPatternRefs"] = references
    question["reviewStatus"] = "draft"
    path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"updatedQuestions": len(answer_keys), "answerKeys": answer_keys, "distinctPublicExamPatterns": len(references), "status": "draft"}, ensure_ascii=False))
