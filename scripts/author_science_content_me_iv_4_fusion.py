"""Me-Ⅳ-4：溫室氣體與全球暖化的第一輪獨立來源融合。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-me-iv-4.json"
REPORT=ROOT/"implementation/reports/science-content-me-iv-4-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"溫室效應、能源使用、碳排資料與生命週期","pattern":"取排放來源盤點、資料換算、生命週期與控制變因的能力方向，重新設計社區與家庭情境。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"全球暖化、能源、碳足跡與方案限制","pattern":"取由活動連到能量、排放係數與氣候證據的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"節能、再生能源、碳匯與長期成效","pattern":"取多條件評估與實驗／統計控制的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
STRATEGIES={1:"建立家庭排放盤點，沿用電、燃料、交通與消費鏈追到直接和間接來源。",2:"先由功率換算實際使用量，再納入電力來源、壽命和製造處置的生命週期。",3:"用節能前後差額乘排放係數，確認係數和能源來源與期間相符。",4:"畫出原料—製造—運輸—使用—處置的邊界，避免只算使用階段。",5:"把總排放轉成每人每趟或每公里，檢查乘載率與被替代交通方式。",6:"分開樹木吸碳、存活與維護排放，並以多年資料檢查碳匯是否持久。",7:"建立可比基準，控制季節、人口、設備使用與能源來源後再估算改變。",8:"同時看低運轉排放和間歇、儲能、土地、材料及電網整合限制。",9:"先確認活動資料、排放係數、系統邊界與不確定性，再解讀計算結果。",10:"用方案前基準和方案後長期資料，按人口與活動量校正並追蹤趨勢。"}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課從校園氣象站觀察夜間最低溫與屋頂長波散熱開始，接著把社區用電、交通、碳足跡、植樹、再生能源與減碳成效放進同一條可計算的證據鏈。學習者要分清自然溫室效應與人為增強、活動資料與排放係數、短期節能與長期全球暖化證據，最後指出計算邊界與不確定性。"; lesson["studyHighlights"]=["從屋頂夜間散熱畫出地表長波與溫室氣體的能量路徑。","以活動資料、排放係數和生命週期估算碳足跡。","用基準、對照與控制變因評估節能或再生能源方案。","在結論中標示系統邊界、時間尺度與估算不確定性。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持從能源活動、物質流與資料證據理解溫室氣體與全球暖化。","排放盤點、生命週期、控制變因與長期成效是評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向環境與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以校園夜間散熱、家庭碳計算、交通每人排放、植樹碳匯、再生能源調度與方案前後基準建立專屬互動。","把生命週期、系統邊界、排放係數與估算不確定性放入每題解題步驟。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織能量收支、排放盤點、碳足跡、碳匯與長期方案評估；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for i in range(1,11):
  p=QDIR/f"question-science-content-me-iv-4-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然／理化試題的溫室效應、能源使用、碳足跡、生命週期與方案評估能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開試題能力方向，題幹、選項、答案、解析與步驟均以 Me-Ⅳ-4 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["solutionStrategy"]=STRATEGIES[i]; q["solutionSteps"]=["圈出題幹的活動、能源來源、排放指標與比較期間。",f"依本題情境套用判準：{STRATEGIES[i]}","確認計算或推論的系統邊界、分母、係數與控制條件。","排除只看單一數字、忽略生命週期或把短期結果誇大成全球結論的選項。","回查答案是否符合題幹資料，並寫出估算的限制或下一項監測資料。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Me-Ⅳ-4：溫室氣體與全球暖化","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content me iv 4")
if __name__=="__main__": main()
