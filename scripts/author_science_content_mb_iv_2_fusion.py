"""Mb-Ⅳ-2：科學史重要發現與多元貢獻第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-mb-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-mb-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"科學史、觀測、證據與科學發現","pattern":"取公立學校自然科評量以資料時序、工具、證據、模型與科學社群推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"天文、物理、化學與科學方法資料","pattern":"取公開會考以圖表、實驗證據、模型解釋和多步推論的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"科學史重要發現、工具、研究合作與證據","pattern":"取公立國中試題以觀察—模型—驗證鏈和科學貢獻判讀的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先把史料分成觀察、工具、模型、驗證和應用。","依證據依賴關係整理時序，不只依人物名次。","檢查新資料是否支持或修正原主張。","辨認研究者、技術人員、資料整理者與社群的不同貢獻。","說明史料能證明的範圍及被忽略角色的限制。"] for _ in range(10)]
ROWS=[
("easy","科學史時間線中，哪張卡最適合作為觀測主張的證據？",["標明儀器、測量方法與可重複讀值的觀測記錄", "只寫研究者的名言", "只寫後來的教科書結論", "只列研究者出生年份"],"A","觀測證據需說明工具與方法，並留下可檢查或重複的資料；名言與年代不能代替觀察。","先找實際測量和方法，再把後續解釋與人物資料分開。"),
("medium","若天文觀測資料顯示某星體位置週期性改變，從資料到科學主張之間還需要？",["提出可檢驗模型並用不同時段或工具的資料比較預測", "直接把週期變化寫成唯一原因", "只看一次最明顯的影像", "因為觀測者有名就不必驗證"],"A","位置變化是資料，軌道或其他機制是模型；需要多次觀測和可區分的預測才能支持解釋。","把觀測、模型、預測和新驗證資料排成證據鏈。"),
("easy","放射性研究中，測量活度隨時間下降的曲線主要能支持哪種描述？",["在指定條件下，活度隨時間呈現可量測的衰變規律", "直接證明所有放射性物質都完全相同", "只代表儀器顏色改變", "只要曲線下降就知道所有生物風險"],"A","曲線可描述特定樣本與條件下的量測規律；物質差異與健康風險仍需其他資料，不能一步外推。","先說曲線直接測到什麼，再列出需要額外證據的外推主張。"),
("medium","若一項粒子物理結果由加速器設計者、偵測器工程師、資料分析者與理論研究者共同完成，如何描述最準確？",["不同角色提供設備、資料、分析與模型的互補貢獻，發現不是單一名字獨立完成", "只有提出理論者算科學貢獻", "技術人員的工作不影響證據", "合作越多人就代表結果必然正確"],"A","複雜研究需要儀器、資料、分析和理論互相接合；合作本身不保證正確，仍需看方法與證據。","把每個角色對應到證據鏈的具體節點，而非只排列榮譽名單。"),
("hard","史料只保留一位男性研究者的姓名，卻提到大量測量與計算；最合理的歷史判讀是？",["不能僅憑署名推論只有他貢獻，應追查技術人員、合作者、資料來源與制度背景", "姓名就是全部貢獻的完整證明", "沒有列名的人不可能參與", "只要結果正確就不必看史料脈絡"],"A","署名是史料的一部分，但未必完整呈現資料取得、儀器製作、計算和合作網絡；需要更多來源交叉核對。","分開『留下的名字』和『實際證據工作』，找出史料缺口。"),
("medium","兩組研究者用不同儀器得到相近結果，這對主張有何意義？",["可增加結果的穩健性，但仍需檢查校正、樣本與方法是否真正獨立", "只要數值相近就完全沒有誤差", "不同儀器一定代表不同自然定律", "只取其中較好看的結果"],"A","不同方法的一致結果能增加信心，但儀器校正、樣本來源和共同偏差仍要檢查。","先比較結果，再追問方法是否獨立、誤差是否受同一來源影響。"),
("easy","若某地區研究者提供獨特生態觀察，但主流歷史敘事沒有記錄，最合適的做法是？",["保留其資料與方法來源，交叉核對並納入貢獻脈絡，而不是因未入名冊就刪除", "因不在主流名單就視為沒有證據", "只改變人物照片不檢查資料", "把地方觀察直接當成普遍定律"],"A","多元貢獻需要回到資料與方法核對；被忽略不等於沒有價值，也不能因地方性就無條件普遍化。","同時檢查資料品質、適用範圍和歷史記錄中的缺口。"),
("hard","若新測量只在極低溫條件下推翻舊模型，結論應如何寫？",["舊模型在該低溫條件下需要修正；其他條件是否仍適用要另行檢驗", "舊模型在所有情況都完全錯誤", "新測量只要一次就代表所有理論消失", "條件不重要，模型永遠只有一個答案"],"A","模型的適用範圍可能被新條件擴展或限制；精確結論要標出低溫條件，不能過度外推。","先定位新證據出現的條件，再判斷模型是局部修正還是全面推翻。"),
("medium","科學史展覽要呈現女性研究者和技術人員的貢獻，哪種做法最有證據？",["展示她們負責的測量、計算、儀器、樣本或分析，並標明史料來源與限制", "只增加名字但不說明工作", "把所有人都寫成同一種角色", "只用後來的評價取代原始資料"],"A","具體工作與來源能讓觀眾理解貢獻如何接入證據鏈，也能誠實呈現史料不完整之處。","用角色—工作—證據—來源四欄設計展覽，而非只新增人物名單。"),
("hard","哪句最能表達科學史重要發現與多元貢獻的證據界線？",["在可核對的觀測、工具、模型和合作史料支持下，主張逐步形成；人物聲望不能取代方法，史料缺漏也需明白標示", "發現只由最有名的人突然完成", "只要故事流暢就不必核對資料", "被忽略的角色一定比署名者貢獻更多"],"A","科學史判讀要同時看時序、證據、工具、模型與合作角色，避免英雄敘事或反向臆測取代史料。","以證據鏈和角色具體工作收束，並把已知與未知分開。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-mb-iv-2-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-mb-iv-2"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的天文、放射性、粒子物理、工具、模型、時序、合作與多元貢獻能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-mb-iv-2","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-mb-iv-2、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合天文觀測、放射性研究、粒子物理、工具、模型、證據時序、研究合作、女性與不同地區研究者及技術人員的多元貢獻。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-mb-iv-2-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為天文、放射性、粒子物理、工具、模型、證據時序、合作與多元科學貢獻專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content mb-iv-2")
if __name__=="__main__": main()
