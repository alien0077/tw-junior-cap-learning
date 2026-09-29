#!/usr/bin/env python3
"""Independently rewrite Chinese character form/sound/meaning questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-common-character-form-sound-meaning"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","字音、字形與語境辨識"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","形音義、錯別字與閱讀理解"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","字詞辨析與語境判讀"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量將字形、字音、字義放進完整詞語與句子，要求依語境查證；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("辨／辯","下列句子中，哪個詞語的用字正確？",["先辨識資料，再辯論結論","先辯識資料，再辨論結論","先辨識資料，再辨論結論","先辯識資料，再辯論結論"],"A","辨識是分辨、認出；辯論是用理由互相討論，兩字雖同音但字義與搭配不同。","先看每個字在詞中的功能，再用詞義與固定搭配逐一核對。"),
 ("澄清讀音","「澄清誤會」的「澄」讀音與下列哪個詞相同？",["澄澈","橙子","登記","乘船"],"A","澄清、澄澈的澄都讀ㄔㄥˊ，表示使混亂變清楚或清澈；橙、登、乘的音不同。","把目標字放回完整詞語朗讀，再用字典注音與詞義交叉確認。"),
 ("慨／概","下列哪一句的用字最恰當？",["他慨括說明研究結果。","他概括說明研究結果。","他感到慨念難忘。","這份概嘆令人動容。"],"B","概括是歸納大意；感慨、慨念等混用會破壞詞義與字形。","先找出句子要表達的是歸納、情緒或概念，再選對應字形。"),
 ("井然語境","志工把報到、分組與借用器材的步驟列成清單，現場安排十分＿＿。",["井然有序","不翼而飛","莫衷一是","首當其衝"],"A","井然有序形容整齊、有條理，和步驟清楚的活動安排相合。","把句中主語與結果畫出來，再以成語的核心意義檢查搭配。"),
 ("戛然／嘎然","演講結束後，擴音器的聲音＿＿停止，現場突然安靜。下列填字何者正確？",["嘎然","戛然","甲然","格然"],"B","戛然可形容聲音突然停止，不能因讀音相近就改用其他字形。","先用整句情境判斷詞義，再確認規範字形，不以同音字代換。"),
 ("形近字查證","看到「再接再厲」與「再接再勵」兩種寫法時，最可靠的判斷流程是？",["依詞典與正式語文資料核對，再放回句子朗讀","選筆畫較少的寫法","看社群留言哪一個較常見","只依發音相同就視為都正確"],"A","形近或同音字不能只靠直覺；查字典與正式語文資料，再回到詞語語境最可靠。","把判斷分成資料查證、詞義比對與句中回讀三階段。"),
 ("既／即","下列哪句的「既」使用正確？",["既然已確認資料，就應標明來源。","他既席完成一段演講。","請既時回覆表單。","問題既刻就能解決。"],"A","既然表示承認前提並引出結果；即席、即時、即刻才使用即。","先辨識詞語在句中表示前提、臨場、時間或立即，再選字形。"),
 ("字義轉換","「開放資料」與「把窗戶打開」中的「開」有何共同點？",["都表示使原本封閉或受限的狀態變得可進入、可使用","都只表示用手推動門窗","前者是錯別字，後者才正確","兩者讀音不同所以不能比較"],"A","開放資料是使資料可被取得，打開窗戶是解除關閉狀態，兩者都保留由閉到通的核心義。","先抓字的核心義，再看不同搭配如何由本義延伸出語境義。"),
 ("語境選字","校刊要寫「同學提出理由互相討論」，下列哪個詞最精確？",["辯論","辨論","辮論","便論"],"A","辯論指雙方提出理由、互相討論；辨、辮、便不是此詞的規範字形。","先以事件判斷是討論或辨認，再核對同音形近字的規範寫法。"),
 ("形音義整合","掌握一個生字時，哪項做法最能同時降低誤讀與誤用？",["只背部首","只記同音字","記錄字形、注音、核心義與一個完整例詞，再回句查證","只看字在單獨字表中的排列"],"C","形音義必須與完整詞語連結；例詞與回句能檢查讀音、字形和語意是否一致。","建立形音義卡片，再用新句測試是否能遷移，不讓單一線索代替完整判斷。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與完整詞語、句子，確認題目問形、音、義或查證流程。",f"找語境證據：觀察詞性、搭配、聲音與句意，不能只靠單字直覺；本題核心是「{explanation}」",f"核對正解：選項 {target} 同時符合規範字形、讀音、詞義與句中功能。","排除誘答：檢查是否誤用同音字、形近字、孤立字義，或把本義硬套到引申語境。","回讀驗證：以字典注音與完整例句重新朗讀，確認形、音、義三者彼此一致。"]
 item={"id":f"question-chinese-common-character-form-sound-meaning-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ab-iv-1"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究形音義、形近字與語境查證能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫常用字形音義題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-common-character-form-sound-meaning-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
