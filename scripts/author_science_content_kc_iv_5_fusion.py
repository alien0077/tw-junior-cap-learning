"""Kc-Ⅳ-5：載流導線受磁力與電動機的錯置題修正與第一輪融合。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-kc-iv-5.json"; REPORT=ROOT/"implementation/reports/science-content-kc-iv-5-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"載流導線、磁力方向、電動機與實驗變因","pattern":"取電流—磁場—受力三向關係與控制變因能力方向，重新設計方向檢查實驗。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"磁場、電流、線圈轉矩與能量轉換","pattern":"取由直導線受力連到線圈、換向與馬達模型的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"電動機、受力方向、換向器與實驗設計","pattern":"取方向判讀、力矩與裝置故障分析能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
ITEMS=[
 (1,"載流直導線放在磁場中時，哪個條件最能決定本課所討論的橫向磁力是否出現？",["只有導線顏色不同","有電流且導線與磁場方向不平行","只要導線很長就一定有力","只要附近有磁鐵就一定有力"],"B","磁力與電流、磁場及兩者夾角有關；導線與磁場平行時，本課的橫向磁力為零。","先標出傳統電流與磁場方向，再檢查夾角是否讓導線有有效受力分量。"),
 (2,"載流導線與均勻磁場方向完全平行，其他條件不變；其磁力最可能為何？",["最大","接近零","只由電阻決定","一定向上"],"B","導線與磁場平行時，電流方向在磁場中沒有垂直分量，因此橫向磁力為零或接近零。","先確認導線與磁場夾角，再使用方向規則判斷大小與方向。"),
 (3,"磁場方向固定，若把載流導線中的傳統電流方向反轉，受力方向通常如何？",["不變","反轉","一定變成零","只改變導線長度"],"B","受力方向由電流與磁場共同決定；只反轉電流，受力方向也會反轉。","固定磁場箭頭，只把電流箭頭反向，再用弗萊明左手規則重判。"),
 (4,"電流方向固定，若把外加磁場方向反轉，導線受力方向通常如何？",["反轉","不變","只增加溫度","必定消失且不需看角度"],"A","磁場方向是受力三向關係的一部分；只反轉磁場，受力方向會反轉。","固定電流與導線位置，反轉磁場箭頭，檢查受力向量如何改變。"),
 (5,"其他條件相同，將載流導線的電流增加，通常受磁力大小會如何？",["增加","減少到零","與電流無關","只改變磁場方向"],"A","在磁場、有效長度與夾角固定時，受力大小會隨電流增加而增加。","列出控制條件，只改變電流，再比較導線偏轉或力的測量值。"),
 (6,"矩形線圈兩側的載流導線在磁場中受到方向相反的力，為何可能使線圈轉動？",["兩力作用線分開形成力矩","兩力完全抵消所以一定不動","線圈自動產生重力","磁場只會吸引線圈"],"A","大小相近、方向相反但作用線分開的力可形成力偶，合力可能為零而合力矩不為零，於是線圈轉動。","先分開計算合力與力矩，再看兩側作用線是否形成轉動效果。"),
 (7,"直流電動機使用換向器的主要作用是什麼？",["在每半圈適時改變線圈電流方向，使轉矩方向能繼續推動轉動","讓線圈永遠沒有電流","把磁場完全消除","只增加電阻而不影響轉動"],"A","線圈轉過特定位置後，若電流不換向，轉矩可能反向；換向器讓轉矩維持同一轉動趨勢。","追蹤半圈前後線圈受力方向與轉矩方向，再連到換向器接點切換。"),
 (8,"電動機正常運轉時，最主要的能量轉換是？",["電能轉成機械能，並伴隨部分熱與聲音逸散","機械能轉成核能","熱能完全消失","磁場不需要任何能量就持續做功"],"A","電流在磁場中受力使轉子轉動，輸入電能轉為機械能，實際還有電阻與摩擦造成的能量逸散。","畫出電源輸入、磁力做功、轉動輸出及損失的能量流程。"),
 (9,"小馬達通電後只轉半圈便停止，電源與磁鐵正常；哪項檢查最直接對應本單元機制？",["檢查換向器與電刷接觸是否在轉動中正確切換電流","只測量外殼顏色","增加負載直到停止","把磁鐵移得更遠但不記錄條件"],"A","換向失效或接觸不良可能讓線圈轉過半圈後轉矩反向或中斷，符合只轉半圈的症狀。","先把故障現象對應到電流連續性、換向時序與轉矩方向，再設計單項檢查。"),
 (10,"研究電流大小是否影響載流導線受磁力，哪項設計最公平？",["固定磁場、導線有效長度與夾角，只改變電流並重複測量受力","同時改變磁鐵距離、導線長度與電流","每次換不同角度且只量一次","只記錄電流方向，不量受力大小"],"A","要研究電流的影響，磁場、有效長度與夾角等因素需固定，並以重複測量降低偶然誤差。","列出自變因、控制變因與測量量，固定幾何條件後分級改變電流。"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以方向檢查實驗為入口，先替直導線配對傳統電流、磁場與受力三個箭頭，再把兩側相反磁力放回線圈分析合力矩。學習者會比較電流、磁場、導線角度與有效長度的變化，理解換向器如何讓轉矩持續，最後用電刷與負載故障情境診斷小馬達只轉半圈的原因。"; lesson["studyHighlights"]=["用弗萊明左手規則判斷電流、磁場與受力三向關係。","區分導線平行於磁場時的零磁力與非平行時的受力。","從線圈兩側受力建立力偶、轉矩與換向器模型。","以電能—機械能轉換和單一變因實驗診斷馬達。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以磁場、電流、受力、力矩與能量轉換理解電動機。","方向判讀、線圈模型、換向與控制變因是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向電磁與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以方向檢查實驗桌、三箭頭配對、線圈力偶、換向器接點與半圈故障診斷建立本課互動。","移除原本錯置的歐姆定律日期—電壓—電阻題，改為十題電動機與載流導線受力原創推理。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織載流導線受磁力、弗萊明左手規則、線圈轉矩、換向器與電動機；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for i,prompt,opts,ans,exp,strat in ITEMS:
  p=QDIR/f"question-science-content-kc-iv-5-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{exp} 正確答案為選項 {ans}：「{opts[ord(ans)-65]}」。"}; q["examPatternRefs"]=refs(); q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然／理化試題的載流導線受力、磁場方向、電動機、換向與實驗控制能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開試題能力方向，題幹、選項、答案、解析與五步解法均以 Kc-Ⅳ-5 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["solutionStrategy"]=strat; q["solutionSteps"]=["圈出傳統電流、磁場、導線有效段、角度與線圈位置。",f"依本題情境套用判準：{strat}","用左手規則、力偶或能量鏈檢查方向與大小。","排除把磁力當吸引、把受力當電流方向或忽略換向的選項。","回查答案是否符合裝置條件，並寫出故障或實驗限制。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Kc-Ⅳ-5：載流導線受磁力與電動機","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"replacedMisalignedQuestionBank":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原錯置的歐姆定律題；三筆公開試題僅作 pattern-only 來源。版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content kc iv 5")
if __name__=="__main__": main()
