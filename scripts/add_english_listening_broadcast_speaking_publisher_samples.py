#!/usr/bin/env python3
"""Record public-school publisher evidence for English listening 1-Ⅳ-10..11 and speaking 2-Ⅳ-1."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；歌謠韻文、公共訊息與口語字詞表達定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；節奏活動、廣播理解與口語練習定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；韻文音韻、公共場所聽解與課堂口語評量定位。"),
]
UNITS = [
    ("lesson-english-performance-1-iv-10", "1-Ⅳ-10：歌謠韻文節奏音韻", ["節奏", "音韻", "重讀", "押韻"], "聽辨拍點、重讀、弱讀與押韻位置，觀察聲音模式如何支撐跟讀與記憶，再把音韻線索和歌謠韻文的主要內容連結。", "只會跟唱不代表能分析；需指出重讀或押韻的證據，並區分聲音形式和文本意思。"),
    ("lesson-english-performance-1-iv-11", "1-Ⅳ-11：公共場所廣播", ["公共廣播", "關鍵資訊", "場所", "行動指示"], "在車站、機場、校園或商店廣播中辨認場所、時間、對象、變更與下一步行動，利用重複、數字和語氣確認關鍵訊息。", "只抓到地點可能錯過真正任務；需把時間、限制、對象與行動要求組合成可執行的理解。"),
    ("lesson-english-performance-2-iv-1", "2-Ⅳ-1：說出課堂字詞", ["口語字詞", "發音", "重音", "可理解表達"], "在課堂和生活情境中說出常用字詞，注意音節、重音、尾音與語速，並以圖片、動作或短句證明字詞能被正確使用，而不只會單獨朗讀。", "發音像不像母語者不是唯一標準；需檢查聽者是否理解、詞義是否切合情境，以及說法能否延伸到短句。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred seventy-seven unit samples", "Seven hundred eighty unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
