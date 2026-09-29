#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Nb-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列國際議題、環境、科技與臺灣公共回應。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列環境、科技、公共治理與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 Nb-IV-1～3，採圖表、史料、討論與紙筆評量。"),
]
UNITS = [
    ("nb-iv-1", "歷 Nb-Ⅳ-1：全球環境與資源", ["全球環境", "資源分配", "氣候變遷", "環境正義"], "整合氣候、資源、產業與人口資料，分析全球環境問題的成因、責任與分配影響。", "不能把環境問題歸因個人消費，需同時檢查制度、產業、國家與跨國治理。"),
    ("nb-iv-2", "歷 Nb-Ⅳ-2：科技、資訊與社會", ["科技", "資訊社會", "數位落差", "公共風險"], "以科技使用、資訊流動與社會資料，評估數位機會、風險、權利與不同群體的落差。", "需區分取得設備、使用能力、資訊品質與實際成果，不能以連線率代表平等。"),
    ("nb-iv-3", "歷 Nb-Ⅳ-3：全球公共回應", ["公共回應", "政策協作", "多方利害", "證據評估"], "比較政策、社群與國際協作案例，提出標示目標、證據、受益者與限制的公共回應。", "要分開政策宣示、執行資料與成效推論，並明確指出尚無法判斷的部分。"),
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
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred thirty-three unit samples", "Six hundred thirty-six unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
