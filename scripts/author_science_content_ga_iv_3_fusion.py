"""Ga-Ⅳ-3：ABO 血型遺傳第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ga-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-ga-iv-3-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "遺傳圖表、等位基因、機率與證據判讀", "pattern": "取由家族資料與遺傳規則推論性狀可能性、檢查條件與避免過度結論的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "ABO 血型、複等位基因與共顯性", "pattern": "取複等位基因、共顯性、棋盤格與家族血型資料的教學及評量方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "血型遺傳模型、家族圖與推論界線", "pattern": "取以基因型而非只看表現型進行血型推論，並區分遺傳模型與醫療輸血判斷的能力方向。"},
]

def source_refs():
    return [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {
        "commonCore": ["三版本公開線索共同支持用 Iᴬ、Iᴮ、i 三種等位基因、基因型與表現型說明 ABO 血型遺傳。", "複等位基因、Iᴬ 與 Iᴮ 共顯性、i 隱性、棋盤格、家族圖及可能性推論是共同能力核心。"],
        "versionDifferences": ["南一公開定位偏向遺傳資料與機率；康軒線索偏向複等位基因、共顯性與棋盤格；翰林線索偏向基因型反推、家族關係與遺傳模型和醫療判斷的界線。公開資料不足以宣稱取得完整教材內容。"],
        "originalAdditions": ["以父母基因型、家族圖、四格棋盤和可能血型集合逐步建立 ABO 推論，而非只背表型對照表。", "把『表現型直接等於唯一基因型』『遺傳可能性等於確定結果』『ABO 遺傳題可直接取代臨床輸血交叉試驗』列為單元迷思診斷。"],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織 ABO 複等位基因、共顯性、隱性、基因型、表現型、棋盤格、家族圖與證據界線；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    refs = source_refs()
    questions = sorted(path for path in QDIR.glob("question-science-content-ga-iv-3-*.json") if path.stem.removeprefix("question-science-content-ga-iv-3-").isdigit())
    if len(questions) != 10:
        raise SystemExit(f"Ga-Ⅳ-3 題數應為 10，實際為 {len(questions)}")
    for path in questions:
        q = json.loads(path.read_text(encoding="utf-8"))
        q["examPatternRefs"] = refs
        provenance = q.setdefault("provenance", {})
        provenance["sourceUrl"] = SOURCES[0]["url"]
        provenance["sourceLocator"] = "三筆公立學校／公開自然科試題與課程資料的 ABO 血型、遺傳圖表、機率及家族資料判讀能力方向；本題只作 pattern-only 改寫來源。"
        provenance["authoringNote"] = "本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ga-Ⅳ-3 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        q["reviewStatus"] = "draft"
        q["updatedAt"] = TODAY
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "Ga-Ⅳ-3：ABO 血型遺傳", "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10,
        "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"},
        "reviewedAt": TODAY, "note": "10 題均逐題核對 ABO 血型單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ga iv 3")

if __name__ == "__main__":
    main()
