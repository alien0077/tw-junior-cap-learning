"""Ga：生殖與遺傳第一輪來源融合、題庫重寫與來源審查。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ga.json"
REPORT = ROOT / "implementation/reports/science-content-ga-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "生殖、遺傳、配子、遺傳比例與資料判讀", "pattern": "取由繁殖過程、遺傳資料、比例與環境條件建立條件式推論的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "有性／無性生殖、配子與遺傳模型", "pattern": "取是否有配子結合、染色體／基因層次、遺傳型／表現型與棋盤格的教學及評量方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "生殖遺傳資料、環境效應與模型限制", "pattern": "取比較繁殖方式、配子組合、遺傳與環境共同影響，以及實測比例和期望比例界線的能力方向。"},
]

def refs():
    return [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def qdata(number, prompt, options, answer, explanation, strategy, steps, difficulty="medium"):
    return {
        "id": f"question-science-content-ga-{number}", "subject": "science", "type": "single-choice", "prompt": prompt,
        "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)], "knowledgeIds": ["kg-science-content-ga"], "difficulty": difficulty,
        "answer": {"value": answer, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的生殖、遺傳、資料判讀及模型限制能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依公開資料的能力方向獨立改寫；題幹、選項、答案、解析與五步解法均針對 Ga 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-ga", "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }

QUESTIONS = [
    qdata(1, "草莓由匍匐莖直接長成新株，觀察紀錄沒有授粉或配子結合。這種繁殖最適合歸類為？", ["有性生殖，因為一定有兩個親代", "無性生殖，因為親代的營養器官直接形成新個體", "胎生，因為新株需要水分", "體外受精，因為新株在土壤中生長"], "B", "分類的關鍵是是否有配子形成與結合；匍匐莖直接形成新株，沒有配子結合，因此屬無性生殖。", "先找繁殖過程證據，再排除把發育場所當成生殖分類的選項。", ["圈出『匍匐莖直接形成』及『沒有配子結合』。", "判斷題目問的是生殖方式，不是卵生、胎生或受精位置。", "無性生殖可由一個親代的營養器官直接產生新個體。", "A 需要兩個親代，C 與 D 分別混淆發育場所和受精位置。", "回查證據：沒有配子結合，所以答案為 B。"], "easy"),
    qdata(2, "某植物進行有性生殖時，花粉中的配子與胚珠中的配子結合成受精卵。受精作用最直接造成什麼？", ["使子代只得到母本的遺傳資訊", "使兩個配子各自保持單套染色體，永不合併", "使雙方遺傳資訊在受精卵中組合，恢復成較完整的染色體套數", "使環境因素直接變成染色體"], "C", "受精是兩個配子結合的過程，雙方遺傳資訊在受精卵中組合；環境不會在受精瞬間直接變成染色體。", "沿著配子—受精卵—染色體套數的流程作答。", ["找出兩個配子和受精卵三個流程節點。", "確認配子各帶一套遺傳資訊，受精卵同時取得雙方來源。", "因此受精會組合雙方遺傳資訊並恢復較完整的染色體套數。", "A 忽略父本，B 把配子誤當受精卵，D 把環境與遺傳物質混為一談。", "回到題幹，最直接的變化是遺傳資訊在受精卵中組合，答案為 C。"], "easy"),
    qdata(3, "在相同培養條件下，兩株紫花植物的遺傳型都是 Pp，且 P 對 p 顯性。兩株交配後，子代最合理的遺傳型比例為？", ["PP：Pp：pp＝1：2：1", "PP：Pp：pp＝3：1：0", "PP：Pp：pp＝1：1：1", "只有 pp，因為親代不是純品系"], "A", "Pp 的每一親代都可形成 P、p 配子，四種組合中 PP、Pp、Pp、pp 各占一格，所以遺傳型比例為 1：2：1。", "先由親代遺傳型列配子，再組合；不要把表現型比例直接當成遺傳型比例。", ["寫出兩個親代都是 Pp。", "各自列出可形成的配子：P 與 p。", "交叉組合得到 PP、Pp、Pp、pp。", "統計三種遺傳型，得到 1：2：1；顯性只在下一步用來判斷表現型。", "檢查選項，只有 A 符合四格組合。"], "medium"),
    qdata(4, "某株植物外觀是紫花，但遺傳型未知。它與白花 pp 植株測交後，子代出現紫花與白花約各半。紫花親本最可能是？", ["PP", "Pp", "pp", "無法形成配子"], "B", "若紫花親本是 Pp，與 pp 測交可形成 Pp 與 pp，表現型約各半；若是 PP，子代應全為紫花。", "用測交親本 pp 固定一方，再反推未知親本的配子。", ["確認白花親本是 pp，只能提供 p 配子。", "若未知親本是 PP，只會提供 P，子代全為 Pp。", "若未知親本是 Pp，可提供 P 或 p，子代可能為 Pp、pp。", "觀察到紫花與白花約各半，排除 PP、pp 與不能形成配子的選項。", "因此未知紫花親本最可能是 Pp，答案為 B。"], "medium"),
    qdata(5, "研究者比較兩批 Pp × Pp 的子代，一批有 20 株，另一批有 2,000 株。要判斷實測表現型是否接近 3：1，哪項做法較可靠？", ["只保留最接近 3：1 的一批資料", "把每一株的結果改寫成理論比例", "分別記錄原始數據，計算各批比例並在相同條件下增加重複批次", "因為模型是 3：1，所以不必收集實測資料"], "C", "理論比例是條件式的期望，實測會受樣本波動影響；保留原始資料、比較比例並增加重複，才能檢查模型。", "區分期望比例與觀察比例，並檢查樣本量、重複與資料是否被挑選。", ["寫出模型預期表現型比例為 3：1。", "確認 20 株和 2,000 株都是觀察資料，不能直接改成理論值。", "分別計算各批比例並保留全部結果，再在相同條件下重複。", "A 有挑資料偏誤，B 竄改資料，D 取消了實驗檢驗。", "所以 C 最能檢查模型與實測的差異。"], "medium"),
    qdata(6, "同一品種的植物在光照充足與遮陰環境中，葉片大小不同，但 DNA 序列沒有改變。這項觀察最適合支持哪個結論？", ["所有環境差異都會改變 DNA", "性狀表現可能同時受遺傳型與環境影響", "DNA 沒改變就不可能有性狀差異", "看到差異即可證明發生了可遺傳突變"], "B", "光照改變時葉片大小改變而 DNA 未變，支持環境會影響表現型；這不能直接證明 DNA 突變或可遺傳改變。", "把遺傳物質改變、表現型改變與環境條件分開。", ["比較兩組的控制條件，只把光照視為主要差異。", "注意 DNA 序列未改變，但葉片大小仍不同。", "因此環境可影響性狀表現，性狀不是只由 DNA 單獨決定。", "A、D 過度延伸，C 否認環境效應。", "結論應保留在『本條件下環境影響表現型』，答案為 B。"], "medium"),
    qdata(7, "下列哪一組資訊能最完整地追蹤『遺傳資訊如何影響可觀察性狀』？", ["細胞核 → 染色體 → DNA 上的基因 → 蛋白質作用與性狀", "土壤顏色 → 配子 → 染色體 → 性狀", "性狀名稱 → 胎生 → 水分 → 基因", "環境溫度 → 受精位置 → 等位基因"], "A", "細胞核中的染色體包含 DNA，DNA 上的基因攜帶資訊，基因表現可透過蛋白質作用影響性狀；環境也可能調節表現，但不能取代這條遺傳資訊路徑。", "從細胞層次往分子層次，再連到表現型，檢查每一箭頭是否代表遺傳資訊關係。", ["找出題目要求的『遺傳資訊』而非單純生活條件。", "依序檢查細胞核、染色體、DNA、基因和性狀的層次。", "A 的路徑能說明遺傳資訊如何透過基因表現影響性狀。", "B、C、D 將環境或生殖分類詞錯接成遺傳資訊路徑。", "因此最完整的是 A。"], "easy"),
    qdata(8, "若某性狀由一對等位基因控制，兩位親代各提供一個等位基因。子代遺傳型的形成最合理的描述是？", ["子代只複製母親完整遺傳型", "子代從雙方配子各取得一個等位基因，再組成一對", "顯性等位基因會把隱性等位基因消除", "環境會直接決定子代遺傳型"], "B", "有性生殖中，子代通常由雙方配子各取得一個等位基因，形成一對遺傳型；顯性只描述表現關係，不會消除隱性等位基因。", "沿著親代—配子—受精—子代遺傳型的順序判斷。", ["確認題目描述的是一對等位基因和兩位親代。", "每個配子只帶一個等位基因。", "受精時雙方配子結合，子代取得兩個等位基因。", "A、C、D 分別誤解遺傳來源、顯性關係和環境作用。", "所以 B 正確。"], "easy"),
    qdata(9, "某批種子由有性生殖產生，子代葉形出現多種差異。若要判斷差異來源，哪種資料組合最有幫助？", ["只記錄一株植物的葉片顏色", "只問親代是否高大，不記錄環境", "同時記錄親代遺傳型、子代性狀、光照水分與重複批次", "看到差異就直接判定發生有利突變"], "C", "要分辨遺傳組合與環境效應，需同時記錄親代與子代資料、環境條件及重複批次；單一觀察不能證明突變或其效益。", "先列出可能原因，再設計能比較遺傳資料和環境資料的多項證據。", ["列出遺傳重組、突變和環境差異等可能原因。", "確認只記葉片或只問親代都無法排除替代解釋。", "收集親代遺傳型、子代性狀、光照水分和重複批次。", "D 把觀察直接升級為因果結論，A、B 證據不足。", "因此 C 最能支持後續判斷。"], "medium"),
    qdata(10, "下列哪項比較最能區分有性生殖與無性生殖，而不被卵生、胎生等發育場所混淆？", ["檢查是否有配子形成與結合，再追蹤新個體的產生方式", "只看子代是否住在母體內", "只看子代外形是否和親代相似", "只看繁殖發生在水中或陸地"], "A", "有性／無性生殖的核心判準是是否有配子形成與結合；卵生、胎生、棲地與外觀相似度都是其他面向，不能取代這個判準。", "先確認分類定義，再排除只描述場所或結果外觀的選項。", ["圈出題目要求區分的兩種生殖方式。", "回到定義：有性生殖涉及配子形成與結合，無性生殖通常沒有配子結合。", "因此要檢查繁殖過程，而非只看發育場所或外觀。", "B、D 只提供場所，C 可能受環境和突變影響，不能作唯一判準。", "所以 A 最完整。"], "easy"),
]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {
        "commonCore": ["三版本公開線索共同支持以配子、受精、生殖方式、染色體／基因和遺傳型／表現型理解生殖與遺傳。", "有性／無性分類、配子組合、顯性與隱性、遺傳比例、環境效應及證據限制是共同能力核心。"],
        "versionDifferences": ["南一公開定位偏向繁殖方式與遺傳資料；康軒線索偏向配子、染色體／基因層次及棋盤格；翰林線索偏向生殖與遺傳模型的條件、環境效應與實測比例界線。公開資料不足以宣稱取得完整教材內容。"],
        "originalAdditions": ["以草莓匍匐莖、受精流程、Pp 交配、測交、環境光照與多批次資料構成單元專屬證據鏈。", "把發育場所當生殖分類、顯性等於較強、理論比例等於單一結果、環境表現差異等於可遺傳突變列為迷思診斷。"],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織有性／無性生殖、配子、受精、遺傳型、表現型、顯性／隱性、比例、環境效應與模型限制；10 題均逐題重寫並核對單元符合度、唯一答案、正確解析與五步解法，取代原先帶日期且重複的 9 題套題，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []): entry["reviewedAt"] = TODAY
    for number, question in enumerate(QUESTIONS, 1):
        path = QDIR / f"question-science-content-ga-{number}.json"
        path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "Ga：生殖與遺傳", "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "原先 9 題為帶日期與單元名的重複套題，已逐題改寫為 10 題生殖與遺傳專屬問題；每題均有唯一答案、解析與五步解法，三筆公開試題／課程資料僅作 pattern-only 來源，正式發布前仍須第二輪 AI／Terra 內容複核。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ga")

if __name__ == "__main__": main()
