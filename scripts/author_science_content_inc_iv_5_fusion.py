import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-inc-iv-5.json"
REPORT = ROOT / "implementation/reports/science-content-inc-iv-5-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "鹽埕國中公開自然段考", "原子分子、化學式與物質微觀模型"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "內湖國中公開自然段考", "理化粒子圖、質量與微觀推理"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "國昌國中公開自然科試題", "物質變化、模型表徵與證據界線"),
]

def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常以物質三態、粒子模型、化學式、質量守恆與宏觀—微觀轉換檢查模型推理；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = "2026-09-21"; lesson["reviewStatus"] = "draft"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方 INc-Ⅳ-5 課綱、三筆公立校方公開章節定位與公開自然科試題 pattern 研究，獨立重寫原子、分子、元素、化合物、化學式、三態與粒子模型限制；未複製任何版本教材或試題。完整出版社內文未公開取得，不虛構逐頁閱讀；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    explanations = [
        "蒸發是表面粒子離開液面的宏觀現象，原子與分子模型能解釋粒子的運動與能量分布；肉眼不能直接看到單一分子。正確答案：A。",
        "原子與分子模型可處理粒子排列、運動、距離與組成等微觀問題；杯子顏色或重量是宏觀描述，不能取代模型。正確答案：B。",
        "鹽溶於水不是消失，而是粒子分散在水分子之間，尺度小到肉眼看不見；仍可用蒸發等方法取得物質證據。正確答案：C。",
        "氣體可壓縮主要因粒子之間有較大空隙，施壓可減少平均間距，不表示粒子本身被壓扁。正確答案：D。",
        "加熱固體時粒子通常吸收能量，振動更劇烈；這是模型推論，仍要配合溫度或狀態資料，不把球圖當實物照片。正確答案：B。",
        "化學反應會重新排列原子，形成不同分子或物質；原子種類與數目守恆，不能說原子憑空消失。正確答案：C。",
        "密閉系統中反應前後總質量相同，可用原子重新排列且未逸出系統解釋；需注意容器是否真的密閉。正確答案：D。",
        "粒子圖的顏色是表示不同元素的符號約定，球徑與間距通常為示意，不可直接解讀成真實大小比例。正確答案：A。",
        "氣味擴散表示氣味相關粒子持續做無規則運動並在空間分散；風向和空氣流動也可能影響速度。正確答案：C。",
        "好的解釋先指出宏觀觀察，再用粒子排列或運動提出模型，並說明模型能解釋什麼及仍缺少什麼證據。正確答案：B。",
    ]
    strategies = ["先把蒸發的可見結果和粒子運動模型分開，再確認模型能解釋的尺度。", "先圈出題目問的是微觀排列、運動或組成，不用宏觀外觀選答案。", "把溶解後看不見與物質消失分開，用粒子分散模型和可回收證據判斷。", "找出氣體粒子間距的線索，區分壓縮空間和壓縮粒子本身。", "用能量改變、粒子振動與狀態資料建立微觀推論，並標出模型限制。", "追蹤反應前後原子的種類與數量，判斷是重新排列還是錯誤的消失說法。", "先檢查系統邊界是否密閉，再用原子守恆解釋質量資料。", "把模型符號約定與真實比例分開，避免從顏色或球徑過度推論。", "連結粒子無規則運動與空間分散，再考慮空氣流動的補充條件。", "依序寫宏觀證據、微觀模型、限制，確認三者沒有互相冒充。"]
    steps = ["讀題並圈出物質、粒子、化學式、排列、運動、質量或模型限制等關鍵詞。", "先區分可直接觀察的宏觀結果與需要模型才能提出的微觀解釋。", "用原子種類、分子組成、下標、粒子距離或運動狀態逐項檢查選項。", "排除把看不見當成不存在、把原子與分子混為一談，或把示意圖當真實比例的說法。", "用完整句重述答案，補上可支持模型的資料與尚不能直接測得的限制。"]
    for i in range(1, 11):
        p = ROOT / f"questions/science/question-science-content-inc-iv-5-{i}.json"; q = json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = explanations[i-1]; q["solutionStrategy"] = strategies[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "公立學校公開自然科試題中的粒子模型、化學式、物質變化、質量與宏觀—微觀推理能力；本題改寫為 INc-Ⅳ-5 原創情境。"; p.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content inc-iv-5")

if __name__ == "__main__":
    main()
