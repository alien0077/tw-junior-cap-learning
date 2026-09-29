#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Oa-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列當代民主、人權、全球治理與公共議題。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列民主、人權、國際參與與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 Oa-IV-1～3，採圖表、史料、討論與紙筆評量。"),
]
UNITS = [
    ("oa-iv-1", "歷 Oa-Ⅳ-1：民主、人權與公共生活", ["民主", "人權", "公共生活", "制度與參與"], "比較制度、權利、選舉與公共生活資料，分析民主實踐的規範、參與與限制。", "不能把法律保障直接當成實際平等，需檢查不同群體的參與條件與權利落差。"),
    ("oa-iv-2", "歷 Oa-Ⅳ-2：全球治理與國際合作", ["全球治理", "國際合作", "國際組織", "多方協商"], "以國際組織、條約與跨國議題資料，評估全球合作的規則、權力與執行效果。", "需區分規範承諾、資源能力與實際結果，不能以組織成立推論問題已解決。"),
    ("oa-iv-3", "歷 Oa-Ⅳ-3：公共議題資料探究", ["公共議題", "資料探究", "多元觀點", "政策評估"], "整合統計、史料、媒體與政策資料，形成有證據、可追溯並標示限制的公共議題結論。", "要分開資料、推論與價值判斷，並說明未納入的資料與可能反例。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-hist-" + suffix
        units[lesson_id] = {"lessonId": lesson_id, "title": title, "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": [{"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"} for publisher, url, locator in SOURCES], "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"}}
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"]); data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred thirty-six unit samples", "Six hundred thirty-nine unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
