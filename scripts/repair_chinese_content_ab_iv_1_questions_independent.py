#!/usr/bin/env python3
"""Independently rewrite Chinese Ab-IV-1 common-character questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-content-ab-iv-1"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","常用字形音義與詞語"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","字音、字形、詞義與語境"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","常用字辨析與查證"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量將常用字放在詞語、句子與查證情境中，要求整合字形、字音、詞義、部件與語境；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("字形選擇","下列哪句的常用字形使用正確？",["研究者仔細核對資料，沒有遺漏。","研究者仔細核對資料，沒有遺落。","研究者仔細核對資料，沒有遺誤。","研究者仔細核對資料，沒有移漏。"],"A","在『資料沒有漏掉』的語境中，遺漏是規範詞，字形與詞義都相合。","先判斷句子要表達的動作，再用固定詞語與字典核對形音義。"),
 ("載音義","「載」在「記載資料」與「載客列車」中的讀音和意思如何區分？",["都讀ㄗㄞˇ，都表示承受","前者讀ㄗㄞˇ表示記錄，後者讀ㄗㄞˋ表示承載","前者讀ㄗㄞˋ表示記錄，後者讀ㄗㄞˇ表示承載","兩詞讀音相同但意思完全相同"],"B","記載的載讀ㄗㄞˇ，表示記錄；載客的載讀ㄗㄞˋ，表示承載。","先把多音字放回完整詞語，再同時核對讀音、詞性與語意。"),
 ("詞語搭配","新規定公布後，校方請各班＿＿說明理由；最適合填入？",["分別","分辨","分辯","分貝"],"C","各班分別說明表示各自、逐一說明；分辨是辨別，分辯是爭辯，分貝是音量單位。","先看句子需要副詞、動作或名詞，再用詞義與搭配排除形近字。"),
 ("語境用字","下列哪句用字最恰當？",["請把研究結果概括成三點。","請把研究結果概廓成三點。","請把研究結果慨括成三點。","請把研究結果槪括成三點。"],"D","概括表示歸納大意，符合把結果整理成三點的語境；其他字形不合規範或混用。","抓住動作的語意，再核對規範字形與正式詞語，不以同音或形近字代替。"),
 ("分量詞義","「這篇報告的分量很重」中的「分量」最接近？",["物品的重量","文章或意見的重要程度與影響力","食物的份量大小","字的筆畫數"],"A","報告的分量重是引申義，表示內容重要、有影響力，不是實際秤重。","先看詞語修飾的對象，再判斷是本義或引申義，避免只套單字字面。"),
 ("單字歧義","只看到單獨一個「樂」字，沒有詞語或句子時，最可靠的做法是？",["直接固定讀ㄌㄜˋ","依最常見意思作答，不必查證","承認資訊不足，尋找完整詞語或上下文後再查規範讀音與義項","選筆畫最少的讀法"],"B","樂有多個讀音與義項，缺乏語境時不能武斷；應補足詞語或上下文再查證。","先辨認題目資訊是否足夠，再用語境與工具確認，而不是以直覺補答案。"),
 ("成語義項","要形容「先處理根本原因，使表面問題自然消失」，哪個成語最適合？",["釜底抽薪","火上加油","走馬看花","緣木求魚"],"C","釜底抽薪比喻從根本處理問題，符合移除薪柴使火熄滅的核心意義。","先把情境改寫成白話動作，再找與根本、表面、因果方向相符的成語。"),
 ("事實語氣","研究者＿＿呈現測量結果，沒有把推測說成事實；最適合填入？",["如實","如是","儒實","茹實"],"D","如實表示按照事實、不加虛構，正好對應客觀呈現測量結果。","先判斷句子需要的語意，再核對同音形近字的規範詞形。"),
 ("部件線索","「清、情、晴、請」含有相近部件；下列判斷最正確？",["相近部件保證四字讀音與意思完全相同","青可提供部分聲音線索，但三字旁仍使詞義方向不同，需放回詞語判斷","只要看到青就能直接選字","四字都是同一個詞的不同寫法"],"A","青可能提供聲音線索，水、心、日、言等部件與整字詞義相關，形近不能互換。","先分出聲旁與形旁，再把每字放回詞語核對讀音、字形與義項。"),
 ("完整查證","要確認一個陌生常用字在文章中的形、音、義，哪個流程最完整？",["看部首後直接猜答案","查字典注音與義項，觀察詞語上下文，核對規範字形並用原句回讀","只抄網路留言最多的寫法","只比較字的筆畫數"],"B","字典、語境、規範字形與回讀互相驗證，能降低單一線索造成的誤判。","依形—音—義—語境順序查證，最後用原句與例詞測試是否能正確使用。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與詞語、字音、字形、部件、語境或查證流程。",f"整合形音義：把單字放回完整詞語與句子，檢查讀音、詞義及固定搭配；本題核心是「{explanation}」",f"核對正解：選項 {target} 能同時符合規範字形、讀音、詞義與上下文。","排除誘答：檢查是否只靠同音、形近或最常見讀法，或把本義硬套到引申語境。","回讀驗證：用字典與原句重新朗讀，確認字形、字音、字義在實際使用中都一致。"]
 item={"id":f"question-chinese-content-ab-iv-1-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ab-iv-1"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究常用字形音義、部件、詞語搭配與查證流程。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫 Ab-Ⅳ-1 常用字題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-content-ab-iv-1-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
