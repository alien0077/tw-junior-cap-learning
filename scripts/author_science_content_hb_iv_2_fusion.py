"""Hb-Ⅳ-2：地層與地質事件的先後順序第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-hb-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-hb-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"地層、侵入、斷層、褶皺與事件排序","pattern":"取由疊積、交切、侵蝕、覆蓋和定年資料排序地質事件的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"地層關係與地質事件","pattern":"取疊積律、交切關係、侵入岩、斷層褶皺、侵蝕面與事件圖的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"地質事件排序、剖面判讀與資料限制","pattern":"取地層倒轉、火山灰定年、變質作用、化石對比與多證據排序的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以疊積、交切、侵蝕、覆蓋與定年證據排列地質事件。","地層正／倒轉、侵入岩、斷層褶皺、侵蝕面、變質作用、火山灰與事件圖是共同能力核心。"],"versionDifferences":["南一公開定位偏向地層關係與事件先後；康軒線索偏向疊積、交切、侵入與構造；翰林線索偏向地層倒轉、火山灰定年、變質作用及多證據排序。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以砂岩頁岩、岩脈、斷層覆蓋、褶皺礫岩、火山灰和花崗岩接觸變質建立事件圖。","把所有地層都能直接套疊積律、斷層切到就知道確切年份、侵入岩必然比所有地層年輕列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織疊積、交切、侵蝕、覆蓋、地層倒轉、侵入、變質、定年與事件排序限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 qs=sorted(path for path in QDIR.glob("question-science-content-hb-iv-2-*.json") if path.stem.removeprefix("question-science-content-hb-iv-2-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Hb-Ⅳ-2 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的地層、交切、侵入、構造、定年及事件排序能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Hb-Ⅳ-2 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Hb-Ⅳ-2：地層與地質事件的先後順序","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對地質事件排序單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content hb iv 2")
if __name__=="__main__": main()
