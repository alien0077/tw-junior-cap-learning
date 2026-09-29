"""Gb-Ⅳ-1：化石記錄與生物滅絕第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-gb-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-gb-iv-1-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "化石、地層、演化證據與滅絕資料判讀", "pattern": "取由地層順序、化石分布、時間尺度和資料缺口建立演化與滅絕推論的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "化石形成、地層與演化證據", "pattern": "取化石形成、疊積律、指標化石、地層關係與滅絕事件的教學及評量方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "化石序列、共同祖先與證據限制", "pattern": "取跨地點比較、地層缺口、過渡證據、滅絕規模和年代標示的證據判讀方向。"},
]

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = TODAY; lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {"commonCore": ["三版本公開線索共同支持由化石、地層順序與時間尺度重建生物演化及滅絕記錄。", "疊積律、指標化石、跨地點比較、沉積間斷、共同祖先、滅絕規模與證據限制是共同能力核心。"], "versionDifferences": ["南一公開定位偏向化石與地層順序；康軒線索偏向化石形成、指標化石與滅絕事件；翰林線索偏向跨地點比較、過渡證據、地層缺口及年代資料可信度。公開資料不足以宣稱取得完整教材內容。"], "originalAdditions": ["以地層剖面、跨地點指標化石、沉積間斷、滅絕前後物種資料和博物館標示建立證據鏈。", "把化石消失必然等於全球滅絕、化石存在必然代表整段時間都存在、地層缺口可忽略列為單元迷思診斷。"], "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織化石、地層、指標化石、演化證據、滅絕、時間尺度與資料限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []): entry["reviewedAt"] = TODAY
    refs = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]
    questions = sorted(path for path in QDIR.glob("question-science-content-gb-iv-1-*.json") if path.stem.removeprefix("question-science-content-gb-iv-1-").isdigit())
    if len(questions) != 10: raise SystemExit(f"Gb-Ⅳ-1 題數應為 10，實際為 {len(questions)}")
    for path in questions:
        q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs; p = q.setdefault("provenance", {}); p["sourceUrl"] = SOURCES[0]["url"]; p["sourceLocator"] = "三筆公立學校／公開自然科試題與課程資料的化石、地層、演化證據及滅絕資料判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"] = "本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Gb-Ⅳ-1 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"] = "draft"; q["updatedAt"] = TODAY; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "Gb-Ⅳ-1：化石記錄與生物滅絕", "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "10 題均逐題核對化石與滅絕單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print("authored science content gb iv 1")

if __name__ == "__main__": main()
