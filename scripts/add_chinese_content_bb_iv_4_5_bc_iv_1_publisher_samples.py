#!/usr/bin/env python3
"""Record independent public-school publisher evidence for Chinese Bb-IV-4/5 and Bc-IV-1."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; REPORT=ROOT/"implementation/reports/publisher-chapter-evidence-samples.json"
NANI="https://www.tyjh.tyc.edu.tw/uploads/1628566893476Cy21aKmg.pdf"
KANG="https://course.tn.edu.tw/course/114J%E9%87%91%E5%9F%8E%E5%9C%8B%E4%B8%ADC5-1%E9%A0%98%E5%9F%9F%E5%AD%B8%E7%BF%92%E8%AA%B2%E7%A8%8B%28%E8%AA%BF%E6%95%B4%29%E8%A8%88%E7%95%AB%E6%99%AE%E9%80%9A%E7%8F%AD%E5%85%AB%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%870718155545.pdf"
HANLIN="https://www.chjh.tyc.edu.tw/uploads/neilfilefolder/20file/file/196_69_511%E6%99%AE%E9%80%9A%E7%8F%AD%E5%90%84%E9%A0%98%E5%9F%9F%E7%A7%91%E7%9B%AE%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%E5%9C%8B%E6%96%87.pdf"
LICENSE="只記錄公立學校課程計畫的教材版本、章節學習重點與評量方向，不複製教材正文、例題、題目、答案或版面。"
def S(p,u,l,c,r,a):return(p,u,l,c,r,a)
SAMPLES=[
 {"lessonId":"lesson-chinese-content-bb-iv-4","title":"Bb-Ⅳ-4：直接抒情","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；以詩歌與散文辨識直接抒情的情感詞、語氣和說話位置，連結生活經驗、口語分享與寫作評量；核讀 2026-09-20。",["直接抒情由說話者明白表達感受或態度","情感強度要由詞語、語氣和文本情境判斷","個人感想需和文本明示區分"],["情感詞與語氣標記","說話者／情境／情感表","第一人稱短文"],["口語","習作","自我評量","紙筆"]),
  S("kanghsuan",KANG,"臺南市公立國中康軒版八年級課程計畫；將抒情、生活價值與文本反思結合實作、口頭、自評、習作和紙筆評量，要求說明感受來源與表達目的；核讀 2026-09-20。",["直接抒情要配合語境與溝通目的","感受表達可轉成價值思辨與生活回應","口語與書面輸出都要檢查情感是否具體"],["語氣梯度","情境—感受—目的表","抒情段落改寫"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"桃園市公立國中翰林版國文課程計畫；以新詩、自然／生命文本和主題寫作安排直接抒情、作品分享與紙筆評量；核讀 2026-09-20。",["直接抒情可和詩歌聲律、自然感受及人物經驗連結","作品分享需說明情感與語句證據","寫作能檢查情感表達是否明確而不空泛"],["情感—意象對照","朗讀與語氣觀察","主題寫作與發表"],["口語","實作","習作","紙筆／分享"]),
 ],"common":["先找明示情感、語氣與說話者，再說明情感如何服務篇章目的","直接抒情不等於任意宣告感想，仍須有語境與語句證據","寫作與口語活動要要求具體情境和可辨識的情感理由"],"diff":["南一強調情感詞、語氣與生活連結","康軒把直接抒情接到價值思辨與情境表達","翰林較突出詩歌、自然生命感受、朗讀和主題寫作"]},
 {"lessonId":"lesson-chinese-content-bb-iv-5","title":"Bb-Ⅳ-5：事件景物間接抒情","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；以敘事事件與景物描寫分析間接抒情，要求從細節、氛圍與事件轉折推論情感，並用討論、習作和紙筆評量；核讀 2026-09-20。",["間接抒情要由事件選擇、景物細節和語氣推論","同一景物在不同情境可能承擔不同情感","情感推論不能脫離敘事轉折"],["事件／景物／情感鏈","氛圍詞語標記","景物改寫與效果說明"],["討論","習作","自我評量","紙筆"]),
  S("kanghsuan",KANG,"臺南市公立國中康軒版八年級課程計畫；把自然、生命、環境和敘事文本放入價值思辨，採實作、口頭、自評、習作與紙筆評量檢查描寫如何傳情；核讀 2026-09-20。",["要先描述可見細節，再推論作者態度","景物與事件需和人物選擇或公共價值連結","改寫可測試替換細節後情感效果是否改變"],["細節—效果配對","人物行動與景物對照","敘事片段改寫"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"桃園市公立國中翰林版國文課程計畫；以敘述事件和描寫景物的間接抒情連結自然、生命與社群文本，安排主題寫作、口語分享和紙筆評量；核讀 2026-09-20。",["間接抒情要比較事件、景物與情感的層次","細節安排可讓讀者感受而非直接告知","作品要提出語句證據並說明情感轉折"],["事件—景物—情感三欄表","敘述與描寫切換標記","主題寫作與分享"],["學習單","口語表達","主題寫作","紙筆"]),
 ],"common":["先列出事件或景物的具體證據，再推論情感，不以情緒標籤代替分析","間接抒情的效果在於讓讀者從選材、氛圍和轉折感受態度","改寫題要說明替換細節如何改變情感與篇章效果"],"diff":["南一強調事件、景物與情感推論鏈","康軒加入環境、生命和價值思辨的傳情分析","翰林突出自然、社群文本和主題寫作的遷移"]},
 {"lessonId":"lesson-chinese-content-bc-iv-1","title":"Bc-Ⅳ-1：邏輯客觀理性說明","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；以科學知識、產品、環境、制度與演講等說明文本，檢查資料組織、因果、定義、客觀語氣和報告表達；核讀 2026-09-20。",["說明文要以明確對象、分類、定義和因果組織資訊","客觀語氣仍需檢查資料來源與推論界線","報告和圖表能把說明轉成可理解結構"],["說明文結構圖","事實／解釋／推論分層","產品或制度報告"],["口頭提問","學習單","小組討論","分組報告"]),
  S("kanghsuan",KANG,"臺南市公立國中康軒版八年級課程計畫；以說明文本、演講、科技資訊和問題解決訓練邏輯、客觀、理性表達，採實作、口頭、自評、習作和紙筆評量；核讀 2026-09-20。",["說明要區分觀察資料、解釋和主張","資訊統整需保留來源與證據強度","口頭演講與書面說明都要有清楚組織"],["資料—解釋—結論卡","說明段落重組","演講／產品說明任務"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"桃園市公立國中翰林版課程計畫；以說明、議論與科技文化文本安排資料蒐集、組織、視覺化、報告和作品分享，檢核客觀說明與讀者理解；核讀 2026-09-20。",["客觀說明要看資訊選擇、組織和讀者需求","資料整理與視覺化不能掩蓋證據不足","報告需能回答問題並說明資料限制"],["資訊來源表","圖表與文字互證","主題探索報告"],["口語","實作","習作","定期紙筆／專題"]),
 ],"common":["先界定說明對象與目的，再用定義、分類、因果或程序組織資訊","客觀不是沒有立場，而是把事實、解釋、推論和限制分開","評量要要求來源、資料組織、結論和讀者可理解性"],"diff":["南一偏重說明文本結構、資料層次與報告","康軒把邏輯說明接到演講、科技資訊與問題解決","翰林較突出資料蒐集、視覺化、報告和限制說明"]},
]
def main():
 d=json.loads(REPORT.read_text(encoding="utf-8"));existing={x.get("lessonId") for x in d["units"]};added=[]
 for s in SAMPLES:
  rec={"lessonId":s["lessonId"],"title":s["title"],"evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":[{"publisher":p,"sourceUrl":u,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":l,"accessedAt":"2026-09-20","observedConcepts":c,"observedRepresentations":r,"observedAssessment":a,"licenseBoundary":LICENSE}for p,u,l,c,r,a in s["sources"]],"fusionReview":{"commonCore":s["common"],"differencesToReview":s["diff"],"originalSynthesisBoundary":"本樣本只記錄三筆可追溯的公立學校章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
  if rec["lessonId"] not in existing:d["units"].append(rec);added.append(rec["lessonId"])
 d["unitCount"]=len(d["units"]);d["updatedAt"]="2026-09-20";REPORT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 bp=ROOT/"implementation/reports/blockers.json";b=json.loads(bp.read_text(encoding="utf-8"))
 for x in b.get("blockers",[]):
  if isinstance(x.get("reason"),str)and "unit samples"in x["reason"]:x["reason"]=re.sub(r"Four hundred twenty-nine unit samples","Four hundred thirty-two unit samples",x["reason"])
 bp.write_text(json.dumps(b,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps({"unitCount":d["unitCount"],"added":added},ensure_ascii=False))
if __name__=="__main__":main()
