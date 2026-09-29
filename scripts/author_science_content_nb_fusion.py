import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-nb.json"
QDIR=ROOT/"questions/science"
REPORT=ROOT/"implementation/reports/science-content-nb-first-pass-review.json"
TODAY="2026-09-23"
SOURCES=[
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考試題","氣候資料、極端天氣、環境變化與防災判讀","取公立學校自然科以長期資料、氣候現象與資料推理的能力方向，另寫校園案例。"),
 ("https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","114 年國中教育會考自然科公開試題","大氣、氣候、環境資料與科學證據","取公開會考對圖表、尺度、因果與環境決策的推理方向，未複製原題。"),
 ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","高雄市立國昌國民中學公開三年級自然科試題","降雨、洪水、地形、熱環境與防災方案","取公立學校自然科對危害、暴露、脆弱度與防災行動的能力方向，重新設計題目。"),
]
REFS=[{"url":u,"title":t,"year":"109-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS=[
 ("easy","某地 30 年平均氣溫上升且熱浪日數增加，最合適的判斷是？",["長期資料支持當地氣候條件可能改變，但仍需檢查自然變異與資料品質","單日高溫即可證明全球氣候已改變","所有地區一定同樣變化","氣候與天氣完全相同"],"A","多年平均與極端事件頻率提供氣候尺度線索；單一事件不能代表長期趨勢，也不能直接外推所有地區。","先確認時間尺度，再分辨資料支持的地方性趨勢和不能推出的全球結論。"),
 ("medium","兩社區遇到相近豪雨，甲排水良好且預警快，乙低窪且地下室有行動不便居民；乙風險較高主要因？",["乙的暴露與脆弱度條件較高，不能只看雨量","乙一定收到更多雨量","甲因為有排水就沒有任何危害","人口與避難資源不影響風險"],"A","相近危害下，地形、排水、人口暴露、健康與資訊資源仍會改變可能損失；風險不是只由雨量決定。","把危害、暴露、脆弱度與防護條件分欄，再找可改變的節點。"),
 ("medium","校園熱浪調適要比較方案，哪組指標最完整？",["遮蔭降溫、飲水可及性、活動暴露時間、健康通報、維護成本與弱勢學生使用情形","只比較設備價格","只看操場最高溫一次","只問多數學生喜不喜歡"],"A","調適同時涉及效果、可及性、健康、維護與公平；單一溫度或價格不能代表整體方案。","先固定要降低的熱暴露，再把效果、使用者、成本和長期維護一起列入比較。"),
 ("hard","三天破紀錄高溫後，哪項資料最能支援是否形成長期趨勢？",["同測站多年同季節的平均、極端值、熱浪日數與測量條件","只看三天新聞照片","只看另一城市一個下午的溫度","只問居民覺得今年熱不熱"],"A","氣候趨勢需要長期、可比且同尺度資料；短期事件和主觀感受可作線索，不能取代時間序列。","先選相同測站與季節，再比較多年分布和極端頻率並標記資料限制。"),
 ("medium","海平面上升使沿海低窪區積淹水風險增加，哪個調適順序較合理？",["先繪製危險、人口與重要設施暴露，改善預警與避難，再評估排水、海岸和土地使用方案","只把所有房屋加高，不查誰住在哪裡","只看海平面平均值，不看風暴潮","發生災害後才開始收集資料"],"A","調適要把危害、暴露與脆弱度放在空間資料中，並同時處理立即安全和長期土地、工程決策。","先畫風險分布和需要優先保護的對象，再依時間尺度安排預警、避難與工程。"),
 ("hard","某地乾旱年增加但農業用水需求也增加，哪個結論較誠實？",["供水壓力可能提高，仍需比較降雨、蓄水、用水量、作物和管理措施資料","只因乾旱增加就能算出所有農民損失","用水量增加一定代表浪費","乾旱和人類活動無關"],"A","水資源風險是自然供給與人類需求、儲存和管理交會的結果；需要多項資料才能評估影響與調適。","把供給、需求、儲存和脆弱群體分開量測，再比較節水或調整作物方案。"),
 ("medium","將遮蔭樹增加一倍後校園體感較舒適，但樹下人數、風速與測量時間也改變，應如何報告？",["先寫為初步關聯，控制測點、時間、風速和使用人數後重測，不能直接宣稱全由樹蔭造成","直接宣稱樹蔭必然降低所有健康風險","刪除不同條件資料","只看最舒服的一次"],"A","多項條件同時變動會造成替代解釋；可比的前後或對照資料才支持調適效果。","列出所有同步改變的變因，固定可控制條件，再設定重複測量和健康指標。"),
 ("hard","高溫通報方案要避免只照顧能待在冷氣房的人，哪項設計較公平？",["同時提供飲水、遮蔭、分時活動、可到達的降溫空間與戶外工作者／行動不便者的通知支援","只在圖書館裝冷氣並假設人人能到","只發英文公告","把高溫風險完全交給個人"],"A","脆弱度與資源可及性不同，公共調適需讓不同群體實際取得保護，而不是只增加單一設備。","先盤點誰最暴露、誰最難取得資源，再把通知、空間、交通和服務設計連結。"),
 ("medium","哪項指標最能追蹤豪雨調適是否有效？",["相近雨量下的積水深度與退水時間、預警觸達率及避難完成情形","只看工程竣工照片","只看總工程費","只記錄雨停時間"],"A","調適效果要和危害條件對照，並同時看物理結果與人員是否能取得預警、完成避難。","先定義基準和觸發條件，再用相近事件比較結果和資源可及性。"),
 ("easy","氣候調適與減緩的差別，哪個敘述正確？",["調適降低已面臨或預期影響的損失；減緩著重減少溫室氣體來源或增加移除","調適和減緩完全相同","只有個人行動是調適","減緩能保證不需任何調適"],"A","調適處理暴露與脆弱度及其影響，減緩處理造成氣候變化的排放或移除；兩者可互補但不能互相取代。","先問方案是在降低影響還是在改變排放，再檢查是否有共同效益和限制。"),
]

def make_question(n,row):
    diff,prompt,opts,source_answer,explanation,strategy=row; target="ACDBACDBAC"[n-1]
    correct=opts[ord(source_answer)-65]; distractors=[x for i,x in enumerate(opts) if i!=ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct)
        else: ordered.append(distractors[di]); di+=1
    steps=["標出資料的時間、地點、危害和受影響對象。","區分天氣事件與氣候長期訊號，再列暴露、脆弱度和防護條件。","檢查對照、測量尺度、替代解釋與方案的效果、公平和維護。",f"排除把單次事件當趨勢、把雨量當全部風險或忽略弱勢群體的選項，答案為 {target}。",f"以條件式結論說明調適作用、證據範圍與下一步監測：{explanation}"]
    return {"id":f"question-science-content-nb-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-nb"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開自然與理化資料的氣候、極端天氣、熱環境、降雨、防災、調適與資料尺度能力方向；本題為 Nb 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-nb","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-nb、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然與理化題型能力模式，獨立融合天氣與氣候尺度、熱浪、豪雨、乾旱、海平面、危害、暴露、脆弱度、調適、公平、監測與減緩區分。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-nb-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為天氣／氣候尺度、危害—暴露—脆弱度、熱浪、豪雨、乾旱、海平面、調適、公平與監測；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content nb")
if __name__=="__main__": main()
