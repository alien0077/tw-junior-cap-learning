#!/usr/bin/env python3
"""Record public-school/publisher structure evidence for all science performance units."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://www.zmjhs.tyc.edu.tw/uploads/neilfilefolder/14file/file/16_70_5116%E6%99%AE%E9%80%9A%E7%8F%AD%E5%90%84%E5%B9%B4%E7%B4%9A%E5%90%84%E9%A0%98%E5%9F%9F%E7%A7%91%E7%9B%AE%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%E8%87%AA%E7%84%B6%E9%A0%98%E5%9F%9F.pdf", "忠明國中公立校方南一版自然領域課程計畫；自然探究與學習表現架構定位。"),
    ("kanghsuan", "https://digitalmaster.knsh.com.tw/all/video/public/j_nature.xml", "康軒官方公開自然資源 XML；冊次、章節與探究活動結構定位，與公立校方課程計畫交叉核對。"),
    ("hanlin", "https://drive.google.com/uc?id=1gMUVcDjfXmqIapg-fNnfPuLFaK98dxGX&export=download", "林口國中公立校方翰林版自然課程計畫附件；自然探究、證據與表達活動定位。"),
]
DETAILS = {
    "a": ("科學態度與本質", "觀察事實、證據界線與科學態度", "用觀察紀錄和可重做的證據表分開事實、解釋與價值判斷", "課堂觀察、探究紀錄、反思短答"),
    "ah": ("科學思考與探究習慣", "科學思考、探究循環與條件式結論", "把問題、變因、證據、限制與結論串成可追蹤的探究鏈", "探究報告、口頭說明、同儕檢核"),
    "ah-iv-1": ("懷疑並評估科學報導或權威解釋的證據", "來源、證據與主張強度", "比較報導中的資料、方法、樣本與推論範圍", "資料判讀、來源查核、短文論證"),
    "ah-iv-2": ("應用科學知識與探究方法做決定", "科學決策與風險權衡", "在多項限制下比較證據、成本、風險與可行方案", "情境決策、理由表、口頭辯證"),
    "ai": ("科學探究的興趣", "好奇心、動機與持續探究", "由可觀察現象提出可測試問題，記錄修正假設的歷程", "探究日誌、實作投入、學習反思"),
    "ai-iv-1": ("動手實作解決問題並獲得成就感", "實作設計與迭代修正", "將問題拆成材料、步驟、測試與改良循環", "實作作品、過程紀錄、改善說明"),
    "ai-iv-2": ("與同儕討論並分享科學發現樂趣", "合作討論與科學溝通", "用證據回應同伴、分工記錄並共同修正解釋", "小組討論、同儕回饋、成果分享"),
    "ai-iv-3": ("以科學知識與探索方法解釋現象並建立信心", "模型解釋與信心建立", "把課堂概念套到新現象，指出支持解釋的觀察與仍需查證處", "現象解釋、概念圖、口頭答辯"),
    "an": ("科學本質", "科學知識的形成與限制", "從觀察、測量、模型與共同規範理解科學知識如何建立", "概念圖、史料閱讀、短答"),
    "an-iv-1": ("科學觀察、測量與方法受共同標準規範", "測量標準與可重現性", "比較操作定義、單位、儀器與紀錄格式對結果的影響", "測量實作、誤差紀錄、方法比較"),
    "an-iv-2": ("科學知識的確定性與持久性會隨背景變化", "模型修正與證據累積", "以新證據和歷史背景說明科學解釋為何改變或保留", "資料時間線、證據論證、反思"),
    "an-iv-3": ("科學家的多元背景與共同科學特質", "科學社群與多元觀點", "從不同人物與合作案例辨認共同方法、倫理與背景差異", "人物資料閱讀、比較表、短講"),
    "p": ("探究能力－問題解決", "問題定義、證據與方案", "用問題—方法—證據—結論架構完成可檢驗的解決歷程", "探究報告、實驗紀錄、口頭說明"),
    "pa": ("分析與發現", "資料分析與規律發現", "把觀察資料整理成表格、圖表或數學關係，再提出可檢核規律", "圖表製作、數據分析、發現報告"),
    "pa-iv-1": ("分析歸納、製作圖表與數學整理資料", "資料清理與圖表選擇", "先確認單位與欄位，再選圖表、計算量與尺度呈現趨勢", "表格圖表、計算紀錄、資料解釋"),
    "pa-iv-2": ("運用科學與數學形成解釋並比較檢核結果", "模型、計算與交叉檢核", "將數學結果放回科學情境，與觀察或另一種方法比較", "計算題、模型比較、結論檢核"),
    "pc": ("討論與傳達", "證據溝通與科學表達", "依受眾選用文字、圖表、模型或口語，完整呈現方法與限制", "海報簡報、口頭報告、同儕提問"),
    "pc-iv-1": ("檢核探究過程、證據與結果並提出改善", "品質控制與改進", "逐項回查變因、測量、樣本與推論，提出可執行的下一輪改善", "探究自評、錯誤診斷、修正版報告"),
    "pc-iv-2": ("以多種形式完整表達探究過程與成果", "多模態科學傳達", "把同一探究轉成報告、圖表、簡報或模型並保留證據鏈", "成果展、簡報、書面報告"),
    "pe": ("計劃與執行", "探究設計與安全操作", "由問題選變因、器材、步驟與記錄方式，依安全規範完成測量", "實驗設計、器材操作、安全檢核"),
    "pe-iv-1": ("辨明變因並規劃具可信度的探究活動", "變因控制與可信度", "區分自變、應變、控制變因，安排重複與對照以支持比較", "實驗計畫、變因表、設計評析"),
    "pe-iv-2": ("安全操作器材並進行客觀量測與記錄", "儀器、精度與客觀紀錄", "依操作規範讀取儀器、記錄有效位數與異常值，不以預期答案改寫資料", "實作觀察、量測表、誤差說明"),
    "po": ("觀察與定題", "多元觀察與可探究問題", "從現象、資料、圖像或生活情境找出可觀察差異，轉成具體問題", "問題發想、觀察紀錄、提問單"),
    "po-iv-1": ("由多元來源進行有計畫觀察並察覺問題", "來源交叉與觀察計畫", "規劃觀察時間、來源與紀錄欄位，從多筆資料找出值得探究的變化", "觀察計畫、資料摘錄、問題說明"),
    "po-iv-2": ("辨識可科學探究的問題並提出探究問題", "可測試性與問題界定", "把含糊的好奇轉成可操作、可測量且有範圍的探究問題", "問題改寫、可行性檢核、口頭說明"),
    "t": ("探究能力－思考智能", "資料推理、批判與模型思考", "在資料、模型與現象間來回比對，提出可檢驗的推理而非只猜答案", "推理短答、模型活動、資料討論"),
    "tc": ("批判思辨", "數據懷疑與替代解釋", "檢查數據品質、樣本、尺度與替代原因，再判斷主張是否過度", "數據批判、證據辯論、限制清單"),
    "tc-iv-1": ("對科學數據與資訊提出合理懷疑與解釋", "數據可信度與解釋範圍", "從來源、測量、圖表與推論鏈提出具體疑問並給出有證據的替代解釋", "圖表判讀、來源查核、論證"),
    "ti": ("想像創造", "方法變式與創新解法", "改變觀察或實驗方法，預測結果如何變化並設計可比較的測試", "創意設計、預測紀錄、原型測試"),
    "ti-iv-1": ("改變觀察或實驗方法的結果想像與創新", "方法改變與結果預測", "針對器材、尺度或程序提出變式，說明預期影響與控制條件", "設計提案、預測表、實驗比較"),
    "tm": ("建立模型", "模型建構、評估與應用", "用圖示、比例、數學或實體模型表達自然系統，再檢查模型適用範圍", "模型製作、模型評析、情境應用"),
    "tm-iv-1": ("理解、評估並應用自然界模型", "模型假設與限制", "辨認模型省略的條件，以新資料測試模型並說明何時需要更新", "模型比較、資料驗證、改版說明"),
    "tr": ("推理論證", "知識、現象與數據連結", "把課堂知識、觀察現象與實驗數據串成前提—推論—結論的論證", "證據鏈、推理題、口頭論證"),
    "tr-iv-1": ("連結知識、自然現象與實驗數據進行推論", "跨表徵推論與證據鏈", "先對齊概念、現象和數據的尺度，再說明資料如何支持或限制推論", "跨資料解釋、推理報告、同儕質詢"),
}

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8")); units = {x["lessonId"]: x for x in data["units"]}
    for code, (title, core, representation, assessment) in DETAILS.items():
        lesson_id = f"lesson-science-performance-{code}"
        units[lesson_id] = {"lessonId": lesson_id, "title": title, "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": [{"publisher": p, "sourceUrl": u, "sourceKind": "public-school-course-plan-or-official-publisher-structure", "locator": f"{l}；{title}：概念、表徵與評量定位；核讀 2026-09-21。", "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "只記錄公開課程計畫或官方公開結構的章節、教學方向與評量方式，不複製教材、例題、題目或答案。"} for p, u, l in SOURCES], "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"}}
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"]); data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str): b["reason"] = b["reason"].replace("Nine hundred fifteen unit samples", "Nine hundred fifty-four unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(DETAILS)}, ensure_ascii=False))

if __name__ == "__main__": main()
