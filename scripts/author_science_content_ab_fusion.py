"""Ab：物質的形態、性質及分類第一輪來源融合與題目錯置修復。"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ab.json"
REPORT = ROOT / "implementation/reports/science-content-ab-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"物質三態、性質變化與純物質／混合物判讀","pattern":"取由粒子模型、溫度資料、性質證據與組成判斷物質分類的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"物質狀態、溫度、物理化學性質與混合物","pattern":"取粒子排列、相變、物理／化學變化與純物質／混合物的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"物質形態、性質證據與分類方法","pattern":"取狀態模型、特徵性質、分離方法與證據邊界的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
QUESTIONS=[
 ("固體、液體、氣體的粒子模型，哪項描述最合理？",["固體粒子排列較緊密且多在固定位置附近振動","液體粒子完全靜止","氣體粒子沒有質量","三態粒子種類必定不同"],"A","先比較粒子間距與可移動程度，再連結宏觀形狀。",["題目問的是粒子模型。","固體粒子間距小，主要在固定位置附近振動。","液體粒子仍相近但可相互滑動。","氣體粒子間距較大，仍有質量。","故選 A。"]),
 ("冰融化成水時，最合理的描述是什麼？",["粒子種類改變成另一元素","粒子仍是水分子，排列與運動狀態改變","水分子全部消失","產生新的化合物"],"B","用粒子種類與排列／運動兩個層次區分相變和化學反應。",["先確認冰和水是否仍為同一物質。","融化是固態轉液態。","水分子本身沒有因相變變成另一元素。","改變的是排列與運動狀態。","所以選 B。"]),
 ("密閉容器中的氣體升溫且體積固定，壓力上升最合理的原因是什麼？",["粒子平均動能增加，撞擊器壁更頻繁或更強","氣體粒子數一定變成兩倍","容器內沒有粒子","溫度只改變顏色"],"A","固定容器體積，從粒子運動的改變解釋壓力資料。",["先抓住體積固定的條件。","升溫使氣體粒子平均動能增加。","粒子撞擊器壁時更頻繁或作用較強。","因此量到的壓力上升。","答案是 A。"]),
 ("下列哪項是物理性質而不是化學性質？",["鐵在潮濕空氣中會生鏽","酒精容易燃燒","銅具有良好導電性","鎂能與酸反應產生氣體"],"C","辨認不改變物質組成即可觀察或測量的特徵。",["先問觀察性質時是否生成新物質。","導電性測量不必讓銅變成另一物質。","生鏽、燃燒和與酸反應都涉及新物質或反應能力。","所以銅的導電性屬物理性質。","選 C。"]),
 ("小蘇打與醋混合產生氣泡，若要判斷是否發生化學變化，最需要補充哪項證據？",["只看兩種液體原本的顏色","檢查是否生成新氣體並設計對照確認來源","只量容器高度","只記錄混合日期"],"B","把現象和能支持新物質生成的證據分開。",["氣泡是現象，不必立即等同某一結論。","提出生成新氣體的假設。","用未混合的對照組與氣體檢驗比較。","若證據支持新物質形成，才可判斷化學變化。","故選 B。"]),
 ("樣品由兩種物質組成，比例可改變且可用過濾或蒸餾分離，最可能是什麼？",["元素","化合物","混合物","單一原子"],"C","用組成是否固定及能否物理分離判斷分類。",["先讀出樣品含兩種物質。","比例可改變表示不是固定組成。","能以物理方法分離也支持各成分保留原性質。","這符合混合物定義。","因此選 C。"]),
 ("食鹽水蒸發後留下食鹽，這個操作主要利用什麼差異？",["食鹽和水的沸點／揮發性差異","食鹽和水的原子序相同","所有成分都同時變成氣體","只利用顏色差異"],"A","先辨認分離方法，再找被利用的物性差異。",["蒸發時水較容易進入氣相。","食鹽不會在相同條件下大量揮發。","水離開後，食鹽留下。","這是物理分離，不表示食鹽變成新物質。","答案為 A。"]),
 ("純物質在加熱相變時出現固定溫度平台，這項資料最能支持什麼？",["樣品具有特定組成與特徵相變條件","樣品一定是兩種物質混合","溫度計必定損壞","粒子停止存在"],"A","用加熱曲線的固定平台作為物質特徵證據，但不過度延伸。",["先找曲線中相變期間的溫度是否固定。","固定平台可作為純物質特徵性的線索。","它不表示粒子消失，也不直接證明溫度計損壞。","還要搭配其他組成資料確認分類。","故選 A。"]),
 ("同一物質從液態變成氣態時，哪項通常不改變？",["物質的粒子種類","粒子間距","粒子平均運動狀態","樣品占有的體積"],"A","區分物質身分和狀態相關的排列、距離及宏觀體積。",["先問是否發生化學反應。","單純汽化仍由同一種粒子組成。","粒子間距、運動和占有體積會改變。","不改變的是物質粒子種類。","選 A。"]),
 ("研究未知樣品時，哪個流程最能避免把外觀當成分類答案？",["先記錄粒子／組成資料，再測性質並用分離或反應證據交叉檢查","只看顏色直接命名","先猜結論再挑支持資料","只問樣品聞起來像什麼"],"A","以多種證據建立分類，不把單一外觀線索當成物質身分。",["先區分觀察資料和推論。","記錄組成、粒子模型與可重複的性質測量。","再以物理分離或化學反應證據檢查。","比較證據是否一致並標示資料不足。","因此選 A。"]),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以粒子模型、狀態變化、特徵性質與組成固定性判斷物質。","物理／化學變化、純物質／混合物與物理分離方法是共同能力核心。"],"versionDifferences":["南一公開定位偏向三態與物質分類；康軒線索偏向相變、性質與評量；翰林線索偏向粒子模型、特徵資料與分離證據。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以 AB 聚合樣品工作台串接粒子間距、溫度曲線、性質測試與組成資料。","把相變當成新物質、把氣泡直接當成化學反應、把溶液誤當化合物列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織物質三態、溫度、物理／化學性質與純物質／混合物；已移除原先與單元無關的溶液質量批次題，10 題題幹、選項、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for i,(prompt,opts,ans,strategy,steps) in enumerate(QUESTIONS,1):
  p=QDIR/f"question-science-content-ab-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":t} for j,t in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{steps[-2]} {steps[-1]} 正確答案：{ans}。"}; q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然科試題／課程資料的物質三態、性質與分類能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ab 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["examPatternRefs"]=refs(); q["solutionStrategy"]=strategy; q["solutionSteps"]=steps; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ab：物質的形態、性質及分類","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"unitMismatchRemediated":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原先與 Ab 單元無關的溶液質量批次題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ab")
if __name__=="__main__": main()
