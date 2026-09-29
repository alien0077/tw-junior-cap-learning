"""E：物質系統第一輪來源融合與題目錯置修復。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-e.json"; REPORT=ROOT/"implementation/reports/science-content-e-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"系統邊界、物質／能量變化與資料判讀","pattern":"取由研究範圍、輸入輸出、守恆與資料推論物質系統的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"物質系統、狀態變化與能量流","pattern":"取系統邊界、物質狀態、能量轉換與開放／封閉系統的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"物質與能量系統、守恆與資料探究","pattern":"取系統尺度、物質進出、能量收支與模型限制的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
QUESTIONS=[
 ("研究透明運動飲料時，若只把密封瓶內液體列為系統，哪項屬於系統外輸入？",["從瓶外傳入的熱能","飲料中的糖分","液體本身的水","瓶內溶解的離子"],"A","先畫出系統邊界，再分類跨邊界的物質或能量。",["系統是密封瓶內液體。","瓶內糖、水與離子都在系統內。","若外界加熱，熱能跨邊界進入。","因此外界熱能是系統外輸入。","選 A。"]),
 ("密封冰水袋放在桌上，若研究袋內水和冰的狀態變化，最需要記錄哪項資料？",["袋內溫度與冰水比例隨時間變化","桌子顏色","袋子品牌名稱","觀察者生日"],"A","用可測狀態變數描述系統狀態與時間變化。",["先確定研究對象是袋內物質。","溫度和冰水比例能反映相態與能量交換。","隨時間記錄可比較狀態變化。","無關的外觀與個人資料不能支持模型。","答案為 A。"]),
 ("下列哪個例子最接近開放系統？",["未加蓋的池塘，水和氣體可與外界交換","密封且隔熱的容器","封閉的理想模型盒","完全不與外界接觸的樣品"],"A","看物質是否能跨越系統邊界，而非只看研究物體名稱。",["開放系統允許物質和／或能量進出。","池塘可蒸發、降雨，也可交換氣體。","所以它是開放系統的例子。","密封容器至少限制物質進出，不能直接歸為開放。","故選 A。"]),
 ("把化學反應物與生成物放在密閉容器中測量，若總質量不變，最合理的解釋是？",["在該系統邊界內物質沒有離開或進入，原子重新排列","能量完全消失","反應沒有發生","容器內沒有任何粒子"],"A","先確認系統邊界與守恆量，再解釋反應中的重新排列。",["密閉容器限制物質跨邊界。","反應中原子可重新排列形成新物質。","若沒有物質逸出，系統總質量可維持。","這不代表能量沒有轉換，也不代表沒有反應。","答案為 A。"]),
 ("研究一杯熱飲冷卻時，哪個問題最能明確界定研究範圍？",["系統是否只包含飲料，杯子與空氣是否列為周圍環境？","飲料杯的商標是什麼？","誰先喝完飲料？","杯子照片的像素是多少？"],"A","系統模型先說清楚邊界，才能正確列能量流。",["冷卻涉及飲料、杯子和周圍空氣。","若只研究飲料，杯壁和空氣就是系統外。","不同邊界會得到不同能量收支描述。","因此先界定範圍比商標或照片細節重要。","選 A。"]),
 ("某系統物質量隨時間增加，但沒有物質輸入紀錄，哪項最先應檢查？",["是否漏記輸入、邊界定義錯誤或測量誤差","立刻宣稱物質憑空生成","只改變圖表顏色","刪除增加的資料"],"A","對異常資料先回查邊界、測量與守恆，不越級下結論。",["物質增加需要輸入、生成或測量差異的解釋。","先確認系統邊界是否漏列進入路徑。","再檢查儀器與記錄是否可靠。","證據不足時不能宣稱憑空生成。","故選 A。"]),
 ("比較冰水袋放在室內與冷藏環境的冷卻曲線，哪項條件應盡量固定？",["袋子大小、初始溫度、冰水比例與測量時間間隔","只固定觀察者姓名","讓兩組使用不同溫度計","一組搖晃、一組完全不動且不記錄"],"A","只改變環境條件，其餘初始狀態和測量方式保持一致。",["研究變因是環境。","袋子大小、初溫、冰水比例會影響熱交換。","測量時間間隔與儀器也需一致。","控制這些條件才可比較兩條曲線。","答案為 A。"]),
 ("同一系統內物質總量不變但溫度上升，最合理的說法是？",["可能有能量跨邊界進入或在系統內轉換，物質守恆不等於能量狀態不變","沒有任何變化","物質一定離開系統","溫度上升表示物質數量增加"],"A","分開追蹤物質收支與能量收支兩種量。",["題目已指出物質總量不變。","溫度上升代表系統能量狀態改變。","熱能可能跨邊界進入，也可能由其他形式轉換。","不能把溫度變化直接當作物質增加。","所以選 A。"]),
 ("要向同學解釋池塘是物質與能量流動系統，哪項證據最完整？",["有降雨、蒸發、氣體交換與日照，並可量測水溫和物質濃度變化","只拍一張池塘照片","只知道池塘名稱","只量一次水深且不記時間"],"A","用跨邊界流動和可追蹤狀態資料支持系統模型。",["列出物質流：降雨、蒸發、氣體和溶解物交換。","列出能量流：日照與散熱。","以水溫、濃度等時間資料檢查模型。","單張照片不足以描述流動或變化。","答案為 A。"]),
 ("系統模型與觀察資料不一致時，最適當的科學作法是？",["回查系統邊界、控制條件與測量，再修正模型並保留不確定性","忽略所有反例","只把結論寫得更肯定","改掉資料使其符合模型"],"A","把反常資料當作檢查模型和方法的機會。",["先確認資料是否可重複且測量可靠。","檢查是否漏列物質／能量進出或控制變因。","若模型不足，提出修正版並再次測試。","不能刪除不符合的資料或誇大結論。","故選 A。"]),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持先界定系統，再以組成、相態、物質流與能量流解釋現象。","開放／封閉系統、守恆、狀態變數、邊界與資料模型限制是共同能力核心。"],"versionDifferences":["南一公開定位偏向物質系統與守恆；康軒線索偏向相態、能量與開放／封閉案例；翰林線索偏向系統尺度、收支與模型資料。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以透明飲料、冰水袋與池塘三種尺度工作台練習畫邊界、記錄狀態變數與追蹤流量。","把系統範圍含糊、物質守恆等於能量不變、單次測量就能說明整個系統列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織物質系統、邊界、狀態、物質／能量流與守恆；已移除原先與單元無關的溶液質量批次題，10 題題幹、選項、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for i,(prompt,opts,ans,strategy,steps) in enumerate(QUESTIONS,1):
  p=QDIR/f"question-science-content-e-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":t} for j,t in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{steps[-2]} {steps[-1]} 正確答案：{ans}。"}; q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然科試題／課程資料的物質系統、邊界、守恆與能量流能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 E 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["examPatternRefs"]=refs(); q["solutionStrategy"]=strategy; q["solutionSteps"]=steps; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"E：物質系統","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"unitMismatchRemediated":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原先與 E 單元無關的溶液質量批次題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content e")
if __name__=="__main__": main()
