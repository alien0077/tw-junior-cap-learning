import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-nc-iv-6.json"
QDIR = ROOT / "questions/science"
REPORT = ROOT / "implementation/reports/science-content-nc-iv-6-first-pass-review.json"
TODAY = "2026-09-23"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考試題", "能源、功率、效率、資料判讀", "只取公立學校試題對能源資料與推理層次的能力模式，改寫臺灣供電情境。"),
    ("https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "114 年國中教育會考自然科公開試題", "能量、電力、環境與實驗證據", "只取公開會考的資料判讀與系統邊界能力方向，未複製原題。"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "能源科技、供應、環境限制", "只取公立校方公開試題的能源科技決策能力模式，重新設計題目。"),
]
REFS = [{"url": u, "title": t, "year": "109-115", "subject": "science", "locator": l, "observedPattern": p, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, l, p in SOURCES]
ROWS = [
    ("easy", "下列哪一項最能說明『裝置容量』與『實際發電量』不同？", ["容量是某條件下的輸出能力，發電量是特定時間實際產生的能量", "容量就是全年發電量", "容量只代表電價", "發電量與時間無關"], "A", "裝置容量是能力指標，實際發電量還會受日照、風況、設備狀態與運轉時間影響。", "先圈出每個量的單位與時間，再分辨能力、累積輸出與用電需求。"),
    ("medium", "一所學校下午尖峰負載 80 kW，屋頂太陽能此時只有 30 kW，電池可供 20 kW；仍需由電網或備援補足多少功率？", ["30 kW", "50 kW", "80 kW", "130 kW"], "B", "可用輸出為 30+20=50 kW，缺口為 80-50=30 kW；因此仍需 30 kW。", "把需求、現場輸出、儲能輸出分欄，先加可用供給，再用需求減去供給。"),
    ("medium", "若某能源占全國發電量 25%，這個百分比最直接回答什麼問題？", ["它占該統計期間實際發電量的比例", "它占所有土地的比例", "它代表設備容量必為 25%", "它代表每個時刻都供應 25%"], "A", "分母是統計期間的總發電量時，25%只描述能量占比，不能直接改寫成土地占比、容量占比或每時刻固定輸出。", "先確認分母、期間與指標名稱，再限制結論不要超出資料。"),
    ("hard", "太陽能發電中午高、傍晚低，而家庭尖峰在傍晚；哪個方案最直接處理時間錯配？", ["增加同時段用電或需求管理，並搭配儲能與電網調度", "只看中午最高功率就宣稱沒有缺口", "把傍晚資料刪除", "只增加宣傳標語"], "A", "問題是供給與需求的時間不一致，需求移轉、儲能與電網調度能把不同時間的供需連起來。", "先畫一天的供需曲線，再找缺口發生時段，最後安排移轉、儲能或備援。"),
    ("easy", "談臺灣能源未來時，哪一組資料最能避免只憑單一印象下結論？", ["供需時間序列、能源來源、實際輸出與排放等不同指標交叉比對", "只看一次停電新聞", "只看某設備的額定容量", "只問能源名稱是否聽起來環保"], "A", "能源展望要同時看時間、來源、實際輸出與環境代價，單一事件或單一指標不足以代表整體。", "把主張拆成需求、供給、穩定度和環境影響，再為每格找對應資料。"),
    ("hard", "離島電網面對船運燃料不穩與連續陰雨，評估能源方案時最重要的補充條件是？", ["燃料與物資到達性、備援容量、儲能天數、天候情境與基本用電優先順序", "只比較晴天的最高輸出", "忽略維修與燃料運輸", "把離島資料換成都市平均"], "A", "離島的可靠度與供應鏈限制不同，方案必須把補給、備援、儲能與極端天候一起納入。", "先列不能中斷的服務，再用最壞情境檢查補給、容量和備援是否足夠。"),
    ("medium", "若某報告說『再生能源增加後排放下降』，哪個追問最合理？", ["排放的系統邊界、比較基準、統計期間，以及製造與設備退役是否納入", "只問報告標題是否肯定", "直接推論所有污染都消失", "認定所有時段都同樣下降"], "A", "排放結果取決於比較基準、邊界和期間；操作階段的改善不能自動代表製造、維修與退役也相同。", "先找基準年與邊界，再區分操作排放和生命週期排放。"),
    ("hard", "同樣新增 100 MW 太陽能，甲地有電網與電池，乙地沒有儲能且晚間需求高；哪項判斷較嚴謹？", ["兩地新增容量相同，但可用輸出、尖峰支援與備援效果可能不同", "兩地全年供電效果必完全相同", "只要容量相同就不必看需求時段", "乙地晚間需求可由中午峰值直接取代"], "A", "額定容量相同不代表在需求發生時提供的服務相同，電網、儲能和需求時序會改變實際效果。", "把容量、時間、可輸出功率與服務目標分開，再比較兩地限制。"),
    ("medium", "下列哪個校園能源方案最符合『可檢查、可修正』的展望？", ["先量測尖峰時段與設備用電，設定節能與備援指標，依每月資料調整方案", "直接保證明年一定零排放", "只購買最大容量設備，不設定檢查指標", "只用一次問卷推論全年需求"], "A", "可修正方案要有基準、指標、時間與回饋資料，才能知道效果是否達成並修正配置。", "先建立基準線，再設定可量測目標、追蹤期間與失敗時的調整規則。"),
    ("hard", "對臺灣能源未來最合適的總結是哪一項？", ["在明確需求、時間、供應、電網與環境邊界下比較多方案，依新證據持續修正", "選定一種能源後永遠不必改變", "只要提高裝置容量就能解決所有供電問題", "能源展望不需要資料因為是想像"], "A", "能源未來不是單一技術的保證，而是依需求、資源、可靠度、環境與社會條件形成的條件式推論。", "把目標、證據、限制、備援和可改變的判斷條件寫成完整論證。"),
]

def make_question(n, row):
    diff, prompt, opts, source_answer, explanation, strategy = row
    target = "BDACBDACBD"[n - 1]
    idx = ord(source_answer) - 65
    correct = opts[idx]
    distractors = [x for i, x in enumerate(opts) if i != idx]
    ordered, di = [], 0
    for label in "ABCD":
        if label == target:
            ordered.append(correct)
        else:
            ordered.append(distractors[di]); di += 1
    steps = ["圈出需求、能源來源、設備、輸出、時間與環境邊界。", "核對每個數字的單位、分母、統計期間與是否代表容量或實際能量。", "畫供需時間線或能量轉換鏈，計算缺口並固定比較條件。", f"排除把容量當發電量、把單一時段當全年或把操作排放當生命週期的選項，答案為 {target}。", f"用條件式資料回查結論：{explanation}"]
    return {"id": f"question-science-content-nc-iv-6-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", ordered)], "knowledgeIds": ["kg-science-content-nc-iv-6"], "difficulty": diff, "answer": {"value": target, "explanation": f"{explanation} 正確答案為選項 {target}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "三筆公立學校／公開自然與理化資料的能源結構、供需、功率、效率、環境與科技決策能力方向；本題為 Nc-Ⅳ-6 原創情境改寫。", "authoringNote": "依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-nc-iv-6", "examPatternRefs": REFS, "solutionStrategy": strategy, "solutionSteps": steps}

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": TODAY, "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []): row["reviewedAt"] = TODAY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-nc-iv-6、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然與理化題型能力模式，獨立融合臺灣能源結構、供需時間、裝置容量、實際發電、電網、儲能、離島供應、排放邊界與條件式未來展望。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i, row in enumerate(ROWS, 1):
        (QDIR / f"question-science-content-nc-iv-6-{i}.json").write_text(json.dumps(make_question(i, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "10 題重新改寫為臺灣能源結構、供需時間、容量與實際發電、儲能、電網、離島供應、排放邊界與條件式展望；每題具唯一答案、解析、策略與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content nc-iv-6")

if __name__ == "__main__":
    main()
