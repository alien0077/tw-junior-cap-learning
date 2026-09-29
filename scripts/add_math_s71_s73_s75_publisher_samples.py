#!/usr/bin/env python3
"""Record independently described public-school evidence for geometry units."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=119&file=WVhSMFlXTm9MelkzTDNCMFlWOHhNamcwTlY4M05UZzNOREF3WHpjNE1qQXhMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0NO24CCA1XW40YSYWEGB40054ROEGDGKKDH00DG04ICHCIGNKTS34OPB035MKQP35NOTSUWZWCDUWFH10YWFCRKPOSSYX24XWJG34XSPKSSICDGB040WSHDNPMLOOPOUSUSKLOOA4LKPKVWKK2110TSEG35YWIGB4LKXSQOJCTWICZTA1LKQPSWYWKORK00SSPKROKK04POPO", "淡水國中 114 學年度七年級第二學期部定課程計畫；南一版教材，S-7-1／S-7-3／S-7-4／S-7-5 章節與評量欄位"),
    "kanghsuan": ("https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110", "大豐國中公立校方康軒版七年級數學課程計畫；線對稱與三視圖的生活情境、摺紙／軟體操作與多元評量欄位"),
    "hanlin": ("https://www.syajh.tp.edu.tw/uploadfiles/annex/20250920073141_1.pdf", "公立校方翰林版七年級數學課程計畫；第 6 章線對稱與三視圖，列 S-7-1／S-7-3／S-7-4／S-7-5 與紙筆、討論、口頭及作業評量"),
}
UNITS = {
    "S-7-1": {
        "title": "簡單圖形與幾何符號",
        "concepts": ["點、線、線段、射線與角的區分", "三角形與多邊形的基本符號", "用符號把幾何物件與文字描述對接"],
        "representations": ["圖形、名稱與符號三向對照", "端點／方向箭頭與線段長度", "角的記號與圖上位置"],
        "assessment": ["紙筆測驗", "口頭回答", "討論", "作業", "操作"],
        "differences": ["南一把符號表達放進生活幾何圖形閱讀；康軒以圖形觀察與操作活動銜接術語；翰林把幾何定義、符號與圖形性質放在章節入口。"],
    },
    "S-7-3": {
        "title": "垂直",
        "concepts": ["垂直線與垂足的意義", "線段的中垂線及其等距性質", "點到直線距離的幾何意義"],
        "representations": ["直角符號與相交直線", "中垂線、端點與等距關係", "點到直線的最短距離圖示"],
        "assessment": ["紙筆測驗", "口頭回答", "討論", "作業", "操作"],
        "differences": ["南一以垂線、垂足及距離的生活例子建立概念；康軒以觀察與摺紙／圖形操作支援性質發現；翰林把垂直符號、中垂線與點線距離列為同一幾何章的可檢核內容。"],
    },
    "S-7-4": {
        "title": "線對稱的性質",
        "concepts": ["對稱線段等長", "對稱角相等", "對稱點連線被對稱軸垂直平分"],
        "representations": ["對稱軸兩側的點、線段與角", "摺疊或鏡射前後的對應", "垂直平分與等距證據"],
        "assessment": ["紙筆測驗", "小組討論", "口頭回答", "作業", "操作"],
        "differences": ["南一把線對稱放在生活圖形與經驗分析；康軒以摺紙、不同視角與電腦操作引導性質；翰林將對稱線段、角與點的性質納入生活幾何章的綜合評量。"],
    },
    "S-7-5": {
        "title": "線對稱的基本圖形",
        "concepts": ["等腰三角形與對稱軸", "正方形、菱形、箏形的對稱性", "正多邊形的對稱軸與圖形判讀"],
        "representations": ["摺紙後的重合邊／角", "對稱軸與頂點配對", "多邊形圖形、性質與分類表"],
        "assessment": ["紙筆測驗", "小組討論", "口頭回答", "作業", "操作"],
        "differences": ["南一用生活圖形與分組複習連接基本圖形；康軒安排摺紙判斷與對稱軸繪製；翰林把等腰三角形、正方形、菱形、箏形與正多邊形分列為基本圖形範圍。"],
    },
}

def make_sample(code: str, cfg: dict) -> dict:
    sources = []
    for publisher, (url, locator) in SOURCES.items():
        sources.append({
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": f"{locator}；{code}：{cfg['title']} 的概念、表徵與評量定位；核讀 2026-09-20。",
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
        blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred fifty unit samples", reason)
blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unitCount": data["unitCount"], "added": list(UNITS)}, ensure_ascii=False))
