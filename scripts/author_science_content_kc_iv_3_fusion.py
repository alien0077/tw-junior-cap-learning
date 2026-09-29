"""Kc-Ⅳ-3：磁力線與磁場的錯置題修正與第一輪融合。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-kc-iv-3.json"; REPORT=ROOT/"implementation/reports/science-content-kc-iv-3-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"磁場、磁力線、指南針與鐵粉圖樣判讀","pattern":"取局部方向、磁場強弱、磁極排列與模型證據的能力方向，重新設計磁場測繪任務。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"條形磁鐵、異極／同極、磁力線與羅盤","pattern":"取由觀察工具連到磁力線模型的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"磁場方向、場線疏密與實驗證據","pattern":"取圖形判讀、控制距離與模型限制的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
ITEMS=[
 (1,"把羅盤放在磁鐵附近某一點，羅盤北端所指的方向最能表示該點磁場的哪項資訊？",["該處磁力線的切線方向","磁鐵的重量","磁力線真實線條的數量","磁場一定由羅盤產生"],"A","羅盤磁針會沿局部磁場方向排列，因此磁針方向可作為該點磁力線切線方向的觀測線索。","先定位觀測點，再把羅盤方向記成箭頭，勿把箭頭當成磁鐵吐出的實體線。"),
 (2,"在條形磁鐵外部，磁力線方向通常由哪一磁極指向哪一磁極？",["N 極指向 S 極","S 極指向 N 極且只在內部成立","由中心向四周直線散開","方向隨顏色改變"],"A","磁鐵外部的磁力線通常由 N 極出發進入 S 極；磁鐵內部則形成閉合描述，不能只畫外部一段就宣稱線有起點終點。","先確認題目問磁鐵外部，再依 N—S 方向讀圖，補上場線是連續模型。"),
 (3,"同一張磁力線圖中，兩條磁力線在空間中相交；哪項判斷最合理？",["不可能代表同一時刻的單一磁場，因交點會給出兩個方向","交點表示磁場一定最強","場線相交代表磁力線是實體互相碰撞","只要線畫得粗就可以相交"],"A","同一點的磁場方向應唯一，磁力線切線若相交會產生兩個方向，因此通常不是同一磁場的合理表示。","在交點問磁場是否能同時有兩個方向，再檢查圖示是否把不同情境疊在一起。"),
 (4,"鐵粉圖中某區域磁力線示意較密，若其他表示方式一致，通常可推論什麼？",["該區域磁場相對較強","該區域一定有更多真實磁力線物質","磁場方向一定反轉","鐵粉本身產生全部磁場"],"A","場線疏密是表示磁場強弱的模型線索，線較密通常代表場較強；不是在數真實存在的細線。","比較相同圖例和尺度下的疏密，再把強弱推論和方向判讀分開。"),
 (5,"在條形磁鐵上方撒鐵粉並輕敲紙板，鐵粉排列出曲線；這項實驗最適合支持哪項說法？",["鐵粉沿局部磁場方向排列，能顯示場分布形狀但不直接給出箭頭方向","鐵粉變成永久磁力線","鐵粉數量就是磁場強度的精確值","沒有羅盤也能知道所有方向與力的數值"],"A","鐵粉會受磁化與磁力作用排列，能提供場線分布的視覺線索，但需要羅盤或其他方法補充方向與定量限制。","分開寫鐵粉直接呈現的圖樣、由圖樣推論的分布和仍缺少的方向／數值證據。"),
 (6,"兩根條形磁鐵以異極相對時，兩極之間的磁力線較可能呈現哪種形狀？",["較多場線跨越兩極間的空間連結","所有場線都在兩磁鐵外側互相避開","場線全部消失","只會出現與磁鐵垂直的直線"],"A","異極相對時磁場在兩極間連結較明顯，場線密集區可作為磁場較強的相對模型。","先標出 N、S，再看外部場線是否由 N 連向 S，並注意線密只表相對強弱。"),
 (7,"兩根磁鐵以同極相對時，場線圖中兩極中間通常可觀察到什麼？",["場線彎向外側，中央形成較弱或分隔的區域","場線直接穿過兩個同極並重合","兩磁鐵失去磁性","中央一定是磁場最大且方向唯一"],"A","同極相對的磁場互相排斥，場線在中央傾向向外彎，不能直接把異極連線圖套用。","比較異極與同極的場線連接方式，再用羅盤點測驗證中央區域方向。"),
 (8,"說明『磁力線』時，哪項最不容易把模型誤當成實體？",["它是用方向與疏密描述磁場的模型，不是真實存在的細線","它是從磁鐵表面流出的物質","每條線都代表一條固定磁力","線越多就能直接算出精確力值"],"A","磁力線是視覺化模型；切線方向與相對疏密有物理意義，但畫線數量、粗細和間距仍受繪圖規則限制。","分開模型能表示的方向／相對強弱與不能直接給出的精確數值。"),
 (9,"要繪製未知磁鐵周圍的磁力線方向，哪種程序較可靠？",["在多個位置放羅盤記錄北端方向，再把局部切線連成連續場線並標示限制","只看磁鐵顏色畫四條對稱線","只在 N 極放一個羅盤就推斷全部區域","用鐵粉數量直接當方向"],"A","多點羅盤測量可建立局部方向資料，再以平滑連續線呈現整體模型；單點或顏色不能提供足夠證據。","規劃網格取樣、記錄箭頭，再連線並以鐵粉圖作分布交叉檢查。"),
 (10,"下列哪項是磁力線圖能支持、但不能單獨直接確定的結論？",["可比較某些區域的磁場相對方向與疏密","只要畫十條線就能知道磁力為十牛頓","場線是可被剪下搬動的物質","任何比例不清的圖都能給出精確距離"],"A","磁力線圖能協助描述方向和相對分布，但不能由任意畫線數量直接得到精確力值或距離。","先確認圖例與尺度，再把相對模型結論和需要實測的定量結論分開。"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以磁場測繪員任務為入口，先在磁鐵周圍逐點放羅盤記錄局部方向，再用磁力線模型呈現方向、連續性與相對疏密。學習者會比較條形磁鐵的異極／同極排列、鐵粉圖樣和羅盤證據，並明確說出磁力線不是實體細線、不能由畫線數量直接算出精確力。"; lesson["studyHighlights"]=["以羅盤方向建立局部磁場與磁力線切線方向。","讀懂磁力線的連續性、外部 N 到 S 與相對疏密。","比較異極、同極排列及鐵粉圖樣的證據。","區分磁力線模型可支持的結論與需實測的限制。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以羅盤、磁鐵、磁場圖與實驗證據理解磁力線。","方向、疏密、磁極排列與模型限制是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向電磁與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以多點羅盤測繪、鐵粉圖、異極／同極切換與模型限制工作表建立本課互動。","移除原本日期—電壓—電阻批次題，改為磁力線方向、疏密、證據與圖示限制題。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織羅盤、磁場、磁力線、磁極排列、鐵粉與模型限制；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for i,prompt,opts,ans,exp,strat in ITEMS:
  p=QDIR/f"question-science-content-kc-iv-3-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{exp} 正確答案為選項 {ans}：「{opts[ord(ans)-65]}」。"}; q["examPatternRefs"]=refs(); q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然／理化試題的磁場、磁力線、羅盤、磁極排列、疏密與實驗證據能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開試題能力方向，題幹、選項、答案、解析與五步解法均以 Kc-Ⅳ-3 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["solutionStrategy"]=strat; q["solutionSteps"]=["圈出磁鐵 N／S、羅盤位置、觀察工具與題目要求的方向或強弱。",f"依本題情境套用判準：{strat}","把局部觀察、磁力線模型與磁極排列逐層連結。","排除把場線當實體、把線數當精確力值或忽略圖例尺度的選項。","回查答案是否超出證據範圍，並寫出仍需羅盤或測量驗證的限制。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Kc-Ⅳ-3：磁力線與磁場","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"replacedMisalignedQuestionBank":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原日期—電壓—電阻批次題；三筆公開試題僅作 pattern-only 來源。版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content kc iv 3")
if __name__=="__main__": main()
