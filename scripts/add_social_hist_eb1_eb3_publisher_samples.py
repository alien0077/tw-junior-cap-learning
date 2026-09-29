#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Eb-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列近代東亞與臺灣、殖民現代性、戰爭與社會變遷。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列臺灣近代史、殖民統治、戰爭與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 Eb-IV-1～3，採時間線、地圖、史料、討論與紙筆評量。"),
]
UNITS = [
    ("eb-iv-1", "歷 Eb-Ⅳ-1：近代臺灣與世界", ["近代臺灣", "世界連結", "政經變動", "地方社會"], "以政權、貿易、人口與地方社會資料，分析近代臺灣如何處在東亞與世界的連結和權力變動中。", "不能用單一政權視角概括臺灣社會，需區分統治、地方行動與跨域流動。"),
    ("eb-iv-2", "歷 Eb-Ⅳ-2：殖民統治與社會變遷", ["殖民統治", "制度與教育", "資源與勞動", "社會回應"], "比較殖民制度、教育、產業與社會生活資料，判讀制度改造、利益分配與不同群體的回應。", "要分開政策目標、實際效果與人民經驗，不能只用現代化成果替支配關係辯護。"),
    ("eb-iv-3", "歷 Eb-Ⅳ-3：戰爭與臺灣社會", ["戰爭", "動員", "人口與經濟", "記憶與史料"], "從動員、物資、人口與口述或檔案資料，分析戰爭如何改變臺灣社會並留下多重記憶。", "需辨識史料作者、目的與缺漏，不能把單一見證當成全體經驗。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-hist-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [{"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"} for publisher, url, locator in SOURCES],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred three unit samples", "Six hundred six unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
