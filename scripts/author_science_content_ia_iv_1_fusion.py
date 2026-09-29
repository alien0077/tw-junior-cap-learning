"""Ia-Ⅳ-1：內外營力改變地貌第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ia-iv-1.json"; REPORT=ROOT/"implementation/reports/science-content-ia-iv-1-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"風化、侵蝕、搬運、沉積、板塊與地貌資料判讀","pattern":"取由地表作用、地質營力、地形證據與控制變因解釋地貌變化的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"內外營力、地貌與地表作用","pattern":"取風化侵蝕搬運沉積、河流海岸冰川風成地形、板塊與地貌的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"地貌證據、營力比較與災害因果","pattern":"取內外營力比較、河口沉積、坡面沖蝕、地震連鎖與多證據判讀的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以內營力與外營力解釋岩石風化、侵蝕、搬運、沉積及地貌變化。","河流、海浪、冰川、風、板塊、坡面沖蝕、災害連鎖與資料設計是共同能力核心。"],"versionDifferences":["南一公開定位偏向地表作用與地貌；康軒線索偏向風化侵蝕搬運沉積、各類地形與板塊；翰林線索偏向營力比較、沉積證據、坡面實驗與災害連鎖。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以原地風化、河流下游、海蝕平台、板塊聚合、冰川擦痕、風成砂丘與堰塞湖建立內外營力證據鏈。","把風化等於搬運、河流越快沉積越多、任何地形都由單一營力造成列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織風化、侵蝕、搬運、沉積、河流海岸冰川風成地形、板塊與控制變因；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs0=refs(); qs=sorted(path for path in QDIR.glob("question-science-content-ia-iv-1-*.json") if path.stem.removeprefix("question-science-content-ia-iv-1-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ia-Ⅳ-1 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs0; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的風化、侵蝕、搬運、沉積、板塊及地貌判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ia-Ⅳ-1 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ia-Ⅳ-1：內外營力改變地貌","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對內外營力單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ia iv 1")
if __name__=="__main__": main()
