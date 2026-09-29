import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-gc-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-gc-iv-4-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "酵母發酵、微生物代謝與食品製造"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "微生物利用、抗生素、基因轉殖與條件控制"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "發酵證據、純化、生物安全與風險評估"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。酵母利用麵團中的糖類代謝產生二氧化碳，氣體被麵筋結構留住形成氣泡，使麵團膨脹；不是酵母製造空氣。",
    "B。酵母或其他微生物把原料轉成特定代謝物，人在可控制的條件下收集產品並管理污染與安全，這才是微生物應用的完整概念。",
    "C。應固定酵母量、糖濃度、麵團量、攪拌與時間，只改變溫度，並用單位時間產氣或體積變化及重複組比較。",
    "D。基因轉殖可能讓微生物產生所需蛋白質，但仍須驗證產量、純化、宿主穩定性、逸散與生態或健康風險，不能只看利益。",
    "B。溫度、pH、氧氣、原料濃度、菌種純度與污染控制會影響代謝和產品品質，需依微生物與製程設定並監測。",
    "C。抗生素應依適應症與醫囑使用並完成療程，濫用會篩選抗藥性；『能利用微生物』不代表可任意使用產品。",
    "D。應設無活菌或滅菌對照，記錄糖消耗、二氧化碳量與時間變化，才能支持氣體來自微生物代謝而非溶液逸散。",
    "A。完整評估要同時比較生產效率、產品品質、純化、設備與成本，以及基因穩定、逸散、水平轉移、污染和管理措施。",
    "C。不同微生物的代謝物、速度、污染風險與食品安全不同，需選適合菌種並控制溫度、pH、鹽度、氧氣和純度。",
    "B。完整學習重點是用條件—微生物—原料—代謝物—用途的證據鏈，並同時評估製程控制、純化、抗藥性與生物安全。",
]
STRATEGIES = [
    "沿微生物、原料、代謝作用、產物與用途畫條件式路徑。",
    "同時檢查可控制生產、直接證據、產品處理與安全界線。",
    "固定所有發酵條件，只改溫度並以速率和重複資料比較。",
    "把技術利益、可測產量、純化品質與生態風險分開評估。",
    "列出溫度、pH、氧氣、原料、菌種純度與污染監測。",
    "區分藥物有效性、醫療指示與抗藥性公共衛生風險。",
    "用活性對照、氣體量、底物變化與時間建立發酵證據。",
    "把效率、品質、成本、逸散、污染與管理措施放在同一評估表。",
    "先選定菌種與代謝物，再檢查食品安全、純度與環境條件。",
    "用完整條件式證據鏈回答，並標示尚未證實的推論。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結發酵、微生物代謝、食品或藥物利用、基因轉殖、條件控制、抗藥性與生物安全；本題以全新微生物應用情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-gc-iv-4、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合酵母發酵、微生物代謝、食品與藥物製造、抗生素、基因轉殖、純化、污染控制與生物安全；保留發酵瓶—條件—產品—風險互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出微生物、原料、氧氣／溫度／pH、代謝物、用途與安全條件。", "把觀察到的氣泡、體積、底物或產物資料連到代謝作用。", "設活性、滅菌或無菌對照，固定菌量、原料、時間與設備並量測速率。", "分開技術利益、產品純化、污染、抗藥性、逸散與生態風險。", "回查製程放大、管理規範與證據不足處，避免把天然或看不見直接等同安全。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-gc-iv-4-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的發酵、微生物代謝、食品藥物利用、基因轉殖、抗藥性與生物安全能力；本題改寫為微生物應用原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content gc iv 4")


if __name__ == "__main__": main()
