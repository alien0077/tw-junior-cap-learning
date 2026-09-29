"""Kc-Ⅳ-8：電阻發熱與能量逸散的題庫重寫與第一輪融合。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-kc-iv-8.json"; REPORT=ROOT/"implementation/reports/science-content-kc-iv-8-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"電阻發熱、功率、能量、額定值與用電安全","pattern":"取功率—能量—時間、焦耳熱與安全判讀能力方向，重新設計低電壓電熱實驗。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"電功率、電熱器、負載與電路安全","pattern":"取公式條件、額定資料、散熱與過載的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"焦耳熱、電器功率、使用時間與能源逸散","pattern":"取數值計算、裝置比較與安全限制的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
ITEMS=[
 (1,"低電壓電熱片兩端 12 V、通過 3 A 電流；輸入功率是多少？",["4 W","9 W","36 W","144 W"],"C","P＝VI＝12×3＝36 W，代表每秒約轉換 36 J 的能量。","先圈 V 和 I，使用 P＝VI，再把瓦特解讀成每秒能量轉換。"),
 (2,"某電熱器功率 100 W，連續運轉 60 s；理想輸入電能是多少？",["60 J","600 J","6,000 J","60,000 J"],"C","E＝Pt＝100×60＝6,000 J；功率是每秒量，總能量還要乘時間。","確認功率與時間單位，再用 E＝Pt 並檢查焦耳量級。"),
 (3,"在電流固定且時間相同時，電阻由 2 Ω 增至 4 Ω；依 Q＝I²Rt，焦耳熱如何變化？",["減半","加倍","不變","變成零"],"B","I 和 t 固定時 Q 與 R 成正比，電阻加倍，焦耳熱加倍；若改成固定電壓，條件就不同。","先確認固定的是電流還是電壓，再把公式中的變因逐一比較。"),
 (4,"在電壓固定的定值電阻中，電阻增大時輸入功率 P＝V²/R 通常如何？",["增加","減少","必定不變","只改變時間單位"],"B","固定 V 時 P＝V²/R，R 增加會使功率減少；不能直接套用固定電流下的 Q 比較。","辨認控制條件後選擇 P＝VI 或 P＝V²/R，避免把不同情境混用。"),
 (5,"電熱器額定 110 V、550 W，在額定條件下工作時額定電流約為多少？",["0.2 A","2 A","5 A","60,500 A"],"C","I＝P/V＝550/110＝5 A。額定值描述指定電壓下正常工作的基準。","先從銘牌找 P、V，使用 I＝P/V，並用 P＝VI 回算。"),
 (6,"延長線同時接上總功率很大的多個電器，插頭或接點局部變熱；最合理的安全判斷是？",["只要電器能運轉就一定安全","總負載、接點電阻與散熱都要檢查，必要時降低負載並停止使用異常發熱設備","把延長線包起來保溫","增加串聯電阻讓插頭更熱"],"B","過載會提高電流，接點的局部電阻可能把能量集中轉成熱；額定電流、接觸品質與散熱都關係安全。","先辨認設計用途和熱源，再比較總負載、額定值、接點與散熱條件。"),
 (7,"甲電器 800 W 用 5 min，乙電器 400 W 用 20 min；哪項正確？",["甲耗能一定較少","乙耗能較多，因為 E＝Pt：甲 240 kJ、乙 480 kJ","兩者能量相同","只能由功率大小判斷總能量"],"B","甲 E＝800×300＝240,000 J；乙 E＝400×1,200＝480,000 J，乙雖功率較小但使用較久。","把分鐘換成秒，分別算 E＝Pt，再比較功率和時間的共同作用。"),
 (8,"同一支路電流固定，某鬆動接點的接觸電阻比正常接點大；為何它可能局部發熱？",["Q＝I²Rt 顯示相同電流下接觸電阻大會產生較多熱","接點電阻越大越不會有能量轉換","所有熱都只在電熱器產生","因為電壓表會自動加熱接點"],"A","固定 I 與 t 時，Q＝I²Rt；鬆動接點的 R 大，熱可能集中在小區域，造成安全警訊。","把接點視為支路中的電阻，固定電流後比較 R、Q 與散熱位置。"),
 (9,"用電熱裝置比較兩種材料的發熱量，若要使用 Q＝I²Rt，哪項必須寫清楚？",["電流是否固定、電阻、通電時間與熱量測量方法","只記錄材料顏色","只看額定電壓不量電流","把時間省略"],"A","焦耳熱公式有條件；需交代 I、R、t 及測量方法，才能公平比較材料或裝置。","列出自變因、控制變因、測量量與散熱條件，再決定公式適用範圍。"),
 (10,"低電壓模擬電熱站要避免能量逸散與危險，哪項設計最完整？",["使用額定範圍內的電源，限制總負載、保持通風並監測接點溫度","把所有導線纏在一起以提高溫度","移除保護元件並提高電壓","只看裝置是否亮起"],"A","安全設計要同時控制電壓、電流、總負載、散熱與接點狀態，不能以『能運轉』代替額定與熱安全判斷。","先確認額定值和負載，再檢查散熱、接點與保護措施，最後用溫度資料回饋。"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以低電壓電熱實驗站的延長線、電熱片、接點與散熱模型為入口，建立 P＝VI、E＝Pt 與 Q＝I²Rt 的條件化能量帳本。學習者要比較固定電流與固定電壓時的電阻發熱，讀取額定電壓／功率，並把總負載、接觸電阻、通風與局部過熱連到用電安全。"; lesson["studyHighlights"]=["用 P＝VI、E＝Pt 與 Q＝I²Rt 分析功率、總能量和焦耳熱。","分清設計來發熱的元件與不應局部升溫的導線接點。","比較固定電流、固定電壓與額定值的不同公式條件。","以總負載、散熱、接觸電阻與時間評估用電安全。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以電阻、功率、能量、焦耳熱與生活安全理解電熱。","公式條件、額定值、時間、散熱與過載是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向電學與生活安全數位資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以低電壓電熱站、延長線接點、額定銘牌、固定電流／電壓切換與散熱監測建立本課互動。","移除原本日期—電壓—電阻批次題，改為公式條件、能源比較與安全決策題。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織電阻發熱、功率、能量、額定值、散熱與過載安全；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for i,prompt,opts,ans,exp,strat in ITEMS:
  p=QDIR/f"question-science-content-kc-iv-8-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{exp} 正確答案為選項 {ans}：「{opts[ord(ans)-65]}」。"}; q["examPatternRefs"]=refs(); q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然／理化試題的電阻發熱、功率、能量、額定值、焦耳熱與用電安全能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開試題能力方向，題幹、選項、答案、解析與五步解法均以 Kc-Ⅳ-8 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["solutionStrategy"]=strat; q["solutionSteps"]=["圈出 V、I、R、P、E、Q、t、額定值與散熱條件。",f"依本題情境套用判準：{strat}","選擇符合固定條件的公式，統一單位並計算或比較。","排除混用固定電壓／電流、忽略時間、過載或把正常加熱當安全的選項。","回查答案與額定值、能量去向及安全限制是否一致。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Kc-Ⅳ-8：電阻發熱與能量逸散","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"replacedMisalignedQuestionBank":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原日期—電壓—電阻批次題；三筆公開試題僅作 pattern-only 來源。版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content kc iv 8")
if __name__=="__main__": main()
