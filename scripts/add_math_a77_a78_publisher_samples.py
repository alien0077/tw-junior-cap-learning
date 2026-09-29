#!/usr/bin/env python3
"""Record separate public-school publisher evidence for A-7-7 and A-7-8."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf", "桃園市立永豐高中國中部公立校方七年級數學課程計畫；南一版一元一次不等式章節與評量欄位"),
    "kanghsuan": ("https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110", "新北市立大豐國民中學公立校方康軒版七年級數學課程計畫；PDF p.16-19 列 A-7-7／A-7-8、文字列式、數線範圍、負乘反向與評量"),
    "hanlin": ("https://www.cp.ptc.edu.tw/storage/134505/134505_113_B-21_7A.pdf", "屏東縣公立學校七年級數學課程計畫；翰林版一元一次不等式的意義、數線表示與應用評量欄位"),
}
UNITS = {
    "A-7-7": {
        "title": "一元一次不等式的意義",
        "concepts": ["不等號表達上下限或不等關係", "從具體情境列出一元一次不等式", "分辨一元與一次並解讀不等式語句"],
        "representations": ["生活語句與不等號", "條件範圍與數線方向", "未知數、單位與限制條件的對應"],
        "assessment": ["紙筆測驗", "口頭回答", "互相討論", "作業", "情境列式"],
        "differences": ["南一以情境條件與不等號語句互譯作為入口；康軒以交通標誌、票價或碳足跡等生活資料建立不等關係；翰林把符號理解、列式與範圍表達拆成可觀察的學習目標。"],
    },
    "A-7-8": {
        "title": "一元一次不等式的解與應用",
        "concepts": ["解是符合不等式的數值集合", "在數線上用端點與方向表示解集", "解生活應用題並檢查負數乘除造成的方向改變"],
        "representations": ["不等式解與數線陰影／箭頭", "等量操作與不等號方向", "情境限制、解集與答案單位三者回查"],
        "assessment": ["紙筆測驗", "互相討論", "口頭回答", "作業", "生活應用題"],
        "differences": ["南一強調解集的數線表達與情境應用；康軒明列同乘負數時方向反轉並安排文字列式與上下限；翰林以數線標示、求解與應用問題分層檢核。"],
    },
}

def make_sample(code: str, cfg: dict) -> dict:
    sources = []
    for publisher, (url, base_locator) in SOURCES.items():
        sources.append({
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": f"{base_locator}；{code}：{cfg['title']} 的概念、表徵與評量定位；核讀 2026-09-20。",
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
        data["units"].append(make_sample(code, cfg))
data["unitCount"] = len(data["units"])
data["updatedAt"] = "2026-09-20"
REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
blocker_path = ROOT / "implementation/reports/blockers.json"
blockers = json.loads(blocker_path.read_text(encoding="utf-8"))
for blocker in blockers.get("blockers", []):
    reason = blocker.get("reason")
    if isinstance(reason, str) and "unit samples" in reason:
        blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred forty-six unit samples", reason)
blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unitCount": data["unitCount"], "added": list(UNITS)}, ensure_ascii=False))
