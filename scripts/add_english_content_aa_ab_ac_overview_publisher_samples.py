#!/usr/bin/env python3
"""Record public-school publisher evidence for English Aa, Ab and Ac overviews."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；Starter 與字母、語音、字彙學習定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；Get Ready 與語言知識、溝通活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；Starter 與聽說讀寫、數位學習定位。"),
]
UNITS = [
    ("lesson-english-content-aa", "Aa：字母", ["大小寫", "字母辨識", "書寫", "拼字基礎"], "先建立大小寫字母的視覺對應與可讀書寫，再把字母放進姓名、標示和簡短字詞中，連結字母名稱、字音與拼字位置。", "只會背字母歌不代表能辨認或書寫；需分開檢查辨識、筆畫、字母名稱與在字詞中的遷移。"),
    ("lesson-english-content-ab", "Ab：語音", ["發音", "重音", "語調", "聽辨"], "由音節、字詞重音和句子語調建立聽說線索，將音檔、文字與情境對照；同一句型需比較陳述、提問與情緒變化。", "逐字翻譯不能取代聽辨；需說明聲音線索如何影響意義，並以朗讀或錄音回聽檢查。"),
    ("lesson-english-content-ac", "Ac：字彙", ["字詞", "詞義", "詞性", "語境"], "以生活情境和短文本建立字彙網絡，從字形、聲音、詞性、搭配和上下文推定意義，再在新句子中驗證而非只背單一中文對譯。", "知道一個翻譯不等於會用字；需檢查詞性、搭配、語氣與情境是否支持選擇。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred fifty-six unit samples", "Seven hundred fifty-nine unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
