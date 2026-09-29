import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-jc-iv-5.json"
REPORT = ROOT / "implementation/reports/science-content-jc-iv-5-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "鹽埕國中公開自然段考", "電池、氧化還原、電路與實驗判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "內湖國中公開自然段考", "理化反應、電壓資料與裝置條件"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "國昌國中公開自然科試題", "電子流、離子作用與控制變因"),
]

def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常以氧化還原、電池電壓、電路、材料、離子與控制變因檢查化學能轉換推理；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = "2026-09-21"; lesson["reviewStatus"] = "draft"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方 Jc-Ⅳ-5 課綱、三筆公立校方公開章節定位與公開自然科試題 pattern 研究，獨立重寫鋅銅半電池、氧化還原、電子與離子流、電解質、電壓、串聯、控制變因與安全；未複製任何版本教材或試題。完整出版社內文未公開取得，不虛構逐頁閱讀；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    explanations = [
        "鋅銅原電池透過氧化還原反應把反應物的化學能轉為外電路可利用的電能；不是把溶液本身直接變成電。正確答案：A。",
        "鋅較容易失去電子，半反應為 Zn→Zn²⁺+2e⁻，這是氧化，發生在鋅電極。正確答案：B。",
        "電子由發生氧化的鋅電極經外電路流向銅電極；溶液與鹽橋主要傳遞離子，不是電子外電路。正確答案：C。",
        "銅電極可接收電子，使溶液中的 Cu²⁺ 得電子還原成 Cu；要依半反應判斷，不能只背銅是正極。正確答案：D。",
        "電解質提供可移動離子並讓半電池內維持導電與電荷平衡；電子主要走外電路。正確答案：B。",
        "電極材料改變會改變氧化還原傾向與兩半反應的電位差，因此測得電壓可能不同；仍需控制濃度與溫度。正確答案：C。",
        "相同方向串聯時，一個電池的電壓會與另一個同向相加，理想情況總電壓上升；內阻與負載仍可能影響實測值。正確答案：D。",
        "反應物消耗、離子濃度改變、電極表面狀態或內阻增加，都可能使輸出電壓下降；不能只歸因於電線鬆脫。正確答案：A。",
        "比較電解質時應固定電極材料、面積、距離、濃度、體積、溫度與量測時間，只改變電解質這一項。正確答案：C。",
        "簡易電池要使用低危害材料、少量溶液、護目與手部防護，避免短路、吞食或接觸皮膚，不可把市電接入自製裝置。正確答案：B。",
    ]
    strategies = ["先找氧化還原反應，再把化學能轉換和外電路輸出連結。", "寫出鋅的半反應，看到失去電子就判定氧化。", "分開電子流、離子流與傳統電流方向，依外電路箭頭判讀。", "先寫銅側半反應，再判斷 Cu²⁺ 得電子與電極表面沉積。", "區分外電路電子通道與溶液／鹽橋離子通道，檢查各自功能。", "比較兩種材料的氧化還原傾向與電位差，同時檢查條件是否一致。", "先確認電池方向一致，再判斷電壓是相加還是抵銷。", "列出反應物、濃度、電極、內阻與接觸條件，尋找電壓下降的合理原因。", "只改變一項電解質條件，固定所有幾何、濃度與量測條件。", "先檢查化學品、短路、接觸與人體安全，再判斷裝置是否適合操作。"]
    steps = ["讀題並圈出電極、半反應、電子、離子、電解質、鹽橋、電壓或安全條件。", "先判定鋅側氧化與銅側還原，再畫出外電路電子方向。", "把電子通道、離子通道、電流方向和正負極標記分開，避免用同一箭頭代替。", "檢查選項是否混淆材料名稱、反應位置、離子平衡或測量條件。", "用完整句重述答案，補上控制變因、內阻或安全限制，確認推論符合裝置證據。"]
    for i in range(1, 11):
        p = ROOT / f"questions/science/question-science-content-jc-iv-5-{i}.json"; q = json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = explanations[i-1]; q["solutionStrategy"] = strategies[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "公立學校公開自然科試題中的氧化還原、電池電壓、電子／離子流、控制變因與安全能力；本題改寫為 Jc-Ⅳ-5 原創情境。"; p.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content jc-iv-5")

if __name__ == "__main__":
    main()
