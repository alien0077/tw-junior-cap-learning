#!/usr/bin/env python3
"""Record public-school publisher evidence for English writing performance 4-Ⅳ-3..5."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；英文格式、表格填寫與提示句子寫作定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；書寫格式、資訊表格與引導寫句活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；格式規範、資料填寫與句子書面表達評量定位。"),
]
UNITS = [
    ("lesson-english-performance-4-iv-3", "4-Ⅳ-3：正確書寫格式", ["格式", "大小寫", "標點", "版面"], "依文本任務使用大小寫、標點、空格、日期、稱謂、段落與版面格式，完成後用讀者視角檢查資訊是否容易定位和理解。", "字拼對不代表格式正確；需按文本用途檢查每項格式規範，避免把中文慣例直接套到英文。"),
    ("lesson-english-performance-4-iv-4", "4-Ⅳ-4：填簡單表格", ["表格", "欄位", "資料擷取", "核對"], "先讀表格標題、欄位名稱和填寫規則，再從圖片、對話或短文擷取相應資訊；填完逐欄核對格式、單位與資料是否超出來源。", "把資料寫進錯欄會造成整體誤讀；需確認每個答案回應哪一個欄位和來源線索。"),
    ("lesson-english-performance-4-iv-5", "4-Ⅳ-5：提示寫正確簡單句", ["提示寫作", "句型", "語序", "校對"], "依圖片、關鍵字或句型提示形成有主詞、動詞和必要資訊的簡單句，再檢查大小寫、標點、動詞形式和句意是否符合提示。", "逐字抄提示可能產生不完整句；需判斷提示的功能，補足語法關係而不新增沒有根據的內容。"),
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
            blocker["reason"] = blocker["reason"].replace("Eight hundred sixteen unit samples", "Eight hundred nineteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
