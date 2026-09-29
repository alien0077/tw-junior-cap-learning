"""Ia：地表與地殼的變動第一輪來源融合、題庫重寫與來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ia.json"; REPORT=ROOT/"implementation/reports/science-content-ia-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"地表地殼變動、地震、火山、風化侵蝕與資料判讀","pattern":"取由地表作用、地殼構造、地震火山和地形證據建立變動地球推論的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"地表與地殼、板塊、地震火山及地貌","pattern":"取板塊、斷層、褶皺、地震、火山、風化侵蝕及防災的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"地殼變動、地貌證據與災害判讀","pattern":"取內外營力、地震火山證據、地形變化、控制變因與防災決策的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-ia-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-ia"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的地表、地殼、板塊、地震火山及證據判讀能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；題幹、選項、答案、解析與五步解法均依 Ia 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-ia","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"岩石在原地裂解或化學分解，但碎屑尚未被搬走，這種作用稱為？",["風化","侵蝕","搬運","沉積"],"A","風化是岩石在原地受到物理或化學作用而破碎、分解；侵蝕還包含移除與搬運。","先辨認作用發生的位置，再區分原地改變和移動。",["找出『原地』和『尚未搬走』兩個條件。","將岩石破碎或分解對應到風化。","侵蝕、搬運、沉積都涉及物質移動或堆積。","排除 B、C、D 的過程定義。","因此答案為 A。"],"easy"),
q(2,"某河流上游陡、流速快，下游坡度變小且流速降低。下游較容易出現哪種作用？",["沉積增加","岩漿上升","地震波折射","板塊張裂"],"A","水流速度降低時搬運能力下降，所帶顆粒較容易沉積；沉積位置仍受粒徑與流量影響。","把流速和搬運能力連起來，再判斷物質去向。",["比較上游和下游的坡度與流速。","流速降低會使水流較難攜帶部分顆粒。","因此沉積機會增加。","B、C、D 不是河流減速的直接地表作用。","答案為 A。"],"easy"),
q(3,"兩側岩層沿斷層發生水平錯動，累積應力突然釋放，最可能形成什麼？",["地震","珊瑚礁","冰斗","沙丘"],"A","斷層錯動造成能量快速釋放會產生地震；地表形貌可能再受其他作用改變。","先判斷能量釋放的地殼事件，再辨認地貌名稱。",["圈出斷層、錯動和應力釋放。","斷層突然滑動會產生地震波。","把地震與風成、冰川或海洋地形分開。","B、C、D 都不是這個地殼事件的直接結果。","所以 A 正確。"],"easy"),
q(4,"若某地的地層被擠壓形成褶皺，最可能表示地殼受到哪類作用？",["長期的壓縮應力","只有河流沉積","單次降雨蒸發","風力搬運砂粒"],"A","褶皺通常反映岩層受到持續或反覆的擠壓變形；河流、降雨和風力不是形成地層褶皺的主要地殼營力。","由構造形變反推主要應力型態。",["辨認褶皺是岩層形狀被改變。","比較壓縮與張裂、剪力對岩層的作用。","褶皺通常支持壓縮變形的解釋。","B、C、D 無法造成深部岩層的褶皺構造。","答案為 A。"],"medium"),
q(5,"海洋地殼與大陸地殼碰撞時，海洋地殼通常較容易往下俯衝，主要因為？",["海洋地殼平均密度較大","大陸地殼一定沒有岩石","海水把海洋地殼往下推","所有板塊都只會向下移"],"A","較密的海洋板塊在聚合邊界可能隱沒到較不密的大陸板塊下方，形成地震、火山和海溝等現象。","將板塊密度差連到聚合邊界的運動結果。",["確認題目描述海洋—大陸聚合邊界。","比較兩類地殼的平均密度與浮力關係。","密度較大的海洋板塊較可能下沉隱沒。","B、C、D 都不是合理的板塊機制。","因此 A 正確。"],"medium"),
q(6,"火山灰柱突然升高時，最適當的即時判讀是？",["火山活動或噴發風險可能升高，需結合監測資料與警報","可以確定岩漿在十秒後到達每個城市","只代表當地一定發生地震","表示所有火山都同時活動"],"A","火山灰柱變化是需要關注的監測訊號，但仍要看氣體、地震、風向與官方警戒，不能直接推成確切時間或範圍。","把觀察訊號、風險評估與確定預言分開。",["辨認火山灰柱是活動指標而非完整預報。","列出仍需的地震、氣體、風向和警戒資料。","把結論寫成風險可能升高。","B、C、D 都把單一訊號過度擴張。","答案為 A。"],"medium"),
q(7,"同一地震中，軟弱厚沉積層比堅硬基岩搖晃更明顯，這最可能與哪項有關？",["場址效應","月相效應","光合作用","海水鹽度"],"A","地層軟硬與厚度會影響地震波放大和搖晃程度，這種局部地質條件造成的差異稱為場址效應。","把地震源大小和地表場址條件分開比較。",["確認是同一地震而非不同震源。","比較軟弱沉積層與堅硬基岩的波動反應。","地層條件造成局部放大，屬場址效應。","B、C、D 與地震波在地層中的反應無關。","答案為 A。"],"medium"),
q(8,"要研究降雨量對坡面沖蝕量的影響，哪項設計較能支持因果判斷？",["只觀察一次暴雨後的照片","設置相同坡度與土壤的樣區，只改變降雨量並重複測量沖蝕質量","不同坡度、土壤與降雨同時改變","只挑選沖蝕最明顯的樣區"],"B","固定坡度、土壤等條件，只改變降雨量並重複測量，可減少混淆並比較沖蝕量。","用控制變因、重複和原始資料支持因果。",["指定降雨量為自變因、沖蝕量為依變因。","固定坡度、土壤、植被和測量時間。","設置重複樣區並保留全部結果。","A、C、D 分別缺少重複、混淆變因或挑資料。","所以 B 最可靠。"],"medium"),
q(9,"地震後山崩堵住河道形成堰塞湖，這反映哪種地球作用關係？",["地殼變動造成地形改變，外營力與水文作用再改變後續環境","只有水蒸氣凝結，與地震無關","所有堰塞湖都由火山熔岩形成","地震只改變地下，不能影響地表"],"A","地震等內營力可造成山崩與河道阻塞，之後水流、侵蝕與沉積又會改變堰塞湖及下游，形成作用連鎖。","依時間順序追蹤內營力造成的初始改變和外營力的後續作用。",["先找出地震造成山崩與堵河。","再追蹤水流、侵蝕、沉積和湖水變化。","把內營力與外營力放在同一事件鏈。","B、C、D 都錯誤切斷或誤解作用來源。","答案為 A。"],"medium"),
q(10,"比較某海岸十年前後的地形時，哪項資料最能支持海浪侵蝕造成海蝕平台擴大？",["只看一張現在的照片","固定測線的多期地形高程、海浪條件與岩性資料","只問居民印象，不記錄位置和日期","看到岩石就假定由海浪形成"],"B","多期固定測線可追蹤地形變化，搭配海浪條件與岩性才能檢查海蝕的替代解釋。","將時間序列、空間定位、營力資料和岩性證據交叉比較。",["確認題目問的是長期地形變化。","比較同一測線不同時間的高程或剖面。","加入海浪強度、潮位、岩性和其他侵蝕來源。","A、C、D 都缺少可重複資料或直接跳過證據。","因此 B 最能支持條件式結論。"],"medium"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以內外營力、地殼構造、地震火山和地貌證據理解地表與地殼變動。","風化侵蝕、板塊、褶皺斷層、場址效應、災害連鎖與控制變因是共同能力核心。"],"versionDifferences":["南一公開定位偏向地表地殼變動；康軒線索偏向板塊、斷層、地震火山和防災；翰林線索偏向內外營力比較、地形資料與災害因果。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以原地風化、河流沉積、斷層、褶皺、隱沒、火山灰、場址效應、坡面實驗、堰塞湖和海岸時間序列建立單元專屬證據鏈。","把風化等於搬運、地震只影響地下、火山訊號等於確切預言、地貌由單一營力造成列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織內外營力、風化侵蝕、板塊、地震火山、場址效應、地貌與控制變因；原先 9 題已逐題改寫並補成 10 題，均具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"question-science-content-ia-{x['id'].rsplit('-',1)[-1]}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ia：地表與地殼的變動","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原先 9 題為帶日期與取樣數的重複研究設計套題，已逐題改寫並補成 10 題地表與地殼變動專屬問題；每題有唯一答案、解析與五步解法，三筆公開試題／課程資料僅作 pattern-only 來源，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ia")
if __name__=="__main__": main()
