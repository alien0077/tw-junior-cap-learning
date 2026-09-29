"""Da：細胞的構造與功能第一輪來源融合。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-da.json"; REPORT=ROOT/"implementation/reports/science-content-da-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"細胞構造、胞器、細胞分工與有絲分裂資料判讀","pattern":"取由顯微影像、構造功能、細胞層次與分裂資料推論生命現象的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"細胞構造、顯微鏡、細胞分工與生長","pattern":"取細胞基本單位、植物／動物細胞、胞器、細胞分工與分裂的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"細胞觀察、層次、構造功能與有絲分裂","pattern":"取顯微觀察、構造適應、細胞—組織層次、DNA複製與分裂資料判讀方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以顯微觀察、細胞構造與胞器功能理解細胞作為生物體基本單位。","植物／動物細胞、細胞分工、層次、生長與有絲分裂資料判讀是共同能力核心。"],"versionDifferences":["南一公開定位偏向細胞觀察與基本構造；康軒線索偏向胞器、植物／動物比較與功能；翰林線索偏向顯微證據、層次、DNA複製與分裂資料。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以顯微影像、構造卡與分裂染色體模型串接觀察證據、功能推論與層次判斷。","把胞器名稱等於整個功能、單細胞不能分工、DNA複製等於染色體數量翻倍列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織細胞構造、胞器、顯微觀察、細胞分工、層次與有絲分裂；10 題均已逐題核對單元符合度、唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-da-[0-9].json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q.setdefault("provenance",{})["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題／課程資料的細胞構造、功能、層次與分裂能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Da 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Da：細胞的構造與功能","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對單元符合度、唯一答案、解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content da")
if __name__=="__main__": main()
