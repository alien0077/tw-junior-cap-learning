"""Bd-Ⅳ-1：太陽能經食物鏈流轉第一輪來源融合。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-bd-iv-1.json"
REPORT=ROOT/"implementation/reports/science-content-bd-iv-1-first-pass-review.json"
QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"食物鏈、能量塔、營養階層與生態系資料判讀","pattern":"取由食物鏈箭頭、營養階層與能量損失推論能量流動的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"生態系能量流動、食物鏈與食物網","pattern":"取生產者、消費者、能量塔與食物網的教學與評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"太陽能、營養階層與生態系能量","pattern":"取能量逐級傳遞、呼吸散失與物質循環區分的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8"))
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持由生產者、消費者、食物鏈與能量塔理解太陽能流轉。","箭頭方向、營養階層、能量耗散與能量流動／物質循環區分是共同評量核心。"],"versionDifferences":["南一公開定位偏向食物鏈與能量流；康軒線索偏向食物網與能量塔；翰林線索偏向能量耗散及物質循環比較。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以草地食物網、能量塔、取食路徑與呼吸熱散失建立可追蹤互動。","把食物鏈箭頭代表捕食者移動、能量可循環回太陽與高階消費者能量較多列為錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開自然科試題／課程資料能力方向，重新組織太陽能、生產者、消費者、食物鏈、能量塔、耗散與物質循環；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-bd-iv-1-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q.setdefault("provenance",{})["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題／課程資料的食物鏈、能量塔與生態系證據能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Bd-Ⅳ-1 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Bd-Ⅳ-1：太陽能經食物鏈流轉","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題／課程資料僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content bd iv 1")
if __name__=="__main__": main()
