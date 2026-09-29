#!/usr/bin/env python3
"""Independently rewrite Chinese content-root-A questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-content-root-a"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","篇章結構、證據與推論"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","篇章理解、字句線索與主旨"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","結構、修辭與可驗證理解"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量要求由段落順序、轉折、字句、樣本、修辭與跨文本資料建立可驗證理解；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("問題與結構","正文先提出問題，依時間順序記錄觀察，最後回到問題作結；讀者最需掌握？",["問題—觀察—回應的篇章推進","文章共有幾個逗號","作者的姓名","每個觀察者的年齡"],"A","開頭問題設定任務，中段觀察提供材料，結尾回應問題，三者構成篇章推進。","先替各段標示功能，再畫出問題如何被觀察與結論回應。"),
 ("開頭結尾","讀者找出文章反覆回答的問題，再比較開頭與結尾的說法，最能判斷？",["全文主線與結尾是否形成回應或修正","作者最常用的標點","文章的字數","每個人物的外貌"],"B","比較開頭問題與結尾回應能檢查主線、答案變化與篇章收束，不是只看形式。","先寫出開頭問題，再找結尾回答、限制或轉化的句子。"),
 ("現象與證據","一段文字先描述現象，再列出兩個可能原因，最後說明仍需資料；最適合的閱讀任務是？",["直接選一個原因當定論","區分觀察、假設與待查證資料","只記住現象的形容詞","猜作者一定支持哪個原因"],"C","現象是直接資訊，原因是可能解釋，最後明示證據不足；讀者需維持這三層差異。","把句子分成已知、可能與待查，再限制結論不要超出文本。"),
 ("公告證據","公告寫「雨天改在圖書館集合，請七年級先報到」；確認地點與對象最直接的證據是？",["公告中的『圖書館』與『七年級』字句","其他班同學的猜測","公告的版面顏色","上次活動的集合地點"],"D","地點與對象直接寫在公告字句中，是比外部猜測或舊資料更直接的證據。","回到原句圈出名詞與對象，再區分直接證據和背景推測。"),
 ("雖然轉折","「雖然風大，攤販仍固定營業，並加裝備用棚架」中『雖然』主要形成？",["時間順序","讓步關係：前項有阻礙，後項仍發生","同義重複","因果已被完全證明"],"A","風大是阻礙條件，仍營業與加裝棚架是未被阻止的結果，形成讓步。","找出雖然與後續仍、但是等搭配，說明前後條件與結果的關係。"),
 ("結論範圍","文章只提到一次「居民投票通過」，便宣稱「全市都支持」；最大問題是？",["句子太短","把局部、有限資料過度推廣成全市結論","居民投票一定沒有意義","全市不可能有任何支持者"],"B","一次居民投票的範圍與樣本不足以代表全市，結論超出資料能支持的範圍。","先標示資料涵蓋誰與多少，再比較結論所宣稱的範圍。"),
 ("說明文整理","整理一段說明文重點時，哪種做法最能保留篇章結構？",["只抄每段第一個名詞","按問題、方法、證據、限制與結論標示段落功能","把所有數字排成與原文無關的清單","只寫自己的感想"],"C","功能標示保留資訊如何推進，能看見方法、證據、限制與結論的關係。","先抓段落主要任務，再用箭頭連結前提、說明、證據與結論。"),
 ("修辭畫面","「月光把操場鋪成銀色的路」中的『鋪成』主要帶來？",["精確測量月光長度","把光照在地面的畫面寫得具體可感","證明操場真的有道路","表示作者在下命令"],"D","鋪成把月光的延展與地面畫面具體化，形成視覺想像，不是字面工程描述。","找本體、動作與畫面效果，再排除把修辭當作事實命題。"),
 ("共同證據","比較兩篇都談節水的文章，哪項最適合作為共同證據？",["兩篇都用了相同的標題顏色","兩篇都提供可核對的用水數據與觀察期間","其中一篇的作者較有名","讀者比較喜歡第一篇"],"A","相同的資料類型、測量期間與可核對數據能支持跨文本比較，標題或喜好不能取代證據。","先找兩文共同的資料欄位與時間範圍，再比較數值與結論。"),
 ("可驗證改寫","若要把「大家覺得這個方法很好」改成可驗證句子，最適合補上？",["一個更有力的形容詞","受訪人數、評分方式、時間與原始回應","作者覺得它很棒","『大家』兩字加粗"],"B","受訪範圍、方法、時間與原始回應讓讀者能檢查『大家』與『很好』是否有依據。","把模糊主詞與評價拆成誰、多少、何時、如何測量及原始資料。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與段落順序、轉折字、直接字句、樣本、修辭或可驗證資料。",f"建立證據鏈：把字句線索與篇章功能、結論範圍連起來，區分事實、推論與效果；本題核心是「{explanation}」",f"核對正解：選項 {target} 能由文本直接或合理地支持，沒有擴大範圍。","排除誘答：檢查是否只憑外部常識、個人喜好、單一細節，或把修辭字面化。","回讀驗證：回到原句與前後段，再確認答案能被另一位讀者用同樣步驟重做。"]
 item={"id":f"question-chinese-root-a-{i:02d}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-a","kg-chinese-learning-content"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究篇章結構、字句證據、主旨、修辭與可驗證理解能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫內容根節點 A 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-root-a-{i:02d}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
