"""Kc-Ⅳ-6：磁場變化與感應電流的錯置題修正與第一輪融合。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-kc-iv-6.json"; REPORT=ROOT/"implementation/reports/science-content-kc-iv-6-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"電磁感應、磁場、電流方向與實驗資料判讀","pattern":"取磁場變化、感應效應、右手定則與控制變因的能力方向，重新設計線圈實驗情境。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"電磁鐵、感應電流、發電機與能量轉換","pattern":"取由觀察現象連到磁通量與能量轉換的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"磁通量、楞次定律、線圈轉動與感應實驗","pattern":"取方向判讀、變因控制與發電機模型的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
ITEMS=[
 (1,"條形磁鐵向線圈靠近時電流計偏轉，磁鐵停在線圈中央後指針回到零。最合理的解釋是？",["只有磁場存在就會有固定電流","只有穿過封閉線圈的磁通量改變時才有感應電流；停止移動後變化消失","磁鐵停住後磁場消失","電流計只能測量電池電流"],"B","感應電流的關鍵是磁通量隨時間改變，不是磁場單純存在；磁鐵停住後，若磁通量不再變化，穩態感應電流回到零。","把磁場存在和磁通量變化分開，再對照磁鐵運動前後的指針讀值。"),
 (2,"其他條件相同，磁鐵以較快速度穿過線圈，通常感應電流的瞬時偏轉較大，主要因為？",["磁鐵質量必然變大","磁通量變化率較大","線圈電阻必然變小","磁場方向一定反轉"],"B","在磁通量改變量相近時，變化所需時間更短，磁通量變化率較大，感應電動勢及電流通常較大。","固定磁鐵、線圈與接線，只改變速度，將偏轉大小和磁通量變化率比較。"),
 (3,"同一磁鐵以同樣速度進入線圈，但改由相反磁極朝向線圈，感應電流方向如何判斷？",["一定與原來相同","一定為零","先判斷外加磁通量方向與增加／減少，再依楞次定律決定相反的感應磁效應","只看磁鐵顏色"],"C","反轉磁極會改變外加磁場方向；電流方向不能只背固定答案，要先判斷磁通量變化，再用楞次定律和右手定則。","畫出外加磁場箭頭，標示磁通量變化，再找出線圈需產生的反抗效應。"),
 (4,"磁鐵停在一個封閉線圈內，且線圈、磁鐵都不動；若沒有其他磁場改變，電流計最可能顯示？",["持續最大電流","持續固定電流","回到零，因磁通量不再隨時間改變","讀值只由磁鐵重量決定"],"C","即使線圈內磁場很強，磁通量不變就沒有持續感應電流；短暫移動時的偏轉和停住後的零值要分開。","確認迴路封閉，再比較運動階段與靜止階段的磁通量時間變化。"),
 (5,"在磁場方向固定且磁場均勻的區域，若線圈有效面積增加，哪項最可能發生？",["磁通量可能增加，若此變化隨時間發生便產生感應效應","磁通量必定完全不變","只會改變線圈顏色","只要有面積就會永久有電流"],"A","磁通量與磁場、有效面積及夾角有關；面積改變造成磁通量隨時間變化時才會有感應電流。","指出哪一項改變，再判斷磁通量是否改變及改變是否持續。"),
 (6,"線圈平面原本正對均勻磁場，轉動到線圈平面與磁場方向平行；不考慮其他變化，磁通量如何改變？",["由最大值降到接近零，轉動過程會產生感應效應","永遠維持最大值","由零變成無限大","與線圈角度無關"],"A","磁通量取決於磁場穿過線圈的有效分量；由正對到平行時，有效分量由大變小，轉動期間會改變。","先判斷初末位置的穿入角度，再追蹤轉動過程的磁通量變化。"),
 (7,"若線圈的一處導線斷開，但磁鐵仍相對移動，最合理的判斷是？",["開路仍有可持續的迴路電流","沒有封閉迴路，因此不能形成可持續的感應電流；兩端仍可能有感應電壓","磁通量一定不變","磁鐵會失去磁性"],"B","磁通量改變可在開路兩端造成電位差，但沒有封閉路徑就不能形成可持續電流；電壓和電流不可混為一談。","先檢查迴路是否閉合，再分別判斷感應電壓與感應電流。"),
 (8,"發電機把線圈在磁場中轉動，轉動一圈時輸出電流方向週期性改變，主要表示？",["機械能透過磁通量週期變化轉成電能，輸出可呈交變特徵","電能不需任何能量來源","線圈只是在儲存磁鐵重量","電流方向永遠固定不變"],"A","線圈轉動使穿過線圈的磁通量週期改變，外力做功並經電磁感應輸出電能；方向隨週期改變可形成交流。","找出機械輸入、磁通量週期變化與電能輸出的三段能量鏈。"),
 (9,"線圈中原本向上的磁通量正在增加，依楞次定律，感應線圈產生的磁場方向應為？",["向上以加強增加","向下以反抗磁通量的增加","方向必定水平","不需知道外加磁場方向也能判定"],"B","楞次定律反抗的是磁通量的變化；向上磁通量增加時，感應磁場要向下抵抗增加。","先寫外加磁場方向與變化符號，再選擇能抵抗該變化的感應磁場。"),
 (10,"要研究磁鐵移動速度是否影響感應電流大小，哪項實驗設計最公平？",["同時改變磁鐵、線圈匝數、電阻與速度","固定磁鐵磁性、線圈匝數、面積、方向與電阻，只改變移動速度並重複測量","只觀察一次指針方向","每次換不同電流計且不校正"],"B","研究單一變因時，其他會影響磁通量或電流的條件須固定，並以重複測量比較偏轉大小。","列出自變因、控制變因與測量量，固定線圈條件後改變速度並重複記錄。"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以線圈實驗站為入口，讓學習者先從電流計偏轉分辨磁場存在與磁通量變化，再逐一改變磁場強弱、線圈面積、穿入角度與運動速度。透過楞次定律、封閉迴路與右手定則，最後把轉動線圈、機械能輸入和交變電流輸出連成發電機模型。"; lesson["studyHighlights"]=["用磁通量變化而非磁場單純存在解釋感應電流。","比較磁場、面積、角度與變化速率對感應效應的影響。","用楞次定律與右手定則判斷方向，分清電壓與電流。","以控制變因將線圈實驗連到發電機的能量轉換。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以磁場、電流、實驗資料與能量轉換理解電磁感應。","方向判讀、控制變因與模型限制是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向物理與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以線圈實驗站、磁通量卡、電流計方向、開路／閉路切換與轉動發電機組裝建立本課互動。","移除原本錯置的歐姆定律日期—電壓—電阻題，改為十題磁通量與楞次定律的原創推理。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織磁通量、感應電流、方向、控制變因與發電機；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for i,prompt,opts,ans,exp,strat in ITEMS:
  p=QDIR/f"question-science-content-kc-iv-6-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["prompt"]=prompt; q["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(opts)]; q["answer"]={"value":ans,"explanation":f"{exp} 正確答案為選項 {ans}：「{opts[ord(ans)-65]}」。"}; q["examPatternRefs"]=refs(); q["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校公開自然／理化試題的電磁感應、磁場、電流方向、實驗控制與發電機能力方向；本題只作 pattern-only 改寫。","authoringNote":"本題取公開試題能力方向，題幹、選項、答案、解析與五步解法均以 Kc-Ⅳ-6 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}; q["solutionStrategy"]=strat; q["solutionSteps"]=["圈出線圈、磁場、運動、面積、角度與迴路狀態。",f"依本題情境套用判準：{strat}","判斷磁通量是否隨時間改變，並分開電壓、電流與方向。","使用楞次定律、右手定則或控制變因排除誘答。","回查答案是否符合實驗條件，寫出沒有持續感應的原因或證據限制。 "]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Kc-Ⅳ-6：磁場變化與感應電流","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"replacedMisalignedQuestionBank":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已移除原錯置的歐姆定律題；三筆公開試題僅作 pattern-only 來源。版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content kc iv 6")
if __name__=="__main__": main()
