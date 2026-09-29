#!/usr/bin/env python3
"""Independently rewrite Chinese literacy and writing questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-performance-4"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","字音、字形、字義與書寫"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","形音義、字詞與閱讀"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","識字策略、校對與文本"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量要求運用部件、字典、語境、規範字形與校對流程處理陌生字詞，並對抄錄資料保留不確定性；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("形音義查證","遇到不熟悉的「澄清」，哪套方法最能同時確認字音、字形與字義？",["只看部首猜讀音","查可靠字典的注音與義項，再放回完整詞語朗讀並核對字形","依朋友直覺直接寫下來","只抄網路搜尋結果第一行"],"A","字典提供規範注音與義項，完整詞語和字形回讀能檢查實際使用是否正確。","先提出部件線索，再用字典與語境交叉驗證，最後以書寫回讀確認。"),
 ("部件推論","看到陌生字含有「言」部件時，哪項推論最恰當？",["字義一定與說話有關","可能提供與語意相關的線索，但仍需查字形與詞語確認","讀音一定是ㄧㄢˊ","可以不用看上下文"],"B","部件可提供方向，但不能直接決定全部字義或讀音；需結合整字與詞語查證。","把部件當成假設線索，不當成定論，再用字典、詞語與句意排除誤判。"),
 ("形近字辨識","要避免把「辨識」誤寫成形近字，哪項做法最有效？",["只記兩字讀音相同","記住辨、辯、瓣的部件與詞義搭配，並在例句中反覆書寫","選筆畫最少的字","看到相似外形就視為可以互換"],"C","形近字需靠部件、詞義與固定搭配區分，不能只靠聲音或外形。","先比較部件意義，再用完整詞語造句與默寫檢查是否能正確遷移。"),
 ("多音字朗讀","要朗讀「參差不齊」，哪種準備最可靠？",["把參讀成參加的音就好","只看第一個字，不看整個詞","依詞語查規範注音，再在句子中朗讀確認","用最常見的同音字替代"],"D","參差的參、差都有特定詞語讀法，應以規範注音與完整語境確認，不能套用其他詞。","先保留完整詞語，再查音、讀句並比較容易混淆的詞語。"),
 ("詞義判讀","「他仔細地核對資料」中的「仔細」最適切的理解是？",["速度很快","態度謹慎，逐項檢查細節","聲音很小","資料數量很多"],"A","仔細修飾核對的方式，表示謹慎並注意細節，不是速度、音量或數量。","看詞語修飾的對象與動作，再以句中搭配判斷它的語意功能。"),
 ("正式書寫","製作正式名冊時，哪項書寫原則最重要？",["字體越花俏越好","使用可辨識、規範且前後一致的字形，並校對姓名與編號","只要自己看得懂即可","完成後不必保留修改紀錄"],"B","正式名冊重視辨識性、規範性、一致性與資料正確，避免姓名或編號錯誤造成實際影響。","先確定格式與規範，再逐欄核對，最後由另一人或另一輪重新檢查。"),
 ("義項選擇","辭典列出一字三個義項時，如何選出課文中的正確義項？",["永遠選第一個義項","只看字形最像哪一項","把字放回詞語與句子，對照詞性、搭配與上下文","選最長的解釋"],"C","多義字需放回完整語境，依詞性、搭配與前後文判斷，不能只看辭典排列。","先找字在句中的詞性，再用前後文與搭配逐項排除不合者。"),
 ("校對流程","校對一頁手稿時發現兩個疑似錯字，哪個流程最有效？",["看到不順眼就全部改掉","先標記疑處，查字典與原始資料，再逐字回讀並記下修改理由","只問一位同學的直覺","刪掉整句避免判斷"],"D","標記、查證、回讀與記錄理由能保留修改依據，避免把正字誤改或留下無法追蹤的變更。","先區分疑似錯誤與確定錯誤，再以可靠來源逐項確認，不一次大改整頁。"),
 ("古籍抄錄","從掃描影像抄錄古籍資料時，哪項做法最負責任？",["看不清楚的字直接用現代常用字替代","保留版面與異體線索，對模糊處加註並回查其他版本","為了流暢自行改寫句子","只抄自己看得懂的部分"],"A","古籍字形與影像可能有異體、缺損或模糊，應保留證據、標示不確定性並交叉查證。","先忠實抄錄，再標記模糊處與版本差異，最後用其他影本或工具核對。"),
 ("檢核表","要建立自己的識字與寫字檢核表，哪組項目最完整？",["只檢查筆畫數","字形、注音、詞義、詞語搭配、例句與查證來源","只檢查是否寫得漂亮","只記錄考試分數"],"B","完整檢核需涵蓋形、音、義、搭配、語境與來源，才能支持理解與正確使用。","把每個字放進形音義卡片，再加入例詞、例句與來源欄位，定期回測。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與字形、讀音、詞義、資料、語境或校對線索。",f"建立查證流程：先用部件或上下文提出假設，再以字典、原始資料與回讀確認；本題核心是「{explanation}」",f"核對正解：選項 {target} 能同時符合規範、語境與識字書寫的實際目的。","排除誘答：檢查是否只靠直覺、同音或外形，或擅自改寫不確定的資料。","回讀驗證：重新朗讀並逐字比對可靠來源，確認字形、字音、字義及使用位置一致。"]
 item={"id":f"question-chinese-performance-4-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-performance-4"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究形音義、部件、校對、抄錄與識字查證能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫識字與寫字表現題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-performance-4-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
