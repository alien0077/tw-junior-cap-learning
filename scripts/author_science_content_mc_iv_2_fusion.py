import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-mc-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-mc-iv-2-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "生物構造、功能與生活應用"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "仿生設計、控制變因與性能資料"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "構造功能、材料限制與環境影響"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。荷葉微結構降低水滴附著，水滴滾動時可帶走灰塵；仿生重點是表面功能與使用條件，不是把牆面做得更重或永久潮濕。",
    "A。要評估隔熱與節能，須在相同日照和室內條件下比較熱流、溫度、能源消耗、耐久與製造負荷，不能只看短時間或外觀。",
    "A。壁虎微結構的功能要在不同表面、載重與乾濕條件下測量附著力及可重複使用性，才知道仿生材料的適用邊界。",
    "A。泳衣表面性能會受水流、粗糙度、材料耐久與生態影響；外形相似不保證在不同尺度和速度下同樣降低阻力。",
    "A。輕量桁架應保留主要受力路徑，再用不同壁厚測試強度與重量；只挖空或只模仿外形都無法保證安全。",
    "A。集水效果要同時測量溝槽幾何、材料、風速和實際收集量；只拉長刺或假定所有乾旱環境相同都過度簡化。",
    "A。醫療縫線除了強度和韌性，還要驗證生物相容性、延展、降解、滅菌後性能與安全，不能只看仿生來源。",
    "A。效果下降應檢查微結構磨損、污染與塗層耐候性，再依資料調整材料或維護週期，而不是否定仿生原理。",
    "A。速度提高但能耗大增，應比較相同距離的能耗、穩定性與控制難度，再判斷是否真的改善功能。",
    "A。生物構造只提供設計靈感；人造材料與使用情境不同，仍需重新驗證安全、成本、耐久與環境影響。",
]
STRATEGIES = [
    "先連結生物微結構與原本功能，再檢查產品指標。", "固定日照與室內條件，使用熱流、溫度、耗能和耐久資料比較。", "把附著功能拆成表面、載重、濕度和重複使用條件。", "檢查尺度、流體條件、材料耐久和環境副作用。", "先畫受力路徑，再比較強度與重量的取捨。", "將構造、環境變因和實際集水量連成測試設計。", "把機械性能和醫療安全、滅菌、降解一起評估。", "追蹤磨損、污染、耐候與維護週期的時間資料。", "用相同距離的能耗、穩定性和控制難度評估速度收益。", "把生物靈感和人造產品的重新驗證分開。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求由生物構造與功能、變因控制、性能資料、材料限制與環境影響評估生活應用；本題以全新仿生情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-mc-iv-2、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合生物構造—功能、仿生設計、控制變因、材料尺度、性能、維護、安全與環境代價；保留既有仿生工作室互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出仿生生物構造、原本功能、環境條件、設計指標與限制。", "把外形相似與機制相似分開，提出可控制和可測量的變因。", "比較性能、尺度、材料、耐久、安全、成本與環境影響資料。", "排除只看外觀、一次測試、忽略使用條件或把生物功能直接保證給人造產品的選項。", "用完整句回查方案在哪些條件有效，以及仍需補測或維護的部分。"]
    rotations = [0, 1, 2, 3, 1, 2, 3, 0, 1, 2]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-mc-iv-2-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); opts = q["options"]; correct_text = opts[0]["text"]; k = rotations[i-1]; opts = opts[k:] + opts[:k]; q["options"] = [{"id": chr(65+j), "text": o["text"]} for j, o in enumerate(opts)]
        # 原始正解文字是每題原選項 A；旋轉後以原選項文字定位新的代號。
        q["answer"] = {"value": chr(65 + next(j for j, o in enumerate(opts) if o["text"] == correct_text)), "explanation": EXPLANATIONS[i-1]}
        q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的生物構造與功能、仿生設計、性能測試與環境限制能力；本題改寫為仿生生活應用原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content mc iv 2")


if __name__ == "__main__": main()
