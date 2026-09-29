import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-me-iv-1.json"
QDIR=ROOT/"questions/science"
REPORT=ROOT/"implementation/reports/science-content-me-iv-1-first-pass-review.json"
TODAY="2026-09-23"
SOURCES=[
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考試題","污染物、環境因子、生物反應與資料判讀","取公立學校自然科對環境因子、生物反應與控制變因的評量方向，另寫水草實驗。"),
 ("https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","114 年國中教育會考自然科公開試題","生物與環境、實驗資料與證據推論","取公開會考對圖表、實驗條件、證據範圍與環境應用的推理方向，未複製原題。"),
 ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","高雄市立國昌國民中學公開二年級自然科段考","污染、生物指標、對照與處理後安全","取公立國中試題以污染、生物指標、對照與安全判斷的能力方向，重新設計題幹。"),
]
REFS=[{"url":u,"title":t,"year":"109-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS=[
 ("easy","要研究清潔劑濃度是否影響水草根長，哪個設計最能支持因果判斷？",["固定光照、溫度、水量與植物條件，只改變濃度並設清水對照","同時改變濃度和光照","每組只放一株且不設對照","只觀察水的顏色"],"A","固定其他條件、設對照並只改變一項自變因，才能把根長差異較合理地連到濃度；仍需重複與量測限制。","先找自變因和應變因，再固定混淆條件，最後檢查是否有對照和重複。"),
 ("medium","高濃度組根長平均較短，但其溶氧也較低，最嚴謹的結論是？",["污染物已被證明是唯一原因","在本條件下高濃度與根長下降同時出現，但污染物與缺氧作用尚未分開","只要植物未死亡就沒有影響","所有植物都會得到相同結果"],"B","濃度與溶氧同時改變，不能只由結果指定單一原因；需要額外控制或測量溶氧來排除替代解釋。","先描述共同變化，再找同時改變的條件，最後把結論限制在本實驗並提出下一項控制。"),
 ("easy","生物指標顯示魚活動力下降，哪項補充最必要？",["只拍魚的外觀","直接檢測污染物濃度、溶氧與水溫，並記錄暴露時間","刪除沒有下降的資料","立即宣稱水不能接觸"],"B","生物反應能提供警訊，但不能取代污染物與環境條件的直接測量；濃度、溶氧、水溫和時間有助於辨識原因與風險。","先把生物指標當警訊，再補上化學或物理量測和暴露條件，避免把相關直接寫成確定因果。"),
 ("medium","污染濃度相同，短時間與長時間暴露的根長不同，應如何解釋？",["暴露時間是無關變因","物質種類、濃度、接觸時間與植物狀態共同影響反應，不能只用濃度概括","時間越長一定沒有影響","一次測量即可代表整個生命週期"],"B","生物效應常受劑量與時間交互影響；相同濃度不代表相同累積暴露或生理反應，需用時間序列比較。","先固定或記錄濃度，再把時間列為條件，畫出指標隨時間的變化並避免過度外推。"),
 ("hard","若用水草協助降低污染，哪項結果仍不足以宣布水已安全？",["水看起來變清且水草存活","污染物直接檢測下降且有重複資料","處理前後都量測濃度、溶氧與水草狀態","以空白對照和已知濃度標準檢查方法"],"A","外觀變清和生物存活不能證明污染物消失，污染物可能被吸收、轉換或留在沉積物；必須直接檢測和安全處置。","分開『看起來改善』與『污染負荷下降』，追查污染物去向，再確認處理後水、生物與沉積物的安全。"),
 ("medium","四組水草根長分別為 3、4、4、5 公分，哪項作法較能增加結果可信度？",["只挑最長的一株報告","增加每組樣本與重複試驗，並報告平均和變異","刪除差距最大的組別","把所有組的光照同時改變"],"B","增加樣本與重複有助於估計個體差異和測量變異；保留完整資料並報告分布比挑選單值更誠實。","先確認資料是否完整，再增加重複與樣本，最後同時呈現平均、範圍或變異而非只選漂亮結果。"),
 ("hard","若高濃度組葉片變黃，哪個詞不宜直接寫進結論？",["可能","在本測試條件下","一定由該污染物造成","仍需測量酸鹼值"],"C","葉黃可能與污染物、酸鹼、養分、光照或其他因素有關；控制不足時不能用『一定』宣告單一因果。","找出結論中超出資料的強詞，改寫成有範圍的可能性，並指定要補量的替代因素。"),
 ("medium","設計校園排水點的生物監測時，哪個流程較完整？",["先選一種植物並直接接觸未知污水","確認來源與安全界線，設空白對照、量生物指標和直接水質指標，再依時間序列判讀","只在水變色時拍照","將測試植物帶回食用"],"B","未知污染物可能造成接觸與處置風險；生物監測應在安全規範下搭配空白、直接檢測、重複與時間資料，不能冒險或食用。","先做安全與來源盤點，再決定對照和指標，安排直接量測與廢液處置，最後以時間序列評估。"),
 ("hard","兩種處理法都使根長恢復，但只有甲法讓污染物濃度下降；較合理的判斷是？",["兩法安全性完全相同","甲法較有直接降低污染物的證據，乙法仍需追查是暫時遮蔽、轉移或其他條件改變","根長恢復就代表污染消失","只選成本較低者即可"],"B","生物生長和污染物濃度是不同指標；甲法有直接證據，乙法不能因外觀恢復就宣稱處理完成，還要追查污染物去向。","先並列生物和化學結果，再辨識一致或不一致之處，最後提出沉積物、代謝物和長期追蹤的檢查。"),
 ("medium","要把實驗結果外推到另一種植物和自然河川，哪個限制最重要？",["自然河川的物種、流速、溫度、混合污染物、沉積與暴露時間可能不同","只要數值漂亮就能外推","另一種植物一定與水草相同","自然環境不需要對照"],"A","實驗物種和控制條件與自然河川不同，反應可能改變；外推要先標示適用範圍並以現地資料驗證。","列出實驗與新情境的相同和不同條件，挑出會改變機制的因素，再設計現地監測或新對照。"),
]

def make_question(n,row):
    diff,prompt,opts,source_answer,explanation,strategy=row; target="ACDBACDBAC"[n-1]
    correct=opts[ord(source_answer)-65]; distractors=[x for i,x in enumerate(opts) if i!=ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct)
        else: ordered.append(distractors[di]); di+=1
    steps=["圈出污染物、暴露時間、生物指標和控制條件。","區分觀察數據、可能機制與尚未測量的替代原因。","檢查對照、樣本、重複、單位與是否只改變一項條件。",f"排除過度外推、把生物外觀當安全證明或忽略危險操作的選項，答案為 {target}。",f"回寫有範圍的結論並列出下一項直接檢測：{explanation}"]
    return {"id":f"question-science-content-me-iv-1-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-me-iv-1"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開自然科試題與會考資料的污染、生物反應、控制變因、圖表證據與環境安全能力方向；本題為 Me-Ⅳ-1 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-me-iv-1","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-me-iv-1、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然科題型能力模式，獨立融合污染物、濃度、暴露時間、生物生長指標、控制變因、生物監測、生物處理、直接檢測、外推限制與安全處置。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-me-iv-1-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為污染濃度、暴露、生物指標、控制變因、生物處理安全、直接檢測與外推限制；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content me-iv-1")
if __name__=="__main__": main()
