#!/usr/bin/env python3
"""Record independent public-school publisher evidence for Ad-IV-4 and Ba-IV-1/2."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; REPORT=ROOT/"implementation/reports/publisher-chapter-evidence-samples.json"
LICENSE="只記錄公立學校課程計畫或公開教學資源的教材版本、章節學習重點與評量方向，不複製教材正文、例題、題目、答案或版面。"
NANI="https://www.cp.ptc.edu.tw/storage/134508/134508_112_B-1_9A.pdf"
KANG="https://w3.qnm.kh.edu.tw/curriculum/111/plan/%E7%89%B9%E6%95%99%E7%8F%AD/%E8%B3%87%E6%BA%90%E7%8F%AD/%E8%B3%87%E6%BA%90%E7%8F%AD-%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB-%E5%9C%8B%E6%96%871B.pdf"
HANLIN="https://www.yfms.tyc.edu.tw/uploads/1632969569049hbdSdsTC.pdf"
def S(p,u,l,c,r,a): return (p,u,l,c,r,a)
SAMPLES=[
 {"lessonId":"lesson-chinese-content-ad-iv-4","title":"Ad-Ⅳ-4：非韻文古文古典小說語錄寓言","sources":[
 S("nani",NANI,"屏東縣公立國中課程計畫；以古文、古典小說、語錄體與寓言處理非韻文的內容、形式、寓意和文化脈絡，搭配自評、習作、紙筆與口頭評量；核讀 2026-09-20。",["非韻文分類要看敘事、對話、格言或寓言功能","古文理解需結合字句、情節和文化背景","寓意與作者觀點要有篇內證據"],["文體特徵對照","故事情節／寓意證據鏈","古今文化脈絡比較"],["自我評量","習作","紙筆","口頭"]),
 S("kanghsuan",KANG,"高雄市公立國中康軒版資源班課程計畫；明列非韻文與課文理解、賞析、提問及短文表達，採簡化分層、直接／交互／問題解決教學與多元評量；核讀 2026-09-20。",["非韻文閱讀可由情節、人物和語句逐層建構","提示與分層不能取代文本證據","賞析要轉化為提問、表達或短文"],["課文動畫與情節圖","人物／觀點提示","提問及短文輸出"],["紙筆","檔案","口語","學習單"]),
 S("hanlin",HANLIN,"桃園市公立國中課程計畫；在樂府、文言及跨文本活動中連結非韻文的主旨、結構、文化與報告任務，採口頭、作業、資料蒐集、學習單、報告和紙筆評量；核讀 2026-09-20。",["非韻文分析要連結文體與文化內涵","篇章結構支援主旨、寓意與觀點判斷","資料整理和報告能檢查理解組織"],["文體／文化比較","主旨與寓意證據卡","閱讀報告與學習單"],["口頭","作業","資料蒐集","報告／紙筆"]),
 ],"common":["先辨認非韻文形式，再用字句、情節、人物、語錄或寓意證據解讀","古今背景是輔助線索，不能取代篇內證據","評量要從分類延伸到賞析、提問、改寫或報告"],"diff":["南一強調文體、寓意和文化脈絡的整合","康軒以分層提示和問題解決支援古文理解","翰林將非韻文閱讀連結資料整理、文化比較與報告"]},
 {"lessonId":"lesson-chinese-content-ba-iv-1","title":"Ba-Ⅳ-1：順敘倒敘插敘補敘","sources":[
 S("nani",NANI,"屏東縣公立國中課程計畫；以小說與記敘文本辨識順敘、倒敘、插敘和補敘對主旨、懸念與事件理解的作用，並用習作、紙筆與口頭評量；核讀 2026-09-20。",["敘事順序要以事件時間與文本安排雙重判斷","倒敘、插敘和補敘會改變資訊揭露與閱讀期待","順序分析需說明對主旨或節奏的效果"],["事件時間線與文本順序並列","插敘／補敘框線標記","重排段落與效果說明"],["習作","紙筆","口頭","自我評量"]),
 S("kanghsuan",KANG,"高雄市公立國中康軒版資源班課程計畫；以課文動畫、事件理解、短文表達和分層提示教學處理敘事順序，採紙筆、檔案、口語與觀察評量；核讀 2026-09-20。",["先還原事件，再判斷作者為何調整順序","視覺化情節可支援插敘與補敘辨識","排序後要回到語意與表達效果"],["事件卡排序","時間線與文本順序對照","口頭重述與短文改寫"],["紙筆","檔案","口語","觀察"]),
 S("hanlin",HANLIN,"桃園市公立國中課程計畫；在敘事與樂府文本中比較先概述、寫景、抒懷及補述等安排，連結篇章分析、報告和學習單；核讀 2026-09-20。",["順序安排可和景物、情感及人物成長互相驗證","補敘不只是插入資料，還會補足理解所需背景","分析需能轉成口頭或書面組織"],["敘事層次圖","先後／補述功能標記","報告與學習單"],["課程討論","報告","學習單","紙筆"]),
 ],"common":["先建立事件時間線，再比較文本順序，避免把閱讀順序誤當故事時間","每種敘事安排都要連到資訊揭露、節奏、懸念或情感效果","重排或改寫後須說明哪些效果被保留或改變"],"diff":["南一重視敘事順序對主旨與懸念的作用","康軒以事件卡、動畫和分層提示建立理解","翰林將順序安排與景物、抒懷、篇章報告連結"]},
 {"lessonId":"lesson-chinese-content-ba-iv-2","title":"Ba-Ⅳ-2：描寫作用與效果","sources":[
 S("nani",NANI,"屏東縣公立國中課程計畫；以人物、景物與事件描寫分析篇章效果、情感和文化意涵，並用習作、口頭、自評和紙筆任務檢核；核讀 2026-09-20。",["描寫要區分對象、感官線索、視角和情感效果","細節選擇能塑造人物、場景或氛圍","效果解釋必須回扣具體語句"],["感官細節標記","人物／景物描寫證據卡","同景不同視角改寫"],["習作","口頭","自我評量","紙筆"]),
 S("kanghsuan",KANG,"高雄市公立國中康軒版資源班課程計畫；將各種描寫和課文理解、提問、短文表達結合，採直接／交互教學、紙筆、檔案與口語評量；核讀 2026-09-20。",["描寫教學要把可見語句和讀者效果配對","分層提示可引導學生從觀察到解釋","短文輸出能檢查是否掌握描寫手法"],["描寫詞語圈選","語句—效果配對","觀察後短文描寫"],["紙筆","檔案","口語","短文"]),
 S("hanlin",HANLIN,"桃園市公立國中課程計畫；在詩歌、文言和敘事文本中比較描寫、對偶、寫景與抒情功能，安排課程討論、報告、學習單和作品表達；核讀 2026-09-20。",["描寫可同時承擔景物呈現、聲律、情感與主旨功能","修辭形式需與描寫對象和篇章位置一起判斷","作品或報告要提出形式證據與效果"],["描寫／抒情對照","對偶與聲律觀察","作品分享與報告"],["課程討論","報告","學習單","口頭／紙筆"]),
 ],"common":["先指出描寫對象與可觀察語句，再說明視角、感官或修辭如何造成效果","不能只貼『生動』或『優美』標籤，必須解釋語句與讀者感受的關係","改寫活動要保留目標效果並說明用詞選擇"],"diff":["南一偏向人物、景物、事件與情感的描寫證據鏈","康軒以分層提示和短文輸出支援描寫理解","翰林較突出詩歌聲律、對偶、寫景與抒情的連接"]},
]
def main():
 d=json.loads(REPORT.read_text(encoding="utf-8")); existing={x.get("lessonId") for x in d["units"]}; added=[]
 for s in SAMPLES:
  records=[{"publisher":p,"sourceUrl":u,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":l,"accessedAt":"2026-09-20","observedConcepts":c,"observedRepresentations":r,"observedAssessment":a,"licenseBoundary":LICENSE} for p,u,l,c,r,a in s["sources"]]
  rec={"lessonId":s["lessonId"],"title":s["title"],"evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":records,"fusionReview":{"commonCore":s["common"],"differencesToReview":s["diff"],"originalSynthesisBoundary":"本樣本只記錄三筆可追溯的公立學校章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
  if rec["lessonId"] not in existing:d["units"].append(rec);added.append(rec["lessonId"])
 d["unitCount"]=len(d["units"]);d["updatedAt"]="2026-09-20";REPORT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 bp=ROOT/"implementation/reports/blockers.json";b=json.loads(bp.read_text(encoding="utf-8"))
 for x in b.get("blockers",[]):
  if isinstance(x.get("reason"),str) and "unit samples" in x["reason"]:x["reason"]=re.sub(r"Four hundred twenty-three unit samples","Four hundred twenty-six unit samples",x["reason"])
 bp.write_text(json.dumps(b,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps({"unitCount":d["unitCount"],"added":added},ensure_ascii=False))
if __name__=="__main__":main()
