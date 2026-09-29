#!/usr/bin/env python3
"""Record public-school publisher evidence for English listening performance 1-Ⅳ-7..9."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；簡短說明、影片理解與語調表情定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；說明敘述、影音素材與情緒語調活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；影片聽解、情境主旨與語氣態度評量定位。"),
]
UNITS = [
    ("lesson-english-performance-1-iv-7", "1-Ⅳ-7：簡短說明敘述情境主旨", ["說明敘述", "情境主旨", "組織線索", "聽力推論"], "從開場主題、順序詞、數字或例子整理簡短說明與敘述的重點，分辨主題、目的和關鍵細節，再用一句話重述情境主旨。", "抓到一個名詞不等於掌握主旨；需說明資訊如何由開頭、發展和結尾組織起來。"),
    ("lesson-english-performance-1-iv-8", "1-Ⅳ-8：簡易影片主要內容", ["影片理解", "畫面線索", "聲音線索", "內容整合"], "把畫面、字幕、音效和口語訊息互相核對，先建立影片事件或主題的時間線，再判斷哪些線索直接說明、哪些只是推測。", "只看字幕或只看畫面都可能誤解；需標記不同媒介提供的證據，並處理字幕與聲音不一致的地方。"),
    ("lesson-english-performance-1-iv-9", "1-Ⅳ-9：語調所表達的情緒態度", ["語調", "情緒", "態度", "語境"], "比較升降調、重音、停頓、音量與語速，結合字面內容和人物關係判斷驚訝、猶豫、禮貌、拒絕或諷刺等態度；回答時說出聲音證據。", "情緒標籤不是證明；同一語調在不同語境可能有不同效果，需同時考慮文字、情境與說話者關係。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred seventy-four unit samples", "Seven hundred seventy-seven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
