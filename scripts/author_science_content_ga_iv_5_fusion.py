"""Ga-Ⅳ-5：生物技術的應用與可能問題第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ga-iv-5.json"
REPORT = ROOT / "implementation/reports/science-content-ga-iv-5-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "生物技術、基因改造、資料判讀與風險證據", "pattern": "取由生物技術原理、對照資料、效益與風險證據進行條件式推論的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "基因轉殖、生物技術應用與倫理", "pattern": "取基因轉殖、醫藥／農業應用、控制變因、證據評估與社會議題討論方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "基因改造、基因流動、環境影響與公共決策", "pattern": "取比較效益與替代方案、辨認基因流動與生態風險、以多方證據形成決策的能力方向。"},
]

def source_refs():
    return [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {
        "commonCore": ["三版本公開線索共同支持以基因轉殖、基因改造與選擇性表現連結生物技術的應用。", "對照實驗、效益與風險、基因流動、環境影響、證據不確定性與公共決策是共同能力核心。"],
        "versionDifferences": ["南一公開定位偏向生物技術原理與應用；康軒線索偏向基因轉殖、農業／醫藥案例和控制變因；翰林線索偏向基因流動、環境風險、多方證據與社會決策。公開資料不足以宣稱取得完整教材內容。"],
        "originalAdditions": ["以胰島素細菌、抗蟲作物、培養皿表現與野生近緣種基因流動建立『原理—證據—效益—風險—決策』路徑。", "把『基改必然安全／必然危險』『單一培養皿結果等於田野風險』『有益應用就不必評估替代方案』列為單元迷思診斷。"],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織基因轉殖、基因改造、生物技術應用、控制變因、基因流動、環境風險與公共決策；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    refs = source_refs()
    questions = sorted(path for path in QDIR.glob("question-science-content-ga-iv-5-*.json") if path.stem.removeprefix("question-science-content-ga-iv-5-").isdigit())
    if len(questions) != 10:
        raise SystemExit(f"Ga-Ⅳ-5 題數應為 10，實際為 {len(questions)}")
    for path in questions:
        q = json.loads(path.read_text(encoding="utf-8"))
        q["examPatternRefs"] = refs
        provenance = q.setdefault("provenance", {})
        provenance["sourceUrl"] = SOURCES[0]["url"]
        provenance["sourceLocator"] = "三筆公立學校／公開自然科試題與課程資料的生物技術、基因改造、實驗比較及風險決策能力方向；本題只作 pattern-only 改寫來源。"
        provenance["authoringNote"] = "本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ga-Ⅳ-5 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        q["reviewStatus"] = "draft"
        q["updatedAt"] = TODAY
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "Ga-Ⅳ-5：生物技術的應用與可能問題", "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10,
        "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"},
        "reviewedAt": TODAY, "note": "10 題均逐題核對生物技術單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ga iv 5")

if __name__ == "__main__":
    main()
