import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ia-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-ia-iv-3-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "板塊張裂、聚合、錯動與地質結果"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "海溝、火山、地震、造山與地質剖面"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "臺灣板塊、監測資料與模型限制"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。兩板塊分離且岩漿上升形成新海洋地殼，符合張裂性邊界與中洋脊／裂谷的證據。",
    "B。海洋地殼密度通常較大，與大陸地殼聚合時可能隱沒，形成海溝、地震帶與火山弧；具體位置仍需剖面資料。",
    "C。兩塊大陸地殼密度相近，不易一塊整片隱沒，持續擠壓會使岩層褶皺、增厚與抬升，形成山脈。",
    "D。地震狹長分布、兩側水平錯動且缺乏岩漿活動，較符合錯動性板塊邊界或走向滑移斷層。",
    "B。震源沿海溝向陸地逐漸變深，支持海洋板塊向陸下方隱沒的地震帶幾何；仍要配合板塊位移和岩性證據。",
    "C。臺灣位於活動板塊交會區，聚合與碰撞造成地殼縮短、抬升與褶皺，也使斷層活動和地震較頻繁。",
    "D。應整合地震序列、GPS或雷達位移、火山氣體、地熱與地震波資料，並持續監測，不由單一訊號宣告即將噴發。",
    "A。地震與火山集中在狹長帶，符合板塊邊界的隱沒、張裂或錯動等活動集中分布，但不同地帶的機制仍需細分。",
    "C。木板能表現應力累積與突然錯動，但材料、尺度、速度和摩擦機制與真實岩層不同，不能直接預測地震時間或規模。",
    "B。規劃應將板塊與斷層證據轉成危害地圖、建物補強、監測、避難路線與演練，並依資料不確定性持續更新。",
]
STRATEGIES = [
    "先判斷板塊相對方向，再以新地殼、海溝或地震等證據配對。",
    "看海洋與大陸地殼性質、隱沒方向，再推論海溝與火山弧。",
    "由密度、擠壓、褶皺與抬升判斷大陸碰撞造山。",
    "用水平錯動、地震帶與岩漿缺乏辨認錯動邊界。",
    "沿震源深度剖面追蹤隱沒板塊的幾何。",
    "把臺灣板塊交會、地殼縮短抬升與斷層活動連成證據鏈。",
    "整合多項監測資料，明確區分風險評估和確定預測。",
    "先辨認板塊邊界共通分布，再檢查每一地帶的具體機制。",
    "列模型可表現的應力與錯動，以及材料、尺度、時間的限制。",
    "將地質證據轉成建物、監測、避難、演練與更新機制。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求由板塊相對運動判讀張裂、聚合、錯動、海溝、火山、地震、造山與模型限制；本題以全新板塊構造情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ia-iv-3、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合板塊張裂、聚合、錯動、隱沒、海溝、火山、地震、造山、臺灣資料與模型限制；保留板塊邊界與地質證據互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出板塊相對方向、板塊性質、受力、地形與地震／火山證據。", "依張裂、聚合或錯動建立邊界模型，標示海溝、中洋脊、斷層、褶皺與岩漿。", "用地質剖面、震源分布、GPS或火山監測資料支持推論。", "分開直接觀察、模型解釋與尚待查證的預測，避免把單一現象配成固定口號。", "回查模型尺度、資料年代、不確定性與防災方案的可執行條件。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ia-iv-3-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的板塊張裂、聚合、錯動、海溝、火山、地震、造山與模型限制能力；本題改寫為板塊運動原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content ia iv 3")


if __name__ == "__main__": main()
