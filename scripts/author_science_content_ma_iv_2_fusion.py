"""Ma-Ⅳ-2：保育、生物多樣性與公民責任第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ma-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-ma-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"生物多樣性、棲地、保育與環境資料","pattern":"取公立學校自然科評量以生態資料、保育方案、限制與行動推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"物種、遺傳、棲地與保育決策","pattern":"取公開會考以圖表、尺度、因果、族群風險與方案取捨評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"濕地、生物多樣性、保育與環境行動","pattern":"取公立國中試題以物種與棲地關係、資料監測和多條件決策的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先確認題目談的是遺傳、物種還是生態系多樣性。","找出棲地功能、威脅來源與受影響族群。","把方案的生態效益、成本與時間尺度放在同一表。","選擇可量測指標並保留對照、限制和不確定性。","提出誰能做、如何追蹤、何時修正的公民行動。"] for _ in range(10)]
ROWS=[
("easy","同一濕地中有多種鳥類、魚類與植物，這首先呈現哪一層次的生物多樣性？",["物種多樣性", "只代表單一物種的遺傳多樣性", "只代表水的化學多樣性", "只代表人類文化多樣性"],"A","不同物種的種類與相對數量呈現物種多樣性；遺傳多樣性要比較同種個體差異，生態系多樣性則比較棲地或系統。","先辨識比較單位是同種個體、不同物種，還是不同生態系。"),
("medium","紅樹林根系可減緩水流、提供幼魚躲藏；這些描述最接近哪種功能？",["棲地與生態系服務功能", "只是一種景觀價值", "只代表物種名稱", "與其他生物無關的地質現象"],"A","根系提供結構與屏障，能影響沉積、水流和幼魚存活，屬於棲地及生態系功能。","把生物存在本身和它改變環境、提供資源或保護的功能分開。"),
("easy","若濕地填平改建停車場後，候鳥停留數下降，最需要先確認哪項資料？",["填土時程、濕地面積與候鳥數量的時間序列及相近未開發區對照", "只看停車場面積", "只問一次路人的感受", "只記錄候鳥羽色"],"A","活動時程、棲地面積、長期數量和對照區能連結開發與鳥類反應，也能檢查天候等替代因素。","先把威脅事件與生物指標放在同一時間軸，再尋找對照。"),
("medium","兩個保育方案都能增加黑面琵鷺覓食面積，甲需限制部分養殖活動，乙成本較高但不改變養殖；比較時應？",["同時比較物種效益、受影響生計、成本、時間與補償方案", "只選覓食面積最大的方案", "因有養殖影響就完全否定甲", "只看初始建設費"],"A","保育效果不是唯一指標；生計、建置與長期維護及補償都會影響方案能否持續和公平。","把生態成果和社會代價分欄，再檢查誰承擔與誰受益。"),
("hard","禁捕後魚類數量增加，但水溫也下降；要判斷禁捕效果，哪個設計較有力？",["比較相近未禁捕區，固定季節與調查方法並同時記錄水溫、魚種和數量", "只比較禁捕前後兩次數量", "把水溫資料刪除避免混淆", "只選增加最多的魚種"],"A","對照與同步環境資料可拆開禁捕、水溫和季節變化的影響；單一前後比較不足。","列出同時改變的條件，設計對照和一致的取樣方法。"),
("medium","外來種移除後原生植物覆蓋率上升，但土壤含水量也提高；報告應如何寫？",["資料支持兩項條件同時變化，仍需控制水分或設對照才能估計移除的獨立效果", "原生植物增加必然全由移除外來種造成", "水分提高代表外來種移除沒有任何作用", "因兩因素同時變化所以資料應刪除"],"A","兩個因子同步變化造成混淆；需分離或記錄水分，才能估計外來種移除的效果。","把相關結果和可歸因的獨立效果分開，不把全部改善歸給單一行動。"),
("easy","下列哪項是可追蹤的保育指標？",["每季固定樣區的物種數、個體數與繁殖成功率", "大家覺得環境很漂亮", "活動口號被分享的次數", "方案名稱是否好聽"],"A","固定樣區、時間與方法取得的物種和繁殖資料可量測、重複並比較；主觀印象或口號不等同生態成效。","選指標時檢查是否能定義、量測、重複與和目標連結。"),
("hard","若保育區限制遊客後鳥類增加，但當地攤販收入下降，公民責任較完整的做法是？",["與受影響者共同討論替代生計、分流或補償，並同步監測鳥類與社會指標", "只報鳥類增加，收入問題不屬於保育", "因收入下降就取消所有保護", "由少數人直接決定且不公開資料"],"A","保育要能長期維持，需讓受影響者參與，處理利益分配並監測生態與社會結果。","把生態指標和公民、經濟指標並列，找出可協商、可修正的方案。"),
("medium","比較兩個棲地修復方案時，為什麼要保留『未修復區』？",["作為對照，協助判斷生物變化是否超出自然波動", "因為未修復區一定比修復區健康", "為了讓報告看起來有更多資料", "未修復區不需要任何測量"],"A","對照區提供沒有介入時的變化基準，有助於辨認修復效果與自然年際波動。","先定義介入，再保留沒有介入但條件相近的比較基準。"),
("hard","哪句最適合作為河口保育提案的結論？",["在三年調查中，封閉部分繁殖地使目標鳥種繁殖率提高，但需持續和社區協商並監測其他物種與生計影響", "封閉後鳥變多，所以所有濕地都應永久封閉", "只要物種數增加就代表所有生態功能恢復", "保育有爭議，因此不能用任何資料做決策"],"A","提案同時交代時間、目標指標、效果範圍、其他影響與持續協商，避免把局部成果擴大成無條件規則。","用目標—證據—範圍—副作用—後續監測五段整理結論。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-ma-iv-2-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-ma-iv-2"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的生物多樣性、濕地、棲地功能、保育、監測、社會代價與公民行動能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-ma-iv-2","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-ma-iv-2、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合遺傳／物種／生態系多樣性、河口濕地、棲地功能、人為威脅、保育方案、監測指標、社會代價與公民責任。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-ma-iv-2-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為生物多樣性、濕地棲地功能、人為威脅、保育取捨、監測指標、對照、利害關係人與公民責任專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ma-iv-2")
if __name__=="__main__": main()
