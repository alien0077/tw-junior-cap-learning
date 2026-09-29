#!/usr/bin/env python3
"""Record public-school publisher evidence for English listening performance 1-Ⅳ-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；課堂字詞、生活用語與基本句型聽辨定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；字詞音檔、教室互動與核心句型活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；字詞辨識、日常溝通與句型聽說評量定位。"),
]
UNITS = [
    ("lesson-english-performance-1-iv-1", "1-Ⅳ-1：課堂字詞", ["課堂字詞", "語音辨識", "詞義", "聽辨"], "在課堂指令、物品與活動情境中辨認常用字詞的聲音、重音和基本意思，並用動作、圖片或簡短回應證明理解。", "聽到熟悉音節不等於掌握詞義；需結合說話者動作、前後語句與課堂任務判斷。"),
    ("lesson-english-performance-1-iv-2", "1-Ⅳ-2：常用教室與生活用語", ["教室用語", "生活用語", "功能理解", "適切回應"], "依請求、指令、問候、澄清或結束活動等功能辨認常用語，再依人物關係與場所選擇口語或行動回應，避免只逐字翻譯。", "同一句話在教室和日常場所可能有不同功能；需檢查語氣、情境和回應是否相互匹配。"),
    ("lesson-english-performance-1-iv-3", "1-Ⅳ-3：基本重要句型", ["基本句型", "語序", "主旨", "句型聽辨"], "從主語、動詞、時間與疑問詞等線索辨認基本句型的訊息骨架，先抓問題或陳述的目的，再補足關鍵細節並做出相應回應。", "逐字抄下聲音可能漏掉關係；需利用句型與語調預測訊息功能，再以內容核對預測。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred sixty-eight unit samples", "Seven hundred seventy-one unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
