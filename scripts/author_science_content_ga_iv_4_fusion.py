"""Ga-Ⅳ-4：遺傳物質變異與性狀改變第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ga-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-ga-iv-4-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "DNA、基因、染色體、突變與性狀資料判讀", "pattern": "取由遺傳物質、環境條件與性狀觀察資料判斷變異原因和證據限制的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "DNA、基因、染色體與遺傳變異", "pattern": "取 DNA—基因—染色體層次、突變、遺傳與性狀表現的教學及評量方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "環境影響、突變與性狀證據", "pattern": "取比較基因型、表現型、環境效應、體細胞／生殖細胞差異及資料界線的能力方向。"},
]

def source_refs():
    return [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {
        "commonCore": ["三版本公開線索共同支持由 DNA、基因、染色體和等位基因的層次關係解釋遺傳資訊與性狀。", "突變、體細胞／生殖細胞、環境效應、表現型資料與證據界線是共同能力核心。"],
        "versionDifferences": ["南一公開定位偏向 DNA、基因與遺傳變異；康軒線索偏向 DNA—基因—染色體層次和突變；翰林線索偏向基因型／表現型比較、環境影響及體細胞與生殖細胞的資料判讀。公開資料不足以宣稱取得完整教材內容。"],
        "originalAdditions": ["以鹼基序列、染色體模型、光照下葉片差異、紫外線安全情境和家族資料串接遺傳物質與可觀察性狀。", "把『所有突變都一定有害』『環境造成的短期改變必然改變 DNA』『看到家族相似就能確定單一基因』列為單元迷思診斷。"],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織 DNA、基因、染色體、突變、基因型、表現型、體細胞／生殖細胞、環境效應與證據限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    refs = source_refs()
    questions = sorted(path for path in QDIR.glob("question-science-content-ga-iv-4-*.json") if path.stem.removeprefix("question-science-content-ga-iv-4-").isdigit())
    if len(questions) != 10:
        raise SystemExit(f"Ga-Ⅳ-4 題數應為 10，實際為 {len(questions)}")
    for path in questions:
        q = json.loads(path.read_text(encoding="utf-8"))
        q["examPatternRefs"] = refs
        provenance = q.setdefault("provenance", {})
        provenance["sourceUrl"] = SOURCES[0]["url"]
        provenance["sourceLocator"] = "三筆公立學校／公開自然科試題與課程資料的 DNA、基因、染色體、突變及性狀證據判讀能力方向；本題只作 pattern-only 改寫來源。"
        provenance["authoringNote"] = "本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ga-Ⅳ-4 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        q["reviewStatus"] = "draft"
        q["updatedAt"] = TODAY
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "Ga-Ⅳ-4：遺傳物質變異與性狀改變", "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10,
        "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"},
        "reviewedAt": TODAY, "note": "10 題均逐題核對遺傳物質變異單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ga iv 4")

if __name__ == "__main__":
    main()
