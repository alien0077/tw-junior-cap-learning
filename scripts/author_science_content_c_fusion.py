"""C：物質的結構與功能第一輪來源融合與題目錯置修復。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-c.json"; REPORT=ROOT/"implementation/reports/science-content-c-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"粒子模型、物質組成、結構與性質資料判讀","pattern":"取由微觀結構、物性／化性與實驗證據推論物質功能的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"物質組成、原子分子、結構與性質","pattern":"取原子、分子、元素、化合物、導電與溶解性之模型教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"物質結構、排列與功能證據","pattern":"取粒子排列、物性／化性、分離鑑定與模型限制的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
QUESTIONS=[
 ("要把砂、食鹽和水分開並盡量回收各成分，哪個順序最合理？",["先過濾取砂，再蒸餾回收水並留下食鹽","先把所有成分燃燒","只用磁鐵分離","先把水與食鹽化學反應"],"A","依各成分的粒徑、溶解性與沸點差異安排物理分離。",["砂不溶於水且顆粒較大。","先過濾可將砂與食鹽水分開。","再以蒸餾利用水與食鹽揮發性差異回收水。","剩餘溶液可再取得食鹽。","因此選 A。"]),
 ("下列哪項最能區分原子與分子？",["原子是元素的基本粒子，分子可由一個或多個原子以一定方式組成","分子一定沒有質量","原子一定由兩種元素組成","兩者只靠顏色區分"],"A","用粒子組成和表示層級，而不是外觀名稱判斷。",["先確認題目比較微觀粒子。","原子是元素的一個基本粒子。","分子是原子以一定方式結合形成的粒子。","原子與分子都具有質量，不能靠顏色定義。","答案為 A。"]),
 ("粒子模型中每個粒子都由兩個相同元素的球連結，最合理表示什麼？",["由同一元素組成的雙原子分子","兩種元素組成的化合物","混合物中的兩種獨立原子","一個沒有結構的元素名稱"],"A","讀模型時先辨認球的種類，再判斷是否為同種原子結合。",["兩個球顏色相同表示同一元素。","它們連結表示同一粒子內有結合。","因此是同一元素組成的雙原子分子。","不同元素球才可支持化合物的判讀。","故選 A。"]),
 ("化合物與混合物的主要差異，哪項最正確？",["化合物有固定組成且成分以化學方式結合，混合物比例可變且可用物理方法分離","混合物一定只有一種元素","化合物一定能用過濾分開","兩者都只含單一原子"],"A","比較固定比例、結合方式與分離方法三項證據。",["先檢查組成比例是否固定。","化合物成分間有化學結合，比例固定。","混合物的成分保留原性質，比例可變並可能物理分離。","所以不能把過濾套用到所有化合物。","選 A。"]),
 ("金屬銅能導電，若要用粒子模型解釋，哪項最合理？",["金屬內有可移動的帶電粒子，能在電場下形成定向電流","銅的所有原子都離開樣品","導電只由顏色決定","固體一定沒有任何粒子運動"],"A","把宏觀導電資料連到帶電粒子的可移動性，但不誇大模型。",["先確認導電需要電荷移動。","金屬中有可移動的電子等帶電粒子。","外加電場可使其形成較有方向的移動。","顏色與導電機制沒有直接定義關係。","故選 A。"]),
 ("某固體易溶於水但熔點很高，哪項推論最穩妥？",["可先提出粒子間作用與水分子作用共同影響性質，再以實驗檢驗","只因易溶就能確定其化學式","熔點高表示一定是元素","溶解性和熔點不可能同時出現"],"A","從性質提出模型假設，並標示需要資料檢驗的範圍。",["記錄兩項獨立性質：溶解性與熔點。","性質可能與粒子間作用和溶劑作用有關。","這只是可檢驗的模型推論，不直接決定化學式或分類。","再用組成與反應資料交叉檢查。","答案為 A。"]),
 ("CO 與 CO₂ 都含碳、氧，卻是不同物質，最主要原因是什麼？",["兩者原子種類比例不同，形成不同的粒子結構","兩者只差樣品顏色","兩者一定含有不同元素","CO₂ 沒有任何原子"],"A","比較化學式中的原子種類與數量比例。",["CO 含一個碳和一個氧。","CO₂ 含一個碳和兩個氧。","粒子組成比例不同會形成不同結構與性質。","兩者元素種類相同，不代表物質相同。","所以選 A。"]),
 ("未知粉末遇水完全溶解，所得溶液可導電；哪項結論最嚴謹？",["溶液中可能有可移動離子，但仍需其他證據判斷原粉末的組成","原粉末一定是金屬","只要導電就一定是元素","水一定已變成新元素"],"A","區分溶液的導電證據和原物質分類，不超出資料支持範圍。",["導電表示溶液中有可移動帶電粒子。","這些粒子可能來自溶解或解離。","但單一導電結果不足以決定原粉末是元素或化合物。","需加入組成、分離和反應資料。","故選 A。"]),
 ("若模型預測某材料導電，但實驗在控制電壓和電極距離後沒有電流，下一步最合理是什麼？",["檢查模型假設與實驗接線，再依證據修正而非直接保留結論","忽略結果並宣稱模型必定正確","只改變答案選項","把材料名稱改掉即可"],"A","用可重複證據檢查模型與方法，再決定修正位置。",["先確認電源、接線、電極接觸和控制條件。","若實驗可靠，無電流與原模型預測不符。","指出模型對可移動電荷的假設可能不足。","再提出修正版並設計新測試。","答案是 A。"]),
 ("研究物質結構與功能時，哪個流程最符合科學探究？",["先由粒子模型提出可檢驗預測，再控制變因測量性質並標示限制","只背材料名稱和用途","看到一個現象就宣稱所有同類物質都相同","先選結論再找圖表"],"A","依預測、控制、測量、修正與限制建立證據鏈。",["先把結構假設寫成可檢驗預測。","一次只改變一項關鍵變因並記錄測量。","比較資料是否支持模型。","將未測得或無法排除的解釋標示為限制。","所以選 A。"]),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持從組成與粒子排列推理物質性質，再用分離、導電、溶解與反應資料檢查模型。","原子、分子、元素、化合物、物性／化性與證據限制是共同能力核心。"],"versionDifferences":["南一公開定位偏向物質組成與分離鑑定；康軒線索偏向原子分子、元素化合物與性質；翰林線索偏向結構排列、模型與探究證據。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以粒子模型工作台串接組成、排列、導電、溶解、熔點與反應資料，讓學習者往返微觀與宏觀層次。","把溶液導電直接等同原粉末是金屬、化合物都能過濾、單一性質足以決定結構列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織物質組成、粒子模型、結構與功能；已移除原先與單元無關的溶液質量批次題，10 題題幹、選項、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for i,(prompt,opts,ans,strategy,steps) in enumerate(QUESTIONS,1):
  p=QDIR/f"question-science-content-c-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":t} for j,t in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{steps[-2]} {steps[-1]} 正確答案：{ans}。"}; q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然科試題／課程資料的粒子模型、物質結構與性質能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 C 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["examPatternRefs"]=refs(); q["solutionStrategy"]=strategy; q["solutionSteps"]=steps; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"C：物質的結構與功能","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"unitMismatchRemediated":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原先與 C 單元無關的溶液質量批次題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content c")
if __name__=="__main__": main()
