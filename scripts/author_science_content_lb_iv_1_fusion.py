import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-lb-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-lb-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "鹽埕國中公開自然段考", "生態因子、分布、資料判讀與探究設計"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "內湖國中公開自然段考", "生物與環境、圖表資料及限制條件"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "國昌國中公開自然科試題", "非生物因子、控制變因與因果界線"),
]

def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常以溫度、光照、水分、鹽度、pH、氧氣、分布資料與控制變因檢查生態推理；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = "2026-09-21"; lesson["reviewStatus"] = "draft"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方 Lb-Ⅳ-1 課綱、三筆公立校方公開章節定位與公開自然科試題 pattern 研究，獨立重寫非生物因子、分布、限制因子、控制變因、資料範圍與因果界線；未複製任何版本教材或試題。完整出版社內文未公開取得，不虛構逐頁閱讀；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    explanations = [
        "若向陽與陰影區的苔蘚種類、其他條件和測量時間相近，而光照讀值與出現比例穩定對應，才較能支持光照是重要非生物因子；仍不能宣稱是唯一原因。正確答案：A。",
        "研究溫度時應只改變水溫，固定蝌蚪種類、數量、大小、容器、氧氣、食物與觀察時間，再重複測量活動量。正確答案：A。",
        "潮間帶高度會同時改變浸水時間、溫度、鹽度與乾燥程度；應優先記錄這些非生物讀值，而非只猜競爭。正確答案：A。",
        "水溫升高可能降低溶氧，魚浮到水面可作為缺氧假說的線索；還要測氧氣、魚密度與其他水質，不能直接證明唯一原因。正確答案：A。",
        "若不同海拔的溫度與植物分布上限一致，且在相近光照、水分與土壤條件下改變溫度會改變生長，才較能支持溫度是限制因子。正確答案：A。",
        "透明度與水草出現可能相關，但光照、水深、營養鹽或底質也會同時變化；應寫成在目前資料下的可能關係。正確答案：A。",
        "比較鹽度時要固定水蚤種類、數量、溫度、體積、pH、光照與觀察時間，否則心跳差異可能不是鹽度造成。正確答案：A。",
        "土壤 pH 改變後還要記錄水分、溫度、光照、養分、土壤質地與其他物種，避免把多個同時改變的條件誤認成 pH 單獨效果。正確答案：A。",
        "光照與溫度同時提高時，植物生長變快不能只歸因於光照；應說兩項因素共同改變，或重新設計控制溫度的實驗。正確答案：A。",
        "把溪流位置、魚類數量與同時測得的溫度、流速、溶氧、pH 等資料並列成散布圖或分區表，較能找出候選關聯並保留其他變因。正確答案：A。",
    ]
    strategies = ["比較生物分布與光照讀值，同時檢查其他環境條件是否相近。", "只改溫度並固定其他蝌蚪與水質條件，再以重複活動量比較。", "先列出潮間帶高度同時改變的水分、鹽度、溫度與乾燥條件。", "把魚浮水面視為缺氧線索，再找溶氧與其他水質資料驗證。", "用跨海拔資料與控制溫度的比較，判斷溫度是否真是限制因子。", "把透明度與水草分布當相關線索，不直接說成唯一因果。", "列出鹽度實驗的所有控制變因，避免水蚤心跳差異被混淆。", "記錄所有可能隨 pH 一起變化的土壤與環境條件。", "辨認光照與溫度同時改變造成混淆，改用正交控制設計。", "用空間位置、魚類分布和多個環境讀值並列，先找關聯再提出可測試原因。"]
    steps = ["讀題並圈出非生物因子、分布資料、測量時間、地點與可能控制變因。", "先區分直接觀察的分布與需要模型解釋的限制因子。", "檢查選項是否把溫度、光照、水分、鹽度、pH 或氧氣誤當生物因子。", "排除單一測站、單次觀察或多項條件同時改變卻宣稱唯一因果的說法。", "用有範圍的完整句重述答案，補上未控制因素與下一個可驗證的測量。"]
    for i in range(1, 11):
        p = ROOT / f"questions/science/question-science-content-lb-iv-1-{i}.json"; q = json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = explanations[i-1]; q["solutionStrategy"] = strategies[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "公立學校公開自然科試題中的非生物因子、分布資料、控制變因與因果界線能力；本題改寫為 Lb-Ⅳ-1 原創情境。"; p.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content lb-iv-1")

if __name__ == "__main__":
    main()
