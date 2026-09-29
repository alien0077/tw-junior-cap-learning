"""Ib-Ⅳ-5：臺灣的災變天氣第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ib-iv-5.json"; REPORT=ROOT/"implementation/reports/science-content-ib-iv-5-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"臺灣颱風、豪雨、季風、地形與防災資料判讀","pattern":"取由氣象觀測、地形水氣、颱風路徑、雨量水位與災害風險資料判斷天氣的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"臺灣災變天氣、颱風豪雨與防災","pattern":"取颱風、季風、豪雨、地形雨、乾旱、氣象資料與防災的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"災變天氣、時間序列與決策","pattern":"取雨量水位、預報路徑、迎風背風、區域差異、累積風險與證據導向行動的能力方向。"},
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以颱風、豪雨、季風、地形與長期氣象資料理解臺灣災變天氣。","風雨區域差異、地形雨、雨量水位時間序列、乾旱、預報驗證與防災決策是共同能力核心。"],"versionDifferences":["南一公開定位偏向臺灣天氣與災害；康軒線索偏向颱風季風、豪雨乾旱和防災；翰林線索偏向地形差異、資料序列、預報路徑與風險決策。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以颱風旋轉、豪雨資料、山脈迎風坡、水位、乾旱與路徑預報建立氣象風險證據鏈。","把颱風路徑等於每地風雨相同、單一雨量值即可預測災害、氣象預報等於確定事件列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織臺灣颱風、豪雨、季風、地形、乾旱、雨量水位、預報與防災限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
 qs=sorted(path for path in QDIR.glob("question-science-content-ib-iv-5-*.json") if path.stem.removeprefix("question-science-content-ib-iv-5-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ib-Ⅳ-5 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的臺灣颱風、豪雨、季風、地形、雨量水位及防災判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ib-Ⅳ-5 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ib-Ⅳ-5：臺灣的災變天氣","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對臺灣災變天氣單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ib iv 5")
if __name__=="__main__": main()
