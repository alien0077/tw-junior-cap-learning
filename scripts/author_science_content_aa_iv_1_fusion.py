"""Aa-Ⅳ-1：原子模型演變的第一輪來源融合與報告。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-aa-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-aa-iv-1-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"

SOURCES = [
    {
        "url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf",
        "title": "114 年國中教育會考自然科公開試題",
        "year": "114",
        "locator": "原子模型、陰極射線、金箔散射、模型修正與科學證據判讀",
        "pattern": "取由實驗觀察推論微觀模型，並比較模型解釋力與限制的能力方向。",
    },
    {
        "url": "https://www.tksh.ntpc.edu.tw/uploads/1626668076188QlOI4fer.pdf",
        "title": "新北市立泰山高中公開原子模型與科學史銜接教材",
        "year": "公開教材",
        "locator": "陰極射線、金箔散射、原子核與模型修正",
        "pattern": "取由資料反推模型假設、辨識反常結果並修正模型的能力方向。",
    },
    {
        "url": "https://www.tcjh.tyc.edu.tw/image/1534212714782dPiSoOmq.pdf",
        "title": "桃園市立自強國民中學公開自然科段考試題",
        "year": "公開試題",
        "locator": "粒子模型、原子結構與科學證據判讀",
        "pattern": "取把觀察、推論、模型與適用範圍分層判讀的能力方向。",
    },
]


def refs():
    return [
        {
            **source,
            "subject": "science",
            "observedPattern": source["pattern"],
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "paper",
        }
        for source in SOURCES
    ]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["fusionRecord"] = {
        "commonCore": [
            "三版本公開章節線索共同指向以物質粒子、原子結構與科學史證據理解模型演變。",
            "陰極射線、金箔散射、光譜與模型限制是共同的證據判讀核心。",
        ],
        "versionDifferences": [
            "南一公開定位偏向由物質組成問題進入模型；康軒線索偏向章節活動與紙筆／實作評量；翰林線索偏向科學史時間線、模型比較與證據修正。公開資料不足以宣稱取得完整教材內容。",
        ],
        "originalAdditions": [
            "以模型預測卡、散射路徑、光譜證據欄和反常結果重建可操作的證據鏈。",
            "把模型圖不是原子照片、早期模型並非全錯、光譜線不是電子路徑三個迷思放入分層診斷。",
        ],
        "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／教材的能力方向，重新組織道耳頓、湯姆森、拉塞福、波耳與現代模型的證據鏈；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。",
    }
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []):
        entry["reviewedAt"] = TODAY
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"

    for path in sorted(QDIR.glob("question-science-content-aa-iv-1-*.json")):
        question = json.loads(path.read_text(encoding="utf-8"))
        question["examPatternRefs"] = refs()
        question.setdefault("provenance", {})["sourceUrl"] = SOURCES[0]["url"]
        question["provenance"]["sourceLocator"] = (
            "三筆公立學校公開自然科試題／教材的原子模型、粒子證據與模型修正能力方向；"
            "本題只作 pattern-only 改寫。"
        )
        question["provenance"]["authoringNote"] = (
            "本題取公開試題能力方向，題幹、選項、答案、解析與五步解法均依 Aa-Ⅳ-1 重新撰寫，"
            "未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        )
        question["reviewStatus"] = "draft"
        question["updatedAt"] = TODAY
        path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    REPORT.write_text(
        json.dumps(
            {
                "unit": "Aa-Ⅳ-1：原子模型演變",
                "lessonId": lesson["id"],
                "status": "first-pass-ai-review-complete",
                "reviewStatus": "draft",
                "checkedQuestions": 10,
                "checks": {
                    "unitSpecificOriginalContent": True,
                    "threeVersionResearchRecords": True,
                    "threePublicSchoolExamPatternSources": True,
                    "answersAndDetailedSteps": True,
                    "interactivePredictionManipulationExplanation": True,
                    "terraSecondPass": "pending",
                },
                "reviewedAt": TODAY,
                "note": "三筆公開試題／教材僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。",
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content aa iv 1")


if __name__ == "__main__":
    main()
