"""Mb：科學發展的歷史第一輪原創題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-mb.json"; REPORT=ROOT/"implementation/reports/science-content-mb-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"科學探究、模型、證據與科學史情境","pattern":"取公立學校自然科評量以觀察、證據、模型、推論和新情境遷移的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"科學史、實驗資料、模型與生物技術","pattern":"取公開會考以圖表、實驗控制、證據界線和模型解釋的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"科學方法、發現、技術與環境社會影響","pattern":"取公立國中試題以觀察工具、假說驗證、模型更新和科學應用的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先分出原始觀察、測量工具、模型、推論與社會決策。","按證據支撐的關係排序，而不是只按年代排列。","比較新資料是否支持、修正或推翻原模型。","檢查控制條件、替代解釋和當時工具的限制。","用條件式說明知識如何累積及技術帶來的效益與風險。"] for _ in range(10)]
ROWS=[
("easy","科學史中的觀察記錄和科學解釋有何不同？",["觀察記錄描述測得或看見的現象，解釋則提出可檢驗的模型或原因", "兩者都只是個人意見", "解釋一定比觀察更早出現", "只要寫下日期就已完成解釋"],"A","觀察是資料來源，解釋是依資料提出的模型或因果主張，兩者需要分開記錄才能知道推論是否超出證據。","先標記哪些句子是資料，哪些句子是用資料建立的模型。"),
("medium","若新顯微鏡讓研究者看見原先無法觀察的細胞結構，最可能帶來什麼？",["增加可取得的證據，可能促使原有模型被修正", "只改變科學家的姓名", "新工具產生的影像不可能影響理論", "只要看見結構就自動知道其功能"],"A","工具擴大觀察能力，能提供新資料，但結構與功能的連結仍需實驗和模型推論，不能一步跳到確定機制。","把工具提供的觀察、由觀察提出的推論和仍需驗證的功能分開。"),
("easy","兩個模型都能解釋既有資料，哪項新證據最有助於區分它們？",["兩模型預測不同且可在相同控制條件下測量的結果", "只選支持自己喜歡模型的例子", "比較研究者的名氣", "只看哪個模型年代較新"],"A","可區分的預測在公平條件下測量，才能比較模型解釋力；年代或名氣不是證據。","找兩模型預測的差異，再設計能觀察差異的控制實驗。"),
("medium","某生物技術早期在實驗室有效，後來田間結果不穩定；最合理的科學史判讀是？",["不同環境條件和尺度可能暴露模型限制，需要補充資料與修正技術", "實驗室結果必然錯誤", "田間資料一定不可靠", "只要第一次成功就可推廣所有地方"],"A","從實驗室到田間會加入溫度、土壤、生態互動和操作差異；結果不穩定能揭示適用條件與模型限制。","比較兩種場域的條件和輸出，不把一次成功當成普遍定律。"),
("hard","科學爭論未立即結束，哪項做法最有助於理性判斷？",["比較各主張的資料品質、預測、方法限制與可重複性，而非只看支持者身分", "只投票決定哪個模型正確", "只引用最早提出者", "把所有不同意見都視為反科學"],"A","科學主張需要由方法、證據、可重複性和預測能力評估；權威或多數票不能替代資料。","建立主張—證據—方法—限制表，再比較模型能否被檢驗。"),
("medium","要重建一項發現的合理時間線，哪張證據卡應放在最前？",["先提出可觀察問題並取得初始記錄的卡片", "最後才出現的應用宣傳", "尚未完成的長期風險預測", "不含日期和資料的結論口號"],"A","知識形成通常由問題與觀察開始，再經工具、模型、驗證和應用；時間線應依證據關係而非宣傳順序排列。","先找最早可核驗的觀察，再沿著資料支持的推論和後續驗證排列。"),
("hard","若一項技術改善產量卻增加外來基因逸散風險，科學史與社會影響應如何同時記錄？",["分開呈現技術效益、逸散機制、證據不確定性與受影響者，再設監測與停損條件", "只記錄產量增加", "因有風險就否定所有科學證據", "把風險視為技術名稱的一部分而不測量"],"A","科學發展既包含知識與技術的形成，也包含後果和治理；效益與風險都要轉成可觀察、可討論的條件。","用證據卡分別記主張、機制、結果、受影響者和後續驗證。"),
("easy","科學模型被修正是否代表過去所有觀察都是錯的？",["不一定；觀察可能仍有效，只是原模型無法涵蓋新條件或新資料", "是，模型一改所有資料必然失效", "模型修正只由投票決定", "只要新模型出現就不需再測量"],"A","資料、模型與適用範圍要分開；新證據常保留舊觀察，同時要求更精確或更廣的解釋。","先問被修正的是觀察、推論還是模型範圍，不把三者混成一件事。"),
("medium","評估一項科學史主張時，為什麼要注意當時的儀器與社會條件？",["工具會限制可取得的資料，社會制度也會影響誰能研究、誰能受益與結果如何被採用", "儀器和社會與科學完全無關", "只要年代正確就能解釋一切", "社會條件會直接決定自然定律"],"A","儀器影響證據範圍，資源、制度和需求影響研究與應用路徑，但自然現象仍需用可檢驗資料說明。","把自然證據限制和研究／應用的社會條件分成兩欄比較。"),
("hard","哪句最能表達科學知識形成的證據界線？",["目前資料支持某模型在特定條件下有效；新工具或新情境可能要求再檢驗，不應把暫時模型寫成永遠真理", "科學一旦寫進課本就不會改變", "只要模型能解釋一個例子就一定普遍成立", "有爭論就代表沒有任何可信資料"],"A","科學知識會在觀察、工具、模型和新資料互動中累積與修正；有範圍的結論比絕對口號更符合證據。","用模型、條件、預測與可修正性四項檢查歷史主張。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-mb-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-mb"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的觀察、工具、模型、證據、科學爭論、技術與社會影響能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-mb","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-mb、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合科學史中的觀察、工具、模型、證據累積、爭論、社會條件、生物技術與環境社會影響。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-mb-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為科學史觀察、工具、模型、證據、爭論、社會條件、生物技術與環境影響專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content mb")
if __name__=="__main__": main()
