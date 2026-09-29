#!/usr/bin/env python3
"""Independently rewrite Chinese Ab-IV-3 character-making questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-content-ab-iv-3"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","造字法、字形與語義"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","形聲、會意與部件推論"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","字源、語境與查證"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量從字形部件、聲音線索、語義組合與資料限制要求辨認象形、指事、會意、形聲；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("象形觀察","早期字形若以山峰輪廓描摹實物，最能支持哪項判斷？",["象形：以可見外形表示具體事物","指事：以位置標記抽象關係","會意：由兩個意義部件組合","形聲：由形旁與聲旁分工"],"A","直接描摹山峰等可見外形是象形的主要線索，不能只因字形簡單就判定其他造字法。","先判斷字形是否模擬實物，再排除位置標記、意義組合與聲音線索。"),
 ("指事線索","「上」與「下」用基準線及其相對位置表示方向，哪項觀察最有用？",["是否畫出完整物體外形","是否有標記位置或抽象關係的符號","是否有兩個形旁","是否一定可由聲旁讀出"],"B","上下是抽象位置關係，基準線與相對位置是指事的線索，不是對具體物體的描摹。","找位置、標記與抽象概念線索，避免因字形可畫就誤當象形。"),
 ("會意定義","「人」靠在「木」旁形成「休」的意義；最符合的造字法是？",["象形","指事","會意","形聲"],"C","人與木的部件意義共同形成休息概念，是會意的典型理解方式。","逐一說出部件意義，再檢查整字是否由意義關係合成新概念。"),
 ("形聲分工","「晴」的日部提示意義範圍，青部提供聲音線索；這種分工屬於？",["象形","指事","會意","形聲"],"D","一部提示意義、一部提示讀音，是形聲結構的核心分工。","先把部件分成形旁與聲旁，再確認兩者是否各自承擔意義與讀音線索。"),
 ("部件界線","只看到一個字含有「木」部件，就判斷它一定是形聲字；主要問題是？",["木部永遠只表示讀音","單一部件不能證明整字的造字法，仍需看其他部件與字源資料","所有含木字都屬於會意","現代字形完全沒有任何線索"],"A","單一部件只能提供可能線索，不能決定整字造字法；需觀察其他部件、字義與歷史字形。","把部件提示與造字法結論分開，為『一定』這種全稱判斷尋找反例。"),
 ("對照辨識","下列哪組配對最能區分會意與形聲？",["日—象形；上—指事","休—部件意義合成；晴—形旁與聲旁分工","木—指事；明—只有聲旁","河—會意；森—完全沒有部件意義"],"B","休的部件意義合成與晴的形聲分工形成清楚對照，能直接說明兩種造字思路。","用『意義合成』與『形音分工』兩個判準比較，不只背名稱。"),
 ("聲旁查證","看到一個字的聲旁與另一字相同，想推測讀音時最穩妥？",["直接把兩字讀成完全相同","先把聲旁當線索，再查規範注音、詞語與聲調","只看聲旁的筆畫","因為有聲旁就不用看語境"],"C","聲旁可能提供讀音方向，但聲調、語音演變與規範讀音仍需查證。","先提出聲音假設，再用字典與完整詞語驗證，並注意聲調與例外。"),
 ("形聲理解","遇到不熟悉的形聲字，哪套推理最能幫助理解？",["只看形旁直接決定全部字義","只讀聲旁，不查詞語","形旁提供語意範圍、聲旁提供讀音線索，再放回詞語核對","只依現代字形像不像圖畫"],"D","形旁與聲旁各提供部分線索，詞語與上下文負責確認實際義項與讀音。","先分工拆解，再用詞語、字典與句意交叉核對，不把線索當定論。"),
 ("資料不足","題目只給現代字形，沒有古文字、詞語或讀音資料；關於造字法最合理？",["百分之百判定為形聲","只要看筆畫數就能判定","說明目前只能提出假設，需補充字源或語境資料","任何字都不可能研究造字法"],"A","缺乏歷史字形與語境時，可靠程度有限，應標示不確定並要求更多資料，而非武斷判定。","先盤點現有證據，再寫出可支持的最低限度結論與需要補查的資料。"),
 ("線索限制","同學說有形旁和聲旁就能百分之百確定現代讀音與字義；最恰當的回應？",["形旁與聲旁很有用，但只是線索，仍須查規範讀音、詞義與上下文","完全不能利用部件","只要有聲旁就能確定全部意思","古今讀音一定完全不變"],"B","部件能協助提出假設，但語音演變、多義與詞語搭配使它不能保證現代讀音與字義百分之百正確。","指出部件的有效範圍與限制，再安排字典、語境與字源的交叉查證。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與部件、位置、外形、聲音、意義或資料限制線索。",f"拆解造字：區分描摹、標記、意義組合、形音分工及證據不足；本題核心是「{explanation}」",f"核對正解：選項 {target} 符合造字法定義，並保留部件推論的有效範圍。","排除誘答：檢查是否把單一部件當定論、把聲旁當完整讀音，或以現代字形過度推測字源。","回讀驗證：用字源資料、字典、詞語與上下文重新核對，確認結論的證據強度與限制。"]
 item={"id":f"question-chinese-content-ab-iv-3-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ab-iv-3"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究象形、指事、會意、形聲與部件證據界線。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫 Ab-Ⅳ-3 造字法題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-content-ab-iv-3-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
