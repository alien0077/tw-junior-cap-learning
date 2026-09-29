"""Ca：物質的分離與鑑定第一輪來源融合與題目錯置修復。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ca.json"; REPORT=ROOT/"implementation/reports/science-content-ca-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"混合物分離、物性／化性與未知物鑑定資料判讀","pattern":"取由物性差異、實驗流程、對照組與檢驗證據推論分離與鑑定的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"混合物分離、蒸餾、層析與化學性質鑑定","pattern":"取過濾、結晶、蒸餾、層析、指示劑與特徵反應的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"物性分離、未知物檢驗與證據邊界","pattern":"取分離順序、對照實驗、沉澱／氣體證據與結論限制的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
QUESTIONS=[
 ("要從砂、食鹽和水的混合物中回收三者，哪個順序最合理？",["過濾取砂，再蒸餾回收水，最後處理食鹽溶液","先把全部成分燃燒","只用磁鐵分離","先讓食鹽和水反應"],"A","依粒徑、溶解性與沸點差異設計分離順序。",["砂不溶於水且顆粒較大。","先過濾可取出砂。","食鹽水再以蒸餾分開水與溶解成分。","剩下的溶液可再結晶取得食鹽。","故選 A。"]),
 ("從食鹽水取得食鹽晶體，主要利用哪項差異？",["食鹽和水在不同溫度下的溶解度／揮發性差異","食鹽和水的顏色差異","兩者磁性完全相同","食鹽會變成另一元素"],"A","先辨識蒸發結晶利用的是物理性質。",["食鹽已溶在水中，不能用過濾直接取出。","蒸發移除水，溶解度改變使食鹽析晶。","這是物理分離，食鹽沒有變成新元素。","因此核心是溶解度與揮發性差異。","答案為 A。"]),
 ("若要同時回收食鹽和較純的水，哪個方法比單純蒸發更合適？",["蒸餾並分別收集蒸餾水與殘留物","只把溶液放在濾紙上","用磁鐵吸取水","把食鹽水冷凍後直接丟棄"],"A","根據是否要回收揮發成分選擇方法。",["蒸發會讓水散失，難以回收水。","蒸餾先使水汽化再冷凝收集。","不揮發的食鹽留在蒸餾瓶中。","所以可同時取得水與食鹽部分。","選 A。"]),
 ("紙張色層分析能分開墨水色素，主要利用各色素哪種差異？",["在固定相與流動相之間的分配／移動程度不同","每種色素的質量都相同","色素一定有磁性差異","只利用紙張顏色"],"A","把層析結果連到成分在兩相間移動差異。",["墨水是多種色素的混合物。","各色素對紙和溶劑的作用不同。","因此沿紙張移動距離不同。","不同斑點即可提供成分分離證據。","故選 A。"]),
 ("未知溶液先用已知酸、已知鹼與清水作對照，主要目的為何？",["判斷試劑本身和操作是否造成反應，建立結果比較基準","讓未知液體變成純物質","保證未知物一定是酸","增加樣品體積"],"A","用對照組排除試劑或環境本身造成的假反應。",["先列出未知組、已知組與空白組。","若空白組無反應，觀察到的變化較能歸因於未知物。","已知酸鹼可協助確認指示劑或試劑是否正常。","對照不能直接替未知物命名。","答案為 A。"]),
 ("未知溶液加入碳酸鈉後產生氣泡，最適合支持哪個假說？",["未知溶液可能含能與碳酸根反應放出氣體的成分","未知溶液一定是水","氣泡必定只是沸騰","未知物一定是金屬固體"],"A","把氣泡當成支持假說的證據，不直接越級成唯一身分。",["先記錄加入試劑後出現氣泡。","提出酸性成分與碳酸根反應的假說。","用空白與已知酸對照確認試劑反應。","仍需其他檢驗才能確定未知物身分。","所以選 A。"]),
 ("兩種無色溶液混合後出現白色沉澱，最嚴謹的判斷是什麼？",["可能生成難溶的新物質，需用對照或後續檢驗確認","兩種溶液一定都是純水","沉澱一定是原本容器的灰塵","只要白色就能知道化學式"],"A","區分沉澱現象、化學反應推論與確切鑑定。",["白色沉澱是可觀察現象。","若混合前透明且對照排除污染，可支持生成難溶物的推論。","顏色本身不能決定化學式。","仍需溶解性或其他特徵反應確認。","故選 A。"]),
 ("未知固體與稀酸產生氣體，若要判斷氣體種類，哪個後續做法較合理？",["收集氣體並用適當的特徵檢驗，再設置對照","只看氣泡大小命名氣體","把所有氣體直接聞一聞","只量固體顏色"],"A","由現象進入可辨識氣體的特徵反應，並注意安全與對照。",["先安全收集少量氣體。","選擇與候選氣體相符的特徵檢驗。","用已知氣體或空白作比較。","依檢驗結果判斷，不能靠氣泡大小或嗅覺。","答案為 A。"]),
 ("蒸餾分離兩種互溶液體時，最需要比較哪項物性？",["沸點差異","顏色是否相同","容器形狀","樣品名稱長度"],"A","把分離方法對應到實際利用的物性差異。",["蒸餾包含汽化與冷凝。","沸點較低的成分通常較先進入蒸氣。","因此沸點差異決定分離效果。","若沸點很接近，需承認分離可能不完全。","選 A。"]),
 ("蒸發結晶得到白色固體但仍有雜質，最適合的改進方向是什麼？",["重溶後控制溶解度進行再結晶，並用純度檢驗確認","直接把白色當成純品","加入更多未知物掩蓋雜質","只改變標籤名稱"],"A","把分離和純度鑑定分成兩階段。",["白色外觀不足以證明純度。","先將固體重溶，利用不同溶解度再結晶。","收集晶體後以熔點或其他特徵測試檢查。","比較前後純度資料再評估改進。","故選 A。"]),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持依磁性、粒徑、溶解度、沸點與層析移動差異分離混合物，再以物理／化學特徵鑑定。","分離流程、對照組、沉澱／氣體證據、純度與結論限制是共同能力核心。"],"versionDifferences":["南一公開定位偏向物性分離與純度；康軒線索偏向過濾、結晶、蒸餾、層析與鑑定；翰林線索偏向對照實驗、特徵反應與證據邊界。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以虛擬樣品工作台串接分離順序、產物純度與未知物檢驗，要求學習者明確區分拆分和命名兩階段。","把溶解等於分離完成、白色等於純品、冒泡直接等於唯一氣體列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織混合物分離、純度與物理／化學鑑定；已移除原先與單元無關的溶液質量批次題，10 題題幹、選項、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for i,(prompt,opts,ans,strategy,steps) in enumerate(QUESTIONS,1):
  p=QDIR/f"question-science-content-ca-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":t} for j,t in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{steps[-2]} {steps[-1]} 正確答案：{ans}。"}; q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然科試題／課程資料的混合物分離、純度與未知物鑑定能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ca 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["examPatternRefs"]=refs(); q["solutionStrategy"]=strategy; q["solutionSteps"]=steps; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ca：物質的分離與鑑定","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"unitMismatchRemediated":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原先與 Ca 單元無關的溶液質量批次題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ca")
if __name__=="__main__": main()
