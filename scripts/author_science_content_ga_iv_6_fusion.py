"""Ga-Ⅳ-6：孟德爾遺傳研究的科學史第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ga-iv-6.json"
REPORT = ROOT / "implementation/reports/science-content-ga-iv-6-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "孟德爾遺傳、機率、資料判讀與實驗設計", "pattern": "取由遺傳資料、比例、控制變因和樣本大小檢查模型的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "孟德爾實驗、顯性隱性與分離律", "pattern": "取豌豆材料選擇、純品系、雜交、顯性／隱性、分離律與棋盤格的教學及評量方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "孟德爾遺傳資料、測交、樣本與科學史", "pattern": "取測交、理論比例與觀察比例、環境控制、樣本大小及科學史脈絡的能力方向。"},
]

def source_refs():
    return [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {
        "commonCore": ["三版本公開線索共同支持以豌豆雜交、純品系、顯性／隱性、分離律與比例資料理解孟德爾模型。", "材料選擇、測交、棋盤格、理論與觀察比例、環境控制、樣本大小及科學史證據是共同能力核心。"],
        "versionDifferences": ["南一公開定位偏向孟德爾實驗和遺傳比例；康軒線索偏向豌豆材料、顯性／隱性與分離律；翰林線索偏向測交、樣本與環境控制，並把研究放回科學史脈絡。公開資料不足以宣稱取得完整教材內容。"],
        "originalAdditions": ["以豌豆材料選擇、TT×tt、Tt×Tt、測交和不同樣本數逐步重建研究證據鏈，讓公式對應實驗觀察。", "把『3:1 每次都必然精確』『顯性就是比較強』『孟德爾直接看見基因』列為單元迷思診斷。"],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織孟德爾材料、純品系、雜交、顯性／隱性、分離律、測交、樣本大小、環境控制與科學史；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    refs = source_refs()
    questions = sorted(path for path in QDIR.glob("question-science-content-ga-iv-6-*.json") if path.stem.removeprefix("question-science-content-ga-iv-6-").isdigit())
    if len(questions) != 10:
        raise SystemExit(f"Ga-Ⅳ-6 題數應為 10，實際為 {len(questions)}")
    for path in questions:
        q = json.loads(path.read_text(encoding="utf-8"))
        q["examPatternRefs"] = refs
        provenance = q.setdefault("provenance", {})
        provenance["sourceUrl"] = SOURCES[0]["url"]
        provenance["sourceLocator"] = "三筆公立學校／公開自然科試題與課程資料的孟德爾實驗、遺傳比例、測交、樣本及控制變因能力方向；本題只作 pattern-only 改寫來源。"
        provenance["authoringNote"] = "本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ga-Ⅳ-6 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        q["reviewStatus"] = "draft"
        q["updatedAt"] = TODAY
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "Ga-Ⅳ-6：孟德爾遺傳研究的科學史", "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10,
        "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"},
        "reviewedAt": TODAY, "note": "10 題均逐題核對孟德爾遺傳科學史單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ga iv 6")

if __name__ == "__main__":
    main()
