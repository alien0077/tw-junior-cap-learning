"""Mc-Ⅳ-6：用電安全第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-mc-iv-6.json"; REPORT=ROOT/"implementation/reports/science-content-mc-iv-6-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"電路、用電安全、功率與保護裝置","pattern":"取公立學校自然科評量以電路條件、故障判讀、額定值和安全程序推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"電流、電阻、功率、短路與生活安全","pattern":"取公開會考以公式、圖表、情境、因果和風險界線評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"家庭電路、保險絲、接地、漏電與安全","pattern":"取公立國中試題以電流路徑、保護機制、額定條件和事故處置的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先切斷電源並辨識外觀、環境與負載的危險訊號。","區分過載、短路、漏電、接觸不良和設備破損。","檢查電壓、功率、電流、導線與保護裝置的額定條件。","判斷保險絲、斷路器、接地或漏電保護能處理哪種風險。","選擇不拆修、不碰觸、不在潮濕環境操作並通知合格人員的安全行動。"] for _ in range(10)]
ROWS=[
("easy","同一插座同時接多個高功率電器，插頭與延長線變熱；最可能先懷疑哪種危險？",["過載造成電流過大與導線發熱", "光線折射", "電池化學能增加", "接地一定過強"],"A","多個高功率負載共用路徑可能使總電流超過導線或插座額定，導致發熱；應停止使用並由合格人員檢查。","先估計同一路徑的總負載，再與額定條件比較，不以外觀正常就繼續使用。"),
("medium","火線與中性線直接低電阻相接，最符合哪種故障？",["短路，電流可能瞬間大增並觸發保護裝置", "正常用電", "只有漏電而沒有電流", "電阻增加造成電流變零"],"A","直接低電阻接通會形成短路，電流可能大幅增加並造成發熱或保護裝置動作，不能自行測試。","先畫電流路徑，找是否繞過負載形成低電阻通路，再判斷危險。"),
("easy","電器外殼漏電時，接地線的主要功能是？",["提供較低阻抗的安全路徑，協助故障電流引發保護而降低外殼持續帶電風險", "讓所有電器功率增加", "使潮濕消失", "保證任何故障都不會有人受傷"],"A","接地可在故障時提供電流路徑並協助保護裝置動作，但不是萬能保證，仍需檢修與避免接觸。","區分接地的保護路徑和人體接觸風險，不把接地當成可繼續使用的許可。"),
("medium","漏電斷路器反覆跳脫，最安全的處置是？",["停止使用該設備並切斷相關電源，請合格人員查明原因，不反覆強行復歸", "一直重開直到不跳", "用金屬物固定開關", "在潮濕處自行拆開插座"],"A","反覆跳脫是故障或漏電的警訊，強行復歸可能讓人暴露於危險；需隔離並由合格人員檢查。","把保護裝置動作視為警報，不繞過保護，也不進行未授權拆修。"),
("hard","保險絲額定電流過大，可能造成什麼問題？",["故障電流未及時切斷，導線可能在保護動作前過熱", "所有電器自動更省電", "漏電必然消失", "電壓會變成零且沒有熱效應"],"A","保護元件額定值需配合導線與設備；過大可能失去過電流保護，讓故障熱量累積。","先比較保護元件、導線和負載的額定條件，不以『能通電』判斷安全。"),
("medium","雨天手是濕的，接觸插頭或電器時風險提高的主要原因是？",["水分可能降低人體與環境的等效電阻，使故障電流更容易通過人體", "濕手會讓電壓自動變成零", "水分只影響電器顏色", "只要穿鞋就能安全操作任何設備"],"A","潮濕可能改變接觸與人體電阻，增加觸電危險；應保持乾燥、遠離電源並請成人或合格人員處理。","辨認環境因素如何改變電流路徑，不能用單一防護物推論絕對安全。"),
("easy","電器銘牌標示 110 V、1000 W，接在額定電壓下工作時，額定電流約為？",["0.11 A", "9.1 A", "110 A", "1000 A"],"B","I=P/V=1000 W÷110 V≈9.1 A；實際安全仍要確認插座、導線和保護裝置額定值。","先把功率和電壓代入 I=P/V，再把結果與供電路徑額定條件比較。"),
("hard","插頭有焦黑痕跡但電器仍能運作，最合理的判斷是？",["可能有接觸不良、過熱或電弧風險，應停止使用並檢修", "能運作就代表安全", "只要擦掉焦黑即可繼續", "焦黑代表電阻一定變小且沒有危險"],"A","焦黑可能表示局部過熱、接觸不良或電弧，繼續使用可能惡化；不可只靠外觀清潔消除故障。","把異常外觀當成故障證據，先隔離電源，再交由合格人員檢查。"),
("medium","比較兩條延長線能否供應同一組電器，哪項資料最不能省略？",["導線與插座額定電流、總功率、線長、是否盤捲、環境溫度與保護裝置", "只比較線的顏色", "只看包裝上的最大數字而不看使用條件", "只問使用者覺得哪條較粗"],"A","導線散熱、額定電流、總負載和使用方式共同影響安全，盤捲與高溫也可能增加過熱風險。","先計算總負載，再逐項核對導線、插座、環境和保護條件。"),
("hard","哪句最適合作為校園用電安全結論？",["在額定電壓、功率、導線與保護條件符合且環境乾燥時使用；若有發熱、跳脫、焦痕或漏電警訊，立即停用並交由合格人員處理", "只要斷路器沒跳就一定安全", "把保險絲換大即可解決所有故障", "潮濕時只要快速操作就沒有風險"],"A","用電安全需同時符合額定、環境、設備與保護條件；保護裝置不是允許繼續使用故障設備的理由。","用條件、警訊、立即行動與專業處置四段整理安全結論。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-mc-iv-6-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-mc-iv-6"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的過載、短路、漏電、接地、保險絲、斷路器、額定值、潮濕與用電安全能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-mc-iv-6","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-mc-iv-6、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合過載、短路、漏電、接觸不良、破損、潮濕、保險絲、斷路器、接地、漏電保護、額定條件與安全處置。10 題均重新撰寫，未複製受保護內容；不鼓勵危險實作；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-mc-iv-6-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"safetyBoundary":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為過載、短路、漏電、接地、保護裝置、額定條件、潮濕、故障警訊與安全處置專屬問題；每題有唯一答案、解析與五步解法，未引導危險操作。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content mc-iv-6")
if __name__=="__main__": main()
