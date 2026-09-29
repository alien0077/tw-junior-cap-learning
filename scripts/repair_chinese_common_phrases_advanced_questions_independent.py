#!/usr/bin/env python3
"""Independently rewrite advanced Chinese phrase questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-common-phrases-advanced"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","成語語境、詞義與搭配"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","成語辨析、語體與閱讀理解"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","詞語使用、褒貶與情境判讀"),]
def refs():
 return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量把成語放入完整情境，要求判讀本義、引申義、褒貶、搭配與語意修正；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("差強人意","社區第一次試辦借書服務，雖仍有排隊問題，但大致完成預定流程；下列哪個成語最適合評價成果？",["差強人意","不刊之論","炙手可熱","萬人空巷"],"A","差強人意是大致可以令人滿意，並非完全不滿意；試辦有缺點但達成基本目標，使用恰當。","先判斷成果是失敗、尚可或極佳，再核對成語常被誤解的褒貶。"),
 ("莫衷一是","評審對兩件作品各有支持理由，討論很久仍無法形成一致結論；這種情況可說是＿＿。",["不置可否","莫衷一是","不言而喻","一蹴可幾"],"B","莫衷一是指各有各的意見，不能得到一致看法，符合評審意見分歧的語境。","抓住『多方意見』與『沒有共識』兩個條件，排除只表沉默或容易達成的詞。"),
 ("不置可否","主持人聽完兩方說法，只表示會再查資料，沒有說贊成或反對；下列何者最準確？",["首當其衝","按圖索驥","不置可否","耳提面命"],"C","不置可否是對事情不表示肯定或否定，主持人暫不表態正符合。","區分『沒有表態』、『不同意』與『意見一致』，不要把沉默過度解讀。"),
 ("一蹴可幾","「新系統已完成安全測試，但仍需長期觀察，不能＿＿。」空格應填？",["不可名狀","莫衷一是","不言而喻","一蹴可幾"],"D","一蹴可幾比喻事情很快就能成功，句中說仍需長期觀察，正是否定快速完成。","先看句子的否定語氣，再以時間與難度線索檢查成語意思。"),
 ("首當其衝","暴雨使河水暴漲，靠近堤岸且地勢低的住戶最先受到威脅；「首當其衝」在此指？",["最先受到衝擊或危險","最有資格參加比賽","最晚完成任務","最受大家稱讚"],"A","首當其衝描述首先承受衝擊或危險，重點是受影響的先後與直接程度，不是排名或稱讚。","找出事件的第一波影響對象，確認成語指風險承受而非一般的優先順序。"),
 ("不可名狀","展覽結束後，觀眾面對震撼的聲光作品，一時＿＿，只能反覆說太難以形容。",["按圖索驥","不可名狀","不刊之論","相敬如賓"],"B","不可名狀指無法用語言說明或形容，與震撼到難以描述的感受相合。","用後面的解釋語句作同義證據，再確認成語修飾的是感受而非人物關係。"),
 ("不言而喻","公告已列出申請資格、截止日期與必備文件，讀者不必另加說明便能明白規則；最適合的成語是？",["不言而喻","莫衷一是","耳提面命","一蹴可幾"],"A","不言而喻是不用說明就能明白，完整公告讓規則清楚可知，符合此義。","檢查訊息是否已經充分清楚，再判斷是『不用多說即可理解』而非『反覆教導』。"),
 ("耳提面命","教練不是只在比賽前責罵，而是平時反覆提醒隊員安全動作並親自示範；這種教導可稱為？",["不置可否","不翼而飛","耳提面命","差強人意"],"C","耳提面命比喻懇切而反覆地教導提醒，符合教練持續示範與叮嚀的情境。","辨識成語對象與語氣：它需要長期、懇切的指導，不是一次批評或不表態。"),
 ("按圖索驥的限制","只照著十年前的校園地圖尋找現在的無障礙入口，最可能出現什麼問題？",["資料與現況可能不符，不能只靠舊圖判斷","一定能立刻找到入口","會把所有入口都變成出口","能保證地圖沒有任何錯誤"],"A","按圖索驥若忽略資料時效與現場查證，可能因地圖過時而找錯；成語的限制正在於不能機械套用線索。","先肯定線索的用途，再檢查資料時間、現場變化與交叉查證的必要性。"),
 ("語意修正","「這項技術仍在測試階段，距離普遍使用還一蹴可幾。」若要保留原意，應如何改寫？",["距離普遍使用還差得遠，不能一蹴可幾","距離普遍使用已不言而喻","大家對普遍使用莫衷一是","技術成果差強人意所以已完成"],"A","原句把仍在測試與一蹴可幾的快速成功矛盾並置；改成『不能一蹴可幾』才能表達尚需時間。","先找出前後語意衝突，再保留句中事實，改正成語的方向與否定關係。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」及人物、事件、程度、時間或語氣線索。",f"建立語境證據：把成語的本義、引申義、褒貶與使用對象逐一對照；本題核心是「{explanation}」",f"核對正解：選項 {target} 能同時符合詞義、搭配與整句語意。","排除誘答：檢查是否只按單字字面、誤解褒貶、混淆成語功能，或忽略句中的否定與限制。","回讀驗證：用白話重述整句，再確認成語的方向、程度與事件條件沒有被改變。"]
 item={"id":f"question-chinese-common-phrases-advanced-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ab-iv-5"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究成語辨析、褒貶、限制與語意修正能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫進階常用語詞題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-common-phrases-advanced-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
