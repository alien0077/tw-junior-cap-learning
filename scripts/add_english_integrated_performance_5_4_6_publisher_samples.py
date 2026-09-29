#!/usr/bin/env python3
"""Record public-school publisher evidence for English integrated performance 5-Ⅳ-4..6."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；短文短劇朗讀、拼讀規則與對話轉述定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；音韻朗讀、拼字規則與口語轉述活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；短文朗讀、字音拼讀與對話重述評量定位。"),
]
UNITS = [
    ("lesson-english-performance-5-iv-4", "5-Ⅳ-4：朗讀短文短劇", ["朗讀", "短文", "短劇", "語音表達"], "朗讀前先理解句子和角色目的，再以重音、停頓、語調和輪次呈現短文或短劇；回聽時檢查聲音是否幫助聽者理解內容與情緒。", "逐字念完不等於朗讀有效；需兼顧正確、流暢、可理解和情境表達。"),
    ("lesson-english-performance-5-iv-5", "5-Ⅳ-5：拼讀規則讀拼字", ["拼讀規則", "字母音", "音節", "拼字閱讀"], "利用常見字母音、音節、字尾和拼讀模式讀出新字，再以句子或詞組確認讀音和詞義；遇到例外字要標記並查證，不任意套用規則。", "會背規則不代表能遷移；需說明使用哪個音形線索，並驗證讀音是否符合上下文。"),
    ("lesson-english-performance-5-iv-6", "5-Ⅳ-6：轉述簡短對話", ["轉述", "對話", "主旨", "人稱時態"], "先整理對話人物、目的與主要訊息，再依聽者需要改用自己的話轉述，調整人稱、時間、指涉與語氣，保留原對話的關鍵條件。", "逐句翻譯不是轉述；需取捨細節、維持事件關係，並區分原話、摘要和自己的推論。"),
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
            blocker["reason"] = blocker["reason"].replace("Eight hundred twenty-six unit samples", "Eight hundred twenty-nine unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
