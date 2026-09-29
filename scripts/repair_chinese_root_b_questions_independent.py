#!/usr/bin/env python3
"""Independently rewrite Chinese content-root-B evidence questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-content-root-b"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","證據追問、主張與限制"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","篇章觀點、資料與推論"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","跨段整合、修訂與查核"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量要求追問主張的證據、範圍、限制、段落功能、跨文本資料與指涉清楚度；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("公告逐字證據","公告寫「雨天改在圖書館集合，請七年級先報到」；要查核集合資訊，最直接的證據是？",["公告原句中的地點與年級詞語","其他年級同學的猜測","去年活動的照片","公告張貼處的顏色"],"A","圖書館與七年級直接出現在公告原句，是查核地點與對象的第一層證據。","先逐字圈出主張的關鍵詞，再區分原文證據、背景資料與猜測。"),
 ("讓步證據","「雖然風大，攤販仍固定營業，並加裝備用棚架」中『雖然』如何影響觀點？",["刪除前項阻礙，只保留營業結果","承認風大是限制，再以後文行動說明如何回應","表示風大一定造成停業","只表示事件先後"],"B","讓步結構先承認限制，再呈現攤販的因應行動，讓觀點同時包含困難與回應。","找出雖然與後文的仍、但或行動，說明主張如何經過限制修正。"),
 ("推廣範圍","文章只記錄一個社區的 20 份問卷，卻說「全市居民都支持」；應追問？",["問作者喜歡哪種字體","樣本如何抽取、涵蓋範圍與是否能代表全市","把 20 份問卷複製成更多份","只找支持作者的留言"],"C","樣本抽取、涵蓋範圍與代表性決定局部資料能否推廣到全市，不能只看票數。","先標出主張的範圍，再問資料的對象、數量、抽樣方式與遺漏族群。"),
 ("說明結構","整理一段說明文時，若要讓讀者檢查觀點是否有根據，哪種摘要最好？",["只留下作者的結論","依問題、資料、解釋、限制與結論列出功能","把所有例子混成一段","只抄最長的句子"],"D","把資料與限制保留下來，讀者才能追問結論如何由證據支持，以及還有哪些不確定。","先標示每段功能，再把主張、證據、推論與限制分開寫。"),
 ("修辭與證據","「月光把操場鋪成銀色的路」若用來描寫氣氛，哪項說法正確？",["它直接證明操場真的有銀製道路","它用比喻提供畫面與感受，不能當成物理測量資料","它證明月光亮度固定","它是要求讀者立即行動"],"A","鋪成銀色的路是比喻，支持的是視覺與氛圍理解，不是道路材質或亮度的科學證據。","先判斷句子是字面資訊或修辭，再決定它能支持哪一類閱讀結論。"),
 ("跨文共同條件","比較兩篇節水文章時，哪項資料最能作為共同證據？",["作者都用了相同的開頭句","兩文都記錄相同期間的用水量與計算單位","兩文封面顏色相近","讀者覺得第一篇較有趣"],"B","相同期間與單位讓兩文的用水量可直接比較，是共同證據的必要條件。","先對齊時間、單位、對象與測量方法，再比較結果與結論。"),
 ("可驗證主張","若要把「大家覺得這個方法很好」改成可追問的主張，最適合補上？",["把很好改成非常好","說明受訪對象、評分標準、時間與原始回應","刪掉大家保留很好","加上三個驚嘆號"],"C","受訪對象、評分標準、時間與原始回應讓讀者能檢查主張，而不是只增加語氣。","把模糊主詞與評價拆成可觀察的對象、指標、期間與資料。"),
 ("結尾功能","文字先描述老街，再寫居民保存店家的行動，最後提出「我們願意為這些店留下什麼？」；最後一句最可能？",["重複老街的地點","把前文事例轉成需要讀者思考的開放問題","宣布保存計畫已完成","提供店家的營業時間"],"D","最後的開放問題把描述與行動提升到價值思考，邀請讀者延伸判斷。","看結尾是否回扣前文並提出新的思考方向，再區分結論、提問與資訊補充。"),
 ("限制性回應","「研究指出通勤時間縮短，但資料只來自一所學校」；最合理的回應是？",["直接說明全市通勤都變短","肯定資料提供線索，但把結論限制在該校並等待更多樣本","因為樣本少所以研究完全無用","只引用『研究指出』不看方法"],"A","資料可提供一所學校的線索，但樣本限制使結論不能直接推到全市；應保留並等待更多證據。","先承認資料能支持的局部結論，再明確寫出樣本限制與下一步查證。"),
 ("修訂優先序","文字先說結果、後補原因，且代名詞「他」可能指兩個人；第一個優先處理什麼？",["先改成華麗的開頭","先釐清代名詞指涉，避免讀者無法知道行動者","先刪掉所有原因","先增加形容詞數量"],"B","指涉不明會直接破壞讀者理解誰做了什麼，應先釐清人名或重組句子，再處理順序與語言。","先處理造成理解阻斷的核心歧義，再檢查因果順序、段落結構與文字風格。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for idx,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,4):
 target=TARGETS[idx-4]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與主張、樣本、轉折、修辭、跨文資料或指涉線索。",f"追問證據：把觀點拆成原文證據、推論範圍、限制與可查證欄位；本題核心是「{explanation}」",f"核對正解：選項 {target} 讓觀點與證據範圍相稱，並保留文本的結構或語氣。","排除誘答：檢查是否把修辭當數據、把局部樣本推廣、忽略限制，或用語氣強弱代替證據。","回讀驗證：回到原句與前後段，確認另一位讀者能用同樣資料追出答案，不必依賴個人猜測。"]
 item={"id":f"question-chinese-root-b-{idx:02d}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-b","kg-chinese-learning-content"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究證據追問、主張範圍、跨文本與篇章修訂能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫內容根節點 B 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-root-b-{idx:02d}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
