#!/usr/bin/env python3
"""Record independent public-school publisher evidence for Chinese Ac-IV-1/2/3."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
NANI = "https://www.kusjh.kh.edu.tw/files/shares/%E6%95%99%E5%8B%99%E8%99%95/113%E5%9C%8B%E4%B8%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/%E4%BC%8D%E3%80%81%E9%A0%98%E5%9F%9F%E5%AD%B8%E7%BF%92%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%28%E5%85%AB%E5%B9%B4%E7%B4%9A%29.pdf"
KANG = "https://w3.qnm.kh.edu.tw/curriculum/111/plan/%E7%89%B9%E6%95%99%E7%8F%AD/%E8%B3%87%E6%BA%90%E7%8F%AD/%E8%B3%87%E6%BA%90%E7%8F%AD-%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB-%E5%9C%8B%E6%96%871B.pdf"
HANLIN = "https://www.curriculum.chc.edu.tw/storage/164/110/5-7-%E5%9C%8B%E8%AA%9E%E6%96%87.pdf/Go8bL8272DkbZSBkIKB7cjbselE8qpVsFtUIUjGh.pdf"
LICENSE = "只記錄公立學校課程計畫的教材版本、章節學習重點與評量方向，不複製教材正文、例題、題目、答案或版面。"

SAMPLES = [
    {"lessonId":"lesson-chinese-content-ac-iv-1","title":"Ac-Ⅳ-1：標點不同效果","sources":[
        ("nani",NANI,"高雄市公立國中南一版課程計畫；書信與便條單元把標點放入情感表達、說服力、朗讀和學習單，並以口頭、作業、自評與紙筆檢查標點效果；核讀 2026-09-20。",["標點改變停頓、語氣與讀者理解","同一句話可因標點配置產生不同表達效果","標點判讀要回到文本目的與情境"],["朗讀停頓標記","不同標點版本對照","書信或便條改寫"],["觀察紀錄","口頭評量","作業","學習單"]),
        ("kanghsuan",KANG,"高雄市公立國中康軒版資源班課程計畫；以課文、動畫、問答和紙筆／檔案／口語評量處理標點與文句意義，並保留分層提示及生活化語境；核讀 2026-09-20。",["標點和句意理解要同步教學","提示與分層可降低僅靠形式記憶的錯誤","生活語句能檢驗標點是否真正改變語氣"],["句子切分提示","標點與語氣配對","問答及紙筆練習"],["紙筆","問答","觀察","檔案"]),
        ("hanlin",HANLIN,"彰化縣公立國中翰林版國文教學進度總表；以文言故事、寓言和改寫活動讓學生觀察句讀、語意與敘述效果，並以學習單、口語表達、創作和發表評量；核讀 2026-09-20。",["句讀與段落理解互相驗證","標點選擇要能說明對故事語氣或意義的影響","改寫和發表能呈現標點遷移"],["文言句讀分段","故事版本比較","改寫、漫畫與口頭分享"],["學習單","口語表達","創作","小組發表"]),
    ],"common":["標點不是裝飾，需以停頓、語氣、語意與溝通目的說明效果","同一組字詞在不同標點下可能形成不同句意，答案要有上下文證據","評量應從辨認符號延伸到朗讀、改寫或情境表達"],"diff":["南一偏向標點、朗讀與實用文本的情感／說服功能","康軒強調提示、分層和多元評量支援句意理解","翰林把句讀效果放進文言故事與創作改寫"]},
    {"lessonId":"lesson-chinese-content-ac-iv-2","title":"Ac-Ⅳ-2：敘事有無判斷表態等句型","sources":[
        ("nani",NANI,"高雄市公立國中南一版課程計畫；將敘事、有無、判斷、表態句型連結書信便條、生活表達與學習單，要求依溝通目的組織句意；核讀 2026-09-20。",["句型功能取決於敘述、存在、判斷或表態目的","句型要和主語、述語及語境共同判讀","實用文本可檢查句型是否能完成溝通"],["書信便條句型拆解","句型功能分類","生活情境改寫"],["口頭評量","作業","自我評量","學習單"]),
        ("kanghsuan",KANG,"高雄市公立國中康軒版資源班課程計畫；以直接、交互、問題解決和合作學習處理句型，透過課文動畫、問答、檔案與紙筆評量檢查敘事及表態表達；核讀 2026-09-20。",["句型教學需拆成可觀察的主語、關係與語氣","同一情境可用不同句型傳達不同訊息","口語與書面都要驗證句型的溝通功能"],["成分標記","句型與情境配對","合作問答與短句輸出"],["紙筆","檔案","口語","合作觀察"]),
        ("hanlin",HANLIN,"彰化縣公立國中翰林版國文教學進度總表；以神話寓言等文本辨識敘事句、判斷與表態，再轉為成語、故事改寫、漫畫和專題發表；核讀 2026-09-20。",["句型功能可從故事事件與人物觀點辨識","判斷與表態需區分事實敘述和說話者立場","創作改寫能檢查句型是否能支撐敘事"],["故事句型標註","事實／觀點分類","漫畫或故事改寫"],["學習單","口語表達","圖畫創作","專題報告"]),
    ],"common":["先判斷句子要完成的溝通功能，再看結構與語氣，不能只背句型名稱","敘事、存在、判斷、表態的區分要有主語、述語及上下文證據","題目與活動應要求學生把句型放入新情境，而不是只做名詞配對"],"diff":["南一以書信便條等實用文本連結句型與溝通","康軒用分層、合作和多元評量支援句型輸出","翰林從故事人物與事件轉入觀點、改寫和發表"]},
    {"lessonId":"lesson-chinese-content-ac-iv-3","title":"Ac-Ⅳ-3：文句邏輯與意義","sources":[
        ("nani",NANI,"高雄市公立國中南一版課程計畫；把文句邏輯放在文本理解、閱讀策略、口語提問與書面作業中，並以學習單和自我評量追蹤句間關係；核讀 2026-09-20。",["句意需檢查前後因果、轉折、承接與指涉","文句邏輯要連結篇章目的與觀點","口語追問能揭露推論是否有證據"],["句間連接詞標記","因果／轉折關係圖","閱讀提問與段落重組"],["觀察","口頭評量","作業","學習單"]),
        ("kanghsuan",KANG,"高雄市公立國中康軒版資源班課程計畫；以直接、交互、問題解決教學處理文意和提問，透過背景、重要詞彙、紙筆、檔案與口語評量檢查邏輯理解；核讀 2026-09-20。",["文句邏輯需從詞彙、背景和句間關係逐步建構","提問與問題解決可測試推論是否合理","分層資料要保留原句意與證據界線"],["背景／詞彙提示卡","句子排序與關係配對","問題解決式閱讀"],["紙筆","檔案","口語","文本提問"]),
        ("hanlin",HANLIN,"彰化縣公立國中翰林版國文教學進度總表；以文言故事的字句分析、主旨理解、成語來源和改寫活動，讓學生把句子邏輯轉成故事解釋與作品；核讀 2026-09-20。",["句子邏輯要能支持故事因果與主旨判斷","語意推論必須區分文本明示與讀者延伸","改寫與專題發表能呈現邏輯是否連貫"],["故事事件鏈","明示／推論證據表","故事改寫與發表"],["學習單","口語表達","創作","專題報告"]),
    ],"common":["判斷文句意義要先找連接、指涉、因果與轉折證據，再形成解釋","不能把讀者常識當成文本必然結論，需區分明示、合理推論與無資料","評量應要求重組、說明或改寫，檢查邏輯能否遷移"],"diff":["南一較強調閱讀策略、句間關係和口語追問","康軒以詞彙／背景提示和問題解決逐步搭建理解","翰林把句意邏輯轉入故事因果、主旨、改寫與發表"]},
]

def main() -> None:
    data=json.loads(REPORT.read_text(encoding="utf-8")); existing={x.get("lessonId") for x in data["units"]}; added=[]
    for s in SAMPLES:
        records=[]
        for pub,url,loc,concepts,reps,assessment in s["sources"]:
            records.append({"publisher":pub,"sourceUrl":url,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":loc,"accessedAt":"2026-09-20","observedConcepts":concepts,"observedRepresentations":reps,"observedAssessment":assessment,"licenseBoundary":LICENSE})
        rec={"lessonId":s["lessonId"],"title":s["title"],"evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":records,"fusionReview":{"commonCore":s["common"],"differencesToReview":s["diff"],"originalSynthesisBoundary":"本樣本只記錄三筆可追溯的公立學校章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
        if rec["lessonId"] not in existing: data["units"].append(rec); added.append(rec["lessonId"])
    data["unitCount"]=len(data["units"]); data["updatedAt"]="2026-09-20"; REPORT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    blocker_path=ROOT/"implementation/reports/blockers.json"; blockers=json.loads(blocker_path.read_text(encoding="utf-8"))
    for b in blockers.get("blockers",[]):
        if isinstance(b.get("reason"),str) and "unit samples" in b["reason"]: b["reason"]=re.sub(r"Four hundred seventeen unit samples","Four hundred twenty unit samples",b["reason"])
    blocker_path.write_text(json.dumps(blockers,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"unitCount":data["unitCount"],"added":added},ensure_ascii=False))

if __name__ == "__main__": main()
