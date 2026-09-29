#!/usr/bin/env python3
"""Record three public-school publisher-linked chapter records for N-9-1."""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": (
        "https://course.cyc.edu.tw/upfile/course112/sub1/15343601527825912.pdf",
        "嘉義縣大吉國中 112 學年度九年級數學領域南一版；PDF p.105 的第一章比例線段與相似形 1-1 連比，列 N-9-1、連比意義與連比例式。",
    ),
    "kanghsuan": (
        "https://course.cyc.edu.tw/upfile/course114/sub1/15939629187359088.pdf",
        "嘉義縣永慶高中國中部 114 學年度九年級數學科康軒版；PDF p.1 的第一章相似形 1-1 連比，列 N-9-1、共同倍數、連比例式與應用。",
    ),
    "hanlin": (
        "https://course.cyc.edu.tw/upfile/course111/sub1/15080292518292953.pdf",
        "嘉義縣忠和國中 111 學年度九年級數學領域翰林版；PDF p.83 的第一章相似形與三角比 1-1 連比，列 n-IV-4 與連比學習內容。",
    ),
}

CONCEPTS = ["連比的記錄與最簡整數比", "由兩個比對齊共同量求三量連比", "連比例式、比例鏈與生活應用"]
REPRESENTATIONS = ["a:b:c 比例記號", "共同倍數 k 與三欄份數表", "情境量、代數式與回代檢核"]
ASSESSMENT = ["口頭回答", "討論", "作業", "操作", "紙筆測驗"]

def make_record():
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
            "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方式，不複製教材、例題、題目或答案。",
        })
    return {
        "lessonId": "lesson-math-content-n-9-1",
        "title": "N-9-1：連比",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": sources,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一資料以章節與連比意義、最簡整數比及應用呈現。",
                "康軒資料明列共同倍數、連比例式與情境應用。",
                "翰林資料將連比放在相似形與三角比章的起點，並連結 n-IV-4。",
            ],
            "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；正文、例題、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
        },
    }

data = json.loads(REPORT.read_text(encoding="utf-8"))
existing = {x["lessonId"] for x in data["units"]}
added = []
if "lesson-math-content-n-9-1" not in existing:
    data["units"].append(make_record())
    added.append("N-9-1")
data["unitCount"] = len(data["units"])
data["updatedAt"] = "2026-09-20"
REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

bp = ROOT / "implementation/reports/blockers.json"
blockers = json.loads(bp.read_text(encoding="utf-8"))
for blocker in blockers.get("blockers", []):
    reason = blocker.get("reason")
    if isinstance(reason, str) and "unit samples" in reason:
        blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred sixty-nine unit samples", reason)
bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))
