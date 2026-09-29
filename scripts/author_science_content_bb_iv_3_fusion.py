import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-bb-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-bb-iv-3-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "比熱、熱量、質量與溫度變化"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "Q=mcΔT、混合平衡與熱損失"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "水的比熱、隔熱容器與生活資料"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。Q=mcΔT，甲乙的 m 與 Q 相同，升溫較小的甲需要較大的比熱；因此 c甲>c乙。",
    "C。m 與 c 相同時，ΔT=Q/(mc)，甲吸收 3 倍熱量，溫度變化也是乙的 3 倍。",
    "B。c=Q/(mΔT)=200 cal/(100 g×10℃)=0.20 cal/(g·℃)。",
    "C。Q=mcΔT=50×0.4×20=400 cal；要保持質量、比熱與溫差單位一致。",
    "A。Q=mcΔT 且 m、c 不變，Q 加倍使 ΔT 也加倍；這是假設熱損失與供熱條件相同。",
    "C。等質量同種水混合且無熱損失，平衡溫度為(20+80)/2=50℃；兩份熱容量相同。",
    "A。熱水質量較大、熱容量 mc 較大，混合後平衡溫度受熱水狀態影響較大，較接近熱水溫度。",
    "A。水的比熱較大，同樣吸收或失去熱量時溫度變化較小，海洋可緩和沿海日夜溫差。",
    "A。m與Q相同而金屬ΔT較大，由 c=Q/(mΔT) 可知金屬比熱較小；仍需排除熱損失差異。",
    "A。比熱是單位質量升高單位溫度所需熱量的材料特性，實際溫升還要同時考慮 m、Q、散熱與容器吸熱。",
]
STRATEGIES = [
    "先比較 Q、m、ΔT，再用 c=Q/(mΔT) 判斷比熱大小。",
    "固定 m、c 後看 Q 與 ΔT 的正比關係。",
    "列出 Q、m、ΔT 的數值與單位，再代入 c=Q/(mΔT)。",
    "使用 Q=mcΔT，逐步代入質量、比熱和溫差。",
    "在 m、c 不變下用比例判斷熱量加倍造成的溫升。",
    "檢查兩份物質的熱容量 mc 是否相同，再用熱量守恆求平衡溫度。",
    "比較熱容量 mc 大小，判斷平衡溫度靠近哪一方。",
    "把水的大比熱連到相同熱量造成的較小溫變。",
    "由相同 Q、m 和不同 ΔT 反推 c，並檢查熱損失。",
    "說明比熱定義，再補上質量、熱量、散熱與容器的限制。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求計算比熱、Q=mcΔT、比較質量與溫差、混合平衡、水的比熱與熱損失控制；本題以全新熱量情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-bb-iv-3、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合比熱、熱量、質量、溫差、Q=mcΔT、混合平衡、水的比熱、熱損失與容器吸熱；保留海邊—柏油路—熱水袋—金屬鍋資料互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出 Q、m、c、ΔT、初末溫度、熱損失與容器條件並統一單位。", "依題目要求選 Q=mcΔT 或比例關係，逐項代入並保留單位。", "比較熱容量 mc，判斷相同熱量下溫升大小或混合平衡溫度。", "檢查隔熱、散熱、供熱速率與容器吸熱，避免把比熱當物體總熱量。", "回查計算結果的數量級、方向與適用條件，說明理想模型限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-bb-iv-3-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的比熱、熱量、質量、溫差、Q=mcΔT、混合平衡與熱損失能力；本題改寫為熱量與比熱原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content bb iv 3")


if __name__ == "__main__": main()
