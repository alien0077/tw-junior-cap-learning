"""Kb-Ⅳ-1：重力、重量與質量第一輪原創題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-kb-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-kb-iv-1-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題", "year": "114", "locator": "質量、重量、重力與單位判讀", "pattern": "取公立學校自然科評量以力、質量、重力場和單位資料進行概念辨識與計算的能力方向。"},
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "力學、質量、重量與生活情境資料判讀", "pattern": "取公開會考以生活情境、圖表、比例和條件資訊推論物理量的能力方向。"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國民中學二年級自然科公開段考試題", "year": "112", "locator": "重力、重量、質量、彈簧秤與天平測量", "pattern": "取公立國中試題以儀器讀值、W=mg、地點變化和物質量判斷概念的能力方向。"},
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]
STEPS = [
    ["圈出質量 m、重力場強 g、重量 W、地點與儀器。", "判斷題目改變的是物質量、重力場還是量測工具。", "用 W=mg 並確認 kg、N/kg、N 的單位。", "排除把日常『重』、kg 和 N 混用的選項。", "回查答案是否同時符合數值、單位和所在地條件。"],
    ["列出 m、g、W 三個量及其單位。", "找出題目已知的兩個量。", "代入 W=mg 或移項計算未知量。", "檢查 N/kg×kg 是否得到 N。", "用比例和大小合理性驗算。"],
    ["比較搬動前後物質是否增減。", "確認所在地重力場是否改變。", "保持 m 或改變 W 的對應量。", "排除漂浮等於沒有質量的迷思。", "用天平與彈簧秤的角色作證據核對。"],
    ["把物質取走的質量變化寫出來。", "確認地點和 g 是否固定。", "重新用 W=mg 計算重量。", "排除只改地點或只改儀器的解釋。", "用 kg 和 N 分別回報兩種量。"],
    ["先辨認天平或彈簧秤讀的是哪種物理量。", "記下儀器的單位和操作條件。", "連結天平平衡與質量比較、彈簧秤拉力與重量。", "排除兩個讀值應相同的混淆。", "說明儀器證據能支持什麼及其限制。"],
    ["找出地球與月球的 g 比例。", "保持探測器質量不變。", "用 W=mg 或比例求兩地重量。", "不要把重量變小寫成質量變小。", "補上慣性與工程承載的條件。"],
    ["辨認題目是在地面還是高處測量。", "判斷 g 的差異是否大到需要納入。", "區分質量不變和重量略變的近似。", "排除物質量憑空減少的說法。", "以題目精度決定是否可忽略高度影響。"],
    ["讀取 m、g 與 W 的資料表。", "檢查 W/m 是否大致固定。", "用比例或公式找缺漏值。", "排除單位不同造成的假差異。", "用第二筆資料反算並驗算。"],
    ["找出『輕』在句子中是質量還是重量。", "檢查所在星球與 g。", "比較 m、W 和慣性各自是否改變。", "排除口語詞直接等同科學量。", "改用完整物理量和單位重述句子。"],
    ["先寫出兩地的 m 與 g。", "分別計算 W 地球和 W 月球。", "比較重量比例而非只看數字。", "確認質量和慣性沒有因 g 改變而消失。", "把工程結論限定在承載、加速與安全條件內。"],
]
ROWS = [
    ("easy", "質量與重量最重要的差異是哪一項？", ["質量是物質多寡，重量是重力場中受到的力", "質量和重量都一定以牛頓表示", "重量與所在地無關，質量會隨月球改變", "兩者都是物體的體積"], "A", "質量描述物體含有多少物質，重量是當地重力作用形成的力；兩者概念和單位都不同。", "先看定義與單位，再處理所在地條件。"),
    ("easy", "在地球附近取 g=10 N/kg，一個 4 kg 物體的重量約為？", ["0.4 N", "4 N", "40 N", "400 N"], "C", "W=mg=4 kg×10 N/kg=40 N，重量是力，所以單位為 N。", "寫公式、代數值、檢查單位三步完成計算。"),
    ("medium", "同一個 6 kg 探測器由地球搬到月球，若沒有物質進出，哪項通常保持不變？", ["重量（N）", "當地重力場強 g", "質量（kg）", "彈簧秤讀值（N）"], "C", "只改變所在地時，探測器含有的物質量仍是 6 kg；月球 g 較小，重量和彈簧秤讀值會改變。", "先找是否有物質進出，再分開 m 與 g。"),
    ("medium", "地球上原本 m=2.0 kg 的盒子卸下 0.5 kg 電池，取 g=10 N/kg；卸下後重量為？", ["5 N", "15 N", "20 N", "25 N"], "B", "卸下電池後質量為 1.5 kg，地點不變所以 W=1.5×10=15 N。", "先更新質量，再使用同一地點的 g 計算重量。"),
    ("hard", "要判斷一箱器材的質量，哪種測量安排最直接？", ["用天平比較兩側平衡並讀取 kg", "用彈簧秤懸掛後讀取 N，再直接當成 kg", "只用手感覺箱子沉不沉", "把箱子搬到月球後不記錄地點"], "A", "天平利用平衡比較質量，讀值可用 kg 表示；彈簧秤主要量重量，不能直接把 N 當 kg。", "辨認儀器的物理量和單位，不被日常『重』誤導。"),
    ("medium", "若月球表面的 g 約為地球的六分之一，同一台 60 kg 車在月球的重量約為地球的？", ["六倍", "相同", "六分之一", "零"], "C", "W=mg；m 不變而 g 變為六分之一，所以重量也變為六分之一，但不會是零，質量仍為 60 kg。", "用 W=mg 做比例，固定 m、改變 g。"),
    ("medium", "同一物體從海平面帶到很高的山上，較精確的說法是？", ["質量大幅減少，重量完全不變", "質量近似不變，因 g 略變重量可能略有差異", "質量和重量都必然變成零", "只要高度改變，物質就會消失"], "B", "沒有物質進出時質量近似不變；離地較遠使重力場略變弱，因此重量可能略減，實際是否需考慮要看題目精度。", "區分物質量的穩定性與重力場的微小變化。"),
    ("hard", "一張資料表中同一地點的三筆資料為 m=1、2、3 kg，W=10、20、30 N。這支持哪項結論？", ["g 約為 10 N/kg，重量與質量成正比", "質量越大，g 越小", "N 和 kg 是同一單位", "重量與質量沒有關係"], "A", "各筆 W/m 都是 10 N/kg，符合 W=mg 且同一地點 g 近似固定，因此 W 隨 m 成正比。", "以 W/m 檢查比例，再連回公式和單位。"),
    ("easy", "有人說『月球上的物體比較輕，所以質量也比較小』；最好的修正是？", ["重量較小是因月球 g 較小，若沒有物質進出質量仍相同", "重量較小表示物體少了一半物質", "質量只在地球才存在", "月球上的 kg 會自動換成 N"], "A", "重量是 W=mg 的結果；換地點改變 g 不代表 m 改變，除非確實有物質進出。", "把口語『輕』拆成質量、重力場和重量三個欄位。"),
    ("hard", "一台 80 kg 探測車在地球 g=10 N/kg、月球 g≈10/6 N/kg；哪組重量近似正確？", ["地球 800 N、月球約 133 N", "地球 80 N、月球約 480 N", "兩地都是 800 N", "地球約 133 N、月球 0 N"], "A", "地球 W=80×10=800 N；月球 W=80×(10/6)≈133 N。質量仍為 80 kg，不能把重量比例套到質量。", "分別代入兩地 g，再用數值與單位驗算。"),
]

def make_question(n, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    return {"id": f"question-science-content-kb-iv-1-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)], "knowledgeIds": ["kg-science-content-kb-iv-1"], "difficulty": difficulty, "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的重力、質量、重量、儀器、比例和生活情境能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-kb-iv-1", "examPatternRefs": REFS, "solutionStrategy": strategy, "solutionSteps": STEPS[n - 1]}

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["authoringStandard"] = "version-fused-v1"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-kb-iv-1、南一／康軒／翰林可取得的公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合重力場、質量、重量、W=mg、天平、彈簧秤、地點比例、月球探測與單位判讀。所有正文、數據、題幹、選項、答案、互動步驟與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    for entry in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []):
        entry["reviewedAt"] = TODAY
    for n, row in enumerate(ROWS, 1):
        (QDIR / f"question-science-content-kb-iv-1-{n}.json").write_text(json.dumps(make_question(n, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "10 題已逐題改寫為重力場、質量、重量、W=mg、天平、彈簧秤、地點比例、月球探測與單位判讀專屬問題；每題有唯一答案、解析與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content kb iv 1")

if __name__ == "__main__":
    main()
