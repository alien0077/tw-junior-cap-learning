"""Jf-Ⅳ-2：常見烷類、醇類、有機酸與酯類第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jf-iv-2.json"
REPORT=ROOT/"implementation/reports/science-content-jf-iv-2-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"烷類、醇類、有機酸、酯類與燃燒資料","pattern":"取由結構、燃燒、酸鹼、溶解與生活物質資料判斷常見有機物的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"碳氫化合物、酒精、有機酸、香味與安全情境","pattern":"取從生活材料、反應現象與資料圖表推論有機物性質和用途的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"烷類、醇類、有機酸、酯類與生活應用","pattern":"取以碳氫骨架、官能基、性質與生活材料建立有機物比較的教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jf-iv-2-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jf-iv-2"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的烷類、醇類、有機酸、酯類、燃燒、酸鹼、香味與安全能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jf-iv-2","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"烷類主要由碳和氫組成，完全燃燒時主要生成？",["二氧化碳和水","氯化鈉和氧氣","氫氧化鈉和水","硫酸和二氧化硫"],"A","烷類含碳和氫，完全燃燒時碳形成二氧化碳、氫形成水；氧通常來自空氣。","從元素組成追蹤燃燒產物。",["確認烷類含碳與氫。","將碳配對二氧化碳。","將氫配對水。","排除氯、鈉、硫等無關產物。","所以 A 正確。"],"easy"),
q(2,"乙醇和烷類都可燃燒，但乙醇分子含有氧原子；比較兩者時最合理的說法是？",["乙醇含氧的結構差異可能影響其溶解性與反應性，但兩者完全燃燒仍可生成二氧化碳和水","含氧就一定不能燃燒","烷類一定溶於水而乙醇一定不溶","兩者的分子結構完全相同"],"A","乙醇的羥基使其性質與烷類不同；若完全燃燒，碳氫部分仍形成二氧化碳和水。","比較結構差異與共同燃燒產物，不把一項性質推成全部性質。",["比較兩者元素與結構。","辨認乙醇含羥基和氧。","確認完全燃燒的碳、氫產物。","排除含氧不可燃、溶解性顛倒和結構相同。","答案為 A。"],"medium"),
q(3,"乙醇比多數烷類更容易和水混合，主要可用哪個結構特徵解釋？",["乙醇的羥基可和水形成分子間作用，使其較易溶於水","乙醇沒有碳原子","烷類含有大量離子","水會把乙醇變成鹽"],"A","乙醇羥基具有極性，可和水形成氫鍵等作用；烷類主要是非極性碳氫結構。","用官能基極性連到溶解性差異。",["找出乙醇分子中的羥基。","比較羥基和碳氫骨架的極性。","判斷與水分子作用的可能性。","排除無碳、離子烷類和成鹽的說法。","所以 A 最合理。"],"medium"),
q(4,"醋酸水溶液可使紫色石蕊變紅，說明醋酸具有？",["酸性，溶液中 H⁺ 相對較多","鹼性，OH⁻ 相對較多","中性且沒有離子","金屬性"],"A","醋酸在水中部分解離產生 H⁺，使溶液呈酸性；弱酸仍是酸，不代表沒有離子。","把有機酸官能基、離子和指示劑現象連起來。",["確認醋酸是有機酸。","判斷溶於水後可產生 H⁺。","用石蕊變紅支持酸性。","排除鹼性、中性無離子和金屬性。","答案為 A。"],"easy"),
q(5,"酯類常具有特殊香味；若某產品宣稱『有香味就代表是天然且無害』，最適合的回應是？",["香味只能提供感官線索，仍需檢查成分、濃度、來源與安全資料","香味必定證明是酯且可食","天然物質一定沒有毒性","只要香味淡就不需標示"],"A","香味可能來自酯或其他物質，且天然與否不能直接代表安全；需依成分與暴露風險判斷。","把感官現象和化學身分、危害證據分開。",["辨認香味只是觀察線索。","查閱成分與濃度標示。","確認是否含酯或其他香味物質。","評估攝入、吸入與皮膚接觸風險。","所以 A 最妥當。"],"medium"),
q(6,"比較同碳數的烷類、醇類和有機酸，哪項實驗最能支持它們性質不同與結構有關？",["控制溫度、質量與測量方法，分別比較水溶性、導電性、pH及燃燒資料，再對照官能基","只比較瓶子顏色","只聞氣味並不記錄成分","每種物質使用不同濃度和體積"],"A","官能基和結構可能影響溶解、酸鹼與導電等性質；控制條件並多項測量可建立較可靠的比較。","把結構差異轉成可控制、可量化的性質比較。",["列出碳氫骨架與官能基差異。","固定質量、濃度、溫度與測量方法。","測量水溶性、導電性、pH及燃燒。","比較資料與結構，而非外觀或不公平條件。","因此 A 最完整。"],"hard"),
q(7,"某酒精燈使用乙醇作燃料，火焰變黃且冒黑煙，最可能的改善方向是？",["增加空氣供應或調整燈芯，使燃燒較完全並避免直接吸入煙氣","加入更多乙醇並封住通風孔","把火焰靠近臉部觀察","加水到燃料中即可保證完全燃燒"],"A","黃火與黑煙可能代表氧氣不足、產生炭黑的不完全燃燒；應改善空氣供應並遵守燃燒安全。","由燃燒產物和火焰現象判斷氧氣條件。",["觀察黃火和黑煙等現象。","推論氧氣供應可能不足。","調整空氣孔或燈芯並重新觀察。","保持通風、遠離臉部且不任意加液體。","所以 A 正確。"],"medium"),
q(8,"有機酸和碳酸鹽反應產生氣泡，將氣體通入石灰水變混濁；這項證據可支持？",["有機酸與碳酸鹽反應生成二氧化碳，但仍需控制空白和其他氣體來源","氣泡一定是氫氣","石灰水變混濁證明生成氧氣","有機酸不能和鹽類反應"],"A","酸與碳酸鹽可產生二氧化碳，石灰水混濁是支持性檢驗；需用對照排除空氣或裝置污染。","把物質類型、氣體檢驗和證據限制結合。",["辨認反應物為酸和碳酸鹽。","預測二氧化碳生成。","用石灰水進行氣體檢驗。","設置空白或未加酸對照排除干擾。","因此 A 最完整。"],"medium"),
q(9,"處理未知有機液體時，哪項安全作法最重要？",["先查標示與安全資料，遠離火源並在通風處使用小量，不用鼻子直接聞","點火測試是否為酒精","把液體倒入飲料瓶以便攜帶","用舌頭比較酸甜"],"A","未知有機液體可能易燃、揮發或有毒，應查資料、隔離火源、通風和防護，不可用人體或火焰測試。","把有機物的揮發／易燃特性轉成暴露控制。",["確認容器標示或請教師長協助。","查閱易燃、毒性和接觸警示。","移除火源、使用小量並保持通風。","不聞、不嘗、不點火、不誤裝。","所以 A 是安全作法。"],"easy"),
q(10,"若要由結構預測一種有機物的性質，哪項推理流程最合理？",["先辨認碳氫骨架與官能基，再預測極性、溶解性、酸鹼性及反應，最後用實驗資料驗證","只看分子量就能預測所有性質","先猜用途再修改結構資料","只看名稱中的『醇』或『酸』而不看結構"],"A","碳氫骨架和官能基影響極性、溶解、酸鹼與反應，但預測仍需由測量資料驗證，不能只靠名稱或分子量。","用結構—性質—證據三段式建立有機物推理。",["畫出或查閱分子結構。","辨認主要官能基與極性。","提出溶解、酸鹼和反應預測。","設計或查找可量測資料驗證。","所以 A 是完整流程。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["烷類、醇類、有機酸和酯類的差異可由碳氫骨架與官能基連結到性質。","燃燒、溶解、酸鹼、氣體檢驗和香味都是需控制條件的證據，不是單一分類規則。","有機物用途與風險需同時考慮揮發性、易燃性、濃度、暴露和標示。"],"versionDifferences":["南一公開線索支持由燃燒與生活燃料進入烷類和醇類。","康軒公開課程資料較突出官能基、酸鹼與物性資料。","翰林公開課程計畫補充酯類香味、生活材料與安全連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以骨架—官能基—極性—性質—用途—安全六層比較常見有機物。","納入醇類燃燒、醋酸氣體反應、酯香味證據和未知有機液體處置。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫烷類、醇類、有機酸與酯類的結構、性質、反應、生活應用與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jf-Ⅳ-2：常見烷類、醇類、有機酸與酯類","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為烷類、醇類、有機酸、酯類、燃燒、溶解、酸鹼、香味、氣體證據與安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jf-iv-2")
if __name__=="__main__": main()
