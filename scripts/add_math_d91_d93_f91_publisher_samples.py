#!/usr/bin/env python3
"""Record independent publisher evidence for grade-nine statistics/probability/functions."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/"implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES={
 "nani":("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/378739209.pdf","卓蘭高中附設國中／公立校方南一版九年級數學課程計畫；D-9-1 統計數據分布及 F-9-1 二次函數章節定位"),
 "kanghsuan":("https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=100&file=WVhSMFlXTm9MelkzTDNCMFlWOHhNamd6T1Y4MU56WXlNRFl3WHpjNE1USXpMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0DCNKCCQLOO40QKTSST54WSLKUSSSROPOIHKK2004GDLOQONKTSMOOPB0FHMPQPMPNOTSUWZWWXVWFH10YWFCSSWUX25HCA0UWIGVWKO40XSUSB040MPTXGDTWA0ZWUSOPTWFGTS45QKNOKK21HHDGB0JC24KK14WTIGYSEG14WSMLID30B514YWRKA434DCDGA0WWQOPP1000ZSIGMOIGDGJDLO", "淡水國中 114 學年度九年級第二學期康軒版數學課程計畫；D-9-2／D-9-3 機率、樹狀圖與古典機率情境"),
 "hanlin":("https://www1.fsm.kh.edu.tw/plan/special_112/112%E8%B3%87%E6%BA%90%E7%8F%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf","高雄市公立校方翰林版第六冊數學課程計畫；F-9-1 二次函數與 D-9-1／D-9-2／D-9-3 統計與機率學習內容及評量定位"),
}
UNITS={
 "D-9-1":("統計數據的分布",["全距描述資料跨度", "四分位距描述中央資料散布", "盒狀圖呈現分布、位置與離群資料"],["排序資料與五數摘要", "盒狀圖端點／四分位數", "統計量與文字結論互譯"],["紙筆測驗","口頭回答","討論","作業"],["南一以統計數據分布安排全距、四分位距與盒狀圖；康軒把統計分布放入資料處理；翰林強調盒狀圖與資料特性的判讀。"]),
 "D-9-2":("認識機率",["機率表達不確定性", "以兩層樹狀圖列出可能結果", "把結果數與事件條件對照"],["樹狀圖分支", "樣本空間與事件", "分數／小數機率與生活情境"],["紙筆測驗","口頭回答","課堂觀察","作業"],["南一從可能結果與資料整理銜接機率；康軒明列樹狀圖與日常情境；翰林以機率和樹狀圖作為統計資料溝通活動。"]),
 "D-9-3":("古典機率",["對稱情境下的等可能結果", "銅板、骰子、撲克牌與抽球的古典機率", "探究圖釘等不具對稱物體的實驗機率"],["樣本空間列表", "等可能結果比例", "實驗次數與理論機率比較"],["紙筆測驗","口頭回答","操作","討論"],["南一以古典情境連結樣本空間；康軒同時安排對稱與不對稱物體的探究；翰林把實作、資料紀錄與機率解釋放在評量脈絡。"]),
 "F-9-1":("二次函數的意義",["二次函數關係的辨識", "從具體情境列出兩量的二次關係", "區分變數、係數與情境限制"],["情境表格與代數式", "輸入輸出對應", "數值資料與拋物線前置關係"],["紙筆測驗","口頭回答","討論","作業"],["南一以情境與代數式列出二次關係；康軒把二次函數放進機率／統計後的函數主線；翰林將具體列式、圖形與極值作連續學習脈絡。"]),
}
def make(code,cfg):
 title,concepts,reps,assess,diffs=cfg;sources=[]
 for pub,(url,loc) in SOURCES.items():
  sources.append({"publisher":pub,"sourceUrl":url,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":f"{loc}；{code}：{title} 的概念、表徵與評量定位；核讀 2026-09-20。","accessedAt":"2026-09-20","observedConcepts":concepts,"observedRepresentations":reps,"observedAssessment":assess,"licenseBoundary":"只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。"})
 return {"lessonId":f"lesson-math-content-{code.lower()}","title":f"{code}：{title}","evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":sources,"fusionReview":{"commonCore":concepts,"differencesToReview":diffs,"originalSynthesisBoundary":"本樣本只記錄三筆公立學校章節級證據；正文、例題、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
data=json.loads(REPORT.read_text(encoding="utf-8"));existing={x["lessonId"] for x in data["units"]}
for code,cfg in UNITS.items():
 lid=f"lesson-math-content-{code.lower()}"
 if lid not in existing:data["units"].append(make(code,cfg))
data["unitCount"]=len(data["units"]);data["updatedAt"]="2026-09-20";REPORT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
bp=ROOT/"implementation/reports/blockers.json";blockers=json.loads(bp.read_text(encoding="utf-8"))
for b in blockers.get("blockers",[]):
 r=b.get("reason")
 if isinstance(r,str) and "unit samples" in r:b["reason"]=re.sub(r"Three hundred [a-z-]+ unit samples","Three hundred sixty-eight unit samples",r)
bp.write_text(json.dumps(blockers,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"unitCount":data["unitCount"],"added":list(UNITS)},ensure_ascii=False))
