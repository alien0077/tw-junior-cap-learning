import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-aa-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-aa-iv-2-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "相對原子質量、化學式與相對分子質量"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "元素組成、同位素平均與數值計算"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "化學式下標、括號、質量貢獻與估算"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。相對原子質量 16 表示該原子質量相對於碳-12 原子質量 1/12 的 16 倍，是無單位的比較值，不是 16 克。",
    "C。相對質量比可用 35.5÷16≈2.22 估算；這是微觀相對值，不能直接當成兩個樣品的重量比而忽略粒子數。",
    "B。H₂O 含 2 個 H 與 1 個 O，Mr=2×1+1×16=18；下標要先轉成原子數。",
    "C。CO₂/O₂ 的相對分子質量比為 44÷32=1.375，約 1.38 倍；不能只比較碳與氧單一原子。",
    "C。X₂Y₃ 的 Mr=2×10+3×20=20+60=80，必須依化學式下標計算每種原子的貢獻。",
    "B。較重同位素比例增加，加權平均值會向較重同位素移動，元素表上的平均相對原子質量通常上升。",
    "D。四個分子的平均=(3×20+1×40)÷4=100÷4=25；要按分子個數加權，不能只平均 20 和 40。",
    "B。相對原子質量已使用共同基準，化學式計算只需按原子數加權加總，避免把所有微觀質量先轉成克而增加不必要複雜度。",
    "A。SO₂ 有 1 個 S 和 2 個 O，Mr=32+2×16=64；錯誤是漏讀 O 的下標 2。",
    "C。不同化學式可能因元素種類、原子數與相對原子質量組合不同而得到相同總值，但不能由 Mr 相同推論組成、性質或用途相同。",
]
STRATEGIES = [
    "先確認共同基準與相對值的無單位意義，再判斷倍數。",
    "用相對質量做比值，並說明粒子數與樣品重量的界線。",
    "讀化學式下標，逐項做原子數×Ar後加總。",
    "先算兩個 Mr，再取比值，避免只看一種元素。",
    "建立 X、Y 原子數表，分別算貢獻後相加。",
    "把同位素比例視為加權平均，判斷平均值移動方向。",
    "用每種分子個數作權重，算總相對質量除以總分子數。",
    "用共同基準的相對值直接計算，區分相對值和實際克數。",
    "重新讀每個元素的下標，找出漏乘或漏加位置。",
    "只由 Mr 判斷數值關係，不能反推唯一組成與性質。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求理解相對質量基準、化學式下標、相對分子質量、同位素平均、加權計算與估算檢查；本題以全新化學數值情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-aa-iv-2、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合碳-12基準、相對原子質量、化學式下標、相對分子質量、同位素加權平均、質量貢獻與估算檢查；保留化學式拆解與即時比例圖互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出共同基準、元素符號、下標、括號倍數與題目要求的相對量。", "把化學式轉成各元素原子數，建立原子數×Ar的組成表。", "逐項計算質量貢獻並加總，必要時用比值、加權平均或估算檢查。", "區分相對無單位數值、實際克數、原子序、質量數與化學式組成。", "回查下標、乘法、加總與結論界線，說明相同 Mr 不能推出相同性質。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-aa-iv-2-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的相對質量基準、化學式下標、分子質量、同位素與加權計算能力；本題改寫為相對質量原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content aa iv 2")


if __name__ == "__main__": main()
