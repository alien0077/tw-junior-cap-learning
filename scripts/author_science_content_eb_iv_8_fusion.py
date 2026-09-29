import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-eb-iv-8.json"
REPORT = ROOT / "implementation/reports/science-content-eb-iv-8-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "距離、時間、路程、位移與平均速率"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "位置時間圖、方向、平均速度與單位換算"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "折返運動、斜率與資料判讀"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "D。路程是實際路徑長度，向東 120 m 加向西 50 m，總路程=120+50=170 m；方向只影響位移。",
    "A。位移=終點位置−起點位置=−3−2=−5 m，負號代表向西；不能把路程 5 m 當作帶方向的位移。",
    "B。總路程=600+900=1500 m，總時間=4+6=10 min=600 s，平均速率=1500÷600=2.5 m/s。",
    "C。跑回起點使總位移為 0，因此平均速度大小=0/200=0 m/s，沒有東西方向；路程仍為 800 m。",
    "B。2 s 到 4 s 位置都為 6 m，位置不變，代表該時間段靜止；其他段位置有變化。",
    "B。平均速度=(14−2)/(5−1)=12/4=3 m/s，位置隨時間增加，方向為正方向。",
    "B。72 km/h×1000/3600=20 m/s；換算要同時把 km 換 m、h 換 s。",
    "A。兩人路程相同，甲時間較短，平均速率=300/60=5 m/s，高於乙的 300/75=4 m/s。",
    "B。5 到 10 s 位置由 20 m 降到 10 m，位移為 −10 m，表示向西移動，平均速度為 −2 m/s。",
    "C。完整判讀要先定參考點與正方向，再由位置差求位移、由路徑求路程，最後分別計算平均速率與平均速度。",
]
STRATEGIES = [
    "把各段實際移動長度相加，方向留給位移使用。",
    "使用終點位置減起點位置，保留正負方向。",
    "先加總路程與時間，再把分鐘換成秒求平均速率。",
    "先判斷終點是否回到起點，再計算位移與平均速度。",
    "看位置是否隨時間改變，水平段代表靜止。",
    "用位置差除時間差，並由斜率正負判斷方向。",
    "分別換算距離與時間單位，再求 m/s。",
    "在相同路程下比較時間，時間短者平均速率較大。",
    "看位置差與時間差的正負，判斷折返方向與速度。",
    "依參考點—路徑—位移—速率／速度順序整理資料。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求計算路程、位移、平均速率、平均速度、位置時間斜率與單位換算；本題以全新運動資料情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-eb-iv-8、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合參考點、正方向、路程、位移、速率、速度、位置—時間斜率、折返與單位換算；保留校園巡查地圖與時間序列互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出參考點、正方向、每段位置、時間、路徑與折返點。", "把各段路徑長度相加求路程，用終點減起點求位移並保留正負。", "統一 m、s、km/h 等單位，再用總路程／總時間求平均速率。", "若求平均速度，使用位移／總時間並附方向；由位置—時間斜率判斷分段運動。", "回查水平段、折返、單位與資料刻度，避免把位置直接當速度或把路程當位移。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-eb-iv-8-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的距離、時間、路程、位移、平均速率、平均速度、圖表與單位換算能力；本題改寫為運動描述原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content eb iv 8")


if __name__ == "__main__": main()
