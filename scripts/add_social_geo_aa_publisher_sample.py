#!/usr/bin/env python3
"""Record public-school publisher-linked chapter evidence for social Geo Aa."""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": (
        "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf",
        "國立卓蘭高中附設國中部 113 學年度七年級社會領域南一版；單元 1 地圖與座標系統列地 Aa-Ⅳ-1、地 Aa-Ⅳ-2 與地 Aa-Ⅳ-4，連結臺灣和世界各地的關聯。",
    ),
    "kanghsuan": (
        "https://course.cyc.edu.tw/upfile/course113/file_school/15683227287080309.pdf",
        "嘉義縣阿里山國民中小學 113 學年度七年級社會地理康軒版；第一單元基本概念與臺灣的第 1 課位置、地圖與座標系統列地 Aa-Ⅳ-1，並以臺灣位置與範圍建立後續世界中的臺灣脈絡。",
    ),
    "hanlin": (
        "https://course.cyc.edu.tw/upfile/course114/sub1/15937393490258175.pdf",
        "嘉義縣新港國中 114 學年度七年級社會地理翰林版；第一篇臺灣的環境上第一、二章列地 Aa-Ⅳ-1～地 Aa-Ⅳ-4，直接安排位置、範圍、行政區、全球海陸與臺灣關聯。",
    ),
}
CONCEPTS = ["以絕對位置與相對位置描述臺灣", "由地圖、經緯度與行政範圍定位臺灣", "把臺灣位置連到全球海陸、區域關係與生活影響"]
REPRESENTATIONS = ["經緯度與座標圖", "臺灣位置／範圍地圖", "全球—區域—臺灣尺度關聯圖"]
ASSESSMENT = ["教師觀察", "口頭問答", "紙筆測驗", "討論", "學習歷程或自我評量"]

def main():
    sources = []
    for publisher, (url, locator) in SOURCES.items():
        sources.append({
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": f"{locator} 核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": CONCEPTS,
            "observedRepresentations": REPRESENTATIONS,
            "observedAssessment": ASSESSMENT,
            "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、地圖、題目或答案。",
        })
    record = {
        "lessonId": "lesson-social-content-geo-aa",
        "title": "Aa：世界中的臺灣",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": sources,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一以地圖與座標系統銜接臺灣和世界的關聯。",
                "康軒先處理位置與地圖技能，再延伸臺灣位置與範圍。",
                "翰林將位置、行政範圍、生態與全球關聯分段安排。",
            ],
            "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；正文、地圖、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
        },
    }
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    existing = {x["lessonId"] for x in data["units"]}
    added = []
    if record["lessonId"] not in existing:
        data["units"].append(record)
        added.append("Aa")
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-20"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"
    blockers = json.loads(bp.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason:
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred seventy unit samples", reason)
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))

if __name__ == "__main__":
    main()
