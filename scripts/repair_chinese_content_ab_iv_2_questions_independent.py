#!/usr/bin/env python3
"""Independently rewrite Chinese Ab-IV-2 contextual word questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-content-ab-iv-2"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","詞語、字形、字音與語境"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","用字、詞義與語境"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","常用詞辨析與查證"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量將形近、同音、多音與詞義選擇放進完整語境，要求依搭配、語氣與上下文作可查證判斷；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("詞語用字","校刊想寫一篇文章＿＿社區長者的生活經驗，最適合填入？",["紀錄","記綠","既錄","記錄"],"A","紀錄可作動詞，表示把經驗記下來；其他選項不是此語境的規範用字。","先判斷句子需要的動作，再用固定搭配與詞典核對字形。"),
 ("辨識搭配","下列哪句最適合使用「辨識」？",["辨識照片中的鳥類種類","辨識朋友的善意所以很感動","辨識問題的根本原因並提出方案","辨識飯菜很好吃"],"B","辨識常指分辨、認出對象，照片中的鳥類屬於清楚的辨認任務；其他句子較需分析、感受或評價。","先確認詞語的動作對象，再區分辨識、分析、感受與評價的功能。"),
 ("推翻推論","「新證據＿＿原先的推論」中，哪個詞最能表達使原推論失去成立基礎？",["支持","延長","推翻","裝飾"],"C","推翻表示使原有主張不再成立，符合新證據改變原先推論的語境。","先把句子改寫成白話，再判斷動詞與主語、受詞之間的因果方向。"),
 ("著音義","下列哪組「著」的讀音與意思相同？",["著名、著手","著急、著手","著名、著急","睡著、著火"],"D","睡著與著火的著都讀ㄓㄠˊ，分別表示進入睡眠狀態與燃燒；其他詞語讀音或義項不同。","多音字必須逐詞查證，先核對讀音與義項再比較，不能只看字形。"),
 ("語境填詞","他＿＿完成修正，才把報告交出；最適合填入？",["終於","偶爾","立刻","大概"],"A","終於表示經過等待或努力後完成，和修正後才交出的時間轉折相合。","先找句中的時間與結果關係，再選能表達過程、程度或先後的詞語。"),
 ("提醒動詞","「老師＿＿我們遵守實驗室規則」中，最恰當的動詞是？",["提醒","題醒","提省","蹄醒"],"B","提醒是預先告知、使人注意，搭配『我們遵守規則』自然。","先確認句子需要的動作，再排除同音形近字並檢查詞語搭配。"),
 ("清楚程度","「請把操作步驟寫得＿＿，新手才容易照著做」最適合？",["清楚","清楚楚","清處","青楚"],"C","清楚表示明白、不含糊，修飾操作步驟能直接服務新手理解。","找出受詞與使用目的，再選能表示程度與理解效果的規範詞。"),
 ("單字不足","題目只給一個同音字，沒有詞語或句子；最妥當的做法是？",["直接依最常見讀音決定","依字形筆畫猜意思","把所有同音字都當成正確","指出資訊不足，要求補充語境後再查字典核對"],"D","沒有詞語與句子時，無法確定字音、字形或義項；應先補足語境與可靠查證。","先判斷證據是否足夠，再提出需要的詞語、句子、注音或字典資料。"),
 ("成語語境","研究者＿＿呈現資料，沒有把尚未證明的推測寫成結論；最適合？",["如實","如是","儒實","茹實"],"A","如實表示按照事實呈現，符合研究寫作需要的證據分寸。","先辨認句子的語體與功能，再核對同音形近詞的規範字形。"),
 ("完整流程","判斷一個不熟悉的常用字時，哪個流程最完整？",["看部首直接猜答案","查注音與義項、放回詞語上下文、核對字形並回讀句子","只問同學的第一印象","把字換成同音字就算完成"],"B","完整流程整合工具、語境、字形與回讀，能降低孤立字形或直覺造成的錯誤。","依形音義與語境分層查證，最後以原句檢查能否正確理解與使用。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與句中的主語、動作、搭配、語氣或查證條件。",f"回到語境：先判斷句子需要的詞義與功能，再核對形、音、義及固定搭配；本題核心是「{explanation}」",f"核對正解：選項 {target} 能在完整句子中成立，且字形、讀音與詞義相互一致。","排除誘答：檢查是否只看單字、混淆同音形近字、把不同詞性硬套，或忽略資訊不足。","回讀驗證：用字典與原句重新朗讀，確認替換後語氣、搭配與意思都沒有改變。"]
 item={"id":f"question-chinese-content-ab-iv-2-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ab-iv-2"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究常用詞語境、字音、字形、字義與查證流程。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫 Ab-Ⅳ-2 語境辨識題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-content-ab-iv-2-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
