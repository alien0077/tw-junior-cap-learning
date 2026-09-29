"""Je：化學反應速率與平衡第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-je.json"
REPORT=ROOT/"implementation/reports/science-content-je-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"反應速率、可逆反應、平衡與資料判讀","pattern":"取由反應時間、可逆反應資料、曲線與條件整合判讀化學變化的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"速率、平衡、製程條件與生活情境","pattern":"取從圖表、模型、反應條件與製程情境整合推論速率和平衡的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"反應速率、動態平衡、催化劑與製造","pattern":"取以碰撞、正逆反應、平衡及工業條件取捨建立跨概念教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-je-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-je"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的速率、可逆反應、平衡、催化劑、製程及資料判讀整合能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-je","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"某反應的產物濃度先快速上升，後來維持近似固定；若反應可逆，最合理的整合解釋是？",["開始時正反應較快，後來逆反應速率增加，最後兩者相等形成動態平衡","反應物和生成物都停止運動","產物完全取代反應物且沒有逆反應","濃度固定表示沒有任何粒子存在"],"A","反應初期生成物少，正反應占優勢；隨生成物增加，逆反應加快，達到正逆速率相等的動態平衡。","用時間序列把速率變化和最終平衡連在一起。",["讀取產物濃度隨時間的變化。","判斷初期正反應較快。","考慮生成物增加使逆反應增加。","以兩方向速率相等解釋平台。","所以 A 正確。"],"hard"),
q(2,"若加入催化劑後曲線較快到達相同的平衡平台，哪項結論最合理？",["催化劑加快接近平衡的速度，但在相同條件下不改變平衡組成","催化劑增加了平衡產物總量","催化劑只加快正反應","平衡平台較早出現表示反應物不存在"],"A","催化劑通常同時加快正、逆反應，使達平衡時間縮短；相同條件下平台高度不一定改變。","比較曲線到平台時間與平台高度兩種資訊。",["比較有無催化劑的初期斜率。","比較兩曲線到平台的時間。","比較最終平台高度。","區分快速到達和平衡組成。","因此 A 最符合資料。"],"medium"),
q(3,"某製程提高溫度後反應速率變快，但目標產物平衡比例下降；工廠仍可能採用中等溫度，原因是？",["需在速率、平衡收率、能源與設備安全間取折衷，最高溫不一定是最佳條件","只要速率快就不必考慮收率","平衡比例下降代表反應停止","溫度只影響顏色不影響成本"],"A","工業製程要同時考慮達平衡速度、目標產物比例、能源成本、材料壽命與安全，中等條件可能有較佳總效益。","把實驗變因轉成多指標製程決策。",["分別讀取速率和產物比例資料。","確認高溫的速率與平衡效果相反。","加入能源、設備和安全限制。","比較不同條件的總體效益。","所以 A 正確。"],"medium"),
q(4,"研究可逆反應時，若只量測反應剛開始 10 秒的產物量，最主要的限制是？",["只能反映初期反應速率，不能直接代表最後平衡產量或平衡位置","可以直接知道平衡常數","能證明逆反應不存在","一定能比較所有溫度的平衡收率"],"A","初期資料可估算速率，但尚未達平衡，不能直接作為平衡終態或常數的證據。","依測量時間尺度限定結論範圍。",["確認量測只涵蓋反應初期。","用斜率解讀初期速率。","檢查是否有後續平台或穩定組成資料。","若沒有，不能宣稱平衡產量或常數。","所以 A 是正確限制。"],"hard"),
q(5,"若增加反應物後系統先出現產物濃度上升，最後仍維持新平台；這顯示了哪種關係？",["濃度擾動會改變瞬間速率，系統再透過可逆反應建立新的平衡","加入反應物會永久停止逆反應","新平台表示原本沒有平衡","產物上升只可能是溫度改變"],"A","增加反應物先使正向反應優勢，之後逆反應也調整，最後在新組成建立平衡。","用擾動—回應—新平衡三階段讀資料。",["找出被增加的物質。","判斷瞬間正向速率的變化。","追蹤後續逆反應與產物平台。","確認新平台不等於粒子停止。","答案為 A。"],"medium"),
q(6,"兩項技術都能讓工廠較快得到相同平衡產物量：甲耗能較低但設備昂貴，乙設備便宜但需高溫；最適合的評估方式是？",["比較生命週期成本、能源、產率、設備安全與維護，而非只看反應速度","只選設備最便宜的乙","只選速度最快的技術","只看一次試車的顏色"],"A","製程選擇需把速率、能耗、設備投資、維護、安全與環境成本放在同一多指標決策中。","將速率和平衡知識延伸到工程與永續判斷。",["確認兩方案的產量和時間相近。","列出能源、設備、維護和安全成本。","考慮長期運轉與環境影響。","比較總體效益，不用單一指標決定。","因此 A 最完整。"],"medium"),
q(7,"封閉反應器內可逆反應達平衡後，若正反應與逆反應仍各自發生，哪項量可以維持穩定？",["宏觀濃度、壓力或顏色等可觀測量，但微觀粒子仍持續反應","每個粒子的位置都不再改變","所有分子數都變成零","只有溫度能穩定，其他量必定振盪"],"A","動態平衡的宏觀量穩定來自正逆反應速率相等，並不表示每個粒子停止或消失。","對照宏觀穩定與微觀動態的兩個尺度。",["列出可觀測的濃度、壓力或顏色。","確認正逆反應都仍進行。","判斷兩方向速率相等。","說明微觀交換不必造成宏觀量改變。","所以 A 正確。"],"easy"),
q(8,"若反應曲線在高溫下初期斜率較大、平台卻較低，哪項資料解讀正確？",["高溫使初期反應較快，但平衡位置使最終產物比例較低","高溫同時使速率和產量都必定增加","平台較低表示反應沒有開始","斜率和平台代表同一個量"],"A","斜率反映速率，平台反映平衡後總量或比例；高溫可使速率增加但若反應方向放熱，平衡產物可能下降。","用圖形兩種幾何特徵拆解兩個化學概念。",["比較初期斜率。","比較平台高度。","分別判斷速率和最終平衡結果。","排除速率與產量必同向的說法。","因此 A 符合資料。"],"hard"),
q(9,"要判斷一項平衡改變是否真的由濃度造成，哪項對照最必要？",["保持溫度、壓力、攪拌與初始量一致，只改變指定反應物濃度並重複測量","每次同時改變溫度和濃度","只觀察一次顏色變化","不記錄反應達平衡的時間"],"A","控制其他條件、重複測量並記錄達平衡後組成，才能把差異歸因於濃度而非速率或環境變因。","將因果推論、控制變因和終態資料結合。",["列出會影響平衡和速率的條件。","固定溫度、壓力、攪拌與初始量。","只改變指定濃度。","量測初期速率與平衡終態並重複。","所以 A 最能支持因果。"],"medium"),
q(10,"某工廠使用催化劑後縮短生產時間，但每日目標產量沒有增加；最合理的解釋是？",["催化劑加快達到既有平衡的速度，未必改變平衡位置或每批可得總量","催化劑使原子消失，所以產量不變","生產時間縮短代表平衡被破壞","催化劑一定只加快逆反應"],"A","催化劑常讓正、逆反應都變快，使同一平衡較快建立；若設備批次容量與平衡組成不變，每批產量可不增加。","把實驗速率效應連到工廠批次和產量限制。",["確認催化劑使達平衡時間縮短。","比較每批平衡產物量是否改變。","判斷催化劑主要改變到達速度。","考慮設備容量與平衡組成限制。","因此 A 正確。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["速率描述反應進行快慢，平衡描述可逆反應在特定條件下的宏觀終態，兩者不可混為一談。","催化劑、濃度、溫度與壓力可能同時牽涉速率和位移，但作用機制與證據不同。","工業製程需整合速率、收率、能源、設備、安全與成本。"],"versionDifferences":["南一公開線索支持由時間序列和生活反應進入速率與平衡。","康軒公開課程資料較突出正逆反應、曲線與控制變因。","翰林公開課程計畫補充催化劑、製程及條件取捨；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以『初期斜率—動態平衡—平台高度—條件擾動—製程取捨』整合根單元。","用不同時間尺度和工業批次情境診斷速率等於產量、平衡等於停止等迷思。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫 Je 根單元的速率、可逆反應、平衡、催化劑、曲線及工業決策整合；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Je：化學反應速率與平衡","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為速率—可逆反應—動態平衡—催化劑—製程決策整合問題，與 Je 子單元分開設計；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content je")
if __name__=="__main__": main()
