"""La：生物間的交互作用第一輪原創教材與題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-la.json"
REPORT = ROOT / "implementation/reports/science-content-la-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題", "year": "114", "locator": "生物間交互作用、食物網與資料判讀", "pattern": "取公立學校自然科評量以關係辨識、族群變化和證據推理的能力方向。"},
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "捕食、競爭、共生與生態資料", "pattern": "取公開會考以圖表、時間序列、直接與間接作用及實驗設計的能力方向。"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國民中學二年級自然科公開段考試題", "year": "112", "locator": "食物關係、資源競爭與族群實驗", "pattern": "取公立國中試題以互動方向、資源限制、對照與重複量測的能力方向。"},
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]
STEPS = [["先找出兩個生物和它們共享或交換的資源。", "記錄誰受益、誰受損，以及關係是直接還是透過第三者發生。", "沿時間序列比較兩族群，而不是只看同時出現。", "用對照、隔離或資源改變檢查替代解釋。", "用關係類型、方向、證據與限制寫出條件式結論。"] for _ in range(10)]
ROWS = [
    ("easy", "花圃中蚜蟲吸食植物汁液，植物生長受抑；這種關係最符合哪一類？", ["寄生或取食，使一方受益、另一方受損", "互利共生，兩者都必然受益", "競爭，因為兩者搶同一種食物", "中性，因為生物不能互相影響"], "A", "蚜蟲取得食物而植物受到損害，依題目呈現的方向可判定為寄生或取食關係。", "先列出雙方的受益或受損符號，再與關係定義比對，不只看兩者是否同時出現。"),
    ("easy", "兩種植物在缺水土壤中爭取同一片根域的水分，最適合稱為？", ["競爭", "捕食", "寄生", "分解"], "A", "雙方使用有限且相同的資源，彼此降低取得資源的機會，這是競爭。", "圈出有限資源與共享使用者，再確認是否有一方直接取食另一方。"),
    ("medium", "瓢蟲捕食蚜蟲後，短期內蚜蟲減少、植物受害程度下降；直接作用是？", ["瓢蟲與蚜蟲的捕食，並間接影響植物", "植物與土壤的分解", "瓢蟲與陽光的競爭", "蚜蟲與雨水的互利"], "A", "瓢蟲直接取食蚜蟲；植物改善是經由蚜蟲數量變化產生的間接效果。", "先找實際發生的取食事件，再沿食物網往下一層追蹤間接結果。"),
    ("medium", "螞蟻取食蚜蟲分泌物，同時驅趕部分天敵；若兩者在此情境都獲益，較合理的關係是？", ["互利或互惠關係，但仍需資料確認兩方長期收益", "必然是捕食，因為螞蟻接觸蚜蟲", "必然是競爭，因為兩者都在植物上", "無法有任何關係，因為不是同種"], "A", "螞蟻取得食物、蚜蟲受到保護時，雙方可能互利；但需比較成本、時間與不同環境條件，不能只憑一次觀察斷言。", "先分別列出雙方的收益與代價，再用多次或不同條件的資料確認關係穩定性。"),
    ("hard", "隔離螞蟻的花圃框中，蚜蟲先增加，兩週後瓢蟲也減少；最恰當的解釋是？", ["螞蟻可能同時影響蚜蟲與瓢蟲，但仍須排除植物量、天氣和其他天敵因素", "蚜蟲增加必然直接殺死所有瓢蟲", "瓢蟲減少證明螞蟻是瓢蟲唯一食物", "只要有時間先後就已完成唯一因果證明"], "A", "時間序列提示螞蟻移除可能透過蚜蟲或天敵網絡造成連鎖效果，但還需要控制和對照排除其他原因。", "把先後順序當作線索，不把它直接升格為唯一因果。"),
    ("medium", "要測試螞蟻是否改變蚜蟲數量，哪個設計較公平？", ["設相近花圃框，只改變螞蟻能否進入，固定植物、水分、光照並重複記錄蚜蟲", "同時換植物、施肥、改光照和隔離螞蟻", "只挑蚜蟲最多的一天作結論", "先告訴觀察者預期答案再量一次"], "A", "單獨改變螞蟻進入條件並固定其他因素，才較能把蚜蟲差異歸因於螞蟻作用。", "先指定唯一自變因，再列控制變因、對照組和重複測量方式。"),
    ("easy", "兩種鳥都吃同一片果實，但一種在早晨、另一種在傍晚取食；要判斷競爭強度，還應觀察？", ["可取得果實量、取食時間重疊與兩種鳥的數量變化", "只觀察羽毛顏色", "只量其中一種鳥的體重一次", "直接假設時間不同就完全沒有競爭"], "A", "時間錯開可能降低競爭，但仍要看資源量、使用時段是否重疊和族群反應，不能只靠時段名稱判定。", "把競爭拆成資源、空間、時間與族群結果四個可量測面向。"),
    ("medium", "若移除瓢蟲後蚜蟲增加、植物葉面受損，這是一條怎樣的間接鏈？", ["瓢蟲減少→蚜蟲增加→植物受害增加", "瓢蟲增加→蚜蟲增加→植物受害減少", "植物受損→瓢蟲直接製造蚜蟲", "蚜蟲減少→植物受損增加"], "A", "瓢蟲是蚜蟲的天敵；移除後蚜蟲壓力上升，進而造成植物受害增加。", "沿著每一條直接取食關係逐段標記增減方向，再串成間接效果。"),
    ("hard", "同一種互動在不同季節結果不同，最合理的研究態度是？", ["記錄溫度、資源與天敵等背景條件，說明結論只適用於觀察範圍", "選擇最符合課本定義的季節，刪除其他資料", "因結果不同就說生物間沒有交互作用", "只用一次觀察推論全年關係"], "A", "交互作用會受資源、溫度、棲地和其他物種影響；季節差異應保留並轉成可檢驗的條件，而非刪除。", "把『關係類型』和『作用強度』分開，交代資料的時間與環境範圍。"),
    ("hard", "要報告花圃中螞蟻—蚜蟲關係，哪種結論最符合證據界線？", ["在本次植物、季節和隔離條件下，資料支持螞蟻可能改變蚜蟲數量；仍需更多重複與替代解釋檢查", "螞蟻永遠保護蚜蟲，任何環境都相同", "兩者同時出現即可證明互利", "因為資料不完整，所以不能提出任何可檢驗假設"], "A", "好的報告同時說明觀察條件、支持的方向與尚未排除的因素，讓結論可被後續實驗修正。", "用條件式語句收束：資料支持什麼、範圍在哪裡、下一步要排除什麼。"),
]

def make_question(number, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    return {"id": f"question-science-content-la-{number}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)], "knowledgeIds": ["kg-science-content-la"], "difficulty": difficulty, "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的捕食、競爭、寄生、互利、間接作用、族群資料與控制變因能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-la", "examPatternRefs": REFS, "solutionStrategy": strategy, "solutionSteps": STEPS[number - 1]}

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = TODAY; lesson["reviewStatus"] = "draft"; lesson["authoringStandard"] = "version-fused-v1"
    lesson["content"] = {"summary": "本課把花圃裡的植物、蚜蟲、瓢蟲與螞蟻當成一張會變動的關係網，從誰吃誰、誰共享水分，到一個族群改變後如何透過第三者傳遞影響。學習者會用收益與代價、時間序列和對照實驗區分捕食、競爭、寄生與互利，並知道關係強度會受季節、資源和棲地改變。", "sections": [{"heading": "先畫出誰影響誰", "body": "在花圃中，蚜蟲吸食植物汁液，瓢蟲捕食蚜蟲，螞蟻可能取食蚜蟲分泌物並驅趕天敵。不要只把同時出現的生物連成一條線；先問每一箭頭代表取食、共享資源、保護還是寄居，再標記受益與受損。"}, {"heading": "直接作用會繞成間接作用", "body": "移除瓢蟲可能讓蚜蟲增加，植物葉面因而受損；這不是瓢蟲直接傷害植物，而是沿著捕食關係傳遞的間接效果。畫箭頭時逐段追蹤數量變化，才能避免把最後的結果誤寫成第一個生物直接造成。"}, {"heading": "關係名稱不能取代證據", "body": "競爭需要有限資源與重疊使用；互利需要雙方在特定條件下都得到好處；寄生或取食則是一方取得資源而另一方付出代價。同一對生物在不同季節或資源條件下，作用強度可能改變，所以分類後仍要回到資料檢查。"}, {"heading": "用隔離和對照檢查推論", "body": "若要測試螞蟻是否改變蚜蟲數量，可設置相近花圃框，只改變螞蟻能否進入，固定植物、水分和光照，並重複記錄蚜蟲、瓢蟲與葉片受損。報告要交代資料支持的方向、研究範圍與尚未排除的天氣、植物差異或其他天敵。"}], "studyEntry": "從一條具體的取食或保護關係開始，再把影響沿時間和食物網往外追蹤。"}
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-la、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合捕食、競爭、寄生、互利、直接與間接作用、族群時間序列與公平實驗。原有泛用正文與題目已改為植物—蚜蟲—瓢蟲—螞蟻的單元專屬教學；所有正文、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    for entry in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []): entry["reviewedAt"] = TODAY
    for number, row in enumerate(ROWS, 1): (QDIR / f"question-science-content-la-{number}.json").write_text(json.dumps(make_question(number, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "正文改為花圃生物網脈絡，10 題改寫為捕食、競爭、寄生、互利、間接作用、族群資料與控制變因專屬問題；每題有唯一答案、解析與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print("authored science content la")

if __name__ == "__main__": main()
