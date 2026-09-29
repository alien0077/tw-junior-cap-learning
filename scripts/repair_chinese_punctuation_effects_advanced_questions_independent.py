#!/usr/bin/env python3
"""Independently rewrite advanced Chinese punctuation-effect questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-punctuation-effects-advanced"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","標點、語氣與句讀"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","標點辨析、語氣與閱讀"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","標點修訂與篇章層次"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量要求依上下文、語氣與分句關係安排標點，並判斷標點改動造成的語意變化；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("問號與反問","「難道我們可以在沒有查證的情況下直接轉發嗎＿＿」句末問號主要造成什麼效果？",["提出反問，促使讀者否定草率轉發","單純列出三項資料","表示句子已經結束但沒有語氣","引出後面的說明"],"A","難道……嗎形成反問，期待讀者思考並否定未查證就轉發的做法。","先找反問詞與預設答案，再判斷問號是在真正詢問還是在加強立場。"),
 ("驚嘆號語境","「警報突然響起，請所有人立刻離開實驗室＿＿」在緊急公告中使用驚嘆號，最需注意什麼？",["可加強急迫語氣，但不能取代清楚的行動指示","一定能讓所有人理解集合地點","會自動證明警報是真實的","可用來表示列舉項目"],"B","驚嘆號能加強急迫或強烈語氣，但公告仍需明確說明行動與地點，符號不能代替資訊。","先說明語氣效果，再檢查內容是否提供可執行的指示與證據。"),
 ("冒號層次","「研究結論只有一項：樣本數不足，不能推論全校。」冒號後的內容主要是？",["新的問句","對前面『一項』的具體說明","三個並列物品","作者姓名註記"],"C","冒號把總說『只有一項』與具體結論連接，後句是前句的內容說明。","看冒號前是否有總說或提示語，再確認後面是解釋、列舉或引用。"),
 ("分號對照","「第一組先完成訪談，仍需整理逐字稿；第二組完成問卷，已開始統計。」分號最清楚呈現？",["同一名詞的列舉","兩個具有內部逗號的對照分句","問句與答案","直接引語的開端"],"D","前後兩組各自包含逗號分隔的內部資訊，分號把兩個平行分句分開，層次比逗號清楚。","先看分號兩側能否各自成為完整分句，再觀察是否存在對照或並列關係。"),
 ("標點改動","把「你已經完成報告。」改成「你已經完成報告？」最直接的語意變化是？",["由陳述已完成改為詢問是否完成","由詢問改為命令","增加列舉項目","改成直接引用"],"A","句號陳述完成的資訊，問號則要求對方確認，說話者的言語行為由陳述轉為提問。","只改一個標點時，比較句子的語氣、預期回應與資訊確定程度。"),
 ("逗號邊界","「如果資料仍未核對，請先保留結論，不要急著發布。」逗號在此最重要的作用是？",["把條件分句與主要請求分開","列出同層名詞","表示強烈驚訝","引出直接引語"],"B","逗號把如果引出的條件與後面的請求切開，讓讀者看見『在什麼情況下』採取行動。","先找連接詞與分句邊界，再看逗號是否標出條件、轉折或補充關係。"),
 ("修訂驗證","修訂一段標點混亂的公告後，哪個做法最能確認標點真的改善理解？",["只計算符號數量是否增加","朗讀並請讀者說出分句關係與應採取的行動","把所有符號都改成逗號","只看版面是否對稱"],"C","朗讀與讀者重述能檢查停頓、語氣、層次及行動要求是否清楚，不能只看符號數量。","先說明修訂目的，再用朗讀、重述與情境回應驗證讀者是否讀懂。"),
 ("括號與正文","「集合地點在圖書館（雨天改至體育館），請攜帶學生證。」若刪去括號內容，最可能遺失什麼？",["主要集合地點","雨天的例外安排","攜帶學生證的要求","句子的主語"],"D","括號補充雨天改地點的例外條件，刪去後讀者會不知道特殊情況如何處理。","比較刪除前後主句，再指出括號提供的是例外、補充還是核心命令。"),
 ("列舉與冒號","「本次評量看三件事＿＿理解、證據與表達。」空格最適合的標點是？",["？","！","：","；"],"A","前面的三件事是總說，後面列出三項具體內容，應以冒號引出說明。","先看前句是否有總括數量，再確認後面是否逐項展開。"),
 ("長句層次","一段文字先說明問題背景，接著列出兩項證據，最後提出限制；讀者可用分號最直接掌握什麼？",["每個字的讀音","不同層級分句與論述階段","作者的出生地","標題的字體大小"],"B","分號可區隔較大的分句層級，幫助讀者看出背景、證據與限制的論述階段。","先找各分句的功能，再用標點層級確認篇章的推進關係。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與標點前後的分句、語氣、層次或例外條件。",f"比較語意：先把標點拿掉或改成另一符號，觀察預期回應與論述關係；本題核心是「{explanation}」",f"核對正解：選項 {target} 能具體說明標點造成的語氣、句界或篇章層次。","排除誘答：檢查是否只按符號外形、混淆列舉與說明，或把語氣效果誤當成內容證據。","回讀驗證：朗讀並用白話重述句子，確認標點安排讓讀者能正確掌握意思與下一步行動。"]
 item={"id":f"question-chinese-punctuation-effects-advanced-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ac-iv-1"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究進階標點、語氣變化、分句層次與修訂驗證能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫進階標點題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-punctuation-effects-advanced-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
