#!/usr/bin/env python3
"""Independently rewrite Chinese learning-content evidence questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-learning-content"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","事實、推論與證據"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","閱讀理解、指涉與推論"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","文本證據、語氣與改寫"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量要求區分直接資訊、推論、語氣、指涉與受眾改寫，並以文本證據限制結論；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("直接事實","實驗紀錄寫著「下午兩點測得盆栽高度 18 公分」，讀者可以直接確認什麼？",["該次測量記錄的時間與數值","盆栽一定是全校最高的植物","植物明天一定會長高","測量者一定很喜歡園藝"],"A","紀錄直接提供下午兩點與 18 公分，其他說法都需要額外證據或預測。","先圈出文本明確寫出的時間、數值與動作，再把未寫出的評價或預測排除。"),
 ("反語語氣","同學遲到三次後，朋友笑著說「你可真準時啊！」最合理的判讀是？",["單純客觀表揚準時","可能帶有反語或揶揄，需結合前文理解","表示朋友不知道時間","直接證明同學今天沒有遲到"],"B","前文多次遲到與『真準時』不一致，語境支持反語或揶揄；不能只按字面當成讚美。","比較字面與前文事實是否衝突，再判斷語氣與說話者態度。"),
 ("閱讀目的","公告先寫集合時間與地點，再列出必帶物品；讀者最應先做什麼？",["找出需要採取的時間、地點與準備行動","猜公告作者的家庭背景","只注意標題顏色","把所有內容改成故事"],"C","公告的功能是讓讀者採取行動，時間、地點與物品是直接可執行的資訊。","先確認文本面向的讀者與目的，再整理能直接轉成行動的欄位。"),
 ("合理推論","紀錄寫「雨停後積水逐漸減少；下午體育課改回操場」，下列哪項較合理？",["雨停後操場永遠不會再積水","操場狀況改善到足以恢復課程，但細節仍需現場確認","全校學生都最喜歡雨天","體育老師一定沒有其他安排"],"D","恢復操場課程可支持狀況改善的有限推論，但不能推成永遠、全校或人物心理等過度結論。","先找文本直接連結，再把推論範圍控制在時間、地點與證據能支持的程度。"),
 ("指涉查證","句子寫「小安把書交給小美，請她放回書架」，『她』若有歧義，最妥當的作法是？",["一律指前面第一個人名","只看『她』這個字就決定","回看動作、性別與上下文，必要時改寫成明確人名","猜作者最熟悉誰"],"A","代詞指涉要依動作與上下文確認；若仍不清楚，改寫人名可避免讀者誤解。","先列出所有可能先行詞，再用語法、語意與上下文排除，必要時消除歧義。"),
 ("定義追蹤","說明文定義「雨水回收是把降雨收集後再利用」，閱讀後最應追蹤哪組資訊？",["收集對象、處理方式與再利用目的","作者喜歡的顏色與食物","文章共有幾個逗號","讀者是否住在山區"],"B","定義提供對象、流程與目的的核心框架，後文應追蹤這些要素如何被具體說明。","把定義拆成名詞、動作與目的，再沿著這三條線索閱讀例子與限制。"),
 ("修正初判","讀者先覺得人物很冷淡，後文卻寫他替同學保密；最佳閱讀方法是？",["堅持第一印象，不看後文","用後文新證據修正初判，重新評估人物動機","只看人物說話次數","把替人保密直接解讀成所有行為都正確"],"C","後文提供新的行動證據，讀者應更新人物理解，但仍需避免把一個行動擴張成全面評價。","記下初判與新證據，再比較兩者，保留能由文本支持的有限結論。"),
 ("受眾改寫","把給教師的實驗室安全公告改寫給低年級學生，哪項最恰當？",["刪去所有安全規則，只保留口號","保留關鍵步驟，用較短句和具體動作說明，並保留警告","加入與實驗無關的笑話","把所有專有名詞改成完全錯誤的詞"],"D","受眾改寫要保留核心安全資訊，同時調整句長、詞彙與動作指示，不能犧牲正確性。","先列不可刪的安全要求，再依讀者年齡調整語言與順序，最後回查資訊是否完整。"),
 ("事實與評價","紀錄寫「今天回收三袋紙類」，學生說「這代表大家很有公德心」；兩句差異是？",["前句是可核對的記錄，後句是延伸評價或推論","兩句都是直接測量數據","前句一定錯，後句一定對","後句完全不需要其他證據"],"A","三袋紙類是可查核的行為與數量；公德心是由此延伸的評價，需更多行為與脈絡支持。","把句子分成可觀察資料與評價，再問評價是否有足夠代表性與其他證據。"),
 ("標題限制","只看到文章標題「新的開始」，沒有正文時，最穩妥的判斷是？",["只能知道標題提供的模糊方向，不能確定全文主旨","可以確定主角、時間與結局","標題一定在反諷","不用正文也能判斷作者立場"],"B","標題線索不足以支持人物、事件、結局或立場等完整結論，應等待正文證據。","先說明標題能提供的最低限度線索，再列出目前無法確認的內容。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與文本中的時間、數值、語氣、代詞、定義或受眾線索。",f"證據分層：區分直接寫出、合理推論、評價與尚待查證的內容；本題核心是「{explanation}」",f"核對正解：選項 {target} 的結論範圍與文本證據完全相稱。","排除誘答：檢查是否把第一印象當事實、把一個例子推廣到全部，或加入文本沒有提供的背景。","回讀驗證：回到原句逐字核對，確認答案能指出直接證據或清楚標示推論界線。"]
 item={"id":f"question-chinese-learning-content-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-learning-content"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究直接資訊、推論、語氣、指涉、受眾與證據界線能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫學習內容辨讀題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-learning-content-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
