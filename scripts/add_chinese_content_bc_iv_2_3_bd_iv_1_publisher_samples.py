#!/usr/bin/env python3
"""Record independent public-school publisher evidence for Chinese Bc-IV-2/3 and Bd-IV-1."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; REPORT=ROOT/"implementation/reports/publisher-chapter-evidence-samples.json"
NANI="https://www.tyjh.tyc.edu.tw/uploads/1628566893476Cy21aKmg.pdf"
KANG="https://www.kusjh.kh.edu.tw/files/shares/%E6%95%99%E5%8B%99%E8%99%95/113%E5%9C%8B%E4%B8%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/%E4%BC%8D%E3%80%81%E9%A0%98%E5%9F%9F%E5%AD%B8%E7%BF%92%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%28%E5%85%AB%E5%B9%B4%E7%B4%9A%29.pdf"
HANLIN="https://www.chjh.tyc.edu.tw/uploads/neilfilefolder/20file/file/196_69_511%E6%99%AE%E9%80%9A%E7%8F%AD%E5%90%84%E9%A0%98%E5%9F%9F%E7%A7%91%E7%9B%AE%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%E5%9C%8B%E6%96%87.pdf"
LICENSE="只記錄公立學校課程計畫的教材版本、章節學習重點與評量方向，不複製教材正文、例題、題目、答案或版面。"
def S(p,u,l,c,r,a):return(p,u,l,c,r,a)
SAMPLES=[
 {"lessonId":"lesson-chinese-content-bc-iv-2","title":"Bc-Ⅳ-2：描述列舉因果問題解決比較分類定義","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；以說明與議論文本安排描述、列舉、因果、問題解決、比較、分類和定義，連結報告、討論、習作和寫作；核讀 2026-09-20。",["寫作手法要對應說明目的與資訊關係","因果與問題解決需分清現象、原因、方案和結果","比較分類必須交代共同標準"],["手法—目的配對","因果／問題解決流程圖","分類標準與比較表"],["口頭提問","學習單","習作","分組報告"]),
  S("kanghsuan",KANG,"高雄市公立國中康軒版課程計畫；以說明文、演講與議題文本實作描述、比較、分類、定義和問題解決，採實作、口頭、自評、習作和紙筆評量；核讀 2026-09-20。",["手法選擇要由讀者需求與文本目的決定","分類需維持互斥或可重疊的界線說明","寫作輸出要檢查步驟、證據與結論是否相接"],["讀者／目的／手法表","方案比較矩陣","說明段落重組與寫作"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"桃園市公立國中翰林版課程計畫；將描述、列舉、因果、比較、分類等手法連結詩文、文化文本、資料整理與主題探索報告；核讀 2026-09-20。",["同一文本可組合多種說明手法但各有功能","文化與生活資料要說清楚分類依據和比較尺度","報告能檢驗手法是否服務主旨"],["段落手法標註","多尺度比較表","主題探索報告"],["口語","實作","習作","紙筆／專題"]),
 ],"common":["先判斷寫作目的與資訊關係，再選擇描述、因果、分類、比較或定義","每種手法都要有可檢查的標準、步驟或關係，不能只貼標籤","遷移活動要讓學生用新資料重組說明並說明選擇理由"],"diff":["南一偏重說明手法與報告／寫作的功能對應","康軒突出讀者需求、問題解決與多元實作","翰林將手法結合文化資料、尺度比較與主題探索"]},
 {"lessonId":"lesson-chinese-content-bc-iv-3","title":"Bc-Ⅳ-3：數據圖表圖片工具列輔助","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；以科技、環境與說明文本結合資訊整理、圖表與報告，要求讀取輔助資料並檢查文字與視覺訊息的一致性；核讀 2026-09-20。",["圖表標題、單位、時間與資料範圍先於結論","圖片與文字需互相支持，不能只看視覺印象","資料解讀要分觀察、比較、推論和限制"],["圖表讀取卡","文字／圖像互證表","資料報告與圖表製作"],["學習單","小組討論","分組報告","習作"]),
  S("kanghsuan",KANG,"高雄市公立國中康軒版課程計畫；將科技資訊、說明文與演講結合檢索、統整、解釋和口頭表達，採實作、口頭、自評、習作和紙筆評量；核讀 2026-09-20。",["輔助工具要服務訊息理解而非取代文字證據","圖表判讀需確認座標、單位、比例和時間","口頭說明要把視覺資料轉成有順序的結論"],["圖表元素檢查表","數據—結論證據鏈","演講簡報任務"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"桃園市公立國中翰林版課程計畫；安排資料查找、整理與視覺化工具完成語文主題探索報告，並以口語、實作、習作、紙筆和專題檢核；核讀 2026-09-20。",["視覺化需選擇符合資料型態的圖表","來源、範圍和限制要在作品中可追溯","報告須說明圖表如何支持主旨"],["來源與資料範圍表","圖表選型比較","視覺化主題報告"],["口語","實作","習作","定期紙筆／專題"]),
 ],"common":["先核對標題、單位、時間、來源和尺度，再讀圖表或圖片訊息","觀察到的資料與推論出的結論要分層，不能把視覺印象當成證據","作品需保留來源與限制，並說明輔助資料如何支援主旨"],"diff":["南一著重文字與視覺訊息互證","康軒把圖表閱讀連到科技資訊、統整與演講","翰林較突出資料查找、圖表選型與視覺化報告"]},
 {"lessonId":"lesson-chinese-content-bd-iv-1","title":"Bd-Ⅳ-1：事實理論為論據達說服建構批判","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；以演講、議論和說明文本區分主張、事實、理論與例證，安排提問、論辯、報告、習作和寫作評量；核讀 2026-09-20。",["主張要和論據、推理關係分開辨識","事實需可核對，理論需說明適用範圍","說服、建構和批判都要回應反例或限制"],["主張—理由—證據圖","事實／觀點／理論分類","論辯與短文"],["口頭提問","分組討論","分組報告","作文"]),
  S("kanghsuan",KANG,"高雄市公立國中康軒版課程計畫；以演講與公共議題訓練檢索、統整、解釋、省思及有條理論辯，採實作、口頭、自評、習作與紙筆評量；核讀 2026-09-20。",["論證品質要看證據相關性、充分性與推理是否跳躍","多元資料整合需標出來源和觀點位置","口頭與書面論證都要回應聽眾或讀者"],["論證結構卡","來源／證據強度表","演講與反駁練習"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"桃園市公立國中翰林版課程計畫；以事實、理論和比較／比喻等論證方式處理文化、科技與公共文本，安排資料蒐集、報告、作品分享和紙筆評量；核讀 2026-09-20。",["論據選擇要服務主張而非堆疊資料","比較和比喻要交代對應關係及界線","報告需呈現資料來源、推論和可被質疑處"],["論據功能標記","比較／比喻論證對照","資料報告與批判回應"],["口語","實作","習作","定期紙筆／專題"]),
 ],"common":["先找主張，再分辨事實、理論、例證與推理，最後檢查是否真正支持結論","有效論據要有來源、相關性和充分性，不能以聲量或權威代替證明","建構或批判時需回應反例、限制與不同立場"],"diff":["南一偏重主張—論據—推理結構和論辯寫作","康軒突出資料檢索、證據強度與演講回應","翰林將論據分析延伸到文化科技文本、比較／比喻與專題報告"]},
]
def main():
 d=json.loads(REPORT.read_text(encoding="utf-8"));existing={x.get("lessonId") for x in d["units"]};added=[]
 for s in SAMPLES:
  rec={"lessonId":s["lessonId"],"title":s["title"],"evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":[{"publisher":p,"sourceUrl":u,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":l,"accessedAt":"2026-09-20","observedConcepts":c,"observedRepresentations":r,"observedAssessment":a,"licenseBoundary":LICENSE}for p,u,l,c,r,a in s["sources"]],"fusionReview":{"commonCore":s["common"],"differencesToReview":s["diff"],"originalSynthesisBoundary":"本樣本只記錄三筆可追溯的公立學校章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
  if rec["lessonId"] not in existing:d["units"].append(rec);added.append(rec["lessonId"])
 d["unitCount"]=len(d["units"]);d["updatedAt"]="2026-09-20";REPORT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 bp=ROOT/"implementation/reports/blockers.json";b=json.loads(bp.read_text(encoding="utf-8"))
 for x in b.get("blockers",[]):
  if isinstance(x.get("reason"),str)and "unit samples"in x["reason"]:x["reason"]=re.sub(r"Four hundred thirty-two unit samples","Four hundred thirty-five unit samples",x["reason"])
 bp.write_text(json.dumps(b,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps({"unitCount":d["unitCount"],"added":added},ensure_ascii=False))
if __name__=="__main__":main()
