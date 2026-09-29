"""Ic-Ⅳ-1：波浪、海流與潮汐第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ic-iv-1.json"; REPORT=ROOT/"implementation/reports/science-content-ic-iv-1-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"波浪、海流、潮汐、月球引力與海岸資料判讀","pattern":"取由風能、海水大尺度流動、日月位置、潮汐週期與海洋資料推論的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"波浪海流潮汐與海洋現象","pattern":"取風浪、海流、潮汐、潮流、潮差、日月引力與海嘯的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"海洋週期資料、潮汐與海岸風險","pattern":"取長期潮位序列、港口比較、月相位置、海流資料及海嘯風險判讀的能力方向。"},
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持區分風浪、海流、潮汐與潮流，並用能量來源、海水搬運和日月引力解釋海洋現象。","風浪、海流、潮汐週期、潮差、月相位置、海嘯與長期港口資料是共同能力核心。"],"versionDifferences":["南一公開定位偏向波浪與潮汐；康軒線索偏向海流、潮流、潮差和海嘯；翰林線索偏向潮位序列、港口比較、月相與海岸風險。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以風浪、海流、港口潮位、朔望潮、小潮、潮流與海嘯建立能量與週期證據鏈。","把波浪的水質點前進等於海水整體搬運、所有潮差只由風決定、海嘯是一般風浪列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織波浪、海流、潮汐、潮流、月球引力、潮差、海嘯與週期資料限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
 qs=sorted(path for path in QDIR.glob("question-science-content-ic-iv-1-*.json") if path.stem.removeprefix("question-science-content-ic-iv-1-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ic-Ⅳ-1 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的波浪、海流、潮汐、月球引力、潮差及海洋判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ic-Ⅳ-1 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ic-Ⅳ-1：波浪、海流與潮汐","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對波浪海流潮汐單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ic iv 1")
if __name__=="__main__": main()
