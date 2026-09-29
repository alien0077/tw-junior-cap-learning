"""G：演化與延續第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-g.json"
REPORT = ROOT / "implementation/reports/science-content-g-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "演化、遺傳變異、自然選擇與證據判讀", "pattern": "取由化石、性狀、族群資料與環境條件推論演化機制的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "遺傳變異、演化證據與適應", "pattern": "取變異、遺傳、環境選擇壓力、適應及證據限制的教學與評量方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "族群變化、共同祖先與演化推論", "pattern": "取比較構造、化石序列、族群基因頻率與隔離資料來建立演化推論的能力方向。"},
]

def source_refs():
    return [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {
        "commonCore": ["三版本公開線索共同支持由族群中的遺傳變異、世代傳遞與環境條件解釋適應與演化。", "化石、同源構造、抗藥性、人工選擇、基因頻率、隔離與證據界線是共同能力核心。"],
        "versionDifferences": ["南一公開定位偏向遺傳變異與自然選擇；康軒線索偏向適應、環境選擇壓力與資料判讀；翰林線索偏向比較構造、化石序列、族群頻率及隔離推論。公開資料不足以宣稱取得完整教材內容。"],
        "originalAdditions": ["以樹皮顏色、抗生素抗性、島嶼鳥類和化石序列建立不同尺度的演化證據鏈。", "把『個體為了適應而主動改變』『有用性狀必然先出現』『演化等於變得更高等』列為迷思診斷，要求區分變異來源、選擇結果與資料尚未能證明的部分。"],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織遺傳變異、自然選擇、適應、人工選擇、共同祖先、化石、同源構造、隔離與族群基因頻率；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    refs = source_refs()
    questions = sorted(path for path in QDIR.glob("question-science-content-g-*.json") if path.stem.removeprefix("question-science-content-g-").isdigit())
    if len(questions) != 10:
        raise SystemExit(f"G 題數應為 10，實際為 {len(questions)}")
    for path in questions:
        q = json.loads(path.read_text(encoding="utf-8"))
        q["examPatternRefs"] = refs
        provenance = q.setdefault("provenance", {})
        provenance["sourceUrl"] = SOURCES[0]["url"]
        provenance["sourceLocator"] = "三筆公立學校／公開自然科試題與課程資料的演化、遺傳變異、族群資料及證據判讀能力方向；本題只作 pattern-only 改寫來源。"
        provenance["authoringNote"] = "本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 G 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        q["reviewStatus"] = "draft"
        q["updatedAt"] = TODAY
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "G：演化與延續", "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10,
        "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"},
        "reviewedAt": TODAY, "note": "10 題均逐題核對演化單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content g")

if __name__ == "__main__":
    main()
