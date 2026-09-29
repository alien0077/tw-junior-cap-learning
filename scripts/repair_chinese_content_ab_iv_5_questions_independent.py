#!/usr/bin/env python3
"""Independently rewrite Chinese Ab-IV-5 word-usage questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-content-ab-iv-5"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","詞語使用、語意與語氣"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","詞義、搭配與表達分寸"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","常用語詞辨析與語境"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量把常用詞放入完整句子，要求辨析本義與引申義、褒貶、搭配、語氣、程度與查證界線；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("深的引申義","下列哪句的「深」與「文章思想很深」同樣表示理解或程度不淺？",["夜色很深，路燈逐一亮起。","他對這個議題的研究很深，能說明多種影響。","井水很深，取水要小心。","山谷很深，回聲很久才消失。"],"A","研究很深的深是引申義，表示理解、探究程度深入；其他句多指空間或時間。","先看深修飾的對象，再區分空間、時間與抽象程度的義項。"),
 ("沉著語境","面對突如其來的批評，他仍保持＿＿，沒有立刻反駁；最適合？",["沉著","沉重","沉澱","沉沒"],"B","沉著表示鎮定、冷靜，能與沒有立刻反駁的行為搭配；其他詞義不合。","先用後半句的行為判斷人物狀態，再核對詞語的褒貶與搭配。"),
 ("毅力分寸","「他終於完成任務，展現出堅韌的毅力」若改成「固執的毅力」，主要改變？",["由正面稱許轉為可能帶有不顧情況的負面或保留評價","由事實變成疑問","由過去變成未來","詞義完全不變"],"C","堅韌多正面稱許持續努力，固執可能暗示不願調整，語氣評價因此改變。","比較兩個修飾詞的褒貶與適用情境，不只看它們都能和毅力搭配。"),
 ("周延義項","「這項制度需要更周延的規畫，才能照顧不同家庭」中的周延最接近？",["速度很快","周到而完整，考慮面向充分","文字很短","態度強硬"],"D","周延形容考慮周全、沒有遺漏，符合制度需照顧不同家庭的語境。","把抽象形容詞改寫成具體判準，再用句中的不同家庭檢查涵蓋範圍。"),
 ("提醒搭配","「老師＿＿我們在討論前先查證資料」中，最恰當的詞語是？",["提醒","題醒","提省","蹄醒"],"A","提醒表示使人注意並預先告知，能搭配查證資料的行動要求。","先判斷句子需要提醒、命令或描述，再核對同音形近字的規範寫法。"),
 ("查清楚表達","正式報告要表達「事情已經查清楚」，下列說法最適當？",["事情已經查明，相關資料也已附在後面。","事情應該差不多吧。","事情可能被查過。","事情有人聽說過。"],"B","查明是正式且明確表示查證完成的詞，並以附資料支持結論。","先確認報告需要的確定程度與語體，再選能被資料支持的正式表達。"),
 ("聆聽與聽見","「他善於聆聽不同意見」若換成「聽見不同意見」，最可能？",["更強調主動理解與尊重","把主動、有目的的傾聽降成只是接收到聲音","完全不改變語意","表示意見已經被採納"],"C","聆聽含有專注、主動理解的態度，聽見較偏向感官接收，表達的溝通品質下降。","比較兩詞的動作主動性、目的與語氣，再看是否符合人物的溝通行為。"),
 ("開的多義","「他把問題看得很開」與「請把窗戶打開」中的開，何者正確？",["前者是心理態度的引申義，後者是解除關閉狀態的本義","兩者都只表示推動窗戶","前者是錯別字，後者才正確","兩者讀音一定不同且無關"],"D","看得開表示想得通、不計較，是抽象引申；打開窗戶是由關閉到開啟的具體狀態。","先找兩句的受詞與搭配，再比較本義如何延伸到心理態度。"),
 ("未確定跡象","下列哪句最精確表達「結果尚未確定，但已有一些跡象」？",["結果已經完全證實。","結果絕對不可能發生。","結果沒有任何線索。","初步資料顯示可能有效，但仍需更多觀察。"],"A","初步、可能與仍需觀察同時保留跡象與不確定性，沒有過度保證。","圈出程度與限定語，確認句子既沒有把跡象寫成結論，也沒有抹去現有資料。"),
 ("詞典與語境","某詞在字典中有兩個義項，但題目只給詞語本身、沒有完整句子；最合理？",["永遠選第一個義項","指出語境不足，補充例句或上下文後再判斷","兩個義項都可直接當答案","選最常見的意思就不用查證"],"B","缺少句子時無法判斷詞語實際義項，應補足上下文或例句，再依搭配與詞性選擇。","先辨認資訊缺口，再要求能區分義項的上下文，不用直覺取代證據。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與詞語搭配、受詞、程度、褒貶、語體或上下文線索。",f"比較語意：把詞語換成白話，區分本義、引申義、確定程度與語氣；本題核心是「{explanation}」",f"核對正解：選項 {target} 能在完整句子中成立，且詞義與表達分寸相符。","排除誘答：檢查是否只看字面、忽略搭配、把可能寫成確定，或混淆同音形近詞。","回讀驗證：重新朗讀句子，確認替換後的語氣、褒貶、程度與篇章目的都沒有改變。"]
 item={"id":f"question-chinese-content-ab-iv-5-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ab-iv-5"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究常用語詞的詞義、搭配、褒貶、程度與語體查證。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫 Ab-Ⅳ-5 常用語詞使用題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-content-ab-iv-5-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
