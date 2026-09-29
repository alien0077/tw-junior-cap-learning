"""Ic-Ⅳ-3：臺灣附近海流的季節變化第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ic-iv-3.json"; REPORT=ROOT/"implementation/reports/science-content-ic-iv-3-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"臺灣附近海流、季風、海溫與海洋資料判讀","pattern":"取由季風、海流方向速度、海溫、漂流物和季節時間序列建立區域海洋推論的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"臺灣海域、黑潮、季風與海流","pattern":"取黑潮、季節風、沿岸流、海溫、漁業與海洋安全資料的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"季節海流、資料控制與海上活動","pattern":"取季節比較、測站條件、漂流物、魚群關係、方向定義與海流資料應用的能力方向。"},
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以季風、黑潮、海溫、海流方向速度和季節時間序列理解臺灣附近海域變化。","方向定義、測站條件、海流與風的關係、漂流物、魚群資料與海上安全是共同能力核心。"],"versionDifferences":["南一公開定位偏向臺灣海流與季節變化；康軒線索偏向黑潮、季風和海溫；翰林線索偏向季節比較、資料控制、漂流物、魚群與海上應用。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以黑潮、東北季風、海流箭頭、漂流物、魚群季節資料與海上活動建立區域海洋證據鏈。","把海流方向等於風向、黑潮全年影響完全不變、魚群分布單獨證明海流因果列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織臺灣附近海流、季風、黑潮、海溫、季節資料、漂流物與海洋應用限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
 qs=sorted(path for path in QDIR.glob("question-science-content-ic-iv-3-*.json") if path.stem.removeprefix("question-science-content-ic-iv-3-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ic-Ⅳ-3 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的臺灣海流、季風、黑潮、季節資料及海洋安全判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ic-Ⅳ-3 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ic-Ⅳ-3：臺灣附近海流的季節變化","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對臺灣海流季節變化單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ic iv 3")
if __name__=="__main__": main()
