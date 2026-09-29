#!/usr/bin/env python3
"""Independently rewrite Chinese punctuation-effect questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-punctuation-effects"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","標點、語氣與句讀"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","標點辨識、句意與閱讀理解"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","標點使用、語氣與段落組織"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量把標點放入完整語境，要求判讀停頓、語氣、列舉、轉折與說明層次；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("逗號與句號","班會通知要表達先完成分組、再領取材料，最後才開始製作；下列標點安排最清楚？",["先分組，領取材料，最後開始製作。","先分組。領取材料，最後開始製作。","先分組，領取材料。最後，開始製作？","先分組；領取材料；最後開始製作？"],"A","同一流程中的連續步驟可用逗號分隔，完整通知結束用句號；A能保留先後關係且語氣穩定。","先判斷句內是同一流程還是不同分句，再依停頓強度選標點。"),
 ("問號語氣","老師問：「你已經把來源標在報告最後一頁＿＿」此處最適合用什麼？",["。","！","？","："],"C","句子是直接詢問是否完成，句末用問號才能提示讀者等待回答。","先辨識說話者是在陳述、驚嘆、提問或引出說明，再核對句末符號。"),
 ("驚嘆號分寸","看到校園菜園第一朵花開了，學生興奮地喊：「真的開了＿＿」最適合的標點是？",["。","，","！","；"],"C","驚嘆號可呈現驚喜與強烈情緒，符合學生的興奮喊話；不是一般敘述句的句號。","從動詞與語氣詞找情緒強度，再避免把所有感嘆都當成客觀陳述。"),
 ("冒號引說明","下列哪句最適合用冒號引出後面的具體內容？",["本次調查有三個步驟：設計問卷、發放問卷、整理結果。","本次調查：有三個步驟，設計問卷、發放問卷。","本次調查有：三個步驟設計問卷、發放問卷。","本次調查有三個步驟；設計問卷、發放問卷、整理結果。"],"A","冒號可放在總說後，引出後面的分項說明；A的前後層次最完整。","先找前面是否有總說語，再確認冒號後是否真的是解釋、列舉或具體內容。"),
 ("頓號列舉","校慶攤位準備了＿＿海報、桌牌、抽獎券和回收箱。空格最適合填？",["、","，","；","："],"A","同一層次的並列名詞用頓號分隔，列舉內容前的空格也可用頓號接續。","判斷詞語是否同層並列，再區分頓號、逗號與分號的停頓層級。"),
 ("分號層次","下列哪句適合用分號區隔兩個各自完整、但彼此對照的分句？",["雨停了，操場仍很濕；社團活動因此改到教室。","雨停了；，操場仍很濕。","雨停了，操場仍很濕：社團活動因此改到教室。","雨停了？操場仍很濕；社團活動因此改到教室。"],"A","前後是兩個有相對完整意義的分句，分號能標示比逗號更明顯的層次；A也保留因果關係。","先切出分句，再比較逗號、分號與冒號所需的結構層級。"),
 ("引號範圍","校長提醒「請把走廊保持暢通」，其中引號主要標示什麼？",["校長的直接引語","整段文章的主旨","列舉的三個項目","問句的答案"],"A","引號框住校長實際說出的話，讓讀者知道這是直接引語而非作者轉述。","先看引號內是否是原話，再分辨直接引語、特定名稱或反語等功能。"),
 ("括號補充","公告寫著「集合地點在活動中心（雨天改至禮堂）」，括號內容的功能是？",["補充特殊情況的說明","提出與前文相反的主張","表示讀者正在提問","取代整句的結論"],"A","括號補充雨天時的例外安排，不改變主要集合地點的敘述。","判斷括號內容拿掉後主句是否仍完整，再確認它是補充、註解還是正文。"),
 ("破折號轉折","「我們原本要戶外觀察——午後雷雨突然來了。」破折號在此最主要呈現？",["話題或情況的突然轉折","同層名詞的並列","疑問等待回答","列出三個步驟"],"A","破折號把原定計畫與突發雷雨連接，凸顯情況突然改變；不是列舉符號。","觀察破折號前後的語意是否出現補充、轉折、語氣跳接或解釋。"),
 ("標點與理解","閱讀一段研究報告時，正確標點最直接能幫助讀者掌握什麼？",["句子邊界、停頓、語氣與前後層次","作者所有未寫出的私人想法","文章資料一定全部正確","不必理解詞義也能知道結論"],"A","標點提供句讀與層次線索，能支撐理解，但不能代替詞義查證或證據判讀。","先說明標點實際提供的閱讀線索，再保留它不能取代內容證據的界線。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與句子中的停頓、語氣、列舉或補充線索。",f"拆解句意：先切出分句與層次，再判斷標點要呈現的關係；本題核心是「{explanation}」",f"核對正解：選項 {target} 能讓句界、語氣與前後邏輯同時清楚。","排除誘答：檢查是否把頓號當逗號、把分號當句號、忽略引號範圍，或只依符號外形猜答案。","回讀驗證：把句子朗讀一次，確認停頓位置與讀者理解的語氣、層次完全一致。"]
 item={"id":f"question-chinese-punctuation-effects-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ac-iv-1"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究標點、句讀、語氣與段落層次能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫標點表意效果題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-punctuation-effects-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
