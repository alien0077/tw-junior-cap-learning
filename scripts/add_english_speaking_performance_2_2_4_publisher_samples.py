#!/usr/bin/env python3
"""Record public-school publisher evidence for English speaking performance 2-Ⅳ-2..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；生活用語、教室互動與人物描述口語定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；情境口語、教室用語與人物資訊活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；日常溝通、課堂互動與人物描述評量定位。"),
]
UNITS = [
    ("lesson-english-performance-2-iv-2", "2-Ⅳ-2：依情境使用生活用語", ["生活用語", "情境", "禮貌", "口語回應"], "依場所、人物關係、目的和禮貌程度選擇問候、請求、道歉、感謝或拒絕的說法，並用語調和非語言線索讓對方理解意圖。", "背出正確句子不等於合宜；需說明為何該語句適合此對象和情境，並能處理對方回應。"),
    ("lesson-english-performance-2-iv-3", "2-Ⅳ-3：依情境使用教室用語", ["教室用語", "指令", "請求澄清", "互動"], "在課堂活動中用英語請求重複、確認意思、取得物品、加入討論或回報完成狀態；表達要短而可執行，並根據教師或同儕回應修正。", "把所有課堂語句當成命令會造成互動失禮；需分辨請求、確認、回饋和指示的功能。"),
    ("lesson-english-performance-2-iv-4", "2-Ⅳ-4：描述自己家人朋友", ["人物描述", "外貌", "個性", "關係"], "以可觀察的外貌、興趣、習慣和關係資訊描述家人或朋友，使用適切形容詞與句型，並尊重個資與被描述者的感受。", "把刻板印象當成個性描述會失真；需區分觀察、推測與評價，選擇與目的有關的細節。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred eighty unit samples", "Seven hundred eighty-three unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
