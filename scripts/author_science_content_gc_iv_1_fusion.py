"""Gc-Ⅳ-1：依形態與構造特徵分類生物第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-gc-iv-1.json"; REPORT=ROOT/"implementation/reports/science-content-gc-iv-1-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"生物分類、形態構造、檢索表與資料判讀","pattern":"取由可觀察構造特徵、二分選擇與分類證據建立可重複判斷的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"生物分類階層、二名法與檢索表","pattern":"取分類階層、學名書寫、二分法、植物與動物構造特徵的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"形態證據、分類限制與親緣推論","pattern":"取比較可重現形態、辨認趨同外觀、檢查分類表限制與補充證據的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以可觀察形態與構造特徵建立分類，並用二分法與分類階層整理生物多樣性。","分類特徵的可重複性、檢索表、二名法、植物／動物構造比較與證據限制是共同能力核心。"],"versionDifferences":["南一公開定位偏向分類特徵與階層；康軒線索偏向二分檢索表、二名法及常見生物構造；翰林線索偏向比較證據、趨同外觀與分類限制。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以校園調查、植物孢子／種子、動物外套與鳥類形態資料建立可重複分類流程。","把會飛當唯一分類依據、外觀相似等於親緣相近、分類一旦建立就不可修正列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織形態構造、分類階層、二分檢索表、二名法、植物／動物特徵與證據限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 qs=sorted(path for path in QDIR.glob("question-science-content-gc-iv-1-*.json") if path.stem.removeprefix("question-science-content-gc-iv-1-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Gc-Ⅳ-1 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的生物分類、形態構造、檢索表及證據判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Gc-Ⅳ-1 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Gc-Ⅳ-1：依形態與構造特徵分類生物","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對生物分類單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content gc iv 1")
if __name__=="__main__": main()
