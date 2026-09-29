"""Kc-Ⅳ-4：電流生磁場與安培右手定則的錯置題修正與第一輪融合。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-kc-iv-4.json"; REPORT=ROOT/"implementation/reports/science-content-kc-iv-4-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"電流生磁場、右手定則、電磁鐵與實驗判讀","pattern":"取電流方向、磁場方向、線圈磁極與控制變因的能力方向，重新設計校園電磁檢測情境。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"直導線磁場、螺線管、指南針與反接電源","pattern":"取由觀察證據連到圓形磁場與磁極方向的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"安培右手定則、磁力線、電磁鐵與實驗控制","pattern":"取方向判讀與裝置比較的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
ITEMS=[
 (1,"長直導線電流由紙面向讀者流出；依安培右手定則，導線周圍磁場方向為何？",["以導線為中心順時針","以導線為中心逆時針","全部向右","沒有磁場"],"B","右手拇指指向紙外電流，四指彎曲方向為逆時針磁場。磁場是繞導線的圓形方向，不是單一直線箭頭。","先確認電流是紙外圓點，再用右手拇指和四指判斷圓周方向。"),
 (2,"長直導線電流由紙面向內流入；在同一觀察位置，磁場方向相較電流向外時如何？",["仍為逆時針","反為順時針","一定消失","只變成直線方向"],"B","反轉電流方向會使同一位置的圓形磁場方向反轉；紙內電流對應順時針。","把電流箭頭改成紙內叉號，再重新做右手動作，不要背單一圖形。"),
 (3,"通電直導線附近指南針偏轉，哪項結論最直接受到觀察支持？",["導線周圍存在會影響指南針的磁場","導線一定具有永久磁性","指南針產生電流","電流方向無法改變磁場"],"A","指南針偏轉表示周圍有磁場方向與地磁合成後改變；要再用控制實驗判斷磁場來自通電導線。","比較通電與斷電、導線位置與指南針方向，分開觀察和因果推論。"),
 (4,"其他條件相同，若通電直導線的電流增加，附近同一位置的磁效應通常如何？",["增強","必定減弱到零","方向一定反轉","與電流大小無關"],"A","電流增大通常使導線周圍磁場增強；方向仍由電流方向決定，大小和方向是不同判斷。","固定方向與觀察距離，只改變電流，比較指南針偏轉或磁場測量值。"),
 (5,"同一通電直導線，指南針從近處移到較遠處；在其他條件不變下，磁場通常如何？",["較弱","較強且方向一定反轉","完全不變","只改變指南針重量"],"A","長直導線周圍磁場通常隨距離增加而減弱，但繞行方向由電流方向決定，不會因遠近自動反轉。","固定電流和方位，只改變距離，分開記錄強弱與方向。"),
 (6,"用右手握住通電螺線管，四指沿傳統電流繞行方向彎曲；拇指所指的一端代表？",["螺線管的 N 極方向","電流表負端","一定是 S 極","地磁南方而與線圈無關"],"A","右手四指沿線圈電流方向時，拇指指向螺線管內部磁場和 N 極方向。","先沿繞線方向放四指，再看拇指指向哪一端，避免直接猜磁極。"),
 (7,"螺線管電池反接，線圈匝數與電流大小近似不變；最可能發生什麼？",["N、S 極互換，磁場方向反轉","線圈磁場完全消失","匝數自動增加","只有電阻變大"],"A","電池反接使傳統電流方向反轉，依右手定則螺線管的磁場與 N、S 極互換。","追蹤電源極性、繞線電流方向與右手拇指方向三個箭頭。"),
 (8,"比較兩個螺線管的磁效應，甲匝數較多但電流較小，乙匝數較少但電流較大；最公平的判斷是？",["只看匝數就能決定誰較強","只看電流就能決定誰較強","需控制長度、鐵芯、匝數與電流等條件，不能由單一資訊直接判定","兩者一定完全相同"],"C","螺線管磁效應與匝數密度、電流、鐵芯及幾何有關；資訊不足時應保留不確定性。","列出影響變因，先統一幾何與材料，再比較匝數密度和電流。"),
 (9,"想研究電流大小是否影響直導線附近磁場強度，哪項設計較適當？",["固定導線、距離與方向，只改變電流並重複讀取指南針偏角","同時改變距離與電流","每次換不同指南針不校正","只記錄電池顏色"],"A","固定距離、導線方向與儀器，單獨改變電流並重複測量，才能把偏轉差異歸因於電流。","明確列出自變因、控制變因和測量量，再建立多個電流工作點。"),
 (10,"下列哪項沒有把安培右手定則和載流導線受力的左手規則混淆？",["右手定則判斷電流產生的磁場方向，左手規則可判斷磁場中電流導線的受力方向","兩者都只判斷電壓大小","右手定則只適用電池，左手規則只適用指南針","看到任何箭頭都不需確認研究對象"],"A","安培右手定則處理電流造成的磁場；載流導線在外磁場中的受力則是另一個方向關係，須先確認問題對象。","先讀題目問的是產生磁場還是受到磁力，再選擇相應規則與箭頭。"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以校園電磁檢測站為入口，先用指南針偏轉證明通電導線周圍有磁場，再把紙外／紙內電流、圓形磁力線、距離與電流大小放進安培右手定則。最後將每匝線圈的磁場疊加成螺線管 N、S 極，利用反接電源、匝數與控制變因把模型遷移到電磁鐵與繼電器。"; lesson["studyHighlights"]=["用指南針偏轉與圓形磁力線建立電流生磁證據。","以右手拇指與四指判斷直導線和螺線管磁場方向。","區分電流方向、磁場方向、強弱與觀察距離。","用反接、匝數、鐵芯與控制變因分析電磁鐵。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以電流、磁場、指南針、線圈與電磁裝置理解電磁作用。","方向判讀、磁極、觀察證據與控制變因是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向電磁與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以三張導線截面、指南針偏轉、紙內／紙外切換、螺線管反接與電磁鐵比較建立本課互動。","移除原本日期—電壓—電阻批次題，改為右手定則、磁場強弱、磁極與實驗設計題。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織電流生磁、直導線、螺線管、右手定則、磁極與控制變因；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for i,prompt,opts,ans,exp,strat in ITEMS:
  p=QDIR/f"question-science-content-kc-iv-4-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{exp} 正確答案為選項 {ans}：「{opts[ord(ans)-65]}」。"}; q["examPatternRefs"]=refs(); q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然／理化試題的電流生磁、直導線、螺線管、右手定則、指南針與實驗控制能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開試題能力方向，題幹、選項、答案、解析與五步解法均以 Kc-Ⅳ-4 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["solutionStrategy"]=strat; q["solutionSteps"]=["圈出傳統電流方向、導線／線圈幾何、觀察點與磁極問題。",f"依本題情境套用判準：{strat}","用安培右手定則建立磁場圓周或螺線管拇指方向。","排除把受力規則、電子方向、磁場強弱與方向混為一談的選項。","回查答案是否符合圖示、控制條件與觀察證據，並寫出限制。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Kc-Ⅳ-4：電流生磁場與安培右手定則","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"replacedMisalignedQuestionBank":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原日期—電壓—電阻批次題；三筆公開試題僅作 pattern-only 來源。版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content kc iv 4")
if __name__=="__main__": main()
