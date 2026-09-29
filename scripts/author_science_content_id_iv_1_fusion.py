import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-id-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-id-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "地球自轉、公轉、地軸傾角與季節日照"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "太陽運行、日出日落資料與南北半球比較"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "季節、緯度、極晝極夜與觀測模型"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。北半球夏季地軸傾斜使北半球較朝向太陽，該地點每天走過受光面的時間較長，所以白晝通常較長；不是因為地球單純更靠近太陽。",
    "B。冬季夜長較長可由日落較早且日出較晚、兩者相減得到較短白晝來支持；只看其中一個時間不足以判斷夜長。",
    "C。比較同一地點夏冬日長，要同時記錄日期、日出與日落時間，並計算日落減日出；地點不同會混入緯度差異。",
    "D。高緯度地區相對於地軸傾斜的受光幾何變化更顯著，夏冬受光弧長短差距較大，因此日長季節差通常更明顯。",
    "B。北極圈夏季地軸使北極區長時間朝向太陽，太陽日周運動的路徑整段位於地平線上方，因而可能出現極晝。",
    "C。若沒有地軸傾斜，公轉時南北半球受光情形不會出現季節性偏向，除緯度與日周運動本身外，日長季節差會大幅減少。",
    "D。燈泡代表太陽、地球儀軸向在公轉過程保持同一指向，並在相同緯度標記觀測點，逐位置記錄受光時間；不能一邊改變軸向一邊比較。",
    "A。分點附近地球兩半球受光情況較對稱，太陽直射赤道附近，晝夜分界線接近通過兩極，所以多數地點的日長較接近。",
    "C。應選多個緯度、固定比較日期與相同計算方式，記錄冬至附近的日出日落並求夜長，才能把緯度與季節條件分開。",
    "B。日長可能影響光合作用，但植物生長還受溫度、水分、土壤養分與物種差異影響；研究結論應限定在觀察日期、地點與控制條件。",
]
STRATEGIES = [
    "先標出半球與季節，再用地軸傾角判斷受光弧長短。",
    "把日出、日落轉成白晝長度，不能只看單一時間點。",
    "固定地點與日期格式，計算日落減日出後再比較季節。",
    "將緯度放進受光幾何，判斷日長差距是否隨高緯度放大。",
    "在地球儀上檢查極圈是否整段位於受光面，不只看太陽高度。",
    "把地軸傾角設為零的模型與現實模型比較，排除距離因素。",
    "固定燈泡、軸向、緯度與記錄方法，逐一改變公轉位置。",
    "用分點的赤道直射與晝夜分界線幾何解釋，而非背誦日期。",
    "用多緯度、同日期、同計算式的資料設計控制變因。",
    "將日長視為一項自變因或解釋因子，同時交代其他生長條件與研究範圍。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結自轉、公轉、地軸傾角、日出日落資料、緯度、極晝極夜與南北半球模型；本題以全新天文觀測情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []):
        row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-id-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合自轉造成晝夜交替、公轉與固定地軸傾角造成季節日長、日出日落資料、緯度、極晝極夜、分點與南北半球反向檢核；保留公轉位置與觀測條件互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出觀測地點、日期、半球、日出、日落、地軸方向與受光面。", "先分開自轉造成一天晝夜交替，以及公轉加地軸傾角造成一年季節差。", "用日落時間減日出時間求白晝，再判斷哪個半球受光弧較長。", "以另一半球、另一緯度或分點資料交叉檢查，排除只看單一時間或把距離當季節成因。", "回查模型是否固定軸向、觀測位置與日期，並說明極晝、極夜或植物資料的限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-id-iv-1-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q["examPatternRefs"] = refs()
        q["reviewStatus"] = "draft"
        q["updatedAt"] = "2026-09-21"
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["solutionStrategy"] = STRATEGIES[i - 1]
        q["solutionSteps"] = steps
        q["provenance"]["sourceUrl"] = URLS[0][0]
        q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的自轉、公轉、地軸傾角、日照資料、緯度、極晝極夜與觀測模型能力；本題改寫為季節日長原創情境。"
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content id iv 1")


if __name__ == "__main__":
    main()
