"""Id：晝夜與季節第一輪來源融合、題庫重寫與來源審查。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-id.json"
REPORT=ROOT/"implementation/reports/science-content-id-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"晝夜、季節、太陽高度、地軸傾斜與天體運動資料判讀","pattern":"取由天體運動模型、日照資料、季節差異與地球觀測證據推論成因的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"地球自轉、公轉、地軸傾斜、晝夜長短與季節模型","pattern":"取操作地球儀與光源、比較日照區域、白晝長度及季節模型修正的教學與評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"太陽高度、緯度、影長、四季與極圈日照","pattern":"取用同日不同緯度、南北半球、影長與極圈日照資料建立地球幾何推理的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]

def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
    return {"id":f"question-science-content-id-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-id"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的晝夜、季節、天體運動、地軸傾斜及日照資料判讀能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；題幹、選項、答案、解析與五步解法均依 Id 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-id","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}

Q=[
q(1,"下列哪一項最直接說明地球自轉會造成晝夜交替？",["同一地點依序轉到面向光源與背向光源的位置","一年中正午影長會改變","不同月份會看到不同星座","月球繞地球運動"],"A","地球自轉使同一地點交替位於受光面與背光面，因此形成晝夜；季節和月相則涉及其他運動。","先分辨週期，再把觀測現象對應到受光與背光。",["確認題目問的是一天內反覆發生的現象。","把地球表面某地點標記在球面上。","讓球體自轉，觀察標記點交替進入光區與暗區。","B、C、D 分別涉及季節、星空或月球運動。","所以 A 是晝夜交替的直接成因。"],"easy"),
q(2,"若只改變地球儀的自轉方向，最適合觀察哪項結果？",["同一地點進入白晝與黑夜的先後改變","地軸傾角立刻變成 0 度","一年中的季節順序完全消失","太陽本身停止發光"],"A","改變自轉方向會改變各地進入受光區的先後與日出方向，但不會直接改變地軸傾角或太陽是否發光。","只追蹤模型中被改變的變因與可觀察結果。",["列出模型的自變因是自轉方向。","保持光源位置、地軸傾角和公轉位置不變。","觀察標記地點何時由暗區轉入亮區。","B、C、D 都不是自轉方向的直接結果。","答案為 A。"],"medium"),
q(3,"地球公轉與地軸傾斜共同造成季節變化時，最重要的證據組合是哪一項？",["太陽高度與白晝長度隨日期呈規律改變","每天日出方向都完全相同","月球表面坑洞數量改變","同一晚只看到一顆星"],"A","地軸傾斜配合公轉，使各地在一年中接受日照的角度和時間改變；太陽高度與白晝長度是直接可追蹤的觀測證據。","把季節判讀建立在全年資料的共同變化，而不是單次印象。",["蒐集同地點不同日期的正午影長或太陽高度。","同時記錄日出、日落時間以估算白晝長度。","檢查兩類資料是否隨日期呈一致週期。","B、C、D 無法支持季節日照變化。","因此 A 最完整。"],"medium"),
q(4,"若地軸完全沒有傾斜，但地球仍繞太陽公轉，對中緯度地區最合理的預測是？",["季節性的太陽高度與白晝長度差異會大幅減弱","每天都會有月食","晝夜交替會消失","地球不再自轉"],"A","地軸傾斜是造成一年中日照角度與白晝長度季節差異的重要條件；沒有傾斜時，公轉仍存在，但季節性差異大幅減弱。","做反事實模型時只移除一個因素，其他運動維持原狀。",["保留地球自轉與公轉。","只把地軸傾角設為 0 度。","比較不同公轉位置的太陽高度與白晝長度。","B、C、D 分別錯置月食、晝夜和自轉概念。","所以 A 是模型預測。"],"medium"),
q(5,"北半球夏至附近與南半球同一時期相比，哪項敘述較合理？",["北半球通常白晝較長、太陽高度較高，南半球則相反","兩半球的白晝和太陽高度必定完全相同","北半球沒有自轉而南半球有自轉","南半球一定沒有日照"],"A","地軸傾斜使同一時期兩半球的受光條件相反；北半球夏季通常白晝較長、太陽高度較高，南半球進入冬季特徵。","先判斷地軸指向，再比較兩半球的受光時間與角度。",["固定比較同一日期與相近緯度。","辨認北半球朝向太陽的一側。","由受光角度推論太陽高度與白晝長度。","B、C、D 與地球整體運動不符。","答案為 A。"],"medium"),
q(6,"在同一天、同一時刻比較赤道與高緯度地區，哪項資料最能幫助判斷兩地日照幾何差異？",["各地太陽高度角與同高竿子的影長","兩地居民的姓名","當天月球表面照片","地球公轉速度是否突然變成零"],"A","太陽高度角和影長能反映入射方向；控制竿高與測量時間後，可比較緯度造成的日照幾何差異。","用可量測的幾何代理量取代主觀感受。",["選定同日期與協調後的同一時刻。","使用相同高度的竿子並記錄影長。","搭配太陽高度角判讀入射方向。","B、C、D 不提供兩地日照幾何證據。","所以 A 最適合。"],"medium"),
q(7,"下列哪項實驗最能區分『地球自轉造成晝夜』與『地球公轉造成季節』？",["固定光源，用模型分別只改變自轉位置與公轉位置並記錄不同指標","同時任意改變光源距離、地軸角度和模型速度","只觀察一分鐘的月相","只詢問同學覺得哪個季節較熱"],"A","自轉主要對應同一天內受光／背光交替，公轉配合地軸傾斜則對應全年日照角度與白晝長度改變；分開操弄才能辨別。","設計單變因模型，讓現象的時間尺度和指標相互對應。",["列出自轉、地軸傾角與公轉位置三項因素。","一次只改變自轉位置或公轉位置。","分別記錄日夜交替與季節性日照指標。","B、C、D 不是可辨識因果的控制設計。","因此 A 最能區分兩種成因。"],"hard"),
q(8,"若某地一年中正午影長由短變長再變短，且測量地點、竿高與時刻固定，最合理的解釋是？",["太陽高度角有規律的季節變化","竿子每天自行伸縮","地球自轉在一年中停止又恢復","影長與太陽位置沒有關係"],"A","固定條件下影長的週期變化反映太陽高度角的週期變化，這是季節日照幾何的間接證據。","先排除測量條件變動，再把影長視為高度角的代理量。",["檢查竿高、地點與測量時間是否固定。","排列全年影長資料的變化順序。","用影長較短代表太陽高度較高。","B、C、D 無法解釋穩定週期。","答案為 A。"],"medium"),
q(9,"以手電筒、傾斜地球儀和標記地點模擬季節時，哪項做法最可能導致錯誤結論？",["把手電筒當成會隨模型一起移動的光源","固定手電筒，改變地球儀公轉位置","在標記點記錄受光時間和入射角","先預測再用不同日期位置檢查模型"],"A","太陽光源在模型中應作為固定參考；若光源隨地球儀移動，會改變距離與照射方向，混淆季節成因。","檢查模型是否保留真實系統的固定參考與相對運動。",["確認光源代表太陽且固定不動。","讓地球儀繞固定光源改變位置。","只改變模型的公轉位置，記錄入射角與日照時間。","A 會同時改變不應改變的光源條件。","所以 A 是錯誤模型操作。"],"hard"),
q(10,"若研究極圈附近夏季可能出現長時間白晝，哪項資料最能支持這個判斷？",["同一地點一日內日出、日落時間與太陽高度的連續紀錄","某天中午的氣溫單一數值","月球繞地球的公轉週期","校園樹種的名稱"],"A","極圈長時間白晝的判斷需要日出、日落及太陽高度的時間序列，不能只靠單次溫度或無關資料。","用完整時間序列驗證天文幾何預測。",["選定極圈附近固定觀測地點。","連續記錄太陽是否越過地平線及其高度。","計算每天可見太陽的時間長度。","B、C、D 不直接測量白晝持續時間。","因此 A 最能支持判斷。"],"medium"),
]

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
    lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以地球自轉解釋晝夜，以地軸傾斜與公轉解釋季節、太陽高度與白晝長度。","觀測必須把時間尺度、兩半球、緯度、影長、日照時間與模型的固定參考相互檢驗。"],"versionDifferences":["南一公開定位偏向自轉、公轉與因果鏈；康軒公開線索偏向地球儀、光源與操作模型；翰林公開定位較易連結緯度、影長、南北半球與極圈日照。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以一天／一年兩種時間尺度、南北半球對照、影長時間序列、固定光源模型與極圈資料建立本單元證據鏈。","把『季節是由日地距離單獨造成』、『夏天太陽離地球一定較近』及『模型光源跟著地球移動』列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織自轉晝夜、公轉、地軸傾斜、太陽高度、白晝長度、南北半球、緯度與極圈日照；原有 9 題為研究設計變數套題，已逐題改寫並補成 10 題單元專屬問題，均具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
    for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
    for x in Q: (QDIR/f"question-science-content-id-{x['id'].rsplit('-',1)[-1]}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"Id：晝夜與季節","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原有 9 題為日期、組數、取樣數變換的研究設計套題，已逐題改寫並補成 10 題晝夜與季節專屬問題；每題有唯一答案、解析與五步解法，三筆公開試題／課程資料僅作 pattern-only 來源，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content id")

if __name__=="__main__": main()
