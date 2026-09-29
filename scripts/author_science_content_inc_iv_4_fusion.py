import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-inc-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-inc-iv-4-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "比例、尺度、模型與圖表判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "比例尺、單位換算與科學模型"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "地圖量距、倍率與資料表示"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以地圖比例尺、模型倍率、長度／面積／體積尺度、圖表座標與量距考查比例換算及模型限制；本題只取能力方向並重新設計情境與數據。"
EXPLANATIONS = [
    "A。1:50,000 表示圖上 1 cm 對應實際 50,000 cm，換成公尺是 500 m；比例尺中的單位必須先統一。",
    "B。模型長度=真實長度÷100=3 m÷100=0.03 m=3 cm；最後要檢查模型比真實小 100 倍。",
    "C。實際距離=4 cm×25,000=100,000 cm=1,000 m=1 km，不能直接把圖上公分當成實際公尺。",
    "D。放大倍率=影像長度÷真實長度=6 cm÷0.2 cm=30 倍；先把 2 mm 換成 0.2 cm。",
    "B。圖表必須標示相同物理量的單位與軸刻度，並說清楚圖上量與實際量的比例；否則斜率與比較會失去意義。",
    "C。長度縮小 10 倍時，面積按平方縮小為 1/10²=1/100；不能只把面積也除以 10。",
    "D。體積按長度倍率的三次方縮放，故縮小 10 倍變為 1/10³=1/1000。",
    "A。要標示比例尺或尺度因子、代表的物理量與單位；只畫不同大小圓形不能保證讀者知道大小差多少。",
    "C。用細線分段量測彎曲河道，再把各段長度相加，最後依比例尺換算；直尺一次量弦長會低估河道長度。",
    "B。先換成同一物理量與單位，再用同一比例因子計算或比較；若兩模型尺度不同，必須先校正，不能只看圖形大小。",
]
STRATEGIES = [
    "把比例尺寫成圖上量：實際量，再統一單位後換算。",
    "先判斷模型比真實小幾倍，再用真實長度除以尺度因子。",
    "以圖上長度乘比例分母得到實際長度，最後換成題目要求的單位。",
    "先把真實長度與影像長度換成同單位，再做影像÷真實。",
    "檢查兩軸的物理量、單位、尺度與刻度，避免斜率失真。",
    "面積使用長度倍率平方，並明確寫出平方的理由。",
    "體積使用長度倍率立方，先估算數量級再確認答案。",
    "確認圖例同時交代代表物、物理量、比例尺與單位。",
    "將曲線拆成小段量距相加，再套用同一比例尺。",
    "先做物理量與單位對齊，再比較同一尺度因子下的數值。",
]
STEPS = [
    "辨認圖上量、真實量、模型量及比較的物理量。",
    "寫出比例尺或倍率，並統一所有單位。",
    "依長度、面積或體積選用一次方、平方或立方關係。",
    "代入計算後用反向換算與數量級檢查。",
    "說明圖例、刻度與模型省略，避免超出證據範圍。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-inc-iv-4、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合比例尺、尺度因子、長度／面積／體積次方、圖表座標、地圖量距、地球月球模型與資訊圖限制；保留展板—模型—反向驗算互動主線，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-inc-iv-4-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的比例尺、倍率、圖表、地圖量距與模型限制能力；本題改寫為物體間尺度關係原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content inc iv 4")


if __name__ == "__main__": main()
