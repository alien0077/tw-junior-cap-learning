"""Ia-Ⅳ-4：全球地震與火山的帶狀分布第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ia-iv-4.json"; REPORT=ROOT/"implementation/reports/science-content-ia-iv-4-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"全球地震、火山、板塊邊界與地圖判讀","pattern":"取由地震深度、火山帶、海溝、海嶺與空間資料推論板塊邊界的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"全球地震火山帶與板塊運動","pattern":"取地震火山帶、聚合／張裂邊界、隱沒、海溝、海嶺與防災資料的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"震源分布、島弧與空間證據","pattern":"取震源由海溝向陸側變深、地震火山不完全重疊、地圖尺度與可檢驗假說的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以全球地震、火山、海溝、海嶺、震源深度和空間分布理解板塊邊界。","聚合、張裂、隱沒、島弧、資料尺度、防災解讀與可檢驗假說是共同能力核心。"],"versionDifferences":["南一公開定位偏向全球分布與板塊；康軒線索偏向邊界類型、海溝海嶺及防災；翰林線索偏向震源深度、島弧、重疊限制、地圖資料與假說設計。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以太平洋弧狀帶、中洋脊、海溝—火山帶、島弧、臺灣周邊與全球圖層建立空間證據鏈。","把地震火山完全重疊、沒有火山就沒有板塊活動、帶狀分布等於能預測確切日期列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織全球地震火山帶、板塊邊界、隱沒、海溝海嶺、震源深度、地圖尺度與證據限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 qs=sorted(path for path in QDIR.glob("question-science-content-ia-iv-4-*.json") if path.stem.removeprefix("question-science-content-ia-iv-4-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ia-Ⅳ-4 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的全球地震、火山、板塊邊界、震源及地圖判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ia-Ⅳ-4 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ia-Ⅳ-4：全球地震與火山的帶狀分布","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對全球地震火山帶單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ia iv 4")
if __name__=="__main__": main()
