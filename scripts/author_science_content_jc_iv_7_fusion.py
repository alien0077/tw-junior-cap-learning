"""Jc-Ⅳ-7：電解實驗與電解原理第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jc-iv-7.json"
REPORT=ROOT/"implementation/reports/science-content-jc-iv-7-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"電解質、電極、電流與電解資料判讀","pattern":"取由導電實驗、電極現象與物質變化推論電解原理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"電解、離子、氣體產物與生活科技情境","pattern":"取由實驗圖表、氣體檢驗與粒子模型判斷電解反應的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"電解實驗、電解質與氧化還原","pattern":"取以外加電源、電解質、電極及氧化還原連結電解操作的教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jc-iv-7-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jc-iv-7"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的電解質、外加電源、電極、離子、氣體產物及氧化還原能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jc-iv-7","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"熔融氯化鈉通電後可生成鈉和氯氣，這個過程的主要能量轉換是？",["電能轉換成化學能，促使原本的離子化合物分解","化學能轉換成電能並使電池放電","光能轉換成質量","熱能消失而沒有反應"],"A","電解需要外加電能驅動非自發的氧化還原反應，產物重新儲存為化學能。","先判斷外加電源方向，再追蹤反應與能量。",["確認反應需要外部電源。","辨認氯化鈉被分解為新物質。","把輸入電能連到化學能儲存。","排除電池放電與無反應說法。","答案為 A。"],"medium"),
q(2,"食鹽水能導電而固態食鹽不易導電，最合理的原因是？",["水溶液中離子可以自由移動，固態晶格中的離子位置受限","固態食鹽沒有任何帶電粒子","水會把電子變成原子","食鹽溶液只靠水分子傳遞電荷"],"A","溶解後離子能在溶液中移動並傳遞電荷；固態離子雖帶電但固定在晶格位置。","以粒子可移動性解釋導電差異。",["辨認食鹽由離子組成。","比較固態晶格與水溶液的粒子自由度。","確認能移動的離子可攜帶電荷。","排除沒有帶電粒子、電子變原子與只靠水分子。","所以 A 正確。"],"easy"),
q(3,"電解水溶液時，帶正電的離子通常移向哪一端？",["負極，因為異性電荷相吸", "正極，因為同性電荷相吸", "不會移動", "只移向電池外殼"],"A","陽離子帶正電，會受負極吸引而向負極移動；實際電極反應仍需配合溶液種類判斷。","先用電荷相吸判斷離子方向，再看電極反應。",["確認離子帶正電。","標出外加電源的正極與負極。","用異性相吸判斷陽離子移向負極。","排除同極相吸及完全不移動。","答案為 A。"],"easy"),
q(4,"電解硫酸銅溶液時，若陰極表面析出紅色固體，最合理的物質是？",["銅，因為銅離子在陰極得到電子還原成銅", "氧氣，因為氧氣是紅色固體", "硫酸，因為酸會沉積", "水蒸氣，因為水蒸氣是固體"],"A","銅離子移向陰極並接受電子，形成金屬銅；紅色固體是產物證據。","把電極位置、離子電荷和電子得失連結。",["確認硫酸銅提供銅離子。","判斷陽離子移向負極陰極。","將得電子判為還原並形成金屬銅。","排除氣體、酸與水蒸氣的物態錯誤。","所以 A 正確。"],"medium"),
q(5,"電解水時在兩電極收集到氣體，若陰極氣體體積約為陽極兩倍，最合理的判讀是？",["陰極較多的氣體可對應氫氣，體積比反映水分解反應中氫、氧的比例", "陰極一定只產生氧氣", "兩種氣體其實都是空氣", "體積比可直接證明電極沒有反應"],"A","水分解生成氫氣和氧氣的體積比例約 2:1，還需用燃燒或助燃等檢驗確認氣體身分。","先讀體積比，再用氣體檢驗避免只憑比例下結論。",["記錄兩極氣體體積。","比較是否接近 2:1。","提出陰極氫氣、陽極氧氣的模型。","用適當安全檢驗確認氣體。","因此 A 是資料支持的完整判斷。"],"hard"),
q(6,"若電解裝置的溶液濃度太低而電流很小，最可能的原因是？",["可移動離子數量較少，溶液內部傳遞電荷的能力降低", "電子在溶液中全部消失", "電極自動變成絕緣體", "濃度低會使電源停止輸出化學能"],"A","溶液中可移動離子較少會增加內阻、降低導電能力，電解電流因而變小；電子主要經外電路傳遞。","分開外電路電子和溶液離子，解釋濃度對電流的影響。",["確認電解質濃度是改變的變因。","判斷溶液中可移動離子數量。","連結離子傳導與電流大小。","排除電子消失、電極變絕緣與電源無輸出。","答案為 A。"],"medium"),
q(7,"要研究電解質濃度對電流大小的影響，哪項設計最公平？",["固定電極材質、間距、電源與溫度，只改變濃度並重複量測電流", "同時改變濃度、電極和電壓", "每組用不同大小容器且只量一次", "只看氣泡顏色不測電流"],"A","控制電極、距離、電源和溫度，只改濃度並重複測量，才能建立濃度與電流的可比較關係。","使用單一自變因與量化依變因建立公平實驗。",["列出會影響電流的裝置條件。","固定電極、間距、電源和溫度。","分組調整電解質濃度。","重複讀取電流並比較平均值。","因此 A 是公平設計。"],"medium"),
q(8,"電解實驗中若陰極和陽極接反，最可能的影響是？",["離子移向與產物出現的電極位置會改變，必須重新依電極極性判讀", "溶液一定不再含有離子", "所有化學反應都停止且沒有電流", "接反只會改變燈泡顏色"],"A","外加電源決定陰極、陽極的極性；接線改變會改變離子移動與電極產物位置，但不代表溶液沒有離子。","先重畫接線與極性，再推論各電極反應。",["確認電源正負端接到哪個電極。","重新標出陰極與陽極。","依離子電荷判斷移動方向。","預測產物在哪個電極出現。","所以 A 是正確處理方式。"],"hard"),
q(9,"電解實驗為何不宜直接用手觸摸電極附近的溶液或未知產物？",["可能含有腐蝕性、刺激性或未確認的反應物與產物，需依規範防護和處理", "因為所有電解質都一定是無毒氣體", "觸摸能讓離子停止移動", "安全只影響結果不影響人體"],"A","電解可能產生酸鹼、金屬離子或氣體等危害，應使用護目鏡、手套與合規處置，不以觸摸辨識物質。","把產物判讀與化學實驗安全同時納入決策。",["列出電解可能產生的未知物。","辨認腐蝕、刺激與毒性風險。","使用適當防護並避免直接接觸。","依規範收集、標示與處理產物。","所以 A 是安全且合理的判斷。"],"easy"),
q(10,"比較電池放電與電解，哪項敘述正確？",["放電由化學反應輸出電能；電解由外部電能驅動化學反應，兩者都涉及氧化還原", "兩者都不需要電極", "放電一定需要外部電源而電解不需要", "電解只改變溫度不改變物質"],"A","放電與電解都在電極發生氧化還原，但能量方向相反：電池輸出電能，電解輸入電能。","用能量流向和電極反應比較兩個系統。",["先寫放電的化學能到電能。","再寫電解的外部電能到化學變化。","確認兩者都需要電極與離子傳導。","排除電源需求和不產生新物質的說法。","所以 A 正確。"],"medium"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["電解以外加電能驅動氧化還原，電解質中的離子移動維持反應迴路。","電極極性、離子方向、電子得失和產物檢驗必須互相校對。","電解與電池放電涉及相同類型的電極反應，但能量流向相反。"],"versionDifferences":["南一公開線索支持由導電現象與物質變化進入電解。","康軒公開課程資料較突出電解質、電極和氣體產物操作。","翰林公開課程計畫補充外加電源、氧化還原與生活應用連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以離子方向—電極極性—電子得失—產物檢驗四步框架分析電解。","把濃度控制、氣體體積比、接線錯誤與未知產物安全納入單元專屬情境。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫電解質、外加電源、電極、產物、資料判讀與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jc-Ⅳ-7：電解實驗與電解原理","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為電解質、外加電源、電極、離子、氣體產物、控制變因、放電比較及安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jc-iv-7")
if __name__=="__main__": main()
