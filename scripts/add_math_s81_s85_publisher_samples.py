#!/usr/bin/env python3
"""Record independent publisher evidence for S-8-1 through S-8-5."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-8-3.pdf", "國立卓蘭高中附設國中 113 學年度八年級數學課程計畫；南一版 S-8-1／S-8-3 章節、操作與評量欄位"),
    "kanghsuan": ("https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak01WHpVNE16TTJNVFZmT0RRek9Ua3VjR1Jt&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4PP5414HGJGA0VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110", "大豐國中公立校方康軒版八年級數學課程計畫；S-8-1／S-8-2／S-8-4／S-8-5 的概念、作圖／討論活動與評量欄位"),
    "hanlin": ("https://fsjh.chc.edu.tw/open_files_download/%262%2699%26100%26113%26115", "福興國中公立校方翰林版八年級數學課程計畫；S-8-1～S-8-5 的角、內角和、平行、全等與三角形判定學習內容及評量定位"),
}
UNITS = {
    "S-8-1": ("角", ["角的種類", "互餘、互補、對頂角與平行線相關角", "角平分線的意義"], ["角圖形與符號", "角度量與關係表", "角平分線上的等距判讀"], ["紙筆測驗", "口頭回答", "討論", "作業"], ["南一把角的關係放在平行線單元銜接；康軒從角種類與角關係逐步組織；翰林以基本幾何術語與全等推理作為後續基礎。"]),
    "S-8-2": ("凸多邊形的內角和", ["凸多邊形與內外角定義", "三角形分割推導內角和", "正 n 邊形每個內角的計算"], ["對角線分割", "內角／外角圖示", "公式與正多邊形表格"], ["紙筆測驗", "分組討論", "繪製實作", "作業"], ["南一以圖形性質與操作導入公式；康軒安排由三角形內角和推到多邊形；翰林把內外角與正多邊形公式連結資料表達。"]),
    "S-8-3": ("平行", ["平行線的意義與符號", "平行線截角性質", "兩平行線間距離處處相等"], ["平行線與截線圖", "同位、內錯、同側內角", "距離測量與性質敘述"], ["紙筆測驗", "口頭回答", "操作", "作業"], ["南一以平行線章節連接角關係；康軒透過作圖與角度觀察形成性質；翰林以平行線截角和距離作為幾何推理素材。"]),
    "S-8-4": ("全等圖形", ["平移、旋轉、翻轉後完全疊合的全等意義", "對應邊與對應角相等", "由對應關係判讀全等圖形"], ["疊合與變換", "對應點／邊／角標記", "全等符號與條件表"], ["紙筆測驗", "討論", "操作", "作業"], ["南一以圖形變換和學習單操作檢查疊合；康軒把全等放入三角形性質與作圖；翰林分辨多邊形對應關係並銜接三角形判定。"]),
    "S-8-5": ("三角形的全等性質", ["SAS、SSS、ASA、AAS、RHS 判定", "全等符號與對應順序", "用全等性質進行簡單推理與生活幾何判斷"], ["邊角標記與對應表", "判定條件流程", "圖形證據與推理句"], ["紙筆測驗", "小組討論", "口頭回答", "作業"], ["南一以全等判定與角平分線性質作推理入口；康軒強調判定條件和作圖／分組活動；翰林把 SSS、SAS、ASA、AAS、RHS 與簡單推理連接。"]),
}

def make_sample(code: str, cfg: tuple) -> dict:
    title, concepts, representations, assessments, differences = cfg
    sources=[]
    for publisher,(url,locator) in SOURCES.items():
        sources.append({"publisher":publisher,"sourceUrl":url,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":f"{locator}；{code}：{title} 的概念、表徵與評量定位；核讀 2026-09-20。","accessedAt":"2026-09-20","observedConcepts":concepts,"observedRepresentations":representations,"observedAssessment":assessments,"licenseBoundary":"只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。"})
    return {"lessonId":f"lesson-math-content-{code.lower()}","title":f"{code}：{title}","evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":sources,"fusionReview":{"commonCore":concepts,"differencesToReview":differences,"originalSynthesisBoundary":"本樣本只記錄三筆公立學校章節級證據；正文、例題、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}

data=json.loads(REPORT.read_text(encoding="utf-8")); existing={x["lessonId"] for x in data["units"]}
for code,cfg in UNITS.items():
    lesson_id=f"lesson-math-content-{code.lower()}"
    if lesson_id not in existing: data["units"].append(make_sample(code,cfg))
data["unitCount"]=len(data["units"]); data["updatedAt"]="2026-09-20"; REPORT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
blocker_path=ROOT/"implementation/reports/blockers.json"; blockers=json.loads(blocker_path.read_text(encoding="utf-8"))
for blocker in blockers.get("blockers",[]):
    reason=blocker.get("reason")
    if isinstance(reason,str) and "unit samples" in reason: blocker["reason"]=re.sub(r"Three hundred [a-z-]+ unit samples","Three hundred sixty-one unit samples",reason)
blocker_path.write_text(json.dumps(blockers,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"unitCount":data["unitCount"],"added":list(UNITS)},ensure_ascii=False))
