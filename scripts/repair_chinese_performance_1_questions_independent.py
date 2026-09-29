#!/usr/bin/env python3
"""Independently rewrite Chinese listening and communication questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-performance-1"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","聆聽、重點與語氣"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","口語理解、摘要與回應"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","聆聽紀錄、觀點與行動"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量要求聽取重點、區分事實與推測、辨識語氣與觀點，並將口語內容轉成可行動紀錄；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("聆聽目的","聽校外教學說明前，先確認自己的聆聽目的最主要是為了？",["知道哪些資訊要轉成出發前的準備行動","猜講者的家庭背景","記住每個修辭名稱","判斷講者聲音好不好聽"],"A","聆聽目的會決定要抓哪些重點；校外教學需轉成時間、物品、集合與備案等行動。","先問自己聽完要做什麼，再依目的篩選時間、地點、任務與限制資訊。"),
 ("優先重點","說明會提到集合時間、雨天備案、攜帶物品與活動故事；若要準備出發，最優先記錄哪組？",["故事中的形容詞","集合時間、地點、備案與必帶物品","講者重複的口頭禪","現場誰坐在第一排"],"B","能直接影響出發與安全的時間、地點、備案與物品是行動重點，故事與口頭禪不是首要資訊。","依聽後任務排序：先抓可執行、可查核、與安全相關的資訊。"),
 ("語氣保留","老師說「這個安排也許還能再想想」，聽者不應直接記成什麼？",["老師可能保留意見","安排尚未完全定案","老師已正式宣布否決安排","需要等待更多討論"],"C","也許與還能再想想表示保留與未定案，不能推成已正式否決。","圈出模態與程度詞，判斷確定性，再把記錄寫成與原話相同的強度。"),
 ("事實推論","大家聽完都點頭，若要做聆聽紀錄，哪項最精確？",["全班一定同意方案","可記錄部分人點頭，但不能僅據此確定全班同意","方案已經依法通過","沒有人反對方案"],"D","點頭是可觀察行為，但不能直接推論所有人的內心態度或正式同意。","把看見的動作與對態度的推論分開，為較大的結論保留證據要求。"),
 ("追問資訊","講者說「下週會調整流程」，但沒有日期與負責人；最有效的追問是？",["你喜歡這個流程嗎？","這段故事好不好笑？","請說明確切日期、調整內容與負責人是誰。","為什麼今天不是下個月？"],"A","日期、內容與負責人是把模糊承諾轉成可追蹤行動所需的關鍵欄位。","追問時間、任務、負責人與完成標準，避免只問感受或重複原句。"),
 ("摘要層次","演講先說明社區缺水，再介紹回收雨水的限制，最後呼籲先試辦；最佳摘要是？",["社區缺水，所以應忽略所有限制","回收雨水有助於回應缺水，但需先看限制並以試辦評估","演講只是在介紹缺水數字","講者最喜歡回收雨水"],"B","摘要保留問題、方案限制與最後主張，呈現完整論述方向，而非只摘一個細節。","依問題—方案—限制—主張的順序整理，保留轉折與結論。"),
 ("理由完整","同學說「我反對延長活動，因為回家交通會變得困難」。最完整的記錄是？",["同學反對延長活動，理由是返家交通可能增加困難","同學討厭所有活動","延長活動一定違法","大家都同意同學的理由"],"C","記錄要保留立場與明示理由，『可能』反映交通困難的程度，不能擴大成討厭所有活動。","把說話者的立場、理由與確定程度分開記下，不加入未說出的群體結論。"),
 ("同理回應","朋友分享失敗經驗後說「我現在不想找解法，只想先讓你聽我說」，最合宜的回應是？",["立刻列出五個解決方案","先表示願意聆聽並簡短回應感受，尊重對方暫不求解","責怪對方沒有事先查資料","把話題改成自己的成功經驗"],"D","對方明確提出目前只需要被聆聽，先承接感受比立刻給建議更符合溝通需要。","先確認對方的需求，再用回述與情緒詞表示理解，等對方準備好才討論方案。"),
 ("多方觀點","聽到校方、學生與家長對手機管理的不同說法，整理時最妥當的是？",["只保留校方說法","把三方觀點與各自理由分欄記錄，不先混成同一立場","選按讚最多的說法","刪除互相矛盾的內容"],"A","不同角色可能有不同需求與理由，分開記錄才能保留觀點差異並進一步比較。","先標示說話者與主張，再記理由、證據與未解問題，不以多數或權威直接取代整理。"),
 ("行動紀錄","要把一場公共說明會聽成可供行動的紀錄，哪套方法最完整？",["只記最有趣的故事","記下主旨、關鍵事實、決定、待辦事項、負責人、期限與疑問","只記講者使用的成語","只依記憶寫一段感想"],"B","可行動紀錄要同時涵蓋主旨、事實、決定、待辦、責任、期限與待查疑問，才能支持後續執行。","先用欄位整理聽到的資訊，再回聽或追問缺漏，最後核對每項行動的責任與期限。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與聽者目的、說話者、語氣、理由、期限或行動線索。",f"分層整理：區分原話事實、合理推論、立場與未說出的假設；本題核心是「{explanation}」",f"核對正解：選項 {target} 保留原話的資訊範圍與確定程度，並能支持適當回應。","排除誘答：檢查是否把點頭當同意、保留當否決、個人觀點當全體結論，或急著提供對方未要求的建議。","回讀驗證：用聆聽紀錄重述一次，確認人物、主張、理由與下一步都能回到原話找到依據。"]
 item={"id":f"question-chinese-performance-1-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-performance-1"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究聆聽目的、重點、語氣、觀點、摘要與行動紀錄能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫聆聽與溝通表現題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-performance-1-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
