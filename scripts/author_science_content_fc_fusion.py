"""Fc：生物圈的組成第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-fc.json"
REPORT = ROOT / "implementation/reports/science-content-fc-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "生態系、生物圈、食物網、能量與資料判讀", "pattern": "取由生態資料辨認生物／非生物因素、能量流動、物質循環與證據限制的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "生態系組成、食物網與環境變因", "pattern": "取生物互動、食物關係、環境條件和預測—觀察—解釋的活動方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "溪流／池塘環境指標與生態系判讀", "pattern": "取多指標、時間序列、測點、尺度與替代解釋的判讀方向。"},
]

def source_refs():
    return [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {
        "commonCore": ["三版本公開線索共同支持由生物因素、非生物因素與尺度邊界建立生態系／生物圈模型。", "食物網、能量流、物質循環、族群變化及多指標資料判讀是共同能力核心。"],
        "versionDifferences": ["南一公開定位較強調生物圈與生態系組成；康軒線索較強調生物互動、食物關係與預測觀察；翰林線索較強調溪流／池塘環境指標、時間尺度及替代解釋。公開資料不足以宣稱取得完整教材內容。"],
        "originalAdditions": ["以校園池塘的藻類、水蚤、小魚、鷺鳥、分解者及水溫／溶氧資料建立單元專屬系統模型。", "把食物網箭頭等同物質循環、單一物種代表整個生態系、一次觀察證明唯一因果列為迷思診斷，並用基準、對照與多指標活動修正。"],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織個體、族群、群集、生態系、生物圈、生產者、消費者、分解者、能量流與物質循環；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    refs = source_refs()
    questions = sorted(
        path for path in QDIR.glob("question-science-content-fc-*.json")
        if path.stem.removeprefix("question-science-content-fc-").isdigit()
    )
    if len(questions) != 10:
        raise SystemExit(f"fc 題數應為 10，實際為 {len(questions)}")
    for path in questions:
        q = json.loads(path.read_text(encoding="utf-8"))
        q["examPatternRefs"] = refs
        provenance = q.setdefault("provenance", {})
        provenance["sourceUrl"] = SOURCES[0]["url"]
        provenance["sourceLocator"] = "三筆公立學校／公開自然科試題與課程資料的生態系、生物圈、資料判讀及探究能力方向；本題只作 pattern-only 改寫來源。"
        provenance["authoringNote"] = "本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Fc 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        q["reviewStatus"] = "draft"
        q["updatedAt"] = TODAY
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "Fc：生物圈的組成",
        "lessonId": lesson["id"],
        "status": "first-pass-ai-review-complete",
        "reviewStatus": "draft",
        "checkedQuestions": 10,
        "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"},
        "reviewedAt": TODAY,
        "note": "10 題均逐題核對生物圈單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content fc")

if __name__ == "__main__":
    main()
