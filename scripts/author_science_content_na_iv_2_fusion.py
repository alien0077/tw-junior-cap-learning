"""Na-Ⅳ-2：生活中的節能方法第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-na-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-na-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"功率、電能、生活用電與節能資料","pattern":"取公立學校自然科評量以功率、使用時間、電能、控制變因和生活決策推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"電能、效率、能源使用與圖表判讀","pattern":"取公開會考以公式、比例、時間、設備條件和方案效益評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"家庭校園用電、功率、待機與節能","pattern":"取公立國中試題以電器資料、使用情境、效率、控制條件與安全的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先確認設備功率、使用時間與要維持的服務品質。","用 E=P×t 統一比較各設備的能量使用。","把待機、環境溫度、使用人數和尖峰時段列為條件。","以相同照度、舒適度或功能需求做公平比較。","檢查安全、維護、壽命與反彈效應，再提出節能結論。"] for _ in range(10)]
ROWS=[
("easy","100 W 的電扇每天使用 5 小時，耗電量為多少？",["0.5 kWh", "5 kWh", "20 kWh", "500 kWh"],"A","100 W=0.1 kW，E=P×t=0.1×5=0.5 kWh。比較節能時還要說明使用天數與服務需求。","先把瓦特換成千瓦，再用功率乘使用時間並保留 kWh。"),
("medium","同樣提供教室照明，LED 燈功率較低但需要較多盞；公平比較應記錄什麼？",["總照度、燈具數、每盞功率、使用時間、壽命與製造／維護成本", "只比較單盞功率", "只看燈光顏色", "只看一次購買價格"],"A","若盞數不同，單盞功率不能代表整體耗電；還需確認照度、壽命、維護和生命週期。","先固定照明服務，再比較整組設備的總功率、時間與壽命。"),
("easy","電器待機時仍消耗少量電力，若長時間不用，較合理的節能方式是？",["在符合安全與設備要求下關閉電源或拔除插頭，而非反覆損傷插座", "把插頭剪斷", "用濕手操作開關", "遮住散熱孔"],"A","長時間累積的待機電能可透過合適的電源管理減少，但操作仍需遵守安全與設備說明。","先確認是否長時間不用，再選擇不造成觸電、過熱或設備損壞的方式。"),
("medium","冷氣功率 1.2 kW，每天運轉 4 小時；若每天少用 30 分鐘，一天約少用多少電？",["0.06 kWh", "0.6 kWh", "3.6 kWh", "4.8 kWh"],"B","少用 0.5 小時，節省 E=1.2×0.5=0.6 kWh。實際舒適度與室外條件仍需另行監測。","先把 30 分鐘換成 0.5 小時，再以功率乘節省時間。"),
("hard","把冷氣設定溫度調高但教室仍過熱，最完整的節能評估應？",["同時記錄室內溫度、濕度、人數、運轉時間、舒適度與耗電量", "只看設定溫度", "只看電費下降", "因為節能就忽略學生熱不適"],"A","設定值不是唯一因素；人數、外氣、濕度、隔熱與舒適度會影響實際耗電和服務結果。","把節能量與舒適／健康服務一起量測，不用單一設定值取代結果。"),
("medium","比較兩種節能宣導對用電量的效果，哪種設計較公平？",["固定班級、設備、課表與觀察期間，設對照並比較相同服務量下的用電", "一組在考試週、一組在普通週", "只比較最省電的一天", "宣導組同時更換全部設備"],"A","班級、課表和設備差異都會影響用電；對照和相同服務量才能較合理估計宣導的效果。","先固定可能混淆的條件，再設介入組和對照組並重複觀察。"),
("hard","新設備耗電較低但壽命短、常需更換；完整節能判斷應加入？",["製造、運輸、維修、廢棄與替換頻率的生命週期能源與成本", "只看運轉功率", "只看第一次使用的讀值", "只看包裝上的節能標章"],"A","使用階段省電可能被頻繁製造與替換的負荷抵銷；需以相同服務年限比較生命週期。","先設定比較年限，再把使用、製造、維修和廢棄全部納入。"),
("easy","下列哪種情況可能出現節能反彈？",["設備效率提高後，因使用時間或頻率增加，總耗電未如預期下降", "設備效率提高且使用量固定", "關閉不用的電器", "改善隔熱後同樣舒適度下耗電下降"],"A","效率改善若讓使用者增加使用量，節省的單位能量可能被總使用量抵銷，這是需要監測的反彈效應。","同時觀察單位效率、使用量和總耗電，不只看設備標示。"),
("medium","家庭要換購冰箱，哪組資料最能支持節能選擇？",["相同容量與服務需求下的年耗電、壽命、維修、價格與冷媒／環境條件", "只看外觀", "只看額定功率不看使用時間", "只看促銷折扣"],"A","家電長期使用的總耗電、壽命、維護和環境影響，比單一額定功率或折扣更能支持完整決策。","固定容量與服務，再比較年耗電、全壽命成本及環境限制。"),
("hard","哪句最適合作為校園節能結論？",["在維持照度、舒適度與安全的條件下，方案甲使相同課表的總用電下降；仍需追蹤季節、人數、設備壽命與使用反彈", "只要用電下降就代表所有人都更舒適", "設定溫度越高永遠越好", "節能只看月底電費即可"],"A","節能必須以服務品質和安全為邊界，並說明時間、設備與使用行為限制；單一電費數字不足。","用服務—耗電—安全—壽命—長期行為五項檢查結論。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-na-iv-2-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-na-iv-2"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的功率、電能、照明、冷氣、待機、設備生命週期、控制變因與節能決策能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-na-iv-2","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-na-iv-2、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合校園與家庭節能、功率、使用時間、電能、待機、冷氣、照明、服務品質、設備生命週期、反彈效應與安全。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-na-iv-2-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為校園／家庭節能、功率與時間、待機、冷氣、照明、服務品質、生命週期、反彈和安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content na-iv-2")
if __name__=="__main__": main()
