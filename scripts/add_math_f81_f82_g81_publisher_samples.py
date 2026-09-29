#!/usr/bin/env python3
"""Record independent publisher evidence for F-8-1, F-8-2 and G-8-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/"implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES={
 "nani":("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-8-3.pdf","卓蘭高中附設國中 113 學年度八年級第一學期南一版數學課程計畫；F-8-1／F-8-2 函數章與 G-8-1 畢氏定理連接坐標距離的欄位"),
 "kanghsuan":("https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak01WHpVNE16TTJNVFZmT0RRek9Ua3VjR1Jt&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4PP5414HGJGA0VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110","大豐國中公立校方康軒版八年級數學課程計畫；F-8-1／F-8-2 函數與圖形及 G-8-1 坐標距離的學習內容欄位"),
 "hanlin":("https://fsjh.chc.edu.tw/open_files_download/%262%2699%26100%26113%26115","福興國中公立校方翰林版八年級數學課程計畫；一次函數圖形、生活應用與 G-8-1 坐標兩點距離的教學與評量定位"),
}
UNITS={
 "F-8-1":("一次函數",["由對應關係理解函數", "常數函數 y=c 與一次函數 y=ax+b", "用生活兩量關係建立函數模型"],["輸入輸出表", "文字關係與代數式", "常數與一次變化的比較"],["紙筆測驗","口頭回答","討論","作業"],["南一以對應關係避免先引入抽象 f(x)；康軒把函數定義與生活資料關係並列；翰林以線型函數問題和兩點資料銜接表示法。"]),
 "F-8-2":("一次函數的圖形",["常數函數圖形", "一次函數直線圖形", "由斜率／截距或已知點解讀生活變化"],["表格、坐標點與直線", "截距與變化方向", "圖形和情境敘述互譯"],["紙筆測驗","小組討論","口頭回答","作業"],["南一把函數圖形與應用分兩週操作；康軒安排圖形描繪與資料解讀；翰林以已知兩點求線型函數並判讀圖形情境。"]),
 "G-8-1":("直角坐標系上兩點距離公式",["同水平／鉛垂距離", "由畢氏定理推導坐標兩點距離", "用距離公式處理生活位置問題"],["坐標平面與直角三角形", "水平、垂直差量", "公式、圖形與單位回查"],["紙筆測驗","口頭回答","操作","作業"],["南一明列由畢氏定理建構距離公式；康軒把公式與生活情境及坐標圖形連接；翰林以坐標平面兩點距離作為畢氏定理的應用與評量。"]),
}
def make(code,cfg):
 title,concepts,reps,assess,diffs=cfg; sources=[]
 for pub,(url,loc) in SOURCES.items():
  sources.append({"publisher":pub,"sourceUrl":url,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":f"{loc}；{code}：{title} 的概念、表徵與評量定位；核讀 2026-09-20。","accessedAt":"2026-09-20","observedConcepts":concepts,"observedRepresentations":reps,"observedAssessment":assess,"licenseBoundary":"只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。"})
 return {"lessonId":f"lesson-math-content-{code.lower()}","title":f"{code}：{title}","evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":sources,"fusionReview":{"commonCore":concepts,"differencesToReview":diffs,"originalSynthesisBoundary":"本樣本只記錄三筆公立學校章節級證據；正文、例題、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
data=json.loads(REPORT.read_text(encoding="utf-8")); existing={x["lessonId"] for x in data["units"]}
for code,cfg in UNITS.items():
 lid=f"lesson-math-content-{code.lower()}"
 if lid not in existing:data["units"].append(make(code,cfg))
data["unitCount"]=len(data["units"]); data["updatedAt"]="2026-09-20"; REPORT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
bp=ROOT/"implementation/reports/blockers.json"; blockers=json.loads(bp.read_text(encoding="utf-8"))
for b in blockers.get("blockers",[]):
 r=b.get("reason")
 if isinstance(r,str) and "unit samples" in r:b["reason"]=re.sub(r"Three hundred [a-z-]+ unit samples","Three hundred sixty-four unit samples",r)
bp.write_text(json.dumps(blockers,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"unitCount":data["unitCount"],"added":list(UNITS)},ensure_ascii=False))
