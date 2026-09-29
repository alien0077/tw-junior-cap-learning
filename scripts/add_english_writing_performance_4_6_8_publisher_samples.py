#!/usr/bin/env python3
"""Record public-school publisher evidence for English writing performance 4-Ⅳ-6..8."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；中翻英、生活書信與提示段落寫作定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；句子翻譯、卡片書信與引導段落活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；句意轉寫、功能訊息與短文寫作評量定位。"),
]
UNITS = [
    ("lesson-english-performance-4-iv-6", "4-Ⅳ-6：簡單中翻英", ["中翻英", "句意", "語序", "語境"], "先理解中文句子的事件、時間、語氣和溝通目的，再用英文句型重組，最後檢查主詞、動詞、時態、冠詞與語意是否完整，不逐字替換。", "字面逐詞翻譯可能產生不自然或錯誤句；需保留原句功能與關係，而非只追求字面相似。"),
    ("lesson-english-performance-4-iv-7", "4-Ⅳ-7：簡單卡片訊息書信電郵", ["功能文本", "卡片", "書信", "電郵"], "依收件者、目的與媒介選擇稱呼、開頭、主體資訊、結尾和署名，完成邀請、感謝、祝福或簡短通知，並檢查語氣與格式是否合宜。", "把所有功能文本寫成同一種短文會失去目的；需讓讀者看出為何寫、要知道什麼和如何回應。"),
    ("lesson-english-performance-4-iv-8", "4-Ⅳ-8：提示寫簡短段落", ["提示寫作", "段落", "主題句", "連貫"], "從圖片、關鍵詞或問題提示形成主題句，依時間、空間或理由安排數個相關句子，再用連接詞和結尾句維持段落焦點。", "把提示逐項列出不等於段落；需說明句子之間的關係，刪除離題資訊並檢查指涉與時態一致。"),
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
            blocker["reason"] = blocker["reason"].replace("Eight hundred nineteen unit samples", "Eight hundred twenty-two unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
