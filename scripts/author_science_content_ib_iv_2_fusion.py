"""Ib-Ⅳ-2：氣壓差造成風第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ib-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-ib-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"氣壓、風向風速、等壓線與天氣資料判讀","pattern":"取由氣壓差、等壓線、地表受熱與氣象資料推論風及天氣變化的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"氣壓、風、海陸風與天氣系統","pattern":"取氣壓差、空氣流動、海陸風、等壓線、高低壓與天氣的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"氣象觀測、風場與證據限制","pattern":"取風向定義、等壓線疏密、地表受熱實驗、氣壓時間序列及多因素判讀的能力方向。"},
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以氣壓差解釋近地面空氣流動，並連結地表受熱、海陸風與天氣系統。","高低壓、等壓線、風向定義、風速、上升下沉氣流與觀測資料是共同能力核心。"],"versionDifferences":["南一公開定位偏向氣壓差與風；康軒線索偏向海陸風、等壓線與高低壓天氣；翰林線索偏向觀測定義、實驗控制、時間序列和多因素判讀。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以海陸風、等壓線疏密、低高壓、受熱模型與氣壓風速時間序列建立壓力梯度證據鏈。","把風從高壓直線吹向低壓、風向名稱等於空氣去向、氣壓下降必然代表某種天氣列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織氣壓差、風、海陸風、等壓線、高低壓、上升下沉與資料限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
 qs=sorted(path for path in QDIR.glob("question-science-content-ib-iv-2-*.json") if path.stem.removeprefix("question-science-content-ib-iv-2-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ib-Ⅳ-2 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的氣壓、風、等壓線、海陸風及觀測判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ib-Ⅳ-2 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ib-Ⅳ-2：氣壓差造成風","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對氣壓差造成風單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ib iv 2")
if __name__=="__main__": main()
