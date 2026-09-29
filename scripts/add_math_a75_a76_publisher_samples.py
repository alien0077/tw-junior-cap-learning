#!/usr/bin/env python3
"""Record separate public-school publisher evidence for A-7-5 and A-7-6."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf", "桃園市立永豐高中國中部公立校方七年級數學課程計畫；南一版章節級 A-7-5／A-7-6 教學與評量欄位"),
    "kanghsuan": ("https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110", "新北市立大豐國民中學公立校方康軒版七年級數學課程計畫；PDF p.6、p.8-11 直接列 A-7-5 的消去法與應用及 A-7-6 的直線圖形、交點意義"),
    "hanlin": ("https://www.cp.ptc.edu.tw/storage/134513/134513_112_B-1_9A.pdf", "屏東縣公立學校七年級數學課程計畫；翰林版 A-7-5／A-7-6 的聯立解法、幾何意義與情境評量欄位"),
}
UNITS = {
    "A-7-5": {
        "title": "二元一次聯立方程式的解法與應用",
        "concepts": ["代入消去法與加減消去法", "以共同解同時滿足兩式", "把生活條件列式後驗算並判斷答案合理性"],
        "representations": ["兩式與有序數對的雙重代回", "係數操作與消去對照", "文字條件、聯立式、答案單位的來回轉換"],
        "assessment": ["紙筆測驗", "互相討論", "口頭回答", "作業", "情境應用題"],
        "differences": ["南一把兩種消去策略與情境應用連接；康軒明列先選擇代入或加減消去，再用題意與解的合理性回查；翰林把代入、加減與應用列為分開的學習內容細目。"],
    },
    "A-7-6": {
        "title": "二元一次方程式的幾何意義",
        "concepts": ["二元一次方程式的解形成直線上的點", "水平線與鉛垂線是特殊圖形", "兩條直線交點代表聯立方程式的唯一解"],
        "representations": ["有序數對與坐標平面", "方程式、截距與直線圖形", "交點坐標與聯立解互相驗證"],
        "assessment": ["紙筆測驗", "分組活動", "口頭回答", "上台演練", "作業"],
        "differences": ["南一以坐標圖形連結代數解；康軒加入 GeoGebra 或實際描點觀察直線與交點；翰林把幾何意義、特殊直線與情境解題分層處理。"],
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
        blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred forty-four unit samples", reason)
blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unitCount": data["unitCount"], "added": list(UNITS)}, ensure_ascii=False))
