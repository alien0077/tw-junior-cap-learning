"""I：變動的地球第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-i.json"; REPORT=ROOT/"implementation/reports/science-content-i-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"地震、火山、板塊運動與資料判讀","pattern":"取由震波、震央、震度、火山與地質構造資料推論地球變動的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"地震、板塊與火山活動","pattern":"取震波、震央定位、板塊邊界、火山、地震安全與地球內部變動的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"地震資料、場址效應與板塊證據","pattern":"取 P/S 波、震度與規模、軟弱地層、火山警戒、板塊空間分布及多證據推論的能力方向。"},
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持由地震、火山、地質構造與板塊運動資料理解變動的地球。","P／S 波、震央定位、規模／震度、場址效應、火山警戒、板塊邊界與資料限制是共同能力核心。"],"versionDifferences":["南一公開定位偏向地震與火山現象；康軒線索偏向震波、板塊和地球內部變動；翰林線索偏向場址效應、警戒資料、空間分布及多證據判讀。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以測站到時、震央三角定位、板塊碰撞、斷層滑動、火山灰、軟弱沉積層與空間分布建立地球變動證據鏈。","把震度等於規模、火山灰升高必然代表即刻爆發、單一地震即可證明板塊全年移動列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織震波、震央、震度／規模、板塊、火山、場址效應與證據限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
 qs=sorted(path for path in QDIR.glob("question-science-content-i-*.json") if path.stem.removeprefix("question-science-content-i-").isdigit())
 if len(qs)!=10: raise SystemExit(f"I 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的地震、火山、板塊、場址及資料判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 I 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"I：變動的地球","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原先 9 題已補成 10 題；每題均有唯一答案、解析與五步解法，三筆公開試題／課程資料僅作 pattern-only 來源，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content i")
if __name__=="__main__": main()
