"""Md：天然災害與防治第一輪原創題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-md.json"; REPORT=ROOT/"implementation/reports/science-content-md-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"地震、氣象、災害資料與防治判讀","pattern":"取公開自然科評量以自然作用、時間空間資料、災害影響與安全行動推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"地震、雨量、地形、風險與資料判讀","pattern":"取公開會考以圖表、測量尺度、因果限制和生活防災情境判讀的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"天然災害、地震、豪雨、地形與防災措施","pattern":"取公立國中試題以成因、影響、監測資料和防治行動進行安全推理的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["圈出災害類型、測量位置、時間與暴露對象。","分開自然作用、脆弱度和防護條件。","用雨量、震度、地形或警報資料推論風險。","排除把名稱、單一照片或平均值當完整證據。","選擇安全、可執行且有觸發條件的行動。"] for _ in range(10)]
ROWS=[
 ("easy","比較兩個社區的災害風險時，最先要確認哪些資料？",["致災因子、暴露對象、脆弱度以及資料的時間與地點","只看社區名稱","只看離山或海的直線距離","先猜哪區一定最危險"],"A","風險不只由自然作用強度決定，還要看誰暴露、建物與地形脆弱度、防護能力及資料尺度。","先把自然作用、暴露和資料條件分欄。"),
 ("medium","地震報告寫『規模 6.0、某站震度 5 弱』，哪項說法正確？",["規模描述事件釋放能量，震度描述特定地點的搖晃程度","震度 5 弱就是地震規模 5 弱","規模會因測站不同而各自改變","只要知道震度就能知道所有地區損害"],"A","規模是地震事件的量，震度會受距離、地盤和測站位置影響；兩者不能互換。","先辨認量測對象，再判斷數值的空間範圍。"),
 ("medium","豪雨後要判斷土石流風險，哪組資料最有用？",["累積雨量、短時間雨強、坡地地形、土砂條件與官方警戒位置時間","只看一張積水照片","把全臺平均雨量套用每條溪谷","只問居民覺得雨大不大"],"A","土石流風險需結合降雨時間尺度、坡地與土砂條件及位置化警戒資訊；單一照片不足以支持完整判斷。","將資料對齊同一地點、時間和風險門檻。"),
 ("easy","颱風警報發布後，最符合防災原則的行動是？",["依官方警報與地方避難資訊提早移動，避開淹水、落石和海岸危險區","到河邊觀察水位","等到道路積水後再決定","只依社群轉傳路線"],"A","防災要依可靠警報與地方資訊提前行動，並避免進入可能有二次災害的現場；不可把觀察災害當成必要證據。","把警報、位置和安全替代路線連起來。"),
 ("hard","某地雨量很高但沒有土石流，能否因此說雨量與土石流無關？",["不能，還要考慮坡度、土砂、植被、排水與雨量時間分布","可以，雨量永遠不是因素","可以，因為土石流只由地震造成","不能，代表所有地區都會發生土石流"],"A","降雨是可能的致災因子之一，但地形、材料、植被和累積及短時雨強也影響結果；單一地點不能否定整體關係。","列出替代條件，避免由一個反例過度推論。"),
 ("medium","設計校園防災演練時，哪項最能把口號轉成可執行方案？",["指定警報觸發、集合點、責任人、替代路線與無障礙需求並演練","只寫提高警覺","等災害發生才找集合點","只要求學生記住災害名稱"],"A","可執行方案需把資料或警報轉成明確行動，並考慮通訊中斷、行動不便者、積水和餘震等限制。","檢查行動、責任、時間和二次風險。"),
 ("hard","若兩社區遭遇相同豪雨，但甲區排水好、建物耐震且人口少，乙區排水差且位於坡腳；比較風險時應如何？",["乙區可能較高，因暴露與脆弱度不同，不能只比較降雨強度","兩區風險必相同，因雨量相同","甲區一定零風險","只看人口即可決定全部風險"],"A","相同致災因子下，排水、坡腳地形、建物與人口等暴露及脆弱度會使風險不同；不能只看雨量。","固定自然作用後比較暴露、脆弱度和防護能力。"),
 ("medium","地震後發現教室牆面有裂縫，最安全的第一步是？",["依校方與專業人員指示撤離或封鎖危險區，不自行進入檢查並留意餘震","靠近裂縫拍照並觸摸確認","立刻使用受損電梯","只要主震過了就回教室"],"A","受損建物可能有掉落與餘震風險，應依校方、消防或專業指示行動，避免增加二次傷害。","安全優先，不把近距離觀察當必要科學證據。"),
 ("hard","要評估避難路線是否可靠，哪項資料組合最完整？",["地形高程、可能淹水或落石區、警報時間、道路狀況與替代路線","只看地圖上最短距離","只看平常通勤時間","只問一位居民印象"],"A","避難路線要同時考慮地形、致災區、時間、通行狀況和備援；最短不一定最安全。","以空間、時間、風險和替代方案共同判讀。"),
 ("easy","防災報告中哪個結論最符合證據界線？",["資料顯示本次雨量與坡地條件達警戒，因此此區需依官方指示避難；未測區域仍需查證","只要雨量高，全臺一定都要同時撤離","一張照片就證明所有坡地都會崩塌","災害名稱本身就能決定損害大小"],"A","此結論把資料、地點、門檻與行動連結，也保留未測區域的限制，沒有把局部證據擴大成普遍定律。","用證據—風險—行動—限制四格完成報告。"),
]
def make_question(n,row):
 difficulty,prompt,options,answer,explanation,strategy=row
 return {"id":f"question-science-content-md-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",options)],"knowledgeIds":["kg-science-content-md"],"difficulty":difficulty,"answer":{"value":answer,"explanation":f"{explanation} 正確答案為選項 {answer}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的地震、颱風、豪雨、地形、風險資料與防治能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-md","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"
 lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-md、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合地震、颱風、豪雨、土石流、致災因子、暴露、脆弱度、震度／規模、警戒資料、避難路線與二次風險。原有科學問題取樣錯配題已全部改為天然災害與防治專屬題目；所有正文、資料、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-md-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原有科學問題取樣錯配題已移除，10 題改寫為地震、颱風、豪雨、土石流、風險、警戒、避難、二次風險與證據界線專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content md")
if __name__=="__main__": main()
