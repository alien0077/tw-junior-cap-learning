#!/usr/bin/env python3
"""Independently rewrite Chinese common-phrase usage questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-common-phrases-usage"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","成語語境、詞義與搭配"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","成語辨析、語體與閱讀理解"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","詞語使用、褒貶與情境判讀"),
]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量要求依人物、事件、語氣與搭配判斷成語的本義、褒貶與使用條件；本題採全新校園與公共生活語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("井然有序","志工把報到、分組與器材領取的流程貼成清單，現場進行得＿＿。",["井然有序","首當其衝","不翼而飛","差強人意"],"A","井然有序形容安排整齊、有條理，符合流程清楚且順利進行的情境。","先抓主語和事件，再用成語的核心畫面檢查褒貶與搭配。"),
 ("按圖索驥","研究員依照古地圖與測量資料尋找遺址，這種做法最適合用哪個成語？",["按圖索驥","畫蛇添足","望梅止渴","相敬如賓"],"A","按圖索驥是按照線索或資料尋找目標，這裡不是盲目套用而是依圖與資料查找。","辨析成語時要把字面比喻轉成事件流程，不只看其中一個字。"),
 ("即席","主持人臨時請來賓發表看法，他沒有稿子卻＿＿完成回應。",["即席發言","首鼠兩端","不刊之論","相形見絀"],"A","即席表示臨場、當場，和沒有預先準備稿子的發言搭配自然。","先判斷事件是否臨時發生，再選能描述時間與準備狀態的詞。"),
 ("差強人意","第一版海報雖不完美，但已能清楚呈現日期與地點，成果尚＿＿。",["差強人意","令人髮指","炙手可熱","萬人空巷"],"A","差強人意是大致令人滿意、尚可接受，不是完全不滿意，符合仍能完成溝通任務的情境。","注意成語的實際褒貶常與直覺不同，要用整句成果程度校正。"),
 ("首當其衝","颱風來時，位在低窪地區的地下室＿＿，必須先撤離人員。",["首當其衝","不約而同","鶴立雞群","明日黃花"],"A","首當其衝指最先受到衝擊或承受危險，低窪地下室符合風雨風險的直接情境。","找出誰最先承受事件影響，再判斷成語是否描述風險而非排名。"),
 ("不刊之論","這份報告引用完整資料並清楚說明限制，評審稱其中關於樣本偏差的分析是＿＿。",["不刊之論","不情之請","不速之客","不毛之地"],"A","不刊之論指正確而不可更改的言論，通常用於值得信服的見解；此處資料與限制說明支持正面評價。","先辨認成語的語體和褒貶，再檢查它修飾的是論點還是人物。"),
 ("望其項背","兩支隊伍的成績只差一分，評論說乙隊已＿＿甲隊。",["望其項背","走馬看花","空穴來風","不共戴天"],"A","望其項背表示能夠趕上或接近，兩隊只差一分正符合競爭接近。","辨認成語是否表示接近、落後、超越，並用數據檢查方向。"),
 ("相敬如賓","兩位合作多年的夥伴即使意見不同，仍彼此尊重、耐心聆聽，可說是＿＿。",["相敬如賓","草木皆兵","雞犬不寧","滄海桑田"],"A","相敬如賓形容彼此尊敬，常用於關係和諧的夫妻或相互尊重者，此處可作正向比喻。","先看人物關係與互動態度，再判斷成語的情感色彩和使用範圍。"),
 ("不翼而飛","公告剛貼上，桌上的幾份報名表卻＿＿，工作人員只好重新列印。",["不翼而飛","一帆風順","鞭辟入裡","津津有味"],"A","不翼而飛比喻物品無故消失，符合報名表突然不見而非真的飛走。","遇到比喻成語要從事件結果判斷，不能把字面動作當成真實描述。"),
 ("因地制宜","山區校舍雨季容易濕滑，學校依地形加設止滑條並調整通行路線，做法可稱為＿＿。",["因地制宜","墨守成規","閉門造車","緣木求魚"],"A","因地制宜是依據不同地方的實際條件採取適當措施，山區校舍的調整正符合。","把問題條件與方案對照，檢查成語是否強調依實況調整而非固守或錯用方法。"),
]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與人物、事件、結果及語氣線索。",f"建立詞義證據：把成語的比喻義、褒貶和使用對象與句中情境逐一對照；本題核心是「{explanation}」",f"核對正解：選項 {target}「{answer}」在詞義、搭配與語氣上都能成立。","排除誘答：檢查是否只按單字字面、誤解褒貶、忽略人物關係，或把成語套到不相容的事件上。","回讀整句：用較白話的句子重述成語，再確認原句的時間、程度與情感方向沒有被改變。"]
 item={"id":f"question-chinese-common-phrases-usage-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ab-iv-2"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究成語詞義、褒貶、搭配與語境判讀能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫常用語詞題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-common-phrases-usage-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
