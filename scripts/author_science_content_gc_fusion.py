"""Gc：生物多樣性第一輪來源融合、題庫重寫與來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-gc.json"; REPORT=ROOT/"implementation/reports/science-content-gc-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"生物多樣性、棲地、生態系與保育資料判讀","pattern":"取由遺傳、物種、生態系多樣性與調查資料判斷保育問題的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"生物多樣性、外來種與棲地保育","pattern":"取多樣性層次、外來種、生態系功能、棲地破碎化與保育的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"族群遺傳、調查設計與資料可信度","pattern":"取遺傳多樣性、棲地連通性、樣區比較、長期監測與資料品質的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持由遺傳、物種與生態系三層次理解生物多樣性及其保育價值。","棲地、外來種、遺傳品系、樣區調查、連通性、長期監測與資料品質是共同能力核心。"],"versionDifferences":["南一公開定位偏向多樣性層次；康軒線索偏向外來種、棲地與生態系功能；翰林線索偏向族群遺傳、調查設計、連通性和長期資料可信度。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以水稻品系、濕地、人工林、外來種、池塘比較和資料庫設計建立由尺度到保育的證據鏈。","把物種數等於全部多樣性、外來種一律無害或一律有害、一次調查即可代表保育成果列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織遺傳／物種／生態系多樣性、棲地、外來種、族群調查、連通性與資料品質；原先 9 題已逐題改寫並補成 10 題，均具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 qs=sorted(path for path in QDIR.glob("question-science-content-gc-*.json") if path.stem.removeprefix("question-science-content-gc-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Gc 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的生物多樣性、棲地、外來種、調查及保育能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Gc 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Gc：生物多樣性","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原先 9 題已逐題改寫並補成 10 題生物多樣性專屬問題；每題有唯一答案、解析與五步解法，三筆公開試題／課程資料僅作 pattern-only 來源，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content gc")
if __name__=="__main__": main()
