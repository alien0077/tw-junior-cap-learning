#!/usr/bin/env python3
"""Independently rewrite Chinese common-word recognition questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-common-words-recognition"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","字音、認讀與語境"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","多音字、形音義與閱讀理解"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","詞語認讀、語音辨析與語境"),
]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量常把多音字、形近字、詞義與完整語境結合，要求以詞語而非孤立字形判讀；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("銀行的行","下列哪個詞語中的「行」讀音與「銀行」相同？",["行業","行走","行動","行李"],"A","銀行、行業中的行都讀ㄏㄤˊ，表示商業或組織類別；其他詞多讀ㄒㄧㄥˊ。","先把目標字放回完整詞語，分別朗讀候選，再以詞義與慣用讀音交叉核對。"),
 ("朝夕的朝","「朝夕相處」中的「朝」最接近哪個意思？",["早晨、白天的一端","面向某個方向","朝代名稱","向著某人前進"],"A","朝夕指早晚，朝在此讀ㄓㄠ，和夕相對；不能套用朝代或朝向的義項。","找出同詞中的對偶線索，再用朝與夕的時間關係確認讀音和詞義。"),
 ("重量的重","「重視資料來源」中的「重」應讀哪個音？",["ㄓㄨㄥˋ，表示看得重要","ㄔㄨㄥˊ，表示重新","ㄓㄨㄥ，表示中間","ㄔㄨㄥˋ，表示衝撞"],"A","重視的重讀ㄓㄨㄥˋ，表示看重、認為重要；重新的重才讀ㄔㄨㄥˊ。","先看重後面的詞是視、複或量，再依固定搭配判讀。"),
 ("參差的差","「參差不齊」中的「差」讀音與意思為何？",["ㄘ，表示長短、高低不一致","ㄔㄚ，表示差別","ㄔㄞ，表示差遣","ㄔㄞˋ，表示出差"],"A","參差不齊的差讀ㄘ，形容不整齊，和差別、差遣、出差的讀法與義項不同。","多音字要保留完整詞語，不能把單字最常見讀法直接套上去。"),
 ("參加的參","下列哪句的「參」與「參加」讀音相同？",["參與討論","人參茶","參差不齊","參商二星"],"A","參加、參與的參讀ㄘㄢ，表示加入；人參讀ㄕㄣ，參差讀ㄘ，參商是星宿名稱。","先分辨是加入、植物、形容不齊或星宿，再核對語音。"),
 ("方便的便","「便於攜帶」中的「便」最適合解作什麼？",["便利、容易","糞便","立即、就","便宜"],"A","便於是對某種行動方便、容易；便可表示立即或糞便時，讀音與詞義不同。","把虛詞或實詞放回搭配，觀察它是否修飾於、表示時間或指名物。"),
 ("認讀查證","遇到不熟悉的多音字，哪個做法最可靠？",["先讀完整詞語與句子，再查字典注音並回讀驗證","只看部首就決定讀音","依網路留言最多的讀法直接作答","用自己熟悉的同音字代換"],"A","完整詞語、上下文與可靠字典能共同限制讀音選擇，最後回讀可檢查是否通順。","把認讀判斷做成語境—工具—回讀三步，不讓孤立字形取代證據。"),
 ("詞義證據","要確認「沉澱」在「讓心情沉澱」中的意思，哪項證據最有用？",["看它與心情搭配，理解為情緒慢慢平靜、整理","只看沉字的筆畫數","把它固定解作沉到水底","依詞語長短猜意思"],"A","心情沉澱是引申用法，指情緒平靜與整理；搭配對象能排除物理下沉的字面義。","先找詞語搭配的主語，再用上下文判斷是本義、引申義或專門義。"),
 ("形音辨析","下列哪組字音雖相近，放入句子時不能互相替換？",["辨識／辯論／花瓣","清楚／晴天／心情","全部／全都／完整","快樂／高興／喜悅"],"A","辨、辯、瓣同音或近音但字形與詞義不同，必須依詞語固定搭配選用；其他組多為近義或同類表達。","把相近讀音拆成字形、詞義與搭配三層檢查，而非只憑聲音。"),
 ("閱讀功能","掌握文章中關鍵詞的正確讀音與詞義，最直接有助於什麼？",["理解句子語氣、指涉與段落意思，不被誤讀帶偏","只讓朗讀速度變快，與理解無關","保證能知道作者所有私人經歷","可以不用看上下文"],"A","正確認讀能避免把詞義、語氣或指涉讀錯，但仍須回到上下文；它不是取代閱讀，而是支撐理解。","先說明認讀對理解的具體作用，再保留上下文限制。"),
]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與完整詞語，先判斷題目問讀音、詞義、形音辨析或閱讀功能。",f"找語境證據：觀察搭配、對偶、詞性與前後句，區分古今義或多音字；本題核心是「{explanation}」",f"核對正解：選項 {target}「{answer}」能同時符合詞語慣用讀音與句中語意。","排除誘答：檢查是否只看孤立字、把最常見音硬套、混淆形近字，或忽略本義與引申義的語境差異。","回讀驗證：以字典注音、完整詞語與原句重新朗讀，確認聲音、詞義和段落理解互相一致。"]
 item={"id":f"question-chinese-common-words-recognition-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ab-iv-4"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究多音字、形音義與語境認讀能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫常用詞語認讀題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-common-words-recognition-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
