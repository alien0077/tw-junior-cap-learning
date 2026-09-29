#!/usr/bin/env python3
"""Independently rewrite Chinese oral-expression and discussion questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-performance-2"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","口語表達、說明與溝通"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","口語組織、摘要與回應"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","表達策略、觀點與說服"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量要求依受眾調整說明、組織口語重點、尊重回應、澄清歧義、處理異議並以證據說服；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("受眾調整","要向低年級學生說明圖書館借閱規則，哪種說法最適切？",["使用短句、按步驟說明，並舉一個具體例子","只念規章全文，不解釋詞語","用大量專業術語顯示自己熟悉規則","只說『照規定做』"],"A","低年級需要短句、順序與具體例子，才能把規則轉成可操作行動；不是刪掉所有資訊。","先確認受眾的先備知識，再調整詞彙、句長、順序與例子。"),
 ("重點筆記","說明校外教學注意事項時，哪種筆記最能幫助聽眾掌握重點？",["只抄講者每一句話","用時間、地點、物品、備案四欄整理","只記自己覺得有趣的故事","只記最後一句"],"B","四欄能把說明轉成可查找的行動資訊，兼顧完整性與後續使用。","先找聽眾需要採取的行動，再用固定欄位整理資訊與缺漏。"),
 ("理解回應","同學分享社團失誤：「我忘了備份，結果簡報不見了。」哪句回應最合宜？",["你怎麼連這個都會忘？","沒關係，反正大家都不在意。","我懂你一定很慌；下次我們可以一起確認備份流程。","我以前也遇過，所以你不用再說。"],"C","回應先承接情緒與事實，再提出可行協助，不責備、不淡化，也不搶走對方的分享。","先回述對方的情況與感受，再確認對方是否需要建議，最後提出具體支持。"),
 ("尊重提醒","要提醒同學降低走廊音量，哪句兼顧明確與尊重？",["你們真的很沒公德心。","請把音量調低一些，隔壁班正在上課，謝謝。","閉嘴，不要再講了。","我不喜歡你們的聲音。"],"D","D指出具體行動、理由與禮貌語氣，能讓對方知道要改什麼而不把人貼上負面標籤。","把人格評價改成行為描述，再補上影響與清楚請求。"),
 ("澄清歧義","小組說「下週交資料」但有人不確定是週一還是週五，最好的澄清方式是？",["等到截止日再看誰猜對","直接責怪說話的人不清楚","確認日期、時間、檔案格式與提交位置","選最早一天，不必再問"],"A","澄清應把相對時間轉成日期，並確認格式與位置，才能讓每個人依同一要求行動。","把模糊詞拆成日期、時間、成果形式、負責人與提交管道逐項確認。"),
 ("口頭組織","三分鐘介紹校園菜園，哪種組織最容易讓聽眾記住？",["想到什麼就說什麼","先說主旨，再依位置或流程介紹三個重點，最後用一句話收束","只背所有細節，不說主題","先講最遠的歷史，再突然結束"],"B","主旨—三個重點—收束的結構讓聽眾建立預期並記住資訊，不會被細節淹沒。","先決定核心訊息，再把材料分成少數有順序的區塊，最後回扣主旨。"),
 ("公平主持","主持班級會議時，哪種做法最能公平呈現不同意見？",["只讓最會說話的人發言","記錄每方主張與理由，依序給相近時間並請大家確認摘要","把不同意見刪掉以免爭吵","主持人先宣布自己支持的答案"],"C","公平不等於每人說一樣的句子，而是讓各方有發言機會、完整記錄理由並確認摘要沒有扭曲。","先訂發言規則，再分開記主張與理由，最後請各方核對記錄。"),
 ("程度修正","觀眾把「可能減少」聽成「一定消除」，講者最適合怎麼修正？",["說『你們聽錯了』就結束","重述『目前資料只支持可能減少，不能保證完全消除』並指出依據","把所有限定詞刪掉","改說方案百分之百有效"],"D","重述保留可能的程度，明確區分減少與消除，並補證據界線，能修正過度確定的理解。","指出被放大的詞，再用原本的程度詞與證據重新表述。"),
 ("線上報告","線上報告時鏡頭外有聲音，講者想避免聽眾漏掉關鍵資訊，應如何做？",["繼續講快一點","停下確認聲音狀況，重述關鍵句並提供投影片文字或摘要","假設大家都聽到了","只把麥克風關掉不說明"],"A","確認干擾、重述與提供文字替代能降低訊息遺失，讓不同接收條件的聽眾仍能掌握重點。","先處理通道問題，再用口語與視覺兩種方式補回關鍵資訊。"),
 ("說服流程","要說服同學參加閱讀交換活動，哪套口語流程最完整？",["先說共同需求，再提出活動做法與證據，回應疑慮並給出明確參加方式","只說活動很棒，要求大家相信","先批評不參加的人","只列出規則，不說明對聽眾有何好處"],"B","完整說服要連結受眾需求、主張、理由證據、疑慮回應與行動方式，才能讓聽眾評估並參與。","先了解對方在意什麼，再組成主張—理由—證據—回應—行動的口語鏈。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與受眾、目的、主張、理由、語氣或行動線索。",f"設計表達：把內容、對象與溝通任務對齊，區分說明、回應、澄清與說服；本題核心是「{explanation}」",f"核對正解：選項 {target} 同時清楚、尊重、可操作，並保留必要的證據與限制。","排除誘答：檢查是否只顧自己表達、攻擊人格、過度保證，或省略日期、理由、受眾與下一步。","回讀驗證：假設自己是聽眾，確認聽完能知道重點、感受被尊重，並能採取正確行動。"]
 item={"id":f"question-chinese-performance-2-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-performance-2"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究受眾調整、口語組織、澄清、尊重回應、觀點與說服能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫口語表達與論述題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-performance-2-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
