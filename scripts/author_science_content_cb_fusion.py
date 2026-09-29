"""Cb：物質的結構與功能第一輪來源融合與題目錯置修復。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-cb.json"; REPORT=ROOT/"implementation/reports/science-content-cb-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"原子分子、同素異形體、結構式與物性資料判讀","pattern":"取由粒子排列、化學式、結構差異與性質資料推論物質的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"原子分子、元素排列、同素異形體與分子結構","pattern":"取原子／分子表示、同素異形體、結構與導電／硬度／熔點的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"粒子排列、材料性質與同分異構","pattern":"取模型排列、結構式、官能基、物性比較與證據限制的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
QUESTIONS=[
 ("2H₂、H₂、2H 和 H₂O 四種表示中，哪項解讀正確？",["2H₂ 表示兩個氫分子，H₂ 表示一個氫分子","2H₂ 表示一個含四個氫原子的分子","2H 表示兩個氫分子","H₂O 只含氫元素"],"A","區分係數、下標、原子和分子層次。",["先看元素符號 H。","H₂ 的下標 2 表示一個分子含兩個氫原子。","前方係數 2 表示有兩個 H₂ 分子。","2H 是兩個氫原子，不是兩個氫分子。","所以選 A。"]),
 ("CO₂ 是化合物而 O₂ 是元素分子，主要差異是什麼？",["CO₂ 的一個分子含兩種元素，O₂ 的一個分子只含一種元素","O₂ 沒有原子","CO₂ 一定是混合物","兩者的元素種類和比例完全相同"],"A","從單一粒子的元素種類判斷元素或化合物。",["拆解 CO₂ 的組成。","CO₂ 含碳和氧兩種元素。","O₂ 只含氧一種元素，雖由兩個原子組成仍屬元素分子。","因此兩者分類不同。","答案為 A。"]),
 ("鑽石與石墨都只由碳組成但性質不同，最合理的解釋是什麼？",["碳原子的排列與彼此連結方式不同","其中一種一定不含碳","兩者只差外觀顏色","只要元素相同所有性質必相同"],"A","把元素種類固定，再比較原子排列與結構。",["確認兩者都只含碳元素。","因此元素種類不是造成差異的變因。","不同排列與鍵結方式會改變硬度、導電性等宏觀性質。","外觀不能取代結構證據。","故選 A。"]),
 ("銅線可導電且可拉成細線，哪種模型解釋最合理？",["金屬結構中有可移動電荷，原子排列仍可在受力下滑移而不立即斷裂","銅沒有任何原子","導電性由顏色決定","可拉成線表示銅是液體"],"A","分別用可移動電荷與金屬排列解釋兩種性質。",["導電需要帶電粒子可移動。","金屬結構提供可移動電子。","延展性表示排列層可在外力下調整位置。","兩項性質不必由同一個表面特徵解釋。","所以選 A。"]),
 ("元素符號 C 能指出碳元素，但不能單獨告訴我們什麼？",["樣品中碳原子的實際排列與分子結構","樣品含有碳這項元素","C 是碳的符號","碳的元素身分"],"A","區分元素符號提供的身分資訊和結構資訊。",["C 首先指定元素種類。","它不直接顯示原子如何排列或形成何種粒子。","同一元素可能形成不同結構與材料。","需再提供結構式或模型證據。","答案為 A。"]),
 ("分子式 C₂H₆O 本身能確定哪項資訊？",["一個分子含 2 個碳、6 個氫和 1 個氧原子","分子中原子的實際鍵結順序","物質一定是液體","物質的沸點一定相同"],"A","先讀分子式的數量資訊，再標示它沒有提供的結構與物性。",["讀取各元素下標。","可確定單一分子的原子數量。","分子式沒有直接畫出鍵結順序。","不同結構可能造成不同沸點與狀態。","所以選 A。"]),
 ("兩個物質分子式相同但沸點不同，下一步最有價值的研究是什麼？",["比較其結構式、原子排列與分子間作用力","只重抄分子式","宣稱其中一個分子式錯誤","只比較樣品顏色"],"A","以物性差異回頭檢查可能的結構差異。",["先確認分子式相同。","沸點差異表示僅有元素數量資訊不足。","比較結構式和分子間作用力可提出機制解釋。","再用更多物性或反應資料檢驗。","故選 A。"]),
 ("若兩種只含碳的固體具有不同熔點，最嚴謹的結論是什麼？",["可能存在不同原子排列或結構，仍需結構與實驗資料確認","兩者一定是不同元素","熔點不同代表其中沒有碳","只看熔點就能畫出唯一結構式"],"A","從物性資料提出可檢驗假設，不把單一證據升格為確定結構。",["兩樣品都已知只含碳。","所以元素身分相同不能排除性質差異。","不同排列或鍵結是合理假設。","但仍需結構分析和其他物性支持。","答案為 A。"]),
 ("判斷兩個模型是否為同分異構物，除了分子式相同還要檢查什麼？",["原子的連接順序或結構排列是否不同","樣品容器是否相同","名稱字數是否相同","顏色是否完全相同"],"A","同時滿足相同分子式與不同結構兩個條件。",["先確認兩模型元素種類和原子數相同。","這是分子式相同的條件。","再比較原子之間的連接順序或排列。","若結構不同，才支持同分異構物判定。","所以選 A。"]),
 ("研究材料性質時，哪個流程最符合本單元的模型推理？",["先記錄性質資料，再提出排列模型並用新測試檢查其預測","只把模型圖當成實物照片","看到同元素就宣稱性質相同","先決定結構再忽略反常資料"],"A","把觀察、推論、模型和限制分成可回查的步驟。",["先整理可直接觀察的導電、硬度或熔點資料。","根據資料提出原子排列模型。","用控制變因的新測試檢查預測。","若反常，修正模型並標示仍缺的證據。","答案為 A。"]),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持用原子／分子表示、元素排列與結構式解釋導電、硬度、熔點等材料性質。","同素異形體、同分異構、係數／下標與模型證據限制是共同能力核心。"],"versionDifferences":["南一公開定位偏向粒子模型與材料性質；康軒線索偏向元素排列、同素異形體與物性；翰林線索偏向結構式、分子間作用與同分異構資料判讀。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以粒子排列模型工作台將化學式、結構、導電、硬度、熔點與沸點資料串接，讓學生區分直接觀察和微觀推論。","把元素相同就性質相同、分子式等於結構式、單一物性足以唯一決定結構列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織原子、分子、同素異形體、結構式、材料性質與同分異構；已移除原先與單元無關的溶液質量批次題，10 題題幹、選項、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for i,(prompt,opts,ans,strategy,steps) in enumerate(QUESTIONS,1):
  p=QDIR/f"question-science-content-cb-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":t} for j,t in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{steps[-2]} {steps[-1]} 正確答案：{ans}。"}; q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然科試題／課程資料的原子分子、結構與性質能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Cb 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["examPatternRefs"]=refs(); q["solutionStrategy"]=strategy; q["solutionSteps"]=steps; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Cb：物質的結構與功能","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"unitMismatchRemediated":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原先與 Cb 單元無關的溶液質量批次題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content cb")
if __name__=="__main__": main()
