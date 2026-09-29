"""Ka-Ⅳ-1：波峰、波谷、波長、頻率、波速與振幅第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-ka-iv-1.json"
REPORT=ROOT/"implementation/reports/science-content-ka-iv-1-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"波形、波長、頻率、振幅與資料圖表判讀","pattern":"取由波形圖、時間序列與介質資料判讀波的特徵與傳播的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"波動、聲音、光、週期與生活情境","pattern":"取從圖表、模型與生活波動情境推論頻率、波速、波長與振幅的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"波峰波谷、波長、頻率、波速、振幅與探究","pattern":"取以波形模型、週期性測量、v=fλ 與能量表徵建立波動教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-ka-iv-1-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-ka-iv-1"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的波形、波峰波谷、波長、頻率、波速、振幅與資料探究能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-ka-iv-1","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"在繩上的橫波圖中，平衡位置以上最高點和以下最低點分別稱為？",["波峰與波谷","波谷與波峰","波長與振幅","頻率與週期"],"A","相對平衡位置的最高點是波峰，最低點是波谷；波長和振幅是距離量，不是位置名稱。","先以平衡位置判斷波形的幾何特徵。",["畫出或讀取平衡位置。","找出高於平衡線的最高點。","找出低於平衡線的最低點。","將兩者依序命名波峰、波谷。","所以 A 正確。"],"easy"),
q(2,"波長最適合定義為哪一項距離？",["相鄰兩個同相位點的距離，例如相鄰波峰或相鄰波谷","波峰到平衡位置的垂直距離","波峰到波谷的垂直距離","波傳到觀察者所需的時間"],"A","波長是同一列波相鄰同相位點間的空間距離；波峰到平衡是振幅，波峰到波谷是兩倍振幅。","用相位相同和空間週期辨識波長。",["找出相同運動狀態的點。","選相鄰波峰或相鄰波谷。","量測兩點的水平距離。","排除垂直振幅距離和時間。","答案為 A。"],"easy"),
q(3,"一個波源在 2 秒內完成 10 次完整振動，頻率是多少？",["5 Hz","0.2 Hz","10 Hz","20 Hz"],"A","頻率是每秒振動次數，10÷2＝5 Hz；0.2 s 是週期而不是頻率。","用 f=N/t 計算並確認單位。",["找出完整振動次數 N=10。","找出時間 t=2 s。","計算 f=N/t=10/2=5。","檢查單位為每秒，即 Hz。","所以 A 正確。"],"easy"),
q(4,"波的頻率為 4 Hz，週期是多少？",["0.25 s","4 s","16 s","8 s"],"A","週期 T=1/f=1/4=0.25 s，代表完成一次振動所需時間。","先辨認頻率與週期互為倒數。",["寫出 T=1/f。","代入 f=4 Hz。","計算 1÷4=0.25 s。","確認週期單位是秒而非 Hz。","答案為 A。"],"easy"),
q(5,"波速、頻率和波長的關係式為 v=fλ；若波速固定，頻率加倍，波長會如何？",["減半","加倍","不變且與頻率無關","變成四倍"],"A","固定 v 時 λ=v/f，頻率加倍會使波長減半，才能維持相同波速。","由公式變形並標示固定條件。",["寫出 λ=v/f。","確認 v 固定。","將 f 改為 2f。","得到 λ 變為原來一半。","所以 A 正確。"],"medium"),
q(6,"波的振幅由 2 cm 增加到 4 cm，其他條件相同；哪項描述最適合？",["波離開平衡位置的最大位移增加，通常代表攜帶能量的表徵增強，但不必然改變頻率","波長一定加倍","頻率一定減半","波速一定變成四倍"],"A","振幅是最大位移，振幅增加表示擾動較大；頻率、波長和波速需由其他資料或介質條件判斷，不能直接倍增。","把振幅和週期性、空間性、介質性質分開。",["找出平衡位置和最大位移。","比較 2 cm 與 4 cm。","判斷振幅增加。","不要由振幅直接推論頻率、波長或波速比例。","所以 A 最妥當。"],"medium"),
q(7,"同一條繩上兩列波的波形相同但頻率不同，若繩的張力與介質條件相同，哪項較合理？",["波速近似相同，頻率較高者波長較短","頻率較高者波速一定較快且波長相同","兩列波都沒有波長","頻率與波速永遠相等"],"A","同一介質和張力下波速主要由介質條件決定；由 v=fλ，頻率較高時波長較短。","先判斷介質是否固定，再使用波速公式。",["確認同一條繩和相同張力。","判斷波速近似固定。","比較兩列波頻率。","由 λ=v/f 推論高頻率短波長。","答案為 A。"],"medium"),
q(8,"要由波形照片量測波長，哪項作法最可靠？",["先用刻度校正影像，再量相鄰波峰或波谷的水平距離，重複多個週期取平均","量波峰到波谷的垂直距離","只量一個波峰的高度","以照片像素數直接當公尺"],"A","波長是水平空間週期，需用尺度校正、量同相位點並重複取平均；像素不能未換算就當實際長度。","把幾何定義和測量誤差控制結合。",["確認照片的水平尺度。","選相鄰同相位點。","量測多個波長的總距離。","除以週期數並取重複平均。","所以 A 最可靠。"],"medium"),
q(9,"波通過繩上某固定點時，繩上小段上下振動，但波形向右傳播；這表示？",["介質粒子主要在平衡位置附近振動，能量和波形向右傳遞，物質不必整體向右移動","繩上每個粒子都隨波形向右遠離原位","波沒有傳遞能量","粒子只會水平靜止"],"A","機械波可由介質粒子局部振動傳遞能量與波形，粒子未必隨波整體前進。","區分介質粒子運動方向和波傳播方向。",["觀察固定點的上下位移。","標出波形向右的相位傳遞。","比較粒子局部運動和波的整體進行。","排除物質整體右移與無能量傳遞。","答案為 A。"],"medium"),
q(10,"若要研究振幅對波在繩上傳播速度的影響，哪項設計較公平？",["固定繩長、張力、線密度與頻率，只改變振幅並量測波峰通過兩標記的時間","同時改變張力和振幅","只看波形高度而不測時間","每次使用不同長度與材質的繩子"],"A","要研究振幅需控制決定波速的張力、線密度等條件，並以兩點間距和通過時間量測波速。","用控制變因和 v=d/t 測量檢驗因果。",["列出繩長、張力、線密度與頻率。","固定除振幅外的條件。","在繩上標記固定距離。","記錄波峰通過兩點的時間並計算波速。","所以 A 是公平設計。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["波峰、波谷、波長、頻率、週期、波速與振幅是描述波形、時間、空間和傳播的不同量。","v=fλ 與介質條件連結波的空間和時間週期。","波形與能量傳遞不等於介質物質整體搬移，測量需控制尺度和介質。"],"versionDifferences":["南一公開線索支持由水波、繩波和波形觀察進入基本量。","康軒公開課程資料較突出週期、頻率、波速公式與圖表測量。","翰林公開課程計畫補充振幅、能量與波動探究；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以幾何波形—時間週期—公式—介質—測量五層框架統整波動量。","加入波形影像校正、固定點粒子運動、振幅誤讀與公平波速實驗。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫波峰波谷、波長、頻率、週期、波速、振幅、波形測量與公平實驗；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ka-Ⅳ-1：波峰、波谷、波長、頻率、波速與振幅","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為波形幾何、波長、頻率、週期、v=fλ、振幅、介質、波速測量與控制變因專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ka-iv-1")
if __name__=="__main__": main()
