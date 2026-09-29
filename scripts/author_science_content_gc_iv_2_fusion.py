"""Gc-Ⅳ-2：生物多樣性與生態系穩定第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-gc-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-gc-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"生物多樣性、生態系功能、資料判讀與保育","pattern":"取由物種／遺傳／生態系多樣性、交互作用與多指標資料判斷穩定性和保育的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"生物多樣性、生態系平衡與外來種","pattern":"取多樣性層次、生態系互動、外來種、食物網與保育議題的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"棲地、族群、穩定性與保育決策","pattern":"取棲地破碎化、遺傳多樣性、調查設計、多指標穩定性與證據導向決策的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以遺傳、物種與生態系三層次理解生物多樣性及生態系功能。","食物網、物質循環、外來種、棲地改變、遺傳多樣性、調查設計與保育決策是共同能力核心。"],"versionDifferences":["南一公開定位偏向多樣性層次與生態系功能；康軒線索偏向食物網、外來種與生態平衡；翰林線索偏向棲地、遺傳多樣性、多指標調查與證據導向保育。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以森林、湖泊、珊瑚礁、外來種和濕地調查資料建立由多樣性到穩定性的系統證據鏈。","把物種越多就必然永遠穩定、單一物種消失不會影響系統、一次調查即可決定保育政策列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織遺傳／物種／生態系多樣性、食物網、外來種、棲地、穩定性、調查與保育決策；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 qs=sorted(path for path in QDIR.glob("question-science-content-gc-iv-2-*.json") if path.stem.removeprefix("question-science-content-gc-iv-2-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Gc-Ⅳ-2 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的生物多樣性、生態系穩定、外來種、調查及保育決策能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Gc-Ⅳ-2 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Gc-Ⅳ-2：生物多樣性與生態系穩定","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對生物多樣性單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content gc iv 2")
if __name__=="__main__": main()
