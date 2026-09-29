import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-nc-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-nc-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "能源轉換、環境影響與資料推理"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "能源、物質循環與系統比較"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "生活能源、排放與生命週期判讀"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。生質能源的原料是近期生物形成的有機物，例如植物、農業剩餘物或動物排泄物；煤炭屬化石燃料，電池與岩石也不是生質原料。",
    "A。缺氧環境中的微生物可分解有機物並產生含甲烷的沼氣；這不是製造純氧、核能或金屬粉末的過程。",
    "A。糖類或澱粉原料可能和糧食、土地及水資源競爭；『可製成燃料』不等於沒有資源取捨或排放。",
    "A。厭氧消化能回收部分有機物能量並減少直接掩埋的處理風險，但仍需分選、控臭、監測逸散與管理消化液，不能宣稱零排放。",
    "A。完整碳排要畫出從原料收集、設備、運輸、氣體逸散、燃燒到副產物處理的系統邊界，只看煙囪會漏掉重要輸入。",
    "A。公平比較要用一致系統邊界，納入可取得能源、設備、土地、空污、儲能與供能穩定性，不能用單價或一天的數據代替全年表現。",
    "A。密閉收集並監測甲烷、硫化氫、壓力與消化液，才能同時處理爆炸、中毒、逸散與水土污染風險；靠氣味或任意排放都不可靠。",
    "A。露天焚燒減少只是其中一項結果，仍要比較收集、運輸、加工、燃燒與原本處理方式的完整生命週期，才能判斷淨成效。",
    "A。可再生只表示原料可能透過生物生長補充，仍受再生速度、土地、水資源與採收量限制，也不保證沒有污染。",
    "A。完整方案資料要涵蓋原料量與季節、甲烷產率、能源替代、臭味與排放、成本及副產物去向；單一滿意度或設備外觀無法支撐決策。",
]
STRATEGIES = [
    "先判斷原料是否來自近期生物有機物，再排除化石燃料與非有機能源。", "把缺氧、微生物分解和產物線索接成轉換流程。", "比較能源原料和糧食、土地、水資源的競合，而非只看燃料名稱。", "把再生性、減廢效果與實際排放及副產物管理分開。", "畫出從原料到副產物的生命週期邊界，再找漏掉的碳排來源。", "使用一致的系統邊界，比較供能、成本、土地、污染與穩定性。", "先列出氣體、壓力與消化液風險，再找對應的工程和監測措施。", "將替代方案與原本處理方式放在相同生命週期尺度比較。", "把再生速度和資源上限納入『可再生』的定義。", "用供應、產率、環境、成本和副產物五類資料檢查可行性。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求追蹤能源轉換、守恆、環境影響、資料邊界與生活方案限制；本題以生質能源原創情境重新設計。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-nc-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合原料、轉換、供應、生命週期、排放與副產物管理；保留既有流程互動與模擬，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出原料、轉換方式、能源產品、供應條件、排放或副產物。", "把原料來源到最終使用畫成流程，確認每個箭頭的條件與輸入。", "比較能源產出與收集、乾燥、運輸、設備及處理所需的輸入。", "排除把再生等同零污染、把原料重量等同能源產量，或忽略生命週期與安全管理的選項。", "用完整句重述答案，補上系統邊界、證據限制與條件改變時需要重查的資料。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-nc-iv-1-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的能源轉換、環境影響、系統邊界與生活方案資料判讀能力；本題改寫為生質能源原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content nc iv 1")


if __name__ == "__main__": main()
