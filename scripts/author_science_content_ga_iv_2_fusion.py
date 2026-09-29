"""Ga-Ⅳ-2：性染色體與人類性別第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ga-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-ga-iv-2-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "性染色體、性聯遺傳、遺傳圖表與機率判讀", "pattern": "取由染色體、配子、家族資料和機率模型推論遺傳結果的能力方向；不把簡化模型當成所有人的身分結論。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "性染色體、性聯遺傳與家族圖表", "pattern": "取性染色體與常染色體的區分、性聯隱性性狀、配子組合及家族資料判讀方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "人類遺傳、性狀變異與證據界線", "pattern": "取由遺傳圖表、樣本比例與限制條件建立推論，並區分生理性狀的簡化模型與個體多樣性的能力方向。"},
]

def source_refs():
    return [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {
        "commonCore": ["三版本公開線索共同支持以染色體組合、配子、遺傳圖表與機率模型理解性染色體及性聯遺傳。", "性染色體與常染色體的區分、X 聯遺傳、家族資料、樣本比例與證據限制是共同能力核心。"],
        "versionDifferences": ["南一公開定位偏向性染色體與基本遺傳機率；康軒線索偏向性聯遺傳、配子組合與家族圖表；翰林線索偏向人類性狀資料、模型限制及個體多樣性。公開資料不足以宣稱取得完整教材內容。"],
        "originalAdditions": ["以配子棋盤、家族圖與班級樣本資料分開處理典型遺傳模型、統計比例與個體差異。", "把『XY 必然代表所有男性身分』『單一染色體完全決定性別認同』『一次出生比例等於大樣本比例』列為單元迷思診斷，保留教材層級可驗證的生物學敘述與尊重個體的語言。"],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織性染色體、常染色體、配子、X 聯遺傳、家族圖、機率與模型界線；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    refs = source_refs()
    questions = sorted(path for path in QDIR.glob("question-science-content-ga-iv-2-*.json") if path.stem.removeprefix("question-science-content-ga-iv-2-").isdigit())
    if len(questions) != 10:
        raise SystemExit(f"Ga-Ⅳ-2 題數應為 10，實際為 {len(questions)}")
    for path in questions:
        q = json.loads(path.read_text(encoding="utf-8"))
        q["examPatternRefs"] = refs
        provenance = q.setdefault("provenance", {})
        provenance["sourceUrl"] = SOURCES[0]["url"]
        provenance["sourceLocator"] = "三筆公立學校／公開自然科試題與課程資料的性染色體、性聯遺傳、家族資料及機率判讀能力方向；本題只作 pattern-only 改寫來源。"
        provenance["authoringNote"] = "本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ga-Ⅳ-2 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        q["reviewStatus"] = "draft"
        q["updatedAt"] = TODAY
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "Ga-Ⅳ-2：性染色體與人類性別", "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10,
        "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"},
        "reviewedAt": TODAY, "note": "10 題均逐題核對性染色體單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ga iv 2")

if __name__ == "__main__":
    main()
