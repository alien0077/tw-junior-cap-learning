#!/usr/bin/env python3
"""Record public-school publisher evidence for English integrated performance 5-Ⅳ-10..12."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；故事主旨表達、閱讀填表與書信卡片回應定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；故事重述、表格資訊與功能文本回應活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；故事理解表達、資料整理與書信卡片書面評量定位。"),
]
UNITS = [
    ("lesson-english-performance-5-iv-10", "5-Ⅳ-10：故事短文主旨口頭或書面表達", ["故事主旨", "重述", "口頭表達", "書面表達"], "先從角色、事件和結果推導故事主旨，再依聽者或讀者選擇口頭重述或短文表達，保留因果與關鍵證據，不把細節堆成摘要。", "只抄故事中的一句話不一定是主旨；需說明選材如何支持整體訊息。"),
    ("lesson-english-performance-5-iv-11", "5-Ⅳ-11：閱讀填寫簡單表格資料", ["閱讀填表", "欄位", "資料擷取", "核對"], "先讀表格欄位和文本任務，再從短文、公告或對話擷取相應資訊；填寫後回到原文核對人事時地物、單位和資料範圍。", "表格填滿不代表正確；需確認每一格都有來源證據，並處理同一資訊在文本中的改寫。"),
    ("lesson-english-performance-5-iv-12", "5-Ⅳ-12：理解簡易書信卡片並回應", ["書信卡片", "閱讀理解", "回應", "功能文本"], "辨認寄件者、收件者、目的、時間與需要回應的問題，再依關係和目的寫出有禮、完整且格式相符的回覆，避免漏答或加入沒有根據的資訊。", "只回覆最明顯的一句會漏掉任務；需逐項對照原文中的邀請、問題、限制和下一步。"),
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
            blocker["reason"] = blocker["reason"].replace("Eight hundred thirty-two unit samples", "Eight hundred thirty-five unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
