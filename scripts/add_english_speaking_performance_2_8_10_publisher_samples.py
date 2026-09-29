#!/usr/bin/env python3
"""Record public-school publisher evidence for English speaking performance 2-Ⅳ-8..10."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；發音重音、角色互動與圖片口語定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；語調練習、角色扮演與圖片描述活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；發音口說、情境短劇與圖片敘述評量定位。"),
]
UNITS = [
    ("lesson-english-performance-2-iv-8", "2-Ⅳ-8：正確發音重音語調說基本句", ["發音", "重音", "語調", "基本句"], "以可理解發音為基礎，練習句子重音、停頓和語調，讓基本句的疑問、陳述或禮貌功能清楚；錄音回聽時同時檢查形式和聽者理解。", "追求口音像不像不是唯一判準；需看音段、重音、語調是否造成理解障礙，以及表達是否符合情境。"),
    ("lesson-english-performance-2-iv-9", "2-Ⅳ-9：角色扮演", ["角色扮演", "情境", "輪替", "互動修正"], "依角色卡掌握人物目標、關係和限制，以英語完成多輪互動；演出後交換角色或根據同伴回應修正說法，避免只背固定對話。", "把劇本背完不等於完成溝通；需能在資訊改變、對方追問或忘詞時維持角色目的並修補對話。"),
    ("lesson-english-performance-2-iv-10", "2-Ⅳ-10：描述圖片", ["圖片描述", "空間關係", "觀察", "組織口語"], "先從人物、動作、位置、物件和背景建立觀察清單，再以空間或事件順序組織句子；區分看見的資訊與合理推測，讓聽者能重建畫面。", "逐一念出名詞會缺少關係；需使用位置、動作、時間和因果語句，並避免把圖片以外的猜想當成事實。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {item["lessonId"]: item for item in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [
                {"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教材正文、歌詞、題目、答案或版面。"}
                for publisher, url, locator in SOURCES
            ],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda item: item["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Seven hundred eighty-six unit samples", "Seven hundred eighty-nine unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
