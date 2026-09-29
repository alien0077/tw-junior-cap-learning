#!/usr/bin/env python3
"""Record public-school publisher evidence for English integrated performance 5-Ⅳ-7..9."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；日常對話、故事與廣播聽力筆記定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；聽力活動、故事理解與公共訊息記錄定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；對話故事廣播聽解與重點整理評量定位。"),
]
UNITS = [
    ("lesson-english-performance-5-iv-7", "5-Ⅳ-7：聽日常對話筆記", ["聽力筆記", "日常對話", "關鍵詞", "資訊整理"], "聽對話時記錄人物、目的、時間、地點與待辦事項等關鍵詞，不追求逐字抄寫；聽後用筆記重建對話主旨並核對遺漏。", "寫滿文字不等於好筆記；需取捨與任務有關的資訊，保留可回溯的關係和不確定處。"),
    ("lesson-english-performance-5-iv-8", "5-Ⅳ-8：聽簡單故事筆記", ["故事筆記", "事件順序", "角色目標", "因果"], "用角色、場景、問題、行動、結果或時間線記錄故事骨架，保留轉折與因果；聽後以筆記口頭或書面重述，而非逐句翻譯。", "只記角色和名詞會失去情節；需標記事件先後、衝突和結果如何連接。"),
    ("lesson-english-performance-5-iv-9", "5-Ⅳ-9：聽簡單廣播筆記", ["廣播筆記", "公共資訊", "數字時間", "行動要求"], "聽公共廣播時快速記錄場所、時間、變更、限制與行動要求，利用重複和數字確認；聽後將筆記轉成可執行的行程或回應。", "只記下地點或主題可能無法行動；需核對日期、時間、對象、例外與資訊來源。"),
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
            blocker["reason"] = blocker["reason"].replace("Eight hundred twenty-nine unit samples", "Eight hundred thirty-two unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
