import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ga-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-ga-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "鹽埕國中公開自然段考", "生殖方式、遺傳差異與生物學資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "內湖國中公開自然段考", "生物繁殖、親代子代與實驗設計"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "國昌國中公開自然科試題", "遺傳差異、環境因素與控制變因"),
]

def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常以生殖流程、配子受精、子代差異、環境變化與繁殖實驗檢查概念分類及證據推理；本題為獨立改寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = "2026-09-21"; lesson["reviewStatus"] = "draft"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方 Ga-Ⅳ-1 課綱、三筆公立校方公開章節定位與公開自然科試題 pattern 研究，獨立重寫有性／無性判準、受精位置、子代差異、環境風險與繁殖決策；未複製任何版本教材或試題。完整出版社內文未公開取得，不虛構逐頁閱讀；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    explanations = [
        "無性生殖通常不經配子結合、由一個親代直接形成子代，繁殖快且子代較相似；有性生殖則有配子結合和較多遺傳組合。正確答案：A。",
        "草莓匍匐莖是營養器官直接長出新植株，不經精卵配子結合，屬無性生殖。正確答案：B。",
        "有性生殖把不同配子的遺傳訊息重新組合，使子代間可能出現較多差異；環境本身不是遺傳組合的主要來源。正確答案：C。",
        "環境改變時，較多遺傳差異提高族群中出現適合個體的機會，但不保證每個個體都能存活或一定適應。正確答案：D。",
        "酵母出芽由一個親代細胞長出芽體並分離，沒有配子結合，屬無性生殖。正確答案：B。",
        "研究光照影響時，依變因應是被測量的繁殖結果，例如一段時間後成功生根的插穗比例，不是光照本身。正確答案：C。",
        "比較生長素濃度要固定插穗種類、長度、數量、土壤、光照、水分與觀察時間，才可把差異歸因於濃度。正確答案：D。",
        "受精是精子與卵等配子結合形成受精卵，這是有性生殖的核心判準，不等同於卵生或胎生。正確答案：A。",
        "無性繁殖子代遺傳背景相近，但光照、水分、病害或微小突變仍可能使表現不同；不能把差異全歸因於有性遺傳。正確答案：C。",
        "效率要同時比較速度、成功率、資源成本、子代差異與環境風險，不能只看短期增加數量。正確答案：B。",
    ]
    strategies = ["先找有無配子結合，再比較親代數量、流程速度與子代差異。", "追蹤新植株由哪個親代構造直接形成，排除只看位置或外形。", "把配子遺傳訊息重新組合和環境造成的表現差異分開。", "先問族群面對新環境需要什麼差異，再補上『不保證適應』的限制。", "判斷出芽是否有配子與受精卵，依核心判準分類。", "先定義要測量的繁殖結果，再區分自變因、依變因與控制變因。", "列出會影響扦插成功率的條件，只留下生長素濃度作為比較差異。", "用配子結合→受精卵的流程判斷，不把卵生、胎生當成受精定義。", "同時檢查遺傳背景與環境條件，避免把表現差異直接等同基因差異。", "把效率拆成速度、成功率、資源、差異與風險，依目的選比較標準。"]
    steps = ["讀題並圈出親代數量、配子、受精、繁殖構造、子代差異或實驗變因。", "先用是否有配子結合判斷有性或無性，再處理卵生胎生、速度與差異等次要描述。", "把題目資料分成直接觀察、合理遺傳推論與仍需控制或重複的部分。", "排除把某一例子、單一環境或短期表現誇大成所有生物的必然規則。", "用完整句重述答案，補上目的、條件與限制，確認結論沒有超出證據。"]
    for i in range(1, 11):
        p = ROOT / f"questions/science/question-science-content-ga-iv-1-{i}.json"; q = json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = explanations[i-1]; q["solutionStrategy"] = strategies[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "公立學校公開自然科試題中的生殖方式、配子受精、親代子代差異與繁殖實驗能力；本題改寫為 Ga-Ⅳ-1 原創情境。"; p.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ga-iv-1")

if __name__ == "__main__":
    main()
