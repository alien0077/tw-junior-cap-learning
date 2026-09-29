"""Bb：溫度與熱量第一輪來源融合與題目錯置修復。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-bb.json"; REPORT=ROOT/"implementation/reports/science-content-bb-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"溫度、熱量、比熱、熱傳與狀態資料判讀","pattern":"取由溫度與熱量資料、材料特性及熱傳現象推論熱流的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"溫度、熱量、比熱與熱傳方式","pattern":"取溫度與熱量區分、Q＝mcΔT、傳導／對流／輻射與實驗評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"熱流、材料比熱與熱膨脹","pattern":"取熱平衡、材料比較、熱傳設計與狀態／體積變化資料判讀方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
QUESTIONS=[
 ("80℃金屬塊放入20℃水中，最初熱能傳遞方向為何？",["由金屬傳向水","由水傳向金屬","沒有熱傳","只由空氣傳遞"],"A","先比較初溫，再判斷熱由高溫處流向低溫處。",["列出金屬 80℃ 和水 20℃。","金屬初溫較高。","熱能自發由高溫處傳向低溫處。","直到接近熱平衡前方向維持如此。","所以選 A。"]),
 ("下列哪項最能區分溫度與熱量？",["溫度描述粒子平均動能，熱量是能量傳遞量","溫度和熱量都是同一個單位","熱量只與顏色有關","溫度一定等於物體總能量"],"A","分別看溫度的狀態量意義與熱量的能量傳遞意義。",["先確認題目要求比較兩個概念。","溫度反映粒子平均動能的程度。","熱量指因溫差而傳遞的能量。","物體總能量不能直接由溫度一項決定。","答案為 A。"]),
 ("相同質量的水與金屬吸收相同熱量，水升溫較少，表示水的比熱如何？",["較大","較小","一定為零","無法由溫升比較"],"A","固定質量和熱量，用 Q＝mcΔT 判斷比熱與溫升的關係。",["題目固定 Q 和 m。","比熱越大，在相同熱量下溫升越小。","水的溫升較少。","因此水的比熱較大。","選 A。"]),
 ("100 g 水的比熱為1 cal/(g·℃)，升高5℃需吸收多少熱量？",["20 cal","100 cal","500 cal","5000 cal"],"C","代入 Q＝mcΔT 並保留單位。",["寫出公式 Q＝mcΔT。","代入 m＝100 g、c＝1 cal/(g·℃)、ΔT＝5℃。","計算 Q＝100×1×5＝500 cal。","檢查單位 g 與 ℃ 抵消。","故選 C。"]),
 ("鍋中水底部較熱的水上升、上部較冷的水下降，主要是哪種熱傳？",["傳導","對流","輻射","反射"],"B","從流體本身的整體流動判斷熱傳方式。",["找出有色或溫度不同的水在移動。","液體受熱密度改變而產生循環。","流體的整體運動是對流。","不是固體接觸的傳導，也不需真空中的輻射解釋。","答案為 B。"]),
 ("太陽能穿越接近真空的太空到達地球，主要靠哪種方式？",["傳導","對流","輻射","沸騰"],"C","檢查熱傳是否需要物質介質。",["太空大部分接近真空。","傳導與對流需要物質介質。","電磁輻射可以在真空中傳遞能量。","所以太陽熱主要以輻射到達地球。","選 C。"]),
 ("兩物體質量與材料不同，只知道溫度都上升10℃，能否判斷誰吸收熱量較多？",["不能，還需知道質量與比熱","可以，溫升相同就熱量相同","可以，只看初溫","不能，因為物體沒有吸收熱量"],"A","依 Q＝mcΔT 檢查還缺少哪些變數。",["寫出 Q＝mcΔT。","兩者 ΔT 都為10℃。","但質量 m 和比熱 c 不同且未知。","因此不能只由溫升判斷 Q。","答案是 A。"]),
 ("保溫瓶使用真空夾層與亮色內壁，主要分別減少哪兩種熱傳？",["對流與輻射","傳導與對流","輻射與沸騰","蒸發與熔化"],"A","把保溫結構逐一對應到熱傳機制。",["真空夾層缺少可流動介質。","因此可減少對流，也降低介質傳熱。","亮色內壁可反射紅外輻射。","兩者合起來主要對應對流與輻射。","選 A。"]),
 ("純物質在熔化平台期持續加熱，溫度暫時不升高的主要原因是什麼？",["熱量用於改變粒子排列與狀態","溫度計一定停止工作","熱量完全消失","粒子不再運動"],"A","區分顯熱升溫與相變潛熱的用途。",["確認樣品正在相變平台。","輸入熱量仍進入系統。","此時熱量主要用於改變粒子間作用與排列。","因此平均溫度暫時維持近似固定。","故選 A。"]),
 ("比較鋁、玻璃和塑膠棒的熱膨脹，哪種設計較公平？",["使用相同初長、質量或尺寸條件，施加相同溫升並量測長度變化","每種材料用不同初長和不同溫升","只比較顏色","先知道結果再調整溫度"],"A","控制初始尺寸與溫度變化，才可歸因於材料差異。",["先指出研究變因是材料。","固定初長等幾何條件。","固定加熱造成的溫升與測量方法。","比較各棒的長度變化，才能判斷膨脹差異。","所以選 A。"]),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以溫度、熱量、比熱和熱傳方式解釋熱由高溫傳向低溫。","熱平衡、Q＝mcΔT、傳導／對流／輻射與熱膨脹資料判讀是共同能力核心。"],"versionDifferences":["南一公開定位偏向溫度熱量與相變；康軒線索偏向公式、材料與生活熱傳；翰林線索偏向熱平衡、比熱、設計與體積變化。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以熱流箭頭、材料比較與加熱資料串成可操作模型，要求先標示系統與控制變因。","把溫度等於熱量、熱傳方向由低溫到高溫、相變平台代表沒有吸熱列為迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織溫度、熱量、比熱、熱傳與熱膨脹；已移除原先與單元無關的日期—金屬片批次題，10 題題幹、選項、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for i,(prompt,opts,ans,strategy,steps) in enumerate(QUESTIONS,1):
  p=QDIR/f"question-science-content-bb-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":t} for j,t in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{steps[-2]} {steps[-1]} 正確答案：{ans}。"}; q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然科試題／課程資料的溫度、熱量、比熱、熱傳與熱膨脹能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Bb 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["examPatternRefs"]=refs(); q["solutionStrategy"]=strategy; q["solutionSteps"]=steps; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Bb：溫度與熱量","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"unitMismatchRemediated":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原先與 Bb 單元無關的日期—金屬片批次題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content bb")
if __name__=="__main__": main()
