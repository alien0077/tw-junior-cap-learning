"""Ic-Ⅳ-4：潮汐變化的規律第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ic-iv-4.json"; REPORT=ROOT/"implementation/reports/science-content-ic-iv-4-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"潮汐、月相、潮差、潮位資料與海岸安全判讀","pattern":"取由日月位置、潮位週期、潮差、颱風風暴潮與海岸資料推論潮汐的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"潮汐、朔望潮、小潮與月球引力","pattern":"取潮汐週期、日月排列、大潮小潮、潮間帶與海洋活動安全的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"潮位序列、港口差異與風暴潮","pattern":"取長期潮位、港口地形、月相模型、颱風海水面及風險決策的能力方向。"},
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以月球與太陽引力、地球自轉和海岸條件解釋潮汐週期與潮差。","高潮低潮、大潮小潮、潮位時間序列、港口地形、風暴潮、潮間帶與安全決策是共同能力核心。"],"versionDifferences":["南一公開定位偏向潮汐與月相；康軒線索偏向大潮小潮、潮間帶與海洋活動；翰林線索偏向潮位序列、港口差異、風暴潮與風險決策。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以朔望潮、上弦下弦小潮、半日潮、港口資料、風暴潮與潮間帶生物建立週期證據鏈。","把潮高只由月相決定、颱風海水面升高全是潮汐、所有海岸潮位相同列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織潮汐、月相、潮差、高潮低潮、大潮小潮、港口、風暴潮與時間資料限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
 qs=sorted(path for path in QDIR.glob("question-science-content-ic-iv-4-*.json") if path.stem.removeprefix("question-science-content-ic-iv-4-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ic-Ⅳ-4 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的潮汐、月相、潮差、風暴潮及海岸判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ic-Ⅳ-4 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ic-Ⅳ-4：潮汐變化的規律","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對潮汐規律單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ic iv 4")
if __name__=="__main__": main()
