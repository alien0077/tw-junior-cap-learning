#!/usr/bin/env python3
"""Record separate publisher-scope evidence for A-7-2 and A-7-3."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9Mekk0TDNCMFlWOHhNakU0Tmw4ek16a3pPVGs0WHpJM01qZzRMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0DCNKCCQLOO40QKTSST54WSLKUSSSROPOIHKK2004GDLOQONKTSMOOPB0FHMPQPMPNOTSUWZWWXVWFH10YWFCSSWUX25HCA0UWIGVWKO40XSUSB040MPTXGDTWA0ZWUSOPTWFGTS45QKNOKK21HHDGB0JC24KK14WTIGYSEG14WSMLID30B514YWRKA434DCDGA0WWQOPP1000ZSIGMOIGDGJDLO", "淡水國中 114 學年度七年級第一學期部定課程計畫；南一版教材與 A-7-2／A-7-3 學習內容、教學進度及評量欄位"),
    "kanghsuan": ("https://www.cshs.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=823&file=WVhSMFlXTm9MelEwTDNCMFlWOHhOamcxT0Y4ME9EYzFOamN5WHpRd01UWTRMbkJrWmc9PQ%3D%3D&fname=0054RPA0IC44VXMPED04ROGDVW30B4ICQOQK4020UT0510TSYSA4YS54WWECTTOKVWPOXT154404A0WSST14MOICB0RKMP1444VXXWA0SWMKGHFGUSCCYWFC0040DDKKB0LKUWLOVWTWWSB0403541GDQPMLA0B4ZSFGOOLK30DGRKPO2125HC04MOIGTW14JDRLOPEGFHMOUTXT30FCUW30JGLLUSDC0150RKKKXX0150HGWTHGDCTW25LKFGB0UW10GGFDA0VSKPNO1145", "金山國中 113 學年度七年級第一學期部定課程計畫；康軒版第一冊與 A-7-2／A-7-3 的列式、求解、驗算及應用安排"),
    "hanlin": ("https://www.msjh.tp.edu.tw/uploads/1755572578742THrRJJpw.pdf", "民生國中 114 學年度七年級資源班數學課程計畫；翰林版七年級數學與 A-7-2-1／A-7-2-2、A-7-3-1／A-7-3-2／A-7-3-4 學習內容欄位"),
}
UNITS = {
    "A-7-2": {
        "title": "一元一次方程式的意義",
        "concepts": ["等式與未知數的角色", "從具體情境列出一元一次方程式", "以代入判斷數值是否為方程式的解"],
        "representations": ["文字情境、數量關係與方程式", "等號兩側的平衡表徵", "候選值代入驗證"],
        "assessment": ["口頭回答", "紙筆測驗", "作業", "情境列式"],
        "differences": ["南一從情境列式與先備知識銜接未知數；康軒以章節進度連接代數式與方程式；翰林把『理解方程式及其解』與『從情境列式』拆成細目。"],
    },
    "A-7-3": {
        "title": "一元一次方程式的解法與應用",
        "concepts": ["等量公理維持等式關係", "移項法則與解的一致性", "代回驗算並把解放回生活情境"],
        "representations": ["等式兩邊同步運算", "移項前後的符號變化", "情境條件、方程式與答案合理性三者對照"],
        "assessment": ["紙筆測驗", "口頭說明", "作業", "生活應用題"],
        "differences": ["南一強調由已學代數式與先備知識引導求解；康軒以等量公理、移項與生活情境分段練習；翰林將等量公理、移項及應用問題分列，並保留口語或實作檢核。"],
    },
}

def sample(code: str, cfg: dict) -> dict:
    sources = []
    for publisher, (url, locator) in SOURCES.items():
        sources.append({
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": f"{locator}；{code}：{cfg['title']} 的概念與評量定位；核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": cfg["concepts"],
            "observedRepresentations": cfg["representations"],
            "observedAssessment": cfg["assessment"],
            "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。",
        })
    return {
        "lessonId": f"lesson-math-content-{code.lower()}",
        "title": f"{code}：{cfg['title']}",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": sources,
        "fusionReview": {
            "commonCore": cfg["concepts"],
            "differencesToReview": cfg["differences"],
            "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；正文、例題、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
        },
    }

data = json.loads(REPORT.read_text(encoding="utf-8"))
existing = {item["lessonId"] for item in data["units"]}
for code, cfg in UNITS.items():
    lesson_id = f"lesson-math-content-{code.lower()}"
    if lesson_id not in existing:
        data["units"].append(sample(code, cfg))
data["unitCount"] = len(data["units"])
data["updatedAt"] = "2026-09-20"
REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
blocker_path = ROOT / "implementation/reports/blockers.json"
blockers = json.loads(blocker_path.read_text(encoding="utf-8"))
for blocker in blockers.get("blockers", []):
    reason = blocker.get("reason")
    if isinstance(reason, str) and "unit samples" in reason:
        blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred forty-two unit samples", reason)
blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unitCount": data["unitCount"], "added": list(UNITS)}, ensure_ascii=False))
