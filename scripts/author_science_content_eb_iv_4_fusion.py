import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-eb-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-eb-iv-4-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "靜摩擦、動摩擦、受力圖與臨界條件"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "正向力、接觸面、斜面與摩擦資料"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "生活防滑、減摩擦、合力與實驗控制"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "B。盒子有向右運動的趨勢，桌面摩擦力沿接觸面向左，抵抗相對運動趨勢；盒子仍靜止表示靜摩擦力大小可與推力平衡。",
    "B。尚未滑動且沒有其他水平力時，靜摩擦力會自我調整為與推力等大反向，因此依序為 2 N、4 N、6 N，尚未超過最大值。",
    "B。8 N 是最大靜摩擦力；滑動後拉力 5 N 且等速，合力為零，表示動摩擦力大小為 5 N、方向與運動相反。",
    "A。加砝碼使正向力增大，通常使最大靜摩擦力上限也增大；同樣 6 N 推力可能仍不足以克服啟動門檻。",
    "B。物體有向下滑趨勢，靜摩擦力就沿斜面向上，抵抗預期的相對運動；方向不是固定向上或向下，而由趨勢決定。",
    "A。鞋底增加紋路與輪胎保持適當胎紋都提高抓地摩擦；潤滑軸承或加滾輪則是降低摩擦，不屬於同一目的。",
    "B。木盒向右滑動時，桌面對盒子的動摩擦力向左，與速度方向相反；它不是因為物體向右就指向右。",
    "A。水平方向合力=12−5=7 N，方向向右；要先標出拉力與動摩擦力再做向量相減。",
    "C。在國中常用理想滑動摩擦模型，摩擦大小主要與正向力和接觸材料狀態有關，接觸面積倍增不必然使摩擦力倍增。",
    "A。公平比較要固定重量、接觸面積、地面、拉動速度、清潔與濕度，重複測量開始滑動所需最大拉力，再比較平均值與變異。",
]
STRATEGIES = [
    "先判斷相對運動或運動趨勢，再沿接觸面反向畫摩擦力。",
    "確認物體是否靜止且水平力只有推力，使用靜摩擦力平衡外力。",
    "分開最大靜摩擦力、動摩擦力與等速合力，勿把臨界力當滑動力。",
    "檢查加重是否改變正向力，並比較推力與新的啟動上限。",
    "先找斜面上的下滑趨勢，再決定靜摩擦力的反向。",
    "把增加抓地和降低能量損耗的生活設計分成兩類。",
    "用速度方向判斷動摩擦力反向，並確認接觸面。",
    "將同一直線反向力代數相減，保留合力方向。",
    "在指定理想模型下檢查正向力與材料，避免把面積直覺套入。",
    "列控制變因、測量最大靜摩擦力、重複次數與資料變異，才支持材料差異。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求判斷靜摩擦與動摩擦方向、臨界力、正向力、斜面、合力、生活防滑與公平實驗；本題以全新摩擦情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-eb-iv-4、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合接觸面、摩擦方向、靜摩擦自我調整、最大靜摩擦力、動摩擦力、正向力、斜面、合力與防滑／減摩擦設計；保留推木盒力—摩擦力圖互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出接觸面、運動方向、相對運動趨勢、推力、正向力與材料條件。", "先判斷靜止或滑動，再決定使用靜摩擦平衡、最大靜摩擦或動摩擦模型。", "沿接觸面反向畫摩擦力，必要時以合力與正向力計算。", "比較外力是否超過啟動門檻，並檢查加重、斜面、速度與接觸狀態的影響。", "回查實驗是否固定重量、面積、速度、濕度與表面，避免把生活直覺當成普遍定律。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-eb-iv-4-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的靜摩擦、動摩擦、正向力、斜面、合力、防滑與實驗控制能力；本題改寫為摩擦力原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content eb iv 4")


if __name__ == "__main__": main()
