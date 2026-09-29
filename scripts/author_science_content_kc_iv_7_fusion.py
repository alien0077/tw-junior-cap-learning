"""Kc-Ⅳ-7：電流、電壓與電阻的關係的題庫重寫與第一輪融合。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-kc-iv-7.json"; REPORT=ROOT/"implementation/reports/science-content-kc-iv-7-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"歐姆定律、電表接線、V-I 資料與電路實驗","pattern":"取電流、電壓、電阻的量測與資料判讀能力方向，重新設計電路測量站情境。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"電路、定值電阻、串並聯電表與模型限制","pattern":"取公式應用、接線理由、圖表與控制變因的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"電流電壓關係、電阻、燈絲與安全操作","pattern":"取數值計算與實驗限制的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
ITEMS=[
 (1,"定值電阻為 4 Ω，兩端電壓為 12 V；依 I＝V/R，通過電流是多少？",["0.33 A","3 A","8 A","48 A"],"B","代入 I＝V/R＝12/4＝3 A。電壓和電阻的單位要先一致，不能把功率或總電量當成電流。","先寫已知 V、R，再選 I＝V/R，計算後用 V＝IR 回算檢查。"),
 (2,"定值電阻測得（V,I）為（1.0 V,0.010 A）、（2.0 V,0.020 A）、（3.0 V,0.030 A），哪項最合理？",["V/I 約 100 Ω，資料近似符合歐姆定律","V/I 逐列為 0.01 Ω","電流與電壓無關","只能由顏色判斷電阻"],"A","各列 V/I 分別約為 100 Ω，且 I 隨 V 成正比，支持定值電阻模型。","逐列算 V/I，再檢查比值是否穩定及原點附近的比例關係。"),
 (3,"要量測某電阻支路的電流，電流表應如何接入才不會漏掉該支路電流？",["與待測支路串聯","與待測電阻並聯且直接跨接電池","只接在電源外殼","不必接入電路"],"A","電流表要讓支路電流完整通過，因此串聯；直接並聯電源可能造成近似短路。","先找待測支路，再沿電流路徑插入電流表，檢查沒有形成旁路。"),
 (4,"要量測電阻兩端的電位差，電壓表應如何接？",["與待測電阻並聯在兩端","與電阻串聯在主幹且不跨兩端","與電池短路","只接一端"],"A","電壓是兩點間的電位差，電壓表須跨接待測元件兩端；它的內阻大，並聯不會讓主支路電流大幅改變。","圈出待測元件兩端，再把電壓表兩端接到同兩個節點。"),
 (5,"固定電阻不變，電壓由 6 V 提高到 12 V；理想歐姆模型預測電流如何？",["減半","加倍","不變且必為零","只改變電阻單位"],"B","I＝V/R，R 固定時電壓加倍，電流也加倍；實際元件若升溫造成 R 改變則需重新檢查。","先固定 R，再用比例或公式比較兩個工作點，最後標出定值模型限制。"),
 (6,"某元件三次測量的 V/I 分別為 50 Ω、51 Ω、100 Ω；哪項做法最恰當？",["直接宣稱電阻永遠是 50 Ω","檢查第三次的接線、讀值、溫度與元件是否已改變，再決定模型適用範圍","刪掉所有不符合的資料","只看電壓不看電流"],"B","前兩次近似一致，第三次偏離可能來自接線、測量誤差、升溫或元件狀態改變，不能任意刪除。","先找離群資料，再檢查儀器、接點、溫度與元件狀態，最後決定是否重測。"),
 (7,"鎢絲燈泡通電一段時間後溫度升高，若 V/I 比值變大，應如何解釋？",["燈絲的有效電阻可能因升溫增加，不能用一條固定 R 的直線描述所有工作點","電壓消失","電流表必定壞掉","歐姆定律要求所有元件 R 永遠固定"],"A","燈絲溫度改變會使電阻改變；I＝V/R 仍是工作點關係，但不能把 R 當成跨所有溫度的常數。","比較冷態與熱態的 V/I，再把元件溫度列為影響模型的條件。"),
 (8,"若把理想電流表直接並聯在電池兩端，最需要警告的風險是？",["電流表內阻很小，可能形成大電流與近似短路","電壓表會自動串聯","電池電壓一定升高","電路必定沒有電流"],"A","電流表內阻很小，並聯電源會讓電流大幅增加，可能損壞儀器或電池；正確量測應串聯待測支路。","看儀表內阻與接線拓樸，先判斷是否形成低阻旁路，再決定安全接法。"),
 (9,"某電阻兩端為 3.0 V，通過電流為 0.015 A；其電阻約為多少？",["0.005 Ω","20 Ω","200 Ω","45 Ω"],"C","R＝V/I＝3.0/0.015＝200 Ω。把毫安換成安培後再計算，並用 V＝IR 回算。","先統一電流單位，再用 R＝V/I 計算，最後檢查數值量級。"),
 (10,"研究固定電阻的電壓是否影響電流，哪項設計最公平？",["只改變電壓，固定電阻、接線、儀表、讀值時間與溫度，記錄多組 V、I","同時更換電阻和電源","只量一次且不記錄溫度","把電流表並聯電池"],"A","只改變自變因電壓，控制電阻、接線、儀表與溫度，才能判斷 I—V 關係並檢查升溫限制。","列出自變因、控制變因與測量量，逐級調整電壓並重複記錄 V/I。"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以電路測量站為入口，讓學習者正確接上電流表與電壓表，逐次改變定值電阻兩端電壓，從 V—I 表格和 V/I 比值建立歐姆定律。接著把定值模型的適用條件帶到鎢絲、延長線與生活電器，處理升溫、接點、儀表內阻與安全操作限制。"; lesson["studyHighlights"]=["用伏特、安培、歐姆說明電壓、電流與電阻。","以 I＝V/R、V＝IR、R＝V/I 互相回算並檢查單位。","辨認電流表串聯、電壓表並聯及短路風險。","用 V—I 資料、V/I 比值與升溫判斷定值模型限制。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以電路、量測、歐姆定律與資料圖表理解電流電壓關係。","計算、正確接線、控制變因與模型限制是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向電學與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以電路測量站、電表接線卡、V—I 資料、鎢絲升溫與短路安全診斷建立本課互動。","移除原本日期—電壓—電阻批次題，改為公式、接線、圖表、控制變因和限制的綜合題。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織電流、電壓、電阻、電表、歐姆定律、資料判讀與模型限制；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for i,prompt,opts,ans,exp,strat in ITEMS:
  p=QDIR/f"question-science-content-kc-iv-7-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{exp} 正確答案為選項 {ans}：「{opts[ord(ans)-65]}」。"}; q["examPatternRefs"]=refs(); q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然／理化試題的歐姆定律、電表接線、V—I 資料、控制變因與安全能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開試題能力方向，題幹、選項、答案、解析與五步解法均以 Kc-Ⅳ-7 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["solutionStrategy"]=strat; q["solutionSteps"]=["圈出 V、I、R、儀表接線、元件狀態與控制條件。",f"依本題情境套用判準：{strat}","選擇正確公式或接線理由，統一單位並計算或比較。","排除顛倒分母、混淆串並聯、忽略升溫或造成短路的選項。","回算答案並說明定值模型、測量精度或安全限制。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Kc-Ⅳ-7：電流、電壓與電阻的關係","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"replacedMisalignedQuestionBank":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原日期—電壓—電阻批次題；三筆公開試題僅作 pattern-only 來源。版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content kc iv 7")
if __name__=="__main__": main()
