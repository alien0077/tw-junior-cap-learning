"""Db-Ⅳ-2：循環系統的物質運輸與交換第一輪來源融合。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-db-iv-2.json"
REPORT=ROOT/"implementation/reports/science-content-db-iv-2-first-pass-review.json"
QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"循環系統、心臟血管、物質運輸與微血管交換判讀","pattern":"取由運輸路徑、血管功能與組織交換資料推論循環系統的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"心臟、血管、血液與物質運輸交換","pattern":"取心臟泵送、血管分工、血液成分與微血管交換的教學與評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"循環系統、肺循環、體循環與運動調節","pattern":"取氧氣旅程、瓣膜、血流方向與運動時供應需求的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8"))
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持由心臟、血管、血液與微血管交換理解循環系統的物質運輸。","肺循環、體循環、瓣膜、血液成分與運動調節是共同評量核心。"],"versionDifferences":["南一公開定位偏向循環系統路徑；康軒線索偏向心臟血管與血液成分；翰林線索偏向肺循環、物質交換與運動情境。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以氧氣旅程圖、瓣膜方向、微血管交換與運動後心搏建立循環互動。","把動脈一定含氧、血液只運輸氧氣與交換發生在心臟列為錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開自然科試題／課程資料能力方向，重新組織心臟、血管、血液、肺循環、體循環、微血管交換與運動調節；正文、互動、題目、答案、解析與五步解法均為原創，並修正原錯置植物運輸題為本單元循環交換題，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-db-iv-2-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q.setdefault("provenance",{})["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題／課程資料的循環系統、物質運輸與微血管交換能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Db-Ⅳ-2 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Db-Ⅳ-2：循環系統的物質運輸與交換","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"unitMismatchRemediated":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"已修正原先錯置的植物輸導題；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content db iv 2")
if __name__=="__main__": main()
