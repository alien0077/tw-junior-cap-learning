#!/usr/bin/env python3
"""Record public-school publisher evidence for English integrated performance 5 and 5-Ⅳ-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；聽說讀寫綜合應用、字彙溝通與問答定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；整合技能、字彙句型與情境問答活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；綜合溝通、字彙句型與口語回應評量定位。"),
]
UNITS = [
    ("lesson-english-performance-5", "語言能力（聽說讀寫綜合應用能力）", ["綜合應用", "聽說讀寫", "策略整合", "任務遷移"], "把聽、說、讀、寫放進同一個有目的的任務：先從輸入擷取資料，再用口語或書面產出回應，最後依讀者或聽者反應修正，檢查語言形式與溝通目的是否一致。", "單一技能測驗不代表綜合應用；需追蹤輸入、理解、產出和回饋之間的證據鏈。"),
    ("lesson-english-performance-5-iv-1", "5-Ⅳ-1：基本字彙理解使用", ["字彙理解", "詞性", "搭配", "語境使用"], "由字形、發音、詞性、搭配和上下文理解基本字彙，再把字彙放入新句子或短對話中使用，確認詞義與情境相符。", "背出中文對譯不等於會用；需檢查詞性、搭配、語氣和句中角色。"),
    ("lesson-english-performance-5-iv-2", "5-Ⅳ-2：用字彙句型日常溝通", ["字彙句型", "日常溝通", "情境", "互動修補"], "選擇符合目的和對象的字彙句型完成問候、請求、描述、邀約或求助，並依對方回應用確認、重述或替代說法維持互動。", "只套用句型可能忽略情境；需說明選擇的功能，並處理對方沒有照預期回答的情況。"),
    ("lesson-english-performance-5-iv-3", "5-Ⅳ-3：常見問答回應", ["問答", "理解問題", "回應", "資訊完整"], "先判斷問題要求的人事時地物或理由，再用完整但適量的資訊回答；若問題含糊或資料不足，能請對方澄清而不是任意猜測。", "重複問題或只回答一個單字可能無法完成互動；需使回答與問題焦點、時態和對象一致。"),
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
            blocker["reason"] = blocker["reason"].replace("Eight hundred twenty-two unit samples", "Eight hundred twenty-six unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
