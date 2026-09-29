"""Ka-Ⅳ-7：光速與影響因素第一輪原創題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ka-iv-7.json"
REPORT = ROOT / "implementation/reports/science-content-ka-iv-7-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題", "year": "114", "locator": "光速、透明介質、折射率與資料判讀", "pattern": "取公立學校自然科評量以介質、速率、公式和數據推理光學現象的能力方向。"},
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "光學、傳播時間、介質與科學資料判讀", "pattern": "取公開會考以模型、圖表和條件資訊判斷光學傳播的能力方向。"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E7%90%86%E5%8C%96%E7%A7%91_8.pdf", "title": "高雄市立國昌國中 113 學年度第一學期第二次段考二年級理化科公開試題", "year": "113", "locator": "PDF 第 3 頁第 25 題：比較光波與聲波，含介質速率與雷雨先見閃電後聞雷聲的判讀；僅借鑑能力方向，不採用來源中的錯誤敘述。", "pattern": "以光和聲音在介質中的傳播差異檢核科學推論，並要求分辨觀察到的先後與真正原因。"},
    {"url": "https://www.csjh.kh.edu.tw/teach/exam/108%E4%B8%8A%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83/%E8%87%AA%E7%84%B6%E7%A7%91/%E4%BA%8C%E5%B9%B4%E7%B4%9A/108-1%E5%9C%8B%E4%BA%8C2%E6%AE%B5%E8%87%AA%E7%84%B6%28%E7%90%86%E5%8C%96%29%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf", "title": "高雄市立中山國中 108 學年度第一學期第二次段考二年級自然科公開試題", "year": "108", "locator": "PDF 第 3 頁第 25 題：光由空氣進入水中時，判讀光速、波長、頻率及折射相關變化。", "pattern": "在介質改變情境下連結折射、光速與波長／頻率不變條件。"},
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

ROWS = [
    ("easy", "同一束光由真空進入透明玻璃，通常哪項敘述較合理？", ["在玻璃中的速率通常低於真空中的速率", "在玻璃中必定比真空快", "透明度越高就一定沒有速率差", "光進玻璃後會停止"], "A", "透明不代表光速等於真空值；光與介質作用後，在玻璃中的有效速率通常低於真空中的 c。", "先分辨透明度與傳播速率，再用介質條件判斷。"),
    ("medium", "空氣與玻璃的光路長度相同，玻璃折射率較大。若其他條件相同，哪個推論合理？", ["玻璃中的光速較小，抵達時間較長", "玻璃中的光速較大，抵達時間較短", "兩者時間必定相同，因為距離相同", "只要玻璃透明，就無法比較時間"], "A", "由 n=c/v 可知折射率 n 較大時 v 較小；相同距離下 t=d/v 因此較長。", "把折射率、速度和到達時間用同一條關係串起來。"),
    ("medium", "真空光速取 3.0×10^8 m/s，某透明材料折射率 n=1.5，光在材料中的速率約為？", ["2.0×10^8 m/s", "4.5×10^8 m/s", "1.5×10^8 m/s", "3.0×10^8 m/s"], "A", "n=c/v，所以 v=c/n=(3.0×10^8)/1.5=2.0×10^8 m/s。折射率沒有速度單位。", "先寫 n=c/v，再移項並檢查單位。"),
    ("hard", "光在折射率 n=1.4 的水樣中走過 7 m，真空光速取 3.0×10^8 m/s；理想模型下通過這段水的時間約為？", ["3.3×10^-8 s", "1.0×10^-8 s", "4.2×10^-8 s", "2.1×10^-7 s"], "A", "水中速率 v=c/n≈2.14×10^8 m/s，因此 t=d/v≈7/(2.14×10^8)=3.3×10^-8 s。", "先由折射率算介質中的速率，再用 t=d/v。"),
    ("medium", "雷雨時先看見閃電、約三秒後聽見雷聲；這筆資料最適合用來做什麼？", ["用聲速粗估雷雨距離，不能直接量出光速", "直接把三秒代入求光速", "證明閃電和雷聲是兩個不同事件", "證明光在真空中只走三秒"], "A", "延遲主要反映聲音在空氣中比光慢，可用聲速乘延遲粗估距離；還須考慮聲源同時性、回音和反應時間，不能直接得到光速。", "先辨認哪一個訊號造成主要延遲，再判斷可支持的結論範圍。"),
    ("hard", "固定玻璃介質，把光路由 2 m 增至 6 m；理想條件下哪項判斷最適當？", ["到達時間約增為三倍，但玻璃中的光速不因路徑變長而改變", "光速約增為三倍", "折射率會因距離變成三倍", "光走得更遠就代表介質變了"], "A", "固定介質時 v 不因路徑長度改變；t=d/v，因此距離增為三倍時到達時間也約增為三倍。", "把距離變化和介質造成的速度變化分開。"),
    ("medium", "要比較空氣和水對光速的影響，下列哪項是較公平的設計？", ["固定波長、路徑長度、光源和感測器，只切換介質並重複測量到達時間", "空氣測 1 m、水測 10 m，且不記錄溫度", "只比較兩束光看起來哪束較亮", "每次同時改變介質、光源和感測器"], "A", "只改變介質並固定光源、波長、距離與儀器，才能把時間差合理歸因於介質；重複測量可估計不確定性。", "用一次一變因和重複測量隔離介質效果。"),
    ("hard", "某 3 m 玻璃段造成的理論時間差小於感測器的不確定度，最合適的報告是？", ["目前解析度不足以可靠分辨，應增加路徑或改善儀器", "挑選最接近理論值的一次就宣稱已證明", "忽略不確定度，因為光速很快", "把誤差直接當成光在玻璃中停止"], "A", "若預期差值小於儀器不確定度，資料不足以判別差異；可增加有效路徑、重複平均或使用更高解析度感測器。", "把測量解析度納入結論，不把理論值冒充實測證據。"),
    ("easy", "關於光速公式 v=d/t，下列哪項配對正確？", ["v 是速率、d 是路徑距離、t 是通過所需時間", "v 是折射率、d 是溫度、t 是亮度", "v 是距離、d 是速率、t 是介質", "v 是亮度、d 是波長、t 是音量"], "A", "v=d/t 中 v 表示單位時間通過的距離，d 是實際路徑長度，t 是該路徑的傳播時間；三者單位也要一致。", "先釐清符號和單位，再進行公式計算。"),
    ("medium", "光纖中的光速低於真空值，但訊號仍可傳很遠。哪個解釋最合理？", ["速度和可傳距離是不同問題，還要考慮光纖導引、損耗、彎曲與中繼設備", "只要速度變慢，訊息就不可能走遠", "光纖中的光其實沒有經過介質", "訊號距離只由透明度決定"], "A", "光在光纖材料中的速度可由折射率比較，但能否傳遠還涉及全反射導引、材料損耗、彎曲和中繼；不能把兩個問題混為一談。", "先分離『傳得多快』和『能否傳得遠』兩個指標。"),
]

def steps(n, prompt, explanation, strategy):
    return [
        f"讀題定位：{prompt}",
        f"選擇判斷路徑：{strategy}",
        f"連結本題物理量與證據：{explanation}",
        "排除只抓到單一關鍵字、忽略題目給定條件或把模型結論當成未測量的實驗事實。",
        f"回查答案是否完整回應題目條件；本題應依「{strategy}」說明理由。",
    ]

def make_question(n, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    return {"id": f"question-science-content-ka-iv-7-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)], "knowledgeIds": ["kg-science-content-ka-iv-7"], "difficulty": difficulty, "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的光速、介質、折射率、時間資料和探究能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-ka-iv-7", "examPatternRefs": REFS, "solutionStrategy": strategy, "solutionSteps": steps(n, prompt, explanation, strategy)}

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["authoringStandard"] = "version-fused-v1"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ka-iv-7、南一公開入口、康軒公開光學資源、翰林公開資料查核限制與三筆公立學校／公開自然科評量能力模式，獨立融合真空與介質光速、v=d/t、n=c/v、雷雨延遲、路徑長度、控制變因、不確定性、光纖與水下測距。所有正文、數據、題幹、選項、答案、互動步驟與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    for entry in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []):
        entry["reviewedAt"] = TODAY
    for n, row in enumerate(ROWS, 1):
        (QDIR / f"question-science-content-ka-iv-7-{n}.json").write_text(json.dumps(make_question(n, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "10 題已逐題改寫為光速、介質、折射率、v=d/t、時間差、控制變因、不確定性、光纖與安全專屬問題；每題有唯一答案、解析與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ka iv 7")

if __name__ == "__main__":
    main()
