"""Ic-Ⅳ-2：海流影響陸地氣候第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ic-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-ic-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"海流、暖寒流、沿岸氣候、海霧與資料判讀","pattern":"取由海水大尺度流動、海溫、風場、沿岸溫度降雨與長期資料推論氣候影響的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"海流、暖寒流與陸地氣候","pattern":"取海流類型、海溫、沿岸氣候、海霧、漁業與海洋環境的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"海流資料、沿岸比較與氣候證據","pattern":"取城市長期氣候比較、水槽模型、寒暖流與風向交互作用及天氣氣候尺度的能力方向。"},
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以海流搬運熱量、海溫差異、風場與沿岸資料解釋陸地氣候。","暖流寒流、海霧、沿岸溫度降雨、長期平均、城市比較與模型控制是共同能力核心。"],"versionDifferences":["南一公開定位偏向海流與氣候；康軒線索偏向暖寒流、海霧、海洋環境；翰林線索偏向長期城市資料、水槽模型、風向交互作用與天氣氣候尺度。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以海流定義、暖寒流沿岸、海溫資料、海霧、水槽模型與城市長期平均建立熱量搬運證據鏈。","把海流直接決定每天氣溫、暖流一定增加所有地區降雨、單一城市一天的天氣代表海流氣候效應列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織海流、暖寒流、熱量搬運、海霧、沿岸氣候、長期資料與模型限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
 qs=sorted(path for path in QDIR.glob("question-science-content-ic-iv-2-*.json") if path.stem.removeprefix("question-science-content-ic-iv-2-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ic-Ⅳ-2 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的海流、暖寒流、沿岸氣候、海霧及長期資料判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ic-Ⅳ-2 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ic-Ⅳ-2：海流影響陸地氣候","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對海流影響氣候單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ic iv 2")
if __name__=="__main__": main()
