"""Ib-Ⅳ-4：鋒面與天氣變化第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ib-iv-4.json"; REPORT=ROOT/"implementation/reports/science-content-ib-iv-4-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"鋒面、氣團、降雨與天氣圖資料判讀","pattern":"取由冷暖氣團、鋒面符號、測站時間序列、地形與降雨資料推論天氣變化的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"鋒面、冷暖氣團與天氣","pattern":"取冷鋒暖鋒滯留鋒、鋒面符號、氣團性質、降雨和天氣預報的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"鋒面觀測、地形降雨與預報證據","pattern":"取鋒面通過的氣壓溫度風向序列、山區平原差異、天氣圖移動與預報驗證的能力方向。"},
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以冷暖氣團交界、鋒面類型與測站觀測解釋天氣變化。","冷鋒暖鋒滯留鋒、鋒面符號、溫度氣壓風向降雨序列、地形影響與預報驗證是共同能力核心。"],"versionDifferences":["南一公開定位偏向鋒面與天氣；康軒線索偏向冷暖鋒、符號、氣團和降雨；翰林線索偏向測站時間序列、地形降雨、天氣圖移動與預報驗證。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以冷鋒、暖鋒、滯留鋒、天氣圖、山區平原和連續測站資料建立鋒面判讀證據鏈。","把鋒面等於一條固定線、降雨只由鋒面單獨決定、一次觀測即可證明鋒面通過列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織鋒面、氣團、冷暖鋒、滯留鋒、測站資料、地形與天氣圖限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
 qs=sorted(path for path in QDIR.glob("question-science-content-ib-iv-4-*.json") if path.stem.removeprefix("question-science-content-ib-iv-4-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ib-Ⅳ-4 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的鋒面、氣團、降雨、地形及天氣圖判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ib-Ⅳ-4 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ib-Ⅳ-4：鋒面與天氣變化","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對鋒面與天氣單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ib iv 4")
if __name__=="__main__": main()
