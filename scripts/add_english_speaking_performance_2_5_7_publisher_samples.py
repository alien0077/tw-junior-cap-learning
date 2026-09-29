#!/usr/bin/env python3
"""Record public-school publisher evidence for English speaking performance 2-Ⅳ-5..7."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；需求意願、人物描述與提問口語定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；生活溝通、資訊描述與問答活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；意願感受、人物事件描述與提問回應評量定位。"),
]
UNITS = [
    ("lesson-english-performance-2-iv-5", "2-Ⅳ-5：表達需求意願感受", ["需求", "意願", "感受", "禮貌表達"], "用適切句型、情緒詞和語調說明需要什麼、想做什麼或感受到什麼，依對象和情境調整直接程度，並聽懂對方是否接受或需要澄清。", "只說出單字不能完成表達；需讓聽者知道需求內容、強度、理由或下一步，也要尊重對方的選擇。"),
    ("lesson-english-performance-2-iv-6", "2-Ⅳ-6：人事時地物描述回答", ["人事時地物", "描述", "資訊組織", "回答"], "以 who、what、when、where、which 等資訊欄位組織描述或回答，依問題挑出相關細節，避免把不確定的推測說成已知事實。", "把所有細節都說出來會降低清楚度；需判斷問題焦點、使用正確時間與地點線索，並保持回答和問題對齊。"),
    ("lesson-english-performance-2-iv-7", "2-Ⅳ-7：人事時地物提問", ["提問", "疑問詞", "資訊缺口", "追問"], "先辨認自己缺少的是人物、事件、時間、地點或物件資訊，再選擇疑問詞和句型提出可回答的問題；依答案提出必要追問或修正理解。", "只會套疑問詞不代表問得有效；需檢查問題是否有明確資訊缺口、語序是否正確、對方是否能據此回答。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred eighty-three unit samples", "Seven hundred eighty-six unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
