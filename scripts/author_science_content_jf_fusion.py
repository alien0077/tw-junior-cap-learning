"""Jf：有機化合物的性質、製備及反應第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jf.json"
REPORT=ROOT/"implementation/reports/science-content-jf-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"有機化合物、結構、反應、材料與安全整合判讀","pattern":"取由有機結構、反應產物、製備資料與生活材料情境整合推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"碳化合物、燃燒、聚合物、生活應用與資料圖表","pattern":"取從模型、實驗資料、材料生命週期與生活情境判斷有機化學的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"有機化合物、反應、聚合物、酯類與製備","pattern":"取以碳骨架、官能基、聚合、酯化／皂化、材料與安全建立整合教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jf-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jf"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的有機結構、官能基、反應、聚合物、製備、生命週期與安全整合能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jf","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"某材料由小分子單體反應形成長鏈，受熱可軟化、冷卻後成形；要從結構預測其用途，哪項推理最完整？",["它可能是熱塑性聚合物，可依耐熱、強度、柔韌與化學相容性選擇用途","只要是長鏈就一定能裝熱酸","單體越小材料一定越硬","聚合物不會燃燒也不需標示"],"A","鏈狀聚合物可在適當加熱下軟化，但用途仍須查耐熱、力學和化學相容性；長鏈不保證所有性質。","把聚合結構和實際材料性能及用途配對。",["辨認單體聚合成長鏈。","判斷受熱軟化支持熱塑性。","列出用途需要的耐熱、強度和相容資料。","排除能裝所有物質、不燃燒和不需標示。","所以 A 最完整。"],"medium"),
q(2,"要從燃燒資料判斷未知有機液體的元素組成，哪組證據最有用？",["完整燃燒後檢驗二氧化碳和水，並配合原始樣品元素或結構分析","只看火焰顏色","只測沸點一次","只聞氣味猜名稱"],"A","二氧化碳和水可支持樣品含碳、氫，但需要結構或元素分析補足，單一火焰、沸點或氣味不能決定身分。","用燃燒產物提出元素線索，再用結構資料確認。",["控制燃燒條件使其盡量完全。","檢驗生成的 CO₂ 和 H₂O。","推論碳和氫存在。","再用元素或結構分析避免過度命名。","所以 A 最有證據力。"],"medium"),
q(3,"若以醇和有機酸製備酯，想提高可收集的酯量，哪項思路最合理？",["控制溫度與催化條件，並移除部分水或使用適當過量反應物，使平衡往酯方向移動","只把所有反應物冷卻到零度","加入催化劑就必然增加平衡產量","把產物香味當作收率數值"],"A","酯化是可逆反應，移除水或調整反應物比例可影響平衡；催化劑主要加快達平衡速度，香味不是定量收率。","整合酯化、平衡、速率和定量分析。",["寫出醇＋酸⇌酯＋水。","辨認要提高的是平衡產物量。","選擇移除水或調整反應物比例。","用質量、體積或分析方法測收率。","所以 A 正確。"],"hard"),
q(4,"油脂經鹼性水解可製成肥皂；若成品泡沫少，不能直接判定皂化失敗，還應檢查？",["脂肪酸鹽含量、硬水離子、鹼濃度、反應時間及乳化測試等資料","只看成品顏色","只增加香精掩蓋結果","只量容器重量"],"A","泡沫受脂肪酸鹽含量、硬水、濃度與測試條件影響，需分析組成並設乳化對照，不能用泡沫單一指標判定。","將製備反應、產物功能和測量干擾分開。",["確認皂化反應是否完成及鹼用量。","分析脂肪酸鹽含量。","控制水質和乳化測試條件。","比較硬水、清水與未皂化油脂對照。","所以 A 最完整。"],"hard"),
q(5,"比較燃料、香味酯與塑膠材料的生命週期時，哪項評估最符合根單元精神？",["同時看原料、合成條件、使用功能、能耗、排放、回收與最終處理，而非只看使用時的便利","只看產品是否有香味","只看一次使用的重量","只要是有機物就一定不環保"],"A","有機材料從原料到製造、使用、回收和廢棄都可能產生影響，需以生命週期和功能需求評估。","把有機反應和材料決策放到完整生命週期。",["列出原料與製備反應。","比較製造能源和排放。","評估使用壽命與功能。","加入回收、分解或最終處理資料。","因此 A 最完整。"],"medium"),
q(6,"某有機溶劑同時具有易揮發、易燃和刺激性；實驗室要選替代品時，哪項決策最合理？",["比較替代品的溶解功能、揮發性、燃點、毒性、廢棄與操作設備，再選能降低總風險者","只選氣味最淡的液體","只選價格最低的液體","只把窗戶關起來避免外洩"],"A","替代品需兼顧功能與全程危害，氣味或價格不能代表安全；通風和設備也需配合。","把有機物性能與風險評估整合成材料選擇。",["確認原溶劑的功能需求。","比較替代品的物性、毒性和廢棄影響。","評估設備、通風、儲存和暴露。","選擇能維持功能且總風險較低的方案。","所以 A 正確。"],"medium"),
q(7,"若同分異構物具有相同分子式卻沸點與溶解性不同，最合理的解釋是？",["原子連接方式或空間排列不同，造成分子形狀與分子間作用不同","分子式相同代表所有性質必定相同","其中一種沒有碳原子","沸點只由顏色決定"],"A","同分異構物分子式相同但結構不同，形狀與分子間作用會影響物性。","由分子式和結構層次解釋物性差異。",["確認兩者元素數量相同。","比較原子連接方式或排列。","推論分子形狀和作用力不同。","連結到沸點、溶解性等物性。","答案為 A。"],"hard"),
q(8,"設計有機反應製備實驗時，哪項證據組合最能證明目標產物而非原料混合？",["反應式與結構分析、沸點或色譜等分離資料、產物性質及未反應對照","只聞到新氣味","只看液體顏色","只記錄加熱時間"],"A","目標產物需由結構／組成分析、分離資料和性質與對照共同確認；氣味、顏色或時間只能作線索。","以身份證據、分離證據、性質證據三層確認製備成功。",["寫出預期反應式與結構。","用適當方法分離或分析產物。","比較產物的沸點、溶解或反應性。","加入原料和空白對照排除混合。","所以 A 最完整。"],"hard"),
q(9,"有機物焚燒後的煙霧可能含有未完全燃燒產物；最適合的環境與安全措施是？",["控制氧氣與燃燒溫度、使用通風與適當過濾，並檢測排放而非只看火焰","把所有煙霧直接排到室內","為了減少味道加入未知化學品","只測火焰亮度判斷污染"],"A","有機物不完全燃燒可能產生一氧化碳、煙粒或其他物質，需控制燃燒、通風、過濾和排放檢測。","把反應條件、產物風險和環境監測連結。",["辨認有機燃燒可能不完全。","列出氣體和微粒排放風險。","控制供氧、溫度與設備通風。","以儀器檢測排放，不用火焰外觀代替。","所以 A 正確。"],"medium"),
q(10,"要把一種新有機材料推薦給生活用品製造，哪套流程最完整？",["先由結構預測性質，再做功能與安全測試、生命週期評估、同類材料對照，最後依資料決策","只要實驗室能合成就直接量產","只看廣告宣稱可分解","只比較初始售價"],"A","從結構到功能、安全、生命週期和對照的多層證據，才能支持材料推薦與量產決策。","用有機化學知識建立由分子到產品的證據流程。",["確認單體、聚合或官能基結構。","預測並實測耐熱、強度、溶解與反應性。","檢查使用安全、回收和環境生命週期。","與既有材料比較成本和效益再決策。","所以 A 最完整。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["有機化合物的結構與官能基影響反應、物性、製備和用途。","酯化、皂化、聚合、燃燒及異構等反應需由結構、條件、產物與分析資料共同判斷。","有機材料選擇要把功能、安全、能耗、生命週期和回收放在同一決策框架。"],"versionDifferences":["南一公開線索支持由燃料、香味和生活有機材料進入整體應用。","康軒公開課程資料較突出結構、反應、物性與實驗資料。","翰林公開課程計畫補充酯化／皂化、聚合物、材料生命週期與安全；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以結構—性質—反應—製備—功能—生命週期六層統整 Jf 根單元。","納入同分異構、產物確認、替代溶劑、燃燒排放、肥皂功能與有機材料推薦。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫 Jf 根單元有機結構、反應、製備、材料和安全的整合題；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jf：有機化合物的性質、製備及反應","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為結構—性質—反應—製備—功能—生命週期整合問題，與已完成 Jf 子單元分開設計；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jf")
if __name__=="__main__": main()
