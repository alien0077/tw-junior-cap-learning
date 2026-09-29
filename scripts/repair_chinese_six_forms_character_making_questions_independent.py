#!/usr/bin/env python3
"""Independently rewrite Chinese character-making questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-six-forms-character-making"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","字形、造字與語境"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","字形結構、形音義與閱讀"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","造字法辨識與字形推論"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量從字形部件、字義線索與語境要求辨認造字方式，並區分象形、指事、會意及形聲；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("象形線索","下列哪項最能說明「山」作為早期字形時的造字線索？",["以圖畫山峰外形來表示實物","用聲旁表示讀音","把兩個抽象概念相加","在字形上加指示符號"],"A","象形以描繪事物外形為主要線索，山的早期字形可看出山峰的形狀。","先問字形是否直接模擬可見事物，再排除聲音、組合概念或指示位置的線索。"),
 ("指事線索","「上」的字形用短線標示基準線上方，這種造字思路最接近？",["象形","指事","會意","形聲"],"B","指事用抽象符號或位置標記表示難以直接描繪的概念，上方位置正是此類線索。","找『位置、標記、指示』等抽象提示，不要因字形簡單就誤判為象形。"),
 ("會意組合","「休」由人靠在木旁組成，用來表達休息；下列判斷何者最合理？",["只靠聲旁提示讀音","以兩個部件的意義合成新意","直接描繪一種動物","以符號標示上下位置"],"C","人與木的意義組合出休息情境，是會意的核心：部件意義共同參與新字義。","分別解讀部件，再檢查它們是否以意義組合，而不是只提供讀音。"),
 ("形聲結構","「晴」以「日」提示意義、以「青」提示讀音；這種結構屬於？",["指事","會意","象形","形聲"],"D","形聲字由形旁提示意義範圍、聲旁提示讀音；晴的日與青分工明確。","把部件分成意義線索與聲音線索，再判斷兩者是否形成形聲結構。"),
 ("形旁範圍","看到「河、湖、海」都有水部，最合理的推論是？",["水部通常提供與水或液體相關的意義線索","水部一定精確表示每字的讀音","三字都是象形字","只要有水部就能忽略整個詞語語境"],"A","水部常縮小字義搜尋範圍，提示水或液體相關概念，但不能代替完整字義判斷。","先把形旁當作語意方向提示，再以整字與詞語確認，不過度推論。"),
 ("聲旁限制","形聲字的聲旁最適合被理解為什麼？",["一定決定字的全部意思","提供可能的讀音線索，但讀音仍須查證","只表示字的部首","保證古今讀音完全相同"],"B","聲旁通常提供讀音線索，但受聲調、語音演變與規範讀音影響，不能視為絕對答案。","先利用聲旁提出假設，再用字典注音與完整詞語驗證。"),
 ("不能只看字形","要辨識一個字的造字法，為什麼不能只看現代字形外觀？",["現代字形可能經過演變、簡化或部件變形","所有字都沒有固定部件","字形永遠不能提供任何線索","只要看筆畫數就能知道字義"],"C","字形歷經演變與簡化，現代外觀可能掩蓋早期構形；需結合字源、部件與字義資料。","先承認字形的線索價值，再檢查演變與資料來源，避免只憑像不像下結論。"),
 ("會意語境","「明」由日與月組成，常用來表達明亮；下列說法最恰當的是？",["兩個部件的意義共同形成整字概念","日只提示讀音、月只提示部首","明是單純描繪月亮外形","明的字義與部件完全無關"],"D","日月都參與明亮概念的形成，這是會意式的意義組合線索。","逐一說出部件意義，再看整字是否由它們共同指向新概念。"),
 ("象形與指事","象形與指事最核心的差異是什麼？",["前者描繪具體形體，後者用符號或位置指示抽象概念","前者一定有聲旁，後者一定有形旁","前者只出現在現代字，後者只出現在外來語","兩者完全沒有差別"],"A","象形重在描摹可見事物，指事重在用標記或位置表達抽象關係；這是兩者的核心差異。","比較『描繪形體』與『指示概念』兩個功能，不被字形繁簡或筆畫數干擾。"),
 ("形聲綜合查證","研究「銅」的字形時，看到金部與同聲旁，最完整的說明應是？",["金部可能提示金屬義，同可提供讀音線索，仍須查證現代讀音與詞義","金部決定讀ㄊㄨㄥˊ，同決定全部字義","只要看到金部就能判定任何相關詞義","同是象形部件所以與讀音無關"],"B","金部提供金屬類意義方向，同可能提供讀音線索，但需用字典與詞語查證，不可把線索當定論。","分別標記形旁與聲旁的功能，再以規範資料和完整詞語做最後驗證。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與字形部件、位置、意義或讀音線索。",f"拆解構形：分別說明部件可能提供的功能，再連回整字與語境；本題核心是「{explanation}」",f"核對正解：選項 {target} 同時符合造字法定義、部件功能與查證界線。","排除誘答：檢查是否把形旁當聲旁、把線索當定論，或只憑現代字形外觀硬猜字源。","回讀驗證：以字源資料、字典讀音與完整詞語重新檢查，確認形、音、義的推論都有證據。"]
 item={"id":f"question-chinese-six-forms-character-making-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ab-iv-3"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究象形、指事、會意、形聲與部件查證能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫六書與造字題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-six-forms-character-making-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
