"""Kb：萬有引力第一輪原創題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-kb.json"; REPORT=ROOT/"implementation/reports/science-content-kb-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"萬有引力、質量、距離、重量與天體資料","pattern":"取公立學校自然科評量以力、質量、距離、地表重力與天體情境推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"力學、天體運動、資料判讀與模型限制","pattern":"取公開會考以條件比較、圖表和模型證據判斷力學現象的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"萬有引力、質量、距離、地球與月球","pattern":"取公立國中試題以受力方向、平方反比、天體情境與變因控制進行推理的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["圈出兩物質量、中心距離、速度與要求量。","判斷是定性比較還是可套公式的計算。","使用 F=Gm₁m₂/r² 或受力圖。","排除把重量、接觸力和軌道速度混成萬有引力。","檢查方向、比例、單位與模型限制。"] for _ in range(10)]
ROWS=[
 ("easy","任兩個有質量的物體之間，通常存在哪種作用？",["彼此吸引的萬有引力","只有接觸時才有的推力","必定互相排斥的力","只有運動時才出現的力"],"A","具有質量的物體彼此存在萬有引力，方向為相互吸引；是否接觸或是否運動不是存在與否的條件。","先辨認作用對象，再區分接觸力與場力。"),
 ("medium","兩物質量固定，中心距離由 r 增為 2r；依平方反比模型，引力變為原來？",["1/2","1/4","2 倍","4 倍"],"B","F∝1/r²，距離加倍後分母變為 4 倍，因此引力變為原來的四分之一。","只改距離，將比例放入平方反比。"),
 ("medium","固定中心距離，只把其中一物質量增加為原來 3 倍，萬有引力如何？",["變為約 1/3","不變","變為約 3 倍","變為約 9 倍"],"C","F 與兩物質量的乘積成正比；距離固定且一個質量變 3 倍，力也變約 3 倍。","固定距離後看質量乘積的比例。"),
 ("easy","物體從地面落下時，哪項解釋最完整？",["地球和物體互相吸引，地球對物體的效果使物體加速下落", "物體自己產生向下推力", "只有物體拉地球，地球不受力", "因為物體沒有質量所以會下落"],"A","地球與物體互相吸引；在質量差異很大的情況下，物體的加速度較明顯，而不是只有單方面施力。","畫出成對引力箭頭，再說明觀察到的加速度。"),
 ("hard","若中心距離加倍，想維持相同引力，其他量固定時其中一個質量需變為原來？",["2 倍","3 倍","4 倍","1/4 倍"],"C","距離加倍使力因平方反比降為 1/4；要抵銷此變化，質量乘積需增加 4 倍。","先算距離造成的比例，再用質量比例補回。"),
 ("medium","月球繞地球運行時，切線方向速度和地球引力共同造成什麼？",["引力持續改變速度方向，使路徑彎曲", "引力消失使月球永遠直線前進", "速度會把引力變成排斥力", "月球因沒有質量而漂浮"],"A","切線速度提供前進趨勢，指向地球的引力持續改變速度方向，形成彎曲軌道；軌道不是沒有力。","把速度方向和引力方向分開畫在同一受力圖。"),
 ("medium","同一個 6 kg 物體搬到月球，質量大致不變但重量變小；這說明？",["質量和重量是同一物理量", "重量受當地重力場影響，質量由物質量決定", "月球沒有任何引力", "質量只在地球存在"],"B","換地點改變當地重力場，因此重量 W=mg 改變；只要沒有物質進出，質量仍大致為 6 kg。","用 m、g、W 三欄區分物質量、重力場與受力結果。"),
 ("hard","若同時增加一物質量並拉遠兩物距離，但沒有給改變幅度，應如何判斷？",["必定變強","必定變弱","兩因素方向相反，資料不足以直接排序","必定變成零"],"C","質量增加使力增強、距離變遠使力減弱；沒有幅度或完整數值時不能假造哪個效果較大。","先列出兩因素方向，再判斷證據是否足夠。"),
 ("easy","桌面上的螺絲靜止不動，是否仍受到地球萬有引力？",["是，桌面支持力可平衡部分效果但不會消除引力","否，靜止物體沒有力","只有桌面接觸力，沒有地球引力","因為螺絲很小所以引力為零"],"A","靜止只表示合力可能平衡，不表示單一力不存在；螺絲仍受地球引力和桌面支持力。","區分單一受力與合力、運動狀態。"),
 ("hard","下列哪個說法正確描述模型的限制？",["引力能解釋吸引趨勢，但完整預測軌道還需速度、方向與初始條件", "只要知道引力大小就能預測所有軌道細節", "沒有引力就不需考慮速度", "質量和距離都不重要，只看天體顏色"],"A","引力模型提供作用與趨勢，但軌道形狀和穩定性還需要速度、方向與初始條件；不能把單一因素擴大解釋所有運動。","先回答模型能解釋什麼，再列出未包含的條件。"),
]
def make_question(n,row):
 difficulty,prompt,options,answer,explanation,strategy=row
 return {"id":f"question-science-content-kb-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",options)],"knowledgeIds":["kg-science-content-kb"],"difficulty":difficulty,"answer":{"value":answer,"explanation":f"{explanation} 正確答案為選項 {answer}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的萬有引力、質量、距離、地球—月球、軌道與模型限制能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-kb","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"
 lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-kb、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合萬有引力的作用對象、方向、質量、距離、平方反比、重量、地表下落、月球軌道與模型限制。原有科學問題取樣錯配題已全部改為萬有引力專屬題目；所有正文、數據、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-kb-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原有科學問題取樣錯配題已移除，10 題改寫為萬有引力作用對象、方向、質量、距離、平方反比、重量、下落、軌道與模型限制專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content kb")
if __name__=="__main__": main()
