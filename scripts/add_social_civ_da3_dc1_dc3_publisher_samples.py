#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Da-IV-3 and Dc-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版公民課程的公平正義與文化差異範圍，定位公 Da-IV-3、Dc-IV-1～3。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版公民課程列制度性公平、文化差異、文化位階與尊重包容。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版公民課程列公 Da-IV-3、Dc-IV-1～3，採問題討論、隨堂測驗與課堂問答。"),
]
UNITS = [
    ("da-iv-3", "公 Da-Ⅳ-3：行善與制度性公平正義", ["個人行善", "制度設計", "公平正義", "結構性不平等"], "用同一社會問題的個人援助、公共制度與長期結果比較表，分析行善能補位但未必消除造成不平等的制度條件。", "要求區分立即救助與制度改革的作用、對象與副作用，不能把個人善意直接等同社會正義。"),
    ("dc-iv-1", "公 Dc-Ⅳ-1：日常生活中的文化差異", ["文化", "生活方式", "群體經驗", "文化差異"], "以飲食、語言、家庭習俗與校園互動的生活案例，區分文化差異與個人偏好，呈現文化在群體中學習與變動。", "要求以案例證據描述差異，避免把單一成員的行為當成整個文化的固定特徵。"),
    ("dc-iv-2", "公 Dc-Ⅳ-2：語言文化位階與不平等", ["文化位階", "語言權力", "制度偏見", "不平等"], "用同一公共服務在不同語言使用者身上的流程與成本圖，追蹤規則、資源與社會評價如何造成位階差異。", "要求分辨差異本身與由權力／制度造成的不平等，不能只用『大家不同』掩蓋排除效果。"),
    ("dc-iv-3", "公 Dc-Ⅳ-3：尊重包容文化差異", ["尊重", "包容", "平等互動", "衝突調整"], "以校園或社區共同規範的協商情境，讓學生比較表面容忍、平等參與與調整制度安排的不同層次。", "要求提出可執行的溝通與制度調整方案，並檢查是否同時保護個人權利與群體差異。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-civ-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [{
                "publisher": publisher, "sourceUrl": url,
                "sourceKind": "public-school-course-plan-identifying-publisher-material",
                "locator": locator, "accessedAt": "2026-09-21",
                "observedConcepts": [title, *core],
                "observedRepresentations": [representation],
                "observedAssessment": [assessment],
                "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
            } for publisher, url, locator in SOURCES],
            "fusionReview": {
                "commonCore": core,
                "differencesToReview": [representation, assessment],
                "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。",
            },
        }
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str):
            b["reason"] = b["reason"].replace("Five hundred twenty-four unit samples", "Five hundred twenty-eight unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
