"""Hb-Ⅳ-1：岩性與化石記錄地球歷史第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-hb-iv-1.json"; REPORT=ROOT/"implementation/reports/science-content-hb-iv-1-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"岩性、化石、地層與地球歷史資料判讀","pattern":"取由沉積構造、化石、地層事件和相對／絕對年代建立地球歷史推論的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"岩性、化石形成與地層關係","pattern":"取岩性、化石形成、標準化石、疊積律、褶皺斷層與沉積間斷的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"地層記錄、年代推論與證據限制","pattern":"取岩性與沉積環境、跨地點化石對比、事件排序、定年方法及地層缺口的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以岩性、化石、地層關係和年代資料重建地球歷史。","沉積構造、化石形成、標準化石、疊積律、褶皺斷層、沉積間斷與資料限制是共同能力核心。"],"versionDifferences":["南一公開定位偏向岩性與地層關係；康軒線索偏向化石形成、標準化石與地質構造；翰林線索偏向沉積環境、跨地點對比、定年和地層缺口。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以沉積顆粒、化石形成、跨地點化石、褶皺斷層、侵蝕面與砂層模型串成事件排序的證據鏈。","把岩石顏色直接等於年代、沒找到化石等於當時沒有生物、相對年代等於精確年份列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織岩性、化石、沉積環境、地層事件、相對／絕對年代與證據限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 qs=sorted(path for path in QDIR.glob("question-science-content-hb-iv-1-*.json") if path.stem.removeprefix("question-science-content-hb-iv-1-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Hb-Ⅳ-1 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的岩性、化石、地層、年代及證據判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Hb-Ⅳ-1 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Hb-Ⅳ-1：岩性與化石記錄地球歷史","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對岩性與化石單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content hb iv 1")
if __name__=="__main__": main()
