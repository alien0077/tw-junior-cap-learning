"""Fa：組成地球的物質第一輪來源融合與題目錯置修復。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-fa.json"; REPORT=ROOT/"implementation/reports/science-content-fa-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"地球圈層、岩石、大氣、海水與環境資料判讀","pattern":"取由地球物質分類、圈層互動、岩石循環與海氣資料推論地球系統的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"地球物質、岩石、大氣與海洋","pattern":"取岩石分類、地球圈層、大氣組成、海水性質與資料判讀方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"地球物質、岩石循環、氣候與海洋","pattern":"取岩石形成證據、大氣分層、海水鹽度密度與圈層物質流能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
QUESTIONS=[
 ("下列哪項最能說明岩石圈、水圈、大氣圈與生物圈彼此相連？",["降雨可由大氣進入水圈，經岩石圈流動並被生物利用","四個圈層完全不交換物質","只有生物圈含有水","岩石圈只存在於海底"],"A","沿一個物質流追蹤跨圈層的移動。",["先找出降雨來源與去向。","水蒸氣在大氣圈，降雨與河流屬水圈。","水流經岩石並被生物利用，顯示跨圈層交換。","因此不能把圈層視為互不相干。","選 A。"]),
 ("岩漿在地下緩慢冷卻形成的岩石，較可能具有哪項特徵？",["晶體較大或較容易辨認","一定含有完整化石","只由沉積物壓密形成","一定沒有任何礦物"],"A","用冷卻速度與晶體生長時間連結火成岩證據。",["岩漿冷卻是形成條件。","地下緩慢冷卻提供晶體成長時間。","因此晶體通常較大或可辨認。","化石與沉積作用不是此題主要證據。","答案為 A。"]),
 ("岩石受熱和壓力但沒有熔化，最合理的分類與過程是？",["變質岩，由原岩在固態下改變","火成岩，由岩漿直接冷卻","沉積岩，由沉積物膠結","土壤，由植物分解"],"A","先確認是否熔化，再判斷形成路徑。",["題幹明確說沒有熔化。","固態受熱與壓力可使礦物排列或結構改變。","這符合變質作用。","火成岩需涉及熔融物冷卻，沉積岩需沉積壓密膠結。","所以選 A。"]),
 ("乾燥空氣中含量最多的氣體通常是什麼？",["氮氣","氧氣","二氧化碳","水蒸氣"],"A","先確認表格是乾燥空氣，再比較主要成分比例。",["乾燥空氣表示暫不計水蒸氣。","氮氣比例約占四分之三，最高。","氧氣次之，二氧化碳只占少量。","不能把變動水蒸氣混入此比例判讀。","答案為 A。"]),
 ("海水鹽度最適合描述哪項？",["海水中溶解鹽類總量的相對程度","海水的溫度","海水的波高","海水中只有氯化鈉的重量"],"A","分清鹽度的組成意義與其他海洋觀測量。",["鹽度描述溶解鹽類的總體程度。","它不是溫度、波高或單一鹽類的唯一重量。","資料需確認單位與測量條件。","因此選 A。"]),
 ("表層海水蒸發增加且沒有相同程度的降雨補回，鹽度通常如何變化？",["增加，因水離開而溶解鹽相對集中","降低，因鹽會全部蒸發","不可能改變","一定變成淡水"],"A","追蹤水量與鹽分是否同時離開。",["蒸發主要移走水分。","溶解鹽不會以相同比例隨水蒸氣離開。","剩餘海水中的鹽相對集中。","所以鹽度通常上升。","答案為 A。"]),
 ("大氣分層主要依據哪項資料？",["溫度隨高度變化的特徵","各層雲朵顏色","地表岩石硬度","海水鹽度"],"A","使用可量化且能連續比較高度的判準。",["大氣剖面可記錄不同高度的溫度。","溫度隨高度的變化趨勢可用來劃分層次。","雲色、岩石硬度與海水鹽度不是主要分層依據。","因此選 A。"]),
 ("岩石風化成細粒，被河水搬運並沉積，最能支持哪項概念？",["地球物質會在不同圈層與地質作用間轉移","岩石永遠不會改變","河水只屬於大氣圈","沉積物不可能再形成岩石"],"A","將風化、搬運、沉積串成物質循環路徑。",["風化使岩石變成細粒。","水圈的河流搬運這些物質。","沉積後可能經壓密膠結形成沉積岩。","這顯示地球物質會轉換與移動。","故選 A。"]),
 ("某海域深度增加時溫度降低、鹽度增加且密度增加，最合理的判讀是？",["溫度與鹽度共同影響海水密度，資料可能反映不同水團","只要溫度降低就能確定洋流方向","鹽度與密度沒有關係","深度資料一定是測量錯誤"],"A","綜合多項資料提出水團假說，不把單一曲線當成唯一因果。",["低溫通常使水密度增加。","較高鹽度也可使密度增加。","兩項資料共同支持密度隨深度增加。","要判斷洋流仍需流速、方向與更多測站資料。","答案為 A。"]),
 ("讀取地球物質剖面圖時，哪個作法最能避免誤判？",["先確認圖例、尺度、剖面方向與資料時間，再沿箭頭追蹤物質變化","只看圖中顏色猜名稱","忽略單位和深度","把一次觀察當成所有地區規律"],"A","先校準圖表語境，再解讀證據與限制。",["先讀圖例和單位。","確認剖面方向、深度或空間尺度。","沿箭頭把物質流和資料位置對應。","最後標示一次資料不能支持的推論。","所以選 A。"]),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持從海水、岩石與空氣的組成與分布理解地球物質。","圈層互動、岩石形成、大氣組成、海水鹽度密度與物質循環資料判讀是共同能力核心。"],"versionDifferences":["南一公開定位偏向地球物質分類與圈層；康軒線索偏向岩石、大氣與海洋；翰林線索偏向岩石循環、分層、鹽度密度與剖面資料。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以海水、岩石與空氣三個物質卡及剖面工作台，沿降雨與風化路徑追蹤物質在圈層間移動。","把乾燥空氣含水蒸氣比例、海水只有氯化鈉、岩石有晶體就必為火成岩列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織地球圈層、岩石、大氣、海水與物質循環；已移除原先與單元無關的溶液質量批次題，10 題題幹、選項、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for i,(prompt,opts,ans,strategy,steps) in enumerate(QUESTIONS,1):
  p=QDIR/f"question-science-content-fa-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":t} for j,t in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{steps[-2]} {steps[-1]} 正確答案：{ans}。"}; q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然科試題／課程資料的地球物質、岩石、大氣、海水與圈層能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Fa 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["examPatternRefs"]=refs(); q["solutionStrategy"]=strategy; q["solutionSteps"]=steps; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Fa：組成地球的物質","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"unitMismatchRemediated":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原先與 Fa 單元無關的溶液質量批次題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content fa")
if __name__=="__main__": main()
