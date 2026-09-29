#!/usr/bin/env python3
"""Independently rewrite Chinese sentence-pattern questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-sentence-patterns"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","句型、語意與語氣"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","句子功能、推論與表達"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","句型辨識與語境判讀"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量把句型放進生活與閱讀語境，要求辨認事件、判斷、立場、推測及請求功能；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("敘事句","「傍晚，志工把遺失物送到警衛室，並在簿子上留下聯絡方式。」這句主要完成什麼功能？",["交代人物、時間與事件發展","判定某物的定義","表達作者贊成或反對","要求讀者立刻行動"],"A","句子交代傍晚、志工、送遺失物與留下方式，是按事件提供資訊的敘事。","先找時間、人物、動作與事件順序，再判斷句子是在敘述發生了什麼。"),
 ("判斷句","「這份紀錄是目前最完整的版本。」句中說話者主要在做什麼？",["描述一連串事件","對對象作出判定或歸類","請求對方修改文件","推測明天的天氣"],"B","句子用「是」把紀錄判定為目前最完整的版本，核心是對對象作判斷。","尋找主語與判定內容，區分『是什麼』和『做了什麼』。"),
 ("表態句","「我支持先試辦兩週，再依實際數據決定是否延長。」這句最明顯表達？",["單純記錄時間","對人物下定義","說話者的立場與主張","描述物品位置"],"C","我支持……表明說話者的立場，後半句還提出依數據決定的主張。","先圈出支持、反對、應該或希望等立場詞，再找它指向的主張。"),
 ("敘事與判斷","下列哪句屬於敘事句，而不是判斷句？",["這份表格是最後定稿。","校門在八點十分開啟，學生陸續進入。","這項安排很公平。","他是本次活動的主持人。"],"D","B描述開門與學生進入的事件過程，其他句子都在對人事物作判定或評價。","看句子是否有動作與時間推進；有事件發展通常是敘事，不要只看句子長短。"),
 ("可能性","「氣象預報顯示午後可能有雷雨，戶外課程或許需要調整。」這段語氣表示？",["已確定課程取消","對過去事件作完整記錄","提出沒有證據的命令","保留不確定性的推測"],"A","可能、或許都保留不確定性，句子是根據預報提出推測，不是宣布確定結果。","圈出可能、或許、應該等模態詞，再判斷說話者的確定程度。"),
 ("祈使與請求","「請在表單送出前再次確認聯絡電話。」這句的主要功能是？",["要求或提醒讀者採取行動","說明電話的定義","記錄表單已經送出","表達對電話的喜愛"],"B","請……是禮貌的要求，指示讀者在送出前確認資料。","先看句首是否有請、務必、不要等指示詞，再確認行動對象。"),
 ("判斷線索","要辨識「這座橋是社區最早建成的公共設施」的判斷功能，最重要的線索是？",["有地點名詞橋","有「是」把對象與判定內容連結","有社區兩字","句子沒有問號"],"C","「是」把這座橋與『社區最早建成的公共設施』連結，直接形成判斷。","不要只靠名詞或標點猜測，先找主語、繫詞與判定內容的關係。"),
 ("立場強弱","「這個方案也許值得再討論，但目前資料還不足以直接通過。」最準確的理解是？",["說話者完全贊成方案","說話者完全反對方案","說話者沒有任何態度","先保留可能性，同時提出目前的限制"],"D","也許表示保留，資料不足則提出限制；整句不是全盤贊成或反對。","分別標出可能性詞與限制語，再合併判斷立場的方向和強度。"),
 ("事件資訊","若只寫「活動很順利」，讀者最缺少哪種資訊？",["事件如何發生、誰做了什麼及結果依據","句子的主語一定不存在","作者的姓名與年齡","所有標點符號的名稱"],"A","很順利是概括評價，沒有交代人物、行動、時間或結果證據，讀者難以重建事件。","把概括評語拆開，追問誰、何時、做了什麼、結果如何與依據在哪裡。"),
 ("綜合辨識","閱讀「研究小組完成測量後，組長表示這批資料仍需複核，因此建議下週再公布。」下列分析何者最完整？",["全句只有判斷，沒有事件","前半敘述事件，後半包含判斷與建議立場","全句只有命令，要求大家複核","全句只是在描述地點"],"B","完成測量是事件敘述；仍需複核是判斷，建議下週公布則表達後續立場與行動。","依連接詞切分分句，再為每一段標示事件、判斷、推測或立場功能。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」及時間、人物、動作、判定詞、模態詞或立場詞。",f"切分句意：依連接詞與語氣把句子拆成資訊單位，判斷事件、判斷、推測或立場；本題核心是「{explanation}」",f"核對正解：選項 {target} 能對應句子的主要功能與語意強度。","排除誘答：檢查是否只看一個字、把評價當事件、把推測當確定，或忽略句中的限制。","回讀驗證：用白話重述句子，確認人物做了什麼、說話者判斷什麼以及立場強弱都沒有遺漏。"]
 item={"id":f"question-chinese-sentence-patterns-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ac-iv-2"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究句型、事件、判斷、立場與推測能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫句型辨識題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-sentence-patterns-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
