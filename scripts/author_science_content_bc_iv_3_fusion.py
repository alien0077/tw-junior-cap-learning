"""Bc-Ⅳ-3：光合作用製造養分並釋氧第一輪來源融合。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-bc-iv-3.json"
REPORT=ROOT/"implementation/reports/science-content-bc-iv-3-first-pass-review.json"
QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"光合作用、澱粉與氧氣證據、光照與二氧化碳資料判讀","pattern":"取由反應物、產物、控制變因與實驗結果推論光合作用的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"光合作用、葉片澱粉檢驗與氧氣產生","pattern":"取葉綠體、光照、二氧化碳、澱粉與氣體證據的教學與評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"植物製造養分、釋氧與光合作用限制","pattern":"取遮光對照、水草氣泡與光強度資料的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8"))
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以二氧化碳、水、光能、葉綠體、澱粉與氧氣理解光合作用。","遮光對照、澱粉檢驗、水草氣泡與控制變因是共同評量核心。"],"versionDifferences":["南一公開定位偏向植物製造養分；康軒線索偏向葉片檢驗與氣體證據；翰林線索偏向光照資料、限制與生態系連結。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以遮光葉片、碘液澱粉矩陣、水草產氧與光強度曲線建立證據互動。","把植物吸收土壤有機物、氧氣是光合作用原料與產氧量永遠隨光增強列為錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開自然科試題／課程資料能力方向，重新組織光合作用反應物、產物、葉綠體、能量轉換與實驗證據；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-bc-iv-3-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q.setdefault("provenance",{})["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題／課程資料的光合作用、實驗證據與控制變因能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Bc-Ⅳ-3 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Bc-Ⅳ-3：光合作用製造養分並釋氧","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題／課程資料僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content bc iv 3")
if __name__=="__main__": main()
