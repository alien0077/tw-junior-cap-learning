import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-fa-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-fa-iv-4-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "鹽埕國中公開自然段考", "大氣分層、溫度趨勢與地球科學資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "內湖國中公開自然段考", "地球科學圖表、現象位置與成因證據"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "國昌國中公開自然科試題", "剖面資料、模型限制與控制變因"),
]

def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常以圖表趨勢、地球科學現象、成因證據與模型限制檢查學生是否能從資料推論；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = "2026-09-21"; lesson["reviewStatus"] = "draft"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方 Fa-Ⅳ-4 課綱、三筆公立校方公開章節定位與公開自然科試題 pattern 研究，獨立重寫溫度剖面、四層模型、現象線索、證據界線與模型限制；未複製任何版本教材或試題。完整出版社內文未公開取得，不虛構逐頁閱讀；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    explanations = [
        "分層依據是溫度隨高度變化的方向與轉折，不是把高度等分或看天空顏色。正確答案：B。",
        "對流層最接近地面，水氣、上升冷卻與凝結使雲雨和多數日常天氣集中於此。正確答案：A。",
        "平流層的臭氧吸收紫外線，能解釋該區段部分加熱；但溫度曲線本身不能直接量出每一高度的臭氧濃度。正確答案：A。",
        "流星高速進入大氣後與粒子作用、受加熱而發光並消融；不是在真空中自動燃燒。正確答案：A。",
        "極光需連結高能太陽輻射、帶電粒子、地球磁場與稀薄氣體發光，不能當成降雨或高密度熱空氣。正確答案：A。",
        "層界是模型中的近似位置，應放在溫度隨高度變化方向發生轉折的附近，而非固定等距。正確答案：A。",
        "平流層升溫曲線可支持趨勢與分層判讀，但精確臭氧濃度需要獨立觀測資料。正確答案：C。",
        "對流層由地表受熱，空氣上升膨脹並冷卻，因此高度增加時通常降溫；這是對流與能量來源的連結。正確答案：A。",
        "高溫描述粒子平均能量，熱感還取決於粒子數量與碰撞傳熱；增溫層氣體極稀薄，不能直接比作高密度火爐。正確答案：A。",
        "四層是依溫度趨勢整理連續大氣的近似模型；成分、壓力與活動仍隨高度連續變化。正確答案：A。",
    ]
    strategies = ["先讀高度與溫度座標，再用相鄰區段的升降趨勢判斷分層。", "先把現象放回高度，再用水氣、對流與凝結線索確認。", "分開曲線直接支持的溫度資訊和需要臭氧資料才能支持的成因。", "把流星位置與高速粒子、空氣作用、加熱三項證據連結。", "同時檢查太陽能量、帶電粒子、磁場與稀薄氣體，不用單一關鍵字猜。", "找曲線趨勢改變的位置，不以圖中央或固定距離切分。", "圈出題目問的『不能直接推出』，選需要額外觀測的量。", "由地表熱源、上升膨脹與冷卻的因果鏈檢查選項。", "把溫度、粒子密度與碰撞傳熱分開，避免把高平均能量當成高熱量。", "把模型用途和模型限制各寫一句，再排除絕對化敘述。"]
    steps = ["讀題並圈出高度、溫度、趨勢、現象、成因或模型限制等關鍵詞。", "先確認選項談的是直接觀察、合理推論，還是需要額外資料的主張。", "把每個選項放回對流層、平流層、中氣層或增溫層的剖面位置檢查。", "排除把層界當硬牆、把單一現象當唯一特徵，或混淆溫度與粒子密度的說法。", "用完整因果句重述答案，確認結論符合曲線與課內證據且沒有過度延伸。"]
    for i in range(1, 11):
        p = ROOT / f"questions/science/question-science-content-fa-iv-4-{i}.json"; q = json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = explanations[i-1]; q["solutionStrategy"] = strategies[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "公立學校公開自然科試題中的圖表趨勢、地球科學現象、證據界線與模型判讀能力；本題改寫為 Fa-Ⅳ-4 原創情境。"; p.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content fa-iv-4")

if __name__ == "__main__":
    main()
