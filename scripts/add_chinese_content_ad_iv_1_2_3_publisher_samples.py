#!/usr/bin/env python3
"""Record independent public-school publisher evidence for Chinese Ad-IV-1/2/3."""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/"implementation/reports/publisher-chapter-evidence-samples.json"
NANI="https://www.cp.ptc.edu.tw/storage/134505/134505_112_B-1_9A.pdf"
KANG="https://www.kusjh.kh.edu.tw/files/shares/%E6%95%99%E5%8B%99%E8%99%95/113%E5%9C%8B%E4%B8%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/%E4%BC%8D%E3%80%81%E9%A0%98%E5%9F%9F%E5%AD%B8%E7%BF%92%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%28%E4%B9%9D%E5%B9%B4%E7%B4%9A%29.pdf"
HANLIN="https://www.yfms.tyc.edu.tw/uploads/1632969569049hbdSdsTC.pdf"
LICENSE="只記錄公立學校課程計畫的教材版本、章節學習重點與評量方向，不複製教材正文、例題、題目、答案或版面。"

def src(pub,url,loc,concepts,reps,assess):
    return (pub,url,loc,concepts,reps,assess)

SAMPLES=[
 {"lessonId":"lesson-chinese-content-ad-iv-1","title":"Ad-Ⅳ-1：篇章主旨結構寓意分析","sources":[
  src("nani",NANI,"屏東縣公立國中課程計畫；以小說、散文與跨文本閱讀處理篇章主旨、結構、寓意和人物／事件證據，並採自評、習作、紙筆與口頭活動；核讀 2026-09-20。",["主旨須由段落重點和全文目的歸納","結構要看事件、觀點或論證如何組織","寓意與分析需分開明示證據和合理推論"],["段落重點表","事件／觀點結構圖","人物證據到主旨的推論鏈"],["自我評量","習作","紙筆","口頭評量"]),
  src("kanghsuan",KANG,"高雄市公立國中康軒版九年級課程計畫；以記敘、說明與議題文本連結句段理解、寫作目的、觀點和多元評量，包含實作、口頭、自評、習作及紙筆；核讀 2026-09-20。",["篇章主旨要由句子、段落與主要概念逐層整合","結構判讀要配合文本形式與寫作特色","報告、討論和紙筆可互相驗證分析"],["段落摘要與結構標記","寫作目的／觀點辨識","文本比較與口頭論辯"],["實作","口頭","自我評量","習作／紙筆"]),
  src("hanlin",HANLIN,"桃園市公立國中課程計畫；在樂府詩、文言文本與文化內容中安排主旨、結構、寓意分析，並以口頭、作業、資料蒐集、報告、學習單和紙筆評量呈現閱讀成果；核讀 2026-09-20。",["篇章分析需結合文體、文化背景與段落功能","主旨與寓意要能回扣文本細節","資料蒐集和報告可檢查分析是否有組織"],["文體與篇章結構對照","主旨／寓意證據卡","閱讀報告與學習單"],["口頭","作業","資料蒐集","報告／學習單／紙筆"]),
 ],"common":["主旨不是單一句子的重述，要整合段落重點、結構與作者目的","寓意與讀者感想必須用文本細節區分明示和推論","評量要要求證據鏈、摘要、比較或口頭說明，而非只選標題"],"diff":["南一資料強調不同文體的主旨與結構分析","康軒較突出句段整合、寫作目的與觀點","翰林把文體、文化背景、資料蒐集和報告結合"]},
 {"lessonId":"lesson-chinese-content-ad-iv-2","title":"Ad-Ⅳ-2：新詩現代散文現代小說劇本","sources":[
  src("nani",NANI,"屏東縣公立國中課程計畫；以現代散文、小說和劇本的內容、形式與寫作特色作跨文體閱讀，並用自評、習作、紙筆和口頭任務檢核理解；核讀 2026-09-20。",["不同文體要比較敘事視角、場景、語言與結構","新詩和散文的形式證據不可用小說分析框架取代","劇本理解需注意角色、對話、舞台行動與衝突"],["文體特徵比較表","詩／散文意象與語氣標記","劇本角色—對話—舞台指示圖"],["自我評量","習作","紙筆","口頭／實作"]),
  src("kanghsuan",KANG,"高雄市公立國中康軒版九年級課程計畫；將新詩、現代散文、現代小說與劇本放入文本內容、形式、寫作特色和議題討論，採實作、口頭、自評、習作與紙筆評量；核讀 2026-09-20。",["文體形式與寫作目的要一起判讀","閱讀須說明文本如何透過描寫、對話或意象產生效果","多元文本閱讀可轉成評論與表達"],["文體線索卡","描寫手法與效果配對","文本評論與討論"],["實作","口頭","自我評量","習作／紙筆"]),
  src("hanlin",HANLIN,"桃園市公立國中課程計畫；以古典／現代詩歌、敘事文本與篇章分析連結情感、文化和寫作任務，安排資料蒐集、報告、學習單、口頭與紙筆評量；核讀 2026-09-20。",["文體辨識要和情感、文化內涵及表達目的連結","不同作品可用形式證據進行比較而非只背分類","報告與改寫能檢查是否掌握文體規則"],["詩歌節奏與意象觀察","作品形式／文化內涵對照","報告與改寫任務"],["資料蒐集","報告","學習單","口頭／紙筆"]),
 ],"common":["先判斷文體規則，再選用相應的形式、語言、角色或結構證據","比較不同文體時要指出可觀察差異及其表達效果","改寫或評論必須保留原文體的核心限制並說明轉化理由"],"diff":["南一偏向多文體內容、形式和寫作特色比較","康軒將文體分析與議題討論、評論表達連結","翰林較強調詩歌、文化內涵、資料蒐集和作品轉化"]},
 {"lessonId":"lesson-chinese-content-ad-iv-3","title":"Ad-Ⅳ-3：韻文古體樂府近體詞曲","sources":[
  src("nani","https://w3.qnm.kh.edu.tw/curriculum/111/plan/%E7%89%B9%E6%95%99%E7%8F%AD/%E8%B3%87%E6%BA%90%E7%8F%AD/%E8%B3%87%E6%BA%90%E7%8F%AD-%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB-%E5%9C%8B%E6%96%872A.pdf","高雄市公立國中南一版第四冊課程計畫；從古體詩、樂府詩、近體詩、詞曲的形式、格律、朗誦和篇章賞析切入，採紙筆與實作評量；核讀 2026-09-20。",["韻文分類需連結句式、節奏、押韻和文體來源","朗誦是檢查音韻與情感，不是單純背誦","形式分析要回到詩中意象與主旨"],["格律／句式比較","節奏與押韻標記","朗誦及詩句改寫"],["紙筆","實作","朗誦／學習單"]),
  src("kanghsuan","https://fsjh.chc.edu.tw/open_files_download/%262%2699%26365%26368%26370","彰化縣福興國中公立康軒版第三冊課程計畫；古體詩選安排音韻和諧、格律形式、吟誦、注釋與賞析，並以實作、口頭、自評、習作和紙筆評量；核讀 2026-09-20。",["古體詩的音韻與句式要由朗讀和文本觀察驗證","格律形式不可脫離詩句情感與寫作手法","吟誦、提問和習作能共同檢核理解"],["吟誦節奏標記","格律與詩句對照","詩作角色獨白／賞析"],["實作","口頭","自我評量","習作／紙筆"]),
  src("hanlin","https://www.chjh.tyc.edu.tw/uploads/neilfilefolder/20file/file/196_69_511%E6%99%AE%E9%80%9A%E7%8F%AD%E5%90%84%E9%A0%98%E5%9F%9F%E7%A7%91%E7%9B%AE%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%E5%9C%8B%E6%96%87.pdf","桃園市公立國中翰林版國文課程計畫；以新詩、古體詩、樂府與近體詩等韻文安排主題探索、資料整理、視覺化報告、口語分享與紙筆評量；核讀 2026-09-20。",["韻文閱讀要兼顧形式、情感和文化脈絡","不同詩體可用資料整理和朗讀比較","主題報告能把詩句證據轉成有條理的觀點"],["詩體演變時間線","意象／情感證據表","朗讀、專題與視覺化整理"],["口語","實作","習作","定期紙筆／專題"]),
 ],"common":["韻文判讀要同時看文體、句式、節奏、押韻與意象，不以名稱猜答案","朗誦與格律分析必須回到詩句證據及情感效果","比較題要指出形式差異如何造成閱讀或表達效果"],"diff":["南一以韻文分類、格律和朗誦賞析建立基礎","康軒較突出古體詩吟誦、格律和角色化表達","翰林把詩體比較延伸到文化脈絡、資料整理和專題分享"]},
]

def main():
    d=json.loads(REPORT.read_text(encoding="utf-8")); existing={x.get("lessonId") for x in d["units"]}; added=[]
    for s in SAMPLES:
        records=[]
        for p,u,l,c,r,a in s["sources"]:
            records.append({"publisher":p,"sourceUrl":u,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":l,"accessedAt":"2026-09-20","observedConcepts":c,"observedRepresentations":r,"observedAssessment":a,"licenseBoundary":LICENSE})
        rec={"lessonId":s["lessonId"],"title":s["title"],"evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":records,"fusionReview":{"commonCore":s["common"],"differencesToReview":s["diff"],"originalSynthesisBoundary":"本樣本只記錄三筆可追溯的公立學校章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
        if rec["lessonId"] not in existing: d["units"].append(rec); added.append(rec["lessonId"])
    d["unitCount"]=len(d["units"]); d["updatedAt"]="2026-09-20"; REPORT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    bp=ROOT/"implementation/reports/blockers.json"; b=json.loads(bp.read_text(encoding="utf-8"))
    for x in b.get("blockers",[]):
        if isinstance(x.get("reason"),str) and "unit samples" in x["reason"]: x["reason"]=re.sub(r"Four hundred twenty unit samples","Four hundred twenty-three unit samples",x["reason"])
    bp.write_text(json.dumps(b,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"unitCount":d["unitCount"],"added":added},ensure_ascii=False))
if __name__=="__main__": main()
