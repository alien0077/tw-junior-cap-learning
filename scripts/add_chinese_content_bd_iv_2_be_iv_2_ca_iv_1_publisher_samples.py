#!/usr/bin/env python3
"""Record independent public-school publisher evidence for Chinese Bd-IV-2/Be-IV-2/Ca-IV-1."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; REPORT=ROOT/"implementation/reports/publisher-chapter-evidence-samples.json"
NANI="https://www.pnjh.tyc.edu.tw/wwwdata/academic/plan/114/5-1-1-1.pdf"
KANG="https://www.cp.ptc.edu.tw/storage/134510/134510_112_B-1_9A.pdf"
HANLIN="https://course.cyc.edu.tw/upfile/course110/sub1/14826234423048540.pdf"
LICENSE="只記錄公立學校課程計畫的教材版本、章節學習重點與評量方向，不複製教材正文、例題、題目、答案或版面。"
def S(p,u,l,c,r,a):return(p,u,l,c,r,a)
SAMPLES=[
 {"lessonId":"lesson-chinese-content-bd-iv-2","title":"Bd-Ⅳ-2：比較比喻等論證","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；將比較、比喻等論證放入多元文本、閱讀策略與觀點表達，要求辨識對應關係、論證目的及作品評析；核讀 2026-09-20。",["比較論證要交代比較項目、標準與結論","比喻需說明本體、喻體及相似點的邊界","論證效果要回到主張與讀者理解"],["論點—比較標準表","本體／喻體／相似點卡","論證改寫與評析"],["課程討論","學習單","創作","口語／紙筆"]),
  S("kanghsuan",KANG,"屏東縣公立國中課程計畫；在古文、小說與文化文本中以比較、比喻支援主旨、寓意、觀點及寫作，採實作、口頭、自評、習作與紙筆評量；核讀 2026-09-20。",["論證方法需和篇章目的與文化脈絡相連","比喻不能只看表面相似，要檢查論點是否被支持","比較與反思可轉成口頭或書面表達"],["論證方法標記","比喻關係圖","文本比較與短文"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"嘉義縣公立國中課程計畫；以飲食、文化與生活文本安排觀點、比較、比喻及人生哲理的寫作轉化，採提問、學習單、討論和創作評量；核讀 2026-09-20。",["生活經驗可作為喻例但必須明確說明對應","比較不同文化文本要保留尺度與語境","創作需檢查論證是否連貫"],["生活喻例與文本對照","文化比較表","哲理短文與發表"],["提問","學習單","討論","創作"]),
 ],"common":["比較要明確說明對象、標準和結論，比喻要明確說明對應與界線","不能把表面相似當成完整論證，需檢查是否支持主張","評量要要求學生解釋方法如何改變理解或說服效果"],"diff":["南一偏重論證結構、閱讀策略與觀點評析","康軒把方法放進古文、小說、文化脈絡與多元評量","翰林較強調生活喻例、文化比較和哲理創作"]},
 {"lessonId":"lesson-chinese-content-be-iv-2","title":"Be-Ⅳ-2：書信便條對聯等人際溝通","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；語文天地安排書信、便條與對聯的格式、慣用語、對象與用途，連結生活溝通、撰寫練習及多元評量；核讀 2026-09-20。",["應用文本先判斷對象、目的、關係和正式程度","書信便條重視格式、稱謂、署名與訊息完整","對聯需兼顧對仗、字數、意義和文化情境"],["對象／目的／格式表","書信與便條版面標記","對聯類型與創作"],["實作","口頭","自我評量","習作／紙筆"]),
  S("kanghsuan",KANG,"屏東縣公立國中課程計畫；以對聯種類、用途、格式、撰寫要領和生活欣賞活動教學，並採實作、口頭、自評、習作與紙筆評量；核讀 2026-09-20。",["格式規則服務於實際溝通情境","對聯創作要核對結構、語意和使用場合","欣賞活動要能說明文化內涵而非只背名稱"],["應用文格式清單","對聯上下聯結構檢核","生活場景改寫"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"嘉義縣公立國中課程計畫；在書信便條教學中安排設定情節與對象、實際寫信、格式注意事項、應用練習、口頭提問與學習單；核讀 2026-09-20。",["寫作前要明確設定收件人、情境與目的","書信和便條雖都溝通，但長度、格式和語氣不同","作品需以讀者角度檢查訊息是否可執行"],["收件人／情境／目的卡","書信與便條比較","實際寫作與同儕檢核"],["口頭提問","學習單","應用練習","作品"]),
 ],"common":["先判斷溝通對象、目的與關係，再選用書信、便條或對聯格式","格式、慣用語和語氣是功能的一部分，不能只背版面","作品要經過讀者檢核，確認訊息、禮貌與行動要求清楚"],"diff":["南一同時涵蓋書信、便條、對聯與多元評量","康軒突出對聯種類、用途、格式和文化欣賞","翰林以真實情境寫信、便條和同儕檢核為主"]},
 {"lessonId":"lesson-chinese-content-ca-iv-1","title":"Ca-Ⅳ-1：飲食服飾建築交通名勝休閒文化","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；以各類文本中的飲食、服飾、建築、交通、名勝與休閒文化連結社群生活、文化差異和閱讀理解；核讀 2026-09-20。",["生活文化要從文本細節推回制度、習俗或環境脈絡","同一物件在不同社群可能有不同意義","文化解釋要避免把個案擴大成整體"],["文化物件—社群—脈絡圖","生活方式比較表","文化觀察短報告"],["討論","學習單","習作","口頭／紙筆"]),
  S("kanghsuan",KANG,"屏東縣公立國中課程計畫；以古典、現代與文化文本處理生活形式、社群關係、環境和閱讀策略，安排實作、口頭、自評、習作與紙筆評量；核讀 2026-09-20。",["文化內容需連結文本目的與社會脈絡","比較不同生活方式要交代時間、地區與群體尺度","閱讀結果可轉成尊重差異的表達"],["文化線索卡","時間／地區／群體比較","文本觀點與生活回應"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"嘉義縣公立國中課程計畫；以飲食文化與人生哲理等課文，引導學生理解不同年齡、社群與生活經驗的觀點差異，並以提問、討論和學習單評量；核讀 2026-09-20。",["飲食或生活物件可承載人生觀與世代經驗","文化閱讀要並列不同年齡或群體的看法","討論需以文本和生活經驗互相核對"],["生活物件與價值鏈","世代觀點比較","提問與學習單"],["課堂提問","學習單","討論","紙筆"]),
 ],"common":["先找生活文化線索，再連結時間、地區、群體與文本觀點","文化比較需說明尺度和證據，避免把個人經驗當成普遍規則","評量要讓學生從閱讀走向比較、提問與有根據的回應"],"diff":["南一偏重文化物件、社群脈絡與跨文本閱讀","康軒把文化內容接到環境、社會尺度與尊重差異","翰林以飲食、世代經驗、人生哲理和討論為入口"]},
]
def main():
 d=json.loads(REPORT.read_text(encoding="utf-8"));existing={x.get("lessonId") for x in d["units"]};added=[]
 for s in SAMPLES:
  rec={"lessonId":s["lessonId"],"title":s["title"],"evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":[{"publisher":p,"sourceUrl":u,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":l,"accessedAt":"2026-09-20","observedConcepts":c,"observedRepresentations":r,"observedAssessment":a,"licenseBoundary":LICENSE}for p,u,l,c,r,a in s["sources"]],"fusionReview":{"commonCore":s["common"],"differencesToReview":s["diff"],"originalSynthesisBoundary":"本樣本只記錄三筆可追溯的公立學校章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
  if rec["lessonId"] not in existing:d["units"].append(rec);added.append(rec["lessonId"])
 d["unitCount"]=len(d["units"]);d["updatedAt"]="2026-09-20";REPORT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 bp=ROOT/"implementation/reports/blockers.json";b=json.loads(bp.read_text(encoding="utf-8"))
 for x in b.get("blockers",[]):
  if isinstance(x.get("reason"),str)and "unit samples"in x["reason"]:x["reason"]=re.sub(r"Four hundred thirty-five unit samples","Four hundred thirty-eight unit samples",x["reason"])
 bp.write_text(json.dumps(b,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps({"unitCount":d["unitCount"],"added":added},ensure_ascii=False))
if __name__=="__main__":main()
