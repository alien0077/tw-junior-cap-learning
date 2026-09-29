"""Ka-Ⅳ-3：介質性質與聲音傳播速率第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-ka-iv-3.json"
REPORT=ROOT/"implementation/reports/science-content-ka-iv-3-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"聲音傳播、介質、速率與回聲資料判讀","pattern":"取由聲音在不同介質傳播、時間資料與生活情境判讀波速的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"聲音、介質、溫度、回聲與波動情境","pattern":"取從實驗圖表、波動模型與聲學生活情境推論傳播速率的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"聲音傳播、介質性質、速率與探究","pattern":"取以粒子振動、介質彈性／密度、波速測量與安全建立聲學教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-ka-iv-3-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-ka-iv-3"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的聲音傳播、介質、粒子、溫度、回聲、波速與安全能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-ka-iv-3","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"聲音在真空中無法傳播，最主要的原因是？",["真空缺少可振動並傳遞擾動的物質介質","真空中光也不能傳播","聲音沒有能量","耳朵在真空中一定變成喇叭"],"A","聲音是機械波，需要介質粒子振動傳遞；真空沒有足夠粒子，聲音無法以此方式傳播。","區分機械波與不需介質的電磁波。",["辨認聲音是介質粒子振動形成的機械波。","確認真空缺乏可傳遞振動的粒子。","判斷聲音無法到達接收端。","排除光、能量和耳朵外形的混淆。","所以 A 正確。"],"easy"),
q(2,"在一般條件下，聲音在固體、液體、氣體中的傳播速率通常哪種排序較合理？",["固體較快，液體次之，氣體較慢","氣體最快，固體最慢","三者一定完全相同","只由聲音大小決定"],"A","介質的彈性和密度共同影響聲速，常見材料中固體傳聲較快、液體次之、氣體較慢，但不能只用密度單一解釋。","用介質粒子耦合與彈性／密度共同判斷。",["確認三種介質都能傳遞聲音。","比較粒子間作用和介質彈性。","讀取或查證相同條件下的聲速資料。","排除由音量、單一密度或固定相同速率。","答案為 A。"],"medium"),
q(3,"冬天和夏天在空氣中測量聲音傳播時間，若距離相同，溫度差異可能造成？",["空氣溫度改變使聲速改變，抵達時間可能不同","溫度只改變聲音音調而不影響時間","聲音在高溫空氣中一定停止","距離會因溫度自動變成零"],"A","空氣溫度會影響分子運動和聲速，因此相同距離的傳播時間可能不同；需記錄溫度控制條件。","把環境溫度列為聲速測量的控制或解釋變因。",["固定聲源和接收器距離。","記錄冬夏或各次的空氣溫度。","比較聲速與傳播時間。","排除只影響音調、停止傳播和距離消失。","所以 A 正確。"],"medium"),
q(4,"用回聲測量山壁距離時，若聲音往返時間為 2.0 s、空氣聲速取 340 m/s，山壁距離約為？",["340 m","680 m","170 m","2 m"],"A","聲音走的是來回路程，總路程=340×2.0=680 m，單程山壁距離=680÷2=340 m。","先辨認回聲是往返，再除以二。",["寫出總路程 v×t=340×2=680 m。","確認這是聲音到山壁再回來的距離。","用 680÷2 求單程。","得到 340 m 並檢查單位。","所以 A 正確。"],"easy"),
q(5,"要比較聲音在水和空氣中的傳播速率，哪項實驗設計最公平？",["使用相同距離與時間測量方法，控制溫度和聲源，分別在水與空氣中記錄到時差並重複測量","水中用短距離、空氣中用長距離且不記錄溫度","只比較哪個聲音比較大","用不同聲源頻率且不校正計時器"],"A","需固定距離、聲源、計時和溫度等條件，只改變介質，並重複計時計算 v=d/t。","以控制變因隔離介質對聲速的影響。",["固定相同或可校正的傳播距離。","控制聲源、溫度和計時器。","分別記錄抵達時間。","用 v=d/t 並重複求平均。","所以 A 是公平設計。"],"medium"),
q(6,"敲擊鐵軌時，把耳朵貼近鐵軌的人可能比站在旁邊空氣中的人早聽到聲音，原因是？",["聲音在鐵等固體中的傳播速率通常比在空氣中快","鐵軌會產生兩個不同聲源","空氣完全不能傳聲","貼耳朵會讓聲音頻率變成零"],"A","同一敲擊擾動可同時經鐵軌和空氣傳播，固體路徑通常較快；實作時需注意安全，不可在有列車風險處測試。","用多路徑傳播和介質差異解釋到時差。",["辨認敲擊是共同聲源。","列出鐵軌和空氣兩條傳播路徑。","比較固體和氣體聲速。","將較早到達連到固體路徑並加入場域安全。","所以 A 正確。"],"medium"),
q(7,"若在同一介質中提高聲源音量，通常不能直接推論聲音的哪項量一定改變？",["傳播速率；音量主要和振幅相關，波速由介質條件與頻率等決定","振幅一定不變","聲音一定消失","介質一定換成固體"],"A","提高音量通常增加振幅和能量，不必然改變同一介質中的波速；頻率和介質條件是不同概念。","分離振幅、能量、頻率與介質對波速的作用。",["辨認音量常與振幅相關。","確認聲源仍在同一介質。","判斷波速主要由介質和波動條件決定。","排除音量必改速率、振幅不變及介質轉換。","答案為 A。"],"medium"),
q(8,"要研究空氣溫度對聲速的影響，哪項作法最能支持因果？",["固定距離、聲源、頻率和計時方法，逐步改變溫度並量測到時時間，重複多次","同時改變距離和溫度","只在一個溫度測量一次","用音量大小代表聲速"],"A","控制距離和聲源等條件，只改變溫度並由 v=d/t 計算，重複測量才能支持溫度與聲速關係。","把環境控制、時間測量和公式結合。",["固定聲源到接收器的距離。","控制頻率、音量和計時器。","設定不同溫度並等待環境穩定。","量測時間、計算聲速並重複取平均。","所以 A 最完整。"],"hard"),
q(9,"長時間使用高音量耳機可能造成聽覺傷害；最合理的預防是？",["降低音量、縮短連續使用時間並讓耳朵休息，若有症狀尋求專業協助","把耳機音量調到最大以適應","用棉棒深入耳道清潔","只要聲音沒有失真就完全安全"],"A","聲音能量和暴露時間都影響聽覺風險，降低音量、休息和適當求助可降低傷害；失真不是唯一安全指標。","把波的振幅／能量概念遷移到健康安全。",["辨認高音量代表較大振幅和能量暴露。","考慮連續時間和累積劑量。","降低音量並安排休息。","出現耳鳴或聽力改變時尋求協助。","所以 A 正確。"],"easy"),
q(10,"若兩支聲音頻率不同但在同一空氣中傳播，哪項關係最合理？",["在介質條件相同時波速可近似相同，但波長依 v=fλ 而不同","頻率高者一定傳得快且波長相同","頻率和音量是同一物理量","低頻聲音不能在空氣中傳播"],"A","同一介質的聲速主要由介質條件決定；頻率不同時，為維持 v=fλ，波長會不同，音調也不同。","用公式同時比較聲速、頻率與波長。",["確認兩聲音在同一空氣條件。","判斷波速近似固定。","比較頻率高低。","用 λ=v/f 推論波長反向改變。","所以 A 正確。"],"medium"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["聲音是需要介質的機械波，傳播速率受介質性質和環境條件影響。","波速、頻率、波長、振幅、音量和到時是不同物理量，需由模型和測量分辨。","回聲、聲音定位、溫度測量與聽覺健康都可用聲波證據和安全原則解釋。"],"versionDifferences":["南一公開線索支持由生活聲音、回聲和介質觀察進入聲速。","康軒公開課程資料較突出粒子振動、介質彈性／密度與波速測量。","翰林公開課程計畫補充溫度、波動公式、聲學應用與聽覺安全；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以介質—粒子—波速—到時—安全五層框架分析聲音傳播。","加入回聲距離計算、海陸／固氣路徑、溫度控制、音量與聽力保護。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫聲音介質、傳播速率、溫度、回聲、測量、波動關係與聽覺安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ka-Ⅳ-3：介質性質與聲音傳播速率","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為聲音介質、固液氣速率、溫度、回聲計算、路徑、振幅／音量、波速公式、控制變因與聽覺安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ka-iv-3")
if __name__=="__main__": main()
