#!/usr/bin/env python3
"""Independently rewrite Chinese main-idea and structure questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-main-idea-structure"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","篇章主旨、段落功能與推論"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","閱讀理解、主旨與結構"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","篇章線索、寓意與證據"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量要求結合段落功能、轉折、反覆線索、事件結果與全文證據判斷主旨及寓意；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("段落功能","閱讀校園菜園文章時，先為每段標記『問題、觀察、解釋、結論』，最主要的幫助是？",["看出各段如何共同推進全文意思","只計算文章有幾個字","直接知道作者的年齡","不用再讀段落內容"],"A","段落功能標記能顯示資訊如何由問題推進到證據、解釋與結論，協助掌握全文結構。","先替各段找主要任務，再把任務串成篇章的推進路線。"),
 ("主旨要素","一篇文章寫居民共同修復老橋，並說明修復過程中如何協調不同意見；最完整的主旨應包含？",["只寫老橋很漂亮","共同修復老橋，以及協作與溝通的意義","只寫文章出現居民","只寫最後一天的天氣"],"B","主旨要同時涵蓋核心事件與作者藉事件呈現的重點意義，不能縮成單一細節。","先找反覆出現的事件，再找事件背後被說明或強調的觀點。"),
 ("轉折線索","文章先列出新措施的便利，接著用『然而』指出弱勢使用者仍有困難；讀者應如何理解？",["後半仍只是重複前半","轉折後通常出現需要調整或重新衡量的重點","全文一定改成反對新措施","然而只表示時間順序"],"C","然而標示觀點轉向，後半對前半的樂觀說法加上限制，是理解作者完整立場的重要線索。","圈出轉折詞，比較前後主張的差異與後半是否修正前半。"),
 ("寓意證據","寓言中烏龜先拒絕炫耀速度，最後靠持續完成長途任務；判斷寓意時最重要的是？",["只看動物名稱","只記第一段的對話","把結尾結果與前面的選擇、行動連起來","猜作者最喜歡哪種動物"],"D","寓意需由角色選擇、持續行動與結尾結果共同推導，不能只憑角色名稱或個人偏好。","先整理角色做了什麼，再檢查結果如何回應前文，最後用適當範圍概括。"),
 ("反覆線索","文章多次出現『把門留一條縫』，結尾又寫孩子終於邀請新同學進教室；這個反覆意象最可能？",["只是增加字數","與接納、保留進入可能的主題形成呼應","表示門的材質很特別","證明所有人都喜歡開門"],"A","門縫在前後情節中反覆出現，從具體動作延伸到接納他人的意義，形成主題呼應。","把重複詞語放回前後段落，比較它的字面功能與情節、主題功能。"),
 ("不佳主旨","下列哪個主旨寫法最不適合概括一篇談『社區如何透過共享工具減少浪費』的文章？",["共享工具需要規劃與信任，能減少重複購買","文章介紹共享工具的做法及其環境意義","第三段有一個居民借到電鑽","社區合作可把個人需求轉成資源共享"],"B","第三段的單一電鑽例子只是細節，不能涵蓋全文的做法、意義與合作觀點。","檢查主旨是否能解釋全文，而不是只對應一個段落或一項例子。"),
 ("結尾結果","寓言結尾寫狐狸雖得到食物，卻因急著炫耀而失去朋友；讀者先應追問什麼？",["狐狸的毛色是什麼","結尾結果如何回應前面的選擇與行動","故事共有幾個逗號","作者住在哪裡"],"C","結尾的失去朋友要與狐狸急於炫耀的行動連結，才能推導出行為與後果的寓意。","把結尾結果與導致結果的關鍵行動配對，再概括可遷移的道理。"),
 ("結構轉折","一篇說明文先介紹雨水回收的優點，後段改談維護成本與使用限制；這種結構通常？",["只增加無關背景","讓讀者看見同一方案的多面向與限制","表示前段全部錯誤","使全文不可能有主旨"],"D","後段轉折補上成本與限制，使讀者從單一優點轉向較完整的評估，而非否定前文。","比較轉折前後的資訊功能，判斷後段是補充限制、修正或完全推翻。"),
 ("全文範圍","若一個主旨只能解釋文章中描述市場聲音的段落，卻無法涵蓋後面人物決定改變消費方式的段落，可能缺少？",["對全文後半行動與意義的整合","更多文章標題裝飾","作者的出生日期","每個字的注音"],"A","主旨若無法解釋後半的行動與意義，表示只抓到局部資訊，缺少跨段整合。","測試主旨能否覆蓋開頭、發展與結尾，對無法納入的段落補回核心概念。"),
 ("寓意範圍","最可靠的寓意答案通常應具備哪項特徵？",["只重述一個角色名字","只使用『做人要好』等空泛口號","能以全文事件與結果支持，且不超出文本證據","一定要猜作者的人生經歷"],"B","寓意需由全文事件與結果支持，並控制在文本能證明的範圍，不能用空泛口號或外加作者私生活。","先列文本證據，再把道理寫成能解釋事件且不過度延伸的一句話。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與段落、轉折、反覆詞、事件結果或全文範圍線索。",f"整理證據：把線索放回開頭、發展與結尾，判斷它們如何共同指向主旨或寓意；本題核心是「{explanation}」",f"核對正解：選項 {target} 能解釋全文主要材料與作者呈現的意義。","排除誘答：檢查是否只抓單一細節、忽略轉折後限制、把個人常識加進文本，或寫成空泛口號。","回讀驗證：逐段對照主旨，確認每個重要段落都能被涵蓋，且結論沒有超出文章證據。"]
 item={"id":f"question-chinese-main-idea-structure-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ad-iv-1"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究主旨、段落功能、轉折、寓意與全文證據能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫篇章主旨結構題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-main-idea-structure-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
