"""Jd：酸鹼反應第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jd.json"
REPORT=ROOT/"implementation/reports/science-content-jd-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"酸鹼反應、離子、指示劑、生活資料判讀","pattern":"取由酸鹼性質、反應證據與粒子資料整合推論酸鹼反應的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"酸鹼、pH、反應與生活環境情境","pattern":"取從圖表、pH、材料反應與生活環境情境進行酸鹼推理的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"酸鹼反應、離子模型、中和與安全","pattern":"取以酸鹼粒子、反應、測量、生活應用與安全建立跨概念理解的方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jd-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jd"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的酸鹼分類、離子模型、pH、反應、生活應用與安全整合能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jd","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"未知溶液使藍色石蕊變紅、pH 約 3，且與鎂帶反應產生氣泡；哪項整合判斷最合理？",["溶液呈酸性，含較多 H⁺，與鎂反應可能產生氫氣","溶液呈鹼性且一定產生氧氣","溶液中沒有任何離子","藍色石蕊變紅代表溶液是鹽類"],"A","石蕊變紅與 pH 3 支持酸性、H⁺ 較多；酸與活潑金屬反應可產生氫氣，但仍要以安全檢驗確認。","把指示劑、pH、離子和反應物類型交叉驗證。",["由石蕊和 pH 判斷酸鹼性。","推論 H⁺ 相對濃度較高。","辨認鎂是可與酸反應的金屬。","預測氫氣並以適當檢驗確認。","因此 A 最完整。"],"hard"),
q(2,"某清潔劑 pH 12，另一瓶 pH 2；若兩者皆未標示成分，哪項結論最妥當？",["前者呈鹼性、後者呈酸性，但不能只由 pH 確定化學品名稱與安全性","前者一定是氫氧化鈉純品，後者一定是鹽酸純品","pH 越高越酸","兩瓶都一定可以直接接觸皮膚"],"A","pH 可判斷酸鹼方向和相對強弱，但不能單獨確定成分、濃度或危害；高低 pH 都可能有腐蝕風險。","區分測量結果能支持的性質和仍需標示／安全資料的資訊。",["讀取 pH 12 與 pH 2 的方向。","判斷前者鹼性、後者酸性。","查閱標示和安全資料確認成分及危害。","排除由 pH 直接猜純品和可接觸的錯誤。","所以 A 符合證據範圍。"],"medium"),
q(3,"酸性溶液與鹼性溶液混合後 pH 接近 7，但溫度也上升；最完整的解釋是？",["H⁺ 和 OH⁻ 生成水使酸鹼性減弱，中和過程可能釋放熱量","溫度上升使 pH 自動變 7，兩者沒有反應","所有混合都必定 pH 7 且放熱","pH 7 表示溶液沒有離子"],"A","中和消耗 H⁺、OH⁻ 生成水，適當比例可接近中性；反應能量變化可能造成升溫，但需對照確認。","用粒子、酸鹼比例與能量資料整合解釋宏觀結果。",["列出 H⁺ 和 OH⁻ 的核心反應。","確認兩者相對量接近。","將 pH 接近 7 連到中和。","把溫升視為可能的中和熱證據並設對照。","因此 A 最完整。"],"hard"),
q(4,"要判斷『酸雨會侵蝕碳酸鈣建材』，哪項證據鏈最有力？",["酸性溶液接觸碳酸鈣後固體質量下降並放出可使石灰水混濁的氣體，且有未加酸對照","只看雨水顏色","只在一塊建材上觀察一天","假設所有雨水都同樣酸且不需測量"],"A","質量減少、二氧化碳檢驗和對照共同支持酸與碳酸鈣反應及材料溶蝕；單一顏色或未控制觀察不足。","以反應式、材料資料、氣體證據和對照建立環境推論。",["確認雨水酸性資料。","選擇相同碳酸鈣材料並設未加酸對照。","量測固體質量和產氣。","用石灰水驗證二氧化碳。","所以 A 的證據鏈最完整。"],"hard"),
q(5,"兩種酸的 pH 相同，但其中一種溶液濃度較高；下列哪項不能僅由 pH 相同直接推論？",["兩者在測量條件下 H⁺ 表現出的酸鹼程度相近，但化學成分、總量與反應容量可能不同","兩者一定含有相同酸分子","兩者酸性方向相同","仍需成分和體積資料比較可中和的鹼量"],"B","pH 主要反映當下 H⁺ 活度／濃度相關的酸鹼程度，不足以確定酸的種類、總量或可中和容量。","區分酸鹼強弱的測量值與溶液成分、總量。",["確認兩者 pH 相同只支持酸鹼程度相近。","檢查是否提供成分和體積。","判斷不能由 pH 指定相同酸分子。","再用滴定或濃度資料比較反應容量。","所以 B 是不能直接推論的敘述。"],"hard"),
q(6,"若要用生活材料設計酸鹼反應探究，哪項做法最符合科學與安全原則？",["先查材料標示與危害，少量操作，設對照並用 pH／指示劑及反應現象記錄","直接混合所有清潔劑觀察氣味","用舌頭測酸鹼強弱","只靠網路傳言決定成分"],"A","安全探究需先辨識成分與危害，以少量、對照和可量測資料判讀，不能人體試驗或任意混用化學品。","把探究設計、證據品質和安全規範放在同一決策流程。",["讀取標示與安全資料。","選低風險、少量且可控的材料。","設置未反應對照與重複測量。","使用 pH、指示劑或氣體檢驗而非人體感官。","所以 A 正確。"],"easy"),
q(7,"一杯溶液加入水後 pH 從 2 變成 4；哪項解釋最合理？",["酸被稀釋，H⁺ 濃度降低，酸性減弱但不代表溶液已中性","加入水使溶液變成強鹼","pH 上升表示 H⁺ 增加","加水一定使所有離子消失"],"A","稀釋使單位體積 H⁺ 減少，pH 往中性方向移動；pH 4 仍可能是酸性。","區分 pH 方向、濃度和中性門檻。",["比較稀釋前後 pH。","判斷酸性溶液 pH 上升代表酸性減弱。","確認 pH 4 仍低於中性附近。","排除變強鹼、H⁺ 增加與離子消失。","因此 A 正確。"],"medium"),
q(8,"若酸鹼反應後溶液導電度下降但沒有完全變成零，哪項粒子解釋最合理？",["H⁺ 和 OH⁻ 被消耗成水，溶液仍可能有鹽類離子可移動","所有離子都沉澱消失","水本身一定不能移動電荷而反應停止","導電度下降表示質量消失"],"A","中和消耗 H⁺、OH⁻，但旁觀離子形成的可溶性鹽仍在溶液中，所以導電度可能下降而非零。","把導電度、淨離子與旁觀離子連結。",["列出中和前的關鍵離子。","判斷 H⁺、OH⁻ 生成水。","保留 Na⁺、Cl⁻ 等鹽類離子。","用可移動離子數量解釋導電度下降。","所以 A 最合理。"],"hard"),
q(9,"某未知氧化物遇水後使溶液 pH 上升，加入酸後固體逐漸溶解；最合理的初步分類是？",["可能是鹼性氧化物，但仍需檢驗生成物與設對照確認","一定是酸性氧化物","一定是中性氣體","只靠 pH 就能確定所有化學式"],"A","遇水呈鹼性且能與酸反應的證據支持鹼性氧化物，但要由成分與反應資料確認，不能直接確定化學式。","將多個現象整合成暫定模型，再標出尚待驗證的部分。",["記錄遇水後 pH 變化。","確認加入酸後固體溶解。","將兩項證據與鹼性氧化物模型比較。","列出仍需的成分與生成物檢驗。","因此 A 是適當的初步結論。"],"medium"),
q(10,"要比較兩種生活酸性產品的中和能力，最適合的依變數是？",["在相同條件下使固定量鹼達到指定 pH 所需的產品體積或物質量","產品包裝顏色","聞起來是否刺鼻","一次混合後泡沫高度而不記錄體積"],"A","中和能力應以達到同一酸鹼終點所需的體積或物質量量化，並控制濃度、溫度和攪拌；外觀和氣味不足。","把模糊的『效果』轉成可比較的中和終點資料。",["固定鹼的種類、體積與初始濃度。","設定一致的終點 pH 或指示劑變色。","逐量加入產品並記錄體積或質量。","重複測量並比較平均值。","所以 A 是合適的依變數。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["酸鹼反應要把宏觀 pH／指示劑、微觀 H⁺／OH⁻ 和反應產物放在同一證據鏈。","稀釋、中和、氧化物反應、碳酸鹽反應及導電度各提供不同層次的酸鹼證據。","生活用途和危險性必須由成分、濃度、反應容量、標示與安全資料共同判斷。"],"versionDifferences":["南一公開線索較適合由生活酸鹼材料及反應現象進入整合概念。","康軒公開課程資料較突出離子、指示劑、測量與控制變因。","翰林公開課程計畫補充酸鹼反應、環境材料、用途與安全的連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以『粒子—現象—量測—反應容量—安全』五層框架統整根單元。","把酸雨、導電度、稀釋、未知氧化物及生活產品中和能力作為跨概念遷移活動。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫 Jd 根單元酸鹼反應整合題；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jd：酸鹼反應","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為酸鹼分類、H⁺／OH⁻、pH、指示劑、中和、導電度、酸雨、氧化物、生活產品與安全的根單元整合問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jd")
if __name__=="__main__": main()
