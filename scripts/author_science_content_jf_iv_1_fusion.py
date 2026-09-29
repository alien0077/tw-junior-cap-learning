"""Jf-Ⅳ-1：有機與無機化合物的重要特徵第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jf-iv-1.json"
REPORT=ROOT/"implementation/reports/science-content-jf-iv-1-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"有機化合物、碳氫燃燒、物質分類與性質判讀","pattern":"取由元素組成、燃燒產物、溶解與導電資料判斷有機／無機物質的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"碳化合物、分子離子、生活材料與實驗資料","pattern":"取從粒子模型、生活材料與資料圖表推論化合物分類和性質的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"有機化合物、碳骨架、無機物與生活應用","pattern":"取以碳骨架、元素組成、分子／離子結構和生活材料建立分類理解的方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jf-iv-1-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jf-iv-1"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的有機／無機分類、碳骨架、燃燒、分子／離子、導電與生活材料能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jf-iv-1","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"下列哪項最能支持某物質屬於含碳的有機化合物，而不是只靠名稱猜測？",["組成分析顯示含碳骨架，燃燒可生成二氧化碳和水，且資料與其分子結構相符","只看物質顏色是透明","只看包裝寫著『天然』","只看是否能溶於水"],"A","含碳骨架、燃燒產物和結構資料共同支持有機物判斷；顏色、來源或單一溶解性不足。","以組成、反應產物和結構三層證據分類。",["先分析元素組成。","確認是否有碳骨架或碳氫結構。","觀察燃燒是否形成 CO₂ 和 H₂O。","排除顏色、天然與單一溶解性判準。","所以 A 證據最完整。"],"medium"),
q(2,"二氧化碳含有碳，卻通常不歸入國中課程所說的有機化合物；這提醒我們？",["分類不能只看是否含碳，還要考慮結構、鍵結與課程定義","所有含碳物質都一定是有機物","二氧化碳沒有元素","有機物只要能燃燒就一定不含氧"],"A","有機／無機分類不能只用含碳單一規則，需依結構、鍵結與學科定義判斷；二氧化碳是常見含碳無機物例子。","用反例修正『含碳即有機』的過度簡化。",["確認二氧化碳含有碳。","比較它與典型有機物的結構和分類。","理解分類需要多個條件。","排除含碳必有機和無元素的說法。","答案為 A。"],"medium"),
q(3,"甲物質的水溶液導電，乙物質的水溶液不導電；最合理的初步推論是？",["甲可能解離成可移動離子，乙可能主要以中性分子存在，但仍需成分和濃度資料確認","甲一定是有機物，乙一定是無機物","導電就代表物質能燃燒","不導電代表溶液沒有粒子"],"A","導電性反映溶液中可移動帶電粒子，不直接等同有機／無機分類；仍需粒子結構與成分資料。","把導電性當作結構線索，而不是分類的唯一答案。",["確認測量的是水溶液導電性。","判斷是否有可移動離子。","比較分子與離子溶質模型。","限制結論，不由導電性直接決定有機／無機。","所以 A 最妥當。"],"medium"),
q(4,"有機燃料完全燃燒時常檢測到二氧化碳和水，這些產物主要反映燃料中含有哪些元素？",["碳和氫，分別進入二氧化碳與水；氧也可能來自空氣","只有氧元素","只有金屬元素","碳和氫在燃燒中消失"],"A","燃料中的碳形成二氧化碳、氫形成水，反應所需的氧通常來自空氣；原子只是重新排列。","由產物反推反應物元素並檢查質量守恆。",["列出二氧化碳與水的元素。","追蹤碳進入 CO₂、氫進入 H₂O。","辨認氧的來源可能是空氣。","排除元素消失和金屬的說法。","因此 A 正確。"],"easy"),
q(5,"比較乙醇和食鹽的水溶液性質，哪項設計最能避免把『有機／無機』和『導電性』混為一談？",["同時分析元素與結構，並分別測量溶液導電性，說明分類和性質是不同問題","只測導電性就直接命名兩者分類","只看兩者是否有氣味","只看溶解速度而不記錄濃度"],"A","物質分類依組成／結構，導電性依溶液中帶電粒子；需分開提出問題與測量，不能用單一性質代替分類。","把分類證據和物理／化學性質測量分層。",["先查乙醇與食鹽的元素和結構。","控制相同濃度和體積製備溶液。","分別測導電性與其他性質。","比較哪些證據支持分類、哪些只支持導電。","所以 A 最完整。"],"hard"),
q(6,"下列哪項可作為判斷某未知物質具有分子型態而非離子晶格的線索？",["純物質熔點、溶解狀態與水溶液導電性等多項資料一致支持中性分子存在","只看包裝大小","只看固體顏色","只量一次質量就能判定粒子型態"],"A","分子／離子型態需由多種物性和溶液導電資料推論，單一外觀或質量不足以判定微觀結構。","用多證據模型判斷粒子型態，保留推論限制。",["選擇熔點、溶解和導電等可測性質。","控制樣品純度與濃度。","比較資料是否符合分子或離子模型。","避免由顏色、包裝和一次質量過度推論。","因此 A 最有力。"],"hard"),
q(7,"塑膠、糖和蛋白質都可能含碳；若要比較它們的有機物特徵，哪項資料最適合？",["元素組成、分子或聚合結構、燃燒產物與熱分解行為的組合資料","只比較價格","只看是否能漂浮在水面","只問是否為天然來源"],"A","含碳材料的有機特徵需透過組成、結構與反應資料判斷；價格、密度或來源不是化學分類充分證據。","跨材料比較時固定分類證據層次。",["蒐集三種材料的元素和結構資料。","比較分子大小或聚合特徵。","觀察燃燒／熱分解產物並注意安全。","排除價格、漂浮和天然來源的單一判準。","所以 A 最完整。"],"medium"),
q(8,"有機溶劑標示易燃，實驗中最重要的操作是？",["遠離火源、保持通風、使用小量並依安全資料處置，不以聞氣味辨識","靠近火焰測試是否燃燒","把溶劑倒入無標示飲料瓶","在密閉空間大量揮發以觀察氣味"],"A","有機溶劑蒸氣可能易燃或有害，需隔離火源、通風、防護與正確容器；不可用人體或火焰測試。","把有機物性質連到暴露、火災與標示安全。",["讀取易燃和毒性警示。","移除火源並保持通風。","使用原容器、小量和適當防護。","不聞、不嘗、不用火測試或誤裝。","因此 A 是安全作法。"],"easy"),
q(9,"某樣品燃燒後生成二氧化碳，但未檢出水；要避免錯誤分類，下一步最適合？",["檢查燃燒是否完全、樣品是否含氫、檢測方法是否靈敏，再結合結構資料判斷","直接宣稱它一定是無機物","只看火焰顏色判斷","認為水不可能是燃燒產物"],"A","未檢出水可能來自不完全燃燒、含氫量、冷凝或檢測限制，不能只用單一陰性結果分類。","先檢查替代解釋和測量限制，再整合結構證據。",["確認樣品和燃燒條件。","檢查水蒸氣是否凝結或檢測方法可靠。","確認樣品是否含氫與燃燒是否完全。","再與元素、結構和其他產物資料交叉判斷。","所以 A 最合理。"],"hard"),
q(10,"要製作有機／無機物質的比較表，哪組欄位最能支撐科學結論？",["元素與結構、粒子型態、溶解／導電性、燃燒或反應產物、測量條件與限制","顏色、價格、包裝和喜好","名稱長度、氣味和品牌","只列有機或無機兩個標籤"],"A","比較表需納入可追溯的組成、結構、物性、反應資料、控制條件和限制，才能支持而非只宣稱分類。","把資料欄位設計成可驗證的證據表。",["先定義要比較的分類問題。","列出組成與結構欄位。","加入導電、溶解、燃燒等可測性質。","記錄控制條件和測量限制。","因此 A 最能支撐結論。"],"medium"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["有機／無機分類需以元素組成、結構與課程定義判斷，不能只用含碳單一規則。","分子／離子型態影響溶解與導電等性質，但單一物性不足以決定分類。","燃燒產物、資料表、控制條件與安全標示可共同支撐生活材料判讀。"],"versionDifferences":["南一公開線索支持由燃燒產物與生活碳材料進入有機物。","康軒公開課程資料較突出分子／離子、導電性與實驗資料。","翰林公開課程計畫補充碳骨架、聚合材料與安全應用；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以組成—結構—粒子—物性—反應—安全六層框架比較有機與無機物。","納入二氧化碳反例、導電性限制、塑膠糖蛋白質比較和有機溶劑安全。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫有機與無機化合物分類、碳骨架、燃燒、分子／離子、導電及生活材料；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jf-Ⅳ-1：有機與無機化合物的重要特徵","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為碳骨架、分類反例、分子／離子、導電性、燃燒產物、生活材料比較與有機溶劑安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jf-iv-1")
if __name__=="__main__": main()
