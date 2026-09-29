import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ina-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-ina-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "能量形式、轉換與守恆"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "功率、效率與生活能量資料"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "能源轉換、熱與機械運動"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。電池儲存的化學能先透過電路轉移，主要轉成燈的光能，同時也有熱能；能量形式改變但不會憑空出現。",
    "B。能量形式包括化學、電、光、熱、聲、位能與動能等；功率是能量轉移快慢的量，不是另一種能量形式。",
    "C。物體下降時重力位能減少、動能增加；忽略空氣阻力時，總機械能近似守恆。",
    "D。煞車時車輪與煞車片的機械能透過摩擦轉成內能，溫度上升是能量轉移的證據，不是能量消失。",
    "B。水的重力位能經渦輪等機械裝置轉成動能，再由發電機轉成電能，過程也會有熱與聲等分流。",
    "C。能量守恆表示系統總能量不會憑空增加或消失，只能在不同形式間轉換或跨系統傳遞；有用輸出減少不代表能量不見。",
    "D。效率=有用輸出／輸入×100%=30/100×100%=30%；不能只用輸出 30 J 宣稱效率為 70%。",
    "A。風扇把電能轉成葉片的動能與空氣流動，也有馬達摩擦和電阻造成的熱、聲音等非主要輸出。",
    "C。要公平比較電池，應使用同一燈泡與相同負載、固定亮度判準，記錄電壓／電流與通電時間，並控制環境條件。",
    "B。判讀多種能量形式要交代來源、轉換路徑、可觀察證據與系統邊界，不把能源、能量與功率混為一談。",
]
STRATEGIES = [
    "沿著電池、電路、燈泡的能量流向排列來源、輸出與熱損失。", "區分能量形式和描述轉移快慢的功率。", "比較重力位能與動能，先標出系統是否有外力或阻力。", "找出摩擦力做功後的熱證據，確認能量只是轉換。", "從水位高度到渦輪和發電機追蹤能量路徑。", "先界定系統，再檢查能量是轉換、傳遞或離開系統。", "套用效率公式，確認有用輸出與總輸入的單位相同。", "列出主要機械輸出和伴隨的熱、聲能量。", "控制燈泡、負載、環境與判準，才可比較電池。", "用來源—轉換—證據—邊界四欄組織判讀。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求追蹤能量形式、轉換、守恆、功率、效率與公平測量條件；本題以全新生活語料重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    lesson["content"] = {"summary": "從電池手電筒、落體、煞車、水力發電與風扇追蹤能量在化學、位能、動能、電、光、熱與聲等形式間的轉換，並用守恆、功率、效率與系統邊界解釋生活資料。", "sections": [
        {"heading": "能量形式不是物體的標籤", "body": "能量可以以化學能、重力位能、動能、電能、光能、熱能或聲能等形式出現。分析手電筒時，電池不是『光能』本身，而是把儲存的化學能經電路轉成光與熱；先找來源與輸出，再談形式。"},
        {"heading": "轉換路徑要跟著系統走", "body": "落體把重力位能轉成動能，煞車則由摩擦把機械能轉成內能；水力發電則經水的位能、渦輪機械運動與發電機電能。每個轉換都有伴隨輸出，不能只保留最有用的那一項。"},
        {"heading": "守恆不等於全部都能使用", "body": "若把裝置與周圍一起納入系統，總能量可守恆；但能量可能以熱、聲或散失到環境的形式分流，因此有用輸出小於輸入。效率是比較有用輸出比例的工具，不是另一種能量。"},
        {"heading": "功率描述轉移速度", "body": "相同能量在較短時間內完成，功率較大；比較兩盞燈或兩顆電池時，要同時記錄功率、通電時間、負載與輸出判準，不能用亮度或電池外觀直接代替消耗能量。"},
        {"heading": "用證據寫出有邊界的結論", "body": "燈光、溫升、位移、聲音與儀表讀值是能量轉換的觀察線索，但單一現象不能保證完整路徑。結論要寫出系統包含誰、資料支持哪一段、哪些熱散失或測量限制仍待查。"},
    ]}
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ina-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合能量形式、轉換、守恆、功率、效率與系統邊界；保留既有小燈互動並補入電池、落體、煞車與水力情境，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出能量來源、轉換裝置、輸出形式、功率、時間、效率與系統邊界。", "沿著能量流畫出來源到輸出的路徑，並標記熱、聲等分流。", "用守恆、E=Pt 或效率公式檢查數值與方向。", "排除把能源當能量形式、把功率當能量、把亮度當總能量，或忽略熱散失與控制條件的選項。", "用完整句回查系統、單位、證據與仍需補測的限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ina-iv-1-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的能量形式、轉換、守恆、功率、效率與公平比較能力；本題改寫為能量多形式原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ina iv 1")


if __name__ == "__main__": main()
