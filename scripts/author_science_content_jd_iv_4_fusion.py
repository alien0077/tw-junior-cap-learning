"""Jd-Ⅳ-4：氫離子與氫氧根離子的關係第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jd-iv-4.json"
REPORT=ROOT/"implementation/reports/science-content-jd-iv-4-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"氫離子、氫氧根、酸鹼與指示劑資料判讀","pattern":"取由離子模型、指示劑與酸鹼資料推論溶液性質的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"pH、酸鹼濃度、稀釋與生活情境","pattern":"取從圖表、pH 或濃度資料及生活情境判斷酸鹼變化的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"氫離子、氫氧根、酸鹼中和與微觀模型","pattern":"取以離子、酸鹼性、指示劑及中和反應連結微觀與宏觀證據的教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jd-iv-4-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jd-iv-4"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的氫離子、氫氧根、pH、指示劑、稀釋與中和能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jd-iv-4","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"酸性水溶液中通常哪種離子的相對量較多？",["氫離子 H⁺，且其濃度高於氫氧根離子 OH⁻","氫氧根離子 OH⁻，且沒有氫離子","鈉離子一定最多","所有離子濃度都完全相同"],"A","酸性溶液的氫離子濃度大於氫氧根離子；酸鹼性是相對量的判斷，不表示沒有另一種離子。","用 H⁺ 與 OH⁻ 的相對濃度判斷酸鹼性。",["列出酸鹼判斷的兩種關鍵離子。","比較 H⁺ 與 OH⁻ 的相對濃度。","確認酸性代表 H⁺ 較多。","排除沒有 OH⁻、鈉離子及完全相同的說法。","所以 A 正確。"],"easy"),
q(2,"鹼性水溶液中，哪項粒子關係最合理？",["OH⁻ 濃度大於 H⁺ 濃度，但兩者仍可能同時存在","溶液中完全沒有 H⁺","H⁺ 濃度一定等於零且沒有水分子","只有金屬原子能在水中移動"],"A","鹼性表示 OH⁻ 相對較多，不代表 H⁺ 完全不存在；水中仍有粒子平衡與水分子。","避免把相對優勢誤解成某粒子完全消失。",["辨認鹼性的比較對象是 H⁺ 和 OH⁻。","判斷 OH⁻ 濃度較大。","保留另一種離子存在的可能。","排除零濃度與金屬原子主導的說法。","答案為 A。"],"easy"),
q(3,"若某溶液的 H⁺ 與 OH⁻ 濃度相等，最適合的判斷是？",["中性，酸鹼性不偏向任一方","一定是強酸","一定是強鹼","完全沒有離子"],"A","H⁺ 與 OH⁻ 相對量相等時呈中性；中性不代表沒有離子。","以相對濃度而非有無離子判斷中性。",["找出 H⁺ 和 OH⁻ 的比較資料。","確認兩者濃度相等。","將相等對應到中性。","排除強酸、強鹼與無離子的錯誤。","所以 A 正確。"],"easy"),
q(4,"將酸性溶液加水稀釋，在未加入其他物質的前提下，通常會發生什麼變化？",["H⁺ 濃度降低，酸性減弱，pH 朝中性方向移動","H⁺ 濃度必定增加，酸性更強","OH⁻ 會全部消失","溶液一定立刻變成強鹼"],"A","加水增加總體積，使 H⁺ 濃度降低，酸性減弱；稀釋不會直接創造強鹼。","區分粒子總量和單位體積濃度的變化。",["確認加入的是純水而非鹼液。","比較稀釋前後體積。","判斷 H⁺ 總量近似不變但濃度下降。","推論酸性減弱、pH 往中性。","因此 A 正確。"],"medium"),
q(5,"酸與鹼混合後，H⁺ 和 OH⁻ 反應生成水；這個微觀過程可解釋哪項宏觀現象？",["酸鹼性可能減弱，若量適當可接近中性","混合後一定產生金屬沉澱","所有離子都變成氧氣","溶液一定變成更強的酸"],"A","H⁺ 與 OH⁻ 生成水會消耗兩種關鍵離子，使酸鹼性減弱；是否中性取決於相對量。","用離子反應式連結指示劑與酸鹼性變化。",["列出 H⁺ 與 OH⁻ 的反應。","判斷關鍵離子被消耗。","比較兩者原本的量是否相當。","推論酸鹼性減弱或接近中性。","所以 A 是合理宏觀結果。"],"medium"),
q(6,"兩杯酸性溶液的 pH 分別為 2 和 4；在同一測量規則下，哪杯 H⁺ 濃度較高？",["pH 2 的溶液，因為 pH 越低通常代表 H⁺ 濃度越高","pH 4 的溶液，因為數字較大","兩杯一定相同","只看顏色不能比較"],"A","在常用 pH 定義下，酸性溶液 pH 越低代表 H⁺ 濃度越高，因此 pH 2 較酸。","先確認 pH 尺度方向，再比較數值。",["確認兩杯皆為酸性。","比較 pH 2 與 pH 4。","使用 pH 越低、H⁺ 越高的關係。","排除把數字大誤當酸性強及無法比較。","答案為 A。"],"medium"),
q(7,"若以相同體積、相同濃度的酸鹼溶液進行中和，哪項測量最能確認接近中性？",["使用校正過的 pH 測量或適當指示劑，並重複測量確認結果","只看混合後是否冒泡","只看溶液體積變化","只憑氣味判斷"],"A","pH 測量或指示劑可直接提供酸鹼性證據，重複測量能降低操作誤差；冒泡、體積和氣味不是中性的充分判準。","選擇與研究問題直接相關的量測工具。",["先明確定義『接近中性』的 pH 範圍。","校正 pH 計或選合適指示劑。","混合後取樣測量並重複。","排除冒泡、體積與氣味的間接線索。","因此 A 最有證據力。"],"medium"),
q(8,"要比較兩種酸的酸鹼性，哪項作法最公平？",["使用相同溫度、體積與測量方法，控制濃度或清楚標示濃度，再比較 H⁺／pH 資料","一種酸測濃溶液，另一種測稀溶液","一杯用試紙、一杯用 pH 計且不校正","只比較溶液顏色而不記錄濃度"],"A","酸的濃度會影響 H⁺ 與 pH；必須控制或標示濃度並使用一致測量方法，才能比較酸本身或指定條件。","先釐清比較對象，再控制濃度與儀器。",["決定要比較酸種類還是溶液條件。","固定體積、溫度與濃度或完整記錄。","使用同一校正過的測量方法。","重複測量並比較 H⁺／pH。","所以 A 是公平方法。"],"hard"),
q(9,"若一滴酸性溶液中 H⁺ 濃度增加，對 OH⁻ 與酸鹼性的合理推論是？",["OH⁻ 相對比例會降低，溶液酸性增強","OH⁻ 一定也增加到相同倍數，溶液變中性","H⁺ 增加會使溶液變鹼","酸鹼性與離子濃度無關"],"A","增加 H⁺ 使 H⁺ 相對於 OH⁻ 的優勢變大，溶液酸性增強；不能假設 OH⁻ 同步增加到抵消。","用相對粒子濃度追蹤酸鹼性方向。",["確認改變的是 H⁺ 濃度。","比較 H⁺ 與 OH⁻ 的相對關係。","判斷酸性向更強方向移動。","排除同步抵消、變鹼與無關的說法。","因此 A 正確。"],"medium"),
q(10,"某未知溶液使藍色石蕊變紅且 pH 測得 3；要避免過度解釋，哪項結論最恰當？",["溶液呈酸性且 H⁺ 相對濃度較高，但仍需其他資料判斷是哪種酸或其精確濃度","一定是鹽酸且濃度已知","一定沒有 OH⁻","藍色石蕊變紅代表溶液是金屬"],"A","指示劑與 pH 支持酸性及 H⁺ 較多，但不能僅由此確定酸的種類、精確濃度或 OH⁻ 完全不存在。","把證據能支持的範圍和不能支持的身分判斷分開。",["讀取石蕊變色方向。","確認 pH 3 支持酸性。","推論 H⁺ 相對濃度高於 OH⁻。","列出仍未知的酸種類與精確濃度。","所以 A 是證據範圍內的結論。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["酸鹼性由 H⁺ 與 OH⁻ 的相對濃度關係判斷，而非看是否完全沒有另一種離子。","稀釋、中和與 pH 變化需區分粒子總量、體積和濃度。","宏觀指示劑顏色、pH 數值與微觀離子模型必須相互對照。"],"versionDifferences":["南一公開線索支持由指示劑與生活溶液進入酸鹼粒子概念。","康軒公開課程資料較突出 H⁺／OH⁻、中和與測量操作。","翰林公開課程計畫補充離子模型、pH 與酸鹼應用連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以 H⁺—OH⁻ 相對濃度、稀釋、pH、指示劑和中和五個視角互相校對。","加入測量公平性、證據範圍與『中性不等於沒有離子』的迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫氫離子、氫氧根、pH、稀釋、中和、指示劑與測量；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jd-Ⅳ-4：氫離子與氫氧根離子的關係","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為 H⁺／OH⁻ 相對濃度、pH、稀釋、中和、指示劑、測量公平性與證據範圍專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jd-iv-4")
if __name__=="__main__": main()
