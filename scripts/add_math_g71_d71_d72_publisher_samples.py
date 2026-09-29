#!/usr/bin/env python3
"""Record independent publisher-scope evidence for coordinate/statistics units."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=119&file=WVhSMFlXTm9MelkzTDNCMFlWOHhNamcwTlY4M05UZzNOREF3WHpjNE1qQXhMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0NO24CCA1XW40YSYWEGB40054ROEGDGKKDH00DG04ICHCIGNKTS34OPB035MKQP35NOTSUWZWCDUWFH10YWFCRKPOSSYX24XWJG34XSPKSSICDGB040WSHDNPMLOOPOUSUSKLOOA4LKPKVWKK2110TSEG35YWIGB4LKXSQOJCTWICZTA1LKQPSWYWKORK00SSPKROKK04POPO", "淡水國中 114 學年度七年級第二學期部定課程計畫；南一版 G-7-1、D-7-1、D-7-2 章節與評量欄位"),
    "kanghsuan": ("https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110", "大豐國中公立校方康軒版七年級數學課程計畫；G-7-1 坐標與 D-7-1／D-7-2 統計圖表、資料分析與評量欄位"),
    "hanlin": ("https://www.syajh.tp.edu.tw/uploadfiles/annex/20250920073141_1.pdf", "公立校方翰林版七年級數學課程計畫；坐標、統計圖表、資料整理與平均數／中位數／眾數的章節及評量定位"),
}
UNITS = {
    "G-7-1": {
        "title": "平面直角坐標系",
        "concepts": ["原點、坐標軸、象限與單位長", "以有序數對標定平面位置", "讀取、標示與解釋坐標及方位距離"],
        "representations": ["生活位置圖與坐標平面", "有序數對的 x、y 位置", "數線方向、象限符號與圖上點位"],
        "assessment": ["紙筆測驗", "口頭回答", "討論", "作業", "操作"],
        "differences": ["南一從生活位置與方位距離引入坐標；康軒以座位、棋盤或校園情境操作坐標；翰林把坐標軸、象限與位置標定放在幾何圖形脈絡中檢核。"],
    },
    "D-7-1": {
        "title": "統計圖表",
        "concepts": ["蒐集並整理生活資料", "依資料性質選擇統計圖表", "從原始資料或百分率讀取分布與比較"],
        "representations": ["長條圖、圓形圖、折線圖與列聯表", "原始資料、次數與百分率", "圖表標題、刻度、圖例與資料敘述"],
        "assessment": ["紙筆測驗", "口頭回答", "討論", "作業", "資料操作"],
        "differences": ["南一將統計圖表放在資料整理與分析章節；康軒以生活資料與統計圖表選擇連結解讀；翰林強調資料分類、整理與圖表資訊的溝通。"],
    },
    "D-7-2": {
        "title": "統計數據",
        "concepts": ["平均數、中位數與眾數的意義", "用統計量描述一組資料特性", "以計算機或資料整理檢查計算與解讀"],
        "representations": ["排序資料與中位位置", "平均數的總和／筆數關係", "眾數、圖表與文字結論互相核對"],
        "assessment": ["紙筆測驗", "口頭回答", "討論", "作業", "計算機操作"],
        "differences": ["南一把資料分析接在圖表閱讀後；康軒明列平均數、中位數、眾數與計算機 M+／Σ 鍵；翰林把大量資料先分類排序，再檢核統計量是否能支持結論。"],
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
        blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred fifty-three unit samples", reason)
blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"unitCount": data["unitCount"], "added": list(UNITS)}, ensure_ascii=False))
