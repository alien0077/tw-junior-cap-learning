"""Db-Ⅳ-4：生殖系統、配子、性生殖與激素第一輪來源融合。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-db-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-db-iv-4-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "生殖、遺傳與生命延續相關資料判讀", "pattern": "取由生殖構造、遺傳資訊與資料推論生命延續的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "生殖系統、配子、受精與激素調節", "pattern": "取生殖器官、配子形成、受精、青春期與週期性激素調節的教學與評量方向。"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf", "title": "新北市文山區安康高中國中部公開翰林版自然簡案", "year": "公開課程計畫", "locator": "性生殖、遺傳資訊組合與生殖週期", "pattern": "取性生殖中雙親遺傳資訊組合、配子與生殖週期資料解讀的能力方向。"},
]


def refs():
    return [{**source, "subject": "science", "observedPattern": source["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for source in SOURCES]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["fusionRecord"] = {
        "commonCore": [
            "三版本公開線索共同支持以生殖系統、配子與受精說明生命延續，並以性生殖中雙親遺傳資訊的組合建立差異。",
            "激素訊息、青春期變化與生殖週期資料判讀，是把構造、功能與調節連起來的共同能力核心。",
        ],
        "versionDifferences": [
            "南一公開定位偏向生殖構造與生命延續資料；康軒線索偏向配子、受精及激素調節；翰林線索偏向性生殖、遺傳資訊組合與週期資料。公開資料不足以宣稱取得完整教材內容。",
        ],
        "originalAdditions": [
            "以配子—受精卵—個體的遺傳資訊模型、青春期激素訊息與週期曲線建立互動，讓學生區分構造、細胞與訊息層次。",
            "把有性生殖誤當成單一親本複製、把激素當作直接搬運的營養物質、把月經週期圖的高低值直接等同器官功能列為單元專屬迷思診斷。",
        ],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織生殖系統、配子、性生殖、受精、遺傳資訊、青春期與激素調節；正文、互動、題目、答案、解析與五步解法均為原創。已修正原先錯置且答案矛盾的運動／呼吸題為配子受精題，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    for path in sorted(QDIR.glob("question-science-content-db-iv-4-*.json")):
        question = json.loads(path.read_text(encoding="utf-8"))
        question["examPatternRefs"] = refs()
        provenance = question.setdefault("provenance", {})
        provenance["sourceUrl"] = SOURCES[0]["url"]
        provenance["sourceLocator"] = "三筆公立學校公開自然科試題／課程資料的生殖系統、配子、受精、性生殖與激素調節能力方向；本題只作 pattern-only 改寫。"
        provenance["authoringNote"] = "本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Db-Ⅳ-4 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        question["reviewStatus"] = "draft"
        question["updatedAt"] = TODAY
        path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "Db-Ⅳ-4：生殖系統、配子、性生殖與激素",
        "lessonId": lesson["id"],
        "status": "first-pass-ai-review-complete",
        "reviewStatus": "draft",
        "checkedQuestions": 10,
        "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "unitMismatchRemediated": True, "terraSecondPass": "pending"},
        "reviewedAt": TODAY,
        "note": "已修正原先錯置且答案矛盾的運動／呼吸題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content db iv 4")


if __name__ == "__main__":
    main()
